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
