import random
lst=["S","W","G"]

ch=1
user_pts=0
comp_pts=0
print("\t\tWELOCME TO SNAKE WATER GUN GAME")
print("Enter S for Snake")
print("Enter W for Water")
print("Enter G for Gun")
while(ch!="done"):
    #print("\n")
    print("Enter your choice(enter done to exit): ",end="")
    ch=input()
    #print(choice)
    choice=random.choice(lst)
    if(ch==choice):
        print("COMPUTER'S CHOICE: ",choice)
        print("It's a tie")
    elif(ch=="S" and choice=="W"):
        print("COMPUTER'S CHOICE: ",choice)
        print("User wins")
        user_pts=user_pts+1
    elif(ch=="S" and choice=="G"):
        print("COMPUTER'S CHOICE: ",choice)
        print("Computer Wins")
        comp_pts=comp_pts+1 
    elif(ch=="G" and choice=="S"):
        print("COMPUTER'S CHOICE: ",choice)
        print("User wins")
        user_pts=user_pts+1
    elif(ch=="G" and choice=="W"):
        print("COMPUTER'S CHOICE: ",choice)
        print("Computer wins")
        comp_pts=comp_pts+1
    elif(ch=="W" and choice=="G"):
        print("COMPUTER'S CHOICE: ",choice)
        print("User Wins")
        user_pts=user_pts+1
    elif(ch=="W" and choice=="S"):
        print("COMPUTER'S CHOICE: ",choice)
        print("Computer Wins")
        comp_pts=comp_pts+1

print("\t\t RESULT")
print("USER POINTS: ",user_pts)
print("COMPUTER POINTS: ",comp_pts)
if(user_pts>comp_pts):
    print("YOU WIN!!!!!!!")
elif(user_pts<comp_pts):
    print("YOU LOSE!!!!!!")
else:
    print("IT'S A TIE!!!!")
print("\nThank you for playing")    
         
    
        
    


