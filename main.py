def calculate_tip(bill_amount, tip_percentage):
 tip_amount=bill_amount*(tip_percentage/100)
 total_amount=bill_amount+tip_amount
 return tip_amount, total_amount
def convert_km_to_miles(km):
    miles=km*0.621371
    return miles
def main():
 bill_amount = float(input("Enter The Bill Amount: $"))
 tip_percentage = float(input("Enter The Tip Percentage: "))
 tip, total = calculate_tip(bill_amount, tip_percentage)
 print(f"Tip Amount: ${tip:.2f}")
 print(f"Total Amount: ${total:.2f}")
 km=float(input("Enter the distance in kilometers: "))
 miles=convert_km_to_miles(km)
 print(f"{km} kilometers is equal to {round(miles, 2)} miles.")
if __name__ == "__main__":
    main()