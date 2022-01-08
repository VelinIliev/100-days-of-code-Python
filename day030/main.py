try:
    file =  open("a.txt", "r")
    a_dictonary = {"key": "value"}
    print(a_dictonary["key"])
except FileNotFoundError:
    file =  open("a.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"This key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")

height = 45
weight = 67

if height > 3:
    raise ValueError("Human height should not be over 3 meters")
    
bmi = weight / (height**2)
print(bmi)