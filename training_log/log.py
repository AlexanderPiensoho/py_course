import json
import webbrowser
from menu_func import show_menu

def rick_roll():
    video_url = "https://www.youtube.com/watch?v=xm3YgoEiEDc&list=RDxm3YgoEiEDc&start_radio=1"
    print("Öppnar webbläsaren...")
    webbrowser.open(video_url)

def motivation():
    url_motivation = "https://www.youtube.com/watch?v=OKN8dFO_ZLA"
    print("Dags att bli motiverad")
    webbrowser.open(url_motivation)

while True:
    show_menu()
    menu = input ("\nVälj meny (1-5): ")

    if menu == "1":
        print("Vad tränade du idag?")
        training = input ("Fyll i om du utförde 'löpning' 'cykling' 'gym' eller behöver 'motivation': ")

        if training == 'löpning':
            print("Hoppas du hade ett bra löppass!")

        elif training == 'cykling':
            print("Hoppas cykelpasset gick bra!")

        elif training == 'gym':
            print("Det är alltid bra att lyfta skrot!")
        elif training == 'motivation':
            motivation()

        else:
            print("Du måste välja 'löpning' cykling' eller 'gym'")
        
    elif menu == "2":
        print("Hur långa var distansen på din cykling eller löpning?")
        user_input_distance = input ("Fyll i aktivitet och distance, t.ex. löpning 8.4: ")
        parts = user_input_distance.split()
        
        if len(parts) != 2:
            print("Fel format! skriv t.ex. löpning 8.4")
            continue
        else: 
            activity = parts[0].lower()
            try:
                distance = float(parts[1])
            except ValueError:
                print("Distansen måste vara en siffra")
                continue

            if activity == "cykling":
                print(f"Du cyklade {distance}km, bra jobbat!")
            elif activity == "löpning":
                print(f"Du sprang {distance}km, Bra jobbat!")
            else:
                print("Mata in korrekt värde: t.ex. löpning 8.4")
        
    elif menu == "3":
        print("===LÄSER IN INFORMATION===\n")
        with open('first.json', 'r', encoding='utf-8') as fil:
            data = json.load(fil)
        print(f"Namn: {data['name']}")
        print(f"Ålder: {data['ålder']}")
        print(f"Stad: {data['stad']}")
        print(f"Hobbies: {data['hobbies']}")
        print(f"Favoritmat: {data['favoritmat']}")
        print(f"Äger en bil: {'Ja' if data['har_bil']else 'Nej'}")
        print(f"Äger ett husdjur: {'Ja' if data['har_husdjur']else 'Nej'}\n")
        print("Dirigerar tillbaka till menyn.")

    elif menu == "4":
        print("\nPROGRAMMET AVSLUTAT...\n")
        break

    elif menu == "5":
        rick_roll()

    else:
        print("Du måste göra ett val mellan 1-4")


