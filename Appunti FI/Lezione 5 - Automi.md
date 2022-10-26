# Automa

Dispositivo astratto che, data una stringa x fornitagli in input, esegue una **computazione**
Se la computazione termina,restituisce,secondo una qualche modalità, un valore

Nel caso del problema di riconoscimento, il valore restituito è booleano

![[appunti fi/immagini/Pasted image 20221026150139.png|center|500]]

"Si" lo abbiamo se $x\in L$, altrimenti avremo "No" $x\not\in L$

## Composizione

- Dispositivo interno, che ad ogni istante assume un **stato** in un possibile insieme finito predefinito
- Uno o più dispositivi di memoria (nastri), sui quali è possibile memorizzare delle informazioni, sotto forma di stringhe di caratteri da alfabeti predefiniti
- Nastri costituiti da celle; ogni cella può contenere un carattere
- Caratteri letti o scritti per mezzo di **testine** che possono muoversi lungo i nastri, posizionandosi sulle diverse celle

