import streamlit as st
import random

st.set_page_config(page_title="Guess the Number", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you find it?")

# Initialize game state
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Function to reset the game
def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Game UI
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")

if st.button("Check Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1
    
    if guess < st.session_state.secret_number:
        st.warning("Too low! Try again. ⬆️")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try again. ⬇️")
    else:
        st.balloons() # Visual celebration!
        st.success(f"🏆 Congratulations! You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True

# Reset button
if st.session_state.game_over:
    if st.button("Play Again"):
        reset_game()
        st.rerun()

st.divider()
st.write(f"Attempts: {st.session_state.attempts}")