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

weapons={
    "Blade":"https://static.wikia.nocookie.net/nova-drift/images/a/ad/Blade.png/revision/latest/scale-to-width-down/100?cb=20191011013410",
    "Blaster":"https://static.wikia.nocookie.net/nova-drift/images/3/3d/Blaster.png/revision/latest/scale-to-width-down/100?cb=20191011013416",
    "Dart":"https://static.wikia.nocookie.net/nova-drift/images/2/29/Dart.png/revision/latest/scale-to-width-down/100?cb=20191011013419",
    "Flak":"https://static.wikia.nocookie.net/nova-drift/images/3/3c/Flak.png/revision/latest/scale-to-width-down/100?cb=20191011013425",
    "Grenade":"https://static.wikia.nocookie.net/nova-drift/images/f/fb/Grenade.png/revision/latest/scale-to-width-down/100?cb=20191011013431",
    "Pulse":"https://static.wikia.nocookie.net/nova-drift/images/a/a9/Pulse.png/revision/latest/scale-to-width-down/100?cb=20191011013435",
    "Railgun":"https://static.wikia.nocookie.net/nova-drift/images/a/ab/Railgun.png/revision/latest/scale-to-width-down/100?cb=20191011013439",
    "Salvo":"https://static.wikia.nocookie.net/nova-drift/images/d/df/Salvo.png/revision/latest/scale-to-width-down/100?cb=20191011013444",
    "Split Shot":"https://static.wikia.nocookie.net/nova-drift/images/0/04/Split_Shot.png/revision/latest/scale-to-width-down/100?cb=20191011013449",
    "Swords":"https://static.wikia.nocookie.net/nova-drift/images/9/96/Swords.png/revision/latest/scale-to-width-down/100?cb=20230925180516",
    "Thermal Lance":"https://static.wikia.nocookie.net/nova-drift/images/a/a4/Thermal_Lance.png/revision/latest/scale-to-width-down/100?cb=20200214110120",
    "Torrent":"https://static.wikia.nocookie.net/nova-drift/images/7/7a/Torrent.png/revision/latest/scale-to-width-down/100?cb=20191011013454",
    "Vortex":"https://static.wikia.nocookie.net/nova-drift/images/5/52/Vortex.png/revision/latest/scale-to-width-down/100?cb=20191011013458"
}

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
    },
    "multiple projectiles":{
        "Volley":"https://static.wikia.nocookie.net/nova-drift/images/5/5d/Volley.png/revision/latest/scale-to-width-down/100?cb=20191011023952",
        "Focus Fire":"https://static.wikia.nocookie.net/nova-drift/images/0/0b/Focus_Fire.png/revision/latest/scale-to-width-down/100?cb=20191011022512",
        "Firing Array":"https://static.wikia.nocookie.net/nova-drift/images/a/af/Firing_Array.png/revision/latest/scale-to-width-down/100?cb=20191011022454",
        "Fusillade":"https://static.wikia.nocookie.net/nova-drift/images/3/39/Fusillade.png/revision/latest/scale-to-width-down/100?cb=20191011022747"
    },
    "damage":{
        "Magnitude":"https://static.wikia.nocookie.net/nova-drift/images/5/5a/Magnitude.png/revision/latest/scale-to-width-down/100?cb=20191011023111",
        "Payload":"https://static.wikia.nocookie.net/nova-drift/images/7/78/Payload.png/revision/latest/scale-to-width-down/100?cb=20191011023139",
        "Splinter":"https://static.wikia.nocookie.net/nova-drift/images/7/70/Splinter.png/revision/latest/scale-to-width-down/100?cb=20191011023722",
        "Charged Shot":"https://static.wikia.nocookie.net/nova-drift/images/7/7e/Charged_Shot.png/revision/latest/scale-to-width-down/100?cb=20191011022025"
    },
    "blast radius":{
        "Blast Radius":"https://static.wikia.nocookie.net/nova-drift/images/4/4b/Blast_Radius.png/revision/latest/scale-to-width-down/100?cb=20191011021659",
        "High Explosive":"https://static.wikia.nocookie.net/nova-drift/images/3/3e/High_Explosive.png/revision/latest/scale-to-width-down/100?cb=20191011022806",
        "Concentrated Blast":"https://static.wikia.nocookie.net/nova-drift/images/5/5b/Concentrated_Blast.png/revision/latest/scale-to-width-down/100?cb=20191011022030",
        "Rupture":"https://static.wikia.nocookie.net/nova-drift/images/3/38/Rupture.png/revision/latest/scale-to-width-down/100?cb=20191011023453"
    },
    "targeting":{
        "Targeting":"https://static.wikia.nocookie.net/nova-drift/images/b/be/Targeting.png/revision/latest/scale-to-width-down/100?cb=20191011023748",
        "Guidance":"https://static.wikia.nocookie.net/nova-drift/images/6/69/Guidance.png/revision/latest/scale-to-width-down/100?cb=20191011022802",
        "Homing Strike":"https://static.wikia.nocookie.net/nova-drift/images/f/f9/Homing_Strike.png/revision/latest/scale-to-width-down/100?cb=20191011022811",
        "Convergence":"https://static.wikia.nocookie.net/nova-drift/images/d/d0/Convergence.png/revision/latest/scale-to-width-down/100?cb=20191011022035"
    }
    # Add all of the mods
}

wild_mods={}
super_mods={}

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