names=[['Michael',50],['Tammy',60],['John',70]]

payment = ('Michael',50)
def settle_up(payments):
    total = 0
    amounts = {}
    for (person, amount) in payments:
        if person not in amounts:
            amounts[person] = 0
        amounts[person] += amount
        total += amount
    
    for person, amount in amounts.items():
        print(f"{person} owes {amount}")

settle_up(names)