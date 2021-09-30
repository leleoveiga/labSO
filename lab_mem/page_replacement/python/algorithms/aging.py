# This is the file where you must implement the Aging algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you whish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

ALGORITHM_AGING_NBITS = 8
"""How many bits to use for the Aging algorithm"""

class Aging:
  def __init__(self):
    self.frames = {}
    self.pages = {}
    self.ALGORITHM_AGING_NBITS = 8
  
  def put(self, frameId):
    self.frames[frameId] = "1" + (self.ALGORITHM_AGING_NBITS - 1) * "0"

  def evict(self):
    mn = ""
    for frame in self.frames:
      if mn == "" or int(self.frames[frame], 2) < int(self.frames[mn], 2):
        mn = frame
    
    self.frames.pop(mn)
    io = self.pages.pop(mn)
    return (mn, io)

  def clock(self):
    for frame in self.frames:
      self.frames[frame] = "0" + self.frames[frame][1:]

  def access(self, frameId, isWrite):
    self.pages[frameId] = isWrite
    self.frames[frameId] = "1" + self.frames[frameId][1:]
