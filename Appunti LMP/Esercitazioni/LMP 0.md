Vedi codice su eclipse LMP 0

Classe Main.java
```java
package it.uniroma2.art.lmp.ex.model;

/**
 * @author Franco
 * <p>questa è la classe di avvio dell'esercizio di LMP</p>
 */
public class Main {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person franco=new Person("Franco","Salvucci","0306609");
		
		//System.out.println(franco.getNome());
		//System.out.println(franco.toString());
		System.out.println(franco);
		franco.saluta();
		
	}

}

```

Classe Person.java
```java
package it.uniroma2.art.lmp.ex.model;

public class Person {
	
	private String nome;
	private String cognome;
	private String codiceFiscale;
	
	public Person(String nome, String cognome, String codiceFiscale) {
		//super();
		this.nome = nome;
		this.cognome = cognome;
		this.codiceFiscale = codiceFiscale;
		
	}
	
	public String getNome() {
		return nome;
	}
	public String getCognome() {
		return cognome;
	}

	public String getCodiceFiscale() {
		return codiceFiscale;
	}
	
	public void saluta() {
		System.out.println("Ciao a tutti!!!");
	}
	
	public String toString() {
		return nome+ " " +cognome + ":" + codiceFiscale;
	}
	
}

```

