## Espressioni regolari

_Def_
Dato un alfabeto $\Sigma$ e dato l'insieme di simboli $(+,\star,(,),.,\emptyset)$ si definisce **espressione regolare** sull'alfabeto $\Sigma$ una stringa
$$r\in(\Sigma\:\cup(+,\star,(,),.,\emptyset))^+$$
tale che valga una delle seguenti condizioni:
1. $r=\emptyset$
2. $r\in\Sigma$
3. $r=(s+t)$, oppure $r=(s\cdot t)$, oppure $r=s^\star$, dove s e t sono espressioni regolari sull'alfabeto $\Sigma$

