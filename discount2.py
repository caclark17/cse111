#Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your computer's operating system.
#Your program correctly computes and prints the discount amount if applicable.
#Your program correctly computes and prints the sales tax amount and the total amount due.
from datetime import datetime

DISCOUNT_RATE = .1

while True:
    # determine what day of the week it is
    today = datetime.now().weekday()

    # ask for the total for the customers purchase
    total = float(input("What is the total? : "))
    if total == 0:
        break

    discount = 0
    # if tue or wed and >= 50
    if (today == 1 or today == 2): 

        if total >= 50:

            # take 10% off total
            discount = total * DISCOUNT_RATE

        else:
            no_discount = 50 - total
            print(
                f"Need to purchase ${no_discount:.2f} to qualify for discount."
            )

    # add 6% sales tax
    tax = (total - discount) * .06

    final = total - discount + tax

    # print initial total, discount, sales tax, new total
    print(f"subtotal: ${total:7.2f}")
    print(f"discount: ${discount:7.2f}")
    print(f"tax:      ${tax:7.2f}")
    print(f"total:    ${final:7.2f}")
    print()
    print()
