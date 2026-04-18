total_miles = 0
total_gallons = 0
trip_count = 0

miles = int(input("Enter the miles driven or -1 to quit: "))

while miles != -1:
    gallons = int(input("Enter the gallons: "))
    total_miles += miles
    total_gallons += gallons
    trip_count +=1

    miles_per_gallon = miles / gallons
    print(f'Miles per gallon = {miles_per_gallon:.2f}')
    combined_milespergallon = total_miles / total_gallons
    print(f'Combined miles per gallon = {combined_milespergallon:.2f}')
    miles = int(input("Enter the miles driven or -1 to quit: "))
    
if trip_count == 0:
    print("No trip was recorded")
else:
   print(f"The total trips is: {trip_count}");
   print(f"The total miles driven is: {total_miles}");
   print(f"The total gallons used is: {total_gallons}");
   print(f"The final combined mile per gallon is: {total_miles / total_gallons:.2f}");


