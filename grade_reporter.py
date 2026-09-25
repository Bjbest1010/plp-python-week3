scores = [72, 45, 90, 61, 38]

passed = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print("Score:", score, "- Grade:", grade)

    if score >= 50:
        passed += 1

    total += score

print("Passed:", passed)
print("Failed:", len(scores) - passed)
print("Average:", round(total / len(scores), 1))