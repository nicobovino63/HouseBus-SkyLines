from os import system, name
import time
from tqdm import tqdm
import argparse

# 'ls': list_
# 'mv <state abbreviation>': stateabbrev_
# 'help': help_

class TermCol:
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  ENDC = '\033[0m'


def cleanup():
  if name == 'posix':
    _ = system('clear')
  elif name == 'nt':
    _ = system("cls")


def cli(*args):
  prompt = input(TermCol.GREEN + "\n\nEnter a Command ~$ " + TermCol.ENDC).lower()
  if prompt == 'ls':
    Cmd.run_list()
  if prompt == '-h':
    Cmd.run_help()
  if prompt == 'mv':
    Cmd.run_mv('')


def system_clock():
  timeout = time.time() + 60 / 12
  while True:
    localtime = time.localtime()
    strftime = time.strftime("%I : %M : %S %p", localtime)
    print(strftime, end = "", flush = True)
    print("\r", end = "", flush = True)
    if strftime == 5 or time.time() > timeout:
      break

  for i in tqdm(range(12)):
    time.sleep(0.2)

  time.sleep(1)
  cleanup()
  cli()


class Cmd:
  def run_list():
    list_ = ["1. (AL) Alabama", "2. (AK) Alaska", "3. (AZ) Arizona", "4. (AR) Arkansas\n", "5. (CA) California", "6. (CO) Colorado", "7. (CT) Connecticut\n", "8. (DE) Delaware\n", "9. (FL) Florida\n", "10. (GA) Georgia\n", "11. (HI) Hawaii\n", "12. (ID) Idaho", "13. (IL) Illinois", "14. (IN) Indiana", "15. (IA) Iowa\n", "16. (KS) Kansas", "17. (KY) Kentucky\n", "18. (LA) Louisiana\n", "19. (ME) Maine", "20. (MD) Maryland", "21. (MA) Massachussetts", "22. (MI) Michigan", "23. (MN) Minnesota", "24. (MS) Mississippi", "25. (MO) Missouri"]
    for x in range(len(list_)):
      print(list_[x])

    time.sleep(1)
    cli()

  def run_help():
    help_ = [TermCol.YELLOW + "'ls': List States", "'-h': You are Here" , "'mv <state abbreviation>': Grab Index of State Counties" + TermCol.ENDC]
    for x in range(len(help_)):
      print(help_[x])

    time.sleep(1)
    cli()

  def run_mv(abbrev):
    abbrev_list = ["al", "ak"]
    abbrev = input(TermCol.RED + "mv " + TermCol.ENDC).lower()
    if abbrev in abbrev_list:
      print(abbrev)
    if abbrev not in abbrev_list:
      exit()


system_clock()

