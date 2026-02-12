#ngulang terus selama statementnya true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break #loop nya akan berhenti di angka 3
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #loop nya akan melewati angka 3
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")