#!/usr/bin/env python3
'''
Program Caculates if a house is affordable for a specifc wage in Santa Cruz County
'''
import sys

exit_code = 0
file = sys.stderr
file.write('Number of Bedrooms? ')
bedrooms = input()
file.write('Hourly Wage? ')
wage = input()

# Error Checking
if bedrooms.isnumeric() is False:
    file.write('ERROR: Please input a Number for Bedrooms!')
    sys.exit(2)
elif int(bedrooms) > 2:
    file.write('ERROR: Plese enter a Number for Bedrooms less than 2!')
    sys.exit(3)

try:
    x = float(wage)
except Exception:
    file.write('ERROR: Wage could not be Computed. Please Retry!')
    sys.exit(4)

if float(wage) < 0:
     file.write('Please enter a Positve Number for Wage')
     sys.exit(5)

# Caculations
if int(bedrooms) == 0:
    house = 2085
elif int(bedrooms) == 1:
    house = 2385
elif int(bedrooms) == 2:
    house = 3138

weekly_wage = 40 * float(wage)
daily_income = weekly_wage / 7
monthly_income = daily_income * 30.4375
house_income = monthly_income * 0.3
housing_wage = house * (3 + 1 / 3) / 30.4375 * 7 / 40

if house_income < house:
    exit_code = 1


x = float(wage) - housing_wage
wage_diff = format(abs(x),'.2f')

# output

check = sys.stdout
output = (
    'The wage of', format(float(wage),'.2f'),
     'has a difference of', wage_diff,
      'from the housing wage of', format(housing_wage,'.2f')
    )

print(output,check)
sys.exit(exit_code)