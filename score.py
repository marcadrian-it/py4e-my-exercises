score = input("Enter Score between 0.0 and 1.0: ")
score = float(score)
if score < 0.0 or score > 1.0:
    print('Error!')
    quit()
else:
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    elif score < 0.6:
        grade = 'F'
print(grade)
