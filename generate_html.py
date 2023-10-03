from generate_tree import gen_tree

def generate_button(name,link,number):
    return f"""<button id="nmod_{number}" onclick="toggle_button({number})"><img alt="{name}" src="{link}"><p class="label">{name}</p></button>""", number+1

# https://nova-drift.fandom.com/wiki/Mods_Overview

# Gear
bodies={
    "Architect":"https://static.wikia.nocookie.net/nova-drift/images/f/fb/Architect.png/revision/latest/scale-to-width-down/100?cb=20191011010925",
    "Assault":"https://static.wikia.nocookie.net/nova-drift/images/e/e0/Assault.png/revision/latest/scale-to-width-down/100?cb=20191011010930",
    "Battery":"https://static.wikia.nocookie.net/nova-drift/images/6/6d/Battery.png/revision/latest/scale-to-width-down/100?cb=20191011010935",
    "Carrier":"https://static.wikia.nocookie.net/nova-drift/images/b/b7/Carrier.png/revision/latest/scale-to-width-down/100?cb=20191226091451",
    "Courser":"https://static.wikia.nocookie.net/nova-drift/images/9/9b/Courser.png/revision/latest/scale-to-width-down/100?cb=20191011010946",
    "Engineer":"https://static.wikia.nocookie.net/nova-drift/images/d/d8/Engineer.png/revision/latest/scale-to-width-down/100?cb=20191011010952",
    "Firefly":"https://static.wikia.nocookie.net/nova-drift/images/d/d7/Firefly.png/revision/latest/scale-to-width-down/100?cb=20191115103311",
    "Hullbreaker":"https://static.wikia.nocookie.net/nova-drift/images/1/17/Hullbreaker.png/revision/latest/scale-to-width-down/100?cb=20191011010957",
    "Research":"https://static.wikia.nocookie.net/nova-drift/images/2/20/Research.png/revision/latest/scale-to-width-down/100?cb=20191011011002",
    "Sentinel":"https://static.wikia.nocookie.net/nova-drift/images/9/91/Sentinel.png/revision/latest/scale-to-width-down/100?cb=20191011011007",
    "Leviathan":"https://static.wikia.nocookie.net/nova-drift/images/0/0a/Leviathan.png/revision/latest/scale-to-width-down/100?cb=20200921205007",
    "Spectre":"https://static.wikia.nocookie.net/nova-drift/images/9/90/Spectre.png/revision/latest/scale-to-width-down/100?cb=20191115103317",
    "Standard Body":"https://static.wikia.nocookie.net/nova-drift/images/4/45/Standard_Body.png/revision/latest/scale-to-width-down/100?cb=20191011011011",
    "Viper":"https://static.wikia.nocookie.net/nova-drift/images/9/99/Viper.png/revision/latest/scale-to-width-down/100?cb=20191011011020",
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