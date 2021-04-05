def choice_num(subject):
    if subject == "Physics":
        return 1
    if subject == "Chemistry" or subject == "Biotech":
        return 2
    if subject == "Mathematics":
        return 3
    if subject == "Engineering":
        return 4


N = int(input())
applicants = []
final_list = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
with open("applicants.txt", 'r') as data:
    for line in data:
        first_name, last_name, phy, chem, math, cse, ch1, ch2, ch3 = line.strip().split(" ")
        applicants.append([first_name + " " + last_name, int(phy), int(chem), int(math), int(cse), ch1, ch2, ch3])
    first_priority = sorted(applicants, key=lambda x: (x[5], -x[choice_num(x[5])], x[0]))
    second_priority = sorted(applicants, key=lambda x: (x[6], -x[choice_num(x[6])], x[0]))
    third_priority = sorted(applicants, key=lambda x: (x[7], -x[choice_num(x[7])], x[0]))
    for applicant in first_priority:
        if len(final_list[applicant[5]]) < N:
            final_list[applicant[5]].append(applicant)
            second_priority.remove(applicant)
            third_priority.remove(applicant)
    for applicant in second_priority:
        if len(final_list[applicant[6]]) < N:
            final_list[applicant[6]].append(applicant)
            third_priority.remove(applicant)
    for applicant in third_priority:
        if len(final_list[applicant[7]]) < N:
            final_list[applicant[7]].append(applicant)
    for k in final_list:
        print(k, len(applicants))
        final_list[k] = sorted(final_list[k], key=lambda x: (-x[1], x[0]))
        for v in range(len(final_list[k])):
            print(final_list[k][v][0], final_list[k][v][1])
        print()
