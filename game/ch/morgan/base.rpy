

init -1 python:
    Event(**{
        "name":"morgan_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "morgan",
        "girls_conditions": {"morgan":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"morgan_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "morgan",
        "girls_conditions": {"morgan":{"contact":"morgan","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(15,16),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"morgan_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "morgan",
        "priority":100,
        "girls_conditions": {"morgan":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"morgan_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "morgan",
        "priority":100,
        "girls_conditions": {"morgan":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"morgan_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "morgan",
        "priority":100,
        "girls_conditions": {"morgan":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_morgan_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"morgan_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "morgan",
        "priority":100,
        "girls_conditions": {"morgan":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"morgan_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "morgan",
        "girls_conditions": {"morgan":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_morgan_hint:
    $ story = morgan.get_flag_value("story")
    "I reached the end of Morgan's story for now."
    return

label morgan_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = morgan.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = morgan.get_activity(bye_hour)
    if not activity == morgan.activity:
        if day != game.week_day:
            $ morgan.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ morgan.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "morgan "+bye_outfit
        if activity["activity"] == "sleep":
            morgan.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            morgan.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            morgan.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            morgan.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            morgan.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            morgan.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            morgan.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            morgan.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            morgan.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            morgan.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            morgan.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            morgan.say "I ll go get dressed."
        hide expression "morgan "+bye_outfit
    return

label morgan_cheated:
    show morgan
    if (game.get_flag_value("bandharem") == 1 and game.active_girl.id in ["anna"]) or (game.get_flag_value("bandharem") == 2 and game.active_girl.id in ["anna", "sasha"]):
        morgan.say "I want some too!"
        show morgan kiss
        "And without warning Morgan kisses me."
        $ morgan.love += 1
    else:
        "I see Morgan looking at me kissing someone else angrily..."
        $ morgan.love -= 5
    hide morgan

    return

label morgan_greet:
    if not morgan.get_flag_value("greeted"):
        $ morgan.set_flag("greeted",True,1)
        show morgan
        $ result = randint (1,3)
        if result == 1:
            morgan.say "Hello, [hero.name]."
        elif result == 2:
            morgan.say "Hi, [hero.name]."
        elif result == 3:
            morgan.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                morgan.say "Good morning [hero.name]."
            elif game.hour < 19:
                morgan.say "Good afternoon [hero.name]."
            else:
                morgan.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Morgan."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                morgan.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Morgan."
            elif game.hour < 19:
                hero.say "Good afternoon Morgan."
            else:
                hero.say "Good evening Morgan."
    return

label morgan_kiss:
    scene expression "bg "+game.room
    if morgan.love() + hero.charm() < 80 and not morgan.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show morgan
        "The timing feels right to me, the moment perfect for things to escalate naturally and flow into something more."
        "I have to lean in close, bending more than just my neck in order to be able to account for Morgan's petite size."
        "At first, she doesn't seem to realise what I'm doing, smoothing her electric blue hair out of her eyes as she smiles up at me."
        "My lips must be nothing more than mere inches from her own before she guesses what my intentions are."
        "She's so close to me by now that I can feel the warmth of her breath on my face."
        "But then I see her impish features contort a little, and I feel her arms pushing me backwards, pushing me away from her."
        "The briefest of expressions flashes across Morgan's face in that moment."
        "I can see no hint of disgust or annoyance that would suggest she's outraged by the idea of me kissing her."
        "But there's clearly genuine surprise as she pulls away from my clumsy attempt to kiss her."
        "From there, her features become more open, and she looks at me with wide eyes."
        "The only explanation for this new expression is that she's now feeling concern over something."
        "And then I realise that it's concern for me."
        "Even though she just instinctively refused to be kissed, Morgan's already worried that she's hurt me in the same act."
        "I never knew a girl could push me away and yet make me love her all the more by doing so."
        hide morgan
    elif not morgan.get_flag_value("kiss"):
        hide morgan
        show expression "morgan kiss "+morgan.get_clothes()+" normal"
        "When it happens, it's almost like there's no preamble or build up that I can recall."
        "We go from laughing like a couple of drunk idiots, to twining our hands together."
        "And the next thing I know, we just seem to pull ourselves together and that's it."
        "I'm bending down to put my lips to Morgan's."
        "And she's standing up on the tips of her toes, doing the opposite to achieve the same effect."
        "The kiss is pretty soft and chaste to begin with."
        "Not really much more than us pressing our lips together and enjoying the sensation of the same."
        "It's only when I open my mouth a little and feel Morgan copy the move that things become somewhat more intense."
        "I feel the very tip of her tongue brush against mine."
        "But then it retreats, as though taunting me into following it back to its lair."
        "As I take the bait, I can feel Morgan beginning to melt from the kiss."
        "She wraps her arms around my neck, and I grab her backside with mine."
        "I don't so much pick her up, as I do support her while she tries to climb up me at the same time."
        "I'm not put off or discouraged by Morgan's petite body, quite the opposite."
        "The fact that I can almost enfold her in my embrace and feel the hot tenacity of her desire is a massive turn on."
        "Likewise, I can feel her pointed tongue as it pushes past my teeth."
        "Morgan kisses like she's possessed by a hunger, and she inspires a similar feeling in my desires for her as well."
        hide expression "morgan kiss "+morgan.get_clothes()+" normal"
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != morgan and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_54
        else:
            $ morgan.love += 1
        $ morgan.set_flag("kiss",1,"permanent","+")
    else:
        hide morgan
        show expression "morgan kiss "+morgan.get_clothes()+" normal"
        "Whenever someone feels the need to comment on the height difference between Morgan and myself, I can't help but crack a smile."
        "They genuinely seem to think that it should be some kind of physical barrier that makes us unsuitable for one another."
        "In fact, it's the very thing that makes the art of kissing her that much more enjoyable."
        "For example, I can't just lean over and peck her on the cheek."
        "I can't even get a good look at her face without inclining my head."
        "Either I have to bend over a little, or she has to stand on her tiptoes - preferably a bit of both for the best possible results."
        "But the real problem for me is trying to resist actually scooping her up and kissing her as I hold her in my arms."
        "It helps to ask, of course, rather than just taking liberties."
        "Though if you've never lifted a petite woman and placed her onto a convenient table or wall so that she was easier to kiss, you've missed out one of life's great pleasures."
        "All of this means that kissing Morgan is an event, and not just a matter of a moment that's forgotten as quickly."
        "And when you have to make an effort to do something, it means so much more that you couldn't believe it."
        "It becomes something to look forward to, something to savour, and a memory that's going to say with you for a long time after it's done too."
        hide expression "morgan kiss "+morgan.get_clothes()+" normal"
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != morgan and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_55
        else:
            $ morgan.love += 1
        $ morgan.set_flag("kiss",1,"permanent","+")
        hide morgan
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
