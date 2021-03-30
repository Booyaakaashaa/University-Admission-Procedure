N = int(input())
M = int(input())
applicants = []
for _ in range(N):
    first_name, last_name, gpa = input().split(" ")
    applicants.append([first_name, last_name, float(gpa)])

print()
