import time

# räknar från 0,1,2
for j in range(3):
    print(j)
print("Aktiverar bomb")

# räknar ner från 10 till 1 -- väljer jag -2 så räknar den ner fast med en siffras mellanrum
for i in range(5,0, -1):
    print(i)
    time.sleep(1)

print("BOOOOOOOOMMMM!!!!")