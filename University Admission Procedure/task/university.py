import os


def choice_num(subject):
    if subject == "Physics":
        return 1
    if subject == "Chemistry":
        return 2
    if subject == "Mathematics":
        return 3
    if subject == "Engineering":
        return 4
    if subject == "Biotech":
        return 5


N = int(input())
applicants = []
final_list = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
with open("applicants.txt", 'r') as data:
    for line in data:
        first_name, last_name, phy, chem, math, cse, ch1, ch2, ch3 = line.strip().split(" ")
        applicants.append([first_name + " " + last_name, float(int(phy) / 2 + int(math) / 2), int(chem), int(math), float(int(cse) / 2 + int(math) / 2), float(int(phy) / 2 + int(chem) / 2), ch1, ch2, ch3])
    first_priority = sorted(applicants, key=lambda x: (x[6], -x[choice_num(x[6])], x[0]))
    second_priority = sorted(applicants, key=lambda x: (x[7], -x[choice_num(x[7])], x[0]))
    third_priority = sorted(applicants, key=lambda x: (x[8], -x[choice_num(x[8])], x[0]))
    for applicant in first_priority:
        if len(final_list[applicant[6]]) < N:
            final_list[applicant[6]].append(applicant)
            second_priority.remove(applicant)
            third_priority.remove(applicant)
    for applicant in second_priority:
        if len(final_list[applicant[7]]) < N:
            final_list[applicant[7]].append(applicant)
            third_priority.remove(applicant)
    for applicant in third_priority:
        if len(final_list[applicant[8]]) < N:
            final_list[applicant[8]].append(applicant)
    cwd = os.getcwd()
    for k in final_list:
        os.chdir(cwd)
        with open(f"{k}.txt", "w") as out_file:
            final_list[k] = sorted(final_list[k], key=lambda x: (-x[choice_num(k)], x[0]))
            for v in range(len(final_list[k])):
                print(final_list[k][v][0], final_list[k][v][choice_num(k)], file=out_file)
