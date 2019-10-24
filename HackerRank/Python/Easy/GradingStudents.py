# Link: https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    gradesList = list(grades)

    for index, grade in enumerate(gradesList):
        higherMutiple = grade + (5- (grade%5))

        if abs(grade-higherMutiple) < 3 and grade>=38:
            gradesList[index] = higherMutiple

    return '\n'.join(map(str,gradesList))

print(gradingStudents([73, 67, 38, 33]))