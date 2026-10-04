from logic_utils import check_guess, get_range_for_difficulty
from streamlit.testing.v1 import AppTest


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_hint():
    # BUG FIX 2: If secret is 50 and guess is 60, hint should be "Too High" and say "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low_hint():
    # BUG FIX 2: If secret is 50 and guess is 40, hint should be "Too Low" and say "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_difficulty_ranges():
    # BUG FIX 3: Hard should be 1-100, Normal should be 1-50
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_new_game_clears_state():
    # BUG FIX 1: New Game should fully reset session state
    at = AppTest.from_file("app.py").run()
    # Simulate playing: submit a guess
    at.text_input(key="guess_input_Normal").input("50").run()
    at.button[0].click().run()  # Submit Guess 🚀

    # Assert session state has changed
    assert at.session_state.attempts > 0
    assert len(at.session_state.history) > 0

    # Click New Game 🔁
    at.button[1].click().run()

    # Assert session state is cleared and restarted
    assert at.session_state.attempts == 1
    assert len(at.session_state.history) == 0
