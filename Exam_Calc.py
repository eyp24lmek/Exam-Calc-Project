import json

students = []

def exam_calc_welcome():
    print("Welcome to the ITUCU exam calculator")
    print("***********************************************")
    print("*     __    __     _                          *")
    print("*    / / /\\ \\ \\___| | ___ ___  _ __ ___   ___ *")
    print("*    \\ \\/  \\/ / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\*")
    print("*     \\  /\\  /  __/ | (_| (_) | | | | | |  __/*")
    print("*      \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___|*")
    print("*                                             *")
    print("*            ITUCU Exam Calc                  *")
    print("*                                             *")
    print("*********************************************** developed by Eyup Sucu")
exam_calc_welcome()

def dataInputFunc():
    counter = 0
    snumber = input("Enter the number of students: ")

    while not snumber.isdecimal():
        print("Please enter a valid number of students:")
        snumber = input("Enter the number of students: ")

    snumber = int(snumber)

    while counter < snumber:
        name = input("Name of student: ")
        cacheName = name.replace(' ', '')
        
        while not cacheName.isalpha():
            name = input("Please enter a valid name: ")
            cacheName = name.replace(' ', '')

        while True:
            try:
                midTerm = int(input("Please enter midTerm exam grade: "))
                if 0 <= midTerm <= 100:
                    print(f"You have entered the midterm exam grade as: {midTerm}")
                    break
                else:
                    print("Your midterm grade must be between 0 and 100")
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                FinalTerm = int(input("Please enter FinalTerm exam grade: "))
                if 0 <= FinalTerm <= 100:
                    print(f"You have entered the FinalTerm exam grade as: {FinalTerm}")
                    break
                else:
                    print("Your FinalTerm grade must be between 0 and 100")
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                Homework = int(input("Please enter homework exam grade: "))
                if 0 <= Homework <= 100:
                    print(f"You have entered the Homework exam grade as: {Homework}")
                    break
                else:
                    print("Your Homework grade must be between 0 and 100")
            except ValueError:
                print("Please enter a valid number.")
        
        student_data = {
            "name": name,
            "midTerm": midTerm,
            "FinalTerm": FinalTerm,
            "Homework": Homework,
            "TotalGrade": None,
            "letterGrade": None
        }

        students.append(student_data)
        counter += 1

def calcFunc():
    student_name = input("Enter student name (or type 'all' to calculate for all students): ")
    for student in students:
        if student_name.lower() == "all" or student['name'] == student_name:  
            midTerm = student['midTerm']
            FinalTerm = student['FinalTerm']
            Homework = student['Homework']
            TotalGrade = midTerm * 30 / 100 + FinalTerm * 40 / 100 + Homework * 30 / 100
        
        if TotalGrade >= 91:
            letterGrade = "AA"
        elif TotalGrade >= 81:
            letterGrade = "BA"
        elif TotalGrade >= 71:
            letterGrade = "BB"
        elif TotalGrade >= 61:
            letterGrade = "BC"
        elif TotalGrade >= 51:
            letterGrade = "CC"
        elif TotalGrade >= 41:
            letterGrade = "E"
        else:
            letterGrade = "F"
        
        print(f"{student['name']} for final grade: {TotalGrade} {letterGrade}")
        student['TotalGrade'] = TotalGrade
        student['letterGrade'] = letterGrade

def showDataFunc():
    newName = input("Enter student name (or type 'all' to see all students): ")
    if newName.lower() == "all":
        for student in students:
            student_json = json.dumps(student, indent=4)  
            print(student_json)  
            print("------------------------")  
    else:
        found = False
        for student in students:
            if student['name'] == newName:
                student_json = json.dumps(student, indent=4)  
                print(student_json) 
                found = True
                break
        if not found:
            print("Student not found")

def saveDataToJson(filename='database.json'):
    with open(filename, 'w') as json_file:
        json.dump(students, json_file, indent=4)  
        print(f"Data has been saved to {filename}")

def loadDataFromJson(filename='database.json'):
    global students  
    try:
        with open(filename, 'r') as json_file:
            students = json.load(json_file)
            print(f"Data has been loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Please save data first.")
    except json.JSONDecodeError:
        print(f"File {filename} contains invalid JSON.")

while True:
    try:
        selection = int(input("To add new data type 1, calculate grades type 2, show data type 3, save data type 4, load data type 5, exit type 0: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if selection == 1:
        dataInputFunc()
    elif selection == 2:
        calcFunc()
    elif selection == 3:
        showDataFunc()
    elif selection == 4:
        saveDataToJson()       
    elif selection == 5:
        loadDataFromJson() 
    elif selection == 0:
        break
    else:
        print("Input is wrong")
