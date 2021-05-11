
import random

caracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ç']
ciclos = ['','!','@','#','$','%','&','?','*','=','>','<']

def retornaIndiceMensagem(mensagem):

    if len(mensagem) > 1:
        contadorLoop = 0
        indices = []
        contadorMsg = 0
        tamanhoMsg = len(mensagem)

        while True:

            if caracteres[contadorLoop] == mensagem[contadorMsg]:

                indices.append(contadorLoop)
                contadorMsg +=1
                contadorLoop = 0
                if len(indices) >= tamanhoMsg:
                    break
            else:
                contadorLoop +=1

        return indices

    else:
        for i in range(len(caracteres)):
            if mensagem == caracteres[i]:
                return i
 

def converteIndiceEmString(indice):
   
    cifrado = []
    for ind in indice:
        if ind >= 27:
            ciclo = int(ind/27)
            resto = ind%27
            cifrado.append(ciclos[ciclo])
            cifrado.append(caracteres[resto])
        else:
            cifrado.append(caracteres[ind])


    return cifrado

def retornaChave(tamanhoIndice):
    chave = []
    for r in range(tamanhoIndice):
        chave.append(random.randint(3,11))

    return chave   

def retornaIndiceCifrado(chave,indice):

    indiceCifrado = []
    c = 0
    for ind in indice:
        indiceCifrado.append(chave[c] * ind)
        c+=1

    return indiceCifrado

def cicloOuCaractere(caractere):

    for ciclo in ciclos:
        if caractere == ciclo:
            return 0
    return 1    

def decifraMensagem(chave,mensagem):
    
    indicePrimitivo = []
    c=0
    for i in range(len(mensagem)):

        if cicloOuCaractere(mensagem[c]) == 0:

            for indiceCiclo in range(len(ciclos)):
                if mensagem[c] == ciclos[indiceCiclo]:

                    indProxLetra = retornaIndiceMensagem(mensagem[c+1])
                    indicePrimitivo.append(indiceCiclo * 27 + indProxLetra)
                    c+=2
                    break

        elif cicloOuCaractere(mensagem[c]) == 1:

            indicePrimitivo.append(retornaIndiceMensagem(mensagem[c]))
            c+=1
        if c >= len(mensagem):
            break

    indiceDecifrado = []
    c=0
    for ind in indicePrimitivo:

        valor = int(ind/int(chave[c]))
        indiceDecifrado.append(valor)
        c+=1

    return indiceDecifrado

def validaChave(chave,mensagem):

    mensagemSemCiclos = []

    for c in range(len(mensagem)):

        for char in caracteres:

            if mensagem[c] == char:
                mensagemSemCiclos.append(mensagem[c])

    chaveConvertida = chave.split('.')

    tamanhoChave = len(chaveConvertida)
    tamanhoMensagem = len(mensagemSemCiclos)

    if tamanhoChave != tamanhoMensagem:

        return False

    elif tamanhoChave == tamanhoMensagem:

        return chaveConvertida
    else:

        return False    

    if chave == None:

        print( "chave invalida")
        return False