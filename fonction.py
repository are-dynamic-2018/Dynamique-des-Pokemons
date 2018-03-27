
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
    
def deplacement(i,j,Vide):
    e=np.random.choice(np.arrange(0,len(Vide)))
    x,y=Vide[e]
    M[x,y]=M[i][j]
    M[i][j]=0    
    return    


def accouplement(i,j, Vide):
    n=np.random.choice(np.arange(0,100))
    if len(acc)*10 > n:
        e=np.random.choice(np.arange(0,len(Vide)))
        sexe=np.random.choice(np.arange(1,2))
        x,y=Vide[e]
        M[x,y]=M[i][j]//1000+sexe*100
    return

def manger(Ma,Ar,M,i,j):
    n=np.random.choice(np.arange(0,100))
    if M[i][j]//1000==1:
        if n<10*(len(Ma)+len(Ar)):
            M[i][j]=0
    elif M[i][j]//1000==3:
        if n<10*len(Ma):
            M[i][j]=0
    return i,j

def matrice_alea():
    N=50
    M=np.zeros((N,N))
    for i in range (0,N):
        for j in range (0,N):
            al_e=np.random.choice(np.arange(0,4))
            al_s=np.random.choice(np.arange(1,3))
            al_a=np.random.choice(np.arange(0,100))
            if al_e==0:
                M[i][j]=1000+al_s*100+al_a
            elif al_e==1:
                M[i][j]=2000+al_s*100+al_a
            elif al_e==2:
                M[i][j]=3000+al_s*100+al_a
            elif al_e==3:
                M[i][j]=4000+al_s*100+al_a
    return M
