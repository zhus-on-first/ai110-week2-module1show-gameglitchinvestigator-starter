def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


# FIX: Collapsed None/empty checks into single guard; removed float truncation;
# added bounds validation — identified with Claude, implemented manually
def parse_guess(
    raw: str | None, min_val: int, max_val: int
) -> tuple[bool, int | None, str | None]:
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw:
        return False, None, "Enter a guess."

    try:
        value = int(raw)
        if value < min_val or value > max_val:
            return False, None, f"Guess must be between {min_val} and {max_val}"
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


# FIX: Removed dead TypeError fallback and even/odd attempt type-switching bug;
# both guess and secret are now always int — identified with Claude, fixed manually
def check_guess(guess: int | None, secret: int) -> tuple[str, str]:
    """
    Compare guess to secret and return (outcome, message).

    Outcome examples: "Win", "Too High", "Too Low"
    """
    if guess is None:
        return "Invalid", "Enter a valid number."

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


# FIX: Removed arbitrary score penalty for Too High/Too Low — wrong guesses
# no longer affect score — identified with Claude, fixed manually
def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    return current_score
