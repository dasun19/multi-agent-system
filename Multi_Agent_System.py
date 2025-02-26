#index_no - 20APP5021
#name - P.L.D.K.Cooray


from colorama import Fore, init

init(autoreset=True)


details_list = []
total_cost = 0

def student_reg_agent(run_last = False):

    global details_list

    try:
        if run_last == False:
            student_details = input("\nStudent Registration Agent: Please enter your name and student id(separate with a comma): ").lower()
            details = student_details.split(",")
            details_list = [detail.strip() for detail in details]
            print(f"\nStudent Registration Agent: Welcome, {details_list[0].capitalize()}(ID:{details_list[1]}). Proceeding to course selection. ")

        elif run_last == True:
            print(f"\nStudent Registration Agent: Your registration is complete. Thank you for registering, {details_list[0].capitalize()}!")

    except IndexError:
        print(Fore.RED + "\nPlease enter your name and student id separate from a comma.")
        student_reg_agent()

def course_selection_agent():

    global total_cost

    courses = {
        'data structures' : 300,
        'algorithms' : 350,
        'machine learning' : 400
    }

    print("\nCourse Selection Agent: Available courses are: \n")

    i = 1
    for key,value in courses.items():
        print(f"{i}. {key.capitalize()} - ${value}")
        i+=1

    try:
        courses_for_reg = input("\nPlease type the courses you want to register for(separate by commas): ").lower()
        courses_list1 = courses_for_reg.split(',')
        courses_list = [course.strip() for course in courses_list1]


        for key in courses_list:
            total_cost += courses[key]

        print(f"\nCourse Selection Agent: You have selected {', '.join(courses_list).capitalize()}. The total cost is ${total_cost}.")

    except KeyError:
        print(Fore.RED + "\nPlease enter available courses only and Please type the correct course name as display in the course list.")
        course_selection_agent()

def payment_agent():

    global total_cost

    payment = int(input("\nPayment Agent: Please enter your payment amount($): ").strip())

    try:

        if payment == total_cost:
            print(f"\nPayment Agent: Payment of ${payment} received. Your registration is confirmed.")
            student_reg_agent(run_last=True)

        else:
            print(Fore.RED + "\nPlease enter the correct total cost.")
            payment_agent()
    except ValueError:
        print(Fore.RED + "\nPlease enter the correct total cost."  )
        payment_agent()


if __name__ == "__main__":

    while True:
        print("\n\n.....University Student Registration System.....")
        print("\nOptions: ")
        print("\n1 - I want to register for courses.")
        print("2 - Exit from the university registration system.")
        options = ['1', '2']

        option = input("\nSelect an Option(1 or 2): ")

        if option not in options:
            print(Fore.RED + "\nPlease select an valid option.")

        elif option == '1':
            student_reg_agent()
            course_selection_agent()
            payment_agent()

        elif option == '2':
            print("\nYou are exiting from the registration system...")
            break