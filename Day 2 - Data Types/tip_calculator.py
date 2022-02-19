print('Welcome to the tip calculator!')

#1. Ask the user for the bill amount.
bill = float(input('\nHow much was your meal?: $'))
#2. Ask the user for the tip percentage.
tip = int(input('\nWhat percentage would you like to tip? (We recommend either 10, 12 or 15): '))
#3. Ask the user for the number of people that will be splitting the bill.
people = int(input('\nHow many people are in your party?: '))
#4. Calculate the total (tip/100 is the percentage).
total_per_person = (bill + (bill*(tip/100))) / people
#5. Format the total so it always shows 2 decimals.
final_total = '${:.2f}'.format(total_per_person)

print(f'\nEach person in your party owes {final_total}')