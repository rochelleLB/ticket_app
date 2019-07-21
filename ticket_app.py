TICKET_PRICE = 10

tickets_remaining = 100

# Run this code while there are still tickets left
while tickets_remaining >= 1:
    print("There are {} tickets remaining".format(tickets_remaining))
    users_name = input("What is your name? ")
    ticket_amount_request = input("Hi {}, how many tickets would you like? ".format(users_name))

    # Expect a ValueError  to happen and handle it appropriately
    try:
        ticket_amount_request = int(ticket_amount_request)
        if ticket_amount_request > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("{}. Please try again.".format(err))
    else:
        #Calculate the price (number of tickets * price) and assign it to a variable
        def ticket_price_calculation(ticket_amount, ticket_price):
            complete_total = ticket_amount * ticket_price
            return "The total cost for your tickets is £{}.".format(complete_total)

        total_price = ticket_price_calculation(ticket_amount_request, TICKET_PRICE)
        print(total_price)
        continue_purchase = input("Would you like to proceed? Y/N ")

        # If they want to proceed
        if continue_purchase.lower() == "y":
            # TODO: Gather credit card info and process
            print("SOLD! Thank you for your purchase.")
            tickets_remaining -= ticket_amount_request
        else:
            #Thank them
            print("Thank you. Come again soon!")

# Alert user that there are no more tickets
print("Sorry {}, we have no tickets left!".format(users_name))
