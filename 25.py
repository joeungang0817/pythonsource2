names = input().split()
scores = input().split()
studentscore = [(names[0], int(scores[0])), (names[1], int(scores[1])),(names[2], int(scores[2])),(names[3], int(scores[3])),(names[4], int(scores[4]))]
print(dict(studentscore))