# #4.12 LAB: Exact change - functions
def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100

    num_quarters = user_total // 25
    user_total %= 25

    num_dimes = user_total // 10
    user_total %= 10

    num_nickels = user_total // 5
    user_total %= 5

    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__': 
    input_val = int(input())    
    if input_val <= 0:
        print("no change")
    else:
        # Calling the exact_change function
        dollars, quarters, dimes, nickels, pennies = exact_change(input_val)

        if dollars == 1:
            print("1 dollar")
        elif dollars > 1:
            print(dollars, "dollars")

        if quarters == 1:
            print("1 quarter")
        elif quarters > 1:
            print(quarters, "quarters")

        if dimes == 1:
            print("1 dime")
        elif dimes > 1:
            print(dimes, "dimes")

        if nickels == 1:
            print("1 nickel")
        elif nickels > 1:
            print(nickels, "nickels")

        if pennies == 1:
            print("1 penny")
        elif pennies > 1:
            print(pennies, "pennies")

# def exact_change(user_total):
#     denominations = [('dollar', 100), ('quarter', 25), ('dime', 10), ('nickel', 5), ('penny', 1)]
#     result = []

#     for name, value in denominations:
#         count = user_total // value
#         user_total %= value

#         if count == 1:
#             result.append(f"1 {name}")
#         elif count > 1:
#             result.append(f"{count} {name}s")

#     return result


# if __name__ == '__main__':
#     input_val = int(input())

#     if input_val <= 0:
#         print("no change")
#     else:
#         change = exact_change(input_val)
#         if len(change) == 0:
#             print("no change")
#         else:
#             print("\n".join(change))
