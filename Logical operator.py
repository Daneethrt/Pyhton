'''#Using marks doing code(and,or operators).
marks1=75
marks2=80
marks3=90
marks4=85
print(marks1>70)#(75>70) is true
print(marks2<70)#(80<70) is false
print(marks3>=90)#(90>=90) is true
print(marks4<=85)#(85<=85) is true
print(marks1>70 and marks2<70 and marks3>=90 and marks4<=85)#In 'And' condition every thing should be true else if one is false then ouput is false.In this condition one is flase then ouput is false.
print(marks1>70 or marks2<70 or marks3>=90 or marks4<=85)#In 'or' condition one should be true then ouput is true. In this condition three are true then ouput is true.
print(not marks1>70)#(75>70) if the condition is true then ouput is false and if it's false then ouput is true.
print(not marks2<70)#(80<70)  if the condition is true then ouput is false and if it's false then ouput is true.
print(not marks3>=90)#(90>=90)  if the condition is true then ouput is false and if it's false then ouput is true.
print(not marks4<=85)#(85<=85) if the condition is true then ouput is false and if it's false then ouput is true.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Using 'AND', 'OR' on numbers.
#Note: 1) Zero---->False.
#Note: 2) Non-Zero--->True.
print(10 and 20)# It check whether both are true and then gives true ouput in this condition
print(0 and 10)# In this conditon one is false and one is true, then due to 'AND' conditon then ouput is false (0).
print(10 or 20)# In this condition if one is true then the ouput will be ture and if both are true, then first value will be the output.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
#Using 'AND', 'OR' on strings.
#Note: 1) Empty string---->False.
#Note: 2) Non-empty string--->True.
print('Danny' and '')# It check whether both are true and then gives true ouput in this condition
print('' and 'Danny')# In this conditon one is false and one is true, then due to 'AND' conditon then ouput is false.
print('' or 'Reddy')# In this condition if one is true then the ouput will be ture and if both are true, then first value will be the output.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



