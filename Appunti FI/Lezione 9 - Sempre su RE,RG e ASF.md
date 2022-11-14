# State elimination

Procedura iterativa di eliminazione degli stati su un automa non deterministico **generalizzato** equivalente, in cui:
1. La funzione di transizione è definita su $Q\times E$, dove $E$ è l'insieme delle espressioni regolari su $\Sigma$, per cui gli archi sono etichettati con e.r
2. Lo stato inziale non ha archi entranti, per cui : $\not\exists q\in Q,e\in E : q_0\in\delta_N(q,e)$
3. Esiste un solo stato finale $q_F$ senza archi uscenti, per cui: $\not\exists e\in E:\delta_N(q_F,e)\neq\emptyset$

