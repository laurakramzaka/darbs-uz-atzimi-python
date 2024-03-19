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