print("**WELCOME to GODZILLA ATTACKS**")

options = [ "A", "B", "C"]

name = input("Hello, what is your name? \n ")

print(f"Hello {name}! Let's start the adventure.")

def start():
  print("It's a beautiful sunny summer day but then you hear a loud ")
  
  for i in range(3):
    print("BOOM")
  
  print("What's that noise? You look outside of your window and see a ginormous, reptilian, angry dinosaur wreaking havoc onto your city.")

  scene1 = input("What do you do?\n A) Check your phone for social media updates \nB) Grab your family and get into the car \nC) Hide under the bed \n") 

  while scene1 not in options:
    print("Not a valid option. Please answer A, B, C")
    scene1 = input("What do you do?\n A) Check your phone for social media updates \nB) Grab your family and get into the car \nC) Hide under the bed \n")

  scene1_options(scene1)
  

def scene1_socialMedia():
  print("You checked twitter, facebook, snapchat and everything was blank, nothing updated. No news appeared about the monster inside the city. Looks like the entire network is out.")
  
  scene2 = input("What do you do next?")


def scene1_car():
  print("You head to the car with your parents and siblings. All of the sudden, a huge shadow encompasses the land. You look back... IT'S GODZILLA HEADING YOUR DIRECTION. Luckily, your mom used to do underground drag racing and she zooms heading North, swerving past people and cars, branches and debris hit the car but nothing phases your mom. 4 hours later.. you all arrive in Alaska. Out of fear, your mom refused to stop driving after Godzilla left the rear mirror view. Your family has escaped, time for a new life in Alaska. THE END")

def scene1_hide():
  print("You hide under your bed. 5 minutes later a huge sonic roar shakes your house and bedroom. You hit your head on your bed frame. Next thing you know, it's morning and you have a huge headache. Turns out.. you just have a cold and it was all a dream. THE END.")

def scene1_options(scene1):
  if scene1 == "A":
    scene1_socialMedia()
  elif scene1 == "B":
    scene1_car()
  elif scene1 == "C":
    scene1_hide()
  else:
    print("try again, choose a,b,c,or d")
    start()


def main():
  start()

main()

# if __name__ == "__main__":  
#   main()