import os
import time
from dotenv import load_dotenv

def kill_slack():
  os.system(r"scripts/killSlack.sh")
  print("Slack process was killed")

def open_terminal():
  os.system("scripts/interactTerminal.sh")
  print("Interaction with terminal finished")

def get_final_time():
  load_dotenv()
  return os.getenv('FINAL_TIME')

def is_valid_time():
      envTime = get_final_time()
      finalTime =  time.strptime(envTime, '%H:%M:%S')
      value = time.localtime()
      return ((value.tm_hour==finalTime.tm_hour and value.tm_min>finalTime.tm_min)== False)

def kill_terminal():
  os.system("scripts/killTerminal.sh")
  print("Interaction with terminal finished")