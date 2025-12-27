import streamlit as st
import random
import time

# -----------------------------
# Game Logic Class
# -----------------------------
class RockPaperScissors:

    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        
        winner_combinations = [
            ('rock', 'scissors'),
            ('scissors', 'paper'),
            ('paper', 'rock')
        ]
        
        if (player_choice, computer_choice) in winner_combinations:
            return "player"
        
        return "computer"


# -----------------------------
# Streamlit UI Setup
# -----------------------------
st.set_page_config(page_title="Rock Paper Scissors", layout="centered")

# Theme Toggle
theme = st.toggle("🌗 Dark Mode")
if theme:
    st.markdown(
        """
        <style>
        body { background-color: #0e1117; color: block; }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("🎮 Rock – Paper – Scissors")
st.write("Play 10 rounds against the computer!")

# -----------------------------
# Session State Initialization
# -----------------------------
if "round" not in st.session_state:
    st.session_state.round = 1
if "player_wins" not in st.session_state:
    st.session_state.player_wins = 0
if "computer_wins" not in st.session_state:
    st.session_state.computer_wins = 0
if "ties" not in st.session_state:
    st.session_state.ties = 0

game = RockPaperScissors("Player")

# -----------------------------
# Scoreboard
# -----------------------------
st.sidebar.title("📊 Scoreboard")
st.sidebar.write(f"**Player Wins:** {st.session_state.player_wins}")
st.sidebar.write(f"**Computer Wins:** {st.session_state.computer_wins}")
st.sidebar.write(f"**Ties:** {st.session_state.ties}")
st.sidebar.write(f"**Round:** {st.session_state.round} / 10")

# -----------------------------
# Game UI
# -----------------------------
st.subheader(f"Round {st.session_state.round} of 10")

player_choice = st.radio("Choose your move:", game.choices, horizontal=True)

if st.button("Play Round"):
    # Animation: "Computer is choosing..."
    with st.spinner("Computer is thinking..."):
        time.sleep(1.2)

    computer_choice = game.computer_choice()

    # Animation: Reveal computer choice
    st.markdown(f"### 🤖 Computer chose: **{computer_choice}**")

    result = game.decide_winner(player_choice, computer_choice)

    # Animated result message
    if result == "player":
        st.success("🎉 You won this round!")
        st.session_state.player_wins += 1
    elif result == "computer":
        st.error("💥 Computer won this round!")
        st.session_state.computer_wins += 1
    else:
        st.info("🤝 This round is a tie.")
        st.session_state.ties += 1

    st.session_state.round += 1

# -----------------------------
# Final Results
# -----------------------------
if st.session_state.round > 10:
    st.subheader("🏁 Final Results")
    st.write(f"**Player wins:** {st.session_state.player_wins}")
    st.write(f"**Computer wins:** {st.session_state.computer_wins}")
    st.write(f"**Ties:** {st.session_state.ties}")

    # Celebration animation
    st.balloons()

    if st.button("Restart Game"):
        st.session_state.round = 1
        st.session_state.player_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.ties = 0
