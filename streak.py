def longest_positive_streak(numbers):
    """
    Calculates the length of the longest streak of positive numbers in a list.
    A streak is a contiguous sequence of positive numbers.
    Zeros and negative numbers break the streak.
    """
    max_streak = 0
    current_streak = 0
    for num in numbers:
        if num > 0:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 0
    max_streak = max(max_streak, current_streak)
    return max_streak