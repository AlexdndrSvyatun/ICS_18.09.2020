name = 'Table.csv'
serparator=';'
file = open(name, 'r')
for line in file:
  for data in line.split(separator):
    print(data)
  print("\n")
  
