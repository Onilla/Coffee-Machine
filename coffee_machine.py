class Coffee:
    water = 400
    milk = 540
    beans = 120
    disposable_cups = 9
    money = 550

    def __init__(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            if action == "exit":
                break
            elif action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "remaining":
                self.remaining()
            else:
                self.take()

    def remaining(self):
        print(f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.disposable_cups} disposable cups
${self.money} of money""")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        coffee = input()
        if coffee == "1":
            if self.water < 250 or self.beans < 16 or self.disposable_cups < 1:
                print("Sorry, not enough water!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.disposable_cups -= 1
        elif coffee == "2":
            if self.water < 350 or self.milk < 75 or self.beans < 20 or self.disposable_cups < 1:
                print("Sorry, not enough water!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.disposable_cups -= 1
        elif coffee == "3":
            if self.water < 200 or self.milk < 100 or self.beans < 12 or self.disposable_cups < 1:
                print("Sorry, not enough water!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.disposable_cups -= 1
        else:
            pass

    def fill(self):

        print("Write how many ml of water you want to add:")
        water_add = int(input())
        print("Write how many ml of milk you want to add:")
        milk_add = int(input())
        print("Write how many grams of coffee beans you want to add: ")
        beans_add = int(input())
        print("Write how many disposable cups you want to add: ")
        disposable_cups_add = int(input())
        self.water += water_add
        self.milk += milk_add
        self.beans += beans_add
        self.disposable_cups += disposable_cups_add

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


cofe = Coffee()
