students = []

for i in range(int(input())):
    name = input()  
    c, t = [int(x) for x in input().split()] 
    students.append((name, c, t)) 

sorted_students = sorted(students, key =lambda x: (-x[1], x[2], x[0]))

for student in sorted_students:
    print(student[0], student[1], student[2])   
