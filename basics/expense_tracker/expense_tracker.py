expenses = []
while True:
    item = input("What did you buy? ('quit' when done): ")

    if item == 'quit':
        break

    cost = float(input(f"How much did {item} cost? "))
    expenses.append((item, cost))

total = sum(cost for item, cost in expenses)
print(f"You spent ${total:.2f} today")



