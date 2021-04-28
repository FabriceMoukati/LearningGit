from random import *
import numpy as np

def printf(f_id, message):
  f_id.write(message)
  return f_id
  
d=np.arange(100).reshape(10,10)

with open("Output.txt", 'w') as f_id:
  printf(f_id,27*'-')
  printf(f_id,'\n')
  for i in range(len(d[0])):
    for j in range(len(d[1])):
      printf(f_id," %i" %(d[i,j]))
    printf(f_id,"\n")
  f_id.close()
  