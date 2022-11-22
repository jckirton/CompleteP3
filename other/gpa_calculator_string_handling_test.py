grades = "abb, c a,b,,d  d, ab, d"

print(f"grades: {grades}")
grades = grades.split(" ")
print(f"grades: {grades}")
for ind in grades:
    print(f"ind: {ind}")
    if len(ind) == 0 or ind == '':
        print(f"grades: {grades}")
        del grades[grades.index(ind)]
        print(f"grades: {grades}")
    else:
        pass
print(f"grades: {grades}")
for ind in grades:
    if ind != "" and ind != ",":
        print(f"ind: {ind}")
        spt = ind.split(",")
        print(f"spt: {spt}")
        for sptind in spt:
            if sptind == "":
                del spt[spt.index(sptind)]
            else:
                print(f"sptind: {sptind}")
                grades.append(sptind)
                print(f"grades: {grades}")
        del grades[grades.index(ind)]
        print(f"grades: {grades}")
    elif ind == "" or ind == ",":
        del grades[grades.index(ind)]
        print(f"grades: {grades}")

for ind in grades:
    print(f"ind: {ind}")
    if len(ind) > 1:
        for ch in ind:
            print(f"ch: {ch}")
            print(f"grades: {grades}")
            grades.append(ch)
            print(f"grades: {grades}")
        del grades[grades.index(ind)]
        print(f"grades: {grades}")
    else:
        pass
for ind in grades:
    print(f"ind: {ind}")
    if len(ind) == 0 or ind == '' or ind == ",":
        print(f"grades: {grades}")
        del grades[grades.index(ind)]
        print(f"grades: {grades}")
    else:
        pass
for ind in grades:
    print(f"ind: {ind}")
    if len(ind) > 1:
        for ch in ind:
            print(f"ch: {ch}")
            print(f"grades: {grades}")
            grades.append(ch)
            print(f"grades: {grades}")
        del grades[grades.index(ind)]
        print(f"grades: {grades}")
    else:
        pass
for ind in grades:
    print(f"ind: {ind}")
    if len(ind) == 0 or ind == '' or ind == ",":
        print(f"grades: {grades}")
        del grades[grades.index(ind)]
        print(f"grades: {grades}")
    else:
        pass
print(f"grades: {grades}")
