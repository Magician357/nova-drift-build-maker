mods={
    "Velocity":"https://static.wikia.nocookie.net/nova-drift/images/0/0f/Velocity.png/revision/latest/scale-to-width-down/100?cb=20191011023943",
    "Snipe":"https://static.wikia.nocookie.net/nova-drift/images/4/40/Snipe.png/revision/latest/scale-to-width-down/100?cb=20191011023719",
    "Calibrate":"https://static.wikia.nocookie.net/nova-drift/images/7/71/Calibrate.png/revision/latest/scale-to-width-down/100?cb=20191011021717",
    "Incendiary Strike":"https://static.wikia.nocookie.net/nova-drift/images/0/07/Incendiary_Strike.png/revision/latest/scale-to-width-down/100?cb=20191011022824"
}

def gen_tree(links_dict,treename,number=0):
    names=[a for a in links_dict]
    links=[links_dict[a] for a in links_dict]
    full=f"""<div id="{treename}" class="tree">
<button id="nmod_{number}" onclick="toggle_button({number})"><img alt="{names[0]}" src="{links[0]}"><p class="label">{names[0]}</p></button>
<div class="side"><button id="nmod_{number+1}" onclick="toggle_button({number+1})"><img alt="{names[1]}" src="{links[1]}"><p class="label">{names[1]}</p></button>
<button id="nmod_{number+2}" onclick="toggle_button({number+2})"><img alt="{names[2]}" src="{links[2]}"><p class="label">{names[2]}</p></button></div>
<button id="nmod_{number+3}" onclick="toggle_button({number+3})"><img alt="{names[3]}" src="{links[3]}"><p class="label">{names[3]}</p></button>
</div>"""
    return full, number+4
    
print(gen_tree(mods,"Velocity")[0])