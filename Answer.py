n = int(input())
marks = {}
avg = 0
scores_sum = 0
for i in range(n):
    name, *mark = input().split()
    scores = list(map(float, mark))
    marks[name] = scores
   
query_name = input()
for i in marks[query_name]:
    scores_sum += i
    
avg = scores_sum/3
print("{:.2f}".format(avg))
    