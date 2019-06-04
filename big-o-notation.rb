
def search(name_to_find)
  @people.each do |person|
    if person.name == name_to_find
      return person 
    end
  end
  return nil 
end

search('Larry')
