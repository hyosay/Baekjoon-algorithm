student = ['One', 'sehi', 'Sang', 'son', 'kang']
A = 0
for i in student:
    student_point = int(input())
    if student_point < 40:
        student_point = 40
    A += student_point
    B = A // 5
print(B)


