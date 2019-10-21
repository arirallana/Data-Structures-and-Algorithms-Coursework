'''
This program takes a number and converts it to binary.

'''

def str_split(s):
    i, d = str(s).split('.')
    d = '0.'+d
    return int(i), float(d)

int_list = []
def int_binary(i):
    if i//2 != 0:
        int_list.append(i%2)        
    else:
        int_list.append(i)
        return False
    return int_binary(i//2)

x_2 = [0]
dec_list = []
def dec_binary(dec):
    x = dec*2
    i, d = str_split(x)
    print(x)
    if x>x_2[-1]:
        dec_list.append(i)
        x_2.append(x)
    else:
        dec_list.append(i)
        return False
    return dec_binary(d)

def run():
    n = input("Please enter a number")

    d = 0.0
    if not '.' in n:
        i = int(n)
    else:
        i, d = str_split(n)

    int_binary(i)
    int_list.reverse()
    int_str = ''
    for a in int_list:
        int_str += str(a)
        conv = int_str

    if d != 0.0:
        dec_binary(d)
        dec_str = ''
        for a in dec_list:
            dec_str += str(a)
            conv = int_str+'.'+dec_str
    print(conv)

run()
