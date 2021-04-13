Course_Room = {'CS101': 3004, 'CS102' : 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}

Course_Instructor = {'CS101': 'Haynes', 'CS102' : 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}

Course_Time = {'CS101': '8:00 a.m.', 'CS102' : '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}

temp = input("Enter your Course Number: ")

if temp in Course_Room and Course_Instructor and Course_Time:
    print(Course_Room[temp], Course_Instructor[temp], Course_Time[temp])
else:
    print("Course not found")
