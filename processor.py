import random

f = open("warlock-obsession-list.md", "r")
all = [ x.rstrip() for x in f ]
head = [ x for x in all if ( x != "" and x[0] != "y") ]

for l in head:
    print("{}".format(l))

fl = [ x for x in all if ( x != "" and x[0] == "y") ]
random.shuffle(fl)
i = 0
for l in fl:
    print("| {} - {} | {} |".format(1+(i*3), 3+(i*3), l) )
    i = i + 1

one_hundred = "you awake from a dream wherein you hear the call of the great old one, posessing you, making you stronger, able to mold and manipulate the minds of others. it is the old one's command that you infect the minds of others to do your bidding. not an obsession so much as an inner power, you are able to dominate others at will. once per short rest, you can cast Dominate Person. the dominated person remains subjugataed until freed, until you choose another person or humanoid to dominate or until 1d6 days have passed. See: Dominate Person spell for all other spell aspects"
print("| {} | {} |".format(100, one_hundred) )
