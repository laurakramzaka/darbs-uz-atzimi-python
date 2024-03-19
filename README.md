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
