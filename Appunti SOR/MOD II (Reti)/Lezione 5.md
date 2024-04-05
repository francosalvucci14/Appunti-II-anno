# Mantenere lo stato utente/server : i cookie

Ricorda : l'interazione HTTP GET/risposta è **senza stato (stateless)**

Nessuna nozione di scambio di messaggi HTTP in più fasi per completare una "transazione" Web
- Non è necessario che il client o il server tengano traccia dello "stato" dello scambio in più fasi
- Tutte le richieste HTTP sono indipendenti l'una dall'altra
- Non è necessario che il client nè il server siano in grado di "recuperare" da una transazione quasi completa ma mia completata

![[Pasted image 20240405103141.png|center|300]]

I siti web e il browser client usano i **cookie** per mantenere lo stato tra le transizioni

Ci sono 4 componenti:
1) Una riga di intestazione nel messaggio di _risposta_ HTTP
2) Una riga di intestazione nel messaggio di _richiesta_ HTTP
3) Un file cookie mantenuto sul sistema terminale dell'utente gestito dal browser dell'utente
4) Un database sul sito

**Esempio**
- Susan usa il browser dal portatile, visita uno specifico sito di e-commerce per la prima volta
- Quando arriva la richiesta HTTP iniziale al sito, il sito crea :
	- **Un  identificativo univoco**
	- **Una voce nel proprio database**, indicizzata dal numero identificativo
- Il server ritorna una risposta che include l'intestazione **Set-Cookie**, che contiene l'identificativo unico e che sarà aggiunto al file dei cookie
- Le successive richieste del browser di Susan per questo sito conterranno l'identificativo in una intestazione cookie

![[Pasted image 20240405104159.png|center|450]]

## Cookie

I cookie possono essere usati per :
- Autorizzazione
- Carrello degli acquisti
- Raccomandazioni
- Stato della sessione dell'utente

>[!info]- Nota
>Cookie e privacy :
>- I cookie consentono ai siti di _imparare_ molto da voi
>- Cookie persistenti di terze parti (tracking cookies) consentono il tracciamento di una identità comune attraverso siti web multipli

