import os


videos = ['.mp4', '.mkv', '.avi', '.mov', '.vob', '.wav', '.mpeg', '.mpg', '.webm', '.wmv']
imagem = ['.png', '.jpg', '.jpeg', '.gif', '.tiff', '.svg', '.ico', '.icon', '.psd', '.raw', '.webp', '.psdx', '.psb']
compactados = ['.rar', '.zip', '.7z']
documentos = ['.docm', '.doc', '.txt', '.pdf', '.xls', '.xlsx', '.ppt', '.docx', '.pptx', '.odt', '.ods', '.odp', '.draw', '.csl', '.xps']
audio = ['.wav', '.mp3', '.ogg', '.aiff', '.aif', '.m4a', '.wma']
fontes = ['.ttf', '.otf', '.woff', '.ttc', '.eot']
executaveis = ['.exe', '.bat', '.app', '.msi', '.tmp', '.chm']




def organize(path) -> None:
    lista_arquivos = os.listdir(path)
    for arquivo in lista_arquivos:
        if os.path.isdir(f'{path}/{arquivo}'):
            pass
        else:
            extensao = os.path.splitext(arquivo)[1]
            if extensao in videos:
                try:
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Videos/{arquivo}')
                    print('sucesso')
                except FileNotFoundError:
                    os.mkdir('/home/elisson/Downloads/Videos')
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Videos/{arquivo}')
                    print('sucesso, criei a pasta Videos e movi o arquivo!')
                else:
                    pass
                
            elif extensao in imagem:
                try:
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Imagens/{arquivo}')
                    print('sucesso')
                except FileNotFoundError:
                    os.mkdir('/home/elisson/Downloads/Imagens')
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Imagens/{arquivo}')
                    print('sucesso, criei a pasta Imagens e movi o arquivo!')
            elif extensao in compactados:
                try:
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Compactados/{arquivo}')
                    print('sucesso')
                except FileNotFoundError:
                    os.mkdir('/home/elisson/Downloads/Compactados')
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Compactados/{arquivo}')
                    print('sucesso, criei a pasta Compactados e movi o arquivo!')
            elif extensao in documentos:
                try:
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Documentos/{arquivo}')
                    print('sucesso')
                except FileNotFoundError:
                    os.mkdir('/home/elisson/Downloads/Documentos')
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Documentos/{arquivo}')
                    print('sucesso, criei a pasta Documentos e movi o arquivo!')
            elif extensao in audio:
                try:
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Audios/{arquivo}')
                    print('sucesso')
                except FileNotFoundError:
                    os.mkdir('/home/elisson/Downloads/Audios')
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Audios/{arquivo}')
                    print('sucesso, criei a pasta Audios e movi o arquivo!')
            elif extensao in fontes:
                try:
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Fontes/{arquivo}')
                    print('sucesso')
                except FileNotFoundError:
                    os.mkdir('/home/elisson/Downloads/Fontes')
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Fontes/{arquivo}')
                    print('sucesso, criei a pasta Fontes e movi o arquivo!')
            elif extensao in executaveis:
                try:
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Executaveis/{arquivo}')
                    print('sucesso')
                except FileNotFoundError:
                    os.mkdir('/home/elisson/Downloads/Executaveis')
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Executaveis/{arquivo}')
                    print('sucesso, criei a pasta Executaveis e movi o arquivo!')
            else:
                try:
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Outros/{arquivo}')
                    print('sucesso')
                except FileNotFoundError:
                    os.mkdir('/home/elisson/Downloads/Outros')
                    os.rename(f'/home/elisson/Downloads/{arquivo}', f'/home/elisson/Downloads/Outros/{arquivo}')
                    print('sucesso, criei a pasta Outros e movi o arquivo!')
    return True
