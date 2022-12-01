import PySimpleGUI as sg
from utils import organize

sg.theme('Default1')

layout = [
    [sg.Text('Bem-vindo ao Organizador de Arquivos!', justification='center', size=(50,4))],
    [sg.Push(),sg.FolderBrowse(key='-PATH-', button_text='Procurar Pasta'), sg.Push()],
    [sg.Push(), sg.Button('Organizar arquivos', key='-SUBMIT-', button_color='#04a900', mouseover_colors='#04e000'), sg.Push()]
]

window = sg.Window('Organizador de pastas', layout, size=(500, 200))


while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == '-SUBMIT-':
        if organize(values['-PATH-']):
            sg.Popup('Pasta organizada com sucesso!')
        
    window.close()
