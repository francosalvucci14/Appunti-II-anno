Algoritmo di DP per II di peso massimo su un'albero (non perforza binario e completo)

**Esempio istanza**

![[Pasted image 20240326100459.png|center|300]]

**Soluzione ottima**

![[Pasted image 20240326100517.png|center|300]]

# Versione 1

**Pseudocodice**

```pseudo
\begin{algorithm}
    \caption{Algoritmo Soluzione}
    \begin{algorithmic}
      \Procedure{Soluzione}{nodo $v$}
        \If{$v$ is Null}
	        \State return 0,0,0
        \EndIf
        \If{$sx(v)$ is Null $\land\space dx(v)$ is Null}
         \State $root(v)\gets val(v)$
         \State $deep(v)\gets 0$
         \State $max(v)\gets val(v)$
         \State return $root(v),deep(v),max(v)$
        \EndIf
        \ForAll{$u$ figlio di $v$}
        \State $opt_{root}(v),opt_{figli}(v),opt_{max}(v)\gets$ Soluzione($v$);
        \State $root(v)\gets val(v)+\sum opt_{figli}$;
        \State $deep(v)\gets \sum\limits opt_{max}$;
        \State $max(v)\gets \max\{root(v),deep(v)\}$;
        \EndFor
        \State return $root(v),deep(v),max(v)$;
      \EndProcedure
      \end{algorithmic}
    \end{algorithm}
    \begin{algorithm}
    \caption{Algoritmo Trova Soluzione}
    \begin{algorithmic}
      \Procedure{SoluzioneOttima}{nodo $v$}
        \State $opt \gets$ Soluzione($v$);
        \State return $opt[2]$
      \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```

L'algoritmo è il seguente, scritto in Python

*Osservazione chiave sull'algoritmo* :
- La chiamata `Ric(nodo.center,bool)` e la chiamata `Ricostruzione(nodo.center,bool)` vengono usate $\iff$ l'albero in input non è binario completo (tipo quello dell'esempio sopra)
- Se l'albero è binario queste chiamate non verrano mai usate, perchè il campo `center` del nodo sarà impostato a `None`

```python
class TreeNode:
    def __init__(
        self,
        val,
        left=None,
        center=None,
        right=None,
        root=None,
        deep=None,
        max=None,
        mark=None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.center = center
        self.root = root
        self.deep = deep
        self.max = max
        self.mark = mark


def Algoritmo(nodo):
    opt = MaxIS_Tree(nodo)
    return opt[2]


def MaxIS_Tree(nodo):
    if nodo == None:
        return 0, 0, 0
    if nodo.left == None and nodo.right == None:
        nodo.root = nodo.val
        nodo.deep = 0
        nodo.max = nodo.val
        
        return nodo.root, nodo.deep, nodo.max
    _, opt_figli_l, opt_max_l = MaxIS_Tree(nodo.left)
    _, opt_figli_r, opt_max_r = MaxIS_Tree(nodo.right)
    _, opt_figli_c, opt_max_c = MaxIS_Tree(nodo.center)
    nodo.root = nodo.val + (opt_figli_l + opt_figli_r + opt_figli_c)
    nodo.deep = opt_max_r + opt_max_l + opt_max_c
    nodo.max = max(nodo.root, nodo.deep)
    return nodo.root, nodo.deep, nodo.max


def Ric(nodo):
    max = Algoritmo(nodo)
    if nodo.root == max:
	    print(f"Nodo che fa parte della soluzione : {nodo.val}")
        Ricostruzione(nodo.left, True)
        Ricostruzione(nodo.right, True)
        Ricostruzione(nodo.center,True)
    else:
        Ricostruzione(nodo.left, False)
        Ricostruzione(nodo.right, False)
        Ricostruzione(nodo.center,False)


def Ricostruzione(nodo, bool):
    if nodo == None:
        return None
    if bool == True:
        Ricostruzione(nodo.left,False)
        Ricostruzione(nodo.right,False)
        Ricostruzione(nodo.center,False)
    else:
        if nodo.root == nodo.max:
            nodo.mark=True
            print(f"Nodo che fa parte della soluzione : {nodo.val}")
            Ricostruzione(nodo.left,True)
            Ricostruzione(nodo.right,True)
            Ricostruzione(nodo.center,True)
        else:
            Ricostruzione(nodo.left,False)
            Ricostruzione(nodo.right,False)
            Ricostruzione(nodo.center,False)

root = TreeNode(2)
l1 = TreeNode(7)
r1 = TreeNode(6)
l2 = TreeNode(3)
l2_r2 = TreeNode(1)
r1_l1 = TreeNode(2)
r1_l2 = TreeNode(3)
r1_l3 = TreeNode(3)

root.left = l1
root.right = r1
l1.left = l2
l1.right = l2_r2
r1.left = r1_l1
r1.center = r1_l2
r1.right = r1_l3

print(f"Soluzione ottima del problema : {Algoritmo(root)}")
Ric(root)
```

L'algoritmo produrrà la seguente soluzione :
- Valore soluzione ottima : 15
- Nodi che fanno parte della soluzione : 7 (nodo interno),2 (foglia),3 (foglia),3(foglia)

## Funzione stampa albero

In aggiunta, metto qui per chi vuole una utility scritta in python, che dato il nodo root di un'albero lo stampa a schermo secondo il seguente ordine :

- Radice
	- Figlio1 (nodo interno)
		- Figlio1.2 (foglia)
	- Figlio2 (foglia)

Il codice è il seguente

```python
def printTree(root, level=0):
    if root == None:
        return None
    if level == 0:
        label="Radice"
    elif root.left != None or root.right != None:
        label = "Nodo interno"
    else:
        label = "Foglia"
    
    print('|_\t' * level + str(root.val)+" "+label)
    sx = printTree(root.left,level + 1)
    dx = printTree(root.right,level + 1)
    cx = printTree(root.center,level + 1)
```

