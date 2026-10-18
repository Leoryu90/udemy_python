# fruits = ["apple", "peach", "pear"]

# for fruit in fruits:
#     print(fruit)

student_scores = [78, 92, 45, 63, 88, 100, 71, 54, 96, 82]

sum_score = 0

for score  in student_scores:
    sum_score += score

print(sum_score)

sum_score2 = sum(student_scores)

print(sum_score2)

max_score = 0

for in_score in student_scores:
    if max_score < in_score:
        max_score = in_score

print(max_score)