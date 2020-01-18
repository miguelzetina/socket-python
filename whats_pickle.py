import pickle


d = {1:"hi", 2:"mike"}
msg = pickle.dumps(d)

print(msg)

recd = pickle.loads(msg)
print(recd)
