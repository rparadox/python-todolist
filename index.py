from os import system
from random import randint
from time import sleep
from collections import namedtuple

Todo = namedtuple("todo", ["code", "title", "time", "des", "status"])


todo_list = [
    Todo(code=1, title="task1", time="2025", des="", status="active"),
    Todo(code=2, title="task2", time="2025", des="", status="deactive"),
    Todo(code=3, title="task3", time="2025", des="", status="active"),
    Todo(code=4, title="task4", time="2026", des="", status="active"),
    Todo(code=5, title="task5", time="2027", des="", status="active"),
]


while True:
    # region show menu options
    print("---------------------------------------------------------")
    print("1. [A]dd todo")
    print("2. [D]isplay todo")
    print("3. [R]emove todo")
    # print("4. [E]dit todo")
    print("5. [S]earch todo")
    print("6. [Q]uit")
    print("---------------------------------------------------------")
    # endregion
    menu = input("Menu: ")
    system("cls")
    match menu:

        case "1" | "A":
            while True:
                # region continue
                ans = input("Do you want to add a todo (yes-etc): ")
                system("cls")

                if ans != "yes":
                    break
                # endregion

                # region add code
                while True:
                    code = randint(1, len(todo_list) + 1)  # 3
                    # region check duplicate code
                    dup = False
                    for todo in todo_list:
                        if todo.code == code:
                            dup = True
                            break
                    # endregion
                    if not dup:
                        break
                # endregion

                # region add title
                while True:
                    title = input("Please enter the title: ")
                    system("cls")

                    if title == "":
                        print("Title is empty! Please try again!")
                        continue

                    # region check duplicate title
                    dup = None

                    for todo in todo_list:
                        if todo.title == title:
                            dup = todo.title
                            break
                    # endregion

                    if dup == None:
                        break
                    print("Duplicate Title:", dup, "! Please try again.")
                # endregion

                # region add time
                while True:
                    time = input("Please enter the time: ")
                    system("cls")

                    if time == "":
                        print("Time is empty! Please try again!")
                        continue

                    elif time in [str(i) for i in range(2025, 2040)]:
                        break

                    print("Time is out of range! Please try again.")
                # endregion

                # region add des
                des = input("Please enter des: ")
                system("cls")
                # endregion

                # region add status
                while True:
                    status = input("Please enter the status: ")
                    system("cls")

                    if status == "":
                        print("Status is empty! Please try again!")
                        continue

                    elif status in ("active", "deactive"):
                        break

                    print("Status is not valid! Please try again.")
                # endregion

                # region display current todo
                print("-------------------------------------")
                print("Title:", title)
                print("Time:", time)
                print("des:", des)
                print("Status:", status)
                print("-------------------------------------")
                # endregion

                # region add todo
                if (
                    input("Are you sure you want to add the above todo (yes-etc): ")
                    != "yes"
                ):
                    continue

                todo = Todo(code, title, time, des, status)
                todo_list.append(todo)
                print("\nTodo Added to the Todo list")
                sleep(3)
                system("cls")
                # endregion

        case "2" | "D":
            while True:
                # region continue
                ans = input("Do you want to See a todo (yes-etc): ")
                system("cls")
                if ans != "yes":
                    break
                # endregion

                # region ask about columns
                if input("Do you want to See all columns (yes-etc)? ") == "yes":
                    display_col = ("code", "title", "time", "des", "status")
                else:
                    system("cls")
                    # region select columns
                    display_col = []
                    while True:
                        print("Selected Columns: ", *display_col)
                        # region get column
                        input_col = input(
                            "Select Columns: code title time des status\n OR quit\nSelect: "
                        )
                        if input_col not in (
                            "code",
                            "title",
                            "time",
                            "des",
                            "status",
                            "quit",
                        ):
                            print("Invalid input column! Please try again.")
                            continue

                        if input_col in display_col:
                            continue

                        if input_col == "quit":
                            system("cls")
                            break

                        display_col.append(input_col)
                        # endregion

                    # endregion
                # endregion

                if len(display_col):
                    # region display todos
                    print(
                        "==============================================================="
                    )
                    print("Row", *display_col, sep="\t")
                    print(
                        "---------------------------------------------------------------"
                    )
                    for row, todo in enumerate(todo_list, 1):
                        print(row, end="\t")
                        for col in display_col:
                            print(getattr(todo, col), end="\t")
                        print()
                    print(
                        "==============================================================="
                    )
                    # endregion
                    sleep(3)

        case "3" | "R":
            while True:
                # region continue
                ans = input("Do you want to Remove a todo (yes-etc): ")
                system("cls")

                if ans != "yes":
                    break
                # endregion

                display_col = ("code", "title", "time", "des", "status")

                # region select remove col
                while True:
                    # region display todos
                    print(
                        "==============================================================="
                    )
                    print("Row", *display_col, sep="\t")
                    print(
                        "---------------------------------------------------------------"
                    )
                    for row, todo in enumerate(todo_list, 1):
                        print(row, *todo, sep="\t")
                    print(
                        "==============================================================="
                    )
                    # endregion
                    remove_col = input(
                        "Select Columns to remove: code title time status\nSelect: "
                    )
                    system("cls")
                    if remove_col in ("code", "title", "time", "des", "status"):
                        break
                    print("Remove column is not Valid! Please try again.")

                # endregion

                # region match remove column

                # region get col
                while True:
                    # region display todos
                    print(
                        "==============================================================="
                    )
                    print("Row", *display_col, sep="\t")
                    print(
                        "---------------------------------------------------------------"
                    )
                    for row, todo in enumerate(todo_list, 1):
                        print(row, *todo, sep="\t")
                    print(
                        "==============================================================="
                    )
                    # endregion

                    val = input("Enter :")
                    system("cls")
                    if not val:
                        print("Empty Field!Please try again!")
                        continue

                    found = False
                    for todo in todo_list:
                        if (int(val) if remove_col == "code" else val) == getattr(todo, remove_col):
                            found = True
                            break

                    if found:
                        break

                    print(remove_col, "does not even exist. Please try again.")
                # endregion
                system("cls")
                found = False
                for todo in todo_list.copy():
                    if getattr(todo, remove_col) == (
                        int(val) if remove_col == "code" else val
                    ):
                        found = True
                        # region display current todo
                        print("-------------------------------------")
                        print("Title:", todo.title)
                        print("Time:", todo.time)
                        print("des:", todo.des)
                        print("Status:", todo.status)
                        print("-------------------------------------")
                        # endregion

                        remove_ans = input(
                            "Do you want to Remove the above todo (yes-etc)? "
                        )
                        system("cls")
                        if remove_ans == "yes":
                            todo_list.remove(todo)
                            system("cls")
                            print("Done.")

                if not found:
                    print("No record Found...")

        # case "4" | "E":
        #     while True:
        #         # region continue
        #         ans = input("Do you want to Edit a todo (yes-etc): ")
        #         system("cls")

        #         if ans != "yes":
        #             break
        #         # endregion

        #         display_col = ("Code", "Title", "Time", "Des", "Status")
        #         display_indexes = (0, 1, 2, 3, 4)

        #         # region select edit col
        #         while True:
        #             # region display todos
        #             print(
        #                 "==============================================================="
        #             )
        #             print("Row", *display_col, sep="\t")
        #             print(
        #                 "---------------------------------------------------------------"
        #             )
        #             for row, todo in enumerate(todo_list, 1):
        #                 print(row, *(todo[i] for i in display_indexes), sep="\t")
        #             print(
        #                 "==============================================================="
        #             )
        #             # endregion
        #             edit_col = input(
        #                 "Select Columns to edit: 1.[C]ode 2.[T]itle \nSelect: "
        #             )
        #             system("cls")
        #             if edit_col in ("1", "2", "C", "T"):
        #                 break
        #             print("Remove column is not Valid! Please try again.")

        #         # endregion

        #         # region match edit column
        #         match edit_col:
        #             case "1" | "C":
        #                 # region get code
        #                 while True:
        #                     # region display todos
        #                     print(
        #                         "==============================================================="
        #                     )
        #                     print("Row", *display_col, sep="\t")
        #                     print(
        #                         "---------------------------------------------------------------"
        #                     )
        #                     for row, todo in enumerate(todo_list, 1):
        #                         print(
        #                             row, *(todo[i] for i in display_indexes), sep="\t"
        #                         )
        #                     print(
        #                         "==============================================================="
        #                     )
        #                     # endregion

        #                     val = input("Code :")
        #                     system("cls")
        #                     if not val:
        #                         print("Empty Field!Please try again!")
        #                         continue

        #                     found = False
        #                     for todo in todo_list:
        #                         if int(val) == todo[0]:
        #                             found = True
        #                             break

        #                     if found:
        #                         break

        #                     print("Code does not even exist. Please try again.")
        #                 # endregion
        #                 search_index = 0

        #             case "2" | "T":
        #                 # region get title
        #                 while True:
        #                     # region display todos
        #                     print(
        #                         "==============================================================="
        #                     )
        #                     print("Row", *display_col, sep="\t")
        #                     print(
        #                         "---------------------------------------------------------------"
        #                     )
        #                     for row, todo in enumerate(todo_list, 1):
        #                         print(
        #                             row, *(todo[i] for i in display_indexes), sep="\t"
        #                         )
        #                     print(
        #                         "==============================================================="
        #                     )
        #                     # endregion
        #                     val = input("title: ")
        #                     system("cls")

        #                     if not val:
        #                         print("Title is empty! Please try again!")
        #                         continue
        #                     break
        #                 # endregion
        #                 search_index = 1
        #         # endregion
        #         system("cls")

        #         found = False
        #         for todo in todo_list.copy():
        #             if todo[search_index] == (int(val) if search_index == 0 else val):
        #                 found = True
        #                 # region display current todo
        #                 print("-------------------------------------")
        #                 print("Title:", todo[1])
        #                 print("Time:", todo[2])
        #                 print("des:", todo[3])
        #                 print("Status:", todo[4])
        #                 print("-------------------------------------")
        #                 # endregion

        #                 edit_ans = input(
        #                     "Do you want to Edit the above todo (yes-etc)? "
        #                 )
        #                 system("cls")
        #                 if edit_ans == "yes":
        #                     # region edit the current todo
        #                     while True:
        #                         edit_item = input("\nSelect item to Edit: 1.[T]itle 2.[Ti]me 3.[D]es 4.[S]tatus\nSelect: ")
        #                         system("cls")
        #                         if edit_item:
        #                             break
        #                         print("Edit item is empty! Please try again.")
        #                     # endregion
        #                     # region match edit items
        #                     match edit_item:

        #                         case "1" | "T":
        #                             # region get title
        #                             while True:
        #                                 new_title = input("New title: ")
        #                                 system("cls")

        #                                 if not new_title:
        #                                     print("New title is empty! Please try again.")
        #                                     continue

        #                                 if new_title == todo[1]:
        #                                     break

        #                                 for todo_ in todo_list:
        #                                     if todo_[1] == new_title:
        #                                         print(new_title, "already exists! Try another one.")
        #                                         break
        #                                 else:
        #                                     break

        #                             # endregion

        #                             todo[1] = new_title

        #                         case "2" | "Ti":
        #                             # region get time
        #                             while True:
        #                                 new_time = input("New time: ")
        #                                 system("cls")

        #                                 if not new_time:
        #                                     print("New time is empty! Please try again.")
        #                                     continue

        #                                 if new_time == todo[2]:
        #                                     break

        #                                 if new_time in tuple([str(i) for i in range(2025, 2040)]):
        #                                     break

        #                                 print("Time is not valid! Please try again.")

        #                             # endregion

        #                             todo[2] = new_time

        #                         case "3" | "D":
        #                             # region get des
        #                             new_des = input("New des: ")
        #                             system("cls")
        #                             # endregion

        #                             todo[3] = new_des

        #                         case "4" | "S":
        #                             # region get status
        #                             while True:
        #                                 new_status = input("New status: ")
        #                                 system("cls")

        #                                 if not new_status:
        #                                     print("New status is empty! Please try again.")
        #                                     continue

        #                                 if new_status == todo[4]:
        #                                     break

        #                                 if new_status in ("active", "deactive"):
        #                                     break

        #                                 print("Status is not valid! Please try again")

        #                             # endregion

        #                             todo[4] = new_status

        #                     # endregion
        #                     print("Done.")

        #         if not found:
        #             print("No record Found...")

        case "5" | "S":
            while True:
                # region continue
                ans = input("Do you want to Search a todo (yes-etc): ")
                system("cls")

                if ans != "yes":
                    break
                # endregion

                # region get search val
                while True:
                    value = input("Search Value: ")
                    system("cls")
                    if not value:
                        print("Value is empty! Please try again!")
                        continue
                    break
                # endregion

                found = False

                # region show todos
                display_col = ("code", "title", "time", "des", "status")
                print(
                    "5==============================================================="
                )
                print("Row", *display_col, sep="\t")
                print("---------------------------------------------------------------")
                for row, todo in enumerate(todo_list, 1):
                    if value in todo:
                        found = True
                        print(row, *todo, sep="\t")

                if not found:
                    print("This value doesn't exist!")
                print("===============================================================")
                # endregion

        case "6" | "Q":
            break

        case _:
            print("Invalid Menu option! Please try again.")
