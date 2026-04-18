total_miles = 0
total_gallons = 0
trip_count = 0

miles = int(input("Enter the miles driven or -1 to quit: "))

while miles != -1:
    gallons = int(input("Enter the gallons: "))
    total_miles += miles
    total_gallons += gallons
    miles_per_gallon = miles / gallons
    trip_count +=1
    print('Miles per gallon =' + miles_per_gallon)
    
    print('Combined miles per gallon = {combined_milespergallon:.2f}')

miles = int(input("Enter the miles driven or -1 to quit: "))
combined_milespergallon = total_miles / total_gallons
    
if trip_count == 0:
    print("No trip was recorded")
else:
   print("The total trips is: " + trip_count);
   print("The total miles driven is: " + total_miles);
   print("The total gallons used is: " + total_gallons);
   print("The final combined mile per gallon is: " + total_miles / total_gallons);


