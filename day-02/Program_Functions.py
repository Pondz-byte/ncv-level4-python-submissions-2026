 def amount_due(facility_code, hours): #Calculate amount before VAT

    if facility_code == "squa":
        rate = 13.00

    elif facility_code == "swim":
        rate = 12.00

    elif facility_code == "gym":
        rate = 11.00

    elif facility_code == "wei":
        rate = 8.00

    amount = rate * hours

    return amount

def final_amount_due(amount): # Calculate final amount including VAT

    vat = amount * 0.14

    final_amount = amount + vat

    return final_amount
 
def display(name, final_amount): # Display customer payment

    print("\n----- PAYMENT DETAILS -----")
    print("Customer name:", name)
    print("Final amount payable: R{:.2f}".format(final_amount))

def process_payment(): Process payment

    name = input("Enter customer name: ")

    facility_code = input("Enter facility code (squa, swim, gym, wei): ")

    hours = float(input("Enter number of hours: "))

    # Calulate amount before VAT
      amount = amount_due(facility_code, hours) 

    # Calculate final amount including VAT
    final_amount = final_amount_due(amount)

    # Display payment details
    display(name, final_amount)

process_payment()


