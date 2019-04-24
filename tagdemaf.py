from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        sense.show_message("Tag dem af")      # Up arrow
      elif event.direction == "down":
        sense.show_letter("Q")      # Down arrow
      elif event.direction == "left": 
        sense.show_letter("A")      # Left arrow
      elif event.direction == "right":
        sense.show_letter("M")      # Right arrow
      elif event.direction == "middle":
        sense.show_letter("K")      # Enter key
      
      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()
