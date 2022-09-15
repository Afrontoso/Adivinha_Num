mediana=int()
resp=str()
""" cont=0 """
listaN=[]

print("Escolha um intevalo de números:")

#Coleta dados do usuário
nMin=int(input("Qual é o menor número do seu intervalo?\n"))
nMax=int(input("Qual é o maior número do seu intervalo?\n"))

# caso o usuario insira dados controversos
if nMin>nMax:
    troca=int()
    nMin=troca
    nMax=nMin
    troca=nMax

#Quantidade de números
quantN=nMax-nMin

#adiciona números na lista
""" while cont<nMax:
    listaN.append(nMin)
    nMin+=1
    cont+=1 """
for i in range(nMin, nMax+1, 1):
    listaN.append(i)

#Posição central
if quantN%2!=0:
    quantN-=1
    mediana=quantN/2
    mediana+=1
else:
    mediana=quantN/2

mediana=int(mediana)
print(listaN)

# resposta
resp=input(f"Seu número é {listaN[mediana]}? S/N\n ").upper()
""" while (resp!='N') or (resp!='S'):
    print("Responda com S ou N!")
    resp=input(f"Seu número é {listaN[mediana]}? S/N\n").upper()
    print(resp) """
if resp=="S":
    print("Achei seu número!!! hehehehehe\n ")
while resp=="N":
    resp=input(f"Seu número é maoir ou menor que {listaN[mediana]}? maior/menor\n ").lower()
    if resp=="maior":
        """ nMin=listaN[mediana] """
        for i in range(nMin, listaN[mediana], 1):
            listaN.pop(0)
            
            print(listaN)

    elif resp=="menor":
        """ nMax=listaN[mediana] """
        for i in range(listaN[mediana], nMax, 1):
            listaN.pop(-1)
            if quantN%2!=0:
                quantN-=1
                mediana=quantN/2
                mediana+=1
            else:
                mediana=quantN/2

            mediana=int(mediana)
            print(listaN)
            
    resp=input(f"Seu número é {listaN[mediana]}? S/N\n ").upper()
    """ 
    if resp=="maior":
         """