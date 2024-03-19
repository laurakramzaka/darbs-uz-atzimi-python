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