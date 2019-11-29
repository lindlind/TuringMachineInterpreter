config = open("config.txt")
cfg = config.readlines()
config.close()

showStrip = cfg[10].split("'")[1]
if showStrip == 'True':
	showStrip = True
else:
	showStrip = False

f = open("states.txt")
state = f.readline().split(": ")[-1].split("\n")[0]
accS = f.readline().split(": ")[-1].split("\n")[0]
rejS = f.readline().split(": ")[-1].split("\n")[0]
eps = f.readline().split(": ")[-1].split("\n")[0]

def printTape(l, r):
	global eps
	l.reverse()
	while len(l) != 0 and l[-1] == eps:
		l.pop()

	r.reverse()
	while len(r) != 0 and r[-1] == eps:
		r.pop()

	l.reverse()
	s = ""

	sp_sz = 0
	sp_here = 0
	for x in l:
		s += x
		sp_here += 1
		sp_sz += 1
	for x in r:
		s += x
		sp_sz += 1
	if len(r) == 0:
		s += eps
		
	s+='\n'
	for i in range(sp_sz):
		if i == sp_here:
			s += '^'
		else:
			s += ' '
	if len(r) == 0:
		s += '^'

	print(s)

table = {}
for line in f:
	line = line.split("-> ")
	line[0] = line[0].split(" ")
	table[(line[0][0],line[0][1])] = line[1].split("\n")[0]

f.close()

print("filename:")
filename = input()

f = open(filename)
l,r = [],list(f.readline().replace(" ","").replace("\n",""))
r.reverse()
f.close()

if showStrip:
	printTape(l.copy(),r.copy())

N = 0
while True:
	if len(r) == 0:
		c = eps
	else:
		c = r.pop()

	try:
		cell = table[(state,c)].split(" ")
	except:
		print("\nreject")
		print("Steps:", N)
		printTape(l,r)
		exit(0)

	c = cell[0]
	newState = cell[1]

	if cell[2] == ">":
		l.append(c)
	elif cell[2] == "^":
		r.append(c)
	else:
		r.append(c)
		if len(l) == 0:
			c = eps
		else:
			c = l.pop()
		r.append(c)

	if showStrip:
		printTape(l.copy(),r.copy())
	state = newState
	N+=1

	if N % 100000 == 0:
		print(N, "steps was completed")

	if state == accS:
		print("\naccept")
		print("Steps:", N)
		printTape(l,r)
		exit(0)

	if state == rejS:
		print("\nreject")
		print("Steps:", N)
		printTape(l,r)
		exit(0)