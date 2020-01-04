init -1 python:
    Event(**{
        "name":"mike_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "mike",
        "girls_conditions": {"mike":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"mike_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "mike",
        "girls_conditions": {"mike":{"contact":"mike","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(11,12),"flag_dateinprogress":0,"chances":10},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"mike_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "mike",
        "priority":100,
        "girls_conditions": {"mike":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"mike_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "mike",
        "priority":100,
        "girls_conditions": {"mike":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"mike_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "mike",
        "priority":100,
        "girls_conditions": {"mike":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_mike_2"},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"mike_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "mike",
        "priority":100,
        "girls_conditions": {"mike":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"mike_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "mike",
        "girls_conditions": {"mike":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50},
        "do_once": False,
        "once_day": True
        })

    Activity(**{
        "name": "have_a_meal_with_mike",
        "hunger": 10,
        "fun": 1,
        "game_conditions": {
            "max_hunger":9,
            "min_hunger":0,
            "min_grooming":0,
            "min_fun":0,
            "min_energy":0, 
            "room":["kitchen"], 
            "flag_female":1
            },
        "icon":"eat",
        "max_girls": 1,
        "girls_conditions": {
            "mike":{
                "present":True,
                "activity":"meal"
                }
            },
        "display_name": "Eat with Mike",
        "label": ["mike_meal"]
        })

    Activity(**{
        "name": "watch_tv_with_mike",
        "duration": 2,
        "fun": 3,
        "icon":"tv",
        "display_name": "Watch TV with Mike",
        "girls_conditions": {
            "mike":{
                "present":True,
                "activity":["tv"]
                },
            "sasha":{
                "not_activity":["tv"]
                }
            },
        "game_conditions": {
            "room":["livingroom"],
            "min_fun":0, 
            "flag_female":1
            },
        "label": ["mike_tv"]
        })

    Event(**{
        "name":"mike_init_re",
        "label": ["mike_init"],
        "girls_conditions": {"mike":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

label mike_init:
    python:
        if not "mike" in HIDDEN and not game.get_flag_value("female"):
            HIDDEN.append("mike")
        mike_love_max = 200
    return

label mike_tv:
    call mike_greet from _call_mike_greet
    show mike
    if hero.charm >= 40 - mike.love() or mike.get_activity()[1]["activity"] == "tv":
        $ mike.set_flag("daily_interact", 1, 1, "+")
        mike.say "Why not."
        $ choices = ["Action movie","Cartoon","SciFi movie","Fashion show", "Discovery channel", "Romantic comedy", "Porn", "Horror movie", "News", "Reality show", "Music channel"]
        python:
            for i in range(1,4):
                choices.remove(randchoice(choices))
            result = renpy.call_screen("select",choices)
        if game.hour > 20:
            show tv bree
        if result == "Action movie":
            "We watch an action movie."
            "Mike looks a little bored."
        elif result == "Cartoon":
            "We watch a funny cartoon."
            "Mike seems to enjoy himself."
            $ mike.love += 2
        elif result == "SciFi movie":
            "We watch a scifi movie."
            "Mike seems to enjoy himself a lot."
            $ mike.love += 3
        elif result == "Fashion show":
            "We watch a fashion show."
            "Mike looks completly bored."
            $ mike.love -= 1
        elif result == "News":
            "We watch the news."
        elif result == "Reality show":
            $ a = randchoice(["dead", "bimbo", "nazi","smart","real","fake","gay","stupid","angry","cute","white","black","racist","socialist","poor","rich","ugly","sexy","fat","mean","nice","old","young","virgin"])
            $ b = randchoice(["housewives","cops","millionaires","geeks","sluts","nuns","cats","dogs","grannys","middle aged men","asians","government officials","strippers","doctors","truck drivers"])
            $ c = randchoice(["the world","venezuela","paris","mars","the sewers","new-york","france","spain","seattle","los angeles","my basement","texas","mexico","brazil", "space"])
            $ d = randchoice(["of","against","meet","discover","lost in"])
            $ t = (a+" "+b+" "+d+" "+c).title()
            "We watch [t]."
            "Mike looks completly bored."
            $ mike.love -= 1
        elif result == "Music channel":
            "We watch concert."
            "Mike looks bored."
        elif result == "Discovery channel":
            "We watch discovery channel."
            "Mike seems to enjoy himself."
            $ mike.love += 1
        elif result == "Romantic comedy":
            "We watch a romantic comedy."
            "Mike seems to enjoy himself a little."
            $ mike.love += 1
        elif result == "Horror movie":
            "We watch a horror movie."
            "Mike seems to be more scared than enjoyed."
            $ mike.love -= 1
        elif result == "Porn":
            if hero.charm >= 100 - mike.love():
                "We watch some porn together."
                menu:
                    "SM porn":
                        $ mike.sub -= 1
                        $ mike.set_flag("porn")
                    "Femdom porn":
                        $ mike.sub += 1
                        $ mike.set_flag("porn")
                    "Gonzo porn":
                        $ mike.love += 1
                    "Lesbian porn":
                        $ mike.love += 1
                "Mike seems to be quite excited by the sight."
                $ mike.love += 1
            else:
                mike.say "Sorry, I don't want to watch this sort of things."
                $ mike.love -= 1
                hide mike
                return
        $ hero.fun+= 1.5
        if game.hour > 20:
            hide bree
    else:
        mike.say "Sorry, I don't have time right now."
        $ hero.activity.set_flag("canceled",True)
        hide mike
    hide tv
    return

label mike_meal:
    call mike_greet from _call_mike_greet_1
    if hero.check_skill("cooking"):
        $ mike.love += 1
    if game.hour < 12:
        show mike
        mike.say "It's nice having breakfast together."
        $ mike.love += 1
    else:
        show mike
        call expression mike.get_chat() from _call_expression_111
    hide mike
    return


label smartphone_mike_hint:
    $ story = mike.get_flag_value("story")
    if not mike_love == mike_love_max:
        "I should get to know Mike better."
    else:
        "I reached the end of Mike's story for now."
    return

label mike_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = mike.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = mike.get_activity(bye_hour)
    if not activity == mike.activity:
        if day != game.week_day:
            $ mike.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ mike.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "mike "+bye_outfit
        if activity["activity"] == "sleep":
            mike.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            mike.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            mike.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            mike.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            mike.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            mike.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            mike.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            mike.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            mike.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            mike.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            mike.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            mike.say "I ll go get dressed."
        hide expression "mike "+bye_outfit
    return

label mike_cheated:
    show mike
    if (game.get_flag_value("bandharem") == 1 and game.active_girl.id in ["kleio"]) or (game.get_flag_value("bandharem") == 2 and game.active_girl.id in ["kleio", "sasha"]):
        mike.say "Hey, That's unfair!"
        mike.say "I like have some fun too!"
        show mike kiss
        "And without warning Mike kisses me."
        $ mike.love += 1
    else:
        "I see Mike looking at me kissing someone else sadly, tears welling up in his eyes..."
        $ mike.love -= 5
    hide mike
    return

label mike_greet:
    if not mike.get_flag_value("greeted"):
        $ mike.set_flag("greeted",True,1)
        show mike
        $ result = randint (1,3)
        if result == 1:
            mike.say "Hello, [hero.name]."
        elif result == 2:
            mike.say "Hi, [hero.name]."
        elif result == 3:
            mike.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                mike.say "Good morning [hero.name]."
            elif game.hour < 19:
                mike.say "Good afternoon [hero.name]."
            else:
                mike.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Mike."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                mike.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Mike."
            elif game.hour < 19:
                hero.say "Good afternoon Mike."
            else:
                hero.say "Good evening Mike."
    return

label mike_kiss:
    scene expression "bg "+game.room
    if mike.love() + hero.charm() < 80 and not mike.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show mike
        "Mike quickly takes a step back, and turns away."
        if mike.love < 40:
            $ mike.sub -= 1
        else:
            $ result = randint(1,2)
            if result == 1:
                $ mike.love -= 1
        hide mike
    elif mike.love() + hero.charm() < 60 or (game.get_flag_value("datescore") >= 75 and not mike.love() + hero.charm() < 60):
        hide mike
        show expression "mike kiss "+mike.get_clothes()
        if not mike.get_flag_value("kiss"):
            "I watch Mike's eyes open wide in surprise, and for a moment I think he might back away."
            "Then our lips touches, for the longest time."
            hide expression "mike kiss "+mike.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != mike and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_107
            $ mike.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Mike, and rest my hands lightly on his shoulder."
            "For a brief moment he looks curious, but I catch sight of a moment of recognition in his eyes before my own drift shut."
            "After the kiss, I catch a glimpse of a small smile playing on his lips before he tries to hide it."
            hide expression "mike kiss "+mike.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != mike and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_108
        $ mike.love += 1
    else:
        hide mike
        show expression "mike kiss "+mike.get_clothes()
        if not mike.get_flag_value("kiss"):
            "I feel my lips passing over Mike's as we embrace, my hands resting comfortably on his shoulders while his own had ventured to my hips."
            "He pushes into my embrace more than he has in the past, but also begin lightly tickling me with his tongue."
            "For a moment, I'm not sure if I'll reciprocate, but I part my lips and allow him access."
            "He let himself inside me, exploring every crevice of my mouth in earnest."
            "I feel rather tense at first, but let out a soft whimper of pleasure."
            hide expression "mike kiss "+mike.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != mike and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_109
        else:
            "Once again Mike steps in closer to me, close enough that our bodies are very nearly touching."
            "He brings one hand to my chin, tilting me up to face him as he leans down to let our lips meet."
            "His tongue yet again pushes through the barrier that my lips form to begin exploring my mouth."
            "Before long, we pulled away from one another, breathless."
            hide expression "mike kiss "+mike.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != mike and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_110
        hide mike
        $ mike.love += 2
    return

label mike_fuck_date_female:
    $ mike.set_flag("sex",1,"permanent","+")
    scene bg bedroom1
    show mike
    "The two of us find ourselves in Mike's room, laughing and joking about something or another, before an awkward silence begins to fill the air."
    "I've had a fun time, but the night isn't over yet, and thanks to where we're both stood it's pretty clear what's about to come next."
    "The two of us give each other sheepish looks as Mike builds up the courage to act, standing for just a little too long for comfort before stepping forwards and pressing his lips against mine."
    "I'm took slightly off guard, his movements having been swift and sudden, but I quickly begin melting into the embrace, wrapping my fingers around his in return as he presses his body against mine more and more."
    "My eyes flutter closed to focus ever more on his lips against mine, on the way that he gently sucks my lip, his teeth brushing lightly against me, his saliva swapping with mine and taste filling my mouth."
    "His movements, while filled with intent, are a touch clumsy, yet his sheer earnestness more than makes up for it."
    "I lose myself as his hand snakes around my waist, pulling me closer still until I can feel his bulge pressing against me through our clothing."
    "It feels like it's only been moments before he pulls away but logic tells me it's been minutes, stood there in silence and simply enjoying one another."
    "I let out a quiet little whine, feeling my need bubbling up from within, desperate to lean forwards and reignite what we just had, but I hold myself back."
    "Our eyes meet and we smile, pausing for a moment to collectively catch our breath before Mike spins around and playfully pushes me down."
    "I let out a quiet yelp as I hit the bed with a soft pomf, my eyes quickly finding Mike's again as I slowly crawl backwards, getting comfortable."
    show mike underwear blush
    "He begins pulling his shirt over his head, his bare chest quickly distracting me from following his lead."
    "His shirt has barely hit the floor as he begins crawling onto the bed after me, ever so slowly clambering over my body as his hand fumbles with his pants."
    "Not wanting to be left behind, I quickly begin tearing my own clothes away, quickly reducing myself to naught but my underwear."
    "A cold breeze washes over my near naked form but I'm quickly warmed again as Mike descends on me, his lips meeting mine yet again as his body presses against mine."
    "His hands trace my thighs, gently dancing across my skin, teasing me needlessly as his tongue invades me, passionately dancing with my own."
    "Once again my eyes close, my mind drifting to the large tent his own underwear proudly showcased, the size both intimidating and intriguing."
    "With my sight cut off, the way his fingers gently explore my flesh is more effective than ever, especially when I feel them slipping behind my back, my bra soon being torn away."
    "My erect nipples brush freely against Mike's chest as we kiss now, one of my arms slung around his neck while the other begins attempting to mimic the man."
    "I trail it down his chest, slowly, stopping at his midrift for a moment, before going further, and further, until my palm made contact with his rod."
    "The thin fabric of his boxers still separate us, but from the way he gasps within our embrace as I gently begin tracing his length I can tell he still feels well enough."
    "Not one to be outdone, or his patience simply beginning to wear thin, I feel the same hand that removed my bra grasp the rim of my panties, tearing them away and leaving me entirely open."
    show mike naked blush
    "A string of saliva still joins us as Mike pulls back, taking his own underwear off too before I could attempt to do it for him, tossing it carelessly across the room as his cock springs into the open."
    "I'm mesmerised by it for a brief moment, watching it twitch in the open air, stand to attention, almost flattered at how quickly Mike got quite this pent up."
    "I subtly spread my legs, feeling the moisture between them practically drip onto the bedsheets, and realise that the feeling is mutual."
    "My arousal is almost painful but I almost suspect Mike's actually is, the two of us staying like that for a few moments as he hastily puts on a condom."
    "Then, with any necessary prep work out of the way, he leans over me once more, our naked bodies pressing together again as I feel his tip begin to trace my entrance."
    show bree miss
    "It rubs my sensitive slit up, then down, doing so several times apparently just to tease me before shifting himself to rub his entire length at once, coating it in my juices."
    "I whimper as he does this again, and again, bucking my hips into him in a desperate desire to feel him inside me already."
    "Fortunately, it doesn't take long before he happily obliges, pulling back one final time, positioning his cock with his hand, then slowly coming forwards once more."
    hide mike
    show bree miss fuck
    "All is silent except the squelch of his cock steadily forcing it's way into my tight passage, my whimpers eventually filling the air to join it."
    "He's large, larger than I'm used to, and my body wraps itself around him tightly enough that he has to put his weight behind his thrust."
    "It hurts, but I bare it, something made ever easier by the unbelievable sensations that come hand in hand with the pain."
    "The deeper he gets the better it feels, his cock exploring and poking my deepest reaches and going further still."
    "My worries that I won't be able to accommodate all of him are quickly relieved when his waist slaps against mine, his cock fully buried within me."
    mike.say "Are. Are you alright?"
    "The first words he's spoken since we arrived ring out in the room, forcing me to open my eyes, meeting his concerned gaze."
    "His arms are trembling, and a bead of sweat is already forming on his brow, threatening to roll down his face at even the slightest movement."
    "Despite having only just broken our kiss his lips look dry, parched, and although there's overwhelming arousal in his gaze, there's equal parts worry and restraint."
    hero.say "I think so."
    "My voice comes out weak, quiet, barely a squeak in fact, but it's hard to sound convincing with a cock buried deep within you."
    "I can feel how shaky my breath seems to be, and can only imagine what I look like to prompt Mike pausing."
    show bree miss fuck cum
    hero.say "Don't stop."
    "I purposefully whisper that part, attempting to entice him back into action, insisting he shouldn't have stopped in the first place, and thankfully, he responds with a simple nod, pausing for a moment before beginning to move once more."
    "He pulls out slowly, but not as slowly as he entered, and he pushes back inside a touch faster still."
    "Despite his size I'm positive that my own arousal is enough for easy entrance. He's trying to be considerate of me."
    "I let out a low moan as he begins moving faster still, steadily building up to a rhythm, our hips slapping together over and over as he pumps in and out."
    mike.say "Oh shit. You're so tight."
    "His voice sounds strained, shaky, even those few words difficult to spit out, and yet they send shivers down my spine."
    mike.say "You're wrapping around me so much."
    "He continues, leaning forwards so his softer inflection can be heard over my own steadily increasing moans."
    mike.say "The way you're clamping down. You want it, don't you?"
    "I wasn't expecting such a direct question, and at first I don't answer him, too absorbed in the way his hand has just grasped my breast, massaging it as he claims me."
    "Thankfully, he's patient, deciding to gently nibble on my ear as he waits for me to be more vocal outside of the formless cries I've been giving him in earnest."
    hero.say "Yes, I want it, Mike."
    "I myself am surprised at how sultry I sound, but have little time to dwell on the matter as a particularly strong sudden thrust forces a gasp out of me."
    mike.say "You're so sexy, [hero.name]."
    mike.say "I'm so lucky."
    "His voice so close to my ear, all he has to do is whisper to near debilitate me, his soft spoken tone contrasting the way his hips begin to grow ever more violent and frantic."
    "His cock, while large, fits me perfectly, rubbing against every little bump and nook in my wet, sopping cunt, each subtle movement of his hips sending waves crashing over me."
    "Not that his movements are even close to being subtle."
    "I can barely form his name thanks to the way that my body seems to have started to disobey me, moving on it's own to begin bucking my hips forwards into Mike's thrusts."
    "My arms reaching up to wrap around his chest and hold him close as his breath washes across my neck, his lips playfully planting kiss after kiss on my bare skin as he fucks me silly."
    show bree miss fuck ahegao
    hero.say "Mike. Ah! Mike! It feels so good~!"
    "I manage to take back control, moaning Mike's name rather than just empty cries, something that the man noticeably seems to enjoy, finding newfound strength to put behind every pump of his hips."
    "I find the wind quickly knocked out of me as he begins caring less and less for my comfort, his arousal taking over and beginning to control his actions."
    mike.say "You sound so sexy when you're screaming my name."
    "His voice in my ear alone makes me throw my head back, clutching desperately for something to hold but finding naught but air, and Mike's back that is, my fingernails digging a little deep."
    hero.say "Mike! I'm close! Oh god! I'm close to cumming!"
    "I let my own inhibitions fall too, screaming as loud as I like, calling out over the frantic sounds of our bodies colliding."
    "The pressure in my loins keeps steadily building, more and more and more even still, and from the way I feel his rod twitching and his movements becoming less and less practised, his next words don't surprise me."
    mike.say "Fuck, so am I, [hero.name]. Cum! Cum for me!"
    "He doesn't have to tell me twice."
    "With one final, grand thrust, I feel an explosion, my body shaking within Mike's grasp as white hot pleasure overcomes me."
    "I scream in ecstasy, my voice melding with Mike's own in a perfect, wonderful melody of pure bliss."
    "His grip of me almost hurts, definitely leaving a mark at least, but my nails digging into him tell a similar story, and through the haze of a quickly fading orgasm I don't care."
    "He collapses on-top of me, the two of us panting heavily."
    "His cock is still inside me, and for a moment I wonder if he'll even pull out before he answers the question with a quiet grunt, freeing his cock from the prison of my pussy."
    "I can see from here just how much semen is pooled inside the condom, but apparently Mike caught me looking, and a devious look floats across his face as he slips the rubber off his cock."
    "He holds it in front of my face, letting me get a good look at just how much is stored within, before smirking, leaning in so his ears are next to my ear once again."
    mike.say "Can't let this go to waste now, can we?"
    "I look between the rubber, then him, before grinning in return."
    hero.say "That'd be such a shame."
    "I open my mouth wide, sticking my tongue out and bracing myself as Mike slowly pours the thick, heavy, creamy contents down my throat, it's salty and unfamiliar taste lingering long after I force myself to swallow it all."
    "Well aware the taste still lingers on my lips, I quickly swivel and give Mike a quick kiss."
    "He laughs, but wipes his mouth with the back of his hand, pulling a slightly disgusted face as he does so, apparently not having enjoyed the brief payback."
    mike.say "You're amazing, you know that?"
    "My cheeks begin to feel hot, now of all times surprisingly enough, so I shut him up with another kiss."
    hero.say "So are you."
    "I break only to return the favour, the two of us grinning madly at each other, before yet again Mike's arms wrap themselves around me and pull me close."
    "I return the embrace, satisfied and happy, my eyes closing as I relax, content with the moment and, perhaps most of all, excited for what the next date might bring."
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
