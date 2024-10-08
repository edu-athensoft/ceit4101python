"""
quiz333
q1
Marie       85
Phoebe      78
Sabrina     96
Emma        85
Jerry       48
Amy         73
Isabelle    59
Clark       45
Jackson     56
tester1     96
tester2     45

"""

dataset = [
    ["Marie",85], ["Phoebe",78], ["Sabrina",96],
    ["Emma",85], ["Jerry",48], ["Amy",73],
    ["Isabelle",59],["Clark",45], ["Jackson",56],
    ["Tester1",96],["Tester2",45]
]

group_no = "GROUP-191116"

# Task 1. Figure out the average score of this group.
print("Task 1. Figure out the average score of this group.")
total_score = 0
for entry in dataset:
    total_score += entry[1]

total_students = len(dataset)
average_score = total_score/total_students
print(f"Average score of Group {group_no} is {average_score:.1f}")
print()

# Task 2. Count how many students got A.  (Grade A:  score >= 90)
# Task 3. Count how many students failed.  (Grade F:  score < 60)
numbers_of_a = 0
numbers_of_f = 0
for entry in dataset:
    if entry[1] >= 90:
        numbers_of_a += 1
    if entry[1] < 60:
        numbers_of_f += 1

print("Task 2. Count how many students got A.  (Grade A:  score >= 90)")
print(f"{numbers_of_a} students got A.")
print()

print("Task 3. Count how many students failed.  (Grade F:  score < 60)")
print(f"{numbers_of_f} students got failed.")
print()

# Task 4. Figure out the highest score and the one(s) who got the score.
# Task 5. Figure out the lowest score and the one(s) who got the score.
highest_score = dataset[0][1]
highest_name_set = set()
highest_name_set.add(dataset[0][0])

lowest_score = dataset[0][1]
lowest_name_set = set()
lowest_name_set.add(dataset[0][0])

last_highest_score = highest_score
last_lowest_score = lowest_score

for entry in dataset:
    if entry[1] >= highest_score:
        highest_name, highest_score = entry
        if highest_score > last_highest_score:
            highest_name_set.clear()
            highest_name_set.add(highest_name)
            last_highest_score = highest_score
        if highest_score == last_highest_score:
            highest_name_set.add(highest_name)
            last_highest_score = highest_score

    if entry[1] <= lowest_score:
        lowest_name, lowest_score = entry
        if lowest_score < last_lowest_score:
            lowest_name_set.clear()
            lowest_name_set.add(lowest_name)
            last_lowest_score = lowest_score
        if lowest_score == last_lowest_score:
            lowest_name_set.add(lowest_name)
            last_lowest_score = lowest_score

print("Task 4. Figure out the highest score and the one(s) who got the score.")
print(f"{highest_name_set} got the highest score {highest_score}")
print()

print("Task 5. Figure out the lowest score and the one(s) who got the score.")
print(f"{lowest_name_set} got the lowest score {lowest_score}")