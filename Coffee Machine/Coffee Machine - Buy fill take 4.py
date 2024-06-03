class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans} g of coffee beans")
        print(f"{self.disposable_cups} disposable cups")
        print(f"${self.money} of money")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        choice = int(input("> "))
        if choice == 1:
            self.buy_espresso()
        elif choice == 2:
            self.buy_latte()
        elif choice == 3:
            self.buy_cappuccino()
        else:
            print("Invalid choice")

    def buy_espresso(self):
        if self.water < 250 or self.coffee_beans < 16 or self.disposable_cups < 1:
            print("Sorry, not enough resources!")
        else:
            self.water -= 250
            self.coffee_beans -= 16
            self.disposable_cups -= 1
            self.money += 4
            print("I have enough resources, making you a coffee!")

    def buy_latte(self):
        if self.water < 350 or self.milk < 75 or self.coffee_beans < 20 or self.disposable_cups < 1:
            print("Sorry, not enough resources!")
        else:
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.disposable_cups -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")

    def buy_cappuccino(self):
        if self.water < 200 or self.milk < 100 or self.coffee_beans < 12 or self.disposable_cups < 1:
            print("Sorry, not enough resources!")
        else:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.disposable_cups -= 1
            self.money += 6
            print("I have enough resources, making you a coffee!")

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water += int(input("> "))
        print("Write how many ml of milk you want to add:")
        self.milk += int(input("> "))
        print("Write how many grams of coffee beans you want to add:")
        self.coffee_beans += int(input("> "))
        print("Write how many disposable cups you want to add:")
        self.disposable_cups += int(input("> "))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


def main():
    machine = CoffeeMachine()
    machine.print_state()
    print("Write action (buy, fill, take):")
    action = input("> ")
    if action == "buy":
        machine.buy()
    elif action == "fill":
        machine.fill()
    elif action == "take":
        machine.take()
    else:
        print("Invalid action")
    machine.print_state()


if __name__ == "__main__":
    main()