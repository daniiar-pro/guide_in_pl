from data_class.news import News
from data_class.study import Study
from data_class.legalisation import legalisation
from data_class.jobsearch import job_search
from data_class.faq import faq
from user_class.report import report
from user_class.donate import donate


def display_menu():
    """Displays sections."""
    print("\nThis website helps you to find appropriate information for your issue:\n")
    print("a. Latest News")
    print("b. Study")
    print("c. Legalisation")
    print("d. Jobs")
    print("e. FAQ")
    print("f. Report an issue")
    print("g. Donate")
    print("h. Go Back\n")


def handle_choice(choice):
    """Get user user"""
    if choice == "a":
        News.get_news()
    elif choice == "b":
        Study.get_study_info()
    elif choice == "c":
        print("Staying legal in Poland involves adhering to the country's laws and regulations. Here are some key aspects to consider:\n")
        legalisation()
    elif choice == "d":
        job_search()
    elif choice == "e":
        print("Frequently asked questions from users:\n")
        faq()
    elif choice == "f":
        report()
    elif choice == "g":
        donate()
    elif choice == "h":
        return False
    else:
        print("Valid option must be selected ;(")
    return True


def main():
    """Runs the program flow"""
    while True:
        display_menu()
        choice = input("To find out more, select (a - h): \n").strip().lower()
        if not handle_choice(choice):
            break


if __name__ == "__main__":
    main()
