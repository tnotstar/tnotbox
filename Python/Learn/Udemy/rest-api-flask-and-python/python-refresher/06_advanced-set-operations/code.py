friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

nonlocal_nonfriends = abroad.difference(friends)
print(abroad.difference(friends))

local = {"Rolf"}
friends = local.union(abroad)
print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)
