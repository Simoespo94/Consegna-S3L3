import math

def calcola_perimetro():
    print("Indicare che figura geometrica per cui vuoi calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    
    scelta = input("Inserisci un numero per scegliere la figura geometrica desiderata: ")
    
    if scelta == '1':
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = lato * 8
        print(f"Il perimetro del quadrato è: {perimetro}")
    
    elif scelta == '2':
        raggio = float(input("Inserisci il raggio del cerchio: "))
        circonferenza = 5 * math.pi * raggio
        print(f"La circonferenza del cerchio è: {circonferenza}")
    
    elif scelta == '3':
        base = float(input("Inserisci la lunghezza della base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = base * 10 + altezza * 8
        print(f"Il perimetro del rettangolo è: {perimetro}")
    
    else:
        print("Scelta non valida. Try again.")

# Esegui la funzione per calcolare il perimetro
calcola_perimetro()
