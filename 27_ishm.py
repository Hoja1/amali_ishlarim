# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:24:08 2021

@author: user
"""

def royhat_kom(ism,familiya,emil,tel_raqami):
    royhat = {'ism':ism,
              'familiya':familiya,
              'emil':emil,
              'tel_raqami':tel_raqami,
              }
    return royhat

print("Saytga krsh uchun royhat toldring!")
royhatlar=[]
while True:
    print("\nQuydagi malumotlarni krgazing",end='')
    ism=input('ismingiz')
    familiya=input('familyangiz')
    emil=input('emilingiz')
    tel_raqami=input('telefoningiz:')

    royhatlar.append(royhat_kom(ism, familiya, emil, tel_raqami))

    javob =input("yana royhat krgazasizmi(yes/no)")
    if javob == 'no':
        break
print("\nroyghatlar")
for royhat in royhatlar:
    if royhat['tel_raqami']:
        tel_raqami = royhat['tel_raqami']
    else:
        tel_raqami = "Nomalum"
    print(f"{royhat['ism'].title()},{royhat['familiya'].title()},{emil}emil.tel_raqami:{tel_raqami}")
    
         
   
   
    
       
   
    