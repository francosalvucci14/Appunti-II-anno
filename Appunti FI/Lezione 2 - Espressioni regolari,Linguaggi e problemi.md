## Espressioni regolari

_Def_
Dato un alfabeto $\Sigma$ e dato l'insieme di simboli $(+,\star,(,),\cdot,\emptyset)$ si definisce **espressione regolare** sull'alfabeto $\Sigma$ una stringa
$$r\in(\Sigma\:\cup(+,\star,(,),\cdot,\emptyset))^+$$
tale che valga una delle seguenti condizioni:
1. $r=\emptyset$
2. $r\in\Sigma$
3. $r=(s+t)$, oppure $r=(s\cdot t)$, oppure $r=s^\star$, dove s e t sono espressioni regolari sull'alfabeto $\Sigma$

**Esempio**
$\Sigma=(a,b)$
Un'espressione regolare su $\Sigma$ appena definito può essere $r=a)+b\cdot b$ 

Le espressioni regolari consentono di rappresentare linguaggi mediante una opportuna interpretazione dei simboli che le compongono. Nella tabella seguente si mostra la corrispondenza tra un'espressione regolare $r$ e il linguaggio $\mathcal L(r)$ che essa rappresenta

![[appunti fi/immagini/Pasted image 20221017111656.png|center]]

**Esempio**

L'espressione regolare $r=((a+b)^\star a)$ rappresenta il linguaggio
$$L=((a+b)^\star a)\implies L((a+b)^\star)\circ L(a)=L((a+b))^\star\circ L(a)=(L(a)\cup L(b))^\star \circ \left\{a\right\}=$$
$$=(\left\{a\right\}\cup\left\{b\right\})^\star\circ\left\{a\right\}=\left\{a,b\right\}^\star\circ\left\{a\right\}\implies \left \{x|x\in\left\{a,b\right\}^+,\text{x termina con a}\right\}$$

**Esercizi** 

1) determinare l'espressione regolare che, sull'alfabeto $\left\{a,b\right\}$, definisce l'insieme delle stringhe il cui terzultimo carattere è una b
2) determinare il linguaggio definito dall'aespressione regolare $a^\star((aa)^\star b+(bb)^\star a)b^\star$ 

## Linguaggi e problemi

L'insieme dei linguaggi è in stretto rapporto con quello dei **problemi di decisione**

_Def (**Problema di decisione**)_
Un problema di decisione è definito su un insieme di possibili **istanze** e associa ad ognuna di esse un valore Vero/Falso

L'insieme delle istanze è partizionato in istanze **positive e negative**: il problema, per ogni istanza, è riconoscere se è un istanza positiva

