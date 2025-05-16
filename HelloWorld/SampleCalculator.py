def simple_calculator():
    expression = input("Enter an arithmetic expression (e.g., 1 + 2 * 3): ")
    try:
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Invalid input. Error:", e)

simple_calculator()

def buyABun():
    bun_price = 2.40
    money = None  # initialize money to avoid UnboundLocalError

    while True:
        user_input = input("Enter money: ")
        try:
            money = float(user_input)
            break  # only break if input is valid
        except ValueError:
            print("You did not enter a valid value.")
            print("Breaking out of this loop, please run the program again")
            break

    if money is not None:
        buns = int(money // bun_price)
        print(f"You can buy {buns} bun(s) with ${money:.2f}.")


buyABun()
