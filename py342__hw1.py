# -*- coding: utf-8 -*-
"""py342_馮定一_hw1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1csJDjHzal0UnnvhR2S_QlVQawZEwCPTs
"""

s1 = {'Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'} 
s2 = {'John', 'Mary', 'Tony', 'Bob', 'Pony', 'Tom', 'Alice'}
print ("數學及格但英文不及格:",s1-s2)
print ("數學不及格但英文及格:",s2-s1)
print ("兩科都及格:",s1 & s2)
print ("全班總共有同學:", s1 | s2)

students = {"Tom":[80, 100, 90, 95], "John":[100, 93, 75, 80]}
for name, values in students.items():
    print(name,':', sum(values)/len(values))