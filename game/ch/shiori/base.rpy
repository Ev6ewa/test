init -1 python:










    Event(**{
        "name":"shiori_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "shiori",
        "girls_conditions": {"shiori":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"shiori_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "shiori",
        "girls_conditions": {"shiori":{"contact":"shiori","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(19,20),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"shiori_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "shiori",
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"shiori_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "shiori",
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"shiori_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "shiori",
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_shiori_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"shiori_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "shiori",
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"shiori_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "shiori",
        "girls_conditions": {"shiori":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

label test_event:
    "pif"
    return

label smartphone_shiori_hint:
    $ story = shiori.get_flag_value("story")
    if not shiori_love == shiori_love_max:
        "I should get to know Shiori better."
    elif not "shiori_scold_1" in DONE:
        "I should see Shiori at work."
    elif not "shiori_scold_2" in DONE:
        "I should see Shiori at work."
    elif not "shiori_scold_3" in DONE:
        "I should see Shiori at work."
    elif not "shiori_scold_4" in DONE:
        "I should see Shiori at work."
    elif not "shiori_scold_5" in DONE:
        "I should see Shiori at work."
    elif not "shiori_office_bj" in DONE:
        "I should see Shiori at work."
    else:
        "I reached the end of Shiori's story for now."
    return

label shiori_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = shiori.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = shiori.get_activity(bye_hour)
    if not activity == shiori.activity:
        if day != game.week_day:
            $ shiori.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ shiori.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "shiori "+bye_outfit
        if activity["activity"] == "sleep":
            shiori.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            shiori.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            shiori.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            shiori.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            shiori.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            shiori.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            shiori.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            shiori.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            shiori.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            shiori.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            shiori.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            shiori.say "I ll go get dressed."
        hide expression "shiori "+bye_outfit
    return

label shiori_cheated:
    show shiori
    "I see Shiori looking at me kissing someone else with envy and lust in her eyes."
    $ shiori.love += 1
    hide shiori
    return

label shiori_greet:
    if not shiori.get_flag_value("greeted"):
        $ shiori.set_flag("greeted",True,1)
        show shiori
        $ result = randint (1,3)
        if result == 1:
            shiori.say "Hello, [hero.name]."
        elif result == 2:
            shiori.say "Hi, [hero.name]."
        elif result == 3:
            shiori.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                shiori.say "Good morning [hero.name]."
            elif game.hour < 19:
                shiori.say "Good afternoon [hero.name]."
            else:
                shiori.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Shiori."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                shiori.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Shiori."
            elif game.hour < 19:
                hero.say "Good afternoon Shiori."
            else:
                hero.say "Good evening Shiori."
    return

label shiori_kiss:
    if shiori.love() + hero.charm() < 80 and not shiori.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show shiori
        "I guess that I've been guilty of reading Shiori as nothing more than a passive little mouse ever since she arrived to work under me in the office."
        "She's always been so shy and retiring, unwilling to even speak up for herself that I suppose that fooled me into thinking that she was utterly passive."
        "On top of that there's also the fact that I'm ninety nine percent sure she keeps fucking up here and there on purpose, almost as if she were trying to get me mad at her."
        "All of that kind of lead me to think that she was going to be a complete pushover, a girl that I could pretty much pounce on at any moment, as soon as the mood took me."
        "That's what inspired me to just lean in when the mood took me just now and try to have an experimental kiss at Shiori's expense."
        "I'd assumed that she wouldn't have it in her to make the slightest objection."
        "And hey, who knew, maybe I'd get a real kick out of it and it could become a regular little distraction around the office whenever the mood took me."
        "But much to my surprise, Shiori actually yelps and dodges quickly out of the way before I can manage to kiss her."
        "She doesn't say a word, offering nothing in the way of an explanation as to just why she's chosen to reject my advances."
        "Instead she hurries well out of the range of any further clumsy attempts to plant one on her."
        "And I find myself scratching my head in puzzlement as she doesn't stop until she's safely within sight of another woman."
        hide shiori
    elif not shiori.get_flag_value("kiss"):
        hide shiori
        show expression "shiori kiss "+shiori.get_clothes()
        "I've always known that Shiori was a timid sort of girl, shy and retiring to the point of being paralysed in a social situation or awkward moment."
        "So it's no surprise that, when turning around suddenly and finding her face no more than an inch or two from mine, she freezes instantly."
        "I don't know if she was trying to get closer in order to whisper something to me, or else it's just an accident of us both turning at the same time."
        "But the effect is like that of a deer caught in the headlights of a speeding car, scared rigid and unable to move, no matter the peril bearing down upon it."
        "I can hear Shiori's breathing to the exclusion of all else."
        "And I can only imagine that her heart must be racing right now, pounding in her chest."
        "I've never seen her up this close before, and I had no idea just how huge and expressive her eyes were."
        "They look to me like I could read the details of her most intimate thoughts written in them without her being able to stop me."
        "Without even thinking of what I'm actually doing, I lean in and kiss her full on the lips."
        "At first, Shiori doesn't move a muscle."
        "In fact she keeps so still and silent that I'm worried she's going to flip out and start screaming any second now."
        "But then I see something change in her eyes, and the lids slowly close, as if becoming suddenly too heavy to keep open a moment longer."
        "It's then that Shiori finally begins to return my kiss, becoming animated once more and then twining herself into me as if this is what she wanted all along."
        hide expression "shiori kiss "+shiori.get_clothes()
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != shiori and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_89
        $ shiori.set_flag("kiss",1,"permanent","+")
        $ shiori.love += 1
    else:
        hide shiori
        show expression "shiori kiss "+shiori.get_clothes()
        "While Shiori might have been slow to warm to the idea of me stealing kisses from her to begin with, she soon seems to warm to the idea."
        "Indeed the need to keep our kisses hidden and secret at first means that she begins to derive a subtle, yet growing thrill from such clandestine moments."
        "But she never takes the initiative, never chooses to be the one that seeks me out and makes the kind of furtive gestures that indicate the time has come for another liaison."
        "I start to think that she's almost as fond of the feeling of having me come and seek her out, as she is of the actual physical act itself."
        "All I need to do is give her the signal, and Shiori will come almost skipping to follow me."
        "And while she's certainly not the most impassioned of kissers, the way that she abandons herself to the experience is quite something in of itself."
        "At times, Shiori has me more than half convinced that she actually enjoys being almost overpowered in this manner."
        "It's as if she finds release in the act of surrendering to me and allowing me to be the one in control, the one making all of the decisions."
        "I keep trying not to dwell on the matter too heavily, and instead remind myself of the fact that I'm having an immense amount of fun here."
        "And surely, if she wasn't enjoying it too, Shiori would have said something to that effect."
        "Wouldn't she?"
        hide expression "shiori kiss "+shiori.get_clothes()
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != shiori and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_91
        $ shiori.love += 1
    return

label shiori_fuck_date:
    $ shiori.set_flag("sex",1,"permanent","+")
    scene bg livingroom
    show shiori












    "As soon as we're back at my place, Shiori lets me lead her up the stairs and into my bedroom."
    show bg bedroom1
    "There's no need to chat or offer her a drink before we get down to business, she simply does as she's told."
    "Even though she's more than enough to get me excited merely based off of her looks and the shape of her body."
    "Shiori keeps looking at me with sideways glances and then down at the floor, her cheeks flushing red at the same time."
    "She seems so shy and filled with anticipation at finally doing more than giving blow-jobs and getting spanked, that it's quite an ego rub for me."
    "Normally a girl would strip herself off at this point, probably make a show of it too."
    "But Shiori just stands there by the bed, biting her lip and looking at me shyly."
    "IS she really this bashful, or is it another one of her manipulative tricks intended to get her just what she wants from me?"
    "Either way, I'm too deeply taken in by her shyness now to be discouraged from taking her by the hand."
    "I take the short, tight dress that she's wearing by the hem and then proceed to almost peel it off of her."
    "Shiori lifts her arms to aid me, and I see her breasts fall free of the dress even before her head is revealed."
    show shiori naked
    "She hasn't been wearing a bra all night, instead relying upon he stretchy material of her dress to support them."
    "They're simply huge for her petite build, but they seem to be totally natural, only adding to the amazing shape of her body."
    "A moment later, her head pops free of the dress, her dark hair dropping around her face like a black mane."
    "Shiori sees the way that I'm looking at her breasts, and a truly delighted smile spreads across her features."
    shiori.say "Do you like them?"
    "As if to prejudice the answer, she puts her hands behind her back, swaying from side to side so that her breasts follow suit."
    "I can only nod a little at first, the sight of this making my mouth go suddenly dry."
    "Shiori giggles happily at my silent answer."
    shiori.say "You can touch them...if you like!"
    if not shiori.get_piercings("nipples"):
        "Eagerly I reach out and take a breast in each hand, feeling their significant weight as I do so."
        "Shiori's breasts are as incredible to touch as they are to gaze at - warm and soft like giant balls of pale dough."
        "I begin to stroke at her nipples, when I hear her sigh, almost ruefully."
    else:
        "Eagerly I reach out and take a breast in each hand, feeling their significant weight as I do so."
        "Shiori's breasts are as incredible to touch as they are to gaze at - warm and soft like giant balls of pale dough."
        "I tug at the rings that pierce her nipples, gently at first and then ever harder as she cries out in delighted pain at the sensation."
    shiori.say "Oh, darn it...I went and did it again!"
    "I look up at her, unsure of just what she can mean by that."
    shiori.say "I used my titties to lure you in, just like a naughty girl would!"
    shiori.say "You should punish me for being so bad..."
    "With that, she looks down at her nipples, and then back up at me with raised eyebrows, her expression mournful."
    "So it's punishment that she wants, is it?"
    "I take her nipples between forefinger and thumb, gently at first, but then rolling and squeezing them with increasing force."
    "Shiori moans with sudden pleasure, almost seeming to melt with the sensations she must be feeling."
    "The expression on her face is ecstatic, and she shakes with barely suppressed desire as I continue to squash and abuse her nipples."
    "I have to confess that, by now, I'm already painfully erect myself."
    "Shiori presses herself against me then, stroking the bulge in my pants as though she's hungry for more than just being roughly fondled."
    shiori.say "Maybe I could strip you...and then you could punish me some more?"
    "I nod again, wondering if I'm ever going to manage to actually get a word out of my mouth tonight."
    "She takes her time about the task, seeming to enjoy being able to do little things that I'd normally think nothing of doing myself."
    "Most girls would be outraged that a guy would even think of asking them to do stuff like this."
    "But Shiori seems to revel in the fact that it makes her seem subservient and even a little cowed."
    "One she has me fully naked, she stares at my cock with wide-eyed amazement."
    shiori.say "Mmm...I'd like to see how this feels in my mouth."
    "She licks her lips slowly and makes a satisfied sound."
    shiori.say "But maybe it's just too big..."
    "She's stroking it with her fingers now, almost ticking under the head."
    menu:
        "Tell her to suck you" if shiori.sub >= 25:
            "I'm so excited by now that I can't even think of stopping to ask Shiori to do what I want or else waiting patiently to see if she has the same thing in mind."
            show shiori bj
            "Instead I simply thrust my cock forwards while she's still making an act out of teasing me, her mouth mere inches from the tip."
            "My guess is that Shiori would have made some squeak of protest, but having an erect cock stuffed into her mouth means all I hear is a muffled yelp."
            "But much to my surprise, she only protests until what I've done becomes clear to her."
            show shiori bj suck
            "And then she seems to recover quickly, as if resigning herself to doing what I want without objection."
            "Though her technique leaves a lot to be desired, Shiori more than makes up for it in sheer enthusiasm for the task at hand."
            "She sucks and licks away with such dedication that I can't help but soon find myself breathing heavily in response."
            "As I already said, it's not as if Shiori has any kind of technique that I can describe."
            "But she looks up at me with those huge eyes, watching me as my cock fills her mouth and threatens to push right down her throat..."
            "The whole experience is enough to make me almost lose control of myself in record time..."
            menu:
                "Cum in her mouth":
                    show shiori bj suck cumshot
                    "There's no way I can hold back from cuming now, and I just hope that Shiori's ready for it!"
                    "I let out an agonised groan and lose myself while my cock is as deep in her mouth as it'll go."
                    "Shiori's eyes go wide, and I can hear her almost choking as the cum hits the back of her throat."
                    "I try to pull out, but the chaos of her coughing around my cock makes it hard to know what the best thing to do would be."
                    "Eventually, with her eyes watering, she manages to regain her breath enough for me to slide quickly out of her mouth."
                    "This leaves her gasping for air, but not looking as though she's about to die of suffocation."
                    if hero.fitness <= 50:
                        $ shiori.love -= 5
                        return
                "Cum on her face" if shiori.sub >= 50:
                    hide shiori
                    show shiori bj high
                    "I might not be able to hold back from cuming, but that doesn't mean I can't pull out in time."
                    "The mere thought of doing so is enough to give me the presence of mind when the moment comes."
                    "Before Shiori truly knows what's happening, my cock is out of her mouth and already twitching before her face."
                    show shiori bj high cumshot
                    "A moment later, the first streamer of cum splashes up across her cheek and over her forehead."
                    "Another and then another follow in quick succession, and Shiori yelps in alarm with each one that hits her."
                    hide shiori
                    show shiori bj high facial
                    "The sight of that innocent, trusting face marred in that way is something that will stick wit me for a long time to come."
                    if hero.fitness <= 50:
                        $ shiori.love -= 5
                        return
                "Hold back" if hero.fitness >= 50:
                    "Somehow, the notion of holding back and saving myself for doing something far more memorable to Shiori keeps me from losing it."
                    "I take hold of the back of her head with one hand, and carefully part her lips with the other."
                    "She looks surprised and disappointed at my actions, which makes me all the more determined to make what I do to her next sufficient compensation."
        "Tell her to give you a titty fuck" if shiori.sub >= 50:
            show shiori bj
            "As much as her mouth looks inviting, it's Shiori's huge breasts that are calling out to me tonight."
            "I reach out and take her by the shoulders, pulling her forward until my cock is wedged into her cleavage."
            "At first she looks a little baffled, and I realise that she's far more innocent than the average girl I've screwed around with in the past."
            "Gently taking her hands in mine, I guide them to the sides of her breasts and press them against the fleshy orbs."
            show shiori bj boobs
            "After moving them up and down a couple of times, I see realisation dawn in Shiori's eyes."
            "And from that point on, she no longer needs to be told what to do."
            "The sheer weight and size of her breasts means that the sensation is incredible from the start."
            "And Shiori soon begins to perspire from the effort, making her cleavage all the more slick as time goes on."
            if shiori.get_piercings("nipples"):
                "I can't keep myself from hooking my fingers into the rings that pierce Shiroi's nipples as she keeps up an impressive pace."
                "She moans and bites at her lower lip in response to the exquisite pain this causes her."
            else:
                "I find that I can't resist the temptation to reach out and pinch at Shiori's nipples as she massages my cock."
                "Her cheeks redden and she groans with pleasure at my touch, making me feel all the more aroused in response."
            "I know that if this goes on for too much longer, I won't have a choice in the matter."
            "I'll cum from what she's doing to me without any trouble whatsoever."
            menu:
                "Cum on her face":
                    show shiori bj boobs cumshot
                    "As my cock comes up from between Shiori's breasts, I stiffen my pose and do all that I can to keep it there."
                    "A moment later, the first streamer of cum splashes up across her cheek and over her forehead."
                    hide shiori
                    show shiori bj boobs facial
                    "Another and then another follow in quick succession, and Shiori yelps in alarm with each one that hits her."
                    "The sight of that innocent, trusting face marred in that way is something that will stick wit me for a long time to come."
                "Hold back" if hero.fitness >= 50:
                    "Somehow, the notion of holding back and saving myself for doing something far more memorable to Shiori keeps me from losing it."
                    "I take hold of the back of her head with one hand, and carefully part her lips with the other."
                    "She looks surprised and disappointed at my actions, which makes me all the more determined to make what I do to her next sufficient compensation."
        "Just fuck her":
            pass
    hide shiori
    show shiori naked blush
    "Shiori glances down at my still stiff cock and her expression becomes one of mock horror."
    shiori.say "You wouldn't...you wouldn't...put it inside of me...would you?"
    "Shiori begins to back away slowly, covering her crotch with one hand and her backside with the other, as if afraid that I'll stick it in her at any moment."
    "Sensing the way she wants this to go, and not being at all adverse to a little rolepaly myself, I advance on her equally slowly."
    shiori.say "Oh please...please don't!"
    "She's almost to the bed now."
    shiori.say "It's so big...there won't be room!"
    if not shiori.get_flag_value("pregnant") >= 9:
        "Shiori bumps into the bed and pantomimes falling over and scrambling onto it."
        shiori.say "Please...please...I'll be good - just don't put it inside of me!"
        "She's on all fours now, her naked ass wriggling as she clambers across the bed, being sure not to go too fast."
    else:
        "Shiori bumps into the bed, her rounded belly making her movements clumsy and causing her to collapse onto it."
        shiori.say "Please...please...I'll be good - just don't put it inside of me!"
        "She's on all fours now, her naked ass wriggling and huge belly keeping her from moving at more than a crawl."
    hero.say "It's too late for that now, Shiori!"
    hero.say "You've been a very bad girl - the worst of all!"
    "Shiori yelps and looks back over her shoulder as I begin to climb onto the bed and crawl after her."
    "She may be doing a good job of keeping up the act, but I can still see the glimmer of anticipation in her eyes as I draw ever closer."
    "It's probably out of the feeling that I'm disciplining her that I can't resist slapping Shiori's backside as I draw close enough."
    "I give her a swift, sharp crack across the right buttock, and then follow it up with one to the left for good measure."
    hero.say "That's far enough, Shiori - stop running away from me now, or I'll start to get really mad with you."
    "She stops, biting her lip in sheer anticipation as she looks back over her shoulder at me."
    hero.say "It's time that you held still and took the punishment that you deserve!"
    "At that, I sit down on the bed and pull her backwards onto my lap."
    "I slide my arms under her knees, and then wrap my hands around the back of her neck, pinning her in place."
    menu:
        "Fuck her pussy":
            "Shiori's wide open to me now, meaning that I can have my pick of just where I want to take things."
            "Her ass feels very inviting indeed, but then I notice that her neat little pussy feels so exposed and inviting that I can't resist."
            "Shiori's lips look so perfect and petite that for a moment I wonder if she was actually play-acting when she said I wouldn't fit."
            "But there's only one way to find out the truth."
            menu:
                "Use a condom" if hero.has_condom():
                    $ condom = True
                    $ hero.use_condom()
                    "I'm about to press on, when I happen to glance at the condoms on the bedside table."
                    "It only takes a moment to release Shiori grab one and slip it on, which is far better than the potential alternative."
                    "I tie her up in my arms once more, and prepare to get down to business."
                "Don't use a condom":
                    $ condom = False
                    "Shiori's the only thing on my mind at that moment, and I just can't wait a second longer to have her."
                    "Without stopping to do as much as draw breath, I thrust my cock upwards."
            show shiori reverse vaginal
            if condom:
                show shiori reverse vaginal condom
            "Shiori begins to moan, even before the head of my dick actually makes contact with her lips."
            "This means that when I finally do slide my cock along the length of her pussy, she draws in several short, sharp breaths at the sensation."
            "She's already warm and slick, but I was right to have guessed that she was going to be tight."
            "As I push my way inside of her, the walls of Shiori's pussy squeeze me so much that I gasp myself."
            shiori.say "Oh, [hero.name]...I can feel you inside of me!"
            shiori.say "You're so big!"
            "The mixture of astonishment and arousal in Shiori's voice makes the sensation of pushing into her all the more intense and enjoyable."
            "For every inch that I make it further into her, there's a sigh or a sudden panting."
            "At first I'm afraid that I'm going to cum before I'm even all of the way into her."
            "Finally, when I'm as far into her as I can go, I just stay there and enjoy the feeling of Shiori's reactions."
            shiori.say "Mmm...[hero.name]...you've filled me up!"
            shiori.say "There's no more room left inside!"
            "I begin to thrust in and out of her then, slowly at first, but then ever faster."
            "If Shiori moaned and sighed when I was just inside of her and still, she's soon crying and almost wailing now that I'm moving."
            hero.say "No more spankings for you, Shiori!"
            hero.say "This is the kind of punishment that you deserve."
            hero.say "And from now on, I'm going to see that you get it!"
            "Her whole body is trembling now, her large breasts swinging back and forth in sympathy with my thrusts."
            "Shiori's cries are getting louder now, growing in volume until I'm worried that she'll soon be genuinely screaming."
            "Perhaps she's just a screamer, but part of me can't help thinking this is all of her repressed, submissive feelings suddenly finding an outlet all at once."
            show shiori reverse milk
            "It's then I notice that her breasts have begun to weep milk, and it's seeping down her body and over me too."
            "Being this deep inside of an ecstatic banshee is almost too much for me."
            "And I can already feel myself beginning to cum."
            menu:
                "Pull out" if not condom:
                    "I don't know how I have the presence of mind to do it, but I wrench myself out of Shiori mere seconds before I cum."
                    show shiori reverse milk out
                    "As intense as the sensation of yanking myself out of her tight little pussy is for me, it must be even more so for her."
                    "Shiori actually lets out a scream and then a little burst of sobs as I leave her empty."
                    show shiori reverse milk out cumshot
                    "My cum rains down on her back, even as I see her thrust one hand towards her pussy."
                    "The cum mingles with the milk now almost squirting from Shiori's breasts as she brings herself off."
                    hide shiori
                    show shiori out reverse milk body
                    "Before the rolling white droplets on her skin have had time to cool, she brings herself off in a flurry of moaning and twitching."
                "Cum inside" if condom:
                    "The last thing on my mind right now is doing anything other than riding out every last second of my climax inside of Shiori."
                    "As I feel it take over, I push myself as far into her as I can possibly go."
                    shiori.say "Ah...[hero.name]...you're going to...make me..."
                    show shiori reverse milk cum
                    "And then she follows my lead, cuming with me so deep within her that I can feel every single moment of her climax."
                    "The milk that was leaking from her breasts before this is almsot squirting forth now."
                    "If anything, she becomes even tighter, clutching me like a fist and ensuring that I spend all of myself inside her."
                "Cum inside" if not condom:
                    "I'm just seconds away from cuming now, and it's in this instant that Shiori seems to recall that I'm inside of her without any protection."
                    "Part of me expects her to freak out and scream for me to pull out before I cum."
                    "But instead she seems to be enjoying the experience all the more."
                    show shiori reverse milk ahegao
                    shiori.say "Oh, [hero.name]...I can feel you so deep!"
                    shiori.say "Punish me some more - cum inside of me...please!"
                    "That's it, I can't hold on any longer."
                    "My orgasm sends me even deeper into Shiori, pushing her into her own, so that she writhes in my lap."
                    hide shiori
                    show shiori reverse milk pussy nodick
                    "When I finaly pull out she let a faint whimper escape her throat as my cum seep out of her pussy."
                    "The milk from her breasts is almost squirting now as she cums, making us both slick with pale white fluids."
                    if (randint(1,3) == 1 or "hung" in hero.skills) and not shiori.get_flag_value("pregnant") and not shiori.get_flag_value("pill"):
                        $ shiori.set_flag("pregnant",1)
        "Fuck her ass" if shiori.sub >= 75:
            "Shiori's neat little pussy looks very inviting, but I'm so into this idea of role-playing her punishment, that I focus on her ass instead."
            hero.say "I'm afraid a simple spanking's not going to cut it this time, Shiori."
            hero.say "You've been so bad, I need to do something far worse to you!"
            "Shiori gasps suddenly, the sound of it very different from the playfully afraid noises she's made before this moment."
            shiori.say "Are you really going to..."
            "She gulps audibly, clearly imagining what I'm about to do to her."
            shiori.say "I've...I've never had it up my bottom before!"
            hero.say "Well, I've never taken you up the ass before, Shiori."
            hero.say "So this is a new experience for the both of us!"
            "I hear Shiori audibly gulp and begin to whimper in anticipation."
            "Taking one of her milky-white buttocks in each hand, I part them a little roughly pull her backwards."
            "I pass my arms under Shiori's thighs and then knot my hands behind her head."
            "The head of my cock presses against Shiori's exposed back-passage, and she whines again at the sensation."
            show shiori reverse anal pain
            "As I begin to push myself inside of her, the progress is slow thanks to the fact that she's tense and resisting."
            "But that just makes the whole thing so much more enjoyable, claiming her an inch at a time and listening to her shrill cries as I do so."
            "When I'm finally into her as deep as I can possibly go, I stay there without moving a muscle, simply enjoying the feel of her body as she shudders in response."
            "In between her desperate gasps, Shiori finally manages to speak."
            show shiori reverse anal normal
            shiori.say "Oh, [hero.name]...you're...you're inside of me so deep!"
            "I begin to move in and out of her, returning her almost instantly to a state of helpless moaning."
            "The more that I pound away on her ass, the more Shiori's muscles contract and squeeze me inside of her."
            "Almost every time she cries out, I feel it translated into a contraction around by dick."
            "I can only describe it as a combination of the tightest hole I've ever fucked and the most aggressive hand-job I can imagine."



            "As if sensing what's about to happen, Shiori lets out a desperate wail."
            shiori.say "Ah...ah...you're going to cum...in my ass!"
            show shiori reverse anal normal milk
            "I see with some surprise, that this exclamation is accompanied by her breasts beginning to leak a constant stream of milk."
            menu:
                "Pull out":
                    "Cuming inside of Shiori would be worth it, even if just for the sake of seeing the look on her face."
                    "But I'm so into the swing of the idea that I'm punishing her by now, that I want to humiliate her some more."
                    show shiori reverse milk out
                    "Moments before I reach my climax, I begin to pull myself out of Shiori's ass."
                    "The intensity of the act and her reaction to it is almost enough to bring me off on its own."
                    show shiori reverse milk out cumshot
                    "And it means that a few seconds after I finally get my cock out of her ass, I cum."
                    hide shiori
                    show shiori reverse milk out body milk
                    "Shiori moans and whimpers meekly as the warm liquid rains down on her bally and then her breasts."
                    "But she makes no complaint, her cheeks burning with shame as it begins to run down."
                    "Almost as if in sympathy, her nipples are now practically squirting milk in quick gushes."
                "Cum inside":
                    "Although the idea of cuming all over Shiori's body is very appealing."
                    "I'm getting off far too much on being inside of her ass to be able to even think about pulling out now."
                    "I keep on pushing myself into Shiori, as far as I can go, and hearing the moans she makes in response."
                    "She must know by now what I'm planning to do, aware of how much I'm using her as something to cum in and humiliating her."
                    show shiori reverse anal ass cum
                    "Shiori screams when I finally cum, as though everything that came before was just a game, and now she's crossed an unspoken line with her desire to be degraded."
                    shiori.say "Oh, [hero.name]...you...you came inside of me...inside of my ass..."
                    shiori.say "I feel so filthy...so dirty that I'll never be clean again!"
                    "As if to further compound her shame, Shiori's breasts continue to spurt milk as she pants with sheer exhaustion."
    hide shiori
    show shiori naked
    "Afterwards, Shiori clings to me like a small, frightened animal, silent and meek once more."
    "I can't help but feel that we've gone so far tonight that there's no chance of things going back to the way they used to be."
    "For better or worse, I've succeeded in turning sweet, innocent little Shiori into a very dirty girl."
    hide shiori
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
