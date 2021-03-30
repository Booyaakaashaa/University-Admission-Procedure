N = int(input())
M = int(input())
applicants = []
for _ in range(N):
    first_name, last_name, gpa = input().split(" ")
    applicants.append([first_name + " " + last_name, float(gpa)])

print("Successful applicants:")
success_applicants = sorted(applicants, key=lambda x: (-x[1], x[0]))
for applicant in success_applicants:
    print(applicant[0])
