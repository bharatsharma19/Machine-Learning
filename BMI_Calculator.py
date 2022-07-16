# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 17:14:54 2022
@author: Bharat Sharma
"""
### Create a BMI Calculation Application

from pywebio.input import *
from pywebio.output import *

def bmicalculator():
    height=input("Please enter your height in cm",type=FLOAT)
    weight=input("Please enter your weight in Kg",type=FLOAT)
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    
    for tuple1,tuple2 in bmi_output:
        if bmi<=tuple1:
            put_text('Your BMI is :%.1f and the person is :%s'%(bmi,tuple2))
            break
        
    
if __name__=='__main__':
    bmicalculator()