student_info_dict = {"namn" : "Alexander", "ålder" : "30", "favoritämnen" : ["matte", "svenska"]}
print(student_info_dict)

favorite_subject = input ("Lägg till ett favoritämne: ")
student_info_dict["favoritämnen"].append(favorite_subject)
print(student_info_dict)
student_list = [student_info_dict]

