init -15 python:
    Activity(**{
        "name": "propose",
        "display_name": "propose",
        "girls_conditions": {
            "ACTIVE":{
                "not_activity":["sleep"],
                "min_love":160,
                "flag_engagedmike":0
                }
            },
        "icon": "askmarry",
        "game_conditions": {"activity":"interact", "label":"ACTIVE_GIRL_propose", "required_item": ["wedding ring"]},
        "label": ["ACTIVE_GIRL_propose"]
        })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
