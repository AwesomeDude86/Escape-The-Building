import time
import sys
import platform,os
Key_Possesion=False
if platform.system()=="Windows":#If running on windows
  def clear():
      os.system("cls")
else:#Other
    def clear():
      os.system("clear")
def running():
    #RUnning animation
    for X in range(100):
        print((X*"*")+"|")
        time.sleep(0.01)
        clear()
def White_Room(key=False):
    White_Direction=input('You are in a white room with doors on three sides of it. To the west is a green door. To the north is a red door. To the east is a brown door. The brown door is locked with a keyhole in it. Choose a direction.')
    if White_Direction=='west':
        Green_Room()
    else:
        if White_Direction=='north':
            Red_Room()
        else:
            if White_Direction=='east':
                Brown_Room(key)
            else:
                print('Dead end.')
                White_Room()

def Green_Room():
    Green_Direction=input('You are in the green room. There is a key on a table in the middle of the room. Type \"take key\" or a direction. to continue.')
    if Green_Direction=='take key':
        Key_Possesion=True
        White_Room(True)
    else:
        if Green_Direction=='east':
            White_Room()
        else:
            print('Dead end.')
            Green_Room()

def Red_Room():
    print('You are in the red room. You see a tribe of Ugandan Knuckles. They start spitting on you.')
    time.sleep(5)
    print('GAME OVER')

def Brown_Room(key=False):
    if key:
        Brown_Direction=input('Whew there was no danger! You can go back or continue. To keep going pressWhich Direction now>')
        if Brown_Direction=='keep walking':
            print('You walk out of the building into the sun.')
            time.sleep(5)
            print('Congratulations! You have exited the building successfully! You successfully took the key to the brown room, entered the brown room, and walked out of the building successfully!')
        else:
            if Brown_Direction=='west':
                White_Room()
    else:
        print('The brown door is locked')
        White_Room()
running()
White_Room()
input("YOu made it!!!!! Go treat yourself to some ice cream!!!!!")
