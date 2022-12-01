
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
    \If{$A[i] \neg i$}
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
Equazione di ricorrenza : $T(n)$
\subsection{Dimostrazione}
\section{Esercizio 2}
\section{Esercizio 3}


\end{document}