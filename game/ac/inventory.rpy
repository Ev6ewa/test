init -15 python:
    Activity(**{
        "name": "inventory",
        "duration": 0,
        "game_conditions": {
            "inventory":"any",
            "min_energy":0,
            "min_hunger":0,
            "min_grooming":0,
            "min_fun":0
            },
        "icon":"inventory",
        "display_name": "Open inventory",
        "label": ["inventory"]
        })

label inventory:
    python:
        result = False
        while not result == "exit":
            result = renpy.call_screen("inventory")
            if result and result != "exit":
                if isinstance(result,Equip):
                    result.equip()
                elif isinstance(result,Consumable):
                    result.use()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
