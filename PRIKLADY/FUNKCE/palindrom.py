def palindrom(slovo):
    slovo_na = slovo [::-1]
    if slovo == slovo_na:
        return True
    else:
        return False

print(palindrom("oko"))
print(palindrom("robot"))
