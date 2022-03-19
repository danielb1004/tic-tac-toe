from ast import Break
import os

from numpy import true_divide

# clear console
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# Interfase
print("///////////////////////////////")
print("This game is tik tak tok")
print("--------------------------------")
print("---|-1-|-2-|-3-|---")
print("---|-4-|-5-|-6-|---")
print("---|-7-|-8-|-9-|---")
print("--------------------------------")


matrix = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

# interactive inteface
def interactive_matrix():
    print("--------------------------------")
    print("---|-{}-|-{}-|-{}-|---".format(matrix["1"], matrix["2"], matrix["3"]))
    print("---|-{}-|-{}-|-{}-|---".format(matrix["4"], matrix["5"], matrix["6"]))
    print("---|-{}-|-{}-|-{}-|---".format(matrix["7"], matrix["8"], matrix["9"]))
    print("--------------------------------")

def check_win(matrix):
    if matrix["1"] == matrix["2"] == matrix["3"] != " ":
        return True
    elif matrix["4"] == matrix["5"] == matrix["6"] != " ":
        return True
    elif matrix["7"] == matrix["8"] == matrix["9"] != " ":
        return True
    elif matrix["1"] == matrix["4"] == matrix["7"] != " ":
        return True
    elif matrix["2"] == matrix["5"] == matrix["8"] != " ":
        return True
    elif matrix["3"] == matrix["6"] == matrix["9"] != " ":
        return True
    elif matrix["1"] == matrix["5"] == matrix["9"] != " ":
        return True
    elif matrix["3"] == matrix["5"] == matrix["7"] != " ":
        return True
    else:
        return False

def control():
    entry = input("Enter your number: ")
    try:
        int(entry)
    except:
        print("Please enter a number")
        entry = input("Enter your number: ")   
    if int(entry) > 9 or int(entry) < 1:
        print("Wrong number")    
    if matrix[entry] == "X" or matrix[entry] == "O":
        print("This number is already taken")
        clearConsole()
        interactive_matrix() 
        control()   
    else:
        matrix[entry] = "X"

def machine_movement():
    controlm = True    
    while True: 
        if matrix["5"] == "5":
            matrix["5"] = "O"
            break
        if matrix["5"] == "X" and matrix["7"] == "7":
            matrix["7"] = "O"
            break
        if matrix["1"] == matrix["2"] and matrix["3"] == "3":
            matrix["3"] = "O"
            break
        if matrix["4"] == matrix["5"] and matrix["6"] == "6":
            matrix["6"] = "O"
            break
        if matrix["7"] == matrix["8"] and matrix["9"] == "9":
            matrix["9"] = "O"
            break
        if matrix["1"] == matrix["4"] and matrix["7"] == "7":
            matrix["7"] = "O"
            break
        if matrix["2"] == matrix["5"] and matrix["8"] == "8":
            matrix["8"] = "O"
            break
        if matrix["3"] == matrix["6"] and matrix["9"] == "9":
            matrix["9"] = "O"
            break
        if matrix["1"] == matrix["5"] and matrix["9"] == "9":
            matrix["9"] = "O"
            break
        if matrix["3"] == matrix["5"] and matrix["7"] == "7":
            matrix["7"] = "O"
            break
        if matrix["2"] == matrix["3"] and matrix["1"] == "1":
            matrix["1"] = "O"
            break
        if matrix["5"] == matrix["6"] and matrix["4"] == "4":
            matrix["4"] = "O"
            break
        if matrix["8"] == matrix["9"] and matrix["7"] == "7":
            matrix["7"] = "O"
            break
        if matrix["4"] == matrix["7"] and matrix["1"] == "1":
            matrix["1"] = "O"
            break
        if matrix["5"] == matrix["8"] and matrix["2"] == "2":
            matrix["2"] = "O"
            break
        if matrix["6"] == matrix["9"] and matrix["3"] == "3":
            matrix["3"] = "O"
            break   
        if matrix["5"] == matrix["9"] and matrix["1"] == "1":
            matrix["1"] = "O"
            break
        if matrix["5"] == matrix["7"] and matrix["3"] == "3":
            matrix["3"] = "O"
            break
        if matrix["1"] == matrix["3"] and matrix["2"] == "2":
            matrix["2"] = "O"
            break
        if matrix["4"] == matrix["6"] and matrix["5"] == "5":
            matrix["5"] = "O"
            break
        if matrix["7"] == matrix["9"] and matrix["8"] == "8":
            matrix["8"] = "O"
            break
        if matrix["1"] == matrix["7"] and matrix["4"] == "4":
            matrix["4"] = "O"
            break
        if matrix["2"] == matrix["8"] and matrix["5"] == "5":
            matrix["5"] = "O"  
            break
        if matrix["3"] == matrix["9"] and matrix["6"] == "6":
            matrix["6"] = "O"  
            break  
        if matrix["1"] == matrix["9"] and matrix["5"] == "5":
            matrix["5"] = "O"  
            break
        if matrix["3"] == matrix["7"] and matrix["5"] == "5":
            matrix["5"] = "O"  
            break
        if matrix["1"] == matrix["6"] and matrix["3"] == "3":
            matrix["3"] = "O"  
            break
        if matrix["3"] == matrix["4"] and matrix["1"] == "1":
            matrix["1"] = "O"  
            break
        if matrix["4"] == matrix["9"] and matrix["7"] == "7":
            matrix["7"] = "O"  
            break
        if matrix["7"] == matrix["6"] and matrix["9"] == "9":
            matrix["9"] = "O"  
            break
        if matrix["7"] == matrix["2"] and matrix["1"] == "1":
            matrix["1"] = "O"
            break
        if matrix["2"] == matrix["9"] and matrix["3"] == "3":
            matrix["3"] = "O"
            break
        if matrix["8"] == matrix["3"] and matrix["9"] == "9":
            matrix["9"] = "O"
            break
        if matrix["8"] == matrix["1"] and matrix["7"] == "7":
            matrix["7"] = "O"
            break
        if matrix["8"] == matrix["4"] and matrix["7"] == "7":
            matrix["7"] = "O"
            break
        if matrix["8"] == matrix["6"] and matrix["9"] == "9":
            matrix["9"] = "O"
            break
        if matrix["6"] == matrix["2"] and matrix["3"] == "3":
            matrix["3"] = "O"
            break
        if matrix["2"] == matrix["4"] and matrix["1"] == "1":
            matrix["1"] = "O"
            break
        if matrix["1"] == matrix["9"] and matrix["6"] == "6":
            matrix["6"] = "O"
            break
        if matrix["3"] == matrix["7"] and matrix["4"] == "4":
            matrix["4"] = "O"
            break
        if matrix["5"] == matrix["6"] and matrix["7"] == "7":
            matrix["9"] = "O"
            break
        if matrix["4"] == matrix["6"] and matrix["7"] == "7":
            matrix["7"] = "O"
            break
        if matrix["2"] == matrix["8"] and matrix["1"] == "1":
            matrix["1"] = "O"
            break
        if matrix["3"] == matrix["5"] and matrix["9"] == "9":
            matrix["9"] = "O"
            break
        break
    



while True:  
    control()
    clearConsole()
    interactive_matrix()
    if check_win(matrix) == True:
        print("You Win")
        break
    machine_movement()
    clearConsole()
    interactive_matrix()
    if check_win(matrix) == True:
        print("You lose")
        break
    counter = 0
    for i in range(1,10):
        if matrix["{}".format(i)] == "{}".format(i):
            counter += 1
    if counter == 0:
        print("TIE!!!")
        break
        
            


        
     

    
    




