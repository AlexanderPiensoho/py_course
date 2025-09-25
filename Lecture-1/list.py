favorite_films = ["Batman: Dark Knight", "Poor Things", "Interstellar"]
print(f"\nDina favoritfilmer är{favorite_films}\n".upper())

user_favorite_film = input("Skriv in din favoritfilm: ".upper())
favorite_films.append(user_favorite_film)
print(f"\nDina nya favoritfilmer är{favorite_films}\n".upper())

for i in favorite_films[::1]:
    print(i.upper())

print(f"\nFörsta filmen är {favorite_films[0]}".upper())
print(f"Sista filmen är {favorite_films[-1]}".upper())


#print(f"Din senaste favoritfilm är {favorite_films[3]}")
