marks = int(input("Enter your marks (0-100)"))

if marks >= 90:
    grade = 'A'

elif marks >= 75 and marks < 90:
    grade = 'B'

elif marks >= 50 and marks < 75:
    garde = 'C'

else:
    grade = 'F'

print("Your grade is", grade)