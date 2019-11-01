import pdb
from collections import defaultdict
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

  return ''.join(done)


