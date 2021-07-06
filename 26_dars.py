# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:18:45 2021

@author: user
"""


yosh = int(input("Yoshingizni kriting? \n>>>>"))
if yosh<=4:
   narx = 0
elif yosh<=12:
    narx = 5000
else:
     narx = 10000
    
    
print(f"Sizga krish {narx} so'm")