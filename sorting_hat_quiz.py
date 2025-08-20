print("-------------------SORTING HAT---------------")
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1. Do you like Dawn or Dusk")
print("1. Dawn")
print("2. Dusk")
choice = input("enter choice 1 or 2 :")
if choice == '1':
 Gryffindor = Gryffindor+1  
 Ravenclaw = Ravenclaw +1
elif choice == '2':
 Hufflepuff = Hufflepuff+1 
 Slytherin = Slytherin+1
else:
  print("Wrong Input")
##  quetion 2 

print("Q2) When I’m dead, I want people to remember me as:  ")
print(" 1. The Good")
print(" 2. The Great")
print(" 3. The Wise")
print(" 4. The Bold ")
choice = input("enter choice (1,2,3 or 4) :")
if choice == '1': 
 Hufflepuff = Hufflepuff+2
elif choice == '2':
 Slytherin = Slytherin+2
elif choice == '3':
   Ravenclaw = Ravenclaw +2
elif choice == '4':
  Gryffindor = Gryffindor+2
else:
  print("Wrong Input")

## qUETION 3 
   
   
print("Q3) Which kind of instrument most pleases your ear?  ")
print(" 1. The violin")
print(" 2. The trumpet")
print(" 3. The piano")
print(" 4. The drum")
choice = input("enter choice (1,2,3 or 4) :")
if choice == '1': 
  Slytherin = Slytherin+4 
elif choice == '2':
  Hufflepuff = Hufflepuff+4
elif choice == '3':
   Ravenclaw = Ravenclaw +4
elif choice == '4':
  Gryffindor = Gryffindor+4
else:
  print("Wrong Input")

print(Gryffindor,
Ravenclaw,
Hufflepuff, 
Slytherin, )

if Gryffindor >= Ravenclaw and Gryffindor > Hufflepuff and Gryffindor >= Slytherin:
 print("Gryffindor has highest point")

elif Ravenclaw  >= Gryffindor and Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
 print(" Ravenclaw has highest point")
elif  Hufflepuff >= Gryffindor and Hufflepuff  >= Ravenclaw and Hufflepuff >= Slytherin:
 print("Hufflepuff has highest point")

elif  Slytherin >= Gryffindor and Slytherin >= Ravenclaw and Slytherin >= Hufflepuff:
 print("Slytherin has highest point")

else:
  print("error")