import os

lista = os.listdir('/home/elisson/Downloads/Outros/')
for arquivo in lista:
    if os.path.isdir(f'/home/elisson/Downloads/Outros/{arquivo}'):
        print('sim')
    else:
        print('nao')