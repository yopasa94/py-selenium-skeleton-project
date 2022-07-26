import os
from dotenv import load_dotenv

def kill_slack():
  os.system("scripts/killSlack.sh")
  print("Slack process was killed")

def get_final_time():
  load_dotenv()
  return os.getenv('FINAL_TIME')