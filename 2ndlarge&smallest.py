# Using max() and min()
a = [12, 45, 2, 46, 31, 10, 8, 6, 4]

largest = max(a)
smallest = min(a)

a.remove(largest)
a.remove(smallest)

second_largest = max(a)
second_smallest = min(a)
print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)
