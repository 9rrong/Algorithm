import bisect

p = int(input())

for _ in range(p):
    parts = list(map(int, input().split()))
    num = parts[0]
    students = parts[1:]
    lined_students = []
    res = 0

    for student in students:
        pos = bisect.bisect_right(lined_students, student)
        lined_students.insert(pos, student)

        res += len(lined_students) - pos - 1
    print(num, res)
