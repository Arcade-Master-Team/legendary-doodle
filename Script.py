meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AFK": "Acronimo para -Away From Keyboard-",
            "XD": "Una forma de reirse por chat la cual imita una cara riendose",
            "AGGRO": "ponerse agresivo/enojado",
            "Trollear": "Provocar o molestar en redes sociales o chats" #Idea original de https://github.com/yordi210895-sketch/cuphead/tree/main
            }

print("Bienvenido al diccionario de memes")
print("En el siguiente apartado podrás buscar una palabra en el diccionario")
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("La palabra no está en la lista")
