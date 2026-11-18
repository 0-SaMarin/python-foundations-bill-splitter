def welcome_script():
    print("Thank you for choosing the Biferia as your restaurant today!")
    tip = int(input("Please insert the amount of tip that you want to award the waiter that served you."))
    amount_of_people = int (input("Would you be so kind to reming us how many people we served today? "))
    bill = int(input("And the bill would be"))
    print("Thak you for all of this information, we will gladly print you receipt briefly.")
    return print_receipt(amount_of_people, bill, tip)


def print_receipt(amount_of_people, bill, tip):
    total_bill = int(bill + bill * tip / 100)
    bill_per_person = total_bill / amount_of_people//2
    print("Subtotal:" + str(bill))
    print("Tip: " + str(tip))
    print(f"Total: + str(total_bill):,")
    print("Bill:" + str(bill_per_person))

    return welcome_script()

