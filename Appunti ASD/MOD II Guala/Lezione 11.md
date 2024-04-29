```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Sempre su Network Flow I

## Relazione tra flussi e tagli

>[!definition]- Lemma Valore del Flusso
>Sia $f$ un qualunque flusso e sia $(A,B)$ un qualunque taglio.
>Allora,  Il valore del flusso $f$ è uguale al flusso netto che attraversa il taglio $(A,B)$
>$$val(f)=\sum\limits_{\text{archi e uscenti da A}}f(e)-\sum\limits_{\text{archi e entranti in A}}f(e)$$

![[Pasted image 20240429105436.png|center|500]]

![[Pasted image 20240429105516.png|center|500]]

![[Pasted image 20240429105526.png|center|500]]

**Dimostrazione del lemma**

$$\begin{align}val(f)&=\sum\limits_{\text{archi e uscenti da s}}f(e)-\sum\limits_{\text{archi e entranti in s}}f(e)\\&=\underbrace{\sum\limits_{v\in A}(\sum\limits_{\text{archi e uscenti da v}}f(e)-\sum\limits_{\text{archi e entranti in v}}f(e))}_{\text{Per la conservazione del flusso, tutti i termini tranne v=s sono 0}}\\&=\sum\limits_{\text{archi e uscenti da A}}f(e)-\sum\limits_{\text{archi e entranti in A}}f(e)\end{align}$$

>[!definition]- Dualità debole
>Sia $f$ un qualunque flusso e sia $(A,B)$ un qualunque taglio.
>Allora, $val(f)\leq cap(A,B)$

**Dimostrazione**

$$\begin{align}val(f)&=\underbrace{\sum\limits_{\text{archi e uscenti da A}}f(e)-\sum\limits_{\text{archi e entranti in A}}f(e)}_{\text{Per il lemma sul valore del flusso}}\\&\leq\sum\limits_{\text{archi e uscenti da A}}f(e)\\&\leq\sum\limits_{\text{archi e uscenti da A}}c(e)\\&=cap(A,B)\end{align}$$
![[Pasted image 20240429110202.png|center|500]]

### Certificato di Ottimalità

>[!warning]- Corollario
>Sia $f$ un flusso e $(A,B)$ un taglio
>Se $val(f)=cap(A,B)$, allora $f$ è un flusso massimo e $(A,B)$ è un taglio minimo

**Dimostrazione**
- Per ogni flusso $f':val(f')\overbrace{\leq}^{\text{Dualità debole}} cap(A,B)=val(f)$
- Per ogni taglio $(A',B'):cap(A',B')\underbrace{\geq}_{\text{Dualità debole}} val(f)=cap(A,B)$

![[Pasted image 20240429110535.png|center|500]]

## Teorema Max-Flow Min-Cut

Diamo ora la definizione del teorema che lega il max flow al min cut, senza dimostrazione

>[!definition]- Teorema Max-Flow Min-Cut
>Il valore del max-flow $\underbrace{=}_{\text{Dualità forte}}$ capacità del taglio minimo

Diamo la definizione di un'altro teorema

>[!definition]- Teorema dei percorsi aumentanti
>Un flusso $f$ è un max-flow $\iff$ non ci sono percorsi aumentanti

**Dimostrazione**

Le seguenti 3 condizioni sono equivalenti per ogni flusso $f$:
1) Esiste un taglio $(A,B)$ tale che $cap(A,B)=val(f)$
2) $f$ è un max-flow
3) Non esiste un percorso aumentante rispetto a $\overbrace{f}^{\text{Se Ford-Fulkerson termina, allora f è un max-flow}}$

