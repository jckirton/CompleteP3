def gpa_calc(*grades: tuple | list | str, do_print: bool):
    """
    GPA calculater function that takes letter grade inputs and outputs a numerical and letter GPA.

    grades: The letter grades being calculated with. Accepts either multiple string objects (resulting in a tuple), a list of string objects, or a single string object.
    do_print: Whether or not to print the result as well as returning the dictionary, or to only return the dictionary.
    """
    letter_to_number = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
    number_to_letter = ["#", "E", "D", "C", "B", "A"]
    grades_sum = 0
    grades_amount = 0
    gpa = 0
    num_gpa = 0
    lett_gpa = ""
    if len(grades) == 1:
        grades = grades[0]
        input_type = type(grades)
    else:
        for grade in grades:
            grade = grade.upper()
            grade_num = letter_to_number[grade]
            grades_sum += grade_num
            grades_amount += 1

    if input_type == str:
        #        print(f"grades: {grades}")
        grades = grades.split(" ")
        #        print(f"grades: {grades}")
        for ind in grades:
            #            print(f"ind: {ind}")
            if len(ind) == 0 or ind == "":
                #                print(f"grades: {grades}")
                del grades[grades.index(ind)]
            #                print(f"grades: {grades}")
            else:
                pass
        #        print(f"grades: {grades}")
        for ind in grades:
            if ind != "" and ind != ",":
                #                print(f"ind: {ind}")
                spt = ind.split(",")
                #                print(f"spt: {spt}")
                for sptind in spt:
                    if sptind == "":
                        del spt[spt.index(sptind)]
                    else:
                        #                        print(f"sptind: {sptind}")
                        grades.append(sptind)
                #                        print(f"grades: {grades}")
                del grades[grades.index(ind)]
            #                print(f"grades: {grades}")
            elif ind == "" or ind == ",":
                del grades[grades.index(ind)]
        #                print(f"grades: {grades}")

        for ind in grades:
            #            print(f"ind: {ind}")
            if len(ind) > 1:
                for ch in ind:
                    #                    print(f"ch: {ch}")
                    #                    print(f"grades: {grades}")
                    grades.append(ch)
                #                    print(f"grades: {grades}")
                del grades[grades.index(ind)]
            #                print(f"grades: {grades}")
            else:
                pass
        for ind in grades:
            #            print(f"ind: {ind}")
            if len(ind) == 0 or ind == "" or ind == ",":
                #                print(f"grades: {grades}")
                del grades[grades.index(ind)]
            #                print(f"grades: {grades}")
            else:
                pass
        for ind in grades:
            #            print(f"ind: {ind}")
            if len(ind) > 1:
                for ch in ind:
                    #                    print(f"ch: {ch}")
                    #                    print(f"grades: {grades}")
                    grades.append(ch)
                #                    print(f"grades: {grades}")
                del grades[grades.index(ind)]
            #                print(f"grades: {grades}")
            else:
                pass
        for ind in grades:
            #            print(f"ind: {ind}")
            if len(ind) == 0 or ind == "" or ind == ",":
                #                print(f"grades: {grades}")
                del grades[grades.index(ind)]
            #                print(f"grades: {grades}")
            else:
                pass
        for grade in grades:
            grade = grade.upper()
            grade_num = letter_to_number[grade]
            grades_sum += grade_num
            grades_amount += 1
    elif input_type == list:
        for grade in grades:
            grade = grade.upper()
            grade_num = letter_to_number[grade]
            grades_sum += grade_num
            grades_amount += 1
    gpa = grades_sum / grades_amount
    num_gpa = round(gpa, 2)
    lett_gpa = number_to_letter[round(gpa)]
    if do_print:
        print(
            f"""GPA Calculation
Given Grades: {grades}

Numerical GPA: {num_gpa}
Letter GPA: {lett_gpa}
"""
        )
    return {
        "Inputted Grades": grades,
        "Actual GPA": gpa,
        "Rounded GPA": num_gpa,
        "Letter GPA": lett_gpa,
    }


if __name__ == "__main__":
    print("\n" * 100)
    grades = input("What are your letter grades?\n")
    print("\n" * 100)
    output = gpa_calc(grades, do_print=True)
