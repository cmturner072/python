tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

#merged tags

merged_tags = tags_one | tags_two
print(merged_tags)
#output {'development', 'tutorials', 'python', 'ruby', 'coding'}
#Eliminated the dupicates in the list 


#tags in tags_one but not in tags_two (subtract items)

exculsive_to_tag_one = tags_one - tags_two
print(exculsive_to_tag_one)
#output {'python'}

#tags in tags_two but not in tags_one 
exclusive_to_tag_two = tags_two - tags_one
print(exclusive_to_tag_two)
#output {'ruby', 'development'}

#tags found in both tags_one and tags_two. Looking for the items in both

universal_tags = tags_one & tags_two
print(universal_tags)
#output {'tutorials', 'coding'}