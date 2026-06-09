dob = input("Enter DOB (DDMMYYYY): ")

# Sum all digits
total = 0
for digit in dob:
    total += int(digit)

# Reduce to a single digit
while total > 9:
    s = 0
    while total > 0:
        s += total % 10
        total //= 10
    total = s

print("Lucky Number =", total)
