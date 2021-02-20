from test_framework import generic_test
# Brute force method to calculate the parity in o(n) time complexity

def parity(x : int) -> int:
    """ Logic: Function that toggles a switch on for odd number
    of 1s and off for even number and returns the toogle state"""
    toggle = 0  # Initialise toggle state to 0
    while x:  # Run the loop till all bits are checked
        toggle ^= (x & 1)  # Turn toggle on for every 2nd 1
        x >>= 1   # Check the next bit in the bit string
    return toggle

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))

