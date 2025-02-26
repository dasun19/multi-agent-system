
#index_no = 20APP5021
#name = P.L.D.K.Cooray

from colorama import Fore, init

init(autoreset=True)

class Student:

    def __init__ (self, name, student_id):
        self.name = name.capitalize()
        self.student_id = student_id
        self.selected_courses = []
        self.total_cost = 0

    def select_courses(self, courses):
        print("\nCourse Selection Agent: Available Courses are:\n")

        i = 1
        for course,value in courses.items():
            print(f"{i}. {course.strip().capitalize()} - {value}")
            i +=1

        while True:
            try:
                courses_for_reg = input("\nPlease type the courses you want to register for (separate by comma): ").lower()
                selected_courses = [course.strip() for course in courses_for_reg.split(',')]

                if not all(course in courses for course in selected_courses):
                    raise KeyError

                self.selected_courses = selected_courses
                for course in selected_courses:
                    self.total_cost += courses[course]

                print(f"\nCourse Selection Agent: You have selected {','.join(map(str.strip, self.selected_courses)).capitalize()}. The total cost is ${self.total_cost}.")
                break

            except KeyError:
                print(Fore.RED + "\nInvalid course selection. Please enter valid course names exactly as displayed. ")


    def make_payment(self):

        while True:
            try:
                payment = int(input("\nPayment Agent: Please enter your payment amount ($): ").strip())

                if payment == self.total_cost:
                    print(f"\nPayment Agent: Payment of ${payment} received. Your registration is confirmed. ")
                    break
                else:
                    print(Fore.RED + "\nIncorrect Amount. Please enter the correct total cost.")

            except ValueError:
                print(Fore.RED + "\nInvalid input. Please enter the correct total cost.")



class RegistrationAgent:

    courses = {
        'data structures' : 300,
        'algorithms' : 350,
        'machine learning' : 400
    }

    def start(self):

        while True:
            print("\n\n.....University Student Registration System.....")
            print("\nOptions: ")
            print("\n1 - I want to register for courses.")
            print("2 - Exit from the registration system.")

            option = input("\nSelect an option(1 or 2): ").strip()

            if option == '1':

                student = self.register_student()
                student.select_courses(self.courses)
                student.make_payment()
                print(f"\nStudent Registration Agent: Thank you for registering, {student.name}!")

            elif option == '2':
                print("\nYou are exiting from the registration system...")
                break

            else:
                print(Fore.RED + "\nInvalid option. Please select 1 or 2.")

    def register_student(self):
        while True:
            try:
                student_details = input("\nStudent Registration Agent: Please enter your name and student ID (separate by a comma): ").strip()
                name, student_id = map(str.strip, student_details.split(','))
                print(f"\nStudent Registration Agent: Welcome, {name.capitalize()} (ID: {student_id}). Proceeding to course selection.")
                student = Student(name, student_id) #create an object from the Student class
                return student

            except ValueError:
                print(Fore.RED + "\nInvalid input. Please enter your name and student ID separated by a comma.")


if __name__ == "__main__":
    system = RegistrationAgent()
    system.start()