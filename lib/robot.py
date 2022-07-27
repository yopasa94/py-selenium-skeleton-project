from secrets import randbelow
import time
from app import is_valid_time, kill_slack, open_terminal, kill_terminal
import pyautogui

class RobotInteraction():
  def make_interaction(self):
    isValidTime = is_valid_time()

    while(isValidTime==True):
      pyautogui.mouseUp(randbelow(1000), randbelow(1000))
      #open_terminal()
      #kill_terminal()
      time.sleep(5)
      isValidTime=is_valid_time()

    if(isValidTime==False):
      kill_slack()
      

myInteraction = RobotInteraction()
myInteraction.make_interaction()
