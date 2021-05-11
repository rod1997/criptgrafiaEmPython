import criptografia

print("\n======================================================================================================")
print("||                                                                                                  ||")
print("||                                                                                                  ||")
print("||                     ------------------ VECTOR CRIPTOGRAFIA -------------                         ||")
print("||                                                                                                  ||")
print("||                                                                                                  ||")
print("======================================================================================================\n\n")


print("DIGITE ALGUMA AÇÃO:\n")
print("[0] Criptografar")
print("[1] Descriptografar")
print("[2] Sair")

acao=int(input())

if acao == 2:
    exit()

if acao == 0:

    msg = str(input("mensagem: "))

    indiceMsg = criptografia.retornaIndiceMensagem(msg)
    chave = criptografia.retornaChave(len(indiceMsg))
    indiceCifrado = criptografia.retornaIndiceCifrado(chave,indiceMsg)
    mensagemCifrada = criptografia.converteIndiceEmString(indiceCifrado)

    print("\nChave: ",chave)
    print("Mensagem cifrada: ","".join(mensagemCifrada))
    print("\n Copie as informaçoẽs.")

elif acao == 1:

    mensagem = str(input("Mensagem cifrada: "))
    chaveString = str(input('\nChave: '))

    chave = criptografia.validaChave(chaveString,mensagem)

    if chave == False:

        while True:

            print("chave invalida! digite novamente")
            chaveString = str(input('\nChave: '))
            chave = criptografia.validaChave(chaveString,mensagem)

            if chave != False | chave == None:
                break


    indiceDecifrado = criptografia.decifraMensagem(chave,mensagem)
    msgDecifrada = criptografia.converteIndiceEmString(indiceDecifrado)

    print("\nMensagem decifrada com sucesso!\n","".join(msgDecifrada))

else:
    exit()
