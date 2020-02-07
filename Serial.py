# para usar esse comando é necessário instalar o módulo pyserial-3.4-py2.py3-none-any.whl (wheel)
# para instalar, logo após fazer o download devemos usar o seguinte comando no cmd DOS
#pip install some-package.whl, o PIP é p gerenciador de instalação dos módulos do python

import serial #importado o módulo serial

# ser = serial.Serial('/dev/ttyUSB0', 9600) para o linux especificando o baud rate 9600
ser = serial.Serial("COM3")#verificar se para o windows é assim
# assin não funciona ser = serial.Serial("USB4")
#ser.write('5') usado para python v2
ser.write(b'5') #Prefixo b necessario se estiver utilizando Python 3.X

ser.read() #leitura da serial
