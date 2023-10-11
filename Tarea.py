meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "Causa":" Una jerga que se usa para referirse a uno compañero o un amigo",
            "Pituco": "Se utiliza para referirse a alguien que tiene mucha plata y no le importa derrochar",
            "Delirar": "Significa cuando una persona esta muy borracha"}
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ") 
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    significado = input("ingresa el significado de la palabra")
    meme_dict[word] = significado
