save_1 = ".chips"
save_2 = ".chips2"
save_3 = ".chips3"


def save_editor(save_1, save_2, save_3):
    editing = True
    chosen = False
    chosen_save = None

    import time
    import os

    while editing:
        try:
            with open(save_1, "r") as file:
                save1_value = str(int(float(file.read()))) + " Chips"
        except FileNotFoundError:
            save1_value = "No Save"
        except ValueError:
            save1_value = "Save Invalid"

        try:
            with open(save_2, "r") as file:
                save2_value = str(int(float(file.read()))) + " Chips"
        except FileNotFoundError:
            save2_value = "No Save"
        except ValueError:
            save2_value = "Save Invalid"

        try:
            with open(save_3, "r") as file:
                save3_value = str(int(float(file.read()))) + " Chips"
        except FileNotFoundError:
            save3_value = "No Save"
        except ValueError:
            save3_value = "Save Invalid"

        print("\n" * 100)
        save = input(
            f"Which save would you like to access?\n1: {save1_value}\n2: {save2_value}\n3: {save3_value}\nPress enter to exit.\n\n"
        )

        if save == "1":
            print("\n" * 100)
            op_or_del = input(
                f"Save 1: {save1_value}\n  - Open\n  - Delete\n  - Back\n\n"
            ).lower()
            if op_or_del in "back":
                pass
            elif op_or_del in "open":
                chosen_save = save_1
                chosen = True
                print("\n" * 100)
            elif op_or_del in "delete":
                print("\n" * 100)
                confirm = input("Are you sure?\n").lower()
                if confirm in "no":
                    pass
                elif confirm in "yes":
                    os.remove(save_1)
                    save1_value = "No Save"
        elif save == "2":
            print("\n" * 100)
            op_or_del = input(
                f"Save 2: {save2_value}\n  - Open\n  - Delete\n  - Back\n\n"
            ).lower()
            if op_or_del in "back":
                pass
            elif op_or_del in "open":
                chosen_save = save_2
                chosen = True
                print("\n" * 100)
            elif op_or_del in "delete":
                print("\n" * 100)
                confirm = input("Are you sure?\n").lower()
                if confirm in "no":
                    pass
                elif confirm in "yes":
                    os.remove(save_2)
                    save2_value = "No Save"
        elif save == "3":
            print("\n" * 100)
            op_or_del = input(
                f"Save 3: {save3_value}\n  - Open\n  - Delete\n  - Back\n\n"
            ).lower()
            if op_or_del in "back":
                pass
            elif op_or_del in "open":
                chosen_save = save_3
                chosen = True
                print("\n" * 100)
            elif op_or_del in "delete":
                print("\n" * 100)
                confirm = input("Are you sure?\n").lower()
                if confirm in "no":
                    pass
                elif confirm in "yes":
                    os.remove(save_3)
                    save3_value = "No Save"
        elif save == "":
            print("\n" * 100)
            print("See you next time!")
            chosen_save = "exit"
            chosen = False
            editing = False
            time.sleep(2)
            print("\n" * 100)
            break
        else:
            print("Please choose one of the three saves.")
            time.sleep(1.5)

        if chosen == True and chosen_save != "exit":
            if chosen_save == save_1:
                with open(chosen_save, "w") as file:
                    edit_to = input(
                        f"What would you like to change this file to?\nChosen save: Save 1\nCurrent contents: {save1_value}\n\n"
                    )

                    if edit_to in "back" or edit_to in "return":
                        pass
                    else:
                        file.write(str(edit_to))
                        print("\n" * 100)
                        print(f"Save 1 has been successfully changed to {edit_to}\n")
                        chosen = False
                        time.sleep(1.5)
                        print("\n" * 100)
            elif chosen_save == save_2:
                with open(chosen_save, "w") as file:
                    edit_to = input(
                        f"What would you like to change this file to?\nChosen save: Save 2\nCurrent contents: {save2_value}\n\n"
                    )

                    if edit_to in "back" or edit_to in "return":
                        pass
                    else:
                        file.write(str(edit_to))
                        print("\n" * 100)
                        print(f"Save 2 has been successfully changed to {edit_to}\n")
                        chosen = False
                        time.sleep(1.5)
                        print("\n" * 100)
            elif chosen_save == save_3:
                with open(chosen_save, "w") as file:
                    edit_to = input(
                        f"What would you like to change this file to?\nChosen save: Save 3\nCurrent contents: {save3_value}\n\n"
                    )

                    if edit_to in "back" or edit_to in "return":
                        pass
                    else:
                        file.write(str(edit_to))
                        print("\n" * 100)
                        print(f"Save 3 has been successfully changed to {edit_to}\n")
                        chosen = False
                        time.sleep(1.5)
                        print("\n" * 100)
        else:
            pass


if __name__ == "__main__":
    save_editor(save_1, save_2, save_3)
