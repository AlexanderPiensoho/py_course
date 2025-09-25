print("==BOMB AKTIVERAD==")
count_down = 10
for count_down in range (5,0,-1):
    print(f"{count_down}")
print("BOOOOOM!!!!")

age = int (input("Hur gammal är du? "))
if 0<= age <= 17:
    print("Du är mindreårig")
elif age >= 18:
    print("Du är myndigt")
else:
    print("Ange din ålder t.ex. 18")