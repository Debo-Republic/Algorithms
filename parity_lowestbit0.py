from test_framework import generic_test
# Function to calculate the parity of an integer in o(k) times
# where k is the number of bits set to 1

def parity(x : int) -> int:
    """ Logic : A Function that counts the number of time the lowest set
     bit needs to be converted to 0 and returns its mod 2. """
    toggle = 0  # Initialise toggle state to 0
    while x:  # Run the loop for every one till all ones are exhausted
        toggle ^= 1  # Turn toggle on every iteration
        x &= (x-1)  # Set the lowest set bit to 0
    return toggle

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
