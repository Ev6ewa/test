init python:
    Event(**{
        "name": "kleio_start",
        "label": ["kleio_start"],
        "priority": 500,
        "duration": 0,
        "game_conditions":{"flagmin_performance":2, "flag_female":0},
        "do_once":True,
        "quit": False,
        })

    Event(**{
        "name": "kleio_start2",
        "label": ["kleio_start"],
        "priority": 500,
        "duration": 0,
        "game_conditions":{"flagmin_band":2, "flag_female":0},
        "do_once":True,
        "quit": False,
        })

    Event(**{
        "name": "kleio_event_01",
        "label": ["kleio_event_01"],
        "priority": 500,
        "duration": 4,
        "game_conditions":{"hours":(14,15),"flag_dateinprogress":0, "flag_female":0},
        "girls_conditions": {"kleio":{"min_love":20,"present":False, "flageq_story":1,'valid':True}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "kleio_event_02",
        "label": ["kleio_event_02"],
        "priority": 500,
        "duration": 4,
        "game_conditions":{"hours":(17,18),"flag_dateinprogress":0, "flag_female":0},
        "girls_conditions": {"kleio":{"min_love":40,"present":False, "flageq_story":2,'valid':True}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "kleio_event_03",
        "label": ["kleio_event_03"],
        "priority": 500,
        "game_conditions":{"activity":"wake_up", "done":"kleio_event_02","hours":(5,9),"flag_dateinprogress":0, "flag_female":0},
        "girls_conditions": {"kleio":{"min_love":80,"present":False,'valid':True}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "kleio_event_05",
        "priority": 500,
        "label": ["kleio_event_05"],
        "duration": 0,
        "game_conditions":{"room":["studio"], "done":"kleio_event_03","flag_dateinprogress":0, "flag_female":0},
        "girls_conditions": {"kleio":{"min_love":150,"present":True, "flageq_story":3,'valid':True}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name":"kleio_init",
        "label": ["kleio_init"],
        "girls_conditions": {"kleio":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "kleio_give_christmas",
        "label": ["kleio_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"kleio":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "kleio_give_birthday",
        "label": ["kleio_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"kleio":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "kleio_give_valentine",
        "label": ["kleio_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"kleio":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "kleio_practice_01",
        "priority": 500,
        "label": ["kleio_practice_01"],
        "duration": 0,
        "game_conditions":{"activity":["practice"],"flagmin_bandpractice":25,"flag_dateinprogress":False, "flag_female":0},
        "girls_conditions": {"kleio":{"min_love":50,"present":True,'valid':True}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "kleio_pregnant_flag",
        "label": ["kleio_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"kleio":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "kleio_say_preg",
        "label": ["kleio_say_preg"],
        "duration": 0,
        "girls_conditions": {"kleio":{"flagmin_pregnant":6, "flag_toldpreg":False}},
        "game_conditions":{"room":["map"],"flag_dateinprogress":False, "flag_female":0},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

label kleio_pregnant_flag:
    $ kleio.set_flag("pregnant",1,mod="+")
    return

label kleio_say_preg:
    scene bg street
    show kleio casual
    "Kleio picks me up on the street corner a little way down from my apartment block, screeching to a halt in her characteristic manner."
    "I'm already sensing that something's off with her, as she usually stops out front of my building, and now she seemingly doesn't want anyone else to see her."
    "As I open the door to get in, I notice that I'm not met by the usual blare of insanely loud punk or metal."
    "Almost before I'm strapped in and certainly before I can speak a single word, Kleio slams the car into gear and tears away from the curb."
    hero.say "And good morning to you, too!"
    kleio.say "What...did you say something to me?"
    "She's obviously distracted, making her normally erratic driving that much worse as a result."
    hero.say "I just said good morning."
    kleio.say "Oh...okay...whatever."
    "Distracted, erratic and none of her usual acid-tongued sarcasm."
    "Even I can sense that there's something serious eating at her this morning."
    hero.say "Kleio, what the hell's up with you?"
    kleio.say "It's...I'm okay, I guess - we just need to talk, that's all."
    "Those four words that all sane men dread to hear - 'we need to talk'!"
    "I say nothing until Kleio picks a suitably deserted back street and pulls in to park."
    "Taking a breath so deep I can hear it, Kleio turns in her seat to look me in the eye as she speaks."
    kleio.say "I don't know how to say this, so I'm just going to come out and say it - I'm pregnant."
    "For a second I can't seem to make sense of what she's said."
    "Then the enormity of it hits me, and I suddenly feel like I've been punched in the gut, all the air sucked out of my lungs."
    if kleio.love <= 175:
        show kleio casual sad
        kleio.say "Yeah, that's pretty much how I thought you'd take it."
        "I can see the sadness in her eyes turning into resentment as she speaks."
        kleio.say "Don't worry, I'm not gonna ask you to settle down and play happy families with me."
        kleio.say "I already called some place and made arrangements."
        menu:
            "Agree":
                hero.say "You are right, it's for the best."
                $ kleio.love -= 20
                $ kleio.sub += 5
            "Disagree" if hero.charm() >= 50:
                hero.say "Don't pretend you know how I feel, I would have supported our child all the way."
                $ kleio.love -= 10
        kleio.say "Yeah, right..."
        $ kleio.set_flag("pregnant",0)
        return
    else:
        kleio.say "Fuck it, I'm sorry to just throw all of this in your lap."
        "I can see the fear and a little bit of hope in her eyes as she lays herself open to me."
        kleio.say "I always told myself that I'd have an abortion if I got pregnant."
        kleio.say "But that was before I met you, and...well, the time we've had together kind of changed my mind."
        kleio.say "I want to keep it - but I want you to be involved as well."
    "My mouth works like a fish out of water, as I still feel breathless and stunned."
    "Kleio keeps on staring at me, as though she won't be happy until she hears something that'll satisfy her."
    menu:
        "No":
            hero.say "Jesus Christ, Kleio...you can't just throw something like this in my face and ask me to cope!"
            hero.say "I'm not even slightly ready to be a parent, and neither are you!"
            "Kleio grimaces at the sting of my words, clearly seeing her hopes dashed, but then her face hardens."
            kleio.say "What are you saying, [hero.name] - that I'd make a shitty mother, or that you're not man enough for the job?!?"
            hero.say "Yes...no...both of them...none of them...I don't know what I mean, damn it!"
            kleio.say "Yeah, maybe...but I do know that you don't care for me enough..."
            $ kleio_love = 0
            $ kleio_love_max = 0
        "Yes":
            hero.say "Yes...of course...if that's what you want...is that what you want?!?"
            show kleio casual happy
            "Kleio's face floods with what looks like a mix of relief and actual genuine joy."
            kleio.say "Of course it's what I want, you moron - would I have asked if it wasn't?"
            hero.say "Sorry...I just never thought of you as the 'mothering type' before, that's all."
            "Kleio shoots me a sideways glance, grinning slyly at the implied insult in my words."
            hero.say "Sorry again...it's something I never thought about either, but with you, it just feels right somehow."
            $ kleio.love += 10
    "The drive back to my apartment is spent in silence, as we both retreat into our own thoughts."
    "I get the feeling that a lot just happened in the space of a very short time, things that will bring big changes in the near future."
    $ kleio.set_flag("toldpreg")
    return

label kleio_event_03:
    scene bg bedroom1
    $ kleio_love_max = 150
    hero.say "Hello?"
    "Her voice sounds disjointed and far away through the phone, but I’d recognize her voice just about anywhere."
    "I could barely hear the nose of a car driving in the background, accompanied by her frantic voice."
    kleio.say "Are you awake?"
    "I blink, surprised by her frantic tone and the time of her call."
    hero.say "I am now. What’s up? Are you okay?"
    kleio.say "Sorry. Are you doing anything right now?"
    hero.say "Well, I was sleeping. Why?"
    kleio.say "I want to show you something. I’ll be at your house in 10."
    hero.say "Wait, Kleio! Hold on, I—"
    "Before I can get in a word of edgewise, I realize that she’s hung up on me."
    "Groaning, fully awake now, I decide that I may as well get ready for her arrival."
    scene bg livingroom
    "Knowing Kleio, she won’t stop until she gets what she wants, whatever that may be."
    "Purposely avoiding looking at the clock, knowing it’s way earlier than I’d ever wake up otherwise, I finish getting dressed just as I hear a quiet knock at my door."
    scene bg house
    show kleio date
    "I open it slowly, facing a small Kleio, who is staring up at me expectedly."
    hero.say "Kleio, what—"
    "Once again she interrupts me, placing a finger against my lips, shushing me."
    kleio.say "Shh. Don’t ask questions."
    $ BAD = False
    menu:
        "Insist":
            hero.say "Uh, no, Kleio, I am definitely going to ask questions. What the hell is going on?"
            "She rolls her eyes, annoyed, but decides to give me an answer."
            kleio.say "I told you, I want to show you something."
            hero.say "Show me what?"
            kleio.say "It’s a surprise, dumbass. Are you in or what?"
            "Grumbling, knowing there was no chance I’d ever be able to fall back asleep after this, I agree, allowing her to lead me down the stairs to her car."
            $ kleio.love -= 1
            $ BAD = True
        "Go along":
            "Against my better judgement, and slightly excited, I stay quiet, allowing her to lead me out of my apartment and down the stairs to her car."
    scene bg street
    show kleio date
    with fade
    "Kleio has a wild glint in her eyes as she quickly loads us into her car and takes off towards the edge of town."
    "She speeds through the empty streets, street lights shining into our car like police headlights."
    menu:
        "Tell her to slow down":
            hero.say "Kleio, what the hell? Slow down!"
            "Kleio rolls her eyes, ignoring my requests as I scramble to find my seatbelt and a handhold, praying there is no one else out on the road with us."
            $ kleio.love -= 1
            $ BAD = True
        "Enjoy the ride":
            "I can’t hold in a hoot of excitement as we tear down the streets, the night still dark and empty as we drive further and further from the city center."
            "Any thoughts of where we might be going were left behind me, my heart racing faster and faster as I realize how beautiful the girl I’m sitting beside really is."
    "Finally, we slow down, reaching an abandoned storage building that rests on the very far edge of town."
    "She curses as she realizes that the night was getting lighter, the deep navy slowly shifting into a paler blue."
    kleio.say "Damnit, we have to hurry, [hero.name]. Come on."
    if not BAD:
        "Almost unconsciously, she slips her hand into mine, dragging me across the dirt parking lot and towards the entrance of the crumbling building, kicking up dirt and grime as we run."
    else:
        "She takes off without a glance back at me, leaving me to chase after her as fast as I could, our feet kicking up clouds of dirt as we approached the entrance to the building."
    scene bg street
    show kleio date
    with fade
    "Finally, we arrive at the base of the large, almost crumbling building, staring up at the decrepit brick, the night light just barely raising before us."
    "Kleio stares up at me, a mischievous glint in her eye."
    kleio.say "Ready?"
    menu:
        "Sure":
            hero.say "Hell yeah, I’m ready."
            "With a huge smile now plastered on her face, she grabs the large concrete door and yanks it open, dragging me across the floor to a rickety metal ladder on the opposite side of the wall."
        "No":
            hero.say "No! No, Kleio, stop. Just stop. I’m all for being impulsive, but not like this. Are you high or something?"
            kleio.say "What? No! Jesus, [hero.name]. I’m not."
            hero.say "Well, regardless, I’m not going in a creepy ass building with you alone without some idea of what’s going on."
            "My words, although harsh, seem to finally get to Kleio. She sighs, turning to me, her face entirely unreadable."
            kleio.say "There’s a view. A really, really good view. And, I don’t know, it’s probably stupid—but I just wanted to share it with someone. Okay?"
            "I couldn’t hide my shock. This whole trip was just for the sake of a sunrise?"
            "I’m tempted to back out, go back home and curl into my bed, forgetting this whole ass thing, but I catch a glimpse of her face, and I can’t."
            "I can tell that, as much as Kleio doesn’t want to admit it, wants to stay tough and untouchable to the outside world, there is something underneath there that she can’t hide forever. She has pain I can’t understand, but she’s trying to let me in."
            "And the only way there is climbing up to the top of this damn roof."
            "Sighing, I lean over, and help her push the heavy door open."
    "We get to the ladder quickly, quicker than I thought possible considering the decrepit nature of the building, her body moving at an almost frantic pace to get to the top of the building."
    "The clangs of the metal are jarring, and, although I’m trying to swallow my fear, I can’t help but think that this whole thing is going to collapse out from underneath me, that this stupid ladder is how I go, and I’m going to have to explain to God what the hell I was trying to do, and, truly, having no idea at all."
    "Kleio notices my fear, and smirks, making a point to climb to the top even faster."
    scene bg rooftop
    show kleio date
    with fade
    "Despite my anxiety, we make it to the roof fine, nearly unscathed, climbing onto the large concrete surface just in time to catch the bright, scathing sun in our eyes."
    "I forget about Kleio for a moment, walking slowly towards the sunrise, soaking in the view."
    "I stare forward, the yellow beautiful and ethereal in the fresh sky."
    "Barely able to break my face away, I see Kleio, looking like a goddess in the light, almost unconsciously slide to the ground, sitting cross legged to watch the sunrise."
    "Without thinking about it, I join her by her side to watch."
    "We watch in silence, unthinking of the time or of the other person standing beside me, simply taking in the view before us, only the sounds of the settling building, the distant highway, and the other’s breath keeping us company."
    "Finally, Kleio breaks the silence with just one simple word."
    kleio.say "See?"
    "I nod, too overcome by the view to say anymore."
    if not BAD:
        "I see her smile at me, ducking her head to hide her barely visible blush."
        "It is this ethereal view, the sight of her rosy smile against the sunrise, that finally sends me spiraling back down to reality."
        hero.say "Why did you show me this, Kleio?"
        "She looks startled, but not angered, by the intrusive question."
        "She breathes in, holding it for just a moment before she let it go, her sigh heavy and laden with something I can’t entirely understand."
        kleio.say "I don’t know, [hero.name]. I know we don’t know one another all that well—we only met recently, if I’m being honest with myself."
        kleio.say "Though, I can’t help but feel that, on some level, we understand one another more than we realize, you know?"
        "Her words catch me off guard. They’re vulnerable, and, for once, completely untinged by sarcasm."
        "This was a rare moment for her, and I wasn’t ready to let her go just yet."
        hero.say "I agree, Kleio. I do."
        "She smiles, and, for a moment, I think that her beauty rivals the sunset, or, even, if I’m daring, is more beautiful than it."
        kleio.say "I know it seems really silly—it’s just a sunrise, we get hundreds of them, and we can look at pictures of them, and really, they aren’t that special at all—but, then again, this is special, in a kind of stupid way, to me, at least."
        "This is my space, my home, my little corner of the universe. I’ve never really taken anyone else up here, but I got sick and tired of being lonely every single day. I wanted to share it with someone else. So, for whatever stupid, silly reason—I brought you."
        hero.say "It’s not stupid, Kleio. I’m really glad you did."
        "I slide my hand across, grabbing hers in mine, not wanting to shatter the moment with anything more."
        kleio.say "Really?"
        hero.say "Really. I couldn’t think of anyone better to share this moment with."
    else:
        "We sit in a comfortable silence, her easily a foot away from me, lost in thought."
        "Her face is clouded with something I can’t understand, and, although I’m distracted by the sunrise, her face distracts me more."
        "Finally, I break the silence."
        hero.say "Kleio, why did you bring me here?"
        kleio.say "I don’t know. Isn’t it enough that I wanted someone to share the sunrise with?"
        "Her answer, although it’s valid, stings. I can tell she’s holding back from me."
        hero.say "Is that really all?"
        kleio.say "I don’t know, [hero.name]."
        kleio.say "Does there have to be a deep, fucking metaphorical answer to every single thing that I do?"
        kleio.say "Can’t we just want to enjoy the sunrise?"
        hero.say "Chill, Kleio. Yes, I think that we can enjoy the sunrise."
        hero.say "In a planned event. But calling me randomly, speeding down the road—wouldn’t that come across as very deliberate to you, if I did it to you?"
        "Kleio ignores me, and I can tell her walls are up, once again."
        kleio.say "Nope. Sometimes people just want to enjoy a fucking sunrise, [hero.name]."
        "I sigh, finally looking away from her, the sky shifting almost as rapidly as her moods."
        hero.say "I guess so, Kleio. I guess so."
        "We sit in silence, the light filling the spaces between us as they get wider and wider."
    scene bg rooftop
    show kleio date
    with fade
    "Finally, as the sun gets to be too high, the sky too blue to justify watching the sunrise anymore, Kleio gets to her feet."
    kleio.say "Are you ready to go? There isn’t much more to watch."
    hero.say "I guess you’re right. Let’s go."
    "We make our way down in silence, taking in the view in our own brains."
    if not BAD:
        kleio.say "So…do you want to go get coffee, or something? Talk about what we saw, or something?"
        hero.say "Really?"
        kleio.say "Yeah. I mean, only if you want to. You seem pretty tired, but that’s why I suggested coffee."
        hero.say "Yeah. Yeah! I’d like that a lot, Kleio. I’d like that a lot."
        kleio.say "Fantastic. Let’s go, then. Let’s go."
        "I smile at her, and slip my hand across the console, taking her hand into mine before we drive off towards the morning sun."
    else:
        kleio.say "Well…that’s all, I guess. I can take you home now."
        hero.say "That was really all you wanted to show me?"
        kleio.say "Yeah, that was it, [hero.name]. That was all."
        "I can sense the discomfort in her voice, and, despite my intense curiosity, I let my tiredness get the better of me, and I decide to let it go."
        hero.say "Whatever, Kleio. Let’s just head home."
        kleio.say "Sounds good. You can go get the sleep I interrupted you from."
        hero.say "Yeah…yeah. Sounds good."
        "Kleio nods, and proceeded to drive in silence towards the morning sun, with me left confused, bewildered, and unsure of where Kleio and I were."
    hide kleio
    return

label kleio_practice_01:
    "With the Battle of the bands getting so close, most of my free time had been eaten up at the practice room."
    "Save for working, eating and sleeping, playing music, or at least trying to and arguing over it was all I'd done."
    "Normally the prospect of being locked in a room with a trio of fiesty women would have been a dream come true."
    "But tempers were getting frayed as we tried to get everything just right."
    "When I noticed their moods at all, Sahsa seemed to be gloomier than ever, and Anna might actually have been sulking a little at her drums."
    "But my recent encounters with Kleio had perked my interest in her."
    "The singer's angriness now felt more like passion to me, her spikey demeanour making me ever more intrigued about her impetuous nature."
    show sasha angry
    sasha.say "Hey, [hero.name], what do you think?"
    "I stare at Sasha, not knowing what she means."
    "I was too busy watching how Kleio moves in front of the mic-stand to pay attention."
    hero.say "Huh?"
    sasha.say "Jesus, [hero.name], wake up! This is important!"
    show kleio angry
    kleio.say "Cut him some slack, Sasha - we're all fried from all this practicing."
    "I flash Kleio a brief smile as a way of saying thanks, and she returns it with an impish, knowning grin of her own."
    sasha.say "Okay, but listen to me this time, alright?"
    "I nod to signal that she should repeat her question."
    sasha.say "That last section, the one before the final chorus - I think we should go back to playing it how we used to."
    kleio.say "Yeah, right - that way always sucked, and I think we should change it, play it like I've been doing."
    sasha.say "You're the lead guitarist, [hero.name] - what do you think?"
    menu:
        "Side with Sasha":
            $ a = 1
            hero.say "If you always played it Sasha's way, maybe it's too late to go making changes?"
            kleio.say "Bullshit!"
            sasha.say "Two against one, Kleio - I win!"
            kleio.say "It was shit before and it's still shit now - we can't hope to win anything if we don't admit that and get better!"
            "Kleio tosses her guitar down, sending the stand toppling over and storms out onto the fire escape for a cigarette."
            $ kleio.love -= 5
        "Side with Kleio":
            $ a = 2
            hero.say "Kleio's way changes the whole feel of the song, makes it edgier - we need to stand out like that."
            kleio.say "YES!"
            sasha.say "We've always played it that way in the past...we don't have the time to learn a new section now."
            kleio.say "Majority rules, Sasha - I win!"
            "Kleio puts her guitar down and waltzes off to the fire escape for a victory smoke."
            $ kleio.love += 5
        "Ask Anna's opinion":
            $ a = 3
            hero.say "I liked both versions...but, Anna - what do you think?"
            "Anna looks genuinely surprised to be asked, as if she's well used to being left out of discussions between Sasha and Kleio on such matters."
            show anna
            anna.say "I'm the same - I like both, so we could use some of one and some of the other, maybe?"
            "Kleio groans like she's being tortured and stomps off onto the fire escape for a cigarette."
            show sasha
            sasha.say "Okay, Anna...let's see if we can come to a compromise."
    hide anna
    hide kleio
    hide sasha
    "I follow Kleio out onto the fire escape, worried that she's mad, but also afraid of copping her wrath at the same time."
    show kleio
    "Hearing my footsteps, she turns round to regard me."
    "She leans against the railings, cigarette in one hand and blowing out a plume of smoke."
    if a == 1:
        hero.say "Sorry if I stamped on you in there, I just thought it was a better way to play the section."
        "Kleio's expression is typically surly and dismissive, but she sniffles slightly, making me wonder if I'd accidentally found a chink in her armour."
        kleio.say "Nah, don't apologise - I'm a big girl, I can take my lumps...I just thought that after..."
        "She lets the words fade into the air like the smoke from her cigarette, clearly hoping that I'd jump in."
        hero.say "After what, Kleio?"
        kleio.say "Nothing...nevermind...I was just being stupid there for a second."
    elif a == 2:
        kleio.say "Thanks for backing me up in there."
        kleio.say "Don't get me wrong - Sasha's a great bass player, but she's no guitar wizard, and that's a fact."
        hero.say "No problem - your way was clearly miles better."
        "Kleio laughs grittily thanks to the cigarette smoke in her mouth and closes the few feet between us."
        "She wraps her arms around my neck and leans herself in closely."
        kleio.say "Seems I was wrong about you back when we first met - I'm really looking forward to collaborating with you more in the future...If you get me?"
        "For all of her radical posturing, I'm amazed to see how predictable Kleio can be when she gets what she wants and had her ego stroked in an agreeable way."
    else:
        hero.say "Just wanted to check you're okay."
        "Kleio sniffles a little, and her eyes look a little red rimmed."
        "Has what just happened in the practice room really got to such a seeminly tough girl so much?"
        kleio.say "I'm fine...really."
        kleio.say "And it's fine too - Sasha and me having to compromise."
        hero.say "I'm sorry I dragged Anna into the argument, I just felt like it wasn't my right to make the casting vote."
        kleio.say "No, you're right...we're supposed to be a band, so everyone should have a say."
        kleio.say "I guess I'm just feeling a little stupid that you, of all people, had to remind me of that fact!"
        "Kleio surprises me by putting her arms around my waist and hugging me tightly, reminding me in turn of just how pleasant her body feels this close."
    "We wait in silence as she finishes her cigarette, and then we go back inside."
    "All I can think as we walk through the door is how much Kleio keeps hidden and intrigue I feel for those depths of her personality."
    hide kleio
    return

label kleio_give:
    if not "cool sunglasses" in hero.inventory.keys():
        $ gift = Equip("cool sunglasses", money_cost = 100, type = "accessory", effects = {"submissive":20,"rebel":20,"charm":5})
        "She hands me a small box."
        hero.say "Wow !\nIs those glasses looks great!"
        hero.say "Thank you so much."
    elif kleio.love() >= 25 and not "military boots" in hero.inventory.keys():
        $ gift = Equip("military boots", money_cost = 100, type = "accessory", effects = {"submissive":20,"gourmand":20,"charm":5})
        "She hands me a pair of boots."
        hero.say "They look fantastic."
        kleio.say "Your welcome [hero.name]."
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "She hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label kleio_give_valentine:
    show kleio
    "Kleio walks hesitantly towards me."
    call kleio_greet from _call_kleio_greet_7
    show kleio
    kleio.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Kleio throws a box of chocolates towards me."
    hero.say "Thank you, Kleio."
    $ hero.gain_item(gift)
    hide kleio
    return

label kleio_give_birthday:
    show kleio
    "Kleio walks towards me."
    call kleio_greet from _call_kleio_greet_8
    show kleio happy
    kleio.say "Happy birthday [hero.name]!"
    call kleio_give from _call_kleio_give
    return

label kleio_give_christmas:
    show kleio
    "Kleio walks towards me."
    call kleio_greet from _call_kleio_greet_9
    show kleio happy
    kleio.say "Merry christmas [hero.name]."
    call kleio_give from _call_kleio_give_1
    return

label kleio_init:
    if "kleio" not in HIDDEN:
        $ HIDDEN.append("kleio")
    $ kleio.set_flag("nodate")
    $ kleio.set_flag("nokiss")
    return

label kleio_start:
    $ kleio_love_max = 20
    $ kleio.set_flag("story",1)
    $ if "kleio" in HIDDEN: HIDDEN.remove("kleio")
    return

label kleio_event_01:
    $ kleio_love_max = 40
    $ kleio.set_flag("story",2)
    play sound "sd/cell_vibrate.mp3"
    pause 1.0
    hero.say "Hello?"
    kleio.say "Hey. It’s Kleio."
    $ hero.smartphone_contacts.append("kleio")
    if hero.charm >= 25:
        hero.say "Oh, hey Kleio. What’s up?"
        kleio.say "Nothing, really. I just figured I’d call you and see if you wanted to come to the mall."
        hero.say "With you?"
        kleio.say "No, with my dog. Of course with me."
        if game.get_flag_value("band"):
            kleio.say "You had better taste in music than I expected when you played for us, and I want someone to go to the record store with me."
            kleio.say "Are you in or out?"
        else:
            kleio.say "You seem to have better taste in music than you looks implies, and I want someone to go to the record store with me."
            kleio.say "Are you in or out?"
        hero.say "Oh! Uh, in. Definitely in. Should I meet you somewhere, or—"
        $ kleio.love += 1
    else:
        hero.say "Kleio? How did you get my number?"
        kleio.say "Does it really matter that much? Sheesh, why are you so defensive?"
        "She’s one to talk."
        hero.say "Nevermind. Sorry. What do you need?"
        kleio.say "I’m bored, Sasha’s at work and Anna is busy. Do you want to come shopping with me or not?"
        "I hesitate. Shopping isn’t my thing by any means, but any chance to break down Kleio’s icy exterior is probably one I should take."
        hero.say "Um. Sure, I guess. What are we shopping for?"
        kleio.say "Music."
        hero.say "Oh. Uh, ok then."
    kleio.say "Meet me at the mall."
    hero.say "I'll be there."
    kleio.say "See you in a minute."
    "Before I even realize it, Kleio hangs up the phone on me."
    scene bg black with fade
    $ renpy.pause(0.1)
    scene bg mall
    show kleio date
    "When I arrive, Kleio is waiting for me at the entrance of the mall."
    kleio.say "Come on, let’s go. The music store closes at eight and I want to be there before it’s empty."
    "Shrugging, I follow along, deciding against mentioning whatever had made her upset—for now."
    "We walk in relative silence, with only a few short words between us, Kleio occasionally tapping away at her phone as we walk."
    "Feeling confident, I decide to ask her about it."
    if hero.charm < 25:
        hero.say "Who are you talking to on there?"
        show kleio date annoyed
        "Kleio glares at me, eyes flaring, and I immediately get the notion that asking this was a bad idea."
        kleio.say "None of your business, asshole. I invited you out to go shopping, not to interrogate my personal life."
        "Before I get another glance, she slides her phone back into her pocket."
        $ kleio.love -= 1
    elif "video_games" in hero.skills:
        hero.say "Playing a game?"
        "Kleio scoffs, slipping her her phone in her pocket, stifling a laugh."
        kleio.say "What, am I twelve now? No, I’m just texting."
        hero.say "Who? Is it someone I know?"
        kleio.say "Ugh. No. Mind your own business, okay?"
        hero.say "Ah. Well, I definitely recommending downloading this one game. It’s called—"
        kleio.say "No offense, but I don’t really care."
        "Despite her harsh words, I can see her hiding a smirk."
        $ kleio.love -= 1
    else:
        hero.say "Whatcha doing?"
        "Kleio looks up at me, annoyed."
        kleio.say "Nothing. What does it matter?"
        hero.say "I was just curious. It’s not a big deal. It’s just, by the way you were typing, it looked important."
        kleio.say "Well, it’s not, okay? Quit being so nosy."
        "Before I get another glance, she slides her phone back into her pocket."
    show kleio date
    "Although it worries me for her, I decide against asking at all, knowing it would just upset her."
    "She leads me through the mall, dead set on her musical mission, as we weave through the patrons and departments."
    "I find myself nearly getting lost a few times, only stumbling up beside her just as we reach the entrance."
    kleio.say "Hurry up, slow-poke. We’re here."
    "Swallowing, I follow her, hoping to God this goes well."
    "We’re barely ten seconds into the store before she starts bombarding me with questions."
    kleio.say "Okay, [hero.name], which do you think? This record or this one?"
    "She holds up two records, and I gulp. This is my chance to prove myself, and I have no idea if I’m gonna get this right."
    $ A = 0
    menu:
        "Michael Jackson":
            hero.say "I definitely think you should go with the Michael Jackson album. I mean, who can go wrong with the King of Pop?"
            "Kleio looks unsure."
            kleio.say "I mean, I guess. He was cool and all, don’t get me wrong, but I mean, I’m more of a guitar person myself."
            "I wince. Of course. I should’ve known that. I’m picking albums for Kleio, not myself. Damnit."
            hero.say "You’re right. Maybe you should go with the other one."
            kleio.say "Yeah, maybe. I’ll take your word for it for now."
            "Hesitantly, she shoves the album up under her arm."
        "Metallica":
            hero.say "Metallica all the way. Come on now, is that even a question?"
            "Kleio grins, shoving the album up under her arm without a second thought."
            kleio.say "Hell yeah, my dude. This one even has my favorite song on it: Master of Puppets."
            hero.say "Oh, yeah. That’s an awesome song. The guitar in that is unreal."
            kleio.say "Right??"
            $ kleio.love += 1
            $ A += 1
    kleio.say "Come on, let’s keep looking."
    "We wade through the store, Kleio working silently, picking up albums and examining them almost like a collector would."
    "Despite her almost permanent scowl on her face, I can’t help but notice how beautiful she looks as she picks over this records."
    "Her physique is entertaining enough that I don’t even really mind being here."
    "However, she eventually breaks my reverie, asking for my opinion once again."
    kleio.say "What about these two? Which do you prefer?"
    menu:
        "Elvis Presley":
            hero.say "Uh, probably Elvis. He’s really great."
            "Kleio frowns, looking at the albums again."
            kleio.say "You’re right, but I’m not sure if he’s really my style."
            hero.say "I mean, he makes rock music! We wouldn’t have rock music without him."
            kleio.say "Yeah. You’re right."
            "She shoves the album underneath her arm, but she doesn’t look too happy about it."
        "Disturbed":
            hero.say "Disturbed are a seriously kickass band, in my opinion, at least."
            "Kleio grins, flipping the album over to read it."
            kleio.say "You have better taste in music than I thought, boy. I may just have to get this."
            "I can’t hold back my smile."
            hero.say "I think you should. You’d love it."
            "With a huge smile, she shoves the record up under her arm before moving on."
            $ kleio.love += 1
            $ A += 1
    "It isn’t long before her arms are full of albums, juggling them beneath her."
    "She’s trying to hide the fact that she’s struggling, but she’s not very good at it."
    "Finally, I decide to step in."
    hero.say "Let me help you. At least until we get to the counter."
    if A == 2:
        "Kleio tries to look defiant, but the blush permeating her cheeks stops it quickly. I open my arms, and she deposits them cheerfully."
        kleio.say "Thanks. I appreciate that. You’ve been very helpful today."
        hero.say "Anytime, Kleio. I’ve liked helping out."
        $ kleio.love += 1
    elif A == 1:
        "Kleio looked up at me, almost startled by my offer."
        kleio.say "Oh. Uh, sure. Here, you can take half, and I’ll carry the other."
        "Shrugging, I accept the offer, knowing her pride was probably in the way for letting me take them all."
        "She deposits half of them carefully into my arms."
    else:
        show kleio date annoyed
        "Kleio rolled her eyes, turning away from me."
        kleio.say "Oh, so now you decide to be helpful?"
        "I’m a little baffled by her response, but I do my best to try again."
        hero.say "I was only trying to be nice, Kleio."
        kleio.say "Yeah, well. I’ve got it."
        $ kleio.love -= 1
    show kleio date
    "Kleio turns to me."
    kleio.say "I’m ready to check out. Come on, the register is this way."
    "Nodding, I follow her, watching her silently check out the records, the clerk filling two plastic bags full before she turns to me."
    kleio.say "Ready to go?"
    "Nodding, I agree with her."
    hero.say "Yeah, sure. Let’s get going."
    "We walk in silence again, weaving through the nearly empty mall, exiting through the same door we came before Kleio decides to speak again."
    if A >= 1:
        kleio.say "Sorry for being so distant today. I’ve been...dealing with some stuff, and I needed a distraction."
        "I’m a little shocked by her admission, but I try not to show it."
        hero.say "I understand. It’s no worries at all—do you want to talk about it? Maybe I can help."
        "Kleio sighs, making her way back towards my place, walking in silence for a moment before she decides to speak."
        kleio.say "My girlfriend and I broke up today."
        if hero.charm < 25:
            hero.say "Oh, so you’re gay?"
            show kleio date annoyed
            "Kleio rolls her eyes, huffing in annoyance."
            kleio.say "Seriously? Is that really all you care about? For your information, no, I’m not. Well, not exactly. I’m bi. But it doesn’t really matter."
            "I falter, realizing my reaction had obviously offended her."
            hero.say "I’m sorry, Kleio. I didn’t mean to upset you. I just didn’t know."
            show kleio date
            kleio.say "Yeah, well, now you do. Not like it matters now, anyway. She’s out of my life, and I’m better off for it."
            hero.say "I hope so."
            "We walk in silence, before reaching the door to my apartment complex. We stand awkwardly for a moment, before she finally breaks the tension."
            kleio.say "Well, have a good night, [hero.name]. Thanks for coming."
            hero.say "You’re welcome, and you too, Kleio. I’m sorry about your girlfriend. If you need me, I’m a phone call away, okay?"
            "She nods, smiling slightly before turning away, disappearing into the evening, leaving me to walk myself upstairs alone."
            hide kleio
        else:
            hero.say "Oh, my gosh, I’m sorry to hear that. Are you doing okay?"
            "She shrugs, looking a bit resigned as she answers."
            kleio.say "Yeah. I mean, as fine as I can be after a breakup."
            kleio.say "I saw it coming for a while, if that counts for anything. It was like ripping off a band-aid though—it hurts, but it had to happen."
            hero.say "I totally understand that."
            kleio.say "It just sucks, I guess, you know? I mean, any breakup sucks, but the way she did it—it was like I didn’t matter to her at all."
            hero.say "What do you mean?"
            kleio.say "She texted me. That’s why I was on my phone so much on the way to the mall."
            kleio.say "I was trying to do damage control, to try and fix things between us again—I just didn’t realize that for once, things weren’t fixable."
            hero.say "Sometimes, things aren’t meant to be fixed. Maybe you’re better off without her."
            kleio.say "You think?"
            hero.say "I mean, you seem okay. Anyone who makes you sad and treats you like that doesn’t really deserve to be in your life, you know?"
            kleio.say "I know. You’re right. It just—hurts. Sorry to drag you into this. I just needed someone today."
            hero.say "Don’t worry about it. I’m glad I could help a little bit though."
            "Though she’s sad, she smiles slightly, and I feel my chest swell when I realized I made her smile."
            kleio.say "Yeah. Me too."
            "We walk in silence for a moment, and, almost unconsciously, I slip my hand into hers. For the moment, it feels right, and she doesn’t object."
            "Eventually, we reach the door to my apartment complex, and she breaks her hand from mine. For a moment, we stand awkwardly, neither of us knowing quite what to do."
            kleio.say "Well, goodnight [hero.name]. Thank you for coming tonight. It really means a lot to me."
            "I smile, pushing a strand of hair behind her ear, stepping closer to her. I feel her heart pounding against mine, our chests pressed up against one another."
            hero.say "Anytime, seriously."
            $ kleio.love += 1
            "She smiles, gazing up at me, and, before I have a chance to second guess myself, I lean down and kiss her."
            "For a moment, she seems startled, but then she leans into the kiss, wrapping her arms around my neck, leaning comfortably into my body."
            "Her lips are soft and warm against mine, and, when she finally pulls away, I feel it’s far too soon."
            "I want nothing more than to kiss her again, feel her body, her breasts pressed against me. It takes everything I have in me not to pull her into me again."
            "She blushes, and, by the way she’s looking at me, it’s clear she’s feeling the same."
            "But, before her hormones get the best of her, she steps away, with a smile still plastered on her face."
            kleio.say "Goodnight, [hero.name]."
            "I just smile, watching her go, gazing at her until I can no longer catch sight of her figure in the masses."
            hide kleio
            "Unable to wipe the smile from my face or the memory of her kiss from my mind, I turn to my complex, ready to tuck in, knowing who would be plaguing my dreams for the rest of the evening."
    else:
        kleio.say "Are you okay to walk yourself home? I have somewhere I need to be."
        "Somewhat startled and hurt by her question, I try my best not to show it."
        hero.say "Oh, uh, sure. It’s no problem. Are you sure you don’t want me to walk you home? It’s really no bother."
        kleio.say "I can handle myself. Thanks, though."
        "Kleio nods, and I realize she’s already leaning away from me. At this point, I have to let her go."
        hero.say "Okay. You’re welcome. Have a good night, Kleio. Thanks for hanging out with me."
        kleio.say "Yeah. I’ll see you at practice, [hero.name]."
        "I watch her go, walking quickly and brusquely, and I find myself feeling almost sad as she leaves."
        hide kleio
        "Hoping I can redeem myself later, I turn, prepping myself for the long walk home that I hadn’t anticipated taking alone."
        "Turning my gaze from the sunset and Kleio to the quickly rising night, I begin my lonely journey home."
    $ kleio.set_flag("nokiss", False)
    $ game.room = "mall"
    return

label kleio_event_02:
    $ kleio_love_max = 100
    $ kleio.set_flag("story",3)
    play sound "sd/cell_vibrate.mp3"
    pause 1.0
    $ s = 0
    hero.say "Hey Kleio, what’s going on?"
    kleio.say "Nothing much"
    "Anyways—are you doing anything right now?"
    hero.say "No, not really. Why?"
    kleio.say "How do you feel about tattoos?"
    "For a moment, I can feel my heart plummet into my stomach."
    "I know that Kleio and I are getting close, but, if she’s suggesting matching tattoos, that’s a one-way train to crazy town that I really don’t want to be on."
    hero.say "Uh, Kleio, I’m glad we’re friends, but..."
    kleio.say "Bitch, do you think I’m suggesting we’re getting matching tattoos? Oh my God..."
    hero.say "Oops. Well, can you really blame me, Kleio?"
    kleio.say "Quit being a dumbass. Do you want to come with me while I get my tattoo or not?"
    hero.say "Uh, sure, I guess."
    kleio.say "Great. I’m outside. Hurry up—my appointment is in 10 minutes."
    hero.say "What? Kleio—"
    "Before I can finish my statement, she abruptly hangs up on me."
    "She has a bad habit of doing that, and of randomly showing up at my apartment, but, considering her, I had better get used to it."
    scene bg street
    "I get dressed quickly before making my way down the stairs to her car. She is lounging outside, finishing up a cigarette, before she sees me."
    "She doesn’t waste time in waving; instead, she jumps into the car, gesturing I follow, before speeding off towards the parlor."
    "She speeds and swerves through traffic, her music blaring so loud that I have to scream to talk to her. However, she doesn’t seem phased."
    hero.say "What are you getting?"
    kleio.say "You mean, what tattoo?"
    hero.say "Yeah."
    kleio.say "I’m not sure. I haven’t quite decided. I’m torn between two—a wolf walking across my collarbone, or a pair of angel wings on my back. Which do you think?"
    menu:
        "Wolf":
            hero.say "A wolf. Duh! That’s so badass."
            kleio.say "You think? I was worried it came off a little too 'alpha bitch'."
            hero.say "No, totally not. I love it, and you should totally get it. I mean, if it’s want you want, anyways."
            kleio.say "Sorry, I think I'll go with the wings [hero.name]."
            $ tattoo = "angel"
        "Angel wings":
            hero.say "Get the angel wings! Holy shit, those would be cool as fuck."
            kleio.say "Right? It’s an idea I’ve had since I was a kid. I’ve just never really had the opportunity to get it done before now."
            hero.say "Well then seize the motherfucking day then, Kleio. Get your angel wings."
            kleio.say "You know what? I absolutely should. Thanks, [hero.name]."
            $ tattoo = "angel"
            $ s += 1
        "None":
            hero.say "I’m not sure, I’m not really a big fan of tattoos."
            "Kleio rolls her eyes at me, clearly annoyed."
            kleio.say "Prude."
            hero.say "Hey!"
            kleio.say "Whatever. I’ll just figure it out myself."
            $ tattoo = "None"
            $ s -= 1
    show kleio
    scene bg mall
    "Before I even realize it, we’ve arrived at the tattoo parlor."
    "The neon sign is blinding, and the artistry, although clearly talented, is gaudy as hell. I feel a chill as she drags me into what is clearly her element."
    "She is not an unknown patron in this shop, sharing a smile with nearly everyone she passes."
    "I feel very uncomfortable, watching the stares rake up and down my unfamiliar body as she makes her way to her appointment room."
    "Her artist, clearly expecting her, is prepped and ready for her arrival. They exchange pleasantries, with me almost entirely ignored, waiting on the sidelines."
    "Finally, without a word to me, the tattoo artist gestures to a small folding chair in the corner, designed for guests of the one getting the tattoo."
    "Feeling regret about this whole endeavor, wondering if I even should have come, I slip into the chair, hoping that at least some part of this will keep me interested."
    "Luckily, I don’t have to wait very long for something interesting to happen."
    "As though it was normal, as though it didn’t matter at all, Kleio crossed her arms at her waist and casually pulls off her shirt."
    hide kleio
    show kleio topless
    "Although I could feel her eyes on me, I couldn’t help but take in the view—she had gorgeous breasts, and I couldn’t stop thinking about how it would feel to have my hands on them..."
    "My reverie is interrupted by Kleio’s harsh laughter."
    kleio.say "Enjoy the view, lover boy, because it’s all you’re gonna get for a while."
    hide kleio
    "As soon as she said it, she slid into the chair, breasts down, back up, hiding herself from my view in preparation for the needle."
    "Feeling slight dazed, I struggled to get my thoughts straight again as the whirr of the needle began to fill the room."
    "We sit in silence for a while, and I feel the awkwardness fill the room."
    "It’s hard to hear over the tattooists needle, and he needs to concentrate, so yelling isn’t very conducive in the room either."
    "For a while, it is just Kleio and I, eyes awkwardly locking every few minutes as the needle dives and surfaces from her flesh."
    "Finally, though, after about an hour of waiting, the artist stepped out to take a quick water break."
    "Kleio sighs, clearly relieved to have a break from the pain, before turning to me."
    show kleio casual
    kleio.say "Have you ever considered getting a tattoo or piercing before?"
    menu:
        "No way":
            hero.say "No way."
            "Kleio rolls her eyes before continuing the conversation."
            "Why not? Too chicken?"
            menu:
                "Yeah":
                    hero.say "Yeah...I just have a low pain tolerance, I guess."
                    kleio.say "Oh my God, don’t be such a fucking baby. It’s really not that bad, honestly, especially after you get used to it."
                    hero.say "I don’t know, Kleio. I’m just not feeling it."
                    show kleio annoyed
                    "She scoffs, annoyed, as the artist reenters the room, looking rejuvenated."
                    kleio.say "Whatever."
                    $ s -= 1
                "No":
                    hero.say "No."
                    kleio.say "Then what is it?"
                    "I shuffle uncomfortably, knowing this is going to be an unpopular opinion, especially in a tattoo shop."
                    hero.say "It’s nothing against you, or anyone in this place, but I just personally think that the unblemished human body is the most beautiful thing in the world, and adding anything else too it just detracts from the whole thing."
                    hero.say "Like a bumper sticker on a Ferrari."
                    "Kleio looks annoyed, but, surprisingly, keeps her cool, sounding almost dry as the artist comes back into the room."
                    kleio.say "How very Biblical of you."
                    "I roll my eyes, watching, almost bored, as the artist finished the last of the work, shooing us out of the store before I really have another chance to blink."
        "Yes":
            hero.say "Hell yeah!"
            "Kleio’s eyes glint with excitement at my words."
            kleio.say "Then why not get something done? You don’t have any yet, right?"
            hero.say "I don’t know, I’ve just never really had the time or the money, you know?"
            kleio.say "You have the time now, and the money, too, right? Go wild, my dude."
            menu:
                "Not right now":
                    hero.say "Eh, maybe another time. I want to think about it more, you know?"
                    kleio.say "Suit yourself, lover boy. It’d make you like ten times hotter."
                    "My mind starts racing, wondering what it means if Kleio thinks I'm hot, as the artist reenters the room to continue."
                    "I watch, almost bored, as the artist finished the last of the work, shooing us out of the store before I really have another chance to blink."
                "Sure":
                    $ s += 1
                    hero.say "You know what, maybe I will."
                    "Right as I speak, the artist reenters the room, overhearing the tailend of our conversation, dollar signs flashing in his eyes as he hears my passing remark."
                    artist_say "What do you want done? I have a buddy who could come fit you in."
                    if hero.money < 200:
                        hero.say "Ah, I was just dreaming. I don’t really have the money for much of anything at the moment."
                        artist_say "Whatever. Suit yourself, my dude. Hopefully we’ll see you back soon. In the meantime, let me finish up on your lady friend here."
                        "I sigh, leaning back into my chair, waiting as the artist finished the last touches on Kleio’s piece."
                    else:
                        menu:
                            "Tattoo":
                                $ c = 0
                                hero.say "A tattoo."
                                artist_say "Fantastic. My buddy in the back can help you out after I finish up with Kleio here."
                                "She shouldn’t have much more to go."
                                "Feel free to flip through the catalogue."
                            "Piercing":
                                $ c = 1
                                hero.say "A piercing."
                                artist_say "Sounds good to me. It shouldn’t take too long, either. Let me finish up with Kleio here, and we can all go back."
                        "The Artist smiles, finishing up Kleio’s piece for the next few minutes as I anxiously await my fate."
                        "Sooner than I thought possible, he was done, tidying up his things and breezily going over aftercare with Kleio."
                        "She approached me with a grin, linking arms with me before dragging me back to the back office."
                        if c == 0:
                            artist_say "Alright, did you make a decision?"
                            "At Kleio’s encouragement, I point to the design I chose—nothing too extravagant for my first time."
                            "The artist nods his approval, and, almost like I was in a dream, I found myself in the seat, listening to the buzz of the needle."
                            "Kleio holds my hand as we go, her breasts hanging so close to my face, grinning at me like a child at a candy store, sending my heart and my mind into a fluttering, dirty mess."
                            kleio.say "It looks great."
                            "We remain like that for a while, the dull aching pain easily forgotten when replaced with Kleio by my side."
                            "Before I know it, the tattoo is done, the artist leaning back from my body and grinning as he admired his work."
                            "He delivers his aftercare advice with ease, my mind struggling to pay attention as Kleio’s warm body pressed closer and closer into mine."
                            "Hoping I had done everything right, we leave the shop, almost giddy, admiring our new art together."
                        else:
                            artist_say "Nice choice. Just hold still—this shouldn’t take long."
                            "Kleio slips her hand into mine, squeezing it nicely as the artist prepped the area for the needle."
                            "I held my breath noticing her beauty, her warm skin, her breasts pressed so nicely against me, that I barely even noticed the needle jam itself into my skin."
                            "Before I even know it, it’s all over, and we leave the shop, smiles on our faces, clutching aftercare in our hands as we leave the store, almost giddy."
    if s >= 0:
        show kleio happy
        kleio.say "I had a lot of fun today, [hero.name]. And it looks like you did, too. Thank you for coming."
        hero.say "Anytime. Anything for you, Kleio."
        "She grins at me, before reaching up, and placing a breathy kiss on my cheek."
        "My mind is spinning, grin plastered permanently on my face, unable to even breathe the whole ride home."
        $ kleio.love += 5
    else:
        show kleio annoyed
        kleio.say "Well, thanks for coming."
        "I’m not stupid—I can tell things are awkward between us. Whatever it may be, I don’t want stick around to find out what’s causing it."
        hero.say "Yeah. Anytime, I guess."
        "She smiles weakly, before gesturing to her car, at least having the decency to take me home."
        "My mind reels the whole ride home, confused and wondering what Kleio and I even are."
    hide kleio
    $ kleio.set_flag("nodate", False)
    $ game.room = "map"
    return

label kleio_event_05:
    $ kleio_love_max = 180
    $ kleio.set_flag("story",4)
    scene bg studio
    "Every string I pluck on my guitar is nearly drowned out by the rain outside."
    "It’s exhausting, trying to write music in these conditions, and I’m considering asking if we can just call it a night."
    show kleio at left
    "Kleio, however, has me slightly distracted; her head is in my lap, leaning back as she hums a few muted tunes, while I absentmindedly stroke her hair. As exhausted as I am, I don’t want this night to end."
    show sasha angry at right
    "Right as I’m about to open my mouth to see what the plan is, Sasha, annoyed, throws down her sheet music, quickly getting to her feet."
    sasha.say "I can’t do this anymore. I’m exhausted, and we are’t getting anything done."
    "Kleio sits up from my lap, confused."
    kleio.say "But Sasha, there’s a massive rainstorm going on. Are you sure you want to leave?"
    "Sasha says nothing, just glares at Kleio through sleepy, angered eyes as she gathers up the rest of her things."
    menu:
        "Walk Sasha home":
            hero.say "Let me at least walk you home, Sasha."
            hide kleio
            "Although she’s annoyed, she relents, and I gather her things and hold the door for her as we walk towards the front door of the small studio."
            "As soon as we’re out of earshot, she spins around to face me, quickly grabbing her things from my arms."
            show sasha
            sasha.say "What are you doing with me?"
            "Baffled, I sputter out a reply."
            hero.say "What do you mean?"
            sasha.say "Kleio has been all over you for, like, the past two weeks, and instead of taking the opportunity I tried to give you, you’re walking me out. You’ve gotta go back in there, I’m sure she’s waiting on you."
            hero.say "What are you talking about?"
            hero.say "Kleio isn’t into me. We’re just—friends, I guess."
            "Sasha rolls her eyes."
            sasha.say "You’ve got to be kidding me. I knew you were an idiot, but I didn’t know you were blind, too. Go back in there. Trust me for once, okay?"
            "Even though her words slightly embarrass me, I find myself nodding along anyway. I see the way Kleio looks at me, and I definitely do want more of it. Perhaps this annoying rainstorm has given me a chance."
            hide sasha
            "With a small smile to Sasha, I say goodbye, before returning back to the studio."
        "Let her leave":
            "I say nothing to Sasha, but do my best to be helpful despite her irritating attitude."
            "I quickly stack up her things, handing her a stack of sheet music, and push her backpack over to her."
            show sasha
            sasha.say "Thanks."
            "I smile at her."
            hero.say "It's nothing, Sasha. Goodnight."
            "Kleio follows suit."
            kleio.say "Goodnight!"
            hide sasha
            "All we get is a door slammed roughly on us, accompanied by a loud roll of thunder from outside."
        "Tell her to stay":
            hero.say "Sasha, I really don’t think that’s a good idea. It’s not safe out there."
            "Sasha glares at me, sending daggers piercing through my skin as she roughly gathers her things."
            sasha.say "And who are you to try and stop me?"
            "I hesitate a bit, but the rainstorm doesn’t seem to be letting up at all, and I really don’t want Sasha to do something stupid just because she’s tired and annoyed."
            "I get to my feet, walking towards her."
            hero.say "Sasha—"
            show sasha wtf
            sasha.say "Shut up, [hero.name]!"
            hide sasha
            "Snarling, she turns her back on me and slams the studio door in my face."
            "Kleio sucks in her breath, and let out a low whistle behind me."
            kleio.say "Yikes."
    show kleio
    "Hesitantly, I return to Kleio, who is now sitting cross-legged, elbows on her knees, leaning forward so far her shirt is gaping wide open. I can’t help but take a look—she has gorgeous breasts."
    "She notices me looking, but, instead of shying away, she lets a slight smile play on her lips as she innocently leans forward just a tiny bit more, just enough to keep me interested."
    "My thoughts are scrambling as I stutter for a response."
    hero.say "So, uh, what are we gonna do for the rest of the night?"
    "Kleio smiles, shrugging her shoulders. Her breasts move with her."
    kleio.say "I’m not sure."
    "Thunder rolls in the distance, and she winces, slightly."
    kleio.say "Definitely not going out in that."
    "I pull my eyes away from her chest, and go sit down next to her again."
    hero.say "You know, you look really good tonight, Kleio."
    "She blushes, but doesn’t shy away. Instead, she stares deeply into my eyes, looking almost seductive as I cross the room."
    "My heart is pounding as I slowly take my seat next to her."
    "I manage to get out a stutter, but nothing further, simply blushing before I cross the room."
    "Kleio notices my nervousness and grins, watching me closely as I take my seat beside her."
    "She quickly flops down onto my shoulder, staring slightly up at me, eyes blinking slowly."
    "I feel my skin growing hot, embarrassed and aroused by her gaze."
    "I shift my seating position slightly, trying to hide my growing boner."
    "It doesn’t work. Kleio sits up again, clambering around to sit on front of me, propped up on her knees, ass resting on her feet."
    "She drags her eyes down my chest, her eyes settling on my growing bulge, her face mere inches from mine when she speaks."
    kleio.say "Excited, are we?"
    "I match her energy as best I can, leaning forward, close enough that our noses are now touching."
    "I smirk slightly, gazing deep into her eyes, only breaking my gaze to get a quick glance at her lips."
    hero.say "Can you blame me?"
    "I’m barely able to contain myself as I watch her slowly move closer."
    "Unable to help it, I find myself blushing profusely, once again trying to shift so that my boner is hidden."
    hero.say "Um, I’m sorry."
    "As I move, she reaches out, grabbing my knee and stopping me from moving."
    kleio.say "No, don’t move. I don’t mind."
    "Barely seconds pass before her lips are on mine."
    "She kisses me fiercely, hands moving swiftly to knock my legs out of the way before she climbs into my lap, wrapping her long, beautiful legs around my waist."
    "I tangle my hands in her short hair as she wraps her arms around me, digging her nails sharply into my back."
    "I gasp as she claws at me, and I feel her smile against my opened mouth."
    "Clearly this was her intention; she slips her tongue inside my mouth to meet mine, kissing me hard as she begins to rock her hips against mine."
    "My dick is rock-hard now, and I no longer try and hide it."
    "I’m shameless as she grinds against me, moaning against her lips as she kisses me."
    "Unable to help it, I slide my lips off hers, kissing down her neck, tracing her tattoo with my lips, listening intently to every moan that she lets out."
    "I match her rocking hips, stride for stride, making sure she knows how much I want her in that moment."
    "Her hands wander down my back, occasionally latching in when I place a small bite."
    "Eventually, they make their way down to my waistband, and she gazes up at me, making perfect eye contact as she begins to unbutton them."






































    "Quick in my move against her, I match her, pace for pace, my hands moving to her own waistband to undo it."
    "Kleio doesn’t even hesitate; she tears off my jeans like a hungry animal, placing kisses on whatever piece of bare skin she can find."
    "I return the favor, tearing off her shirt and undoing her bra, quickly leaning down to kiss her breasts as she helps me kick the last of my jeans off."
    "Her skin is hot against mine as I slowly lower her to a nearby table, my body rocking against hers as I feel her moan."
    "She gasps for air, but I keep kissing her, unable to draw myself away from the beautiful curves of her body."
    "Eventually, she pulls me away, bringing my face back up to meet hers."
    "We crash together, looking like a show of modern art as we hastily try and get as much of each other as we can."
    "Gasping and out of breath, she pulls away, just for a moment, and looks me deep into my eyes. I know what she wants, but I want to hear her say it."
    hero.say "What do you want, Kleio?"
    "She leans up, wrapping her legs around my waist and pulling my hips as close to my body as she can."
    kleio.say "Shut up and fuck me!."
    if hero.has_condom():
        menu:
            "Use a condom":
                $ CONDOM = True
                $ hero.use_condom()
            "Do it raw":
                $ CONDOM = False
    else:
        $ CONDOM = False
    hide kleio
    show kleio rough
    "I need no further instruction; I thrust forward, filling her quickly, making her gasp in pleasure."
    "For a moment, I remain, overwhelmed by the feeling, before I slowly begin to rock my hips back and forth, building up a rhythm."
    "She gasps and moans every time I thrust forward, my hips roughly hitting her ass."
    "Her hands wrap around her own ass, spreading it open to help me get deeper."
    "I press on, so deeply ingrained in the pleasure of her body that I am barely able to focus on anything else."
    "Eventually, though, I notice her getting restless beneath me."
    "Her body is alight and so is mine, desperate to get more of her, to get as much of her as I can, to take her as fast and as hard as I can."
    "I want Kleio, more than anything, and I am doing all I can to have her."
    show kleio rough ahegao
    "Her moans begin to get sharper and louder, her breathing irregular, and I know she is getting close."
    "I keep with my rhythm, desperate to get both her and myself there."
    "She is moaning and crying out, nearly screaming in pleasure, and I find my own moans mixing in with hers, mumbled echoes of her name intermixed with cries of extreme pleasure."
    "Her body was fire, and she had set me alight."
    "Pressure builds up in me, and I begin to fuck her as hard as I could, my body a gun with the trigger nearly pulled."
    "Almost as though we had planned it, she shot her head back, trembling and moaning, the pulsation from her orgasm setting off my own."
    if persistent.xray:
        show kleio rough xray
    else:
        show kleio rough cum
    if not kleio.get_flag_value("pill") and not kleio.get_flag_value("pregnant") and not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills):
        $ kleio.set_flag("pregnant",1)
    "I cum quickly, moaning her name loudly as I feel the pressure that had built up finally release in a moment of pure pleasure."
    "For a moment, it was simply sweet, sweet ecstasy, before I carefully slipped out of her, falling back onto the floor, her quickly following suit beside me."
    hide kleio
    show kleio naked
    "We both are quiet, simply taking a second to catch our breaths before leaning into one another."
    "I wrap my arms around her warm body, pulling her close to me as she hides a slight grin."
    "I make no effort to contain my own: I’m grinning as wide as I can."
    "Finally, she breaks the silence, sitting up, ear cocked to the sky."
    kleio.say "You know, I think the rain stopped."
    "Then, with an unmistakable grin, she tumbles back into my arms, and I couldn’t help but laugh."
    hero.say "You know what, Kleio, you’re absolutely right."
    "She smiles at me, before glancing up from in between my arms."
    kleio.say "Do you want to stay here?"
    hero.say "Actually, why don’t we go back to my place?"
    "Winking, I gently pushing her off and helping her gather her clothes."
    hero.say "I’m sure we can have some more, uh, fun there?"
    "She enthusiastically agrees, and we both quickly change, leaving the dark studio behind as we race out into the dark night, two lovers that are, for a moment, simply alight with one another."
    "I pull her as close as I can to me, savoring for a moment her fluttering heartbeat."
    hero.say "Kleio, I don’t think I ever want to leave."
    hide kleio
    scene bg black with fade
    $ renpy.pause(0.1)
    $ game.pass_time(6, True)
    return


label kleio_fuck_date:
    $ kleio.set_flag("sex",1,"permanent","+")
    scene bg bedroom1
    python:
        o = game.girl_clothes 
        if not o:
            o = ""
    show kleio
    "It's all that I can do to pretty much shove Kleio into my room and close the door."
    "A moment later and I swear she'd have made me do here, right there and then in the hallway."
    "Even now, I'm still caught a little unawares by the contrast between Kleio's crass attitude in public and her almost crazy passion in private."
    "Once we're in my room, it's her pushing me - backwards to the bed as I struggle to strip off my clothes and meet her kisses at the same time."
    "Kleio finally shoves me back and I fall onto the bed, stripped to the waist and with my pants halfway down my thighs."
    kleio.say "That's mine!"
    "She points at my already rising cock as she pulls off her own jacket and t-shirt, then unhooks her bra."
    "It takes her no time at all to yank off the rest of her clothes, and then she parts my legs and kneels on the floor in front of me."
    "Kleio wraps her arms around my waist and slides my cock between her petite breasts."
    "At the same time she gently kisses my stomach and eyes me in a provocative manner."
    kleio.say "Imagine we're still out, and I'm under the table...doing this."
    hide kleio
    show expression "kleio bj "+o
    "With that, she slides down and releases my cock from between her breasts."
    show expression "kleio bj suck "+o
    "It traces its way up her neck, and then over her chin, and she doesn't even hesitate to allow it into her open mouth."
    "As if the feeling of Kleio, lips, tongue, piercings and all, going to work on me wasn't enough, now I can't help imagining her doing the same in public."
    "She takes me in deep all of a sudden, almost swallowing the entire length whilst cupping my balls and squeezing them tightly."
    "I feel myself stiffen, and realise that she's in real danger of making me cum within mere moments."
    menu:
        "Cum on her face":
            "Sensing what's about to happen, Kleio releases me and gasps for breath."
            show expression "kleio bj cumshot "+o
            "But it's too late, and with her face mere inches from the tip of my cock, she takes it all a second later."
            "Her face is glistening with the slowly dripping semen, but she doesn't seem in the slightest bit upset."
            show expression "kleio bj facial "+o
            kleio.say "I told you it was mine...all of it."
            "Almost to emphasize the point, she licks her lips and grins wickedly."
            $ FACIAL = " facial"
            $ kleio.love += 1
            hide expression "kleio bj facial "+o
            scene bg bedroom1
            if not hero.fitness >= 50:
                return
        "Cum in her mouth":
            "I cup my hands behind Kleio's head, holding her down as I cum."
            show expression "kleio bj suck cumshot "+o
            "She struggles a little at first, more thanks to surprise than objection."
            "But then she resigns herself to it and rides out the thrusts of the climax, her submission making it all the more gratifying to feel."
            hero.say "It's yours, Kleio...but I get a say in how you take it from me."
            "Kleio's breathless expression slowly turns into one of knowing amusement, betraying the enjoyment she derives from the occasional act of domination."
            $ FACIAL = ""
            $ kleio.sub += 1
            hide expression "kleio bj suck cumshot "+o
            scene bg bedroom1
            if not hero.fitness >= 50:
                return
        "Stop before cumming":
            hero.say "Oh fuck...Kleio, no more...I want to blow it inside of you!"
            "Not exactly the most poetic of lines, I know - but then Kleio's not the most conventional of girls."
            "Kleio releases my cock with a gentleness that belies her usually forceful demeanour."
            hide expression "kleio bj suck "+o
            scene bg bedroom1
            show kleio
            kleio.say "Whatever you say, [hero.name]...but now you better do something to REALLY impress me!"
            $ FACIAL = ""
    show kleio naked
    "As if to press her claim on me further, Kleio begins to climb upwards, forcing me to scramble further onto the bed."
    "She's already hot and slippery from the effort put into the blowjob, making the entire act all the more sensual and arousing for me."
    "As her groin gets closer to mine, I swear that I can already feel the warmth between her legs, even before she's close to my cock."
    $ CONDOM = ""
    if kleio.get_flag_value("pregnant") < 9:
        if kleio.get_flag_value("drinks")<3:
            if kleio.love < 180 and hero.has_condom():
                kleio.say "Put something on that thing, before it goes anywhere near the business entrance!"
                "I'm too caught up in the moment to object, scambling for a condom from the bedside table."
                "Kleio watches approvingly as I put it on, making the act feel like part of a little show for her benefit."
                $ hero.use_condom()
                $ CONDOM = " condom"
            elif kleio.love < 180:
                kleio.say "Better put a rubber on it, man - otherwise it's game over!"
                "I fumble for a condom from the bedside table, but there's none to be found."
                hero.say "Shit...I ran out!"
                "Kleio gives me a rueful smile as she shakes her head and shrugs whilst climbing off of the bed."
                kleio.say "Sorry, lover boy - looks like that's all you're getting from me tonight!"
                hide kleio
                return
            else:
                kleio.say "Quit stalling - if I'll put it in my mouth, then I'll let you put it inside of me like that too!"
                "Spurred on by her eagerness, I waste no time in pulling Kleio closer to me."
        if not CONDOM and hero.has_condom():
            menu:
                "Use a condom":
                    "I pause for a moment to grab a condom from the bedside table."
                    "Kleio makes a pouting noise at the interruption, but then begins to purr in approval at the sight of me slipping it on."
                    $ hero.use_condom()
                    $ CONDOM = " condom"
                "Do it raw":
                    "Kleio's so close to me now that I can't think of anything but having her without delay."
                    "It seems the feeling's mutual, as she eagerly wraps herself around me in anticipation of what will come next."
        else:
            "Kleio's so close to me now that I can't think of anything but having her without delay."
            "It seems the feeling's mutual, as she eagerly wraps herself around me in anticipation of what will come next."
    else:
        kleio.say "Quit stalling - there is no risk, I can't be double knocked up!"
        "Spurred on by her eagerness, I waste no time in pulling Kleio closer to me."
    "Kleio laughs in a wonderfully filthy manner as I try to manouver her into the position that I have in mind."
    "She makes a show of resisting a little, pretending to snap and bite at me, but soon submits herself to being bent in the way I want."
    menu:
        "Missionary":
            hide kleio
            $ POS = "rough bedroom "
            show expression "kleio rough bedroom out"
            "I push Kleio down onto her back, using all of my weight to pin her to the bed."
            "The force makes her legs ride up in the air, and she quickly wraps them around my back."
            menu:
                "Fuck her pussy":
                    $ HOLE = ""
                    show expression "kleio rough bedroom"+CONDOM
                    "I'm inside of her before she can fully make sense of what's happening."
                    "I deliberatley keep myself from kissing her for the sake of hearing the way that she cries and moans."
                    kleio.say "Oh, shit...[hero.name]...you're turning me into human origami!"
                    kleio.say "You can snap anything you want...just don't fucking stop!"
                    "Her hands are clasped behind her ass, and I'm almost rolling her onto her shoulders when I feel my climax coming over me."
                    "Unable to stop myself, I bite down my lips, thinking that I can taste the copper tang of blood as I cum."
                "Fuck her ass" if kleio.sub > 50:
                    $ HOLE = " anal"
                    show expression "kleio rough bedroom anal"+CONDOM
                    "I'm guessing that Kleio's expecting me to slip into her vagina, but my dick is already sinking into her ass."
                    "She cries out in shock as I push myself all the way in, her mouth forming an exaggerated 'O'."
                    hero.say "Hold that expression, Kleio...it makes you look like a sex-doll!"
                    kleio.say "You'd like that, huh - if I were a fuck toy you could toss around?"
                    hero.say "Only if you had a pull cord that'd make you talk filth when I pulled it."
                    "The combination of her acid tongue and amazing body make me redouble my efforts, and I soon can't hold myself back any longer."
                    $ kleio.sub += 1

        "Doggy" if kleio.sub >= 25:
            $ POS = "doggy "
            show expression "kleio doggy out"+FACIAL
            $ kleio.sub += 1
            "I turn Kleio so that she's on all fours, then give her ass a sharp slap that sends her inching forwards in surprise."
            kleio.say "Hey, [hero.name]...have I been so bad that I need a spanking?"
            "The delight in her eyes tells me instantly that she's enjoying this, and that she wants some more."
            hero.say "No amount of spanking's ever going to fix you, Kleio...no amount of cock, either...but that's not gonna stop me from trying."
            menu:
                "Fuck her pussy":
                    $ HOLE = ""
                    show expression "kleio doggy"+CONDOM+FACIAL
                    "I mount her before she can say another word, enjoying the sensation of pushing into Kleio's tight lips and feeling her tremble in reply."
                    "My chest is pressing down on her back, my face in her sweat-soaked hair, and I can feel her breasts as I reach for them."
                    "We're like animals fucking in an alleyway, nothing but the moment and our coupling seems to matter."
                    "A moment later I feel Kleio toss her head back as she senses that I'm about to cum."
                "Fuck her ass" if kleio.sub > 50:
                    $ HOLE = " anal"
                    show expression "kleio doggy anal"+CONDOM+FACIAL
                    "Without a word, I give in to a wicked impulse and part Kleio's buttocks so that I can push myself into her exposed ass."
                    "She yelps in surprise, far more loudly than I had expected, but she can't hope to either shake me off or slip out from under me now."
                    "I don't waste time being gentle, and yet I can already feel Kleio suddering and continuing to yelp as I move inside of her."
                    hero.say "You deserve this, Kleio...you've been a real bad girl, and this is your punishment."
                    "I catch a glimpse of Kleio's face and see that her cheeks are red and burning, maybe from the effects of my scolding words."
                    "The combination of taking her up the ass and knowing that I've somehow humbled, even dominated a fiery spirit like hers pushes me quickly towards my climax."
                    $ kleio.sub += 1
    kleio.say "Don't hold back - take me with you!"
    scene bg bedroom1
    show expression "kleio "+POS+CONDOM+FACIAL
    menu:
        "Cum inside":
            "I can't tell if Kleio is clawing at the sheets in passion or else in an effort to free herself."
            "Either way it doesn't matter - my weight is too much for her to slip out from under, and there's no time left."
            show expression "kleio "+POS+HOLE+CONDOM+" ahegao"+FACIAL
            "The convulsions grip me and are instantly transferred into Kleio's body, making her buck in sympathy."
            "She cries out, almost like she's in pain, and I can feel her nails digging into my skin, drawing blood."
            "Kleio's cries fade along with my own motions as the climax passes and we sink into a tangled mess amongst the tossed sheets."
            hide expression "kleio "+POS+HOLE+CONDOM+" ahegao"+FACIAL
            if not kleio.get_flag_value("pill") and not kleio.get_flag_value("pregnant") and not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills) and not HOLE==" anal":
                $ kleio.set_flag("pregnant",1)
        "Cum outside" if not CONDOM:
            "Somehow the craziness and reckless streak that Kleio's capable of bringing out in me looses its hold as I peak."
            "It takes all the effort that I can summon, but somehow I manage to drag myself out of her a few short seconds before my climax takes over."
            show expression "kleio "+POS+" out cumshot"+FACIAL
            "I try to make up for it by pulling her close to me and beginning to stroke her roughly to orgasm with my fingers."
            "But instinct tells me that the sighs Kleio is now making are heavily tinged with disappointment, and when she cums it's an anticlimax for her."
            "I try to be positive, thinking that her not objecting means she understands the reason for my actions."
            "But I can't help sharing in her sense of disappointment a little as well."
            hide expression "kleio "+POS+" out cumshot"+FACIAL
    scene bg bedroom1
    show kleio naked
    "Neither of us speaks as we lie still and feel our bodies quickly cooling and becoming chilly where we were so recently burning with heat."
    "I can't help feeling reassured by the feeling of Kleio's back against my stomach and her buttocks nestled in my lap."
    "Part of me wonders if I'm actually getting to know and understand her with the time we're spending together."
    "While another wonders if all I'm doing is uncovering more mysteries in her complicated and yet compelling personality."
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
