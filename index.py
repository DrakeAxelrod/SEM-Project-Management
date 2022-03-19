import os
from datetime import datetime, timedelta

class Plan:
  def __init__(self):
    now = datetime.now()
    monday = str((now - timedelta(days=now.weekday())).date())
    friday = str((now - timedelta(days=now.weekday() - 5)).date())
    dir_name = "[" + monday + "_" + friday + "]"
    script_dir = __file__.replace(os.path.basename(__file__), "")
    self.dir = script_dir + dir_name
    if not os.path.isdir(self.dir):
      os.mkdir(self.dir)

p = Plan()