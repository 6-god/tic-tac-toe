l = [0,1,2,3,4,5,6,7,8]


def instruct():
    print '\n\n\n\n\t\t\t\t\t*****TicTacToe Game*****\n' \
      '\n\n\n**please Enter the position of the board on the basis of given example**\n\n\n' \
      '\t\t__0__|__1__|__2__\n' \
      '\t\t__3__|__4__|__5__\n' \
      '\t\t__6__|__7__|__8__\n'
def display_board():
    global l
    print '\t\t__%r__|__%r__|__%r__\n' %(l[0], l[1], l[2])
    print '\t\t__%r__|__%r__|__%r__\n' %(l[3], l[4],l[5])
    print '\t\t__%r__|__%r__|__%r__\n' %(l[6] , l[7] ,l[8])
def player_input() :
    global l
    global player2
    global player1
    player1=raw_input('\n\nPlayer 1 select a value x or o :')
    player2=0
    if player1=='x':
        player2='o'
    else:
        player2='x'
    print '\n\nPlayer 1 is %r and player 2 is %r\n\n'%(player1,player2)
    display_board()

def win_check(mark):
 return((l[0]==mark and l[1]==mark and l[2]==mark)
        or (l[3]==mark and l[4]==mark and l[5]==mark)
        or (l[6]==mark and l[7]==mark and l[8]==mark)
        or (l[0]==mark and l[3]==mark and l[6]==mark)
        or (l[1]==mark and l[4]==mark and l[7]==mark)
        or (l[2]==mark and l[5]==mark and[8]==mark)
        or (l[0]==mark and l[4]==mark and l[8]==mark)
        or (l[2]==mark and l[4]==mark and l[6]== mark))

def place_marker1():
    global l
    global player1
    global player2
    position_p1 = input('\n\nPlayer 1 enter the postion=')
    print '\n\n'
    l[position_p1] = player1
    display_board()
    if win_check(player1):
        replay(1)




def place_marker2():
    global l
    global player1
    global player2
    postion_p2=input('\n\nPlayer 2 enter the position=')
    l[postion_p2]=player2
    print '\n\n'
    display_board()
    if win_check(player2):
        replay(2)
def replay(winner):
    print "\n\n######_____!!Congratulation!! Player %r won_____##### "%(winner)
    re=raw_input("\n\n\n\n\nEnter 'y' to play again and q to exit::")
    if re=='y':
        play()
    elif re=='q':
        quit()

def play():
    instruct()
    player_input()
    for n in range(0,4):
        place_marker1()
        place_marker2()
play()