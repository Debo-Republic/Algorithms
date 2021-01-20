# Sort a list of numerical array in ascending order
# Algorithm used = Insertion Sort

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a


old = [32, 2, 3, 1, 2, 5, 32, 11]
print(old)
new = insertionsort(old)
print(new)