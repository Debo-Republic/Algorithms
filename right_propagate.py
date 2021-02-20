#  A function to right propagate the the lowest set bit to all the bits
#  to the right of that bit

def right_propagate(x : int) -> int:
    """Logic : Isolating the lowest set bit and a decimal 1 less than value
     of that number will contain all the set bits to be superimposed on the
     original bit."""
    print(bin(x))
    print(bin((x & ~(x-1)) | (x-1) | x))
    return 0

right_propagate(736)