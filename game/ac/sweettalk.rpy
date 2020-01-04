init -15 python:
    Activity(**{
          "name": "sweet_talk",
          "display_name": "Compliment",
          "fun": 1,
          "label": ["sweet_talk"],
          "game_conditions": {"activity":"interact", "flag_female":0},
          "duration": 0,
          "girls_conditions": {
               "ACTIVE":{
                    "not_activity":["sleep"]
                    }
               },
          "icon":"compliment",
          "once_day": "ACTIVE_GIRL"
          })

label sweet_talk:
    call expression game.active_girl.id+"_greet" from _call_expression_24
    python:
        game.smooth_talk(game.active_girl)
    $ game.active_girl.set_flag("interact",1,1,"+")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
