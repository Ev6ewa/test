init -100 python:
    import copy
    import yaml
    import itertools



    game = None

    config.auto_voice = "vo/{id}.mp3"

    GIRLS = {}
    DATES = {}
    ROOMS = {}
    ACTIVITIES = {} 
    EVENTS = {} 
    HIDDEN = []
    HIDE_UI = False
    SEXATTRIBUTES = []

    FLAGS = {}
    SEASONS = ["spring","summer","fall","winter"]
    DAYS = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    gallery_cg_items = []

    KEYS = []
    CODE = ["up","down","left","right","up","down","left","right","b","a"]
    CHEAT = False
    persistent.difficulty = 0
    persistent.notifications = True
    persistent.randomness = 1
    persistent.skip_tutorial = False
    persistent.fast = True
    persistent.room_display = "h"
    persistent.window_opacity = 1.0
    WORK_DIF = 50
    WORK_DIF_2 = 100


    NOTIFICATIONS = []

    randint = renpy.random.randint
    randchoice = renpy.random.choice
    random = renpy.random.random

    def clean_notifications():
        global NOTIFICATIONS
        new = []
        for i in range(len(NOTIFICATIONS)):
            NOTIFICATIONS[i][1] -= 1
            if not NOTIFICATIONS[i][1] == 0:
                new.append(NOTIFICATIONS[i])
        NOTIFICATIONS = new
        renpy.restart_interaction()
define bree_sasha = Character("Bree & Sasha", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define aletta_say = Character("Aletta", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define cassidy_say = Character("Cassidy", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define lavish_say = Character("Lavish", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define palla_say = Character("Palla", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define kylie_say = Character("Kylie", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define alexis_say = Character("Alexis", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define shiori_say = Character("Shiori", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define natalie_say = Character("Natalie", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define ayesha_say = Character("Ayesha", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define lexi_say = Character("Lexi", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define kleio_say = Character("Kleio", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define anna_say = Character("Anna", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define audrey_say = Character("Audrey", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define harmony_say = Character("Harmony", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define samantha_say = Character("Samantha", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define unknown_girl_say = Character("Girl", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
define thug_say = DynamicCharacter("thug_name", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define jack_say = Character("Jack", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define geezer_say = Character("Old pervert", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define dwayne_say = Character("Dwayne", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define master_say = Character("The Master", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define ryan_say = Character("Ryan", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define andre_say = Character("Andrealphus", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define artist_say = Character("Artist", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define man_say = Character("Shady looking man", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define man2_say = Character("Handsome man", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define priest_say = Character("Priest", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define bouncer_say = Character("Bouncer", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define coworker_say = Character("Coworker", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define security_say = Character("Security Officer", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define show_owner_say = Character("Shop owner", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define mike_say = Character("Mike", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define scottie_say = Character("Scottie", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define shawn_say = Character("Shawn", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define manager_say = Character("Manager", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define jeff_say = Character("Jeff the accountant", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
define thug_name = "Thug"


define hero.say = Character("hero.name", who_outlines=[ (1, '#0099ff') ], who_color="#ffffff", dynamic=True)
define active_girl.say = Character("game.active_girl.name", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff", dynamic=True)
define meet_girl.say = Character("[meet_girl.name]", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff", dynamic=True)
define date_girl.say = Character("[date_girl.name]", who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff", dynamic=True)
init -10 python:

    files = renpy.list_files()

    for f in files:
        if f.rsplit("/")[0] == "bg" and f[-4:] in ['webp']:
            
            name = f.split("/")[-1].split(".")[0]
            
            renpy.image(name,f)
        elif f.rsplit("/")[0] == "ch" and f[-4:] in ['webp']:
            if "st" in f.split("/") or "ev2" in f.split("/"):
                name = f.split("/")[-1].split(".")[0]
            else:
                name = tuple(f.split("/")[-1].split(".")[0].split("_"))
            
            renpy.image(name,f)
        elif f[-3:] == "png" and "action_icons" in f:
            
            renpy.image(f.split("/")[-1].split(".")[0]+" idle", LiveComposite(
                                                        (60, 60),
                                                        (0, 0), "ui/icon_bg.png",
                                                        (5, 5), f,
                                                        ))
            renpy.image(f.split("/")[-1].split(".")[0]+" hover", LiveComposite(
                                                        (60, 60),
                                                        (0, 0), "ui/icon_bg.png",
                                                        (5, 5), f,
                                                        (0, 0), "ui/icon_fg.png",
                                                        ))


    files = renpy.list_files()
    files = [f for f in files if f[-3:] == "grl" and "ch" in f]
    for f in files:
        with renpy.file(f) as stream:
            d = yaml.load(stream)
            g = Girl(**d)
            exec(g.id+" = g")

    Activity(**{
        "name": "cheats",
        "duration": 0,
        "game_conditions": {
            "min_energy":0,
            "min_hunger":0,
            "min_grooming":0,
            "min_fun":0,
            "var_CHEAT":True
            },
        "icon":"cheat",
        "display_name": "Cheats",
        "label": ["cheats"]
        })


init:
    transform bottom_to_top:
        yalign 1.0
        linear 5.0 yalign 0.2

screen keynav():
    key "K_UP" action Call("konami", k = "up")
    key "K_DOWN" action Call("konami", k = "down")
    key "K_LEFT" action Call("konami", k = "left")
    key "K_RIGHT" action Call("konami", k = "right")
    key "K_b" action Call("konami", k = "b")
    key "K_a" action Call("konami", k = "a")

label konami(k):

    if len(KEYS) < len(CODE) and CODE[len(KEYS)] == k:
        $ KEYS.append(k)
    else:
        $ KEYS = []
    if KEYS == CODE:
        call successful_code from _call_successful_code
        $ KEYS = []
    return

label successful_code:
    if not CHEAT:
        $ CHEAT = True
    else:
        $ CHEAT = False
    return

label cheats:
    python:
        res = "Girls"
        while res in ["Girls","Attributes","Needs", "Money", "Date", "God mode", "Time"]:
            options = ["Girls","Attributes","Needs", "Money", "God mode", "Time"]
            if game.get_flag_value("dateinprogress"):
                options.append("Date")
            res = renpy.call_screen("select",options ,title = "Cheats")
            if res == "God mode":
                hunger_min = 8
                fun_min = 8
                grooming_min = 8
                energy_min = 8
            elif res == "Time":
                res = renpy.call_screen("select",["next hour","next day","next season"],title = "Time")
                if res == "next hour":
                    game.pass_time(1)
                elif res == "next day":
                    game.pass_time(24)
                else:
                    game.season += 1
                    if game.season > 3:
                        game.season = 0
            elif res == "Needs":
                res = "hunger"
                while res in ["hunger","grooming","fun","energy","all"]:
                    res = renpy.call_screen("select",["hunger","grooming","fun","energy","all"],title = "Needs")
                    if res in ["hunger","grooming","fun","energy"]:
                        
                        
                        hero[res] += getattr(store, res+"_max") - getattr(store, res) 
                    
                    
                    elif res == "all":
                        for n in ["hunger","grooming","fun","energy"]:
                            hero[n] += getattr(store, n+"_max") - getattr(store, n) 
                res = "Needs"
            elif res == "Attributes":
                res = "fitness"
                while res in ["fitness","charm","knowledge"]:
                    res = renpy.call_screen("select",["fitness","charm","knowledge"],title = "Attributes")
                    if res in ["fitness","charm","knowledge"]:
                        hero[res] += min(10,getattr(store, res+"_max") - getattr(store, res))
                res = "Attributes"
            elif res == "Money":
                hero.money += 1000
            elif res == "Date":
                game.set_flag("datescore", 100)
            elif res == "Skills":
                res = "martial_arts"
                skills = ["martial_arts", "golf", "cooking", "dance", "video_games", "guitar", "unlucky", "iron_stomach", "luck", "no_sleep", "hung"]
                for s in hero.skills:
                    if s in skills:
                        skills.remove(s)
                if skills:
                    res = skills[0]
                    while res in skills and skills:
                        res = renpy.call_screen("select",[s.capitalize().replace("_", " ") for s in skills],title = "Skills")
                        res = res.lower().replace(" ", "_")
                        if res in skills:
                            hero.skills.append(res)
                            skills.remove(res)
                            if skills:
                                res = skills[0]
                        else:
                            break
            elif res == "Girls":
                res = "sasha"
                while res in GIRLS:
                    res = renpy.call_screen("select",GIRLS.keys(),title = "Girls")
                    if res in GIRLS:
                        res2 = "sub"
                        while res2 in ["sub", "dom", "love", "lesbian", "location", "unpreg"]:
                            choices = ["sub", "dom", "love", "lesbian", "location"]
                            if GIRLS[res].get_flag_value("pregnant"):
                                choices.append("unpreg")
                            res2 = renpy.call_screen("select",choices,title = "Girl attributes")
                            if res2 == "sub":
                                GIRLS[res].sub += 5
                            elif res2 == "dom":
                                GIRLS[res].sub -= 5
                            elif res2 == "unpreg":
                                GIRLS[res].set_flag("pregnant",0)
                            elif res2 == "love":
                                GIRLS[res].love += getattr(store, res+"_love_max") - getattr(store, res+"_love")
                            elif res2 == "lesbian":
                                GIRLS[res].set_flag("lesbian",5,mod="+")
                            elif res2 == "location":
                                renpy.say("",GIRLS[res].id+" is at "+GIRLS[res].get_room().lower())
                        res = "sasha"
                res = "Girls"
    return

image smartphone = "ui/smartphone.png"
image bg blank = "bg/blank.webp"
image bg black = "bg/black.webp"
image bg splash = "bg/splash.webp"
image bg splash link = "bg/splash_link.webp"

label before_main_menu:
    play music "music/TRG_Banks/swanhead.mp3" loop
    return

label splashscreen:
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .25
            _preferences.volumes['sfx'] *= .5
    scene bg splash
    with fade
    $ renpy.pause(1)
    scene bg splash link
    with dissolve
    $ renpy.pause(1)
    scene bg black
    with fade
    return


label start:
    python:
        store.DONE = []
        store.DONE_HOUR = []
        store.DONE_WEEK = []
        store.DONE_MONTH = []
        store.DONE_DAY = []
        store.FLAGS = copy.deepcopy(FLAGS)
        store.HIDDEN = list(HIDDEN)
        game = Game()
        for g in GIRLS.values():
            exec(g.id+" = g")
        room = game.room
    python:
        for girl in GIRLS.values():
            girl.set_room()
        game.room = "livingroom"
    call intro from _call_intro

label main:
    call enter_room from _call_enter_room
    jump main


label after_load:
    python:
        for girl in GIRLS.values():
            girl.set_room()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
