import time

print("名前を入力してください")
name = input()
x = 1
if x == 1:

    def japanese_game():
        print("ゲームを本当に始めるにはxキーをおしてください")
        start = input()
        if start == "x":
            print("こちらは開発中のゲームになります。エラーに対して十分な対策を行なってはおりますが、予期せぬエラーについては保証致しかねます。")
            print("本当にこの体験版をプレイしますか。スタートするにはxキーを押してください")
            start2 = input()

            if start2 == "x":
                print("このゲームをプレイする際は必ず、ターミナルの文字の大きさを８より大きくしないでください")
                print()       
                print("############################################################################################################################")
                time.sleep(0.5)
                print("############################################################################################################################")
                time.sleep(0.5)
                print("############################################################################################################################")
                time.sleep(0.5)
                print("###########################################################################################################################")
                time.sleep(0.5)
                print("   eeeeeeeee     eeeeeeeeee        tttttttt     aaaaaaaaa    pppppppppp   eeeeeeeee      ")
                time.sleep(0.5)
                print("   e             e                t                      a    p        p   e")
                time.sleep(0.5)
                print("   eeeeeeeee     eeeeeeeeee       t              aaaaaaaaa    pppppppppp   eeeeeeee")
                time.sleep(0.5)
                print("   e                      e       t              a       a    p.           e")
                time.sleep(0.5)
                print("   eeeeeeeee     eeeeeeeeee        ttttttttt     aaaaaaa.    p.           eeeeeeee")
                time.sleep(0.5)
                print("############################################################################################################################")
                time.sleep(0.5)
                print("############################################################################################################################")
                time.sleep(0.5)
                print("############################################################################################################################")
                time.sleep(0.5)
                print("############################################################################################################################")
                time.sleep(0.5)
                print("============================================================================================================================")
                time.sleep(0.5)
                print("       .---.        ")
                time.sleep(0.5)
                print("      /     \\       ")
                time.sleep(0.5)
                print("     | () () |      <-  ")
                time.sleep(0.5)
                print("      \\  ^  /       ")
                time.sleep(0.5)
                print("       |||||        ")
                time.sleep(0.5)
                print("   ___________      ")  
                time.sleep(0.5)
                print("  /           \\     ")
                time.sleep(0.5)
                print(" /  [†]   [†]  \\    <")
                time.sleep(0.5)
                print("/_______________\\   ")
                time.sleep(0.5)
                print(" |  _   _   _  |    ")
                time.sleep(0.5)
                print(" | |#| |#| |#| |    <- ")
                time.sleep(0.5)
                print(" |             |    ")
                time.sleep(0.5)
                print(" |    .---.    |    ")
                time.sleep(0.5)
                print(" |   |  |  |   |    <- ")
                time.sleep(0.5)
                print(" |   |  |  |   |    ")
                time.sleep(0.5)
                print("_|___|__|__|___|____")
                time.sleep(0.5)
                print("=" * 60)
                print()
                print("TEXT型迷路ゲーム")
                print()
                time.sleep(0.5)
                print("@2025")
                time.sleep(0.5)
                print("ゲームを始めるためにはxキーを押す")
                delta = input()
                if delta == "x":
                    print("ゲームを開始します")

                    # print a main menu and the commands
                    print(
                        """
                        TEXT
                        ========
                        Commands:
                        go [direction]
                        get [item]
                        """
                    )

                    rooms = {
                        "ホール": {
                            # "south": "キッチン",
                            "east": "僕の部屋",
                            "north": "倉庫",
                            "item": "携帯電話",
                            "west": "母、祖父、祖母の寝室",
                        },
                        "倉庫": {"south": "ホール", "item": "ペットポトル"},
                        # "キッチン": {"north": "ホー "item": "包丁"},
                        "僕の部屋": {"west": "ホール", "north": "庭"},
                        "母、祖父、祖母の寝室": {"south": "garden", "east": "ホール", "item": "鍵"},
                        "庭": {"south": "僕の部屋","west":"隣の家","north":"道路","item": "りんごの軸"},
                        "隣の家":{"east":"庭","item":"りんご"},
                        "道路":{"south":"庭"}
                    }
                    currentRoom = "ホール"
                    inventory = []

                    def japanese_gocommand():
                        # print the player's current status
                        print("---------------------------")
                        print("You are in the " + currentRoom)
                        # print the current inventory
                        print("Inventory : " + str(inventory))
                        # print an item if there is one
                        if "item" in rooms[currentRoom]:
                            print("You see a " + rooms[currentRoom]["item"])
                            print("---------------------------")

                    # an inventory, which is initially empty

                    # a dictionary linking a room to other rooms
                    try:
                        while True:
                            japanese_gocommand()

                            # get the player's next 'move
                            # .split() breaks it up into an list array
                            # eg typing 'go east' would give the list:
                            # ['go','east']

                            move = ""
                            while move == "":
                                move = input(">")

                            move = move.lower().split()

                            # if they type 'go' first
                            if move[0] == "go":
                                # check that they are allowed wherever they want to go
                                if move[1] in rooms[currentRoom]:
                                    # set the current room to the new room
                                    currentRoom = rooms[currentRoom][move[1]]
                                # there is no door (link) to the new room
                                else:
                                    print("あなたはそっちにいくことができません!")

                            # if they type 'get' first
                            # if they type 'get' first
                            # 変更後（VS Codeの提案通りにまとめたコード）
                            if move[0] == "get" and "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                                inventory += [move[1]]
                                # display a helpful message
                                print(move[1] + " got!")
                                # delete the item from the room
                                del rooms[currentRoom]["item"]
                                # otherwise, if the item isn't there to get
                            if currentRoom == "キッチン" and "item" in rooms[currentRoom]["item"]:
                                print("おっと。その包丁は呪われていたようです")
                                print("あなたはそのナイフに刺されて死んでしまった")
                                print("game over")
                            else:
                                # tell them they can't get it
                                print("あなたはそれを取ることができません  " + move[1] + "!")
                                if (
                                    currentRoom == "道路"
                                    and "鍵" in inventory
                                    and "りんご" in inventory
                                ):

                                    print(f"{name}さんはなんとこの恐怖の家から脱出することができました")
                                    break

                    except KeyboardInterrupt:
                        print("プログラムにエラーが発生しました")

def second_stage():
    def showInstructions():
        #print a main menu and the commands
        print('''
            RPG Game
            ========
            Commands:
            go [direction]
            get [item]
            ''')

    def showStatus():
        #print the player's current status
        print('---------------------------')
        print('You are in the ' + currentRoom)
        #print the current inventory
        print('Inventory : ' + str(inventory))
        #print an item if there is one
        if "item" in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

    #an inventory, which is initially empty
    inventory = []

    #a dictionary linking a room to other rooms
    rooms = {
        'Hall' : {
            'south' : 'Kitchen'
        },
        'Kitchen' : {
            'north' : 'Hall'
        }
    }

    #start the player in the Hall
    currentRoom = 'Hall'

    showInstructions()

    #loop forever
    while True:

        showStatus()
        print("second stage!")
        #get the player's next 'move'
        #.split() breaks it up into an list array
        #eg typing 'go east' would give the list:
        #['go','east']
        move = ''
        while move == '':
            move = input('>')

        move = move.lower().split()

        #if they type 'go' first
        if move[0] == 'go':
            #check that they are allowed wherever they want to go
            if move[1] in rooms[currentRoom]:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            #there is no door (link) to the new room
            else:
                print('You can\'t go that way!')

        #if they type 'get' first
        if move[0] == 'get' :
            #if the room contains an item, and the item is the one they want to get
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                #add the item to their inventory
                inventory += [move[1]]
                #display a helpful message
                print(move[1] + ' got!')
                #delete the item from the room
                del rooms[currentRoom]['item']
            #otherwise, if the item isn't there to get
            else:
                #tell them they can't get it
                print('Can\'t get ' + move[1] + '!')



if name == "":
    i = 0
    print("名前を入力してください")
    name = input()
    i += 1
    time.sleep(0.5)
else:
    print(f"こんにちは{name}さん。始めましょう")

    print("ゲームをスタートするにはyを押してください")
    dell = input()
    if dell == "y":
        japanese_game()
