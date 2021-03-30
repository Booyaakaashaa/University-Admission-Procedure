from hstest import *
from test.application_list import application_list as application_list

input_1 = ["1"]
input_2 = ["23"]
input_3 = ["10"]
input_4 = ["15"]


class TestAdmissionProcedure(StageTest):
    def generate(self):
        return [
            TestCase(stdin=input_1, attach=input_1, files={'applicants.txt': application_list}),
            TestCase(stdin=input_2, attach=input_2, files={'applicants.txt': application_list}),
            TestCase(stdin=input_3, attach=input_3, files={'applicants.txt': application_list}),
            TestCase(stdin=input_4, attach=input_4, files={'applicants.txt': application_list})
        ]

    @staticmethod
    def sort_by_priority(applicants, priority_n, departments_names, departments_lists, max_students):
        accepted_students = []
        for n, dep in enumerate(departments_names):
            dep_list = departments_lists[n]
            if len(dep_list) == max_students:
                continue
            students_needed = max_students - len(dep_list)
            dep_applicants = [applicant[:2]
                              for applicant in applicants if applicant[-1][priority_n] == dep]
            dep_applicants = sorted(dep_applicants, key=lambda x: (-x[1], x[0]))[:students_needed]
            departments_lists[n].extend(dep_applicants)
            accepted_students.extend([appl[0] for appl in dep_applicants])
        applicants = [applicant for applicant in applicants if applicant[0] not in accepted_students]
        return applicants, departments_lists

    @staticmethod
    def get_admission_lists(max_students):
        applicants = application_list.strip().split('\n')
        departments = sorted(['Mathematics', 'Physics', 'Biotech', 'Chemistry', 'Engineering'])
        applicants_data = []
        for line in applicants:
            line = line.split()
            line = [line[0] + ' ' + line[1]] + [float(line[2])] + [line[3:]]
            applicants_data.append(line)
        departments_lists = [[] for _ in departments]
        for i in range(len(applicants_data[-1][-1])):
            applicants_data, departments_lists = TestAdmissionProcedure.sort_by_priority(applicants_data,
                                                                                         i, departments,
                                                                                         departments_lists,
                                                                                         max_students)
        departments_lists = [[' '.join([str(el) for el in applicant])
                              for applicant in sorted(dep, key=lambda x: (-x[1], x[0]))]
                             for dep in departments_lists]
        return departments, departments_lists

    def check(self, reply: str, attach: list):
        n = int(attach[0])
        output = reply.strip().split('\n')
        output = [line for line in output if line]
        if not output:
            raise WrongAnswer("Your output seems to be empty.")
        department_names, admission_lists = self.get_admission_lists(n)
        correct_n_lines = len(department_names) + sum([len(dep_list) for dep_list in admission_lists])
        if len(output) != correct_n_lines:
            raise WrongAnswer("Your output is supposed to contain {0} lines with data (N={1}).\n"
                              "However, {2} lines with data are found.".format(correct_n_lines, n, len(output)))

        for i, department_name in enumerate(department_names):
            if department_name.lower() not in output[0].lower():
                raise WrongAnswer("The current line is supposed to contain the name of the department \"{0}\".\n"
                                  "However, this line contains the following data:\n"
                                  "\"{1}\"\n"
                                  "Make sure that you output the department names. \n"
                                  "Also, make sure that you output them "
                                  "in correct order.\n".format(department_name, output[0]))
            output = output[1:]
            correct_applicants = admission_lists[i]
            output_applicants, output = output[:len(correct_applicants)], output[len(correct_applicants):]
            for j, applicant in enumerate(correct_applicants):
                output_applicant = output_applicants[j]
                if applicant.lower().strip() not in output_applicant.lower():
                    raise WrongAnswer("Line {0} for the {1} department "
                                      "is supposed to contain the following applicant:\n"
                                      "\"{2}\"\n"
                                      "However, this line contains the following data:\n"
                                      "\"{3}\"\n"
                                      "Make sure the procedure of application is "
                                      "implemented correctly in your program.".format(j + 1,
                                                                                      department_name,
                                                                                      applicant,
                                                                                      output_applicant))

        return CheckResult.correct()


if __name__ == '__main__':
    TestAdmissionProcedure().run_tests()
