from random import randrange
from secrets import randbelow
import time
from app import is_valid_time, kill_slack, open_terminal, kill_terminal
import pyautogui

class RobotInteraction():
  def make_interaction(self):
    isValidTime = is_valid_time()

    while(isValidTime==True):
      pyautogui.mouseUp(randrange(1,500), randrange(1,500))
      #open_terminal()
      #kill_terminal()
      time.sleep(10*5)
      isValidTime=is_valid_time()

    if(isValidTime==False):
      kill_slack()
      

myInteraction = RobotInteraction()
myInteraction.make_interaction()
