\documentclass{article}

% Language setting
% Replace `english' with e.g. `spanish' to change the document language
\usepackage[english]{babel}
\usepackage{algorithm}
\usepackage{algpseudocode}
% Set page size and margins
% Replace `letterpaper' with `a4paper' for UK/EU standard size
\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}

% Useful packages
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage[colorlinks=true, allcolors=black]{hyperref}

\title{Problem Set 1}
\author{Ascenzi Leonardo,Folco Damiano, Salvucci Franco, Spadoni Nicolo}

\begin{document}
\maketitle
\tableofcontents

\section{Esercizio 1}
Dato un array V [1 : n] di n interi, progettare un algoritmo che trovi in tempo
lineare (O(n)) e memoria ausiliaria costante (O(1)) il minimo intero positivo
mancante in V .
\subsection{PseudoCodice}
\begin{algorithm}
\caption{Problem Set Esercizio 1}\label{alg:cap}
\begin{algorithmic}
\Require $array\:A$
\State $i=0,n=len(A)$
\While{$i < n$}
    \If{$A[i]=i \vee A[i]\geq n \vee A[i]<0 \vee A[A[i]]=A[i]$}
        \State{$i++$}   \Comment{Incremento i di 1}
    \Else
        \State{$swap(A[A[i]],A[i])$} \Comment{Scambio A[A[i]] con A[i]}
    \EndIf
\EndWhile
\For{$i=1$ to $n$}
    \If{$A[i] \neq i$}
        \State{return i}
    \EndIf
\EndFor
\If{$A[0]=n$}
    \State{return n+1}
\Else
    \State{return n}
\EndIf
\end{algorithmic}
\end{algorithm}
\subsection{Analisi Temporale}
Linea 3,4,5 costo $O(1)$\\
k=num scambi effettuati\\
Equazione di ricorrenza : $T(n)=n(c_3+c_4+c_5)+k+n\implies O(n+k)$\\
Se k = $\Theta(n)$ allora $T(n)=O(3n)\implies O(n)$
\subsection{Dimostrazione}
Dimostrazione di correttezza\\
L'algoritmo è corretto perchè, in tempo lineare e con k scambi, riesce a trovare l'elemento mancante dell'array.
Vige la formula che \\
$$\forall c_i\in A,c_i\in\{1,...,n\},k_{c_1}+...+k_{c_n}< n, con\:k=numscambi,c_i=cellaarray$$\\ Ovvero, per ogni cella dell'array,la somma degli scambi effettuati in ogni cella ($k_{c_i}$) sarà sempre minore della lunghezza dell'array\\
Questo implica che è possibile effettuare gli scambi tutti nella stessa cella, oppure in due celle $c_i,c_j,i\neq j|k_{c_i}+k_{c_j} < n$, e così via\\
A questo punto si ha che, nel caso peggiore, nel ciclo while vengono eseguiti al più n-1 scambi.\\
Alla fine dell'esecuzione del ciclo while, l'array risulterà parzialemente ordinato cioè,per qualche indice i dell'array si avrà che l'elemento in  posizione i conterrà esattamente il valore i.\\
Il ciclo for, che parte da 1 ed esegue al più n passaggi, ci permette di restituire l'indice del primo elemento dell'array che ha un valore diverso dal proprio indice (se esiste), che risulterà essere il valore da ricercare.\\
Nel caso in cui il ciclo for termina la sua esecuzione senza restituire alcun indice, verrà eseguito un controllo sul primo elemento dell'array.\\
Se questo il valore di questo elemento è uguale alla lunghezza dell'array, allora verrà restituita la lunghezza dell'array +1, altrimenti il primo minimo mancante è proprio la lunghezza dell'array.

\section{Esercizio 2}
\section{Esercizio 3}


\end{document}