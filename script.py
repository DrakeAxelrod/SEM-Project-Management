import os
import shutil
from datetime import datetime, timedelta
import os
# from glob import glob
from IPython.display import Markdown
from copy import deepcopy

MONDAY = "monday"
TUESDAY = "tuesday"
WEDNESDAY = "wednesday"
THURSDAY = "thursday"
FRIDAY = "friday"

member_time_slots = {
    "08:00":  "",
    "09:00":  "",
    "10:00":  "",
    "11:00":  "",
    "12:00":  "",
    "13:00":  "",
    "14:00":  "",
    "15:00":  "",
    "16:00":  "",
    "17:00":  "",
    "18:00":  "",
    "19:00":  "",
    "20:00":  "",
}

num_to_slot = {
    8: "08:00",
    9: "09:00",
    10: "10:00",
    11: "11:00",
    12: "12:00",
    13: "13:00",
    14: "14:00",
    15: "15:00",
    16: "16:00",
    17: "17:00",
    18: "18:00",
    19: "19:00",
    20: "20:00",
}


class WhenIsGood(dict):
  def __init__(self):
    self[MONDAY] = deepcopy(member_time_slots)
    self[TUESDAY] = deepcopy(member_time_slots)
    self[WEDNESDAY] = deepcopy(member_time_slots)
    self[THURSDAY] = deepcopy(member_time_slots)
    self[FRIDAY] = deepcopy(member_time_slots)

  def monday(self, name: str, times: list):
    for slot in times:
      if self[MONDAY][num_to_slot[slot]] == "":
        self[MONDAY][num_to_slot[slot]] = name
      else:
        self[MONDAY][num_to_slot[slot]] += ", " + name

  def tuesday(self, name: str, times: list):
    for slot in times:
      if self[TUESDAY][num_to_slot[slot]] == "":
        self[TUESDAY][num_to_slot[slot]] = name
      else:
        self[TUESDAY][num_to_slot[slot]] += ", " + name

  def wednesday(self, name: str, times: list):
    for slot in times:
      if self[WEDNESDAY][num_to_slot[slot]] == "":
        self[WEDNESDAY][num_to_slot[slot]] = name
      else:
        self[WEDNESDAY][num_to_slot[slot]] += ", " + name

  def thursday(self, name: str, times: list):
    for slot in times:
      if self[THURSDAY][num_to_slot[slot]] == "":
        self[THURSDAY][num_to_slot[slot]] = name
      else:
        self[THURSDAY][num_to_slot[slot]] += ", " + name

  def friday(self, name: str, times: list):
    for slot in times:
      if self[FRIDAY][num_to_slot[slot]] == "":
        self[FRIDAY][num_to_slot[slot]] = name
      else:
        self[FRIDAY][num_to_slot[slot]] += ", " + name

  def get_md_string(self):
    table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    table[0] = "|time|"
    table[1] = "|-|"
    for day in self:
      table[0] += f"{day}|"
      table[1] += "-|"
    for day in self:
      i = 2
      for slot in self[day]:
        table[i] = f"|{slot}|"
        i += 1
    for day in self:
      i = 2
      for slot in self[day]:
        table[i] += f"{self[day][slot]}|"
        i += 1
    string = f"## Availability\n\n"
    for s in table:
      string += s + "\n"
    return string + "\n"


class Agenda(dict):
  def __init__(self):
    self[MONDAY] = []
    self[TUESDAY] = []
    self[WEDNESDAY] = []
    self[THURSDAY] = []
    self[FRIDAY] = []

  def monday(self, item: str):
    self[MONDAY].append(item)

  def tuesday(self, item: str):
    self[TUESDAY].append(item)

  def wednesday(self, item: str):
    self[WEDNESDAY].append(item)

  def thursday(self, item: str):
    self[THURSDAY].append(item)

  def friday(self, item: str):
    self[FRIDAY].append(item)

  def get_md_string(self):
    string = "## Agenda\n"
    for day, items in self.items():
      string += f"### {day.capitalize()} \n"
      i = 1
      for item in items:
        string += f"{i}. {item}\n"
        i += 1
    return string + "\n"


class Plan:
  def __init__(self):
    self.wig = WhenIsGood()
    now = datetime.now()
    monday = str((now - timedelta(days=now.weekday())).date())
    friday = str((now - timedelta(days=now.weekday() - 5)).date())
    dir_name = "[" + monday + "_" + friday + "]"
    script_dir = __file__.replace(os.path.basename(__file__), "")
    dir = script_dir + dir_name
    if not os.path.isdir(dir):
      os.mkdir(dir)
    
    if not os.path.isfile(dir + "/Availability.md"):
      with open(dir + "/Availability.md", "w") as f:
        f.write(self.wig.get_md_string())

    if not os.path.isfile(dir + "/Notes.md"):
      with open(dir + "/Notes.md", "w") as f:
        f.write("# Meeting Notes")

    if not os.path.isfile(dir + "/ToDo.md"):
      with open(dir + "/ToDo.md", "w") as f:
        f.write("# To-Do")

    if os.path.isdir("__pycache__"):
      shutil.rmtree("__pycache__")