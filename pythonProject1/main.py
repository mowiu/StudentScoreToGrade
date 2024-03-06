# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def calculate_grade(score):
    grade_ranges = {
        (90, 100): 'A',
        (70, 89): 'B',
        (60, 69): 'C',
        (50, 59): 'D',
        (40, 30): 'F'
    }

    for range_, grade in grade_ranges.items():
        if range_[0] <= score <= range_[1]:
            return grade
    else:
        return 'F'

# Read the student's score from the user




score = int(input("Enter the student's score: "))

# Calculate and display the grade
grade = calculate_grade(score)
print("The student's grade is:", grade)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
