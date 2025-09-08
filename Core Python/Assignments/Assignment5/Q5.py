####        1 way to solve this

#amount = int(input("Enter amount: "))

#notes = [500, 200, 100, 50, 20, 10, 5]

#print("Notes needed:")

#for note in notes:
#    if amount >= note:
#        count = amount // note    
#        amount = amount % note    
#        print(f"{note} x {count}")


####        Another way to solve this


amount = int(input("Enter amount: "))

notes = [500, 200, 100, 50, 20, 10, 5]
count = 0

for n in notes:
    count += amount // n    
    amount = amount % n     

print("Minimum number of notes needed:", count)
