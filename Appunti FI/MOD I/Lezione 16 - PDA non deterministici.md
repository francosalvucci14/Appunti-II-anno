# Automi a pila non deterministici

Un **automa a pila non deterministico** è definito come una settupla $\mathcal M=\langle\Sigma,\Gamma,Z_0,Q,q_0,F,\delta\rangle$ dove $\Sigma$ è l'**alfabeto in input**, $\Gamma$ è l'**alfabeto dei simboli della pila**, $Z_0\in\Gamma$ è il **simbolo iniziale di pila**, Q è un insieme finito e non vuoto di **stati**, $q_0\in Q$ è lo **stato iniziale**, $F\subseteq Q$ è l'**insieme degli stati finali**, $\delta:Q\times(\Sigma\cup\{\varepsilon\})\times\Gamma\to\mathcal P(Q\times\Gamma^\star)$ è la **funzione (parziale) di transizione**

**Oss**
$\mathcal P(Q\times\Gamma^\star)$ è l'insieme potenza di $Q\times\Gamma^\star$

Nel caso degli automi a pila la presenza del non determinismo comporta un aumento del potere computazionale

Mentre gli automi a pila non deterministici riconoscono la classe dei linguaggi non contestuali, gli automi a pila deterministici riconoscono un sottoinsieme proprio di tali linguaggi, la classe dei linguaggi non contestuali deterministici

**Esempio**: accettazione del linguaggio non contestuale $\{w\hat w|w\in\{s,b\}^+\}$, dove $\hat w$ indica la stringa riflessa di $w$  

