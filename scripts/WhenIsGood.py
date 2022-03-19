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
    self.display = (
"""\
|Time|Monday|Tuesday|Wednesday|Thursday|Friday|
|-|-|-|-|-|-|
"""
    )
    self[MONDAY] = deepcopy(member_time_slots)
    self[TUESDAY] = deepcopy(member_time_slots)
    self[WEDNESDAY] = deepcopy(member_time_slots)
    self[THURSDAY] = deepcopy(member_time_slots)
    self[FRIDAY] = deepcopy(member_time_slots)

  def monday(self, name: str, times: list):
    for slot in times:
      self[MONDAY][num_to_slot[slot]] += " " + name + " "

  def tuesday(self, name: str, times: list):
    for slot in times:
      self[TUESDAY][num_to_slot[slot]] += " " + name + " "

  def wednesday(self, name: str, times: list):
    for slot in times:
      self[WEDNESDAY][num_to_slot[slot]] += " " + name + " "

  def thursday(self, name: str, times: list):
    for slot in times:
      self[THURSDAY][num_to_slot[slot]] += " " + name + " "

  def friday(self, name: str, times: list):
    for slot in times:
      self[FRIDAY][num_to_slot[slot]] += " " + name + " "


  def render(self):
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
    string = ""
    for s in table:
      string += s + "\n"
    return Markdown(string)