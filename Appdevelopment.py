must_run = True

def Addcolor():
    file = open('colorlist.txt', 'a')
    new_color = input("Vil du legge til en farge? ")
    file.write(new_color + '\n')
    file.close()

"""def Removecolor():
    a = read_list()
    file = open('colorlist.txt', 'a')
    bad_color = input("Vil du fjerne en farge? ")
    bad_color = str(bad_color)
    try:
        a.index(bad_color)
        for line in file:
            line = line.replace(bad_color, "")
            file.write(line)
    except ValueError:
        print("Du har ikke fargekoden i samlingen")
    file.close()
"""
def searchlist():
    a = read_list()
    find_color = input("Hvilken farge ser du etter? ")
    find_color = str(find_color)
    try:
        a.index(find_color)
        print("Ja, du har fargen. Den er ligger %s " % a.index(find_color))
    except ValueError:
        print("Du har ikke fargekoden i samlingen")

def read_list():
    file = open('colorlist.txt', 'r')
    Amaryllis = file.readline()
    mylist= []
    while Amaryllis != '':
        Amaryllis =Amaryllis.rstrip('\n')
        mylist.append(Amaryllis)
        Amaryllis = file.readline()
    mylist.sort()
    Sorted = mylist
    file.close()
    return Sorted

def see_list():
    a = read_list()
    print(a)

def print_options():
    print("1: Se listen \n ")
    print("2: Finne en spesifikk farge \n")
    print("3: Legge til en farge \n")
    #print("4: Fjerne en farge \n")
    print("5: Avslutte")


def main():
    global colorlist
    global must_run
    while must_run:
        print_options()
        command = int(input("Hva vil du gjøre? "))
        if command == 1:
            see_list()
        elif command == 2:
            searchlist()
        elif command == 3:
            Addcolor()
        #elif command == 4:
        #    Removecolor()
        elif command == 5:
            must_run = False
        else:
            print("Det du skrev tilsvarer ikke en lovlig kommando")

main()
