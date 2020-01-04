layeredimage bg church:
    always:
        "church"

init -2 python:
    Room(**{
        "name":"church",
        "hours":(9,11),
        "days":"7",
        "display_name": "Church",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "music": "music/O_bone_Jesu.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "attend_mass",
        "duration": 1,
        "game_conditions": {
            "room":["church"],
            "min_grooming":5,
            "min_fun":1,
            "min_hunger":1,
            "min_energy":1
            },
        "fun": -2,
        "icon":"mass",
        "display_name": "Attend mass",
        "label": ["attend_mass"],
        })

label attend_mass:
    "I attend a service."
    if game.get_flag_value("female"):
        $ NOTIFICATIONS.append(["{image=ui/icon_good.png}+1",2])
    $ game.set_flag("morality",1,mod="+")

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
