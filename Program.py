from grade import Grade

grade1 = Grade(student_name="Vasya", topic="python", grade="100")
print(grade1)

grade2 = Grade(student_name="Petya", topic="python", grade="90")
print(grade2)

grade3 = Grade(student_name="Mahmud", topic="python", grade="96")
print(grade3)

grade4 = Grade(student_name="Armen", topic="python", grade="99")
print(grade4)

print(Grade.get_average())

grade4.topic = "math"

print(grade4)


