Ritornando a [[LMP 0]], inseriamo le classi ProfessorImpl e StudentImpl e le interfacce corrispondenti, ovvero Student e Professor

Codice di Student
```java
package it.uniroma2.art.lmp.ex.model;

public interface Student extends Person {
	public String getMatricola();
}

```
faccio extends Person per estendere l'interfaccia Student all'interfaccia Person, per prendere tutti i metodi di Person. 
Faccio la stessa cosa con Professor

Codice di Professor
```java
package it.uniroma2.art.lmp.ex.model;

public interface Professor extends Person{
	public String getCattedra();
}

```

Codice di StudentImpl
```java
package it.uniroma2.art.lmp.ex.model;

public class StudentImpl extends PersonImpl implements Student {
	private String matricola;
	public StudentImpl(String nome, String cognome, String codiceFiscale,String matricola) {
		super(nome, cognome, codiceFiscale);
		this.matricola = matricola;
	}
	@Override
	public String getMatricola() {
		return matricola;
	}
}
```

Codice di ProfessorImpl

```java
/**
 * 
 */
package it.uniroma2.art.lmp.ex.model;

/**
 * @author franc
 *
 */
public class ProfessorImpl extends PersonImpl implements Professor {

	/**
	 * @param nome
	 * @param cognome
	 * @param codiceFiscale
	 */
	private String cattedra;
	//esempio di overloading (meglio non farlo)
	public ProfessorImpl(String nome, String cognome, String codiceFiscale) {
		super(nome, cognome, codiceFiscale);
	}
	public ProfessorImpl(String nome, String cognome, String codiceFiscale,String cattedra) {
		//super(nome, cognome, codiceFiscale);
		this(nome,cognome,codiceFiscale);
		this.cattedra = cattedra;
	}
	@Override
	public String getCattedra() {
		return cattedra;
	}
	
	public String toString() {
		return super.toString() + ", " + ((cattedra!=null)?cattedra:"");//espressione compatta per if-then-else
	}
}
```
