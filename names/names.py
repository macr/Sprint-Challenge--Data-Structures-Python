import time


def bisect_left(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# O(n^2)
'''
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''
# Binary search tree: O(n log n)
bst = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# O(n), set uses hash table O(1) for read and write so our total time complexity is O(n)
# Space is O(n) too but with a bigger coefficient for the hash table.
names_2_set = set(names_2)
for name in names_1:
    if name in names_2_set:
        duplicates.append(name)
end_time = time.time()
print(
    f"Builtin set (Fastest): {len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# Space efficient stretch
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# O(n log n), builtin sort
names_1.sort()

# Similar to binary search: O(log n)


def is_duplicate(main_list, item):
    '''check if item in a given sorted list main_list
    O(log n ) similar to binary search
    '''
    idx = bisect_left(main_list, item)
    if idx < len(main_list) and main_list[idx] == item:
        return True
    return False


# total runtime: O(n log n)
duplicates = [n for n in names_2 if is_duplicate(names_1, n)]
end_time = time.time()
print(
    f"In-place sort bisect (least storage): {len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
