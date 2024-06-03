# Write a program that will work endlessly to make coffee for all interested 
# persons until the shutdown signal is given. Introduce two new options: 
# "remaining" and "exit".

# Do not forget that you can be out of resources for making coffee. 
# If the coffee machine doesn't have enough resources to make coffee, the program 
# should output a message that says it can't make a cup of coffee and state what is missing.

# And the last improvement to the program at this step — if the user types 
# "buy" to buy a cup of coffee and then changes his mind, they should be able 
# to type "back" to return into the main cycle.


class CoffeeMachine:
    def __init__(resources):
        resources.water = 400
        resources.milk = 540
        resources.coffee_beans = 120
        resources.disposable_cups = 9
        resources.money = 550

   def print_state(resources):
        print("The coffee machine has:")
        print(f"{resources.water} ml of water")
        print(f"{resources.milk} ml of milk")
        print(f"{resources.coffee_beans} g of coffee beans")
        print(f"{resources.disposable_cups} disposable cups")
        print(f"${resources.money} of money")

    def buy(resources):
        while True:
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            choice = input("> ")
            if choice == "back":
                return
            elif choice == "1":
                resources.buy_espresso()
                return
            elif choice == "2":
                resources.buy_latte()
                return
            elif choice == "3":
                resources.buy_cappuccino()
                return
            else:
                print("Invalid choice")

    def buy_espresso(resources):
        if resources.water < 250 or resources.coffee_beans < 16 or resources.disposable_cups < 1:
            print("Sorry, not enough resources!")
        else:
            resources.water -= 250
            resources.coffee_beans -= 16
            resources.disposable_cups -= 1
            resources.money += 4
            print("I have enough resources, making you a coffee!")

    def buy_latte(resources):
        if resources.water < 350 or resources.milk < 75 or resources.coffee_beans < 20 or resources.disposable_cups < 1:
            print("Sorry, not enough resources!")
        else:
            resources.water -= 350
            resources.milk -= 75
            resources.coffee_beans -= 20
            resources.disposable_cups -= 1
            resources.money += 7
            print("I have enough resources, making you a coffee!")

    def buy_cappuccino(resources):
        if resources.water < 200 or resources.milk < 100 or resources.coffee_beans < 12 or resources.disposable_cups < 1:
            print("Sorry, not enough resources!")
        else:
            resources.water -= 200
            resources.milk -= 100
            resources.coffee_beans -= 12
            resources.disposable_cups -= 1
            resources.money += 6
            print("I have enough resources, making you a coffee!")

    def fill(resources):
        print("Write how many ml of water you want to add:")
        resources.water += int(input("> "))
        print("Write how many ml of milk you want to add:")
        resources.milk += int(input("> "))
        print("Write how many grams of coffee beans you want to add:")
        resources.coffee_beans += int(input("> "))
        print("Write how many disposable cups you want to add:")
        resources.disposable_cups += int(input("> "))

    def take(resources):
        print(f"I gave you ${resources.money}")
        resources.money = 0


def main():
    machine = CoffeeMachine()
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input("> ")
        if action == "buy":
            machine.buy()
        elif action == "fill":
            machine.fill()
        elif action == "take":
            machine.take()
        elif action == "remaining":
            machine.print_state()
        elif action == "exit":
            break
        else:
            print("Invalid action")


if __name__ == "__main__":
    main()