
rapport = open("e23 read and write example.txt", "w")
rapport.write("Dette er en rapport \n"
              "Her skal jeg legge inn mine tall etterhvert")
rapport.close()

rapport2 = open("e23 read and write example.txt", "r")
text = rapport2.read()
print(text)
rapport2.close



