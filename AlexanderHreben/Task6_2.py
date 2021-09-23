#  Write a program which makes a pretty print of a part of the multiplication table.

start_row = 2
fin_row = 4
start_line = 3
fin_line = 7

for num_in_line in range(start_line, fin_line + 1):  # first line
    print("\t", num_in_line, end="")

for num_in_row in range(start_row, fin_row + 1):  # first row
    print("\n", num_in_row, end="")
    for num in range(start_line, fin_line + 1):
        print("\t", (num * num_in_row), end="")
