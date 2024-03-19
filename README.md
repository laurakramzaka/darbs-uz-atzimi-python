# darbs-uz-atzimi-python

def atminet_vardus(dziesmas_teksts, pareizie_vardi):
    vardi = dziesmas_teksts.split()
    trukstosie_vardi = [vards for vards in vardi if '_' in vards]
    
    if len(trukstosie_vardi) != len(pareizie_vardi):
        print("Kļūda: Trūkstoso vārdu skaits nesakrīt ar atbilžu skaitu.")
        return
    
    for i, vards in enumerate(trukstosie_vardi):
        print("Trūkstošais vārds #{} ir:".format(i+1), vards.replace('_', ''))
        minejums = input("Ievadiet savu minējumu: ")
        if minejums.lower() == pareizie_vardi[i].lower():
            print("Apsveicu, jūs pareizi atminējāt vārdu!")
        else:
            print("Diemžēl tas nav pareizais vārds. Mēģiniet vēlreiz.")
            return
    print("Jūs pareizi atminējāt visus vārdus!")

dziesmas_teksts = "Es ________ brīnos, kas ________ varētu būt"
pareizie_vardi = ["parasti", "tas"]

atminet_vardus(dziesmas_teksts, pareizie_vardi)




def atminet_vardu(dziesmas_teksts, pareizais_vards):
    vardi = dziesmas_teksts.split()
    for i, vards in enumerate(vardi):
        if '_' in vards:
            print("Trūkstošais vārds ir:", vards.replace('_', ''))
            minejums = input("Ievadiet savu minējumu: ")
            if minejums.lower() == pareizais_vards.lower():
                print("Apsveicu, jūs pareizi atminējāt vārdu!")
                return
            else:
                print("Diemžēl tas nav pareizais vārds. Mēģiniet vēlreiz.")
                return
    print("Nav trūkstoša vārda šajā dziesmas tekstā.")

dziesmas_teksts = "Es ________ brīnos, kas tas varētu būt"
pareizais_vards = "parasti"

atminet_vardu(dziesmas_teksts, pareizais_vards)



Protams, šeit ir vienkāršots algoritma apraksts:

1. Sadala dziesmas tekstu pa vārdiem.
2. Atrodot vārdus ar "_", tos identificē kā trūkstošos vārdus.
3. Ja trūkstošo vārdu skaits atbilst pareizo vārdu skaitam, programma turpina.
4. Lai spēlētājs varētu minēt, tiek izvadīti trūkstošo vārdu numuri un burtu skaits.
5. Spēlētājam tiek pieprasīts ievadīt minējumu.
6. Pārbauda, vai minējums sakrīt ar pareizo vārdu.
7. Ja minējums ir pareizs, izvada apsveikuma ziņojumu.
8. Ja visi vārdi ir pareizi atminēti, izvada paziņojumu par veiksmīgu atminēšanu.
https://s1vsk-my.sharepoint.com/:w:/g/personal/lk2802_s1vsk_lv/EeLntCNlrgVCioOdoLdLCzsBHCbRLafa7nmLyHv1uCEEvw?e=87ejCj
from random import randint





def atminet_vardu(dziesmas_teksts, pareizais_vards):
    vardi = dziesmas_teksts.split()
    for i, vards in enumerate(vardi):
        if '_' in vards:
            print("Un es skrienu, skrienu vēl, man vēl ________", vards.replace('_', ''))
            minejums = input("Ievadiet savu minējumu: ")
           
            print("Liku ____ zem akmeņa", vards.replace('_', ''))
            minejums = input("Ievadiet savu minējumu: ")

            if minejums.lower() == pareizais_vards.lower():
                print("Pareizi!😎")
                return
            else:
                print("Nepareizi👎")
                return
 

dziesmas_teksts = "Un es skrienu, skrienu vēl, man vēl ________"
pareizais_vards = "jāpaspēj"

dziesmas_teksts = "Liku ____ zem akmeņa"
pareizais_vards = "bēdu"      

atminet_vardu(dziesmas_teksts, pareizais_vards)



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



    # # importē bibliotēkas
from random import randint,shuffle
 
# print(randint (1,100))
# saraksts = [1,2,3,4,5]
# shuffle(saraksts)
# print(saraksts)
 
# # metode try except - parbauda vai tiek ievadīts prasītais
 
# while True:
#     x = input("ievadi veselu skaitli: ")
#     try:
#         if int(x):
#             break
#     except:
#             print(f"{x} nav vesels skaitlis")
 
# print(f"tu ievadiji {x}")
 
 
# # pārbauda vai tiek ievadīts prasītais
 
# x = input("ievadi 1,2 vai 3: ")
# while x not in ["1", "2", "3"]:
#     x = input("ievadi 1,2 vai 3: ")
 
#---------------------------------------
print("\t")

glazites = ["🍸","🍸","🍪"]
print(*glazites)
 
def sajauc(glazites):
    shuffle(glazites)
    return glazites

#print(sajauc(glazites))

#pajautā minējumu
def mans_minejums():
    minejums = ""
    while minejums not in ["1","2","3"]:
        minejums = input("Kurā glāzītē ir bumbiņa (ievadi 1,2 vai 3)?: ")
    return int(minejums)

#print(mans_minejums())

#pārbauda vai minējums pareizs
def parbaudi_minejumu(glazites, minejums):
    if glazites[minejums-1]=="🍪":
        print("Uzvarēji! 🏆")
    else:
        print("Zaudēji... 😔")
        print(*glazites)


#pa soļiem izsauc visas funkcijas
#sajauc glāzītes
sajauktais = sajauc(glazites)

#spēlētāju minējums
speletaja_minejums = mans_minejums()


#parbauda spēlētāju minējumu
parbaudi_minejumu(sajauktais,speletaja_minejums)
