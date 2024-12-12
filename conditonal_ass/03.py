score = 102


# pruning 
if score >= 101 :
    print("Give Correct Score !!!")
    exit()

if score >= 90 :
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=70 :
    grade = 'C'
elif score >=60 :
    grade = 'D'
elif score < 40 : 
    grade = 'F'
else :
    grade = 'E'

print("Grade of student : ", grade)
