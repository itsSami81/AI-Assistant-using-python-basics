
from datetime import datetime
from colorama import init, Fore, Style
import requests

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT)
print("-" * 45)
print(f"🤖 Assistant : ALEXA")
print(f"🚀 Version   :1.0")
print("-" * 45)

#--shows current time
def show_time():
        current_time = datetime.now()
        print(Fore.YELLOW + f"🕒 Current Time : {current_time.strftime('%I:%M:%S %p')}")

#---Calculator 
def calculator():
        a = int(input("Enter 1st number : "))
        op = input("Enter operator (+,-,*,/) : ")
        b = int(input("Enter 2nd number : "))

        if op == "*":
            print(Fore.GREEN + f"Result : {a*b}")

        elif op == "+":
            print(Fore.GREEN + f"Result : {a+b}")

        elif op == "-":
            print(Fore.GREEN + f"Result : {a-b}")

        elif op == "/":
            if b != 0:
                print(Fore.GREEN + f"Result : {a/b}")
            else:
                print(Fore.RED + "Division by zero is not allowed!")

        else:
            print(Fore.RED + "Invalid Operator!")

#---Shows weather 
def show_weather():
    city = input(Fore.BLUE + "Enter city name: ")

    api_key ="ad342457a2294bfdf3c85d2c5b0c97e0"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print(Fore.CYAN + "\n====== WEATHER REPORT ======")
        print(Fore.GREEN + f"🌡 Temperature : {temperature}°C")
        print(Fore.YELLOW + f"💧 Humidity    : {humidity}%")
        print(Fore.MAGENTA + f"☁ Condition   : {condition.title()}")
        print(Fore.CYAN + "============================\n")

    else:
        print(Fore.RED + "❌ City not found!")

#--number guessing game
import random
def guess_number():
    print(Fore.YELLOW+"Number Guessing Game started......\n")
    number = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number (1-10): "))
        if guess == number:
            print("🎉 Correct! You Won.")
            break
        elif guess > number:
            print("📉 Your number is High!")
        else:
            print("📈 Your number is Low!")


#-------Main loop-----
while True:
    n = input(Fore.BLUE + "\n🤖 Enter a command : ").lower()

    if n == "hello":
        print(Fore.GREEN + "Hello! Welcome 😊 How can I help you?")

    elif n == "introduce yourself":
        print(Fore.CYAN + "My name is ALEXA 😎, an AI Assistant")

    elif n == "do you know sami":
        print(Fore.GREEN + "Yes! Sami is my Boss ")

    elif n == "friends of sami":
        print(Fore.YELLOW + "Ali and ???")

    elif n == "tell me time right now":
        show_time()

    elif n=="make a joke":
        import pyjokes
        joke=pyjokes.get_joke()
        print(Fore.LIGHTGREEN_EX+joke+"😁")

    elif n == "run calculator":
        calculator()

    elif n == "tell me weather":
        show_weather()

    elif n == "open youtube":
        import webbrowser
        webbrowser.open("https://www.youtube.com")
    elif n == "lets play a game":
        guess_number()

    elif n == "exit":
        print(Fore.MAGENTA + "👋 Goodbye! Have a nice day.")
        break

    else:
        print(Fore.RED + "❌ Sorry! Invalid command.")