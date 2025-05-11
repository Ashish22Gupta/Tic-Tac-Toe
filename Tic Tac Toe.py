print("\033[1m\n||---Tic Tac Toe Game---||\033[0m")
import time
choice = input("Do You Want To Play the Game?\n"
                "-> Press 'ENTER' or 'SPACEBAR an ENTER' to start game!\n"
                "-> Press 'ANY button' To end game!\n"
                "Your Choice: ").strip()
z = 1
while z != 0:
    if choice != "":
        print("Game Ended. Goodbye!")
        break
    else:
        x = 1
        while(x!=0):
            players = input("\nSelect the number of players:\n"
                        "-> Press '1' for One Player Game\n"
                        "-> Press '2' for Two Player Game\n"
                        "Your Selection: ").strip()
            if players == '1':
                temp = 1
                while(temp!=0):
                    mode = input("\nSelect the mode\n -> Press '1' for Simple Mode\n -> Press '2' for Difficult Mode\nYour Choice:- ").strip()
                    if(mode=="1"):
                        print("You have selected simple mode.")
                        print("Ready to play with the Computer...")
                        time.sleep(2)
                        print("Game Started!")
                        board = []
                        win = 0
                        remaining_spaces = [1,2,3,4,5,6,7,8,9]
                        for i in range(3):
                            board1 =[]
                            for j in range(3):
                                x = "|\033[1;34m-\033[0m|"
                                board1.append(x)
                            board.append(board1)
                        for i in range(3):
                            for j in range(3):
                                print(board[i][j],end=" ")
                            print("")
                        def choices():
                            k=1
                            while(k!=0):
                                user = input("\nselect the location:- ")
                                n=0
                                for i in range(len(remaining_spaces)):
                                    if(user==""):
                                        break
                                    elif(not user.isdigit()):
                                        break
                                    elif(int(user)==remaining_spaces[i]):
                                        n+=1
                                    
                                if(n!=1):
                                    print("Inappropriate option! Please select option as per remaining spaces")
                                    k+=1
                                else:
                                    if(user=="1"):
                                        board[0][0]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[0]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="2"):
                                        board[0][1]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[1]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="3"):
                                        board[0][2]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[2]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="4"):
                                        board[1][0]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[3]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="5"):
                                        board[1][1]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[4]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="6"):
                                        board[1][2]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[5]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="7"):
                                        board[2][0]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[6]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="8"):
                                        board[2][1]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[7]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="9"):
                                        board[2][2]="|\033[1;91mX\033[0m|"
                                        remaining_spaces[8]="|\033[1;91mX\033[0m|"
                                        break
                                    elif(user=="" or user==" "):
                                        print("select the option!")
                                    else:
                                        print("Please select the correct option!")
                                        if (len(remaining_spaces)>8 or len(remaining_spaces)<0):
                                            print("This Space is not Presented")
                            selected = []
                            for i in range(9):
                                if(remaining_spaces[i]!="|\033[1;91mX\033[0m|" and remaining_spaces[i]!="|\033[1;92mO\033[0m|"):
                                    selected.append(remaining_spaces[i])
                            import random
                            computer  = random.choice(selected)
                            print("Computer Selection:- ",computer)
                            if(computer==1):
                                board[0][0]="|\033[1;92mO\033[0m|"
                                remaining_spaces[0]="|\033[1;92mO\033[0m|"
                            elif(computer==2):
                                board[0][1]="|\033[1;92mO\033[0m|"
                                remaining_spaces[1]="|\033[1;92mO\033[0m|"
                            elif(computer==3):
                                board[0][2]="|\033[1;92mO\033[0m|"
                                remaining_spaces[2]="|\033[1;92mO\033[0m|"
                            elif(computer==4):
                                board[1][0]="|\033[1;92mO\033[0m|"
                                remaining_spaces[3]="|\033[1;92mO\033[0m|"
                            elif(computer==5):
                                board[1][1]="|\033[1;92mO\033[0m|"
                                remaining_spaces[4]="|\033[1;92mO\033[0m|"
                            elif(computer==6):
                                board[1][2]="|\033[1;92mO\033[0m|"
                                remaining_spaces[5]="|\033[1;92mO\033[0m|"
                            elif(computer==7):
                                board[2][0]="|\033[1;92mO\033[0m|"
                                remaining_spaces[6]="|\033[1;92mO\033[0m|"
                            elif(computer==8):
                                board[2][1]="|\033[1;92mO\033[0m|"
                                remaining_spaces[7]="|\033[1;92mO\033[0m|"
                            elif(computer==9):
                                board[2][2]="|\033[1;92mO\033[0m|"
                                remaining_spaces[8]="|\033[1;92mO\033[0m|"
                        def winner():
                            global win
                            for i in range(3):
                                for j in range(3):
                                    if((board[0][0]=="|\033[1;91mX\033[0m|" and board[0][1]=="|\033[1;91mX\033[0m|" and board[0][2]=="|\033[1;91mX\033[0m|") 
                                        or (board[0][0]=="|\033[1;91mX\033[0m|" and board[1][0]=="|\033[1;91mX\033[0m|" and board[2][0]=="|\033[1;91mX\033[0m|")
                                        or (board[2][0]=="|\033[1;91mX\033[0m|" and board[2][1]=="|\033[1;91mX\033[0m|" and board[2][2]=="|\033[1;91mX\033[0m|")
                                        or (board[0][2]=="|\033[1;91mX\033[0m|" and board[1][2]=="|\033[1;91mX\033[0m|" and board[2][2]=="|\033[1;91mX\033[0m|")
                                        or (board[0][0]=="|\033[1;91mX\033[0m|" and board[1][1]=="|\033[1;91mX\033[0m|" and board[2][2]=="|\033[1;91mX\033[0m|")
                                        or (board[0][2]=="|\033[1;91mX\033[0m|" and board[1][1]=="|\033[1;91mX\033[0m|" and board[2][0]=="|\033[1;91mX\033[0m|")
                                        or (board[1][0]=="|\033[1;91mX\033[0m|" and board[1][1]=="|\033[1;91mX\033[0m|" and board[1][2]=="|\033[1;91mX\033[0m|")
                                        or (board[0][1]=="|\033[1;91mX\033[0m|" and board[1][1]=="|\033[1;91mX\033[0m|" and board[2][1]=="|\033[1;91mX\033[0m|")):
                                        win+=1
                                        print("\n\033[1m🧑 You Win! 🤖 Computer lose!\033[0m")
                                        break
                                    elif((board[0][0]=="|\033[1;92mO\033[0m|" and board[0][1]=="|\033[1;92mO\033[0m|" and board[0][2]=="|\033[1;92mO\033[0m|")
                                        or (board[0][0]=="|\033[1;92mO\033[0m|" and board[1][0]=="|\033[1;92mO\033[0m|" and board[2][0]=="|\033[1;92mO\033[0m|")
                                        or (board[2][0]=="|\033[1;92mO\033[0m|" and board[2][1]=="|\033[1;92mO\033[0m|" and board[2][2]=="|\033[1;92mO\033[0m|")
                                        or (board[0][2]=="|\033[1;92mO\033[0m|" and board[1][2]=="|\033[1;92mO\033[0m|" and board[2][2]=="|\033[1;92mO\033[0m|")
                                        or (board[0][0]=="|\033[1;92mO\033[0m|" and board[1][1]=="|\033[1;92mO\033[0m|" and board[2][2]=="|\033[1;92mO\033[0m|")
                                        or (board[0][2]=="|\033[1;92mO\033[0m|" and board[1][1]=="|\033[1;92mO\033[0m|" and board[2][0]=="|\033[1;92mO\033[0m|")
                                        or (board[1][0]=="|\033[1;92mO\033[0m|" and board[1][1]=="|\033[1;92mO\033[0m|" and board[1][2]=="|\033[1;92mO\033[0m|")
                                        or (board[0][1]=="|\033[1;92mO\033[0m|" and board[1][1]=="|\033[1;92mO\033[0m|" and board[2][1]=="|\033[1;92mO\033[0m|")):
                                        win+=1
                                        print("\n\033[1m🧑 You lose! 🤖 Computer Win!\033[0m")
                                        break
                                break
                        i = 1
                        while(i>0):
                            if win>=1:
                                break
                            compare=0
                            for i in range(3):
                                for j in range(3):
                                    if(board[i][j]=="|\033[1;91mX\033[0m|"):
                                        compare+=1
                                    elif(board[i][j]=="|\033[1;92mO\033[0m|"):
                                        compare+=1    
                            if(compare<8):
                                print("\nRemaining Spaces:- ",end="")
                                for i in range(9):
                                    if(remaining_spaces[i]!="|\033[1;91mX\033[0m|" and remaining_spaces[i]!="|\033[1;92mO\033[0m|"):
                                        print(remaining_spaces[i],end=" ")
                                choices()
                            elif(compare>=8 and win<1):
                                print("\n🙅 Game Draw!")
                                break
                            winner()
                            for i in range(3):
                                for j in range(3):
                                    print(board[i][j],end=" ")
                                print("")
                        i+=1
                        break
                    elif(mode=="2"):
                        print("You had selected Difficult Mode.")
                        print("Ready to play with the Computer...")
                        time.sleep(2)
                        print("Game Started!")
                        board = []
                        win = 0
                        remaining_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                        for i in range(3):
                            board1 = []
                            for j in range(3):
                                x = "|\033[1;34m-\033[0m|"
                                board1.append(x)
                            board.append(board1)

                        def gameboard():
                            for i in range(3):
                                for j in range(3):
                                    print(board[i][j], end=" ")
                                print("")

                        gameboard()

                        def choices():
                            k = 1
                            while (k != 0):
                                user = input("\nselect the location:- ")
                                n = 0
                                for i in range(len(remaining_spaces)):
                                    if (user == ""):
                                        break
                                    elif (not user.isdigit()):
                                        break
                                    elif (int(user) == remaining_spaces[i]):
                                        n += 1

                                if (n != 1):
                                    print("Inappropriate option! Please select option as per remaining spaces")
                                    k += 1
                                else:
                                    if (user == "1"):
                                        board[0][0] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[0] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "2"):
                                        board[0][1] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[1] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "3"):
                                        board[0][2] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[2] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "4"):
                                        board[1][0] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[3] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "5"):
                                        board[1][1] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[4] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "6"):
                                        board[1][2] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[5] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "7"):
                                        board[2][0] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[6] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "8"):
                                        board[2][1] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[7] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "9"):
                                        board[2][2] = "|\033[1;91mX\033[0m|"
                                        remaining_spaces[8] = "|\033[1;91mX\033[0m|"
                                        break
                                    elif (user == "" or user == " "):
                                        print("select the option!")
                                    else:
                                        print("Please select the correct option!")
                                        if (len(remaining_spaces) > 8 or len(remaining_spaces) < 0):
                                            print("This Space is not Presented")

                            selected = []
                            for i in range(9):
                                if (remaining_spaces[i] != "|\033[1;91mX\033[0m|" and remaining_spaces[i] != "|\033[1;92mO\033[0m|"):
                                    selected.append(remaining_spaces[i])

                            def check_win_move(symbol):
                                for temp in range(9):
                                    if remaining_spaces[temp] != "|\033[1;91mX\033[0m|" and remaining_spaces[temp] != "|\033[1;92mO\033[0m|":
                                        row = temp // 3
                                        col = temp % 3
                                        original = board[row][col]
                                        board[row][col] = symbol

                                        if (
                                            (board[0][0] == board[0][1] == board[0][2] == symbol) or
                                            (board[1][0] == board[1][1] == board[1][2] == symbol) or
                                            (board[2][0] == board[2][1] == board[2][2] == symbol) or
                                            (board[0][0] == board[1][0] == board[2][0] == symbol) or
                                            (board[0][1] == board[1][1] == board[2][1] == symbol) or
                                            (board[0][2] == board[1][2] == board[2][2] == symbol) or
                                            (board[0][0] == board[1][1] == board[2][2] == symbol) or
                                            (board[0][2] == board[1][1] == board[2][0] == symbol)
                                        ):
                                            board[row][col] = original
                                            return temp + 1

                                        board[row][col] = original
                                return None

                            computer = check_win_move("|\033[1;92mO\033[0m|")

                            if computer is None:
                                computer = check_win_move("|\033[1;91mX\033[0m|")

                            if computer is None:
                                import random
                                computer = random.choice(selected)

                            print("Computer Selection:-", computer)

                            if (computer == 1):
                                board[0][0] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[0] = "|\033[1;92mO\033[0m|"
                            elif (computer == 2):
                                board[0][1] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[1] = "|\033[1;92mO\033[0m|"
                            elif (computer == 3):
                                board[0][2] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[2] = "|\033[1;92mO\033[0m|"
                            elif (computer == 4):
                                board[1][0] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[3] = "|\033[1;92mO\033[0m|"
                            elif (computer == 5):
                                board[1][1] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[4] = "|\033[1;92mO\033[0m|"
                            elif (computer == 6):
                                board[1][2] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[5] = "|\033[1;92mO\033[0m|"
                            elif (computer == 7):
                                board[2][0] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[6] = "|\033[1;92mO\033[0m|"
                            elif (computer == 8):
                                board[2][1] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[7] = "|\033[1;92mO\033[0m|"
                            elif (computer == 9):
                                board[2][2] = "|\033[1;92mO\033[0m|"
                                remaining_spaces[8] = "|\033[1;92mO\033[0m|"

                        def winner():
                            global win
                            for i in range(3):
                                for j in range(3):
                                    if ((board[0][0] == "|\033[1;91mX\033[0m|" and board[0][1] == "|\033[1;91mX\033[0m|" and board[0][2] == "|\033[1;91mX\033[0m|") 
                                        or (board[0][0] == "|\033[1;91mX\033[0m|" and board[1][0] == "|\033[1;91mX\033[0m|" and board[2][0] == "|\033[1;91mX\033[0m|")
                                        or (board[2][0] == "|\033[1;91mX\033[0m|" and board[2][1] == "|\033[1;91mX\033[0m|" and board[2][2] == "|\033[1;91mX\033[0m|")
                                        or (board[0][2] == "|\033[1;91mX\033[0m|" and board[1][2] == "|\033[1;91mX\033[0m|" and board[2][2] == "|\033[1;91mX\033[0m|")
                                        or (board[0][0] == "|\033[1;91mX\033[0m|" and board[1][1] == "|\033[1;91mX\033[0m|" and board[2][2] == "|\033[1;91mX\033[0m|")
                                        or (board[0][2] == "|\033[1;91mX\033[0m|" and board[1][1] == "|\033[1;91mX\033[0m|" and board[2][0] == "|\033[1;91mX\033[0m|")
                                        or (board[1][0] == "|\033[1;91mX\033[0m|" and board[1][1] == "|\033[1;91mX\033[0m|" and board[1][2] == "|\033[1;91mX\033[0m|")
                                        or (board[0][1] == "|\033[1;91mX\033[0m|" and board[1][1] == "|\033[1;91mX\033[0m|" and board[2][1] == "|\033[1;91mX\033[0m|")):
                                        win += 1
                                        print("\n\033[1m🧑 You Win! 🤖 Computer lose!\033[0m")
                                        break
                                    elif ((board[0][0] == "|\033[1;92mO\033[0m|" and board[0][1] == "|\033[1;92mO\033[0m|" and board[0][2] == "|\033[1;92mO\033[0m|")
                                        or (board[0][0] == "|\033[1;92mO\033[0m|" and board[1][0] == "|\033[1;92mO\033[0m|" and board[2][0] == "|\033[1;92mO\033[0m|")
                                        or (board[2][0] == "|\033[1;92mO\033[0m|" and board[2][1] == "|\033[1;92mO\033[0m|" and board[2][2] == "|\033[1;92mO\033[0m|")
                                        or (board[0][2] == "|\033[1;92mO\033[0m|" and board[1][2] == "|\033[1;92mO\033[0m|" and board[2][2] == "|\033[1;92mO\033[0m|")
                                        or (board[0][0] == "|\033[1;92mO\033[0m|" and board[1][1] == "|\033[1;92mO\033[0m|" and board[2][2] == "|\033[1;92mO\033[0m|")
                                        or (board[0][2] == "|\033[1;92mO\033[0m|" and board[1][1] == "|\033[1;92mO\033[0m|" and board[2][0] == "|\033[1;92mO\033[0m|")
                                        or (board[1][0] == "|\033[1;92mO\033[0m|" and board[1][1] == "|\033[1;92mO\033[0m|" and board[1][2] == "|\033[1;92mO\033[0m|")
                                        or (board[0][1] == "|\033[1;92mO\033[0m|" and board[1][1] == "|\033[1;92mO\033[0m|" and board[2][1] == "|\033[1;92mO\033[0m|")):
                                        win += 1
                                        print("\n\033[1m🧑 You lose! 🤖 Computer Win!\033[0m")
                                        break
                                break

                        i = 1
                        while (i > 0):
                            if win >= 1:
                                break

                            compare = 0
                            for i in range(3):
                                for j in range(3):
                                    if (board[i][j] == "|\033[1;91mX\033[0m|"):
                                        compare += 1
                                    elif (board[i][j] == "|\033[1;92mO\033[0m|"):
                                        compare += 1    

                            if (compare < 8):
                                print("\nRemaining Spaces:- ", end="")
                                for i in range(9):
                                    if (remaining_spaces[i] != "|\033[1;91mX\033[0m|" and remaining_spaces[i] != "|\033[1;92mO\033[0m|"):
                                        print(remaining_spaces[i], end=" ")
                                choices()
                            elif (compare >= 8 and win < 1):
                                print("\n🙅 Game Draw!")
                                break

                            winner()
                            gameboard()

                        i += 1
                        break
                    elif(mode==""):
                        print("Please enter something")
                    elif(not mode.isdigit()):
                        print("Please Select Appropriate Option!")
                break
            elif players == '2':
                print("Ready to play with another Player...")
                time.sleep(2)
                print("Game Started!")
                board = []
                win = 0
                remaining_spaces = [1,2,3,4,5,6,7,8,9]
                for i in range(3):
                    board1 =[]
                    for j in range(3):
                        x = "|\033[1;34m-\033[0m|"
                        board1.append(x)
                    board.append(board1)

                def game_board():
                    for i in range(3):
                            for j in range(3):
                                print(board[i][j],end=" ")
                            print("")

                game_board()

                def player1():
                    k=1
                    while(k!=0):
                        user1 = input("\nPlayer-1 select the location:- ").strip()
                        n=0
                        for i in range(len(remaining_spaces)):
                            if(user1==""):
                                break
                            elif(not user1.isdigit()):
                                break
                            elif(int(user1)==remaining_spaces[i]):
                                n+=1
                            
                        if(n!=1 and user1!=""):
                            print("Inappropriate option! Please select option as per remaining spaces")
                        else:
                            if(user1=="1"):
                                board[0][0]="|\033[1;91mX\033[0m|"
                                remaining_spaces[0]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="2"):
                                board[0][1]="|\033[1;91mX\033[0m|"
                                remaining_spaces[1]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="3"):
                                board[0][2]="|\033[1;91mX\033[0m|"
                                remaining_spaces[2]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="4"):
                                board[1][0]="|\033[1;91mX\033[0m|"
                                remaining_spaces[3]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="5"):
                                board[1][1]="|\033[1;91mX\033[0m|"
                                remaining_spaces[4]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="6"):
                                board[1][2]="|\033[1;91mX\033[0m|"
                                remaining_spaces[5]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="7"):
                                board[2][0]="|\033[1;91mX\033[0m|"
                                remaining_spaces[6]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="8"):
                                board[2][1]="|\033[1;91mX\033[0m|"
                                remaining_spaces[7]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="9"):
                                board[2][2]="|\033[1;91mX\033[0m|"
                                remaining_spaces[8]="|\033[1;91mX\033[0m|"
                                break
                            elif(user1=="" or user1==" "):
                                print("select any location!")
                            else:
                                print("Please select the correct location!")
                                if (len(remaining_spaces)>8 or len(remaining_spaces)<0):
                                    print("This Space is not Presented")


                def player2():    
                    l=1
                    while(l!=0):
                        user2 = input("\nPlayer-2 select the location:- ").strip()
                        m=0
                        for i in range(len(remaining_spaces)):
                            if(user2==""):
                                break
                            elif(not user2.isdigit()):
                                break
                            elif(int(user2)==remaining_spaces[i]):
                                m+=1
                        
                        if(m!=1 and user2!=""):
                            print("Inappropriate option! Please select option as per remaining spaces")
                        else:
                            if(user2=='1'):
                                board[0][0]="|\033[1;92mO\033[0m|"
                                remaining_spaces[0]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2=='2'):
                                board[0][1]="|\033[1;92mO\033[0m|"
                                remaining_spaces[1]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2=='3'):
                                board[0][2]="|\033[1;92mO\033[0m|"
                                remaining_spaces[2]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2=='4'):
                                board[1][0]="|\033[1;92mO\033[0m|"
                                remaining_spaces[3]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2=='5'):
                                board[1][1]="|\033[1;92mO\033[0m|"
                                remaining_spaces[4]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2=='6'):
                                board[1][2]="|\033[1;92mO\033[0m|"
                                remaining_spaces[5]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2=='7'):
                                board[2][0]="|\033[1;92mO\033[0m|"
                                remaining_spaces[6]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2=='8'):
                                board[2][1]="|\033[1;92mO\033[0m|"
                                remaining_spaces[7]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2=='9'):
                                board[2][2]="|\033[1;92mO\033[0m|"
                                remaining_spaces[8]="|\033[1;92mO\033[0m|"
                                break
                            elif(user2==""):
                                print("select the location!")
                            else:
                                print("Please select the correct location!")
                                if (len(remaining_spaces)>8 or len(remaining_spaces)<0):
                                    print("This Space is not Presented")            

                def winner():
                    global win
                    for i in range(3):
                        for j in range(3):
                            if((board[0][0]=="|\033[1;91mX\033[0m|" and board[0][1]=="|\033[1;91mX\033[0m|" and board[0][2]=="|\033[1;91mX\033[0m|") 
                                or (board[0][0]=="|\033[1;91mX\033[0m|" and board[1][0]=="|\033[1;91mX\033[0m|" and board[2][0]=="|\033[1;91mX\033[0m|")
                                or (board[2][0]=="|\033[1;91mX\033[0m|" and board[2][1]=="|\033[1;91mX\033[0m|" and board[2][2]=="|\033[1;91mX\033[0m|")
                                or (board[0][2]=="|\033[1;91mX\033[0m|" and board[1][2]=="|\033[1;91mX\033[0m|" and board[2][2]=="|\033[1;91mX\033[0m|")
                                or (board[0][0]=="|\033[1;91mX\033[0m|" and board[1][1]=="|\033[1;91mX\033[0m|" and board[2][2]=="|\033[1;91mX\033[0m|")
                                or (board[0][2]=="|\033[1;91mX\033[0m|" and board[1][1]=="|\033[1;91mX\033[0m|" and board[2][0]=="|\033[1;91mX\033[0m|")
                                or (board[1][0]=="|\033[1;91mX\033[0m|" and board[1][1]=="|\033[1;91mX\033[0m|" and board[1][2]=="|\033[1;91mX\033[0m|")
                                or (board[0][1]=="|\033[1;91mX\033[0m|" and board[1][1]=="|\033[1;91mX\033[0m|" and board[2][1]=="|\033[1;91mX\033[0m|")):
                                win+=1
                                print("\n\033[1m🏆 Player-1 Win, 💔 Player-2 lose!\033[0m")
                                return True
                            elif((board[0][0]=="|\033[1;92mO\033[0m|" and board[0][1]=="|\033[1;92mO\033[0m|" and board[0][2]=="|\033[1;92mO\033[0m|")
                                or (board[0][0]=="|\033[1;92mO\033[0m|" and board[1][0]=="|\033[1;92mO\033[0m|" and board[2][0]=="|\033[1;92mO\033[0m|")
                                or (board[2][0]=="|\033[1;92mO\033[0m|" and board[2][1]=="|\033[1;92mO\033[0m|" and board[2][2]=="|\033[1;92mO\033[0m|")
                                or (board[0][2]=="|\033[1;92mO\033[0m|" and board[1][2]=="|\033[1;92mO\033[0m|" and board[2][2]=="|\033[1;92mO\033[0m|")
                                or (board[0][0]=="|\033[1;92mO\033[0m|" and board[1][1]=="|\033[1;92mO\033[0m|" and board[2][2]=="|\033[1;92mO\033[0m|")
                                or (board[0][2]=="|\033[1;92mO\033[0m|" and board[1][1]=="|\033[1;92mO\033[0m|" and board[2][0]=="|\033[1;92mO\033[0m|")
                                or (board[1][0]=="|\033[1;92mO\033[0m|" and board[1][1]=="|\033[1;92mO\033[0m|" and board[1][2]=="|\033[1;92mO\033[0m|")
                                or (board[0][1]=="|\033[1;92mO\033[0m|" and board[1][1]=="|\033[1;92mO\033[0m|" and board[2][1]=="|\033[1;92mO\033[0m|")):
                                win+=1
                                print("\n\033[1m💔 Player-1 lose, 🏆 Player-2 Win!\033[0m")
                                return True
                        return False
                    
                i = 1
                while(i>0):

                    if win>=1:
                        break

                    compare=0
                    for i in range(3):
                        for j in range(3):
                            if(board[i][j]=="|\033[1;91mX\033[0m|"):
                                compare+=1
                            elif(board[i][j]=="|\033[1;92mO\033[0m|"):
                                compare+=1    
                    
                    if(compare<8):
                        print("\nRemaining Spaces:- ",end="")
                        for i in range(9):
                            if(remaining_spaces[i]!="|\033[1;91mX\033[0m|" and remaining_spaces[i]!="|\033[1;92mO\033[0m|"):
                                print(remaining_spaces[i],end=" ")
                        
                        player1()

                        game_board()
                        
                        if winner():
                            break
                        
                        print("\nRemaining Spaces:- ",end="")
                        for i in range(9):
                            if(remaining_spaces[i]!="|\033[1;91mX\033[0m|" and remaining_spaces[i]!="|\033[1;92mO\033[0m|"):
                                print(remaining_spaces[i],end=" ")
                        
                        player2()

                        game_board()
                        
                        if winner():
                            break
                    elif(compare>=8 and win<1):
                        print("\033[1m\n🙅 Game Draw!\033[0m")
                        break

                i+=1
                break
            elif players == "":
                print("Please enter something!")
            else:
                print("Please select an appropriate option.")
    
    choice = input("\nDo You Want To Play the Game again?\n"
                "-> Press 'ENTER' or 'SPACEBAR an ENTER' to start game again!\n"
                "-> Press 'ANY button' To end game!\n"
                "Your Choice: ").strip()