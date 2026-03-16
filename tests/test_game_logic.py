from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_high_low_hints_not_swapped():
    # Bug fix: when guess is too high, hint should say Go LOWER (not Go HIGHER)
    # and when guess is too low, hint should say Go HIGHER (not Go LOWER)
    outcome_high, message_high = check_guess(60, 50)
    outcome_low, message_low = check_guess(40, 50)
    assert "LOWER" in message_high, "Too High hint should say Go LOWER"
    assert "HIGHER" in message_low, "Too Low hint should say Go HIGHER"
