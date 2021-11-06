
#          | prix | vitesse max   | consome moyen | Dis Freinage | Confort | vol coffre | acceletation |
#          | Min  | Max           | Min           | Min          | Max     | Max        | Max
#  poids   | 0.5  | 0.1           | 0.4           | 0.1          | 0.3     | 0.1        | 0.2
#  veto    | 1000 | 5             | 1.5           | 4            | 2       | 50         | 2
#  seuil   |

import pandas as pd
import numpy as np
import sys

def PrometheeI(Data, poid, miniMax):
    print("_______________Promethee I_______________")
    nbrRow = len(Data)
    nbrCol = len(Data[0])

    # print(nbrRow) # 10
    # print(nbrCol) # 7

    res = np.zeros((nbrRow,nbrRow))

    for i in range(nbrRow):
        for j in range(nbrRow):
            if i!=j:
                for k in range(0,nbrCol):
                    if (miniMax[k]=='Max' and Data[i][k]>Data[j][k]) or (miniMax[k]=='Min' and Data[i][k]<Data[j][k]):  
                        res[i][j] += poid[k]

    fluxPositif = np.zeros(nbrRow)
    fluxNegatif = np.zeros(nbrRow)

    for i in range(nbrRow):
        for j in range(nbrRow):
            fluxPositif[i] += res[i][j]
            fluxNegatif[i] += res[j][i]
    
    print("tableau de degres")
    print(res)

    print("flux positif:")
    print(fluxPositif)
    print("flux negatif:")
    print(fluxNegatif)
    
    print("classement de flux positif:")
    print(np.argsort(-fluxPositif))
    print("classement de flux negatif:")
    print(np.argsort(fluxNegatif))

    return res, fluxPositif, fluxNegatif


def PrometheeII(fluxPositif, fluxNegatif):
    print("_______________Promethee II_______________")
    flux = np.zeros(len(fluxPositif))
    for i in range(len(flux)):
        flux[i] = fluxPositif[i] - fluxNegatif[i]
    
    # print(flux)
    sortFlux = np.argsort(-flux)
    # print(sortFlux)

    print("classement de Promethee II:")
    print(sortFlux)

def ElectreIv(Data, veto, miniMax):
    print("_______________Electre Iv_______________")
    nbrRow = len(Data)
    nbrCol = len(Data[0])

    # print(nbrRow) # 10
    # print(nbrCol) # 7

    res = np.ones((nbrRow,nbrRow))

    for i in range(nbrRow):
        for j in range(nbrRow):
            if i!=j:
                for k in range(0,nbrCol):
                    if (miniMax[k]=='Max' and Data[i][k]<Data[j][k] and Data[j][k]-Data[i][k]>veto[k]) or (miniMax[k]=='Min' and Data[i][k]>Data[j][k] and Data[i][k]-Data[j][k]>veto[k]):  
                        res[i][j] = 0
            else:
                res[i][j] = -1
    print(res)
    return(res)

    
    


def ElectreIs(Data, poid, PreferenceThreshold, miniMax):
    print("_______________Electre Is_______________")
    nbrRow = len(Data)
    nbrCol = len(Data[0])

    # print(nbrRow) # 10
    # print(nbrCol) # 7

    res = np.zeros((nbrRow,nbrRow))

    for i in range(nbrRow):
        for j in range(nbrRow):
            if i!=j:
                for k in range(0,nbrCol):
                    if (miniMax[k]=='Max' and Data[i][k]>Data[j][k]) or (miniMax[k]=='Min' and Data[i][k]<Data[j][k]):  
                        res[i][j] += poid[k]
                    elif miniMax[k]=='Max' and Data[i][k]<=Data[j][k]:
                        if Data[j][k] - Data[i][k] < PreferenceThreshold[k]:
                            res[i][j] += (1-(Data[j][k] - Data[i][k])/PreferenceThreshold[k]) * poid[k]
                    elif miniMax[k]=='Min' and Data[i][k]>=Data[j][k]:
                        if Data[i][k] - Data[j][k] < PreferenceThreshold[k]:
                            res[i][j] += (1-(Data[i][k] - Data[j][k])/PreferenceThreshold[k]) * poid[k]
    print("La table :")
    print(res)
    return res


def findCouples(degre, tabVeto, s):
    n = len(degre)
    N = [i for i in range(n)]
    # les couples
    couples = []

    for i in range(n):
        for j in range(n):
            if degre[i][j] > s and tabVeto[i][j] == 1 and degre[i][j] > degre[j][i]:
                couples.append((i,j))
                if j in N:
                    N.remove(j)
    
    print("La relation de surclassement est vérifiée pour les couples :")
    print(couples)
    print("Donc dans ce cas N = ", end='')
    print(N)

def main():
    # values default
    # poid = [5,1,4,1,3,1,2]
    # veto = [1000,5,1.5,4,2,50,2]
    # miniMax = ['Min', 'Max', 'Min', 'Min', 'Max', 'Max', 'Max']
    # PreferenceThreshold = []
    # df = pd.read_csv(r'donnee.csv', header=None)

    poid = [0.1,0.2,0.2,0.1,0.2,0.2]
    veto = [45,29,550,6,4.5,4.5]
    PreferenceThreshold = [20, 10, 200, 4, 2, 2]
    miniMax = ['Min', 'Max', 'Min', 'Min', 'Min', 'Max']
    df = pd.read_csv(r'test.csv', header=None)

    print (df)

    # Operation
    op = 1
    while(op!=0):
        print("List de methode:")
        print("1. Promethee")
        print("2. Electre Iv")
        print("3. Electre Is")

        print("0. exit")
        op = int(input("Choisir la methode vous voulez tester: "))

        if(op==0):
            exit()
        elif(op==1):
            # for i in range(len(df)):
            #     poid.append(input("Choisissez le poid pour chaque attribut : "))

            res, fluxPositif, fluxNegatif = PrometheeI(df.values, poid, miniMax)
            PrometheeII(fluxPositif, fluxNegatif)
        elif(op==2):
            tabVeto = ElectreIv(df.values, veto, miniMax)
            s = float(input("Donnez un niveau de concordance: "))
            degre, fluxPositif, fluxNegatif = PrometheeI(df.values, poid, miniMax)
            findCouples(degre, tabVeto, s)

        elif(op==3):
            degre = ElectreIs(df.values, poid, PreferenceThreshold, miniMax)
            s = float(input("Donnez un niveau de concordance: "))
            tabVeto = ElectreIv(df.values, veto, miniMax)
            findCouples(degre, tabVeto, s)
    
    





if __name__ == "__main__":
    main()


