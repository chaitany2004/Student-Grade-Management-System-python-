# Student Grade Management System


#creating a empty dictionary
student_grades={}

#Add a new student

def add_student(name,grade):
    student_grades[name]=grade
    print(f"Added {name} with a {grade}")
    
    
#update a student 

def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updated as {grade}")
    else:
        print(f"{name} is not found")
        
        
#delete a student

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        
        print(f"{name} has been deleted ")
        
    else:
        print(f"{name} is not found!")
        
# view all students

def display_all_students():
    if student_grades:
        for name,grade in student_grades.items():
            
            print(f"{name} :{grade}")
            
    else:
        print("No students found/added")
        
        
# main
def main():
    print("\n *************Student Grades Management System************")
    
    while True:
        
        print("_________________________________________________________________________")

        
        print("1. Add Student/ 2.Update Student/ 3.Delete Student/ 4.View Student/ 5.Exit")
        
        print("_________________________________________________________________________")
        
        choice =int(input("Enter your choice = "))
        #adding a student 
        if choice==1:
            name = input("enter student name = ")
            grade = int(input("enter the student grade = "))
            add_student(name, grade)
            
        #updating a student 
        elif choice==2:
            name = input("enter student name = ")
            grade = int(input("enter the student grade = "))
            update_student(name,grade)
            
        #deleting a student 
        elif choice==3:
            name = input("enter student name = ")
            delete_student(name)
            
        #display all students 
        elif choice==4:
            display_all_students()
            
        # exit from the system
        elif choice==5:
            print("Closing the system")
            break
        
        else:
            print("Invalid Choice")
            
main()
