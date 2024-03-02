meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "RATIO": "Forma de burlarse de alguien cuando tienen mas respuestas que likes",
            "EZ": "Forma de burlarse de alguien principalmente por perder en algo",
            "BRO": "Se refiere a su amigo",
            "WTF": "Sorprenderse de algo",
            "CREEPYPASTA": "Una historia similar a una leyenda pero aterradora",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }
        
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print("El significado es:", meme_dict[word])
        print("=====================================================================")
        
    else:
        print("No se ha encontrado la palabra")
        print("=====================================================================")
