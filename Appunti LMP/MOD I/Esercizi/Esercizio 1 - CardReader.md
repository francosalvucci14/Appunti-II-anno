Svolto esercizio 1 Card Reader (vedi [Card Reader](http://art.uniroma2.it/teaching/lmp/part_I/stuff/Esempio%20di%20Compito%20-%20Card%20Reader.pdf))

- CardReader e CardFormatDeserializer sono le factory dell'esercizio
- BadlyFileFormattedException è l'eccezione custom

**Stuttura del progetto**

```mermaid
graph LR
	A{Attività}
	B{Attività Commerciali}
	C[Associazione]
	D[Ristorante]
	E[Negozio]
	
	style A fill:black, color:#fff
	style B fill:black, color:#fff
	style C fill:black, color:#fff
	style D fill:black, color:#fff
	style E fill:black, color:#fff
	
	A-- Superclasse di -->B & C
	B--Superclasse di -->D & E
```

- Attività è la superclasse di Attività Commerciali e Associazione, nel emntre Attività Commerciali è la superclasse di Ristorante e Negozio

