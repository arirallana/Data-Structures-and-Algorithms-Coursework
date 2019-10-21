'''
This program inputs a number and converts only the decimal part into base 2
'''


from fractions import Fraction

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
dict_1 = {}
for i in range(62):
    dict_1.update({str(i):chars[i]})

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac
    
def int_part(i):
    x = convert_to_float(i)
    x = x*(2**10)
    print(x)
    int_part = (str(x).split('.')[0])
    print(int_part)

    return int(int_part)
    
int_list = []
def int_conv(x):
    if x//2 != 0:
        int_list.append(dict_1[str(x%2)])    
    else:
        int_list.append(dict_1[str(x)])
        return False
    return int_conv(x//2)



def run():
    n = input("Please enter a number : ")
    n = int_part(n)

    int_conv(n)
    int_list.reverse()
    int_str = ''
    for a in int_list:
        int_str += str(a)
        conv = int_str

    print("Converted value: " '0.' + conv)

run()
