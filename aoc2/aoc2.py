import socket

s = socket.socket(AF_INET, SOCK_STREAM)

def read():
  with open('input') as fd:
      data = fd.read().splitlines()
  return data

def count(data):
  count2=0
  count3=0
  for i in data:
      seen2=False
      seen3=False
      for k in set(i):
          if i.count(k) == 2 and not seen2:
              count2 +=1
              seen2=True
          if i.count(k) == 3 and not seen3:
              count3 +=1
              seen3=True
  return count2,count3
