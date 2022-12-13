import PySimpleGUI as sg
def janela_login():
    sg.theme("Reddit")

    tamanho_texto = 6
    tamahno_input = 20

    captura_dados_layout = [
        [sg.Text("Usuario", size=tamanho_texto), sg.Input(key="usuario", size=tamahno_input)],
        [sg.Text("Senha", size=tamanho_texto), sg.Input(key="senha", size=tamahno_input)]
    ]

    btn_layout = [[sg.Button("Entrar", size=10)]]


    layout = [


        [sg.Column([[sg.Text('', size=(0, 0))]])],
        [sg.Column([[sg.Text('', size=(30, 0))]]), sg.Text("BEM VINDO", font=("Helvetica", 20, "italic"))],
        [sg.Column([[sg.Text('', size=(0, 4))]])],
        [captura_dados_layout],
        [sg.Column([[sg.Text('',size=(4, 0))]]), sg.Column(btn_layout)]


    ]



    return sg.Window("Login", layout, finalize=True, size=(640, 400))

def janela_pedido():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Fazer Pedido")],
        [sg.Checkbox("Pizza Pepperoni", key="pizza1"), sg.Checkbox("Pizza c/ Catupiry", key="pizza2")],
        [sg.Button("Voltar"), sg.Button("Fazer Pedido")]
    ]
    return sg.Window("Montar Pedido", layout, finalize=True)