import pdb
import fileinput
import re
from collections import defaultdict
def read():
  with open('input') as fd:
    data = fd.read()
  return data
def parse(input):
  lines =   [x.lstrip() for x in input.splitlines()]
  deps = defaultdict(set)
  tasks = set()
  for line in lines:
    step = line.split(' ')[1]
    dep = line.split(' ')[-3]
    tasks |= {step, dep}
    deps[dep].add(step)

  done = []
  for _ in tasks: 
    done.append(min(x for x in tasks if x not in done and deps[x] <= set(done)))
 # for _ in tasks: 
 #   tasklist = list(tasks)
 #   tmp = []
 #   for task in tasklist:
 #     if task not in done:
 #       if deps[task] <= set(done):
 #         tmp.append(task)
 #   done.append(min(tmp))

  return set(done)


#print(result)
#HEGMPOAWBFCDITVXYZRKUQNSLJ
#time = 0
#for step in result:
#    time = time + ord(step.lower()) -36
#print("time is %s", time)
# part 2
tasks = set()
# deps maps tasks to a set of prerequisite tasks
deps = defaultdict(set)
for line in fileinput.input('input'):
    a, b = re.findall(r' ([A-Z]) ', line)
    tasks |= {a, b}
    deps[b].add(a)
done = set()
seconds = 0      # total seconds elapsed
counts = [0] * 5 # seconds remaining for worker `i` to finish its current task
work = [''] * 5  # which task worker `i` is performing
while True:
    # decrement each workers remaining time
    # if a worker finishes, mark its task as completed
    for i, count in enumerate(counts):
        if count == 1:
            done.add(work[i])
        counts[i] = max(0, count - 1)
    # while there is an idle worker
    while 0 in counts:
        # find the idle worker
        i = counts.index(0)
        # find a task that has all of its prerequisites satisfied
        candidates = [x for x in tasks if deps[x] <= done]
        if not candidates:
            break
        task = min(candidates)
        tasks.remove(task)
        # have the worker start the selected task
        counts[i] = ord(task) - ord('A') + 61
        work[i] = task
    # if all workers are idle at this point, we are done
    if sum(counts) == 0:
        break
    seconds += 1
print(seconds)
