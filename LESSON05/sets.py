# Sets.
nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed.
nums = {1, 2, 2, 4}
print(nums)

# True is a dupe of 1, false is
# a dupe of 0
nums = {1, True, 2, False, 3,
        4, 0}
print(nums)

# Check if a value is in a set.
print(2 in nums)

# But you can't refer to an
# element in the set with an index
# position or a key..

# Add a new element to a set.
nums.add(8)
print(nums)

# Add elements from one set to
# another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with lists,
# tuples, dictionaries, too..

# Merge two sets to create a new
# set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates.
one = {1, 2, 3}
two = {2, 3, 6}

one.intersection_update(two)
print(one)

# Keep everything except
#  the duplicates.
one = {1, 2, 3}
two = {2, 3, 6}

one.symmetric_difference_update(two)
print(one)
