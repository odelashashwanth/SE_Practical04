
from a import get_result

print("Manual Testing of Result Program")
print("--------------------------------")

test_cases = [0, 39, 40, 50, 75, 100, -1, 101]

for marks in test_cases:
    result = get_result(marks)
    print("Marks:", marks, "Result:", result)

