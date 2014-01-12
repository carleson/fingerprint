import imp
import os
import pluginloader

#////////////////////////////////////////////////////////
# init
#////////////////////////////////////////////////////////
def init():
    print(' ')
    print('Welcome to fingerprint.py')
    print('=========================')

#////////////////////////////////////////////////////////
# loadPlugins
#////////////////////////////////////////////////////////
def loadPlugins():
    for i in pluginloader.getPlugins():
        print("Loading plugin " + i["name"])
        plugin = pluginloader.loadPlugin(i)
        plugin.run()

#////////////////////////////////////////////////////////
# Menu
#////////////////////////////////////////////////////////
def menu():
    print('your options are:')
    print(' ')
    print('1) Addition')
    print('2) Subtraction')
    print('3) Multiplication')
    print('4) Division')
    print('5) Quit fingerprint.py')
    print(' ' )
    return input('Choose your option: ')

#////////////////////////////////////////////////////////
# Main
#////////////////////////////////////////////////////////
init();
choice = menu()

if choice == '5':
    print('Bye')

print(choice)

#loop = 1
#choice = 0
#while loop == 1:
#    choice = menu()
#    if choice == 1:
#        add(input("Add this: "),input("to this: "))
#    elif choice == 2:
#        sub(input("Subtract this: "),input("from this: "))
#    elif choice == 3:
#        mul(input("Multiply this: "),input("by this: "))
#    elif choice == 4:
#        div(input("Divide this: "),input("by this: "))
#    elif choice == 5:
#        loop = 0
#
#print "Thankyou for using calculator.py!"
