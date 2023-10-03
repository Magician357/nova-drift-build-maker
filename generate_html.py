from generate_tree import gen_tree

def generate_button(name,link,number):
    return f"""<button id="nmod_{number}" onclick="toggle_button({number})"><img alt="{name}" src="{link}"><p class="label">{name}</p></button>""", number+1

# https://nova-drift.fandom.com/wiki/Mods_Overview

# Gear
bodies={
    "Architect":"https://static.wikia.nocookie.net/nova-drift/images/f/fb/Architect.png/revision/latest/scale-to-width-down/100?cb=20191011010925"
}
weapons={}
shields={}

# Mods
mods={
    "velocity":{
        "Velocity":"https://static.wikia.nocookie.net/nova-drift/images/0/0f/Velocity.png/revision/latest/scale-to-width-down/100?cb=20191011023943",
        "Snipe":"https://static.wikia.nocookie.net/nova-drift/images/4/40/Snipe.png/revision/latest/scale-to-width-down/100?cb=20191011023719",
        "Calibrate":"https://static.wikia.nocookie.net/nova-drift/images/7/71/Calibrate.png/revision/latest/scale-to-width-down/100?cb=20191011021717",
        "Incendiary Strike":"https://static.wikia.nocookie.net/nova-drift/images/0/07/Incendiary_Strike.png/revision/latest/scale-to-width-down/100?cb=20191011022824"
    },
    "rate of fire":{
        "Rapid Fire":"https://static.wikia.nocookie.net/nova-drift/images/4/4b/Rapid_Fire.png/revision/latest/scale-to-width-down/100?cb=20191011023405",
        "Burst Fire":"https://static.wikia.nocookie.net/nova-drift/images/b/b0/Burst_Fire.png/revision/latest/scale-to-width-down/100?cb=20191011021713",
        "Warpath":"https://static.wikia.nocookie.net/nova-drift/images/8/8c/Warpath.png/revision/latest/scale-to-width-down/100?cb=20191011023956",
        "Siege Weaponry":"https://static.wikia.nocookie.net/nova-drift/images/c/ce/Siege_Weaponry.png/revision/latest/scale-to-width-down/100?cb=20191011023708"
    }#,
    #"multiple projectiles":{}
    # Add all of the mods
}

final=[]
number=0

# Generate body
current="<div id=\"body\">"
for body in bodies:
    link=bodies[body]
    result, number=generate_button(body,link,number)
    current+=result
current+="</div>"
final.append(current)

with open("C:\\Users\\zacha\\OneDrive\\Documents\\programms\\nova drift webite\\nova-drift-build-maker\\generated\\bodies.txt","w") as f:
    f.write(current)

print(number)

# Generate weapon

# Generate shield

# Generate mod
current="<div id=\"mod-trees\">"
for tree in mods:
    value=mods[tree]
    result, number=gen_tree(value,tree,number)
    current+=result
current+="</div>"
final.append(current)

with open("C:\\Users\\zacha\\OneDrive\\Documents\\programms\\nova drift webite\\nova-drift-build-maker\\generated\\normal mods.txt","w") as f:
    f.write(current)

# Generate wild mod

# Generate super mod