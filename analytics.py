def passing_students(students):
    for student in students:
        if student.score >= 50:
            yield student


def make_grader(pass_mark):
    def grader(score):
        if score >= pass_mark:
            return "Pass"
        else:
            return "Fail"

    return grader


def class_average(students):
    if not students:
        return 0

    total = sum(student.score for student in students)
    return total / len(students)


def highest(students):
    if not students:
        return None

    return max(students, key=lambda student: student.score)


def lowest(students):
    if not students:
        return None

    return min(students, key=lambda student: student.score)


def pass_rate(students):
    if not students:
        return 0

    passed = sum(student.has_passed() for student in students)
    return (passed / len(students)) * 100


def first_three_scores(students):
    scores = iter(student.score for student in students)

    results = []

    for _ in range(3):
        try:
            results.append(next(scores))
        except StopIteration:
            break

    return results
