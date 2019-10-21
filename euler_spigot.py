'''
This program implements the spigot algorithm to find the digits of e upto 991 decimal places.
'''
#######-----Works for 991 decimal places-----#######

digits_list = []

def find_carry(base, denom, rem_list, carry=0):
    if denom == 1:
        digits_list.append(carry)
        rem_list.reverse()
        return False
    else:
        rem = rem_list[denom-2]
        product = base*int(rem)
        sum_ = carry+product
        rem_list.append(sum_%denom)
        carry = int(sum_/denom)
        return find_carry(base, denom-1, rem_list, carry)

def find_dec_digit(n, denom, base, rem_list = []):
    for i in range(n):
        if rem_list == []:
            rem_list = [1]*(denom-1)
        else:
            for i in rem_list:
                i=i*2
        find_carry(base, denom, rem_list, carry=0)
        
    digits_str = ''
    for a in digits_list:
        digits_str += str(a)
        
    int_conv(2, base)
    int_list.reverse()
    int_str = ''
    for a in int_list:
        int_str += str(a)

    conv = int_str+'.'+digits_str
    print("e = " + conv)
##    print("decimal places = " + str(len(digits_str)))

int_list = []
def int_conv(i, base):
    if i//base != 0:
        int_list.append(i%base)    
    else:
        int_list.append(str(i))
        return False
    return int_conv(i//base, base)

def run():
    base = int(input("Please enter base (<11) "))
    denom = int(input("Please enter highest denominator "))
    n = int(input("Please enter number of decimal digits "))
    find_dec_digit(n, denom, base)

run()
