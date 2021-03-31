N = int(input())

applicants = []
with open("applicants.txt", 'r') as data:
    for line in data:
        first_name, last_name, gpa, ch1, ch2, ch3 = data.readline().split(" ")
        applicants.append([first_name + " " + last_name, float(gpa), ch1, ch2, ch3])
    sorted_applicants = sorted(applicants, key=lambda x: (-x[1], x[0]))

