#Héctor Sebastián Garrido López 1102123#
Condicion=True
while Condicion == True:
    vi=int(input("Ingrese valor del 1 al 10:"))
    for i in range(1,11):
        print(str(vi)+ "X" + str(i) + "="+ str(vi*i))
    print("Si desea continuar marcar 1, de lo contrario marque 2")
    v2=int(input("¿Desea generar otra tabla?"))
    if v2 == 20:
        Condicion=False