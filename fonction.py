
import numpy as np

def vieillesse(M,i,j):
    if M[i][j]%100==99:
        M[i][j]=0
    else:
        M[i][j]=M[i][j]+1
        n=np.random.choice(99)      
        if M[i][j]%100>n:
            M[i][j]=0 
    return

def position(i,j):
    if i==0:
        if j==0:
            return "CoinSupG"
        elif j==len(M)-1:
            return "CoinSupD"
        else:
            return "CotHaut"
    elif j==0:
        if i==len(M)-1:
            return "CoinBasG"
        else :
            return "CotG"
    elif j==len(M)-1:
        if i==len(M)-1:
            return "CoinBasD"
        else:
            return "CotD"
    elif i==len(M):
        return "CoteBas"
    else:
        return "Milieu"
        
def voisin(i,j):
    Le=[]#environnement
    if position(i,j)=="Milieu":
        Le=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
    elif position(i,j)=="CoinSupG":
        Le=[(i,j+1),(i+1,j),(i+1,j+1)]
    elif position(i,j)=="CoinSupD":
        Le=[(i,j-1),(i+1,j),(i+1,j-1)]
    elif position(i,j)=="CoinBasG":
        Le=[(i,j+1),(i-1,j),(i-1,j+1)]
    elif position(i,j)=="CoinBasD":
        Le=[(i,j-1),(i-1,j),(i-1,j-1)]
    elif position(i,j)=="CotD":
        Le=[(i,j-1),(i-1,j),(i-1,j-1),(i+1,j),(i+1,j-1)]
    elif position(i,j)=="CotG":
        Le=[(i,j+1),(i-1,j),(i-1,j+1),(i+1,j+1)]
    elif position(i,j)=="CotBas":
        Le=[(i,j-1),(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1)]
    elif position(i,j)=="CotHaut":
        Le=[(i,j-1),(i+1,j-1),(i+1,j),(i+1,j+1),(i,j+1)]
    return Le
    
