# Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`.
# Each name should start with a new line.

with open('data/unsorted_names.txt', 'r') as unsort_names:
    sorted_names = sorted(unsort_names.readlines())  # get list
with open('data/sorted_names.txt', 'w') as sort_names:
    sort_names.write(''.join(sorted_names))  # accepts only str
