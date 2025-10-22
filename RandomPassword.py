import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890▧"
length = int(input("Cual es la longiud de la contraseña"))
password = ""
if length <= 5 and length >= 1:
    print("Tu contraseña es demasiado corta")
elif length > 5:
    for i in range(length):
        password += random.choice(characters)
    print(f"Tu contraseña es {password}")
