import ctypes

attribute_hide = 0x02

#dll que manipula no sistema operacional e o torna oculta
turn_back = ctypes.windll.kernel32.SetFileAtrributesW('ocultar.txt', attribute_hide) 
if turn_back:
    print('Arquivo foi ocultado!')
else:
    print('Arquivo não foi ocultado!')