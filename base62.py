'''
This program inputs a number and converts it into any given base upto base 62
'''

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
dict_1 = {}
for i in range(62):
    dict_1.update({str(i):chars[i]})

int_list = []
def int_conv(i, base):
    if i//base != 0:
        int_list.append(dict_1[str(i%base)])    
    else:
        int_list.append(dict_1[str(i)])
        return False
    return int_conv(i//base, base)

x_2 = [0]
dec_list = []
def dec_conv(dec, base, sig):
    x = round(dec*base, sig) 
    i, d = str_split(x)
##    print(x)
    if x>x_2[-1]:
        dec_list.append(dict_1[str(i)])
        x_2.append(x)
    else:
        dec_list.append(dict_1[str(i)])
        return False
    return dec_conv(d, base, sig)

def str_split(s):
    i, d = str(s).split('.')
    d = '0.'+d
    return int(i), float(d)

def run():
    n = input("Please enter a number : ")
    base = int(input("Please enter base : "))

    d = 0.0
    if not '.' in n:
        i = int(n)
    else:
        i, d = str_split(n)
        sig = len(n.split('.')[1])

    int_conv(i, base)
    int_list.reverse()
    int_str = ''
    for a in int_list:
        int_str += str(a)
        conv = int_str

    if d != 0.0:
        dec_conv(d, base, sig)
        dec_str = ''
        for a in dec_list:
            dec_str += str(a)
            conv = int_str+'.'+dec_str
    print("Converted value: " + conv)

run()
