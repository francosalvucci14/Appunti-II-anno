Ritornando a [[Lezione 10 - Capitolo 6]]

# Alberi AVL (Adel’son-Vel’skii e Landis, 1962)

## Definizioni

_Def (Fattore di bilanciamento)_
**Fattore di bilanciamento $\beta(v)$** di un nodo v := altezza del sottoalbero sinistro di v - altezza del sottoalbero destro di v
_Def_
Un albero si dice **bilanciato in altezza** se ogni nodo v ha un fattore di bilanciamento in valore assoluto $\leq1$

**Alberi AVL = alberi binari di ricerca in altezza**

Generalmente $\beta(v)$ mantenuto come informazione addizionale nel record relativo a v

**Esempio**
![[appunti asd/mod i/immagini/Pasted image 20221128161923.png|center|600]]

è un albero AVL? Si, tutti i nodi hanno fattore di bilanciamento = 0

**Esempio**

![[appunti asd/mod i/immagini/Pasted image 20221128162110.png|center|500]]

è un albero AVL? No, Non vale la proprietà sui fattori di bilanciamento

>[!INFO]- Osservazione
>Per convenzione l'altezza di un albero vuoto = -1

**Esempio**

![[appunti asd/mod i/immagini/Pasted image 20221128162438.png|center|600]]

è un albero AVL? Si, proprietà sui fattori di bilanciamento rispettata

## Altezza di alberi AVL

Si può dimostrare che **un albero AVL con n nodi ha altezza $O(log(n))$**

**Idea della dimostrazione**: considerare, tra tutti gli AVL, i più sbilanciati

**Albero di Fibonacci di altezza h**: albero AVL di altezza h con il minimo numero di nodi $n_h$

Minimizzare # nodi fissata l'altezza $\equiv$ Massimizzare altezza fissato # nodi

**Intuizione**: se gli alberi di FIbonacci hanno altezza $O(log(n))$, allora tutti gli alberi AVL hanno altezza $O(log(n))$

**Esempio: come è  fatto un albero di Fibonacci di altezza 2?**

![[appunti asd/mod i/immagini/Pasted image 20221128163216.png|center|600]]

Infatti: se togliamo ancora un nodo, o diventa sbilanciato, o cambia la sua altezza
**Nota**: ogni nodo (non foglia) ha fattore di bilanciamento pari (in valore assoluto) a 1

