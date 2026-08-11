:: 1. Instala PyInstaller en Windows
pip install pyinstaller

:: 2. Navega hasta la carpeta donde copiaste tu Cripter.py
cd ruta\a\tu\carpeta\Crypter

:: 3. Compila el script en un único archivo ejecutable .exe de consola
pyinstaller --onefile --console --name=Cripter Cripter.py
