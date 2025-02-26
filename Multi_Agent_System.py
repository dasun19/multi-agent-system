#index_no - 20APP5021
#name - P.L.D.K.Cooray


from colorama import Fore, init

init(autoreset=True)


def student_reg_agent():

    while True:
        try:
            student_details = input("\nStudent Registration Agent: Please enter your name and student id(separate with a comma): ").strip()
            name, student_id = map(str.strip, student_details.split(","))

            print(f"\nStudent Registration Agent: Welcome, {name.capitalize()}(ID:{student_id}). Proceeding to course selection. ")
            return name, student_id

        except ValueError:
            print(Fore.RED + "\nInvalid input. Please enter your name and student id separate from a comma.")


def course_selection_agent(courses):

    print("\nCourse Selection Agent: Available courses are: \n")

    i = 1
    for key,value in courses.items():
        print(f"{i}. {key.capitalize()} - ${value}")
        i+=1

    while True:

        try:
            courses_for_reg = input("\nPlease type the courses you want to register for(separate by commas): ").lower()
            courses_list1 = courses_for_reg.split(',')
            courses_list = [course.strip() for course in courses_list1]

            if not all(key in courses for key in courses_list):
                raise KeyError

            total_cost = 0
            for key in courses_list:
                total_cost += courses[key]

            print(f"\nCourse Selection Agent: You have selected {', '.join(courses_list).capitalize()}. The total cost is ${total_cost}.")
            return total_cost

        except KeyError:
            print(Fore.RED + "\nPlease enter available courses only and Please type the correct course name as display in the course list.")


def payment_agent(total_cost):

    while True:
        try:
            payment = int(input("\nPayment Agent: Please enter your payment amount($): ").strip())

            if payment == total_cost:
                print(f"\nPayment Agent: Payment of ${payment} received. Your registration is confirmed.")
                return

            else:
                print(Fore.RED + "\nPlease enter the correct total cost.")

        except ValueError:
            print(Fore.RED + "\nPlease enter the correct total cost."  )



def main():

    courses = {
        'data structures': 300,
        'algorithms': 350,
        'machine learning': 400
    }

    while True:
        print("\n\n.....University Student Registration System.....")
        print("\nOptions: ")
        print("\n1 - I want to register for courses.")
        print("2 - Exit from the university registration system.")


        option = input("\nSelect an Option(1 or 2): ")


        if option == '1':
            name, student_id = student_reg_agent()
            total_cost = course_selection_agent(courses)
            payment_agent(total_cost)
            print(f"\nStudent Registration Agent: Your registration is complete. Thank you for registering, {name.capitalize()}!")

        elif option == '2':
            print("\nYou are exiting from the registration system...")
            break

        else:
            print(Fore.RED + "\nPlease select an valid option(1 or 2).")


if __name__ == "__main__":
    main()
