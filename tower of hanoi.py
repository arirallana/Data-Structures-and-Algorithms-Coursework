'''
program to compute the steps to move n disks from A to B 
'''

def tower_of_hanoi(n , from_rod, to_rod, aux_rod): 
    if n == 1: 
        print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return 
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)
    

def run():
    n = int(input("Please enter number of disks"))
    from_rod = str(input("Please enter name of from-rod"))
    to_rod = str(input("Please enter name of to-rod"))
    aux_rod = str(input("Please enter name of auxilary-rod"))
    tower_of_hanoi(n , from_rod, to_rod, aux_rod)
    print("number of Steps = ", (2**n)-1)

run()
