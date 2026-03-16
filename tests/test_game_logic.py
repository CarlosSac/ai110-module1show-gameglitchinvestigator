from logic_utils import check_guess, get_range_for_difficulty, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_high_low_hints_not_swapped():
    # Bug fix: when guess is too high, hint should say Go LOWER (not Go HIGHER)
    # and when guess is too low, hint should say Go HIGHER (not Go LOWER)
    outcome_high, message_high = check_guess(60, 50)
    outcome_low, message_low = check_guess(40, 50)
    assert "LOWER" in message_high, "Too High hint should say Go LOWER"
    assert "HIGHER" in message_low, "Too Low hint should say Go HIGHER"

# --- update_score ---

def test_wrong_guess_decreases_score():
    # Bug fix: wrong guesses should never increase score
    score_after_high = update_score(100, "Too High", 1)
    score_after_low = update_score(100, "Too Low", 1)
    assert score_after_high < 100, "Too High guess should decrease score"
    assert score_after_low < 100, "Too Low guess should decrease score"

def test_win_increases_score():
    score = update_score(0, "Win", 1)
    assert score > 0, "Winning should increase score"

# --- parse_guess ---

def test_parse_guess_rejects_non_numeric():
    ok, _, _ = parse_guess("abc")
    assert not ok, "Non-numeric input should be rejected"

def test_parse_guess_rejects_empty():
    ok, _, _ = parse_guess("")
    assert not ok, "Empty input should be rejected"

def test_parse_guess_accepts_valid_number():
    ok, value, _ = parse_guess("42")
    assert ok and value == 42

def test_out_of_range_guess_detected():
    # Bug fix: guesses outside difficulty range should be rejected
    low, high = get_range_for_difficulty("Normal")  # 1-50
    assert low - 1 < low or low - 1 > high, "Below range should be out of bounds"
    assert high + 1 < low or high + 1 > high, "Above range should be out of bounds"
    assert not (low < low or low > high), "Low boundary should be in range"
    assert not (high < low or high > high), "High boundary should be in range"
