
d = {
	'value1': 5,
	'value2': 4,
	'value3': 3,
	'value4': 2,
	'value5': 1,
}

answer = 1
val=list(d.values())
for i in val:
	answer = answer*i
print(answer)
