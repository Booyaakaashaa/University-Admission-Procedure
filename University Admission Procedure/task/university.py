N = int(input())

applicants = []
final_list = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
with open("applicants.txt", 'r') as data:
    for line in data:
        first_name, last_name, gpa, ch1, ch2, ch3 = data.readline().strip().split(" ")
        applicants.append([first_name + " " + last_name, float(gpa), ch1, ch2, ch3])
    sorted_applicants = sorted(applicants, key=lambda x: (x[2], -x[1], x[3], x[4], x[0]))
    for
