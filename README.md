This code is a command-line program for calculating and managing student exam grades. It offers options to input student data, calculate final grades and letter grades based on specific weighting, view saved data, save data to a JSON file, and load data from a JSON file.
Key Functions:

    exam_calc_welcome: This function displays a welcoming message with a stylized logo for the ITUCU Exam Calculator.

    dataInputFunc: Collects the names and exam scores of students. It validates that:
        The number of students is a valid integer.
        Names contain only alphabetical characters.
        Exam scores (midterm, final, and homework) are integers between 0 and 100.

    Each student’s data is stored in a dictionary with initial placeholders for TotalGrade and letterGrade.

    calcFunc: Calculates the final numeric grade and corresponding letter grade for each student.
        The final grade is based on weights: 30% midterm, 40% final exam, and 30% homework.
        Letter grades are assigned based on ranges for total scores: e.g., AA for scores above 91, BA for scores above 81, and so on.

    showDataFunc: Displays student data.
        It can show details for a specific student or all students.
        Data is displayed in a JSON-like format, improving readability.

    saveDataToJson: Saves the list of student data to a JSON file. By default, it saves to database.json.

    loadDataFromJson: Loads student data from the JSON file. If the file doesn’t exist, it shows an error.

Main Loop:

A main while loop allows users to choose actions:

    1: Add student data.
    2: Calculate and assign grades.
    3: Display student data.
    4: Save data to a JSON file.
    5: Load data from a JSON file.
    0: Exit the program.

Each selection is validated to ensure it’s a number. If the input doesn’t match an option, an error message prompts the user to try again.
