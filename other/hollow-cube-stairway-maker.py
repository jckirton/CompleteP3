def cube_stairway_can_make(size, avaliable, do_print=False):
    makable = False
    amount_needed = 0
    counting_size = size
    
    while counting_size:
        corner_amount_needed = 2 * (counting_size ** 2) - counting_size
        amount_needed += corner_amount_needed
        # print(f"\n\nCurrent size being checked: {counting_size}\n")
        # print(f"Amount needed for corner: {corner_amount_needed}")
        # print(f"Current total amount needed: {amount_needed}")
        counting_size -= 1
    
    if avaliable >= amount_needed:
        makable = True
    
    if do_print:
        if makable:
            excess = avaliable - amount_needed
            print(f'''
You have {avaliable} Cubes

Hollow cube stairway size: {size}
Cubes needed to make: {amount_needed} Cubes
Able to be made: Yes
You will have {'no' if excess == 0 else excess} Cube{'' if excess == 1 else 's'} spare.
''')
            return {"size": size, "cubes_avaliable": avaliable, "is_makable": makable, "cubes_needed": amount_needed, "excess_cubes": excess}
        if not makable:
            more_needed = abs(avaliable - amount_needed)
            print(f'''
You have {avaliable} Cubes

Hollow cube stairway size: {size}
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


if __name__ == "__main__":6
    print("\n" * 100)
    amount_avaliable = int(input("\nHow many cubes do you have?\n"))
    stairway_size = int(input("How big is the hollow cube stairway you are trying to make?\n"))
    print("\n" * 100)
    output = cube_stairway_can_make(stairway_size, amount_avaliable, True)

