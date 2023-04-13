#TASK2
import math

def Area():
    shapes = ["square", "rectangle", "circle", "triangle"]
    Shape = input("Enter shape of object : ")
    if Shape == "square":
        length = float(input("Enter length of one side of the square : "))
        area = length ** 2
        message = "The area of the square is {} ".format(area)
        print(message)

    elif Shape == "rectangle":
        length = float(input("Enter length of the rectangle : "))
        width = float(input("Enter width of the rectangle : "))
        area = length * width
        message = "The area of the rectangle is {} ".format(area)
        print(message)

    elif Shape == "circle":
        radius = float(input("Enter radius of the circle : "))
        area = math.pi * radius ** 2
        message = "The area of the circle is {} ".format(area)
        print(message)

    elif Shape == "triangle":
        base = float(input("Enter base of the triangle : "))
        height = float(input("Enter height of the triangle : "))
        area = 0.5 * base * height
        message = "The area of the triangle is {} ".format(area)
        print(message)

    else:
        print("Invalid shape entered.")

Area()


#TASK3
for z in range (0, 20):
    while z % 2 != 0:
        print(z, end=" ")
        break

