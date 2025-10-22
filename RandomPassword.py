import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890▧"
lenght = int(input("Cual es la longiud de la contraseña"))
password = ""
for i in range(lenght):
    password += random.choice(characters)
print(f"Tu contraseña es {password}")
