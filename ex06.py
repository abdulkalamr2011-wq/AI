class VacuumCleaner:

  def __init__(self, location, status):
    self.location = location  # 'A' or 'B'
    self.status = status  # {'A': 'Dirty', 'B': 'Clean'}

  def act(self):
    print(f"Current Location: {self.location}, Status: {self.status}")
    if self.status[self.location] == "Dirty":
      print(f"Action: Clean {self.location}")
      self.status[self.location] = "Clean"
    elif self.location == "A":
      print("Action: Move to B")
      self.location = "B"
    else:
      print("Action: Move to A")
      self.location = "A"


# Example run
agent = VacuumCleaner("A", {"A": "Dirty", "B": "Dirty"})
for _ in range(4):
  agent.act()
