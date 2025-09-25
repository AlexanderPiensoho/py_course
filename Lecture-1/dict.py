users = {
    "namn": "Alexander",
    "Ålder": "30",
    "Stad": "Älvsjö"
}

for key, value in users.items():
    print(f"{key}: {value}")

add_key = input("Lägg till ny nyckel: ")
add_value = input("Lägg till värde till nyckeln: ")
users[add_key] = add_value

for key, value in users.items():
    print(f"{key}: {value}")

