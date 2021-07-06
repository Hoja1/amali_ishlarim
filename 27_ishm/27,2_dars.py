# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:42:38 2021

@author: user
"""

mahsulotlarm = {
    'fudbolka':80000,
    'shalvar':85000,
    'tapchka':50000,
    'kepka':30000
    }
bozorlik = ('fudbolka','shalvar','naskiy','navushni')
for mahsulot in mahsulotlarm:
   if mahsulot in bozorlik:
       print(f"{mahsulot.title()} {mahsulotlarm[mahsulot]} so'm")

for buyum in bozorlik:
   if buyum not in mahsulotlarm:
       print(f"iltmos dokoningizga {buyum}ham oib keling")