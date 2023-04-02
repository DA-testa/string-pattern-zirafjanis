def read_input():
    # Choose the input type: keyboard or file
    input_type = input().rstrip().lower()
    if input_type == 'i':
        # Read input from keyboard
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        # Read input from file
        with open(input().rstrip()) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    # Print the occurrences in ascending order
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    n = len(text)
    m = len(pattern)
    p = 31  # A prime number used for hash calculation
    h_pattern = 0
    h_text = 0
    power_p = [1]
    matches = []
    # Precompute the powers of p
    for i in range(1, max(n, m)):
        power_p.append(power_p[-1] * p)
    # Calculate the hash value of the pattern and the initial substring of the text
    for i in range(m):
        h_pattern = h_pattern * p + ord(pattern[i])
        h_text = h_text * p + ord(text[i])
    # Compare the hash values of the pattern and the initial substring of the text
    for i in range(n - m + 1):
        if h_pattern == h_text:
            # Compare the characters of the pattern and the substring of the text
            if pattern == text[i:i+m]:
                matches.append(i)
        if i < n - m:
            # Calculate the hash value of the next substring of the text
            h_text = h_text - ord(text[i]) * power_p[m-1]
            h_text = h_text * p + ord(text[i+m])
    return matches

# Launch the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
