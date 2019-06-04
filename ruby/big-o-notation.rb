
def search(name_to_find)
  @people.each do |person|
    if person.name == name_to_find
      return person 
    end
  end
  return nil 
end

search('Larry')

# write it as a binary search 

def search(name_to_find, from = 0, to = nil)
  to ||= @people.count - 1
  mid = (from + to) / 2 

  if name_to_find < @people[mid].name
    search(@people, value, from, mid-1)
  elsif name_to_find > @people[mid].name 
    search(@people, value,  mid+1, to)
  else 
    @people[mid]
  end
end

search('Larry')
