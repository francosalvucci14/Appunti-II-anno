# Parte 1

- Aggiunta della classe CorsoDiStudi
- Modifica della classe StudentImpl
	- aggiunta dei campo corsodistudi e annodicorso
	- modifica dei costruttori
	- aggiunta dei metodi getAnnoDiCorso e getCorsoDiStudi
- Modifica dell'interfaccia Student

Codice della classe CorsoDiStudi

```java
package it.uniroma2.art.lmp.ex.model;

public enum CorsoDiStudi {
    INFORMATICA("INF"),
    INGEGNERIA("ING"),
    PSICOLOGIA("PSI");
    private String codice;

    CorsoDiStudi(String codice){
        this.codice = codice;
    }
    public String getCode(){
        return codice;
    }
}
```

Codice modificato di StudentImpl

```java
package it.uniroma2.art.lmp.ex.model;

public class StudentImpl extends PersonImpl implements Student {
    
    protected String matricola;
    static private int numStudenti = 0;
    private CorsoDiStudi corsoDiStudi;
    private int annoDiCorso;
    
    public StudentImpl(String nome, String cognome, String codiceFiscale,
            CorsoDiStudi corso, int annoDiCorso) {
        super(nome, cognome, codiceFiscale);
        this.corsoDiStudi = corso;
        this.annoDiCorso = annoDiCorso;
        this.matricola = corsoDiStudi.getCode() + ++numStudenti;
    }
    // overload
    public StudentImpl(Person p, CorsoDiStudi corso, int annoDiCorso) {
        this(p.getNome(), p.getCognome(), p.getCodiceFiscale(), corso, annoDiCorso);
    }
    @Override
    public String getMatricola() {
        return matricola;
    }
    public String toString() {
        return super.toString() + ", " + matricola;
    }
    @Override
    public void saluta(Professor prof) {
        // TODO Auto-generated method stub
        System.out.println("salve prof* " + prof);
    }
    @Override
    public void saluta(Professor prof, String appellativo) {
        // TODO Auto-generated method stub
        System.out.println("salve prof* " + prof + ", lei è proprio " + appellativo);
    }
    @Override
    public int getAnnoDiCorso() {
        return annoDiCorso;
    }
    @Override
    public CorsoDiStudi getCorsoDiStudi() {
        return corsoDiStudi;
    }
}
```

Codice modificato di Student

```java
package it.uniroma2.art.lmp.ex.model;

public interface Student extends Person {

    String getMatricola();
    int getAnnoDiCorso();
    CorsoDiStudi getCorsoDiStudi();
    // overload
    void saluta(Professor prof);
    void saluta(Professor prof, String appellativo);
}
```

----
# Parte 2
