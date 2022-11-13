def corner_sheet_can_make(size, avaliable, do_print=False):
    makable = False
    amount_needed = 2 * (size ** 2) - size
    
    if avaliable >= amount_needed:
        makable = True
    
    if do_print:
        if makable:
            excess = avaliable - amount_needed
            print(f'''
You have {avaliable} Cubes

Corner sheet size: {size}
Cubes needed to make: {amount_needed} Cubes
Able to be made: Yes
You will have {'no' if excess == 0 else excess} Cube{'' if excess == 1 else 's'} spare.
''')
            return {"size": size, "cubes_avaliable": avaliable, "is_makable": makable, "cubes_needed": amount_needed, "excess_cubes": excess}
        if not makable:
            more_needed = abs(avaliable - amount_needed)
            print(f'''
You have {avaliable} Cubes

Corner sheet size: {size}
Cubes needed to make: {amount_needed} Cubes
Able to be made: No
You need {more_needed} more Cube{'' if more_needed == 1 else 's'} to be able to successfully make it.
''')
            return {"size": size, "cubes_avaliable": avaliable, "is_makable": makable, "cubes_needed": amount_needed, "additional_cubes_needed": more_needed}
    else:
        if makable:
            excess = avaliable - amount_needed
            return {"size": size, "cubes_avaliable": avaliable, "is_makable": makable, "cubes_needed": amount_needed, "excess_cubes": excess}
        if not makable:
            more_needed = abs(avaliable - amount_needed)
            return {"size": size, "cubes_avaliable": avaliable, "is_makable": makable, "cubes_needed": amount_needed, "additional_cubes_needed": more_needed}


if __name__ == "__main__":
    print("\n" * 100)
    amount_avaliable = int(input("How many cubes do you have?\n"))
    sheet_size = int(input("\nHow big is the corner sheet you are trying to make?\n"))
    print("\n" * 100)
    output = corner_sheet_can_make(sheet_size, amount_avaliable, True)

