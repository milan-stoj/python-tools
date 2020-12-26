# Simple calculator for estimating Blood Alcohol Content %
#
# BAC = ((A / W * r) * 100 ) - (dT * 0.015)
# A = alcohol consumed in grams (US Standard drink = 14g)
# W = body-weight in grams
# r = gender-constant (male = 0.68, female = 0.55 --- set on line 11)

legal_limit = 0.08
standard_drink_weight = 14
gender_constant = 0.68

while True:
    weight_in_lbs = input("Enter you weight in lbs: ")
    weight_in_grams = int(weight_in_lbs) * 453.592

    drinks_consumed = float(input("How many drinks have you consumed?: "))
    alcohol_consumed = drinks_consumed * standard_drink_weight
    hrs_elapsed = float(input("How many hours have elapsed?: "))

    BAC = ((alcohol_consumed)/(weight_in_grams * gender_constant)) * 100 - (hrs_elapsed * 0.015)

    print("-" * 50)
    print("Your estimated BAC:", BAC)
    if BAC > legal_limit :
        print("Stop! You are beyond the legal limit.")
    elif BAC > 2/3 * legal_limit :
        print("Slow-down. You are cutting it close!")
    else:
        print("You are under the legal limit.")
