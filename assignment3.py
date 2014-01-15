age = 12
sisters_age = 8
cats = 5
more_cats = 2
kittens = 3
owners = 6

new_cats = cats + more_cats
all_cats = new_cats * kittens
age_difference = age - sisters_age
cats_per_owner = all_cats / owners

print "Edith is", age, "years old.", "She is", age_difference, "years older than her sister, Ingrid."
print "They have", cats, "cats and just adopted", more_cats, "more.", "They now have", new_cats, "cats."
print "The cats each had %d kittens. There are now %d cats. " % (kittens, all_cats)
print "They need people to adopt the cats. There are %d who want to adopt, so each owner can have %d cats." % (owners, cats_per_owner)
