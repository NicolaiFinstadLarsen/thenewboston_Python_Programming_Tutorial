def get_gender(sex="Unknown"):
    if sex is "M":
        sex = "Male"
    elif sex is "F":
        sex = "Female"
    return sex

print(get_gender(input("What gender are you? Please type M, F or leave it blank: ")))




