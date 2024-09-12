# Design an algorithm and implement a program to solve the Making Change Problem (Greedy Approach)

def make_change():
    amount = int(input("Enter the total amount: "))

    num_coins = int(input("Enter the number of available coin denominations: "))
    coins = []
    for i in range(num_coins):
        coin = int(input(f"Enter coin denomination {i+1}: "))
        coins.append(coin)

    coins.sort(reverse=True)

    remaining_amount = amount
    change = []

    for coin in coins:
        while coin <= remaining_amount:
            change.append(coin)
            remaining_amount -= coin

    print("Minimum number of coins required:", len(change))
    print("Coins used to make the change:", change)

make_change()