import PySimpleGUI as sg
import atribui_variaveisA_janelas as avj


def fechar_janela(event):
    return event == sg.WINDOW_CLOSED

def botao_continuar_janela1_pressionado(window, event):
    return window == avj.janela1 and event == "Continuar"


def voltar_para_janela1(window, event):
    return window == avj.janela2 and event == "Voltar"


def botao_FazerPedido_janela2_pressionado(window, event):
    return window == avj.janela2 and event == "Fazer Pedido"


def verifica_checkbox_selecionada(val):
    if val["pizza1"] == True and val["pizza2"] == True:
        return "pizza1/2"
    elif val["pizza1"] == True:
        return "pizza1"
    elif val["pizza2"] == True:
        return "pizza2"


def exibe_pulpop(escolha):
    if escolha == "pizza1/2":
        sg.popup("Foram solicitadas ( Pizza Pepperoni, Pizza c/ Catupiry )")

    elif escolha == "pizza1":
        sg.popup("Foram solicitadas ( Pizza Pepperoni )")

    elif escolha == "pizza2":
        sg.popup("Foram solicitadas ( Pizza c/ Catupiry )")
