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

