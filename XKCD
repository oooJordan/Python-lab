# -*- coding: utf-8 -*-

def decode_XKCD_tuple(xkcd_values : tuple[str, ...], k : int) -> list[int]:
    '''
    Riceve una lista di stringhe che rappresentano numeri nel formato XKCD
    ed un intero k positivo.
    Decodifica i numeri forniti e ne ritorna i k maggiori.

    Parameters
    valori_xkcd : list[str]     lista di stringhe in formato XKCD
    k : int                     numero di valori da tornare
    Returns
    list[int]                   i k massimi valori ottenuti in ordine decrescente
    '''
    massimi=[]
    
    for i in range(len(xkcd_values)):
        massimi.append(decode_value(xkcd_values[i]))
        
    massimi.sort(reverse = True)
    return massimi[:k]
        
    pass


def decode_value(xkcd : str ) -> int:
    '''
    Decodifica un valore nel formato XKCD e torna l'intero corrispondente.

    Parameters
    xkcd : str                  stringa nel formato XKCD
    Returns
    int                         intero corrispondente
    
    '''
    weights = xkcd_to_list_of_weights(xkcd)
    intero = list_of_weights_to_number(weights)
    return (intero)

def xkcd_to_list_of_weights(xkcd : str) -> list[int]:
    '''
    Spezza una stringa in codifica XKCD nella corrispondente
    lista di interi, ciascuno corrispondente al peso di una lettera romana

    Parameters
    xkcd : str              stringa nel formato XKCD
    Returns
    list[int]               lista di 'pesi' corrispondenti alle lettere romane

    '''
    # INSERISCI QUI IL TUO CODICE
    lista2 = []
    i=0
    while i < len(xkcd):
        c = xkcd[i]
        i += 1 
        n = 0
        while i < len(xkcd) and xkcd[i] == '0':
            n += 1
            i += 1
            
        lista2.append(c + '0' * n)
        
    lista2=list(map(int, lista2))
    return(lista2)
    pass


def list_of_weights_to_number(weigths : list[int] ) -> int:
    '''
    Trasforma una lista di 'pesi' nel corrispondente valore arabo
    tenendo conto della regola di sottrazione

    Parameters
    lista_valori : list[int]    lista di 'pesi' di lettere romane
    Returns
    int                         numero arabo risultante
    
    '''
    # INSERISCI QUI IL TUO CODICE
    somma = weigths[-1]
    for i in range (len(weigths)-1):
        if weigths[i]<weigths[i+1]:
            somma-=weigths[i]
        else:
            somma+=weigths[i]
    return somma
    pass











###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('10010010010100511', decode_value('10010010010100511'), '(397?)')
