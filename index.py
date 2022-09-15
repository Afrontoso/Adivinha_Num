mediana=int()
resp=str()
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
for i in range(nMin, nMax+1, 1):
    listaN.append(i)

#Posição central
if len(listaN)%2!=0:
    quantN-=1
    mediana=quantN/2
else:
    mediana=quantN/2
mediana=int(mediana)

# resposta
resp=input(f"Seu número é {listaN[mediana]}? S/N\n ").upper()

if resp=="S":
    print("Achei seu número!!! hehehehehe\n ")
while resp=="N":
    resp=input(f"Seu número é maior ou menor que {listaN[mediana]}? maior/menor\n ").lower()
    if resp=="maior":
        for i in range(nMin, listaN[mediana], 1):
            listaN.pop(0)
            quantN=len(listaN)
            if quantN%2!=0:
                quantN-=1
                mediana=quantN/2
            else:
                mediana=quantN/2
        nMin=listaN[0]
    elif resp=="menor":
        for i in range(listaN[mediana], nMax, 1):
            listaN.pop(-1)
            quantN=len(listaN)
            print(listaN)
            if quantN%2!=0:
                quantN-=1
                mediana=quantN/2
            else:
                mediana=quantN/2 
        nMax=listaN[-1]         
    mediana=int(mediana)    
    resp=input(f"Seu número é {listaN[mediana]}? S/N\n ").upper()
# resposta
if resp=="S":
    print("Achei seu número!!! hehehehehe\n ")