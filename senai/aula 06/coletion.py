1#-----coleção em python-----
lista = ["Senai", True, 22, 3.5]
print(lista)
print(type(lista))
print(lista[1])
print(len(lista))
del lista[2]
print(lista)
lista.insert(2, "SENAI")
lista.insert(2, "SENAI")
lista.append("Eduane")
lista.append("Senai")




#----------Tupla----------
tupla = ("SENAI", False, 24, 1.73)
print(tupla)
print(type(tupla))
print(tupla[3])



#--------Dicionario------
dicionario = {"nome": "Senai", "logica": True, "numero":2, "n":2.75}
print(dicionario)
print(type(dicionario))
print(dicionario.update({"novo": "SENAI"}))
del dicionario["nome"]

for chave in dicionario.keys():
    print(chave, "->",dicionario[chave])

#-------Conjunto--------

conjunto = {"Senai", True, 10, 2.1}
print(conjunto)
print(type(conjunto))
print(conjunto[1])
conjunto.remove(1)
conjunto.remove("Clodoaldo")
conjunto.discard(2)