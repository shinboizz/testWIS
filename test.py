'''bai1
try:
    string = input('\n- Nhap chuoi: ')
    string_lo = string.lower()
    string_re = string_lo[::-1]
    if string_lo==string_re:
        print('\n=> ',string,'la mot Palindrome\n')
    else:
        print('\n=> ',string,'khong phai la Palindrome\n')
except Exception:
    print('\n=> Loi roi vui long kiem tra lai!\n')

    '''

''''bai2
def fibonacci():
    num = int(input("co bao nhieu so dc tao ra ?: "))
    i = 1
    if num < 0:
        print("vui long nhap so duong! ")
        exit(0)
    elif num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    else:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

print(fibonacci())
input()

'''


'''bai3

num = int(input("nhap 1 so : "))

flag = False

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "khong phai la so nguyen to")
else:
    print(num, "la so nguyen to")
'''


'''bai4
value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print (','.join(value))
'''

'''bai5

num = int(input("nhap 1 so: "))
if (num % 2) == 0:
   print("{0} la so chan".format(num))
else:
   print("{0} la so le".format(num))
'''

'''bai6

x=int(input("Nhập số cần tính giai thừa:"))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print (fact(x))
'''


'''bai7

import random


def compare_numbers(number, user_guess):
    cow = 0
    bull = 0
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            cow += 1
        else:
            if user_guess[i] in number:
                bull += 1
    return cow, bull


if __name__ == "__main__":
    playing = True
    number = str(random.randint(1000, 9999))
    guesses = 0

    print("Let's play a game of Cowbull!")


    while playing:
        user_guess = input("con so ban doan la: ")
        if user_guess == "exit":
            print("good game.")
            break
        if len(user_guess) != 4:
            print("phai nhap 4 so!")
            continue

        cow, bull = compare_numbers(number, user_guess)
        guesses += 1

        print(f" {str(cow)} cows, and {str(bull)} bulls.")

        if user_guess == number:
            playing = False
            print(f"ban chien thang {guesses} guesses! so do la {number}.")
            break
        else:
            print("ban doan sai, thu lai nhe !\n")
            '''

'''bai8
def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(1000,16))
'''