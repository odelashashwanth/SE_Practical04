
def get_result(marks):
    if marks < 0 or marks > 100:
        return "Invalid"
    elif marks < 40:
        return "fail"
    else:
        return "pass"

