def main():
    bill = get_number("What is the total bill? ")
    discount = get_discount(bill)
    bill = bill - (bill * discount)

    tip = get_number("What percentage tip? ")

    people = int(get_number("How many people are splitting it? "))



    total_with_tip = bill + (bill * tip / 100)
    per_person = split_bill(total_with_tip, people)
    print(f"${total_with_tip:.2f} as total with tip")
    print(f"Each person owes ${per_person:.2f}")

    match people:
        case 1:
            print("Just you? No need to split!")
        case 2 | 3:
            print("Cozy group.")
        case _:
            print("Big group — don't forget to double check everyone paid!")

def get_discount(bill):
        if bill >= 100:
            return 0.10
        elif bill >= 50:
            return 0.05
        else:
            return 0.0

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a number. Try again.")


def split_bill(total, n):
    return total / n




main()