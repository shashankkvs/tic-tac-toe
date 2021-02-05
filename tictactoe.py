board=[" " for i in range(10)]
board[0]="LETS PLAY"
select=1
class Player:
    def __init__(self,name,ch=None):
        self.name=name
        self.ch=ch
        def get_playername(self):
            return self.name
        def get_playerchar(self):
            return self.ch
pl1=Player("sha")
pl2=Player("comp")
block=[int(i) for i in range(1,10)]
def printboard():
    print("="*17)
    print("|| "+board[7]+" || "+board[8]+" || "+board[9]+" ||")
    print("="*17)
    print("|| "+board[4]+" || "+board[5]+" || "+board[6]+" ||")
    print("="*17)
    print("|| "+board[1]+" || "+board[2]+" || "+board[3]+" ||")
    print("="*17)

def isboardfull():
    result = False if " " in board else True
    return result

def insert_l(letter,pos):
    board[pos]=letter
    block.remove(pos)

def clear_l(pos):
    board[pos]=" "

def clear_board():
    (clear_l(i) for i in range(1,10))
def print_welcome():
    print("*"+"WELCOME TO TIC-TACT-TOE"+"*")
    select=input("select-- 1:human vs computer\t2:human1 vs human2\n")
    pl1.name=input("Enter Player 1 Name:")
    if select=="2":pl2.name=input("Enter Player 2 Name:")

    pl1.ch=input("{} choose ur character X  or O:".format(pl1.name))
    while pl1.ch not in ["x","o","X","O"]:
        pl1.ch=input("please choose X or O:")
        
    if "X"== pl1.ch or "x"==pl1.ch:
        pl1.ch="X"
        pl2.ch="O" 
    else: 
        pl1.ch="O"
        pl2.ch="X"
    
def linecrossed(x):
    if (x==board[1] and x==board[2] and x==board[3] ) or (x==board[4] and x==board[5] and x==board[6] )or (x==board[7] and x==board[8] and x==board[9] )or (x==board[1] and x==board[4] and x==board[7]) or (x==board[1] and x==board[5] and x==board[9] ) or(x==board[3] and x==board[5] and x==board[7] )or (x==board[2] and x==board[5] and x==board[8]) or (x==board[3] and x==board[6] and x==board[9]): return True
    else: return False
x=3
def playgame():
    print_welcome()
    while not isboardfull():
        printboard()
        if len(block)%2==1: player=pl1
        else : player=pl2
        try:
            x=int(input("{} select a block:".format(player.name)))
        except:
            print("Enter valid number:")
        while x not in block:
            try:
                x=int(input("{} enter the position number[1-9]:".format(player.name)))
            except:
                print("Enter valid number:")
        insert_l(player.ch,x)
        if linecrossed(player.ch):
            print("***CONGRATULATIONS {} YOU WON GAME***".format(player.name.upper()))
            print("GAME OVER")
            break
            
    if isboardfull():print("Game tied")

if __name__ =="__main__":
    while True:
        playgame()
        x=input("DO YOU WANT TO PLAY ANAOTHER GAME\npress p to play\tpress any other key to quit\n ")
        if x != "p":
            print("*"*5+"THANK YOU"+"*"*5)
            break
        



