student = {
    "Tawab" : 80,
    "Ahmed" : 75,
    "Nafi" : 60,
    "Ishraq" : 96
}
 
threshold = 70

# Convert Dictionary to List using items()
list_from_dict = [(key, score) for key, score in student.items() if score > threshold]

# Display the result
print (list_from_dict)