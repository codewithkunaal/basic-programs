# Rock Paper Scissors Game.
import random
def gamewin(comp , p ):
    if comp == p :              #if  tie
        return None
        
                                #if comp choose rock      
    if comp == "r":             
        if p =="s":
            return False
    elif  p=="p":
        return True

                                #if comp choose paper
    if comp == "p":
        if p =="r":
            return False
    elif  p=="s":
        return True

                                #if comp choose scissors
    if comp == "s":
        if p =="p":
            return False
    elif  p=="r":
        return True
    
print("computer's turn :\nchoosing value... :  " )
randno = random.randint(1,3)
# print(randno)
if randno == 1:
    comp = "r"
elif randno == 2:
    comp = "p"
elif randno == 3:
    comp = "s"

p=input("player's turn  \nchoose scissors(s),paper(p),rock(r) :  ")

a = gamewin(comp,p)
print(f"you choose {p} ")                   #printing value player choose 
print(f"comp choose {comp} ")               #printing value computer choose


if a==None:
    print("game is tie..!")
elif a == True:
    print("hurray!...you win")
else:
    print("oops!...you lose")