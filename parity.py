from test_framework import generic_test
# Brute force method to calculate the parity in o(n) time complexity

def parity(x: int) -> int:
    """ Logic: Function that counts total number of on bits(1)
     and returns the remainder when divided by 2"""
    num_1 = 0  # Initialize counter to 0
    while x:  # Run the loop until all bits are exhausted
        num_1 += (x & 1)  # Record if RSB Contains 1
        x >>= 1  # Right shift to check the next bit
    pair = num_1 % 2  # Find the parity
    return pair


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
