def nejd_slovo(text):
    slova = text.split (" ")
    nejd_slov = "a"
    for i in range(len(slova)):
        if len(slova[i]) > len(nejd_slov):
            nejd_slov = slova[i]
    
    return nejd_slov

print(nejd_slovo("Včera jsme šli na výlet do hor")) #vcera