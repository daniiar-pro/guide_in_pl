import csv
from datetime import date


class Donate:
    total_donation = 0
    filename = "./info/total_donation.csv"

    @classmethod
    def display_total_donations(cls):
        """Display all the time donations"""
        try:
            with open(cls.filename, "r") as file:
                reader = csv.DictReader(file)
                cls.total_donation = sum(int(row["amount"]) for row in reader if row)
        except FileNotFoundError:
            print("No previous donations found.")

    @classmethod
    def donate_us(cls):
        Donate.display_total_donations()
        """Prompt user, handle donation"""
        amount = int(input("How much would you like to donate us? "))

        if amount > 0:
            try:
                with open(cls.filename, "a", newline="") as file:
                    fieldnames = ["date", "amount"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    if file.tell() == 0:
                        writer.writeheader()

                    writer.writerow({"date": date.today(), "amount": amount})
                    print(f"You donated: ${amount}")

                    cls.total_donation += amount
            except FileNotFoundError as e:
                print(f"File Not Found: {e}")
            else:
                cls.display_total_donation()
        else:
            print("Cannot donate $0 or less.")

    @classmethod
    def display_total_donation(cls):
        """Display the current total donation."""
        print(f"Total donation: ${cls.total_donation}")





donate = Donate.donate_us
