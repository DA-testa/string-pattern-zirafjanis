# python3

def read_input():
    # read the input type (keyboard or file)
    input_type = input().rstrip()

    if input_type == 'i':
        # read two lines from keyboard input
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'f':
        # read two lines from input file
        with open(input().rstrip()) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        # input type not recognized
        raise ValueError('Input type not recognized')

    # return both lines as a tuple
    return pattern, text

def print_occurrences(output):
    # print the occurrences in ascending order
    print(' '.join(map(str, sorted(output))))


def get_occurrences(pattern, text):
    # Rabin-Karp algorithm to find occurrences of pattern in text
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return occurrences

    # Calculate the hash value of pattern and first window of text
    p_hash = hash(pattern)
    t_hash = hash(text[0:p_len])
    if p_hash == t_hash and pattern == text[0:p_len]:
        occurrences.append(0)

    # Calculate the hash value of each subsequent window of text
    for i in range(1, t_len - p_len + 1):
        t_hash = hash(text[i:i+p_len])
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            occurrences.append(i)

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
