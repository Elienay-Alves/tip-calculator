def tip_calculator():
    print("Welcome to the tip calculator.")

    bill = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? "))
    people_to_split = int(input("How many people to split the bill? "))

    total_per_person = bill / people_to_split
    total_bill_for_person = tip / 100 * total_per_person + total_per_person
    converted_bill_for_person = "{:.2f}".format(total_bill_for_person)

    return f"Each person should pay: ${converted_bill_for_person}"


print(tip_calculator())
