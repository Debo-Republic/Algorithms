from test_framework import generic_test


def count_bits(x: int) -> int:
    """Function to count the number of 1's in a bit string. """
    num_1 = 0
    while x :
        num_1 += x & 1
        x >>= 1
    return num_1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
