# Name: HIMANSHU SAINI

#roll number:2501010201

# Title: GradeBook Analyzer 



import csv
import statistics
def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    return statistics.median(marks.values())

def find_max_score(marks):
    name = max(marks, key=marks.get)
    return name, marks[name]

def find_min_score(marks):
    name = min(marks, key=marks.get)
    return name, marks[name]

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90: grade = "A"
        elif score >= 80: grade = "B"
        elif score >= 70: grade = "C"
        elif score >= 60: grade = "D"
        else: grade = "F"
        grades[name] = grade
    return grades

def manual_input():
    marks = {}
    print("\nManual Entry (type 'done' to finish)\n")
    while True:
        name = input("Name: ")
        if name.lower() == "done":
            break
        score = float(input("Score: "))
        marks[name] = score
    return marks

def load_csv():
    marks = {}
    filename = input("CSV filename: ")
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            marks[row[0]] = float(row[1])
    return marks


def main():

    print("Gradebook Analyzer")
    print("1 = Manual entry")
    print("2 = Load CSV")

    while True:
        choice = input("\nChoose input method: ")
        if choice == "1":
            marks = manual_input()
        elif choice == "2":
            marks = load_csv()
        else:
            print("Invalid choice.")
            continue

       
        avg = calculate_average(marks)
        med = calculate_median(marks)
        hi_name, hi_score = find_max_score(marks)
        lo_name, lo_score = find_min_score(marks)

       
        grades = assign_grades(marks)

       
        passed = [s for s, sc in marks.items() if sc >= 40]
        failed = [s for s, sc in marks.items() if sc < 40]

       
        print("\nName\tScore\tGrade")
        print("---------------------------")
        for name in marks:
            print(f"{name}\t{marks[name]}\t{grades[name]}")

        print("\nAverage:", avg)
        print("Median:", med)
        print("Highest:", hi_name, hi_score)
        print("Lowest:", lo_name, lo_score)

        print("\nPassed:", passed)
        print("Failed:", failed)

        again = input("\nRun again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()