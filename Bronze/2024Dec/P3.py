import sys

def valid_pattern(substring):
    return len(substring) == 3 and substring[0] != substring[1] and substring[1] == substring[2]

def get_modified_substring(text_str, change_pos, replacement, start_pos, length):
    if start_pos < 0 or start_pos+2 >= length:
        return None
    return (text_str[start_pos:change_pos] + replacement + text_str[change_pos+1:start_pos+3]) if start_pos <= change_pos < start_pos+3 else text_str[start_pos:start_pos+3]

# Read input
raw_input = sys.stdin.read().strip().split()
length, threshold = int(raw_input[0]), int(raw_input[1])
text = raw_input[2]
#print(length,threshold,text)

# Get initial pattern counts
pattern_counts = {}
for pos in range(length-2):
    curr = text[pos:pos+3]
    if valid_pattern(curr):
        pattern_counts[curr] = pattern_counts.get(curr, 0) + 1

# Initialize result set
valid_patterns = set()
for pattern, freq in pattern_counts.items():
    if freq >= threshold:
        valid_patterns.add(pattern)

# Try all possible character changes
chars = "abcdefghijklmnopqrstuvwxyz"
for pos in range(length):
    curr_char = text[pos]
    for new_char in chars:
        if new_char == curr_char:
            continue

        # Track frequency changes
        freq_changes = {}
        impacted_pos = [pos-2, pos-1, pos]

        for start in impacted_pos:
            if start < 0 or start+2 >= length:
                continue

            before = text[start:start+3]
            after = get_modified_substring(text, pos, new_char, start, length)

            if valid_pattern(before):
                freq_changes[before] = freq_changes.get(before, 0) - 1

            if after and valid_pattern(after):
                freq_changes[after] = freq_changes.get(after, 0) + 1

        # Update valid patterns based on frequency changes
        for pattern in freq_changes:
            original_freq = pattern_counts.get(pattern, 0)
            updated_freq = original_freq + freq_changes[pattern]
            if updated_freq >= threshold:
                valid_patterns.add(pattern)

# Output results
answer = sorted(valid_patterns)
print(len(answer))
print("\n".join(answer))
