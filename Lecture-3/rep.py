import time

# ===VARIABLER==== #

my_int = 15
my_float = 15.0
my_bool = True
my_str = "15"

#my_sum = my_int + my_str #det här fungerar ej

my_product = my_int * my_str
#print(my_product) #det här fungerar

my_input_num_str = input("Skriv en siffra mellan 1-20: ")

if my_input_num_str.isdigit():
    if 0<= int(my_input_num_str) <=20:
        my_sum = my_int + int(my_input_num_str)
        print(my_sum)
    else:
        print("Värdet är inte mellan 1-20")

else:
    print("Given input är inte en siffra")


# ===WHILE-LOOP=== #

counter = 0 
# i variable är vanligt förekommande när man räknar på något (index), men andra tydligare variabler är inte fel.
my_bool_counter = True
while my_bool_counter:
    print(f"Loop number: {counter}")
    counter += 1
    time.sleep(0.02)
    if counter > 20:
        my_bool_counter = False

name_list = ["Calle", "Eva", "Bert", "Alex", "Elin"]
#      index.   0       1       2       3       4      
counter2 = 0
repetitions = int(input("How many repetions do you want?: "))
while counter2 < repetitions:
    print(name_list[counter2])
    print(f"loop number: {counter2 + 1}") #Börjar räkna från 1 istället för 0 - men börjar ändå på index 0
    counter2 += 1
    time.sleep(0.02)
print("Loop over")

# ==== LISTOR ==== #
person1 = "Calle"
person2 = "Adam"
person3 = "Anna"
user_list_var = [person1, person2, person3]

user_list = ["Adam", "Anna", "Calle"]
#Index          0       1       2

print(user_list)
print(user_list[1]) #När vi vill plocka ut ett element ur listan använder vi oss av index - här printar vi ut "Anna"

print()
# ==== FOR-LOOP ==== #
for user  in user_list:
    print(user)

# Range = [0, 1, 2, 3, 4] i variabel för index - nästlad forloop fortsätter med j variabel
x = int(input("How many repetitions: "))
for i in range(x):
    for j in range(3): 
        print(f"Print count for {i}, #{j+1}")

user_info1 = ["Alexander", "950802", "Vibyholmsvägen 13"]
user_info2 = ["Vincent", "920802", "Täbyvägen 1337"]
user_info3 = ["Monica", "690802", "Hammardalsslingan 26"]

user_data = [user_info1, user_info2, user_info3] #listception - två-dimitionell lista, alltså listor i listor 

for user in user_data: # user i det här fallet kommer vara varje list t.ex. user_info1
    for user_info in user:
        print(user_info, end= " | ") # end= är en parameter som definerar slutet
    print()

# .append() lägger till en bilaga i slutet. .insert() lägger in mitt i listan
while True:
    add_new_user = input("Do you want to add a new user? Y/N: ")
    if add_new_user.upper() == "Y" or add_new_user.upper() == "YES": #användaren kan välja Y eller YES oberoende av stora eller små bokstäver
        new_user_name = input("Your name: ")
        new_person_id = input("Your person number: ")
        new_adress = input("New Adress: ")
        new_user = [new_user_name, new_person_id, new_adress]
        user_data.append(new_user)
    else:
        break

for user in user_data: # user i det här fallet kommer vara varje list t.ex. user_info1
    for user_info in user:
        print(user_info, end= " | ") # end= är en parameter som definerar slutet
    print()
