N = int(input())

applicants = []
final_list = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
with open("applicants.txt", 'r') as data:
    for line in data:
        first_name, last_name, gpa, ch1, ch2, ch3 = data.readline().strip().split(" ")
        applicants.append([first_name + " " + last_name, float(gpa), ch1, ch2, ch3])
    sorted_applicants = sorted(applicants, key=lambda x: (-x[1], x[0]))
    first_priority = sorted(applicants, key=lambda x: (x[2], -x[1], x[0]))
    second_priority = sorted(applicants, key=lambda x: (x[3], -x[1], x[0]))
    third_priority = sorted(applicants, key=lambda x: (x[4], -x[1], x[0]))
    for applicant in first_priority:
        if len(final_list[applicant[2]]) < 4:
            final_list[applicant[2]].append(applicant)
            second_priority.remove(applicant)
            third_priority.remove(applicant)
    for applicant in second_priority:
        if len(final_list[applicant[3]]) < 4:
            final_list[applicant[3]].append(applicant)
            second_priority.remove(applicant)
    for applicant in third_priority:
        if len(final_list[applicant[4]]) < 4:
            final_list[applicant[4]].append(applicant)
