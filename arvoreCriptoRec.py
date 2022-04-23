from sys import stdin,stdout
from math import log
def readln():
    dim = stdin.readline().rstrip("\n")
    folhas = stdin.readline().rstrip("\n")
    
    folhas = [int(i) for i in folhas.split()]
    return int(dim),folhas

def outln(value):
    stdout.write(str(value))
    stdout.write("\n")

def hashcode(x):
    return x % 1000000007

def hashcodeConj(x,y) :
    mod = 1000000007
    return ((x % mod) + (y % mod)) % mod

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def BuildTree(numNiveis,folhasHash,rootAtual):
    
    level=folhasHash
    root=rootAtual
    if(numNiveis>0):
        newLevel=[]
        for j in range(0,len(level),2):
            value=hashcodeConj(level[j].value,level[j+1].value)
            root= Node(value)
            root.left=level[j]
            root.right=level[j+1]
            newLevel.append(root)
        level=newLevel
        rootAtual=root
        return BuildTree(numNiveis-1,level,rootAtual)
    else:
        return root

def arvore():
    dim, folhas= readln()
    folhasHash=[]
    for x in range(len(folhas)):
        root=Node(hashcode(folhas[x]))
        folhasHash.append(root)
    
    numLevels=int(log(dim,2))+1
    if(numLevels>1):
        raiz=BuildTree(numLevels-1, folhasHash,None)
        newLevel=[raiz]
        percorrer(raiz,newLevel)  
    else:
        outln(folhasHash[0].value)
            
def percorrer(root,level):
   
    if len(level)>0:
        newLev=[]
        for i in range(len(level)):
            if(root.value!=None):
                outln(level[i].value)
                root=level[i]
            if(root.left!=None):
                newLev.append(root.left)
            if(root.right!=None):
                newLev.append(root.right)

        level=newLev
        percorrer(root, newLev)
        

if __name__ == "__main__":
    arvore()