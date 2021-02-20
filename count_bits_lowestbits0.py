from test_framework import generic_test


def count_bits(x: int) -> int:
    """Function to count the number of 1s by counting the number of times
     the lowest bit is set to 0"""
    num_1 = 0  # Set counter to 0
    while x:  # Run the loop for every 1 until all 1st are set to 0
        num_1 += 1  # Increment the counter for every iteration
        x &= (x-1)  # Set the lowest bit to 0
    return num_1  # return the number of 1s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
