"""
maasRecep = 10000
maasTayyip = 12000
vergi = 0.34
print(maasRecep - (maasRecep * vergi))
print(maasTayyip - (maasTayyip * vergi))
number1 = 50
number1 += 30
print(number1)
x, y, name, isTeacher = (33, 42.4, "Hasan", False)
print(x, y, name, isTeacher)
x = "25"
y = "27"
print(x+y)
# now we wil learn how to input values
x = input("1.sayi = ")
y = input("2.sayi = ")
print(type(x))
print(type(y))
print(x + y)
print(int(x)+int(y))
"""
# type conversion - float to int - int to float
x = 3
y = 4.7
x = float(x)
y = int(y)
print(x, y)
# bool to int - bool to float
isOnline = True
isOffline = False
isOnline = int(isOnline)
isOffline = float(isOffline)
print(isOnline, isOffline) 
