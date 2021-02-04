
import time,threading

class Singleton:
   __instance = None
   sleepTime = 1
   executeThread = False

   def __init__(self):
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self

   @staticmethod
   def getInstance():
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance


   def startThread(self):
      self.executeThread = True
      self.threadNew = threading.Thread(target=self.foo_target)
      self.threadNew.start()
      print('doing other things...')


   def stopThread(self):
      print("Killing Thread ", self)
      print(self.threadNew)
      self.executeThread = False
      self.threadNew.join()

   def foo(self):
      print("Hello in " + str(self.sleepTime) + " seconds")

   def foo_target(self):
      while self.executeThread:
         self.foo()
         print(self.threadNew)
         time.sleep(self.sleepTime)

         if self.executeThread == False:
            break




sClass = Singleton()
sClass.startThread()
time.sleep(5)
sClass.getInstance().stopThread()

sClass.getInstance().sleepTime = 2
sClass.startThread()

# sClass.getInstance().sleepTime = 2
# time.sleep(5)

# time.sleep(5)
# sClass.getInstance().sleepTime = 3
# sClass.foo()












