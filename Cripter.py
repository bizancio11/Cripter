import random
import zlib
import sys
import os

def cript():
    r1 = random.randint(1, 50)
    r2 = input("Mensaje a cifrar: ")
    nombre_archivo = input("Nombre del archivo para guardar (sin extensión): ") + ".cript"
    
    binario_compacto = "".join(format(ord(c), "08b") for c in r2)
    numero_binario = int(binario_compacto, 2)
    resultado_matematico = numero_binario * r1
    r4 = format(resultado_matematico, "b")
    r5 = zlib.compress(r4.encode('utf-8'))
    
    clave_codificada = zlib.compress(str(r1).encode('utf-8'))
    largo_clave = len(clave_codificada).to_bytes(4, 'big')
    
    with open(nombre_archivo, "wb") as f:
        f.write(largo_clave + clave_codificada + r5)
        
    print(f"\nArchivo guardado exitosamente como: {nombre_archivo}")

def decript():
    nombre_archivo = input("Introduce el nombre del archivo .cript a descifrar: ")
    if not nombre_archivo.endswith(".cript"):
        nombre_archivo += ".cript"
        
    if not os.path.exists(nombre_archivo):
        print("\nEl archivo no existe.")
        return

    try:
        with open(nombre_archivo, "rb") as f:
            datos_completos = f.read()
            
        largo_clave = int.from_bytes(datos_completos[:4], 'big')
        clave_codificada = datos_completos[4:4+largo_clave]
        bytes_comprimidos = datos_completos[4+largo_clave:]
        
        clave_r1 = int(zlib.decompress(clave_codificada).decode('utf-8'))
        
        binario_modificado = zlib.decompress(bytes_comprimidos).decode('utf-8')
        numero_modificado = int(binario_modificado, 2)
        numero_original = numero_modificado // clave_r1
        binario_original = format(numero_original, "b")
        bloques_completos = binario_original.zfill((len(binario_original) + 7) // 8 * 8)
        bytes_lista = [int(bloques_completos[i:i+8], 2) for i in range(0, len(bloques_completos), 8)]
        mensaje_original = bytes(bytes_lista).decode('utf-8')
        
        print(f"\nMensaje recuperado: {mensaje_original}")
        print(f"Clave detectada internamente: {clave_r1}")
    except Exception as e:
        print(f"\nError al descifrar el archivo: {e}")

def menu():
    print("=== CRYPTER FILE MENU ===")
    print("1. Cifrar mensaje y guardar en .cript")
    print("2. Leer y descifrar archivo .cript")
    print("3. Salir")
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == "1":
        cript()
    elif opcion == "2":
        decript()
    elif opcion == "3":
        sys.exit()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()
