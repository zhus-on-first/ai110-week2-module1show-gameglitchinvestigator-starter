from logic_utils import check_guess, parse_guess, update_score


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# parse_guess tests
def test_parse_guess_rejects_float():
    ok, _, _ = parse_guess("3.9", 1, 100)
    assert not ok


def test_parse_guess_rejects_zero():
    ok, _, _ = parse_guess("0", 1, 100)
    assert not ok


def test_parse_guess_rejects_above_range():
    ok, _, _ = parse_guess("101", 1, 100)
    assert not ok


def test_parse_guess_rejects_empty():
    ok, _, _ = parse_guess("", 1, 100)
    assert not ok


def test_parse_guess_rejects_none():
    ok, _, _ = parse_guess(None, 1, 100)
    assert not ok


def test_parse_guess_accepts_valid():
    ok, value, _ = parse_guess("50", 1, 100)
    assert ok and value == 50


# check_guess hint direction tests
def test_check_guess_too_high_hint():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High" and "HIGHER" not in message


def test_check_guess_too_low_hint():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low" and "LOWER" not in message


# update_score tests
def test_update_score_win():
    score = update_score(0, "Win", 1)
    assert score > 0


def test_update_score_too_high_no_change():
    score = update_score(50, "Too High", 1)
    assert score == 50


def test_update_score_too_low_no_change():
    score = update_score(50, "Too Low", 1)
    assert score == 50
