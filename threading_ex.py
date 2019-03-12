import threading
import time

exitFlag = 0
thread_cnt = 8
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print( "%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1



threads = []

for i in range(thread_cnt):
   thread = myThread(i, "Thread-{}".format(str(i)), i % 4)
   threads.append(thread)

for thread in threads:
   thread.start()
print("Exiting Main Thread")

for thread in threads:
   thread.join()
print("Exiting all Threading")
