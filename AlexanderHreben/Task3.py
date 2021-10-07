# File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students
# 2) Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age.

import csv


def get_top_performers(file_path: str, number_of_top_students=5) -> list:
    all_students = list()
    with open(file_path, encoding='utf-8') as file_for_read:
        reader_object = csv.reader(file_for_read, delimiter=",")
        for row in reader_object:
            all_students.append(row)
        # print(all_students)

    sort_students = sorted(all_students[1:], key=lambda student: student[2], reverse=True)
    return [student[0] for student in sort_students[:number_of_top_students]]


def write_in_desending_order(file_path: str):
    all_data = list()
    with open(file_path, encoding='utf-8') as file_for_read:
        reader_object = csv.reader(file_for_read, delimiter=",")
        for row in reader_object:
            all_data.append(row)
        headers = all_data[0]

    sort_students = sorted(all_data[1:], key=lambda student: student[1], reverse=True)

    with open("data/sorted_students.csv", 'w') as file_for_write:
        file_writer = csv.writer(file_for_write, delimiter=",", lineterminator="\r")
        file_writer.writerow(headers)
        for row in sort_students:
            file_writer.writerow(row)


if __name__ == '__main__':
    print(get_top_performers("data/students.csv", 3))
    write_in_desending_order("data/students.csv")
