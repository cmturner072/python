#Set is a merger of a list and dictionary. Recquires all of the items to be unique. No duplicates. If you run it. It will not show the duplicate 

tags = {
  'python',
  'coding',
  'tutorials',
}

#print(tags)
#output {'python', 'coding', 'tutorials'}

#print(tags[1])
#Output does not work in this method

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
#output True

print(query_two)
#output False