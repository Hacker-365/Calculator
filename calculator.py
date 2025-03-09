import math
import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        print("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   
        print("Good Afternoon Sir!") 

    else:
        speak("Good Evening Sir!")  
        print("Good Evening Sir!")

speak("I am your hi-tech calculator sir. Please, tell me how can I help you?")
print("I am your hi-tech calculator sir. Please, tell me how can I help you?")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def factorial(n):
    if n < 0:
        return "Error! Factorial of negative number doesn't exist."
    return math.factorial(n)

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

def square_root(n):
    return math.sqrt(n)

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def cube_root(n):
    return n ** (1 / 3)

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

while True:
    def main():
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Factorial")
        print("6. Area and Perimeter of Rectangle")
        print("7. Area and Perimeter of Triangle")
        print("8. Area and Perimeter of Square")
        print("9. Square and Square Root")
        print("10. Cube and Cube Root")
        print("11. Area and Circumference of Circle")
        
        choice = input("Enter choice (1-11): ")
        
        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))
            
        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", subtract(a, b))
            
        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", multiply(a, b))
            
        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", divide(a, b))
            
        elif choice == '5':
            n = int(input("Enter a number: "))
            print("Result:", factorial(n))
            
        elif choice == '6':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            print("Area:", rectangle_area(length, width))
            print("Perimeter:", rectangle_perimeter(length, width))
            
        elif choice == '7':
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            c = float(input("Enter side c: "))
            height = float(input("Enter height: "))
            print("Area:", triangle_area(b, height))
            print("Perimeter:", triangle_perimeter(a, b, c))
            
        elif choice == '8':
            side = float(input("Enter side length: "))
            print("Area:", square_area(side))
            print("Perimeter:", square_perimeter(side))
            
        elif choice == '9':
            n = float(input("Enter a number: "))
            print("Square:", square(n))
            print("Square Root:", square_root(n))
            
        elif choice == '10':
            n = float(input("Enter a number: "))
            print("Cube:", cube(n))
            print("Cube Root:", cube_root(n))
            
        elif choice == '11':
            radius = float(input("Enter radius: "))
            print("Area:", circle_area(radius))
            print("Circumference:", circle_circumference(radius))
            
        else:
            print("Invalid input. Please enter a number between 1 and 11.")

    if __name__ == "__main__":
        main()
        speak()
        wishMe()
