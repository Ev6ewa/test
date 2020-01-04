layeredimage bg livingroom:
    if game.hour >= 20 or game.hour <= 5:
        "livingroom_night"
    else:
        "livingroom_day"

layeredimage bg house:
    attribute car:
        if_not "rain"
        if_any "car"
        "house_car"
    attribute rain:
        if_not "car"
        if_any "rain"
        "house_rain"

    if game.hour >= 20 or game.hour <= 5:
        if_not ["car","rain"]
        "house_night"
    else:
        if_not ["car","rain"]
        "house_day"

init -2 python:
    Room(**{
        "name":"livingroom",
        "exits": ["secondfloor","map","kitchen","pool", "bedroom1","bedroom2","bedroom3","bathroom", "bedroom4", "bedroom6"],
        "alternate_exits": ["secondfloor","map","kitchen","pool", "bedroom1"],
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "watch_tv_a",
        "fun": 1.5,
        "game_conditions": {"min_fun":0, "room":["livingroom"]},
        "girls_conditions": {"bree":{"not_activity":["tv"], "valid":True},"sasha":{"not_activity":["tv"], "valid":True}},
        "display_name": "Watch TV",
        "icon":"tv",
        "say": [
            "I watch a very strange show... An old man was traveling through time in a phone booth.",
            "I hate reality show, they show you how dumb people can be and they don't shoot them at the end.",
            "Again... A superhero movie, I don't know what's so good about men in tights.",
            "News are so depressing... Let's watch Planet Express, I love that show.",
            ]
        })

    Activity(**{
        "name": "watch_tv_b",
        "fun": 1.5,
        "game_conditions": {"min_fun":0, "room":["livingroom"]},
        "girls_conditions": {"bree":{"valid":False},"sasha":{"not_activity":["tv"], "valid":True}},
        "display_name": "Watch TV",
        "icon":"tv",
        "say": [
            "I watch a very strange show... An old man was traveling through time in a phone booth.",
            "I hate reality show, they show you how dumb people can be and they don't shoot them at the end.",
            "Again... A superhero movie, I don't know what's so good about men in tights.",
            "News are so depressing... Let's watch Planet Express, I love that show.",
            ]
        })

    Activity(**{
        "name": "watch_tv_c",
        "fun": 1.5,
        "game_conditions": {"min_fun":0, "room":["livingroom"]},
        "girls_conditions": {"bree":{"not_activity":["tv"], "valid":True},"sasha":{"valid":False}},
        "display_name": "Watch TV",
        "icon":"tv",
        "say": [
            "I watch a very strange show... An old man was traveling through time in a phone booth.",
            "I hate reality show, they show you how dumb people can be and they don't shoot them at the end.",
            "Again... A superhero movie, I don't know what's so good about men in tights.",
            "News are so depressing... Let's watch Planet Express, I love that show.",
            ]
        })

    Activity(**{
        "name": "watch_tv_d",
        "fun": 1.5,
        "game_conditions": {"min_fun":0, "room":["livingroom"]},
        "girls_conditions": {"bree":{"valid":False},"sasha":{"valid":False}},
        "display_name": "Watch TV",
        "icon":"tv",
        "say": [
            "I watch a very strange show... An old man was traveling through time in a phone booth.",
            "I hate reality show, they show you how dumb people can be and they don't shoot them at the end.",
            "Again... A superhero movie, I don't know what's so good about men in tights.",
            "News are so depressing... Let's watch Planet Express, I love that show.",
            ]
        })

    Activity(**{
        "name": "play_videogames",
        "fun": 3,
        "game_conditions": {"min_fun":0, "room":["livingroom"], "not_valid":"play_videogames_with_bree"},
        "girls_conditions": {"bree":{"not_activity":["tv"]},"sasha":{"not_activity":["tv"]}},
        "display_name": "Play videogames",
        "label": ["play_videogames"],
        "icon":"videogame",
        "required_item": "zbox 360"
        })


    Activity(**{
        "name": "play_videogames_with_bree",
        "fun": 3,
        "game_conditions": {"min_fun":0, "room":["livingroom"]},
        "girls_conditions": {"bree":{"present":True,"valid":True,},"sasha":{"not_activity":["tv"]}},
        "display_name": "Play videogames with bree",
        "label": ["play_videogames_with_bree"],
        "icon":"videogame",
        "required_item": "zbox 360"
        })

    Activity(**{
        "name": "watch_tv_with_everyone",
        "fun": 3,
        "duration": 2,
        "icon":"tv",
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":0, "room":["livingroom"], "flag_female":0},
        "girls_conditions": {"bree":{"activity":["tv"],"present":True, "valid":True},"sasha":{"activity":["tv"],"present":True, "valid":True}},
        "display_name": "Watch TV with everyone",
        "label": ["watch_tv_with_everyone"]
        })


    Activity(**{
        "name": "watch_tv_with_everyone_mike",
        "fun": 3,
        "duration": 2,
        "icon":"tv",
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":0, "room":["livingroom"], "flag_female":1},
        "girls_conditions": {"mike":{"activity":["tv"],"present":True},"sasha":{"activity":["tv"],"present":True}},
        "display_name": "Watch TV with everyone",
        "label": ["watch_tv_with_everyone_mike"]
        })

    Activity(**{
        "name": "clean_the_livingroom",
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2, "room":["livingroom"],"flagmax_chores":99},
        "display_name": "Vacuum",
        "icon":"vacuum",
        "label": ["clean_the_livingroom"],
        "once_week": True
        })

    Event(**{
        "name": "sasha_livingroom_bree",
        "fun": 3,
        "duration": 2,
        "girls_conditions": {"sasha":{"present":True},"bree":{"present":True}, "flag_female":0},
        "game_conditions": {"room":["livingroom"],"chances":5},
        "label": ["sasha_livingroom_bree"],
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"wish_had_console",
        "label": ["wish_had_console"],
        "game_conditions": {"room":["livingroom"],"chances":5},
        "duration": 0,
        "do_once": True,
        "quit": False
        })

    Event(**{
        "name":"polygamy_news_1",
        "label": ["polygamy_news"],
        "game_conditions": {"room":["livingroom"], "activity":"watch_tv", "flagmin_bandharem":1, "hours":(20,21), "flag_polygamy":0},
        "duration": 1,
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name":"polygamy_news_2",
        "label": ["polygamy_news"],
        "game_conditions": {"room":["livingroom"], "activity":"watch_tv", "flagmin_homeharem":1, "hours":(20,21), "flag_polygamy":0},
        "duration": 1,
        "do_once": True,
        "quit": True
        })

    Activity(**{
        "name": "masturbate",
        "fun": 1,
        "duration":0,
        "max_girls":0,
        "label":["masturbate"],
        "icon":"masturbate",
        "game_conditions": {
            "room":["livingroom"],
            "min_energy":0,
            "min_hunger":0,
            "min_grooming":0,
            "max_fun":3,
            "flag_female":0
            },
        "display_name": "Masturbate",
        "once_day": True
        })

    Activity(**{
        "name": "masturbate",
        "fun": 1,
        "duration":0,
        "max_girls":0,
        "label":["livingroom_masturbate_bree"],
        "icon":"masturbate",
        "game_conditions": {
            "room":["livingroom"],
            "min_energy":0,
            "min_hunger":0,
            "min_grooming":0,
            "max_fun":3,
            "flag_female":1,
            "flagmax_morality": -25
            },
        "display_name": "Masturbate",
        "once_day": True
        })

label livingroom_masturbate_bree:
    "I decide to have a little fun by myself"
    "Mmmmmh, that feels good."
    if game.get_flag_value("morality") >= -49:
        $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
        $ game.set_flag("morality",1,mod="-")
    return

label masturbate:
    show couch fun masturbate
    "I decide to have a little fun by myself"
    show couch fun masturbate cumshot
    "Mmmmmh, that feels good."
    return

label wish_had_console:
    "I should buy myself a gaming system, watching TV is boring."
    return

label play_videogames:
    "I play some video games"
    $ game.set_flag("videogames_skill",1,"permanent","+")
    return


label play_videogames_with_bree:
    show bree console 3
    "I play some video games with Bree"
    $ game.set_flag("videogames_skill",1,"permanent","+")
    $ bree.love += 1
    if "video_games" in hero.skills:
        show bree console 1
        $ bree.sub += 1
        "And I win!"
    else:
        show bree console 2
        $ bree.sub -= 1
        "And I lose..."
    return

label clean_the_livingroom:
    python:
        game.set_flag("chores",25,"week","+")
        if game.get_flag_value("chores") > 100:
            bree.love += 1
            sasha.love += 1
    return

label sasha_livingroom_bree:
    $ result = randint(1,2)
    if result == 1:
        show sasha at left
        show bree at right
        "Sasha and Bree are arguing about some stuff."
        python:
            response = renpy.display_menu([("Take Bree's side",1),("Take Sasha's side",2),("Stay neutral",3)])
            if response == 1:
                bree.love += 2
                sasha.love -= 1
            elif response == 2:
                sasha.love += 2
                bree.love -= 1
            elif response == 3:
                bree.love += 1
                sasha.love += 1
        "After my intervention they stop arguing."
    elif result == 2:
        "Sasha and Bree are chatting on the couch."
        "I join them for a while."
        $ bree.love += 1
        $ sasha.love += 1

    return

label polygamy_news:
    $ game.set_flag("polygamy",True)
    "I have that really bad habit of getting home from work on an evening and just collapsing on the sofa with the TV blaring out at me."
    "At one time I might actually have sat down with it in my mind to watch something specific, but these days it's more like sensory white noise."
    "Often I won't even so much as know what I'm watching, unless something truly noteworthy catches my attention or someone else walks in and yells at me."
    "Tonight it was a case of the former, rather than the latter."
    "And in some ways I was rather glad that I was the only person in the room when I realised what was being said."
    "As distracted as I am when slumped in front of the TV there are certain terms and phrases that seem to always break through the haze and register with me."
    "Almost like Pavlov ringing the bell for his trained dogs, I'll immediately sit up and begin to pay attention."
    "In this case, the word just so happens to be 'polygamy'."
    "I look up, instantly intrigued, and see that I'm actually watching the news."
    "Grabbing the remote, I rewind by about thirty seconds to catch the start of the current story."
    man_say "...saw the second reading of the controversial 'Marriage and Social Institution Reform Bill' before the lower house."
    man_say "Dubbed the 'Bigamy Bill' by its critics on account of its most far-reaching effects, the bill was expected to be thrown out finally in today's session."
    "Oh yeah - the bill going through parliament that had a clause about polygamy buried in there somewhere."
    "I'd read a little about it online, and it was supposedly all about equalising the rights of marriage and civil partnerships for everyone, no matter what their professed orientation."
    "The bit about polygamy was probably the least important aspect of it all."
    "But the constantly outraged conservative right were too afraid of being labelled anti-LGBTQ+ bigots to go after the main portions of the bill."
    "So they'd seized upon the polygamy part as a kind of backdoor to oppose it, nicknaming it the 'Bigamy Bill' as a result."
    man_say "But in a shock move, it received the backing of the formerly abstaining members to narrowly pass into law."
    man_say "It's opponents have sited this move as proof of a wider conspiracy to undermine..."
    "The anchor went on with her dissection of the matter, but I had already stopped listening some time beforehand."
    "It was actually happening, and soon the law would change to allow anyone that wanted to marry more than one person at a time."
    "I guess someone else might have been mulling over the wider social implications of this change in the law."
    "But what instantly sprang into my mind, was the fact that if polygamy was normalised, then relationships between more than two individuals would be as well."
    "It might only be the more open-minded of girls that would begin to come round to the idea at first."
    "But surely it would mean that, were someone to raise the possibility with two or more members of the opposite sex, they wouldn't automatically earn themselves a slap across the face?"
    return

label watch_tv_with_everyone:
    $ sasha.set_flag("daily_interact", 1, 1, "+")
    $ bree.set_flag("daily_interact", 1, 1, "+")
    show bree at left
    show sasha at right
    hero.say "Let's watch a movie together."
    $ choices = ["Action movie","Cartoon","SciFi movie","Fashion show", "Discovery channel", "Romantic comedy", "Porn", "Horror movie", "News", "Reality show", "Music channel"]
    python:
        for i in range(1,4):
            choices.remove(randchoice(choices))
        result = renpy.call_screen("select",choices)
    if game.hour > 20:
        hide sasha
        hide bree
        show tv bree sasha
    if result == "Action movie":
        $ renpy.say("", randchoice(["We watch an action movie.","We watch a movie with "+randchoice(["Schwarzenegger","Stallone","Statham"])+".","We watch a "+randchoice(["Die Hard","Rambo","Dirty Harry","James Bond"])+" sequel."]))
        $ sasha.love -= 1
    elif result == "Cartoon":
        "We watch a funny cartoon."
        "Sasha looks a completly bored but Bree seems to enjoy herself."
        $ sasha.love -= 1
        $ bree.love += 2
    elif result == "SciFi movie":
        "We watch a scifi movie."
        "Bree and Sasha seems to enjoy themselves."
        $ sasha.love += 1
        $ bree.love += 3
    elif result == "News":
        "We watch the news."
    elif result == "Reality show":
        $ a = randchoice(["dead", "bimbo", "nazi","smart","real","fake","gay","stupid","angry","cute","white","black","racist","socialist","poor","rich","ugly","sexy","fat","mean","nice","old","young","virgin"])
        $ b = randchoice(["housewives","cops","millionaires","geeks","sluts","nuns","cats","dogs","grannys","middle aged men","asians","government officials","strippers","doctors","truck drivers"])
        $ c = randchoice(["the world","venezuela","paris","mars","the sewers","new-york","france","spain","seattle","los angeles","my basement","texas","mexico","brazil", "space"])
        $ d = randchoice(["of","against","meet","discover","lost in"])
        $ t = (a+" "+b+" "+d+" "+c).title()
        "We watch [t]."
        $ bree.love -= 1
    elif result == "Music channel":
        "We watch a concert."
        "Bree and Sasha seems to enjoy themselves."
        $ sasha.love += 3
    elif result == "Fashion show":
        "We watch a fashion show."
        "Bree looks completly bored but Sasha seems mesmerized."
        $ bree.love -= 1
        $ sasha.love += 1
    elif result == "Discovery channel":
        "We watch a discovery channel."
        "Bree seems to enjoy herself but Sasha looks bored."
        $ bree.love += 1
        $ sasha.love += 1
    elif result == "Romantic comedy":
        "We watch a romantic comedy."
        "Bree seems to enjoy herself very much, but not Sasha."
        $ bree.love += 1
    elif result == "Horror movie":
        "We watch a horror movie."
        "Bree seems to be more scared than enjoyed, but Sasha is beaming."
        $ sasha.love += 2
        $ bree.love -= 1
    elif result == "Porn":
        if hero.charm >= 100 - min([bree.love(),sasha.love()]):
            "We watch some porn together."
            menu:
                "SM porn":
                    $ bree.sub += 1
                    $ sasha.sub += 1
                    $ bree.set_flag("porn")
                "Femdom porn":
                    $ bree.sub -= 1
                    $ sasha.sub -= 1
                    $ bree.set_flag("porn")
                "Gonzo porn":
                    $ bree.love += 1
                    $ sasha.love += 1
                "Lesbian porn":
                    $ bree.love += 1
                    $ sasha.love += 1
                    $ NOTIFICATIONS.append(["Sasha {image=ui/icon_les_vsmall.png}+5",2])
                    $ sasha.set_flag("lesbian",1,mod="+")
                    $ NOTIFICATIONS.append(["Bree {image=ui/icon_les_vsmall.png}+5",2])
                    $ bree.set_flag("lesbian",1,mod="+")
            if bree.love >= 150 and sasha.love >= 150 and game.get_flag_value("homeharem"):
                hide tv
                call bj3_porn from _call_bj3_porn
            else:
                "The girls seems to be quite excited by the sight."
            $ bree.love += 1
            $ sasha.love += 1
        else:
            "They refuse to watch that."
            $ bree.love -= 1
            $ sasha.love -= 1
            return
    $ hero.fun+= 1.5
    if game.hour > 20:
        hide tv

    return


label watch_tv_with_everyone_mike:
    $ sasha.set_flag("daily_interact", 1, 1, "+")
    $ mike.set_flag("daily_interact", 1, 1, "+")
    show mike at left
    show sasha at right
    hero.say "Let's watch a movie together."
    $ choices = ["Action movie","Cartoon","SciFi movie","Fashion show", "Discovery channel", "Romantic comedy", "Porn", "Horror movie", "News", "Reality show", "Music channel"]
    python:
        for i in range(1,4):
            choices.remove(randchoice(choices))
        result = renpy.call_screen("select",choices)
    if game.hour > 20:
        hide sasha
        hide mike
        show tv sasha bree
    if result == "Action movie":
        $ renpy.say("", randchoice(["We watch an action movie.","We watch a movie with "+randchoice(["Schwarzenegger","Stallone","Statham"])+".","We watch a "+randchoice(["Die Hard","Rambo","Dirty Harry","James Bond"])+" sequel."]))
        $ sasha.love -= 1
    elif result == "Cartoon":
        "We watch a funny cartoon."
        "Sasha looks a completly bored but Mike seems to enjoy himself."
        $ sasha.love -= 1
        $ mike.love += 2
    elif result == "SciFi movie":
        "We watch a scifi movie."
        "Mike and Sasha seems to enjoy themselves."
        $ sasha.love += 1
        $ mike.love += 3
    elif result == "News":
        "We watch the news."
    elif result == "Reality show":
        $ a = randchoice(["dead", "bimbo", "nazi","smart","real","fake","gay","stupid","angry","cute","white","black","racist","socialist","poor","rich","ugly","sexy","fat","mean","nice","old","young","virgin"])
        $ b = randchoice(["housewives","cops","millionaires","geeks","sluts","nuns","cats","dogs","grannys","middle aged men","asians","government officials","strippers","doctors","truck drivers"])
        $ c = randchoice(["the world","venezuela","paris","mars","the sewers","new-york","france","spain","seattle","los angeles","my basement","texas","mexico","brazil", "space"])
        $ d = randchoice(["of","against","meet","discover","lost in"])
        $ t = (a+" "+b+" "+d+" "+c).title()
        "We watch [t]."
        $ mike.love -= 1
    elif result == "Music channel":
        "We watch a concert."
        "Mike and Sasha seems to enjoy themselves."
        $ sasha.love += 3
    elif result == "Fashion show":
        "We watch a fashion show."
        "Mike looks completly bored but Sasha seems mesmerized."
        $ mike.love -= 1
        $ sasha.love += 1
    elif result == "Discovery channel":
        "We watch a discovery channel."
        "Mike seems to enjoy himself but Sasha looks bored."
        $ mike.love += 1
        $ sasha.love += 1
    elif result == "Romantic comedy":
        "We watch a romantic comedy."
        "Mike seems to enjoy himself very much, but not Sasha."
        $ mike.love += 1
    elif result == "Horror movie":
        "We watch a horror movie."
        "Mike seems to be more scared than enjoyed, but Sasha is beaming."
        $ sasha.love += 2
        $ mike.love -= 1
    elif result == "Porn":
        if hero.charm >= 100 - min([mike.love(),sasha.love()]):
            "We watch some porn together."
            menu:
                "SM porn":
                    $ mike.sub -= 1
                    $ sasha.sub += 1
                    $ mike.set_flag("porn")
                "Femdom porn":
                    $ mike.sub += 1
                    $ mike.set_flag("porn")
                "Gonzo porn":
                    $ mike.love += 1
                    $ sasha.love += 1
                "Lesbian porn":
                    $ mike.love += 1
                    $ sasha.love += 1
                    $ NOTIFICATIONS.append(["Sasha {image=ui/icon_les_vsmall.png}+5",2])
                    $ sasha.set_flag("lesbian",1,mod="+")
            "They seems to be quite excited by the sight."
            $ mike.love += 1
            $ sasha.love += 1
        else:
            "They refuse to watch that."
            $ mike.love -= 1
            $ sasha.love -= 1
            return
    $ hero.fun+= 1.5
    if game.hour > 20:
        hide mike sasha tv

    return



label bj3_porn:
    "We watch porn..."
    "The excitation could be felt by anyone..."
    bree_sasha "Hey, [hero.name]"
    sasha.say "It's boring to just watch"
    bree.say "Soooo true."
    hero.say "And?"
    "I think about it a moment."
    sasha.say "Let's have some fun..."
    "Sasha's fingers hooks over the straps of her bra then she slides the straps over her shoulders."
    bree.say "Relax, but not too much!"
    "Bree speaks while, shimmying out of her panties."
    "She playfully tosses them off with her foot."
    scene bg livingroom
    show bree naked at left
    show sasha naked at right
    "When I glance at them again, Bree and Sasha stand on either side of the couch."
    "Both of my roomates have removed their clothes and smile down at me with their lust and intent."
    sasha.say "Hope you enjoy the sight,"
    bree.say "Now then!"
    bree.say "Let’s get down to business shall we?"
    "The two nod at each other."
    "The two of them lean in over the couch, each of them giving me their fluttering bedroom eyes."
    "As they climb up onto the couch, Sasha on my left and Bree on my right, the soft words whisper gently to my ears."
    "Soon, the two lay their, their warm bodies up agianst my own, pressed against my spread legs."
    "I reach up and hold onto both of them, sliding my own fingers over their smooth skin."
    hide bree
    hide sasha
    show couch fun bree sasha
    "Together, they wrap their fingers around my shaft, and also together, they roll their tongues out, licking up along my length."
    hero.say "O... oh wow..."
    "Again, they lick up my shaft, up over the glans and over the tip."
    "Their tongues touch, and they both stare up at me, a chuckled shared between the two of them before they wrap their lips around the head."
    "The two best roomates in the world make out with my cock in the middle of it all, their tongues dancing over my skin as their hands move in sync to jerk me off."
    "What did I do to deserve the greatest roomates in the world?"
    "I wonder this as the excitement of their actions tingles up through my body."
    show couch fun bree sasha cumshot
    "I can’t hold back and, with a groan, I release, shooting up onto them."
    "Cum sprays up onto their faces, getting them nice and covered by my jizz."
    hide couch
    show couch fun bree sasha facial
    "The girls smile up at me, batting their half-lidded eyes up in my direction."
    sasha.say "Enjoy this view...,"
    "Sasha takes a finger and slips a drop of my cum off of her face."
    "She hands it to Bree, who wraps her lips around my cock, moaning in delight at the taste."
    hide couch
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
