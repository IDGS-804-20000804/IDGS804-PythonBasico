miDiccionario={"Matricula":20000804, "Apellidos":"Ornelas"}

print(miDiccionario["Apellidos"])
miDiccionario["Materia"]="DWP"
print(miDiccionario)
miDiccionario["Matricula"]=20000000
print(miDiccionario)


del miDiccionario["Apellidos"]
print(miDiccionario)
