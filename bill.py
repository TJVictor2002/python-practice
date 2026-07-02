def main():
    bill = float(input("What is the total bill? "))
    tip = float(input("What percentage tip? "))
    people = int(input("How many people are splitting it? "))

    total_with_tip = bill + (bill * tip / 100)
    per_person = split_bill(total_with_tip, people)
    print(f"${total_with_tip:.2f} as total with tip")
    print(f"Each person owes ${per_person:.2f}")


def split_bill(total, n):
    return total / n


main()