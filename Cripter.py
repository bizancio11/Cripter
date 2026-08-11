import random
import zlib
import sys
import os

def cript():
    r1 = random.randint(1, 50)
    r2 = input("Mensaje a cifrar: ")
    destino = input("Nombre del archivo para guardar (Deja vacío para mostrar en pantalla): ").strip()
    
    # Proceso de cifrado matemático y compresión
    binario_compacto = "".join(format(ord(c), "08b") for c in r2)
    numero_binario = int(binario_compacto, 2)
    resultado_matematico = numero_binario * r1
    r4 = format(resultado_matematico, "b")
    r5 = zlib.compress(r4.encode('utf-8'))
    
    clave_codificada = zlib.compress(str(r1).encode('utf-8'))
    largo_clave = len(clave_codificada).to_bytes(4, 'big')
    
    # Unimos los bytes del resultado cifrado completo
    datos_totales = largo_clave + clave_codificada + r5
    
    if destino:
        if not destino.endswith(".cript"):
            destino += ".cript"
        with open(destino, "wb") as f:
            f.write(datos_totales)
        print(f"\nArchivo guardado exitosamente como: {destino}")
    else:
        # Si no hay archivo, representamos los bytes en formato hexadecimal legible para copiar y pegar
        print("\n=== Mensaje Cifrado (En Memoria) ===")
        print(f"Texto cifrado (Hex): {datos_totales.hex()}")

def decript():
    entrada = input("Introduce el nombre del archivo .cript O el código Hex para descifrar: ").strip()
    
    datos_completos = None
    
    # 1. Intentar leer como archivo si existe en el disco
    if os.path.exists(entrada):
        with open(entrada, "rb") as f:
            datos_completos = f.read()
    elif os.path.exists(entrada + ".cript"):
        with open(entrada + ".cript", "rb") as f:
            datos_completos = f.read()
    else:
        # 2. Si no es un archivo, intentar tratarlo directamente como datos cifrados en memoria (Hex)
        try:
            datos_completos = bytes.fromhex(entrada)
        except ValueError:
            print("\nError: No se encontró el archivo ni se reconoció un código Hex válido.")
            return

    try:
        # Proceso de descifrado
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
        print(f"\nError al descifrar: {e}. Asegúrate de ingresar el archivo o código correcto.")

def menu():
    print("=== CRYPTER FILE & MEMORY MENU ===")
    print("1. Cifrar (Guardar en archivo o ver en pantalla)")
    print("2. Descifrar (Leer archivo o pegar código)")
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
    while True:
        menu()
        print("\n" + "="*30 + "\n")
