#creating a word problem revolving with a cube
#Yusef Bayyat
#8/6/20
#Area of one side equals to 9
from math import *

def main():
    print("Omar is writing a pamphlet on steps to solving a Rubkik's cube. To explain to the clase \n and give reference he is trying to calculate the surface area and volume of the cube.")
    print("")
    print("He needs your help by providing him the amount of sides a Rubik's cube and the area of one side of the cube.")
	print("")
    amountOfSides = int(input("Enter the amount of sides a Rubik's cube has."))
    areaOfOneSide = int(input("Enter the area of one side of a Rubik's cube."))
    print("The amount of sides a Rubik's cube has is")
    print(str(+amountOfSides))
    print("The area of one side of a Rubik's cube is")
    print(str(+areaOfOneSide))
    print("With the new information you helped Omar get, he can now conclude that the surface area of a Rubik's cube is.")
    print(amountOfSides * areaOfOneSide)
    lengthOfCube = int(input("Enter the length of one side of the cube"))
    print("The length of one side of the cube is")
    print(str(+lengthOfCube))
    print("know that Omar has figured out the length of the Rubik's cube, he can now solve for the volume.")
    print("The volume of a Rubik's cube is.")
    print(pow(+lengthOfCube,3))

main()
