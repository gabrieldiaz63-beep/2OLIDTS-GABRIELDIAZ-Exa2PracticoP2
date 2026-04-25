cabeza = None

print("- 8 elementos -")
for i in range(8):
    valor = input(f"Ingresa el dato {i+1}: ")
    nodo = {"dato": valor, "siguiente": None}
    
    if cabeza == None:
        cabeza = nodo
    else:
        temp = cabeza
        while temp["siguiente"] != None:
            temp = temp["siguiente"]
        temp["siguiente"] = nodo

print("\n--- Lista actual ---")
temp = cabeza
while temp != None:
    print(temp["dato"])
    temp = temp["siguiente"]

print("\n- Borrar un elemento -")
eliminar = input("¿Cual quieres eliminar?: ")
actual = cabeza
previo = None

while actual != None:
    if actual["dato"] == eliminar:
        print("valor a borrar:", eliminar)
        if previo == None:
            cabeza = actual["siguiente"]
        else:
            previo["siguiente"] = actual["siguiente"]
        print("elemento eliminado")
        break
    previo = actual
    actual = actual["siguiente"]

print("\n- Lista final -")
temp = cabeza
while temp != None:
    print(temp["dato"])
    temp = temp["siguiente"]

input("\nPresiona Enter")
