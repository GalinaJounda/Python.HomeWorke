# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input())

if n >=1 and n<=5:
    print("Workday")

elif n == 6 or n == 7:
    print("Weekend")
    
else:
    print("It's not a day of tne week")