from generate_tree import gen_tree

def generate_button(name,link,number):
    return f"""<button id="nmod_{number}" onclick="toggle_button({number})"><img alt="{name}" src="{link}"><p class="label">{name}</p></button>""", number+1

from mods import bodies, weapons, shields, mods, wild_mods, super_mods

final=[]

with open("C:\\Users\\zacha\\OneDrive\\Documents\\programms\\nova drift webite\\nova-drift-build-maker\\style.html","r") as fr:
    final.append(fr.read())

number=0

# Generate body
current="<div id=\"body\" class=\"gear\">"
for body in bodies:
    link=bodies[body]
    result, number=generate_button(body,link,number)
    current+=result
current+="</div>"
final.append(current)
final.append("<hr>")

with open("C:\\Users\\zacha\\OneDrive\\Documents\\programms\\nova drift webite\\nova-drift-build-maker\\generated\\bodies.txt","w") as f:
    f.write(current)

# Generate weapon
current="<div id=\"weapon\" class=\"gear\">"
for weapon in weapons:
    link=weapons[weapon]
    result, number=generate_button(weapon,link,number)
    current+=result
current+="</div>"
final.append(current)
final.append("<hr>")

with open("C:\\Users\\zacha\\OneDrive\\Documents\\programms\\nova drift webite\\nova-drift-build-maker\\generated\\weapons.txt","w") as f:
    f.write(current)

# Generate shield
current="<div id=\"shield\" class=\"gear\">"
for shield in shields:
    link=shields[shield]
    result, number=generate_button(shield,link,number)
    current+=result
current+="</div>"
final.append(current)
final.append("<hr>")

# Generate mod

start=number

current="<div id=\"mod-trees\">"
for tree in mods:
    value=mods[tree]
    result, number=gen_tree(value,tree,number)
    current+=result
    if (number-start) % 5 == 0:
        current+="<br>"
current+="</div>"
final.append(current)

with open("C:\\Users\\zacha\\OneDrive\\Documents\\programms\\nova drift webite\\nova-drift-build-maker\\generated\\normal mods.txt","w") as f:
    f.write(current)

# Generate wild mod

# Generate super mod

# write to file

with open("C:\\Users\\zacha\\OneDrive\\Documents\\programms\\nova drift webite\\nova-drift-build-maker\\index.html","w") as f:
    f.write("".join(final))