import time
from bst import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# -----------------------------------------------------------------------
tree = BinarySearchTree(names_1[0])  # 0.1278 seconds O(n log n) runtime
for name in names_1:
    tree.insert(name)
for name in names_2:
    if tree.contains(name):
        duplicates.append(name)
# ------------------------------------------------------------------------
# Replace the nested for loops below with your improvements
# for name_1 in names_1:  # default project runtime is 9.1071 seconds which I need to improve
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
# ------------------------------------------------------------------------
# set_1 = set(names_1)  # 0.0069 seconds constant runtime
# set_2 = set(names_2)
# duplicates = set_1.intersection(set_2)
# ------------------------------------------------------------------------
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
