#start of the system
def main_menu():
    while True:
        print("\n ====== Welcome to the University Management System ====== ")
        print("\n1. Administrator\n2. Lecturer\n3. Student Management\n4. Registrar\n5. Accountant\n6. Exit")
        try:
            user_input = int(input("\nWhat is your role?\n => "))
            if user_input == 1:
                administrator_login()
            elif user_input == 2:
                lecturer_login()
            elif user_input == 3:
                student_management_login()
            elif user_input == 4:
                registrar_login()
            elif user_input == 5:
                accountant_login()
            elif user_input == 6:
                print("Exiting the system. Goodbye!")
                exit()
            else:
                print("Invalid option. Please select a valid role.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#login function for all roles
def login(role_code, calling_menu):
    attempts = 3
    while attempts > 0:
        try:
            print("==========================================================")
            access_code_input = int(input(f"You need to enter the access code to your role:\n => "))
            if access_code_input == role_code:
                calling_menu()
                return
            else:
                attempts -= 1
                print(f"Incorrect code. You have {attempts} attempt(s) left.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("Access denied, kicking you from the system.")
    exit()

#all login credentials for each role
def administrator_login():
    login(54321, administrator_menu)

def lecturer_login():
    login(11011, lecturer_id_login)

def student_management_login():
    login(30003, student_management_menu)

def registrar_login():
    login(77777, registrar_menu)

def accountant_login():
    login(12345, accountant_menu)

#after user finish using one of the role's function, they are given the choice to continue or exit the system
def continue_back_exit():
    print("\n============ What would you like to do next? =============")
    while True:
        try:
            choice = int(input("1. Continue\n2. Exit\n => "))
            if choice == 1:
                break
            elif choice == 2:
                print("Exiting the system. Goodbye!")
                exit()
            else:
                print("Please enter a number from the given menu")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Menu for all roles
def administrator_menu():
    while True:
        print("==========================================================")
        print("\n{Administrator Menu}")
        print("1. Add New Course\n2. Remove Courses\n3. Remove Student\n4. Manage Lecturers\n5. Generate Reports\n6. View All Data\n7. Back to Main Menu")
        try:
            menu_choice = int(input("\nWhich Function are you looking for?\n => "))
            if menu_choice in range(1, 8):
                if menu_choice == 7:
                    main_menu()
                    break # Exit loop when 7 is chosen
                else:
                    admin_choices(menu_choice)
            else:
                print("Please enter a number from the given menu")
        except ValueError:
            print("Invalid input. Please enter a number.")

def admin_choices(menu_choice):
    courses = []
    courses_list = []
    students_list= []
    print("==========================================================")
    if menu_choice == 1:
        add_course(courses)
    elif menu_choice == 2:
        remove_courses(courses_list)
    elif menu_choice == 3:
        remove_students(students_list)
    elif menu_choice == 4:
        manage_lecturers_menu()
    elif menu_choice == 5:
        generate_reports()
    elif menu_choice == 6:
        view_all_data_menu()
    else:
        print("Please enter a number from the given menu")
        print("==========================================================")
    continue_back_exit() #continue back exit is in every menu choice instead of def

#Submenu for manage lecturers function
def manage_lecturers_menu():
    while True:
        print("================= Manage Lecturers Menu ==================")
        print("1. Add Lecturer \n2. Update Lecturer Information \n3. Remove Lecturer \n4. Back to Administrator Menu")
        print("\n==========================================================")
        try:
            menu_choice = int(input("Which Function are you looking for?\n => "))
            if menu_choice in range(1, 5):
                if menu_choice == 4:
                    administrator_menu()  # Exit the loop but back to Admin Menu because it is a sub menu
                    break
                else:
                    lecturer_menu_choices(menu_choice)
            else:
                print("Please enter a number from the given menu")
        except ValueError:
            print("Invalid input. Please enter a number.")


def lecturer_menu_choices(menu_choice):
    lecturers = []
    lecturers_list = []
    if menu_choice == 1:
        add_lecturers(lecturers)
    elif menu_choice == 2:
        update_lecturers(lecturers_list)
    elif menu_choice == 3:
        remove_lecturers(lecturers_list)
    else:
        print("Please enter a number from the given menu")
    continue_back_exit() #continue back exit is in every menu choice instead of def

#Submenu for viewing all data function
def view_all_data_menu():
    while True:
        print("\nView all data Menu")
        print("1. View Courses \n2. View Lecturers \n3. View Students \n4. Back to Administrator Menu")
        try:
            menu_choice = int(input("\nWhich Function are you looking for?\n => "))
            if menu_choice in range(1, 5):
                if menu_choice == 4:
                    administrator_menu() # Exit the loop but back to Admin Menu because it is a sub menu
                    break
                else:
                    view_all_data_choices(menu_choice)
            else:
                print("Please enter a number from the given menu")
        except ValueError:
            print("Invalid input. Please enter a number.")

def view_all_data_choices(menu_choice):
    if menu_choice == 1:
        courses_list = []
        print("\n======== Viewing All Courses ========\n")
        file_loaded = load_courses(courses_list)  # load courses from the file to the list
        if not file_loaded:
            return
        display_courses(courses_list)
    elif menu_choice == 2:
        lecturers_list = []
        print("\n======== Viewing All Lecturers ========\n")
        file_loaded = load_lecturers(lecturers_list)  # load lecturers from the file to the list
        if not file_loaded:
            return
        display_lecturers(lecturers_list)
    elif menu_choice == 3:
        students_list = []
        print("\n======== Viewing All Students ========\n")
        file_loaded = load_students(students_list)  # load students from the file to the list
        if not file_loaded:
            return
        display_students(students_list)
    else:
        print("Please enter a number from the given menu")
    continue_back_exit() #continue back exit is in every menu choice instead of def

##################################################################################################
def lecturer_menu(lecturer_id, lecturer_name, course_codes):
    while True:
        print("==========================================================")
        print("\n{Lecturer Menu}")
        print("1. View Assigned Modules\n2. Record Grades\n3. View Student List\n4. Track Attendance\n5. View Student Grades\n6. Back to Main Menu")
        try:
            menu_choice = int(input("\nWhich Function are you looking for?\n => "))
            if menu_choice in range(1, 7):
                if menu_choice == 6:
                    main_menu()  # To exit the loop and return to the main menu
                    break
                else:
                    lecturer_choices(menu_choice, lecturer_id, lecturer_name, course_codes)
            else:
                print("Please enter a number from the given menu")
        except ValueError:
            print("Invalid input. Please enter a number.")

def lecturer_choices(menu_choice, lecturer_id, lecturer_name, course_codes):
    print("==========================================================")
    if menu_choice == 1:
        print("[View assigned menu]\n")
        view_assigned_menu(lecturer_name, course_codes)
    elif menu_choice == 2:
        print("[Record Grades]\n")
        selected_module = choose_module(course_codes)
        if selected_module:
            print('')
            # ensure student selected is valid
            selected_student = choose_student()
            if selected_student:
                record_grades(selected_module, selected_student)
    elif menu_choice == 3:
        print("[View Student List]\n")
        view_student_list(lecturer_id)
    elif menu_choice == 4:
        print("[Track Attendance]\n")
        selected_module = choose_module(course_codes)
        if selected_module:
            print('')
            # ensure student selected is valid
            selected_student = choose_student()
            if selected_student:
                mark_attendance(selected_module, selected_student)
    elif menu_choice == 5:
        print("[View Student Grades]\n")
        selected_module = choose_module(course_codes)
        if selected_module:
            print('')
            view_student_grades(lecturer_id, selected_module)
    else:
        print("Please enter a number from the given menu")
    print("==========================================================")
    continue_back_exit() #continue back exit is in every menu choice instead of def

################################################################################################################
def student_management_menu():
    while True:
        print("==========================================================")
        print("\n{Student Management Menu}")
        print("1. View Available Modules\n2. Enroll Student\n3. Un-Enroll Student\n4. View Grades\n5. Access Attendance Record\n6. Back to Main Menu")
        try:
            menu_choice = int(input("\nWhich Function are you looking for?\n => "))
            if menu_choice in range(1, 7):
                if menu_choice == 6:
                    main_menu()
                    break  # # Exit loop when 6 is chosen
                else:
                    student_manage_choices(menu_choice)
            else:
                print("Please enter a number from the given menu")
        except ValueError:
            print("Invalid input. Please enter a number.")

def student_manage_choices(menu_choice):
    if menu_choice == 1:
        available_module()
    elif menu_choice == 2:
        enroll_student()
    elif menu_choice == 3:
        un_enroll_student()
    elif menu_choice == 4:
        view_grades()
    elif menu_choice == 5:
        view_attendance()
    else:
        print("Please enter a number from the given menu")
    continue_back_exit() #continue back exit is in every menu choice instead of def

###################################################################################################################
def registrar_menu():
    while True:
        print("==========================================================")
        print("\n{Registrar Menu}")
        print("1. Register New Students\n2. Update Student Records\n3. Manage Enrollments\n4. Issue Transcripts\n5. View Student Information\n6. Back to Main Menu")
        try:
            menu_choice = int(input("\nWhich Function are you looking for?\n => "))
            print("==========================================================")
            if menu_choice in range(1, 7):
                if menu_choice == 6:
                    main_menu()
                    break # Exit loop when 6 is chosen
                else:
                    registrar_choices(menu_choice)
            else:
                print("Please enter a number from the given menu")
        except ValueError:
            print("Invalid input. Please enter a number.")

def registrar_choices(menu_choice):
    students = []
    students_list = []
    if menu_choice == 1:
        register_new_students(students)
    elif menu_choice == 2:
        update_students(students_list)
    elif menu_choice == 3:
        manage_enrollments()
    elif menu_choice == 4:
        issue_transcripts()
    elif menu_choice == 5:
        student_information()
    else:
        print("Please enter a number from the given menu")
    continue_back_exit() #continue back exit is in every menu choice instead of def

####################################################################################################################
def accountant_menu():
    while True:
        print("==========================================================")
        print("\n{Accountant Menu}")
        print("1. Record Tuition Fee\n2. Update Payment Record\n3. View Outstanding Fee\n4. Issue Fee Receipts\n5. View Financial Summary\n6. Back to Main Menu")
        try:
            menu_choice = int(input("\nWhich Function are you looking for?\n => "))
            if menu_choice in range(1, 7):
                if menu_choice == 6:
                    main_menu()
                    break  # Exit loop when 6 is chosen
                else:
                    accountant_choices(menu_choice)
            else:
                print("Please enter a number from the given menu")
        except ValueError:
            print("Invalid input. Please enter a number.")

def accountant_choices(menu_choice):
    if menu_choice == 1:
        record_or_add_tuition()
    elif menu_choice == 2:
        payment_records()
    elif menu_choice == 3:
        outstanding_fee()
    elif menu_choice == 4:
        fee_receipts()
    elif menu_choice == 5:
        financial_summary()
    else:
        print("Please enter a number from the given menu")
    continue_back_exit() #continue back exit is in every menu choice instead of def

############################################################################################################
#All Admin functions
def count_lines_with_values(file_path):  #to count lines for generating reports
    with open(file_path, "r") as file:
        return sum(1 for line in file if line.strip())

def cancel_command(input_value):  #cancel function if 'cancel' is entered
    if input_value.strip().upper() == "CANCEL":
        return True
    return False

def null_input(input_value): #to make sure input is not nothing
    if input_value == "":
        print("Input cannot be null, Please enter a valid input!")
        return True
    return False

def add_course_code(courses):
    while True:  #to loop until the correct input is entered
        new_course_code = input("Please enter the new course code:\n => ").strip().upper()
        if null_input(new_course_code):
            continue
        elif cancel_command(new_course_code):
            return None
        #validating course code so it's not duplicated
        for course in courses:
            if course[0] == new_course_code:
                print(f"Invalid input! ({new_course_code} already exists).")
                break
        else:
            try:
                with open("courses.txt", "r") as course_files:
                    for course in course_files:
                        course_code_from_file = course.split(",")[0].strip()
                        if course_code_from_file == new_course_code:
                            print(f"Invalid input! ({new_course_code} already exists).")
                            break
                    else:
                        return new_course_code  #return the validated code
            except FileNotFoundError: #since the file is not exit
                return new_course_code  #the code will create new file so we can still return the validated code

def add_course_name():
    while True: #to loop until the correct input is entered
        new_course_name = input("Please enter the name of the new course:\n => ").strip().upper()
        if null_input(new_course_name):
            continue
        elif cancel_command(new_course_name):
            return None
        elif any(char.isnumeric() for char in new_course_name): #to make sure input is alphabetic
            print("Course name must be alphabetic. Please try again!")
            continue
        else:
            return new_course_name  #to input the valid answer

def add_course_credits():
    while True: #to loop until the correct input is entered
        new_course_credits = input("Please enter the new courses credits:\n => ").strip()
        if null_input(new_course_credits):
            continue
        elif cancel_command(new_course_credits):
            return None
        elif new_course_credits.isnumeric(): #to make sure input is numeric
            return new_course_credits #to input the valid answer
        else:
            print("Credits must be numeric. Please try again!")


def add_course(courses):
    print("(If you want to cancel, type 'cancel' at any step to stop adding the course.)")
    new_course_code = add_course_code(courses)
    if new_course_code is None:
        return
    new_course_name = add_course_name()
    if new_course_name is None:
        return
    new_course_credits = add_course_credits()
    if new_course_credits is None:
        return
    courses.append([new_course_code, new_course_name, new_course_credits])
    print(f"Course {new_course_name} added successfully.")
    with open("courses.txt", "a") as file:  #if file does not exist then it will create it
        file.write(f"{new_course_code},{new_course_name},{new_course_credits}\n")

def load_courses(courses_list):  #to load lecturers file into list
    try:
        with open("courses.txt", "r") as file:
            for line in file:
                course_code, course_name, course_credits = line.strip().split(",")
                courses_list.append([course_code, course_name, course_credits])
        return True  #file loaded successfully
    except FileNotFoundError:
        print("Courses file is not found in the system.")
        return False  #file not found

def display_courses(courses_list):  #to display the list of the courses
    if not courses_list:
        print("\nNo courses available")
        return False
    print("Below is the list of the courses:\n")
    for index, course in enumerate(courses_list):
        #to print the course details
        print(f"{index + 1}. Course Code: {course[0]} \n   Course Name: {course[1]} \n   Credits: {course[2]}")
        print("==========================================================")
    return True

def save_courses(courses_list):  #to save the updated courses list back to the file
    with open("courses.txt", "w") as file:
        for course in courses_list:
            file.write(",".join(course) + "\n")

def remove_courses(courses_list):
    file_loaded = load_courses(courses_list)  #load courses from the file to the list
    if not file_loaded:
        return  #to exit if the file is not found
    if not display_courses(courses_list):  #if the list is empty then exit
        return
    while True: #to loop until the correct input is entered
        try:
            courses_input = int(input("Enter the number of the course you want to remove:\n => ")) - 1
            if courses_input < 0 or courses_input >= len(courses_list):
                print("Invalid input, please try again!")
                continue  #to asking for the valid input
            selected_course = courses_list[courses_input]
            print(f"Selected Course: {selected_course[0]}")
            while True:
                confirm = input(f"Are you sure you want to remove {selected_course[0]}? (Y/N):\n => ").strip().upper()
                if confirm == 'Y':
                    courses_list.pop(courses_input)
                    print(f"Course {selected_course[0]} removed successfully.")
                    save_courses(courses_list)  # to save the updated list back to the file
                    return  #to exit after the removal is successful
                elif confirm == 'N':
                    print("Removal canceled.")
                    return  #to exit if user cancels
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Manage Lecturer Function
def add_lecturers_id(lecturers):
    while True: #to loop until the correct input is entered
        lecturers_id = input("Please enter the lecturer's ID:\n => ").strip().upper()
        if null_input(lecturers_id):
            continue
        elif cancel_command(lecturers_id):
            return None
        #to validating the lecturer id so it's not duplicated
        for lecturer in lecturers:
            if lecturer[0] == lecturers_id:
                print(f"Invalid input! ({lecturers_id} already exists).")
                break
        else:
            try:
                with open("lecturers.txt", "r") as lecturers_files:
                    for lecturer in lecturers_files:
                        lecturer_id_from_file = lecturer.split(",")[0].strip()
                        if lecturer_id_from_file == lecturers_id:
                            print(f"Invalid input! ({lecturers_id} already exists).")
                            break
                    else:
                        return lecturers_id  #return the validated code
            except FileNotFoundError:
                return None

def add_lecturers_name():
    while True:  #to loop until the correct input is entered
        lecturers_name = input("Please enter the lecturer's name:\n => ").strip().upper()
        if null_input(lecturers_name):
            continue
        elif cancel_command(lecturers_name):
            return None
        elif any(char.isnumeric() for char in lecturers_name):
            print("Lecturer name must be alphabetic. Please try again!")
            continue #to make sure the input is alphabetic
        else:
            return lecturers_name #to return the valid lecturer name

def add_lecturers_phone_number():
    while True: #to loop until the correct input is entered
        lecturers_phone_number = input("Please enter the lecturer's phone number (60XXXXXXXXX):\n => ").strip()
        if null_input(lecturers_phone_number):
            continue
        elif cancel_command(lecturers_phone_number):
            return None
        elif lecturers_phone_number.isnumeric(): #to make sure input is numeric
            return lecturers_phone_number #to return the valid lecturer phone number
        else:
            print("Lecturer's phone number must be numeric. Please try again!")

def add_lecturers_email():
    while True:
        lecturers_email = input("Please enter the lecturer's email (XXX@gmail.com): \n => ").strip().upper()
        if null_input(lecturers_email):
            continue
        elif cancel_command(lecturers_email):
            return None
        else:
            return lecturers_email #to return the valid lecturer email

def add_lectures_course_code():
    while True:  #to loop until the correct input is entered
        print("\nPlease make sure to separate multiple course codes with '|'")
        print("For example: CS001|IT002|IN003")
        print("Enter 'cancel' if you want to cancel the process.\n")
        lecturers_course_code = input("Please enter the lecturer's course code:\n => ").strip().upper()
        if null_input(lecturers_course_code):
            continue
        elif cancel_command(lecturers_course_code):
            return None
        try:
            validated_course_codes = []
            with open("courses.txt", "r") as courses_file:
                for line in courses_file:
                    parts = line.strip().split(",")
                    if parts:
                        validated_course_codes.append(parts[0].upper())
            # to separate inputted course code and to make sure the course code is valid and already exist
            entered_course_codes = lecturers_course_code.split("|")
            invalid_course_codes = [code for code in entered_course_codes if code not in validated_course_codes]
            if invalid_course_codes:
                print(f"The following course codes are invalid or do not exist: {', '.join(invalid_course_codes)}")
                continue
            validated_lecturers_cc = []
            with open("lecturers.txt", "r") as lecturers_file:
                for line in lecturers_file:
                    parts = line.strip().split(",")
                    if len(parts) > 4:  #to make sure there are at least 5 elements in the parts
                        #to separate the inputted course code and to make sure the code is not assigned to another lecturer
                        lecturer_course_codes = parts[4].upper().split("|")
                        for code in lecturer_course_codes:
                            validated_lecturers_cc.append(code)
            invalid_lecturers_codes = [code for code in entered_course_codes if code in validated_lecturers_cc]
            if invalid_lecturers_codes:
                print(f"The following course codes are already assigned to other lecturers: {', '.join(invalid_lecturers_codes)}")
                continue
            else:
                return lecturers_course_code #to return the validated lecturer course code
        except FileNotFoundError:
            print("\nFile does not exist, creating one right now.\nPlease try using the functions now.")
            open("lecturers.txt", 'w').close() #to create the file if the file is not exist

def add_lecturers(lecturers):
    print("(If you want to cancel, type 'cancel' at any step to stop adding the lecturer.) ")
    lecturers_id = add_lecturers_id(lecturers)
    if lecturers_id is None:
        return #to exit if the id input is canceled
    lecturers_name = add_lecturers_name()
    if lecturers_name is None:
        return #to exit if the name input is canceled
    lecturers_phone_number = add_lecturers_phone_number()
    if lecturers_phone_number is None:
        return #to exit if the phone number input is canceled
    lecturers_email = add_lecturers_email()
    if lecturers_email is None:
        return #to exit if the email input is canceled
    lecturers_course_code = add_lectures_course_code()
    if lecturers_course_code is None:
        return #to exit if the course code input is canceled
    lecturers.append([lecturers_name, lecturers_phone_number, lecturers_email, lecturers_course_code])
    print(f"Mr / Mrs {lecturers_name} added successfully.")
    with open("lecturers.txt", "a") as file:
        file.write(
            f"{lecturers_id},{lecturers_name},{lecturers_phone_number},{lecturers_email},{lecturers_course_code}\n")

def load_lecturers(lecturers_list):  #to load lecturers from the file into a list
    try:
        with open("lecturers.txt", "r") as file:
            for line in file:
                line_data = line.strip().split(",")
                if len(line_data) == 5:
                    identification, name, phone, email, course_code = line_data
                    lecturers_list.append([identification, name, phone, email, course_code])
                else:
                    print(f"There maybe extra values in the data. Please check again!")
        return True #file loaded successfully
    except FileNotFoundError:
        print("Lecturers file is not found in the system.")
    return False #file not found

def save_lecturers(lecturers_list):  #to save the updated lecturers list back to the file
    with open("lecturers.txt", "w") as file:
        for lecturer in lecturers_list:
            file.write(",".join(lecturer) + "\n")

def display_lecturers(lecturers_list):  #to display the list of the lecturers
    if not lecturers_list:
        print("\nNo lecturers available")
        return False
    print("\nBelow is the list of the lecturers:")
    for index, lecturer in enumerate(lecturers_list):
        print(f"{index + 1}. Lecturer's ID: {lecturer[0]} \n   Name: {lecturer[1]} \n   Phone: {lecturer[2]} \n   Email: {lecturer[3]} \n   Course Code: {lecturer[4]}")
        print("==========================================================")
    return True

def update_lecturers_option(): #to display the sub menu of what the user wants to update
    print("\nWhat would you like to update?")
    print("1. Name \n2. Phone Number \n3. Email \n4. Course Code \n5. Cancel")
    try:
        input_choices = int(input("\nEnter the function that you want to update:\n => "))
        return input_choices
    except ValueError:
        return None

def update_lecturers_info(index_input, lecturers_list): #to update based on the user choices
    input_choices = update_lecturers_option()
    if input_choices == 1:
        print("(If you want to cancel, type 'cancel' at any step to stop updating lecturer's name.)")
        new_name = add_lecturers_name()
        if new_name is None:
            return False #to exit if the update input name is canceled
        lecturers_list[index_input][1] = new_name
    elif input_choices == 2:
        print("(If you want to cancel, type 'cancel' to stop updating lecturer's phone number.)")
        new_phone_number = add_lecturers_phone_number()
        if new_phone_number is None:
            return False
        lecturers_list[index_input][2] = new_phone_number
    elif input_choices == 3:
        print("(If you want to cancel, type 'cancel' to stop updating lecturer's email.)")
        new_email = add_lecturers_email()
        if new_email is None:
            return False
        lecturers_list[index_input][3] = new_email
    elif input_choices == 4:
        print("(If you want to cancel, type 'cancel' to stop updating lecturer's course code.)")
        new_course_code = add_lectures_course_code()
        if new_course_code is None:
            return False
        lecturers_list[index_input][4] = new_course_code
    elif input_choices == 5:
        print("Update canceled.")
        return
    else:
        print("Invalid choice. Please try again.")
        return
    print(f"Lecturer {lecturers_list[index_input][1]} updated successfully.")
    save_lecturers(lecturers_list)  #to save the updated list back to the file

def update_lecturers(lecturers_list): #update lecturers function
    file_loaded = load_lecturers(lecturers_list)  #to load lecturers from the file to the list
    if not file_loaded:  #if the file is not found then exit
        return
    if not display_lecturers(lecturers_list):  #to display and if the list is empty then exit
        return
    try:
        index_input = int(input("Enter the number of the lecturer you want to update:\n => ")) - 1
        if index_input < 0 or index_input >= len(lecturers_list):
            print("Invalid input, please try again!")
            return
        selected_lecturer = lecturers_list[index_input]
        print(f"\nSelected Lecturer: {selected_lecturer[0]}")
        update_lecturers_info(index_input, lecturers_list)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def remove_lecturers(lecturers_list):
    file_loaded = load_lecturers(lecturers_list)  #load lecturers from the file to the list
    if not file_loaded:
        return  # if file not found then exit
    if not display_lecturers(lecturers_list):  #to display file if the file is empty then exit
        return
    while True:
        try:
            lecturers_input = int(input("Enter the number of the lecturer you want to remove:\n => ")) - 1
            if lecturers_input < 0 or lecturers_input >= len(lecturers_list):
                print("Invalid input, please try again!") #to asking for the valid input
                return
            selected_lecturer = lecturers_list[lecturers_input]
            print(f"Selected Lecturer: {selected_lecturer[0]}")
            while True:
                confirm = input(f"Are you sure you want to remove {selected_lecturer[0]}? (Y/N):\n => ").strip().upper()
                if confirm == 'Y':
                    lecturers_list.pop(lecturers_input)
                    print(f"Lecturer {selected_lecturer[0]} removed successfully.")
                    save_lecturers(lecturers_list) #to save the updated list back to the file
                    return  #to exit after the removal is successful
                elif confirm == 'N':
                    print("Removal canceled.")
                    return #to exit if user cancels
                else:
                    print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def remove_students(students_list):
    file_loaded = load_students(students_list)  #load students from the file to the list
    if not file_loaded:
        return  # if file not found then exit
    if not display_students(students_list):  #to display file if the file is empty then exit
        return
    while True:
        try:
            students_input = int(input("Enter the number of the student you want to remove:\n => ")) - 1
            if students_input < 0 or students_input >= len(students_list):
                print("Invalid input, please try again!")  #to asking for the valid input
                return
            selected_student = students_list[students_input]
            print(f"Selected Student: {selected_student[0]}")
            while True:
                confirm = input(f"Are you sure you want to remove {selected_student[0]}? (Y/N):\n => ").strip().upper()
                if confirm == 'Y':
                    students_list.pop(students_input)
                    print(f"Student {selected_student[0]} removed successfully.")
                    save_students(students_list)  #save the updated list back to the file
                    return
                elif confirm == 'N':
                    print("Removal canceled.")
                    return
                else:
                    print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_reports():
    try:
        #to count how many lines with valid values are in the files
        total_students = count_lines_with_values("students.txt")
        total_courses = count_lines_with_values("courses.txt")
        total_lecturers = count_lines_with_values("lecturers.txt")
        #display the report
        print("\n============ REPORTS =============")
        print(f"Total Students       : {total_students}")
        print(f"Total Courses        : {total_courses}")
        print(f"Total Lecturers      : {total_lecturers}")
        print("==================================\n")
    except FileNotFoundError:
        print("Error: File not found")

############################################################################################################
#All Lecturer functions
def lecturer_id_login():
    print("==========================================================")
    lecturer_id = input("Enter your Lecturer ID (Press '0' to exit):\n => ").strip().upper()            #.upper is used to make validating easier
    while lecturer_id != '0':
        try:
            with open("lecturers.txt", "r") as file:
                found = False
                for line in file:
                    details = line.strip().split(",")
                    # match the lecturer's ID
                    if len(details) == 5 and details[0] == lecturer_id:
                        found = True
                        lecturer_id = details[0]
                        lecturer_name = details[1]
                        course_codes = details[4].split("|")
                if not found:
                    print("No lecturer found with that ID.")
                    lecturer_id = input("Enter Lecturer ID (Press '0' to exit):\n => ").strip()
                else:
                    lecturer_menu(lecturer_id, lecturer_name, course_codes)
        except FileNotFoundError:
            print(f"Error: File not found.")
            exit()

def view_assigned_menu(lecturer_name, course_codes):
    print(f"Hi, {lecturer_name}\nYour assigned module(s):")
    for code in course_codes:
        print(f" - {code}")

def choose_module(options):
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    valid = False
    while not valid:
        # Get user input
        choice = input("Select a module code (press '0' to cancel):\n => ").strip()
        # Validate input
        if choice.isdigit() and 1 <= int(choice) <= len(options):       #to make sure input is numerical
            selected_option = options[int(choice) - 1]
            print(f"You selected: {selected_option}")
            return selected_option
        elif choice == '0':
            return None
        else:
            print("Invalid choice. Please select a valid option.")

def choose_student():
    #allows the user to select a student by their ID from a file.
    student_id = ''
    student_name = ''
    found = False  #flag to track if the record was found
    try:
        while not found:
            # Ask the user for a Student ID
            student_id = input("Enter Student ID (press '0' to cancel):\n => ").strip().upper()
            # Exit condition
            if student_id.lower() == '0':
                return None
            #open the file and read its content
            with open("enrollments.txt", "r") as file:
                lines = file.readlines()
            for line in lines:
                try:
                    #parse the list format in "enrollments.txt"
                    data = eval(line.strip())
                    #compare the first field (StudentID)
                    if data[0] == student_id:
                        found = True
                        student_name = data[1]
                        break
                except (ValueError, SyntaxError) as e:
                    print(f"Skipping malformed line: {line.strip()} - {e}")
            if not found:
                print(f"Student ID {student_id} does not exist.")
        return student_id, student_name
    except FileNotFoundError:
        print(f"Error: The file enrollments.txt does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def record_grades(course_codes, student_info):
    print(f"\n[Recording grade for {student_info[1]} for module {course_codes}]")
    try:
        while True:
            new_grade = input("Enter student's grade (input 'cancel' to cancel):\n => ").strip().upper()
            if new_grade.isdigit() and 0 <= int(new_grade) <= 100:          #to make sure grade is not below 0 or above 100
                try:
                    with open("enrollments.txt", "r") as file:
                        lines = file.readlines()
                    updated_lines = []
                    record_found = False
                    #update grade with the matching record
                    for line in lines:
                        try:
                            #safely parse line as a Python list
                            data = eval(line.strip())
                            if data[0] == student_info[0]:  #match the student ID
                                for course in data[2:]:
                                    if course[0] == course_codes:  #match course code
                                        course[1] = int(new_grade)  #update grade
                                        record_found = True
                                updated_lines.append(str(data) + "\n")
                            else:
                                updated_lines.append(line)
                        except (ValueError, SyntaxError) as e:
                            print(f"Skipping malformed line: {line.strip()} - {e}")
                    #if no matching record was found, inform user and exit
                    if not record_found:
                        print(f"No enrollment record found for ID {student_info[0]} in Module {course_codes}.")
                        break
                    else:
                        print(f"Grade successfully updated for ID: {student_info[0]} in Module {course_codes}.")
                        with open("enrollments.txt", "w") as file:
                            file.writelines(updated_lines)
                        break
                except FileNotFoundError:
                    print(f"Error: enrollments.txt not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif new_grade == 'CANCEL':
                return
            else:
                print("\nInvalid grade input. Please enter a valid number between 0 and 100.")
                continue
    except FileNotFoundError:
        print("===================================================================================")
        print("The file path cannot be found, try and fix this issue beforehand")
        exit()  #will not create a new file but instead exit because the function is only for view

def get_lecturer_courses(lecturer_id):
    #retrieve the list of courses taught by the lecturer based on the lecturer ID.
    with open("lecturers.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == lecturer_id:
                return parts[4].split("|")  # Map LecturerID to courses
    print("Lecturer not found.")
    return []  # Return an empty list if no courses are found

def group_students_by_modules(lecturer_courses):
    #groups students into the courses taught by the lecturer.
    grouped_students = []  # List of tuples: (course_code, [student_ids])
    students_lookup = []  # List of tuples: (student_id, student_name)
    with open("enrollments.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            data = eval(line.strip())  #convert string to list
            student_id = data[0]
            student_name = data[1]
            students_lookup.append((student_id, student_name)) # store student info
            for course_data in data[2:]:  # Extract enrolled courses
                course_code = course_data[0]
                if course_code in lecturer_courses:
                    #check if course_code exists in grouped_students
                    course_found = False
                    for i in range(len(grouped_students)):
                        if grouped_students[i][0] == course_code:
                            grouped_students[i][1].append(student_id)
                            course_found = True
                            break
                    #if not found, create a new entry
                    if not course_found:
                        grouped_students.append((course_code, [student_id]))
    return grouped_students, students_lookup

def view_student_list(lecturer_id):
    # Get modules taught by the lecturer
    lecturer_courses = get_lecturer_courses(lecturer_id)
    # Check if lecturer_courses is empty
    if not lecturer_courses:
        print("No courses found for the lecturer.")
        return
    # Group students by modules
    grouped_students, students_lookup = group_students_by_modules(lecturer_courses)
    if not grouped_students:
        print("No students found for the assigned modules.")
        return
    for course, students in grouped_students:
        print(f"Module: {course}")
        print("StudentID  | Name")
        print("-" * 30)
        for student_id in students:
            student_name = next((name for id_, name in students_lookup if id_ == student_id), "Unknown")
            print(f"{student_id:<10} | {student_name}")
        print("-" * 30)
        print("")

def mark_attendance(course_codes, student_info):
    try:
        with open("enrollments.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The enrollments file does not exist.")
        return
    #flags and updated content
    updated_lines = []
    student_found = False
    for line in lines:
        data = eval(line.strip())  #parse line as a Python list
        student_id = data[0]
        student_name = data[1]
        attendance_courses = data[2:]  #to read index that are 2 and above in list in a list
        if student_id == student_info[0]:  #validate student ID
            student_found = True
            course_updated = False
            for course in attendance_courses:
                if course[0] == course_codes:  #validate course code
                    present = course[2]
                    absent = course[3]
                    #prompt for attendance
                    valid = False
                    choice = ""
                    while not valid:
                        choice = input(f"Is {student_name} present in {course_codes} [Y/N]?\n => ").strip().upper()
                        if choice == "Y":
                            present += 1
                            valid = True
                        elif choice == "N":
                            absent += 1
                            valid = True
                        else:
                            print("Invalid input. Please enter 'Y' or 'N'.")
                    #update the attendance
                    course[2] = present
                    course[3] = absent
                    course_updated = True
                    print(f"[{'ABSENT' if choice == 'N' else 'PRESENT'}] {student_name} in Module {course_codes}.")
            if not course_updated:
                print(f"No enrollment found for {student_name} in {course_codes}.")
        #append updated data
        updated_lines.append(str(data) + "\n")
    if not student_found:
        print(f"Student {student_info[1]} (ID: {student_info[0]}) not found in enrollments.")
    #write updated lines back to the file
    with open("enrollments.txt", "w") as file:
        file.writelines(updated_lines)

def view_student_grades(lecturer_id, course_codes):
    try:
        #read the file contents
        with open("enrollments.txt", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    #filter the records for the specific course
    filtered_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            data = eval(line.strip())  #parse line as a Python list
            student_id = data[0]
            student_name = data[1]
            grade_courses = data[2:]  #to read index that are 2 and above in list in a list
            for course in grade_courses:
                if course[0] == course_codes:  #validate the course code
                    grade = course[1]
                    filtered_records.append((student_id, student_name, grade))
        except Exception as e:
            print(f"Error parsing line: {line.strip()} - {e}")
    #display the results
    if filtered_records:
        print(f"Grades for Module: {course_codes} (Lecturer ID: {lecturer_id})")
        print("    ID    |    Name    | Grade")
        print("-" * 30)
        for record in filtered_records:
            print(f"{record[0]:<6}  | {record[1]:<10} | {record[2]}")
    else:
        print(f"No records found for Module: {course_codes}.")
############################################################################################################
#All Student Management functions
def available_module():
    print("\n======== Available Courses ========\n")
    try:
        with open("courses.txt", "r") as file:
            module_list = []
            for line in file:
                parts = line.strip().split(",")
                module_list.append(parts)
            for index, course in enumerate(module_list): #to display course neatly
                print(f"{index + 1}.Course Code: {course[0]}\n   Course Name: {course[1]}\n   Credit: {course[2]}")
                print("====================================")
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit()

def enroll_student():
    print("====== Enroll Student to a Course ======")
    try:
        while True:
            enroll_student_id = input("Student ID:\n => ").strip().upper() #.upper is used to make validating easier
            enroll_student_name = input("Student Name:\n => ").strip().upper()
            # Check if student exists
            validate_students = []
            with open("students.txt", "r") as student_file:
                for line in student_file:
                    validate_students.append(line.strip().split(","))
            for parts in validate_students:
                if parts[0] == enroll_student_id and parts[1] == enroll_student_name:
                    #to check if a student already existed in enrollments.txt
                    with open("enrollments.txt", "r") as enrollment_file:
                        for line in enrollment_file:
                            if line.strip():
                                parts = eval(line.strip())  #parse the list format in "enrollments.txt"
                                if parts[0] == enroll_student_id and parts[1] == enroll_student_name:
                                    print("There is already data for this student in the system")
                                    return
                        else:
                            validate_courses = []
                            with open("courses.txt", "r") as course_file:
                                for line in course_file:
                                    course_code = line.split(",")[0].strip()
                                    validate_courses.append(course_code)
                            enrollment_record = [enroll_student_id, enroll_student_name]
                            enrolled_courses = []  #so courses cannot be enrolled twice to the same student
                            total_student_course = 5
                            for course in range(total_student_course):
                                while True:
                                    enroll_course_code = input(f"Enter course code for course {course + 1}:\n => ").strip().upper()
                                    if enroll_course_code not in validate_courses:
                                        print(f"Error: Invalid course code")
                                    elif enroll_course_code in enrolled_courses:
                                        print(f"Error: Course already entered")
                                    else:
                                        #use none(grade)and 0(attendance) cannot be added by student manage
                                        enrollment_record.append([enroll_course_code, None, 0, 0])
                                        enrolled_courses.append(enroll_course_code)
                                        break
                            with open("enrollments.txt", "a") as enrollments_file:
                                enrollments_file.write(f"{enrollment_record}\n")
                            print("Successfully enrolled student in course")
                            return
            print("Student does not exist.\n")
            cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
            if cancel_input == '0': #to give user the chance to cancel if ID not found
                break
            else:
                continue
    except FileNotFoundError:
        print("\nFile does not exist, creating one right now.\nPlease try using your functions now.\n")
        open("enrollments.txt", 'w').close() #so it creates the file with no data

def view_enrollments():
    print("\n====== Student Enrollments: ======\n")
    try:
        with open("enrollments.txt", "r") as file:
            enrollments_list = []
            for line in file:
                if line.strip():
                    parts = eval(line.strip())  #to parse or read list in a list
                    enrollments_list.append(parts)
            for index, enrollment in enumerate(enrollments_list):
                student_id = enrollment[0]
                student_name = enrollment[1]
                enrollment_courses = enrollment[2:]
                #if None then it will show as N/A
                course_details = ', '.join([f"[{course[0]}, {course[1] if course[1] else 'N/A'}, {course[2]}, {course[3]}]" for course in enrollment_courses])
                print(f"{index + 1}. Student ID: {student_id}\n   Student Name: {student_name}\n   Courses: {course_details}")
                print("\n================================")
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit()

def un_enroll_student():
    view_enrollments()
    try:
        while True:
            print("Which one do you want to remove?")
            un_enroll_student_id = input("Student ID:\n => ").strip().upper() #.upper is used to make validating easier
            un_enroll_student_name = input("Student Name:\n => ").strip().upper()
            with open("enrollments.txt", "r") as file:
                enrollments = file.readlines()
            updated_enrollments = []
            for line in enrollments:
                if line.strip():
                    parts = eval(line.strip()) #to parse or read list in a list
                    student_id = parts[0]
                    student_name = parts[1]
                    if student_id == un_enroll_student_id and student_name == un_enroll_student_name:
                        print("Successfully un-enrolled student")
                        #to prevent un-enroll loop in the same student
                        un_enroll_student_id = None
                        un_enroll_student_name = None
                    else:
                        updated_enrollments.append(line)
            if un_enroll_student_id is None:
                with open("enrollments.txt", "w") as file:
                    file.writelines(updated_enrollments)
                return
            else:
                print("Student is not from the list\n")
                cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
                if cancel_input == '0': #to give user the chance to cancel if ID not found
                    break
                else:
                    continue
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit()

def view_grades():
    print("\n================= Access Student Grades ==================")
    try:
        while True:
            grades_student_id = input("Student ID:\n => ").strip().upper()       #.upper is used to make validating easier
            grades_student_name = input("Student Name:\n => ").strip().upper()
            grades_student_courses = input("Course Code:\n => ").strip().upper()
            with open("enrollments.txt", "r") as file:
                enrollments = file.readlines()
                for line in enrollments:
                    if line.strip():
                        parts = eval(line.strip()) #to parse or read list in a list
                        student_id = parts[0]
                        student_name = parts[1]
                        grade_courses = parts[2:]
                        if student_id == grades_student_id and student_name == grades_student_name:
                            for course in grade_courses:
                                course_code, grade, present, absent = course
                                if course_code == grades_student_courses:
                                    grades = grade if grade else 'N/A'                 #if none then it will show as N/A
                                    print(f"\n====== Details ======\n")
                                    print(f"Student ID: {student_id}\nStudent Name: {student_name}\nCourse: {course_code}\nGrades: {grades}")
                                    print(f"\n=====================\n")
                                    return
                else:
                    print("\nError: No data found.")
                    cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
                    if cancel_input == '0': #to give user the chance to cancel if ID not found
                        break
                    else:
                        continue
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit()

def view_attendance():
    print("\n========== View Student Attendance Percentage ============")
    try:
        while True:
            attendance_student_id = input("Student ID:\n => ").strip().upper()       #.upper is used to make validating easier
            attendance_student_name = input("Student Name:\n => ").strip().upper()
            attendance_student_courses = input("Course Code:\n => ").strip().upper()
            with open("enrollments.txt", "r") as file:
                enrollments = file.readlines()
                for line in enrollments:
                    if line.strip():
                        parts = eval(line.strip())  #to parse or read list in a list
                        student_id = parts[0]
                        student_name = parts[1]
                        attendance_courses = parts[2:]
                        if student_id == attendance_student_id and student_name == attendance_student_name:
                            for course in attendance_courses:
                                course_code, grade, present, absent = course
                                if course_code == attendance_student_courses:
                                    if present + absent > 0:
                                        attendance_percentage = (present / (present + absent)) * 100
                                    else:
                                        attendance_percentage = 0
                                    print("\n========= Student Attendance =======\n")
                                    print(f"Student ID: {student_id}\nStudent Name: {student_name}\nCourse: {course_code}\nAttendance Percentage: {attendance_percentage:.2f}%")
                                    print(f"\n====================================\n")
                                    return
                else:
                    print("\nError: No data found.")
                    cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
                    if cancel_input == '0': #to give user the chance to cancel if ID not found
                        break
                    else:
                        continue
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit()

############################################################################################################
#All registrar functions
def add_student_id(students):
    while True:
        new_student_id = input("Enter student's ID (TPXXXXXX):\n => ").strip().upper()      #.upper is used to make validating easier
        if null_input(new_student_id):
            continue
        elif cancel_command(new_student_id):
            return None
        for student in students:
            if student[0] == new_student_id:
                print(f"Invalid input! ({new_student_id}) already exists).")
                break
        else:
            try:
                with open ("students.txt", "r") as students_files:
                    for student in students_files:
                        student_id_from_file = student.split(",")[0].strip()
                        if new_student_id == student_id_from_file:
                            print(f"Invalid input! ({new_student_id}) already exists).")
                            break
                    else:
                        return new_student_id
            except FileNotFoundError:
                return new_student_id

def add_student_name():
    while True:
        new_student_name = input("Enter student's name:\n => ").strip().upper()
        if null_input(new_student_name):
            continue
        elif cancel_command(new_student_name):
            return None
        elif any(char.isnumeric() for char in new_student_name):
            print ("Student name must be alphabetic. Please try again!")
            continue
        else:
            return new_student_name

def add_contact_information():
    while True:
        new_contact_information = input("Please enter the student's contact information (60XXXXXXXXX):\n => ").strip()
        if null_input(new_contact_information):
            continue
        elif cancel_command(new_contact_information):
            return None
        elif new_contact_information.isnumeric():
            return new_contact_information
        else:
            print ("Student's contact information must be numeric. Please try again!")

def add_program():
    while True:
        new_program = input("Enter student's program:\n => ").strip().upper()
        if null_input(new_program):
            continue
        elif cancel_command(new_program):
            return None
        else:
            return new_program

def add_department():
    while True:
        new_department = input("Enter student's department:\n => ").strip().upper()
        if null_input(new_department):
            continue
        elif cancel_command(new_department):
            return None
        else:
            return new_department

def register_new_students(students): #to register the student
    print("======== Register New Students ========")
    print("(If you want to cancel, type 'cancel' at any step to stop adding the course.)")
    new_student_id = add_student_id(students)
    if new_student_id is None:
        return
    new_student_name = add_student_name()
    if new_student_name is None:
        return
    new_contact_information = add_contact_information()
    if new_contact_information is None:
        return
    new_program = add_program()
    if new_program is None:
        return
    new_department = add_department()
    if new_department is None:
        return
    students.append([new_student_id, new_student_name, new_contact_information, new_program, new_department])
    print (f"{new_student_name} has been registered successfully!")
    with open ("students.txt","a") as file:
        file.write(f"{new_student_id},{new_student_name},{new_contact_information},{new_program},{new_department}\n")

#to store & list all students registered
def load_students(students_list):
    try:
        with open("students.txt","r") as file:
            for line in file:
                student_id, student_name, student_contact_info, student_program, student_department = line.strip().split(",")
                students_list.append([student_id, student_name, student_contact_info, student_program, student_department])
    except FileNotFoundError:
        print("Students file not found. Starting with an empty list.")
    return students_list

def save_students(students_list):
    with open ("students.txt","w") as file:
        for students in students_list:
            file.write(",".join(students) + "\n")

def display_students(students_list):
    if not students_list:
        print("\nNo students available")
        return False
    print("Below is the list of the students:\n")
    for index, students in enumerate(students_list):
        print(f"{index + 1}. Student ID: {students[0]} \n   Name: {students[1]} \n   Contact Information: {students[2]} \n   Program: {students[3]} \n   Department: {students[4]}")
        print("==========================================================")
    return True

def update_students_option():
    print("\n======= What would you like to update? =======")
    print("1. Name \n2. Contact Information \n3. Program \n4. Department \n5. Cancel")
    try:
        input_choices = int(input("\nEnter the function that you want to update:\n => "))
        return input_choices
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def update_students_info(index_input,students_list):
    input_choices = update_students_option()
    if input_choices == 1:
        print("(If you want to cancel, type 'cancel' at any step to stop updating lecturer's name.)")
        new_name = add_student_name()
        if new_name is None:
            return False
        students_list[index_input][1] = new_name
    elif input_choices == 2:
        print("(If you want to cancel, type 'cancel' at any step to stop updating lecturer's name.)")
        new_contact_information = add_contact_information()
        if new_contact_information is None:
            return False
        students_list[index_input][2] = new_contact_information
    elif input_choices == 3:
        print("(If you want to cancel, type 'cancel' at any step to stop updating lecturer's name.)")
        new_program = add_program()
        if new_program is None:
            return False
        students_list[index_input][3] = new_program
    elif input_choices == 4:
        print("(If you want to cancel, type 'cancel' at any step to stop updating lecturer's name.)")
        new_department = add_department()
        if new_department is None:
            return False
        students_list[index_input][4] = new_department
    elif input_choices == 5:
        print("Update canceled.")
        return
    else:
        print("Invalid choice. Please try again.")
        return

    print(f"Student {students_list[index_input][0]} updated successfully.")
    save_students(students_list)

def update_students(students_list):
    load_students(students_list)
    if not display_students(students_list):
        return
    try:
        index_input = int(input("Enter the number of the student you want to update:\n => ")) -1
        if index_input < 0 or index_input >= len(students_list):
            print("Invalid input, please try again!")
            return
        selected_students = students_list[index_input]
        print(f"\nSelected Student: {selected_students[0]}")
        update_students_info(index_input,students_list)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def manage_enrollments():
    print("\nManage Enrollments")
    view_enrollments()
    while True:
        print("\nWhich one do you want to update?")
        enrollments_student_id = input("Student ID:\n => ").strip().upper()
        enrollments_student_name = input("Student Name:\n => ").strip().upper()
        student_found = False
        successful_update = False  #initialize the flag
        try:
            # read enrollments.txt
            with open("enrollments.txt", "r") as file:
                enrollments = file.readlines()
            updated_enrollments = []
            # validate updated courses
            valid_course = []
            with open("courses.txt", "r") as course_txt:
                for line in course_txt:
                    valid_course.append(line.split(",")[0].strip().upper())
            for line in enrollments:
                if line.strip():  # ensure the line is not empty
                    parts = eval(line.strip())  # parse the list format in enrollments.txt
                    student_id = parts[0]
                    student_name = parts[1]
                    courses = parts[2:]
                    if student_id == enrollments_student_id and student_name == enrollments_student_name:
                        student_found = True
                        while True:
                            enrollments_course_code = input("Enter the course code to remove:\n => ").strip().upper()
                            # validate course code
                            student_courses = []
                            remove_course = False
                            for course in courses:
                                if course[0] == enrollments_course_code:
                                    remove_course = True
                                else:
                                    student_courses.append(course) #keep the course
                            if not remove_course:
                                print("Error: Student not enrolled in this course")
                                continue
                            break
                        parts[2:] = student_courses
                        while True:
                            change_course = input("Enter the new course code:\n => ").strip().upper()
                            duplicate_course = False
                            for course in student_courses:
                                if course[0] == change_course:
                                    duplicate_course = True
                                    break
                            if change_course in valid_course and not duplicate_course:
                                new_course = [change_course, None, 0, 0]
                                student_courses.append(new_course)
                                parts[2:] = student_courses
                                print("Successfully updated student course.")
                                successful_update = True  #exit the loop once the course is successfully updated
                                break
                            elif duplicate_course:
                                print("Error: Student already enrolled in this course.")
                                continue
                            else:
                                print("Error: Please input valid course code.")
                                continue
                    updated_enrollments.append(f"{parts}\n")  # update data
            if not student_found:
                print("\nError: Student not found.")
                cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
                if cancel_input == '0':
                    break
                else:
                    continue
            with open("enrollments.txt", "w") as file:
                file.writelines(updated_enrollments)
            if successful_update:  #check the flag before exiting try block
                break
        except FileNotFoundError:
            print("The file path cannot be found, try and fix this issue beforehand.")
            exit()

def issue_transcripts():
    print("=============== Issue Student Transcript =================")
    try:
        while True:
            transcripts_student_id = input("Student ID:\n => ").strip().upper()
            transcripts_student_name = input("Student Name:\n => ").strip().upper()
            with open("enrollments.txt", "r") as file:
                for line in file:
                    parts = eval(line.strip())  # parse the list format in enrollments.txt
                    student_id = parts[0]
                    student_name = parts[1]
                    courses = parts[2:]
                    if student_id == transcripts_student_id and student_name == transcripts_student_name:
                        print("\n========================================\nSTUDENT TRANSCRIPTS\n========================================")
                        print(f"Student ID: {student_id}\nStudent Name:{student_name}\n========================================")
                        print("Course Code:     Grades:     Attendance:")
                        for course in courses:
                            course_code = course[0]
                            grades = course[1] if course[1] else 'N/A'
                            present = course[2]
                            absent = course[3]
                            if present + absent > 0:
                                attendance_percentage = (present / (present + absent)) * 100
                            else:
                                attendance_percentage = 0
                            print(f"{course_code: <16} {grades: <11} {attendance_percentage}%")
                        return
                else:
                    # This else block executes only if no break occurred
                    print("\nError: No student found.")
                    cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
                    if cancel_input == '0':
                        break
                    else:
                        continue
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit()

def student_information():
    print("=============== View Student Information =================")
    try:
        while True:
            info_student_id = input("Student ID:\n =>  ").strip().upper()
            info_student_name = input("Student Name:\n => ").strip().upper()
            with open("students.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if parts[0] == info_student_id and parts[1] == info_student_name:
                        print("\n========================================\nSTUDENT INFORMATION\n========================================")
                        print(f"Student ID: {parts[0]}\nStudent Name: {parts[1]}\nContact Information: {parts[2]}\nProgram: {parts[3]}\nDepartment: {parts[4]}")
                        print("\n========================================")
                        return
            print("\nError: No student found.")
            cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
            if cancel_input == '0':
                break
            else:
                continue
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit()

############################################################################################################
#All Accountant functions
def subtraction(num1, num2):
    return str(int(num1) - int(num2))

def addition(num1, num2):
    return str(int(num1) + int(num2))

def record_or_add_tuition():
    print("========= Record or Add Tuition Fees for Student =========")
    try:
        while True:     #loop until input is validated
            tuition_student_id = input("Student ID:\n => ").strip().upper()       #.upper is used to make validating easier
            tuition_student_name = input("Student Name:\n => ").strip().upper()
            tuition_student_program = input("Program:\n => ").strip().upper()
            validate_students = []
            with open("students.txt", "r") as student_file:
                for line in student_file:
                    validate_students.append(line.strip().split(","))
            for parts in validate_students:
                if parts[0] == tuition_student_id and parts[1] == tuition_student_name and parts[3] == tuition_student_program:
                    #to see if student record already exist
                    with open("tuition.txt", "r") as tuition_file:
                        for line in tuition_file:
                            parts = line.strip().split(",")
                            if parts[0] == tuition_student_id and parts[1] == tuition_student_name and parts[2] == tuition_student_program:
                                print("There is an existing record of this student tuition in the system. Type '0' if you don't wish to change the data.")
                        else:
                            while True:
                                try:
                                    total_tuition = int(input("Add or Update Tuition Fees:\n => "))
                                    break
                                except ValueError:
                                    print("Please enter a valid number")
                            if update_tuition_record(tuition_student_id, tuition_student_name, tuition_student_program, total_tuition, '0'):
                                print(f"Tuition record updated successfully for {tuition_student_id}")
                            else:
                                print(f"New tuition record added successfully for {tuition_student_id}")
                            return
            print("\nStudent does not exist")
            cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
            if cancel_input == '0':     #to give user the chance to cancel if ID not found
                break
            else:
                continue
    except FileNotFoundError:  #create a txt file if it does not exist
        print("===================================================================================")
        print("\nFile does not exist, creating one right now.\nPlease try using the functions now.")
        open("tuition.txt", 'w').close()


def update_tuition_record(student_id, student_name, student_program, total_tuition, paid_tuition):
    updated_data = False
    records = []
    with open("tuition.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if parts[0] == student_id and parts[1] == student_name and parts[2] == student_program:
                #update tuition and outstanding fee automatically
                parts[3] = addition(parts[3], total_tuition)
                parts[4] = addition(parts[4], paid_tuition)
                parts[5] = subtraction(parts[3], parts[4])
                updated_data = True
            records.append(parts)
    #if previous record does not exist, will create a new one
    if not updated_data:
        records.append([student_id, student_name, student_program, str(total_tuition), str(paid_tuition), str(subtraction(total_tuition, paid_tuition))])
    with open("tuition.txt", "w") as file:
        for record in records:
            file.write(",".join(record) + "\n")
    return updated_data

def payment_records():
    print("====== Record Student Tuition Fees Paid by Student ======")
    try:
        while True:     #loop until input is validated
            paid_student_id = input("Student ID:\n => ").strip().upper()       #.upper is used to make validating easier
            validate_record = []
            with open("tuition.txt", "r") as tuition_file:
                for line in tuition_file:
                    validate_record.append(line.strip().split(","))
            for parts in validate_record:
                if parts[0] == paid_student_id:
                    while True:    #loop once again to prevent unwanted input
                        try:
                            paid_tuition = float(input("Add Paid Tuition Fees:\n => "))
                            break
                        except ValueError:
                            print("Please enter a valid number")
                    parts[4] = addition(parts[4], paid_tuition)
                    parts[5] = subtraction(parts[3], parts[4])
                    print(f"Tuition record updated successfully for {paid_student_id}")
                    with open("tuition.txt", "w") as file:
                        for record in validate_record:
                            file.write(",".join(record) + "\n")
                    return
            print("\nStudent ID not found")
            cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
            if cancel_input == '0':       #to give user the chance to cancel if ID not found
                break
            else:
                continue
    except FileNotFoundError:
        print("===================================================================================")
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit() #will not create a new file but instead exit because the function is only for view

def outstanding_fee():
    print("\n========= List of Students with Outstanding Fee ==========\n")
    try:
        with open("tuition.txt", "r") as file:
            outstanding_fee_list = []
            for line in file:
                parts = line.strip().split(",")
                if int(parts[5]) != 0:
                    outstanding_fee_list.append(parts)
            for index, student in enumerate(outstanding_fee_list):
                print(f"{index + 1}. Student ID: {student[0]}\n   Student Name: {student[1]}\n   Program: {student[2]}\n   Outstanding Fees: {student[5]}\n")
                print("==========================================================")
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit() #will not create a new file but instead exit because the function is only for view


def fee_receipts():
    print(" ================ Print Tuition Receipt ================")
    try:
        while True:
            receipt_student_id = input("Input the Student ID:\n => ").strip().upper()               #.upper is used to make validating easier
            receipt_student_name = input("Input the Student Name:\n => ").strip().upper()
            validate_record = []
            with open("tuition.txt", "r") as file:
                for line in file:
                    validate_record.append(line.strip().split(","))
                for parts in validate_record:
                    if parts[0] == receipt_student_id and parts[1] == receipt_student_name:
                        print("\n============================\nRECEIPT\n============================")
                        print(f"Student ID: {parts[0]}\nStudent Name: {parts[1]}\nProgram: {parts[2]}\nTotal Tuition: {parts[3]}\nPaid Tuition: {parts[4]}\nOutstanding Fee: {parts[5]}")
                        print("============================")
                        return
                print("Error: Student is not found.")
                cancel_input = input("Press 0 if you want to cancel or press anything to continue\n => ")
                if cancel_input == '0':     #to give user the chance to cancel if ID not found
                    break
                else:
                    continue
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit() #will not create a new file but instead exit because the function is only for view

def financial_summary():
    print("UMS Financial Summary")
    tuition_summary = 0.0
    paid_summary = 0.0
    outstanding_summary = 0.0
    try:
        with open("tuition.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")         #automatically summarize all payments
                tuition_summary += float(parts[3])
                paid_summary += float(parts[4])
                outstanding_summary += float(parts[5])
        print("\n=============================\nFinancial Summary\n=============================")
        print(f"Total Tuition Fees: {tuition_summary}\nTotal Paid Fees: {paid_summary}\nTotal Outstanding Fees: {outstanding_summary}")
        print("==============================")
    except FileNotFoundError:
        print("The file path cannot be found, try and fix this issue beforehand.")
        exit() #will not create a new file but instead exit because the function is only for view

main_menu()