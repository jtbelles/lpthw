# LPTHW Exercise 4 EC - budget2.py
# budget1.py rewritten with variables

# Category Header
print "Monthly Expenditures:"

# Listing variables
rent = 1000.0
sl = 55.0
ci = 90.0
food = 200.0
gas = 100.0
cable = 30.0
cp = 100.0
tme = rent + sl + ci + food + gas + cable + cp
mon_income = 2000.00
surplus = mon_income - tme

# Listing the monthly expenditures
print "Rent: ", rent
print "Student Loan: ", sl
print "Car Insuranse: ", ci
print "Food: ", food
print "Gas: ", gas
print "Cable: ", cable
print "Cell Phone: ", cp

# Output Monthly Totals
print "Total Monthly Expenditures: ", tme
print "Monthly Income is: ", mon_income
print "Monthly Surplus is: ", surplus
