from test_framework import generic_test


def parity(x: int) -> int:
    """Function to count whether a given integer contains even number of 1's. """
    num_1 = 0
    while x:
        num_1 += (x & 1)
        x >>= 1
    pair = num_1 % 2
    return pair
   

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
