source ins/bin/activate
# 1. Asegúrate de instalar PyInstaller para tu entorno de Python 3
pip3 install pyinstaller

# 2. Muévete a la carpeta de tu proyecto
cd ~/Escritorio/Python/Crypter

# 3. Compila el script en un único archivo ejecutable nativo
pyinstaller --onefile --name=Cripter Cripter.py

