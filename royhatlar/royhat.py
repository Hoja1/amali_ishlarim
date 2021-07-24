
"""
Created on Sat Jul 24 12:12:10 2021

@author: user
"""

def ishchiliar_uz(ism,familiya,otasni_ismi,tel_raqami,):
    ishchi = {'ism':ism,
           'familiya':familiya,
           'otasni_ismi':otasni_ismi,
           'tel_raqami':tel_raqami,
           
           }
    return ishchi

print("\nishchlar rohati")
ishchiliar = []
while True:
    print(f"\niIshchlar rlayhatni tuzamiz: ")
    ism = input("ismi: ")
    familiya = input("familiyasi: ")
    otasni_ismi = input("otasini ismi: ")
    tel_raqami = input("Telefon raqami: ")
    
    
    ishchiliar.append(ishchiliar_uz(ism,familiya, otasni_ismi, tel_raqami,))
    
    javob = input("yana royhat krgazasizni(yes/no)")
    if javob == 'no':
        break
print("\nRoyhatlar")
for ishchi in ishchiliar:
    if ishchi['otasni_ismi']:
        otasni_ismi=ishchi['otasni_ismi']
    else:
        otasni_ismi = "Nomalum"
    print(f"{ishchi['ism'].title()},{ishchi['familiya'].title()},{ishchi['otasni_ismi'].title()}o'g'li,{ishchi['tel_raqami']}")
    
    
    