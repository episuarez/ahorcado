import os

from ahorcado import Ahorcardo

os.system("cls");

juego = Ahorcardo();

while juego.puedojugar():
    os.system("cls");

    print(juego.obtener_turno());
    
    print("[0] ¿Preguntar por una letra?");
    print("[1] ¿Quieres resolver?");
    opcion = input("Dime que eliges: ");

    if opcion == "0":
        letra = input("Dime una letra: ").lower();
        print(juego.comprobar_letra(letra));
    elif opcion == "1":
        print(juego.intentar_resolver(input("Dime la respuesta: ").lower()));
    else:
        print("Dime una opción correcta...");

    os.system("pause");

print(juego.mensaje_final());
