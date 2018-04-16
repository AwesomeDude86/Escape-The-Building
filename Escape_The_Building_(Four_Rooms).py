print('''
+=====================+

Welcome to the escape room

''')
input("Press enter to start your journey")
import time
import sys
import platform,os,webbrowser as w
Key_Possesion=False
def web(url):
  w.open(url)
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
    input("press enter to exit")
    sys.exit(0)

def timed(timer):
  t=time.time()
  input(">")
  if (time.time()-t)>timer:
    print("YOU DIED")
    input("press enter to exit")
    sys.exit()
  return "win"
def level2():
  print("TO be continued")
def climbing():
  print("you are on a staircase climb up or down")
  a=input(">")
  if a=="left":
    print("Great! You are in a room with Pikataros doing trump wall.There's a bowling ball! What do you do Options:(headbutt or bowling ball)")
    a=input(">")
    if a=="bowling ball":
      print("Great choice")
      level2()
    else:
      print("you've been hit by a pen pineapple apple pen aka PPAP")
  else:
    print("Some dogs scratch you to death! THE END!!")
    sys.exit()
def Brown_Room(key=False):
    if key:
        Brown_Direction=input('Whew there was no danger! You can go back or continue. To keep going type "keep walking" !Which Direction now>')
        if Brown_Direction=='keep walking':
            print('You walk out of the room and fall flat onto a moving train.')
            time.sleep(5)
            print('Press enter to duck because of the tunnel')
            timed(2)
            print("YOu go thorught the tunnel. To the left is a door with a cat picture on it and to the right is a door with a dog picture")
            d=input(">")
            if d=="left":
              print("Yes you have got it now you see a army of ugandan knuckles time to jump! Press enter to jump")
              timed(2)
              print("made it")
              timed(4)
              print("made it")
              timed(5)
              print("made it")
              timed(1)
              print("made it(1 more)")
              timed(0.5)
              print("made it")
              time.sleep(0.1)
              print("""They say "we're not dead yet!!!!!!" """)
              running()
              climbing()
            else:
              print("You fell for it,because it was a bait")
              sys.exit()
              
        else:
            if Brown_Direction=='west':
                White_Room()
    else:
        print('The brown door is locked')
        White_Room()
running()
White_Room()
print('''

You land in a room full of fluffly kittens

''')
input("You made it!!!!! Go treat yourself to some ice cream!!!!! And visit our website")
web("http://pythonsnake2017.pythonanywhere.com")

