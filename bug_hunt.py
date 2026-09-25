count = 1
total = 0

# BUG: The while statement was missing a colon.
# BUG: < stops before 5, so it was changed to <= to include 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: A string cannot be joined directly with an integer, so str() was used.
print("Sum of 1 to 5 is: " + str(total))