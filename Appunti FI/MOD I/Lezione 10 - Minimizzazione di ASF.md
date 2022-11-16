# Minimizzazione

L'ASFD con minimo numero di stati che riconosce un dato linguaggio $L$ può essere derivato partizionando l'insieme $Q$ degli stati in un automa che riconosce $L$ in classi di equivalenza rispetto alla relazione
$$q_i\equiv q_j\iff(\forall x\in\Sigma^\star,\overline\delta(q_i,x)\in F\iff\overline\delta(q_j,x)\in F)$$
Quindi, $q_i\equiv q_j$ se e solo se ogni stringa che porta da $q_i$ ad uno stato finale porta anche da $q_j$ ad uno stato finale (e vice versa)
