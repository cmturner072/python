usernames = [
 'jon',
 'tyrion',
 'theon',
 'cersei',
 'sansa',
]
 
#Continue
 
for username in usernames:
 if username == 'cersei':
   print(f'Sorry, {username}, you are not allowed')
   continue
 else:
   print(f'{username} is allowed')
 
#output
#jon is allowed
#tyrion is allowed
#theon is allowed
#Sorry, cersei, you are not allowed
#sansa is allowed


#Break: Search and distroy method

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)


#output 
  #jon
  #tyrion
  #theon
  #cersei was found at index 3
#Stopped at Cersei