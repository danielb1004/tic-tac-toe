matrix = {
    "1": "O",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}
counter = 0
for i in range(1,10):
   if matrix["{}".format(i)] == "{}".format(i):
    counter += 1
if counter == 8:
    print("yes")