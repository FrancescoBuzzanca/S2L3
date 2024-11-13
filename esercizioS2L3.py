città = input("inserisci il nome della tua città:") #si chiede all'utente di inserire il nome della città
animale =input("inserisci il nome del tuo pet:") #si chiede di inserire il nome dell'animale
colore =input("inserisci il tuo colore preferito:") #si chiede di inserire il colore

nome_band = colore + animale + città #per creare il nome della band si uniranno i dati inseriti precedentemente 


print(f"il nome della tua band è:{nome_band}") #dirà il nome della tua band!

risposta = input("ti piace il nome? (si/no): ")

if risposta == "si":
    print("è stato un piacere aiutarti!")
elif risposta == "no":
    print("usa la tua fantasia")

