layeredimage bg alettaoffice:
    always:
        "alettaoffice"

init -1 python:
    Room(**{
        "name":"alettaoffice",
        "hours": (8,20),
        "display_name": "Aletta's office",
        "exits": ["office", "personal"],
        "alternate_exits": ["office"],
        "days": "123456",
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"work"
        })

    Activity(**{
        "name": "hack_computer",
        "duration": 0, 
        "display_name": "Hack Aletta's computer",
        "girls_conditions":{"aletta":{"present":False}},
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"room":["alettaoffice"], "flag_underinvestigation":True, 'flagmax_workinvestigation': 99},
        "label": ["hack_computer"],
        "icon":"hack",
        "once_day": True
        })

    Event(**{
        "name":"alettaoffice_init",
        "label": ["alettaoffice_init"],
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

label alettaoffice_init:
    python:
        if "aletta" in HIDDEN and not "alettaoffice" in HIDDEN:
            HIDDEN.append("alettaoffice")
    return

label hack_computer:
    $ cassidy.set_flag('hackattempts', 1, mod='+')

    $ game.set_flag("workinvestigation", max(hero.knowledge() / 10, 5), mod='+')
    $ game.pass_time(1)
    if game.get_flag_value('workinvestigation') >= 100:
        "I put everything I've already learned together, and, and go through the accounting details three times, just to check."
        "Once I eliminate the false trails, there is no doubt. The false transactions were created by Dwayne himself."
        "The CEO of this company is embezzling from it, and I'm the fall guy."
        "And now I have proof."
        return

    if cassidy.get_flag_value('hackattempts') == 1:
        "I sit down at Aletta's computer and log in. I honestly don't know what to look for at first, so I start digging through all the folders regarding accounting."
        "I spend about an hour looking through the accounts, but there's so much there I don't know that I really found anything useful."
        "I will have to try again tomorrow."
    elif cassidy.get_flag_value('hackattempts') == 2:
        "I pick up where I left off and look more deeply into the system, going over my own expense accounts for the last several years."
        "It's been awhile, and I should remember all these numbers, but I don't. I flag a few transactions and take some notes on which ones to check tomorrow."
    elif cassidy.get_flag_value('hackattempts') == 3:
        "I spend an hour looking through the transactions I had flagged. While I am sure I didn't make them, I still can't tell where they came from. I'll check again tomorrow."
    elif cassidy.get_flag_value('hackattempts') == 4:
        "After spending another hour checking the transactions, the trail leads to a set of external accounts from a corporate subsidiary. I'll need to research that subsidiary."
    elif cassidy.get_flag_value('hackattempts') == 5:
        "It turns out the company I found out about last time was set up out of Dwayne's office, but the records are purposefully vague about this. Could Dwayne be the real thief? Alas I have no proof of this."
    elif cassidy.get_flag_value('hackattempts') == 6:
        "I dig more into the corporate subsidary, but I keep deadending on what look like false trails of offshore accounts and companies with no employees."
    else:
        "Just when I think I'm getting somewhere, I end up out of clues. It sure looks like these transactions were inserted into my books by someone."
        "But I cannot tell who, and the only proof of this is my recollection of them. Nobody's going to buy that."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
