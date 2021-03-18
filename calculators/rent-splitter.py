# Calculator to determine rent split.
# 

# Renter details
renter_a = "MIL"
a_income = 50000.00
renter_b = "MIR"
b_income = 64000.00

# Apartment Details
monthly_rent = 1275.00
total_square_ft = 820.00

# Renter A Details
a_bedroom_sq_ft = 10 * (13 + 7/12)
a_private_bath = 0.5
a_private_sq_ft = a_bedroom_sq_ft + 50 * a_private_bath

# Renter B Details 
b_bedroom_sq_ft = (9 + 1/12) * (11 + 3/12)
b_private_bath = 0
b_private_sq_ft = b_bedroom_sq_ft + 50 * b_private_bath

# Renter A Payment
total_private_sq_ft = a_private_sq_ft + b_private_sq_ft
a_pct_of_private = a_private_sq_ft / total_private_sq_ft
b_pct_of_private = b_private_sq_ft / total_private_sq_ft

# Rent Splits
a_split = a_pct_of_private * monthly_rent
b_split = b_pct_of_private * monthly_rent

print(renter_a + " pays $" + str(a_split))
print(renter_b + " pays $" + str(b_split))
print(64000/50000)
print(0.28 * monthly_rent)
