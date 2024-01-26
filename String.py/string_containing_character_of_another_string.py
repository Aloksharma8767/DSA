def min_window(s, p):
    if not s or not p:
        return "-1"

    target_counts = {}
    window_counts = {}
    required_chars = len(set(p))
    formed_chars = 0
    left = right = 0
    min_len = float('inf')
    min_window_str = ""

    for char in p:
        target_counts[char] = target_counts.get(char, 0) + 1

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed_chars += 1

        while formed_chars == required_chars:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_str = s[left:right + 1]

            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                formed_chars -= 1

            left += 1

        right += 1

    return min_window_str if min_len != float('inf') else "-1"

# Example usage:
S = "ADOBECODEBANC"
P = "ABC"
result = min_window(S, P)
print(result)




