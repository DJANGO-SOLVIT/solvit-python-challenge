def average(mark):
    return (mark[0]+mark[1]+mark[2])/3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *rest = input().split()
        scores = list(map(float, rest))
        student_marks[name] = scores
    query_name = input()
print(f'{average(student_marks[query_name]):.2f}')