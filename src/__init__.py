from verificacoes import *
import atribui_variaveisA_janelas as avj



while True:
    window, event, val = sg.read_all_windows()
    if fechar_janela(event):
        break

    if botao_continuar_janela1_pressionado(window, event):
        avj.janela2 = avj.janela_pedido()
        avj.janela1.hide()

    if voltar_para_janela1(window, event):
        avj.janela2.hide()
        avj.janela1.un_hide()
    if botao_FazerPedido_janela2_pressionado(window, event):
        escolha = verifica_checkbox_selecionada(val)
        exibe_pulpop(escolha)

