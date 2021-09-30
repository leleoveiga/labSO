# This is the file where you must implement the Second Chance algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you wish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class SecondChance:

  def __init__(self):
    from queue import Queue
    self.frames = Queue()
    self.second_chance = {}
    self.pages = {}

  def put(self, frameId):
    self.frames.put(frameId)
    self.second_chance[frameId] = 0

  def evict(self):
    while(True):
      frameId = self.frames.get()
      if(self.second_chance[frameId] == 0):
        self.frames.put(frameId)
        self.second_chance[frameId] = 1
      else:
        self.second_chance.pop(frameId)
        io = self.pages.pop(frameId)
        return (frameId, io)

  def clock(self):
    pass

  def access(self, frameId, isWrite):
    self.pages[frameId] = isWrite
    self.second_chance[frameId] = 0
