players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

#list version
for player in players:
  print(player)
  #output Altuve Bregman Correa Gattis

  #what you name the first variable does not matter. 
  # Generally you want it to be singular version of the plural version


  players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

#tuple compile
for player in players:
  print(player)
#output Altuve Bregman Correa Gattis
#works exactly the same as a list 


players = {
  '2b': 'Christine',
  '3b': 'Brodie',
  'ss': 'Daniel',
  'dh': 'Abe'
}

#dictionary 
 #recquires multiple for variables and must call items to view inside the dictionary
for position,player in players.items():
  print('Position', position)
  print('Player Name', player)\


  #output 

  #Position 2b
  #Player Name Christine
  #Position 3b
  #Player Name Brodie
  #Position ss
  #Player Name Daniel
  #Position dh
  #Player Name Abe