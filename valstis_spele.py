
from random import randint


valstis = {
"Latvija": "Rīga",
"Lietuva": "Viļņa",
"Igaunija": "Tallina",
"Francija": "Parīze",
"Vācija": "Berlīne",
}

#valstis_saraksts=["Latvija", "Lietuva", "Igaunija", "Francija", "Vācija"]

#atslegu_list = list((valstis_saraksts)) 
#print(atslegu_list) mans variants

atslegas= list(valstis.keys())
#print(atslegas)



skaits = 0
pareizas_atbildes = 0

while True:
    gadijums= randint(0, len(atslegas)-1)

    print("\t")


    galvaspilseta= input(f"Kas ir {atslegas[gadijums]}s galvaspilsēta?")
    if galvaspilseta.lower()=="q":
        print("Paldies par spēli!🤗")
        break
    elif galvaspilseta.capitalize()==valstis[atslegas[gadijums]]:
         print("Pareizi!😄")
         pareizas_atbildes += 1

    else:
        print(f"Nepareizi!💀 Pareizā atbilde: {valstis[atslegas [gadijums]]}")
    skaits += 1

    print("\t")

    print(f"Tu pareizi atbildēji uz {pareizas_atbildes} no {skaits} jautājumiem!")