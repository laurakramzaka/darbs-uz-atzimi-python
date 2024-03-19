#vienkārši piepildīt list ar elementiem
saraksts = list(range(0,11,2))
print(saraksts)

print("\t")

#enumerate - parāda indeksus tuple formā
vards = "pasaule"
for i in enumerate(vards):
    print(i)

print("\t")

#atpakot tuples
for index,burts in enumerate(vards):
    print(index)
    print(burts)
    print("\n")

#izmanto zip - sapako vairākus list kā tuple
my_list = [1,2,3]
my_list2 = ["a","b","c"]
for i in zip(my_list2,my_list):
    print(i)

print("\t")

my_list3 = [2.3,13.4,3.5]
for i in zip(my_list2,my_list,my_list3):
    print(i)

print("\t")

#saliek visu vienā list
print(list(zip(my_list2,my_list,my_list3)))

print("\t")

#izmanto in, lai noskaidrotu vai objektā ir atrodams meklētais??
print("x" in [1,2,3])
print(2 in [1,2,3])
print("a" in "pasaule")
print("atslega2" in {"atslega1":256})
d= {"atslega1":256}
print(256 in d.keys())
print(256 in d.values())

#min un max
my_list = [10,20,15,3.9,45]
print(min(my_list))
print(max(my_list))