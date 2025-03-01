# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    # Collect each student's name and score
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    marks = [record[1] for record in records]
    sortmarks = sorted(set(marks))
    second = sortmarks[1]

    second_lowest_students = [record[0] for record in records if record[1] == second]
    second_lowest_students.sort()

    for student in second_lowest_students:
        print(student)