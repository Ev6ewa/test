init python:
    Event(**{
        "name": "samantha_forgot_money",
        "label": ["samantha_forgot_money"],
        "duration": 0,
        "game_conditions":{"room":["pub"], "chances":5, "flag_female":0},
        "girls_conditions": {"samantha":{"present":True,'valid':True}},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name": "samantha_buy_dress",
        "label": ["samantha_buy_dress"],
        "duration": 0,
        "game_conditions":{"room":["clothesshop"], "chances":5, "flag_female":0},
        "girls_conditions": {"samantha":{"present":True,'valid':True}},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"samantha_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "samantha",
        "girls_conditions": {"samantha":{"contact":"samantha","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(10,20),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"samantha_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "samantha",
        "priority":100,
        "girls_conditions": {"samantha":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"samantha_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "samantha",
        "priority":100,
        "girls_conditions": {"samantha":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"samantha_are_you_sick",
        "label": ["samantha_are_you_sick"],
        "duration": 0,
        "girl": "samantha",
        "priority":100,
        "girls_conditions": {"samantha":{"valid":True,"present":True,"not_activity":"sleep",'valid':True}},
        "game_conditions": {"flag_sick":True,"chances":"love_samantha_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"samantha_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "samantha",
        "priority":100,
        "girls_conditions": {"samantha":{"valid":True,"min_love":160, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"samantha_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "samantha",
        "girls_conditions": {"samantha":{"validappointment":True,"present":True,'valid':True,"not_activity":"sleep"}},
        "game_conditions": {"flag_dateinprogress":False,"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name": "samantha_kiss_me",
        "label": ["samantha_kiss_me"],
        "duration": 0,
        "max_girls": 1,
        "girls_conditions": {"samantha":{"min_love":150,"present":True,'valid':True}},
        "game_conditions":{"flag_female":0, "chances":20},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "samantha_event_02",
        "priority": 500,
        "label": ["samantha_event_02"],
        "duration": 1,
        "game_conditions":{"room":["bakery"], "flag_female":0},
        "girls_conditions": {"samantha":{"min_love":40,"present":True, "flageq_story":1,'valid':True}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "samantha_event_03",
        "label": ["samantha_event_03"],
        "duration": 1,
        "game_conditions":{"room":["park"],"hours":(9,17), "flag_female":0},
        "priority": 500,
        "girls_conditions": {"samantha":{"min_love":60,"present":True, "flageq_story":2,'valid':True}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "samantha_event_04",
        "label": ["samantha_event_04"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["nightclub"], "flag_female":0},
        "girls_conditions": {"samantha":{"min_love":80,"present":False, "flageq_story":3,'valid':True}},
        "do_once":True,
        "quit": True
        })

    Activity(**{
        "name": "tellaboutryan",
        "display_name": "About Ryan",
        "label": ["samantha_event_05"],
        "duration": 0,
        "icon": "samantha",
        "game_conditions": {"activity":"interact", "flag_female":0},
        "girls_conditions": {
            "samantha":{
                "active":True,
                "flageq_story":4
                }
            },
        "do_once": True
        })

    Event(**{
        "name": "samantha_event_A01",
        "label": ["samantha_event_A01"],
        "duration": 1,
        "priority": 500,
        "max_girls":0,
        "game_conditions":{"room":["livingroom", "bedroom1", "bathroom", "secondfloor","kitchen","pool"],"hours":(22,4), "flag_female":0},
        "girls_conditions": {"samantha":{"present":False, "flageq_storyA":1}},
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name": "samantha_event_B01",
        "label": ["samantha_event_B01"],
        "duration": 6,
        "game_conditions":{"hours":(12,20),"days":"6","flag_dateinprogress":0, "flag_female":0},
        "girls_conditions": {"samantha":{"flageq_storyB":1}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "samantha_event_B02",
        "label": ["samantha_event_B02"],
        "duration": 2,
        "game_conditions":{"hours":(10,18),"flag_dateinprogress":0, "flag_female":0},
        "girls_conditions": {"samantha":{"min_love":120,"present":True, "flageq_storyB":2}},
        "do_once":True,
        "priority": 500,
        "quit": True
        })

    Event(**{
        "name": "samantha_event_B03",
        "label": ["samantha_event_B03"],
        "duration": 2,
        "max_girls":0,
        "game_conditions":{"hours":(20,24), "room":["livingroom","kitchen","bedroom1","bathroom","bedroom2","bedroom3","secondfloor"], "flag_female":0},
        "girls_conditions": {"samantha":{"min_love":140, "flageq_storyB":3}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name": "samantha_event_B04",
        "label": ["samantha_event_B04"],
        "duration": 1,
        "priority": 500,
        "max_girls":0,
        "game_conditions":{"hours":(16,24), "room":["livingroom","kitchen","bedroom1","bathroom","bedroom2","bedroom3","secondfloor"], "flag_female":0},
        "girls_conditions": {"samantha":{"flagmin_pregnant":5, "flageq_storyB":4}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "samantha_pregnant_flag",
        "label": ["samantha_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"samantha":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "samantha_event_A02",
        "label": ["samantha_event_A02"],
        "duration": 2,
        "game_conditions":{"room":["bakery"], "flag_female":0},
        "priority": 500,
        "girls_conditions": {"samantha":{"min_love":100,"present":True, "flageq_storyA":2}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "samantha_start",
        "label": ["samantha_start"],
        "duration": 0,
        "priority": 500,
        "game_conditions":{"flagmin_samanthastart":1},
        "do_once":True,
        "quit": False,
        })

    Event(**{
        "name":"samantha_meet_bree",
        "label":["samantha_meet_bree"],
        "girls_conditions" : {"samantha":{"present":True,"valid":True},"bree":{"present":True,"valid":True}},
        "game_conditions": {"room":["pub"], "days_played":20, "flag_female":0},
        "do_once": True
        })

    Event(**{
        "name":"samantha_meet_sasha",
        "label":["samantha_meet_sasha"],
        "girls_conditions" : {"samantha":{"present":True,"valid":True},"sasha":{"present":True,"valid":True}},
        "game_conditions": {"room":["pub"], "days_played":5, "flag_female":0},
        "do_once": True
        })

    Event(**{
        "name":"samantha_chat_bree",
        "label":["samantha_chat_bree"],
        "girls_conditions": {"samantha":{"present":True,"valid":True},"bree":{"present":True,"valid":True}},
        "game_conditions": {"chances":10,"flag_samanthaknowsbree":True, "room":["pub","nightclub"], "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"samantha_init",
        "label": ["samantha_init"],
        "girls_conditions": {"samantha":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "samantha_give_christmas",
        "label": ["samantha_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"samantha":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "samantha_give_birthday",
        "label": ["samantha_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"samantha":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "samantha_give_valentine",
        "label": ["samantha_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"samantha":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name":"samantha_event_C01",
        "label": ["samantha_event_C01"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"samantha":{"contact":"samantha","valid":True,"present":False,"not_activity":"sleep","min_love":160, "flageq_storyC":1}},
        "game_conditions": {"hours":(14,15),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": True,
        "quit": False
        })

    Event(**{
        "name": "samantha_event_C02",
        "label": ["samantha_event_C02"],
        "duration": 2,
        "game_conditions":{"room":["bakery"], "flag_female":0},
        "priority": 500,
        "girls_conditions": {"samantha":{"min_love":170,"present":True, "flageq_storyC":2}},
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name": "samantha_event_C03",
        "label": ["samantha_event_C03"],
        "duration": 2,
        "game_conditions":{"room":["livingroom"], "flag_female":0, "days":"5","hours":(20,22)},
        "priority": 500,
        "girls_conditions": {"samantha":{"min_love":180, "flageq_storyC":3}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name":"samantha_event_E01",
        "label": ["samantha_event_E01"],
        "duration": 1,
        "priority":100,
        "girls_conditions": {"samantha":{"contact":"samantha","valid":True,"present":False,"not_activity":"sleep","min_love":160, "flageq_storyE":1}},
        "game_conditions": {"hours":(14,15),"flag_dateinprogress":0,"chances":25, "flag_female":0},
        "do_once": True,
        "quit": False
        })

    Event(**{
        "name": "samantha_preg_talk",
        "label": ["samantha_preg_talk"],
        "duration": 1,
        "game_conditions":{"hours":(19,21),"room":["livingroom"], "flag_female":0},
        "priority": 500,
        "girls_conditions": {"samantha":{"present":True, "flageq_tellpregnant":1}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "samantha_babyshopping",
        "label": ["samantha_babyshopping"],
        "duration": 1,
        "game_conditions": {
            "room":["date_mall"],
            "flag_female":0
            },
        "girls_conditions": {"samantha":{"present":True,'valid':True, "flagmin_pregnant":10}},
        "do_once": True,
        })

    Event(**{
        "name": "samantha_ending",
        "priority": 500,
        "label": ["samantha_ending"],
        "duration": 0,
        "game_conditions":{"days":"56", "flag_female":0},
        "girls_conditions": {"samantha":{'valid':True, "flag_engagedmike":1}},
        "do_once":True,
        "quit": True
        })

label samantha_ending:
    $ game.hour = 16
    show bg church
    "I suppose most people have spent a lot of time imagining the day they'd get married, planning everything down to the most minute detail."
    "But I've never been one of them, and for most of my life I hadn't really given serious thought to the idea of whether I would ever tie the knot."
    "And now that I am, and the big day is finally here, it all seems pretty surreal, like something that's happening to another person while I'm just looking on."
    "I suppose I was never even sure that Sam would say yes, let alone that we'd make it this far."
    "We made sure to do things differently from the abortive plans she'd previously made with Ryan, choosing a traditional service at a small chapel."
    "The guest list was short, mainly consisting of close family and friends for Sam's side."
    "I have almost no family, and those I do have don't keep in contact, so for me it was an even smaller number of friends in attendance."
    "Though neither of us came out and said as much, I think we were both relieved to be making this a quiet affair, with only the eyes that we chose looking on."
    "My distinct lack of reliable and likeable male friends meant that there was no best man or groomsmen involved."
    "And so on the day, I find myself standing alone at the altar, with only the priest performing the ceremony."
    "But rather than being intimidated as I look back down the length of the chapel, I find that I only feel a sense of anticipation."
    "I guess that it's because I never conjured up images of this day in my mind that I kind of don't know exactly what to expect."
    "In turn, this means that I'm not at all nervous about the many small things that you normally hear of people fretting over at this point."
    "I'm actually just waiting, anticipating the moment when the music that I barely remember choosing will start to play."
    "But I'm really waiting to see Sam come walking in through the doors at the other end of the chapel."
    "When the music starts up for real, I almost fail to register the fact."
    "And it's only when the doors do open, allowing the intense light of day to flood in, that I shake myself back into the moment."
    "At first it's quite impossible to even make Sam out as she walks slowly into the chapel and up the aisle."
    "All I can see is her silhouette, until my eyes adjust themselves and she finally comes into focus."
    show samantha wedding blush
    if not samantha.get_flag_value("pregnant") >= 9:
        "Get ready for some serious cliches from here on in, because I'm too caught up in the moment to be all laid back and original right now."
        "Sam's always been one of the most beautiful girls I can ever remember meeting."
        "Able to turn me on with as little as a smile and drive me crazy with anything much more than that."
        "But today she seems to have become all of that and more in my eyes."
        "Right now it feels as if all of the qualities that made me fall for her are at the surface and on show for everyone to see."
        "Her dress is actually quite a simple affair of white, all the better to show off Sam's natural beauty."
        "She's clutching a bouquet of white flowers, the same as the kind that decorate the chapel."
        "Before I know it, she's walked the short distance up the aisle and is standing before me."
    else:
        "Sam looks simply radiant as she walks up the aisle towards me."
        "In fact, I don't think that I can ever recall thinking her more beautiful than she looks here today."
        "Perhaps the now rather pronounced curve of her belly means that her white dress could not have been more complicated in terms of its cut."
        "But to me, it just adds to the perfection of the moment."
        "We talked a great deal about the fact that she was pregnant before the wedding."
        "And neither of us felt that it was a thing that we should either be ashamed of or try to hide."
        "The child growing inside of her is there because of the love we feel for each other."
        "Probably a more honest declaration of our love so than any wedding ceremony could be."
        "Sam reaches me at the altar while I'm still enjoying the sight of her approach, shaking her head with a smile."
    priest_say "Ahem...shall we begin?"
    "From there I try to concentrate on the moment, really I do."
    "But the words of the ceremony are nothing more than a blur, and it's a wonder I even remember to speak at my various cues."
    "There's the usual pause for dramatic effect as we get to that certain point in the proceedings..."
    priest_say "If anyone present can show just cause as to why this couple may not be lawfully joined together in matrimony, let them speak now or forever hold their peace."
    "There follows a pregnant silence, and I wonder if this is the moment when Ryan will come barging through the doors."
    "Or even worse, one of the girls from my own past exploits!"
    "But after a few seconds, it becomes apparent that we're not about to be treated to a cinematic interloper, and the ceremony proceeds without any further interruptions."
    "All too soon we're approaching the final stages of the ceremony, reciting vows and exchanging rings."
    "Each of these is a simple affair, as Sam and I agreed beforehand that we find significance in each other, and not in repeated words or objects."
    priest_say "It gives me great pleasure to pronounce you man and wife."
    priest_say "You may kiss the bride."
    "I don't need to be told twice."
    "Embracing Sam, I bend her over as far as possible and kiss her deeply."
    "As real as this all feels, there's still that little part of me that almost refuses to believe it."
    "Holy shit - not only did I get the girl in the end, but she followed me up the aisle and became my wife as well!"
    scene bg beach
    if samantha.get_flag_value("pregnant"):
        show samantha ending a
    with fade
    samantha.say "They say that life is the things that happen while you're busy making plans, and I think my own path to getting here proves that's often the case."
    samantha.say "I'd always imagined the way my life would turn out, as far back as I can remember, planning things and dreaming up images of just what it would all look like."
    samantha.say "But then I found that when you have a fixed notion in your head of how things are supposed to turn out for you, sometimes it blinds you to what should have been obvious."
    samantha.say "Take my choice in men - I'd been convinced that, when the right guy came along, I'd know it somehow and be able to make things work with him because it was meant to be."
    samantha.say "So when I moved into the house with [hero.name] and Ryan, the former was friendly and a little quiet, whereas the latter couldn't wait to charm me with his personality and big plans for his life."
    samantha.say "Guess which one of them I fell for and which one of them I probably should have taken a second look at?"
    samantha.say "You'd be right if you assumed that they weren't one and the same person!"
    samantha.say "[hero.name] soon became just a good friend, while Ryan pursued me and won me over."
    samantha.say "And when he asked me to marry him, I thought it was proof that I'd made the right decision."
    samantha.say "Turns out that I was wrong...sort of."
    samantha.say "Ryan was definitely one to pursue a woman, but not the kind to keep it to a single conquest at a time."
    samantha.say "The fact that it was [hero.name] who proved it to me might be cause enough for some people to be suspicious of his motives."
    samantha.say "And I wasn't without my own reservations at the time, it's fair to say."
    samantha.say "But he was very honest with me, didn't deny for a second that he had always possessed feelings for me."
    samantha.say "And after that he left the whole thing in my own hands, not trying to push himself on me for a moment."
    samantha.say "That was when I started to wonder if I hadn't been wrong on all those occasions when I went looking for the things that I thought I wanted."
    samantha.say "I began to think about what might happen if I decided to accept life as it happened and see what it would bring."
    samantha.say "I'm happy to say that it brought [hero.name] to me, and all of the happiness we've had since."
    samantha.say "When, out of the blue, he asked me to marry him, it seemed to be another instance of life taking that unexpected path."
    samantha.say "And so I said yes."
    samantha.say "It hasn't been that long since we tied the knot, and we're still learning to live together as man and wife."
    samantha.say "But a lot has changed in that short space of time."
    samantha.say "[hero.name] moved out of the house that we used to share, and we both finally exorcised the bad memories it held for us."
    samantha.say "We moved to a smaller, but more remote little place up on the coast, within sight of the windswept beach."
    samantha.say "The nature of his job meant that he could work from home."
    samantha.say "And I finally put pen to paper, at least in a metaphorical sense, and wrote down the first of what became many stories in a career as a children's writer."
    samantha.say "I'm not likely to become the next JK Rowling any time soon, but I have a keen agent and a willing publisher, so things are looking good."
    samantha.say "That's what I was doing, just before I began typing this little reflection - working on a story."
    if not samantha.get_flag_value("pregnant"):
        samantha.say "But now I can hear [hero.name] calling me from just outside."
        samantha.say "He's wanting to go on one of the long walks we've taken to having down the beach together."
        samantha.say "Every day we simply head out and walk in the direction that our whim takes us."
        samantha.say "We talk, swap ideas and always keep an eye out for any interesting driftwood or other detritus washed up overnight."
        samantha.say "[hero.name] keeps talking about starting to make sculptures out of what we collect, even selling it at the flea market in the nearest little town."
        samantha.say "He bristles when I tell him to grow a beard and start drinking local IPAs, to become a true hipster."
        samantha.say "But the truth is that I think this new life is changing us both for the better."
        samantha.say "Or maybe just washing over us, like the tide on the driftwood, rubbing away until we're worn down to who we were always supposed to be."
    else:
        samantha.say "But now I can hear [hero.name] calling me from the living room."
        samantha.say "I can hear the small, sweet cries of Isaac too, sounds that are already starting to resemble words."
        samantha.say "Our is starting to toddle now, but he still won't take a single faltering step without his mother being present to watch and clap his efforts."
        samantha.say "I know that sometimes [hero.name] finds the life we're living out here quiet and sedate in comparison to the city."
        samantha.say "But I think that he's becoming satisfied with things in a whole different way to what would have made him happy in the past."
        samantha.say "It's funny how seeming to have less and so often make you want less too."
        samantha.say "I suppose it's just a case of learning what truly has value in life."
    samantha.say "I'm pretty sure that this isn't the end of our story, not by a long measure."
    samantha.say "But perhaps it might the point where our story changes subtly."
    samantha.say "Changes in a way that means it's more interesting to us than to anyone that might happen to be in on it too."
    $ renpy.full_restart()

label samantha_babyshopping:
    show samantha happy
    samantha.say "I’m growing really excited."
    "A grin is plastered on her face, not an uncommon, or unwelcome, sight, and it makes me smile at her in response."
    hero.say "It won’t be long now, we haven’t much time to wait."
    samantha.say "They’ve been kicking a lot lately, I think they’re getting as restless as us."
    hero.say "We might even get an early arrival in that case."
    samantha.say "Oh, I hope so."
    samantha.say "Not early enough for it to be unhealthy of course, but I just can’t wait much longer!"
    "I laugh, snaking an arm around Samantha’s shoulder and pulling her closer."
    hero.say "They’re going to be quite the looker with us as the parents."
    "This time it was Samantha’s time to laugh, blushing as she placed a light kiss on my cheek."
    samantha.say "I hope they’re just like you."
    hero.say "And I hope they’re just like you, so fingers crossed they get the best of both worlds."
    samantha.say "I’ve been making a list of things we need,"
    "Samantha began as she pulled a sheet of paper from her pocket."
    "My jaw drops as I catch sight of what’s written on it. It wasn’t one piece of paper, it was four, each with both sides filled to the brim with things to buy."
    "Suddenly my wallet feels very empty, but I gulp, and nod as Samantha continues."
    show samantha normal
    samantha.say "So I think we should get..."
    "Though I can see the list myself, Samantha reading it aloud makes it seem that much longer."
    samantha.say "And then we can finish with just a few sets of bibs! Got it?"
    hero.say "Yeah I uh… I got it."
    "She grins at me as I nod along, my hands feeling awfully sweaty."
    "Thankfully, Samantha doesn’t mind that as she leans in, taking my hands in hers and stepping close."
    "I find myself lost in her eyes for a few moments."
    samantha.say "I love you, [hero.name]."
    "I wink at her, leaning in and embracing her."
    hero.say "I love you too."
    "Seeing her so overjoyed, that cute little smile, the way her entire face lights up with glee, makes everything worth it."
    "It’s priceless."
    hero.say "Come on then, lots to do."
    "I pull away quickly, keeping her hand in mine and motioning for her to lead."
    "I wouldn’t know where to start, despite planning the trip, and it’s clear she’s come more than prepared."
    "She’s even picked out specific products ahead of time, a level of forethought I’d never have achieved."
    hero.say "You really know what you’re doing, huh?"
    samantha.say "Well, it’s kinda embarassing."
    samantha.say "I didn’t think you’d want to spend all day browsing different onesies, so I came down yesterday to pick some things out."
    "I’m almost stunned for a moment."
    hero.say "You made this trip twice just to make it easier on me?"
    samantha.say "I knew you’d be stressed out with the baby so close, and it was making me restless, so yep."
    "She looks a little sheepish, but I’m too busy appreciating her to calm her down immediately."
    hero.say "I can’t believe you sometimes."
    hero.say "You’re so thoughtful, it’s impressive."
    show samantha happy
    samantha.say "Hehe, I just want to do everything I can to make this easier on you."
    hero.say "That’s my job, I should be doing that for you."
    samantha.say "You already do so much, I just had to return the favour."
    "I scoff, and are about to retort when she suddenly yelps."
    samantha.say "Ah! They’re kicking."
    show samantha babyshopping
    "I practically drop my bags where I stand, freeing up my hands for Samantha to guide to her stomach."
    "Her skin is warm, and, sure enough, I soon feel something bump my hand."
    "I’m surprised at just how violent it is, and it must have shown since Samantha quickly began laughing."
    hero.say "Wow, they’re going to be a real fighter, huh?"
    samantha.say "It definitely feels like it, a little minx too, she keeps waking me up with this."
    "I wave a finger disapprovingly at Samantha’s stomach, shaking my head and putting on my best stern voice."
    hero.say "Now now, Mommy needs her rest, stop waking her up."
    "Samantha laughs at my expression."
    samantha.say "You already look like a dad, now you just need some bad jokes and you’re golden."
    hero.say "Bad jokes?"
    hero.say "How do you make holy water?"
    samantha.say "I don’t know, how?"
    hero.say "You boil the hell out of it."
    "Samantha visibly cringes, though laughs anyway, whether or not it’s simply out of pity I can’t tell."
    samantha.say "Hehe, you really are ready to be a dad."
    hero.say "If that’s all it takes, I’ll be the best dad ever."
    samantha.say "I’m sure you will be anyway, [hero.name]."
    "Another kick interrupts my train of thought, Samantha yelping quietly at what I can only assume was a particularly strong one."
    samantha.say "Maybe they’ll be an athlete."
    hero.say "They’ve certainly got the strength for it."
    hero.say "What do you think, do you want to be an athlete?"
    "I ask the mound on Samantha’s stomach, then leant in, placing my cheek lightly against it."
    "I can’t make out Samantha’s face, but she has to be blushing, I can tell from the way even her stomach grew slightly warmer."
    hero.say "Interesting..."
    "I muse, smirking to myself."
    hero.say "They say they want to be a scientist, Samantha."
    samantha.say "Hehe, you’re lucky, she never talks to me."
    hero.say "Why don’t you talk to Mommy?"
    "I ask, pressing myself a little further into her stomach, not hard enough to harm the baby of course, but enough to freshly embarrass Samantha."
    hero.say "Ah, they say it’s because I’m the cooler parent. Sorry Samantha, straight out of the baby’s mouth."
    samantha.say "Oh, is that right? I’ll remember that the next time they’re craving a chocolate muffin."
    hero.say "Hear that? No more chocolate muffins for you."
    "I start to laugh, but am cut off by a foot to my cheek."
    "Startled, I quickly pull back, though quickly break into laughter alongside Samantha."
    samantha.say "I don’t think she liked that."
    hero.say "Well, I wouldn’t be happy if someone threatened to take MY muffins away."
    hide samantha
    show samantha
    "I stand and quickly embrace Samantha, squeezing her tightly."
    samantha.say "They’re going to be amazing."
    hero.say "Just like their mother."
    samantha.say "Just like their dad."
    "I shut her up with a kiss, otherwise we’d be here arguing over who’s best for the rest of the day."
    "Samantha seems embarrassed the entire situation happened in public, but thankfully we’re soon off again before someone walks down the aisle we’d been standing in."
    "By the time the day’s over, I’ve got enough bags that I struggle to carry them all, and despite it being only a short walk I have to get a cab home."
    "It’s better to have bought everything now than later though, and seeing how happy Samantha was as she picked out cute clothes was worth it alone."
    return

label samantha_give:
    if not "charm book" in hero.inventory.keys() and randint(1,2) == 1:
        $ gift = Consumable("charm book", money_cost = 100, effects = [("charm",2),("time",4)], limit = "week")
        "She hands me a book."
        hero.say "'How to talk to girls and have fun at patries'?"
        samantha.say "To help you get a girlfriend."
        hero.say "Thank you..."
    elif not "funny shirt" in hero.inventory.keys():
        $ gift = Equip("funny shirt", money_cost = 100, effects = {"geek":20,"playful":20,"charm":5})
        "She hands me a 'greatest gay best friend' shirt."
        hero.say "..."
        samantha.say "Come on [hero.name] it's funny!."
        hero.say "Maybe..."
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "She hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label samantha_give_valentine:
    show samantha
    "Samantha walks hesitantly towards me."
    call samantha_greet from _call_samantha_greet_7
    show samantha blush
    samantha.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Samantha throws a box of chocolates towards me."
    hero.say "Thank you, Samantha."
    $ hero.gain_item(gift)
    hide samantha
    return

label samantha_give_birthday:
    show samantha
    "Samantha walks towards me."
    call samantha_greet from _call_samantha_greet_8
    show samantha happy
    samantha.say "Happy birthday [hero.name]!"
    call samantha_give from _call_samantha_give
    return

label samantha_give_christmas:
    show samantha
    "Samantha walks towards me."
    call samantha_greet from _call_samantha_greet_9
    show samantha happy
    samantha.say "Merry christmas [hero.name]."
    call samantha_give from _call_samantha_give_1
    return

label samantha_init:
    if "samantha" not in HIDDEN:
        $ HIDDEN.append("samantha")
    $ samantha.set_flag("nodate")
    $ samantha.set_flag("nokiss")
    return

label samantha_meet_sasha:
    $ game.set_flag("sashaknowssamantha")
    show samantha at left
    show sasha at right
    sasha.say "Hi, I am Sasha."
    samantha.say "I am Samantha, nice to meet you."
    sasha.say "The ex crush?"
    if sasha.love() > 100:
        sasha.say "You must cry at night, like a lot."
        samantha.say "why?"
        sasha.say "Well you missed on the stallion there."
        hero.say "..."
        if samantha.get_flag_value("storyA"):
            samantha.say "It's never too late."
            sasha.say "Had a chance, blew it, move along."
            $ sasha.love += 2
            $ samantha.love += 2
        elif samantha.love() > 40:
            samantha.say "It was a close call with Ryan, I drew lots."
            $ sasha.love += 2
            $ sasha.love += 1
        elif samantha.get_flag_value("story") > 4:
            samantha.say "He is a true friend, that's for sure."
    else:
        samantha.say "That's for him to say"
        samantha.say "I've got to go."
        sasha.say "Bye."
    return

label samantha_chat_bree:
    show samantha at left
    show bree at right
    "Samantha and Bree are talking near the bar."
    if samantha.get_flag_value("engaged") and not samantha.get_flag_value("engaged2"):
        $ samantha.set_flag("engaged2",True)
        show bree happy
        bree.say "I am so happy for you !!"
        show samantha happy
        samantha.say "Thank you, I am so happy for myself too."
        bree.say "I wish I had someone too."
        samantha.say "[hero.name] don't interest you ?"
        if bree.love() > 80:
            bree.say "Yes but I am not sure he sees me like this."
        elif bree.love() > 100:
            bree.say "Yes but just for a good fuck, he is so hot."
            $ samantha_love += 1
            if samantha.love >= 100:
                samantha.say "I wouldn't mind fucking him too..."
                $ bree_love += 1
                samantha.say "But I am not sure sucking my groom's best friend's dick would be proper."
                bree.say "Lol."
        else:
            bree.say "I won't be satisfied with your leftovers!"
    elif 2 < samantha.get_flag_value("story") < 5:
        show samantha sad
        samantha.say "Ryan has been going to that strip club a lot recently."
        bree.say "Why, I don't think that those girls have anything on you."
        samantha.say "He think I don't know but I do, I just play along."
        bree.say "I am not sure that this is a healthy way of doing things."
        samantha.say "He just need to keep thinking of himself as some kind of apex predator..."
        bree.say "What a douche."
        samantha.say "But a cute one."
        bree.say "True..."
    elif samantha.get_flag_value("storyA") > 1 and randint(1,2) == 1:
        samantha.say "I just fucked [hero.name] the other day..."
        bree.say "What ? You are kidding right ?"
        samantha.say "I was a little drunk."
        $ bree.love += 1
        $ samantha.love += 1
    elif samantha.get_flag_value("storyA"):
        bree.say "I can't believe Ryan cheated on you..."
        samantha.say "Yeah, me neither, I am still in shock."
        bree.say "You are like the perfect woman."
        bree.say "Beautiful, funny, and you love to suck dicks."
        samantha.say "I sure do..."
        samantha.say "Thank you [hero.name]"
    elif samantha.get_flag_value("storyB"):
        bree.say "Show me the ring again."
        "Samantha shows her hand to Bree."
        bree.say "It's so beautifull !!!."
    else:
        "They just chat about girly stuff."
    return

label samantha_meet_bree:
    $ game.set_flag("samanthaknowsbree")
    show samantha at left
    "Samantha looks toward Bree."
    samantha.say "I bet that this is one of your new roommates?"
    hero.say "Yep, want to meet her ?"
    samantha.say "Why not, could be fun..."
    show bree at right
    hero.say "Hey, Bree this is Samantha My ex roommate."
    samantha.say "Nice to meet you."
    bree.say "Nice to meet you too."
    if bree.love() > 100:
        bree.say "So, you are the poor girl that let this fine young man go away ?"
        samantha.say "That's one way of saying it."
        bree.say "Let me thank you in behalf of the other women."
        if samantha.love() > 100:
            samantha.say "Don't get cocky, I might just take him back."
            $ samantha.love += 2
            $ bree.love += 2
        else:
            samantha.say "You are welcome."
            $ samantha.love += 1
            $ bree.love += 1
    else:
        bree.say "I am so glad you put that ad, that house is awesome."
        samantha.say "You are welcome."
    return

label samantha_start:
    $ samantha_love_max = 40
    $ samantha.set_flag("story",1)
    $ if "samantha" in HIDDEN: HIDDEN.remove("samantha")
    return

label samantha_move_in:
    menu:
        "Light Boxes" if LB:
            "I pick up as many of the smaller boxes as I can and head inside."
            "I hadn’t actually seen her new apartment yet, so when I walked in I could help but feel the homey atmosphere."
            "Despite some of the furniture still packed in boxes, it felt cramped, but in a cozy way."
            "I knew Sam would definitely love it here."
            "I carefully placed the boxes next to a sofa as Samantha passed by me to get more things."
            $ LB = False
        "Heavy Boxes" if HB:
            if hero.fitness >= 20:
                "I lift the boxes with ease and head into the apartment. I set them down next to the door and stand up to stretch my back."
                samantha.say "Oh, wow! Thanks for getting those. You’re pretty strong!"
                $ samantha.love += 2
            else:
                "I don’t know if I can lift these. I should probably wait for Samantha so we can both take it in."
                menu:
                    "Wait":
                        show samantha casual normal
                        "Samantha finally comes back outside and smirks at me."
                        samantha.say "Need some help?"
                        "I grumble a vague response, but we both grab side of the box and lift together. In no time, we have it sitting in the middle of the main bedroom."
                        samantha.say "Good work, team!"
                    "Take in the Boxes":
                        "I find a grip under the boxes and lift with everything I have. It comes with me, but the second I try to take a step, it all comes crumbling down."
                        "The boxes fall from my arms and I wince as I hear something break. That definitely wasn't good."
                        "Before I could check for damage, Samantha must have heard, as she came sprinting outside."
                        show samantha casual sad
                        samantha.say "Oh no!"
                        hero.say "I’m so sorry!"
                        "Samantha shook her head in dismissal and pulled The cardboard open."
                        "Inside was a variety of jewelry boxes, makeup palettes, and other things I couldn’t quite name."
                        "What stood out the most, though, was a large, engraved mirror."
                        "Cracks webbed the glass and broken shards were strewn across the bottom of the box."
                        "I cringed as I watched her face fall at the sight."
                        hero.say "I’m really sorry about that. I’ll pay for a new one!"
                        "After I said that, I hoped it wouldn't be too much. With my luck, it would be some sort of rare heirloom that she cherished every morning."
                        samantha.say "No, no, it’s okay. Besides, I should be more concerned for you!"
                        samantha.say "You have seven years of bad luck now!"
                        "She smiled up at me trying to brush it off but I could see the tightness in her lips."
                        "I started helping her take the rest in, deciding to let it go like she wanted."
                        $ samantha.love -= 1
            $ HB = False
        "Take in the Desk" if DESK:
            show samantha casual normal
            "As turn to pick up the desk, I find Samantha suddenly next to me."
            samantha.say "I’ll help you take this one in."
            samantha.say "Ryan says it’s a family gift- I don’t want it getting ruined."
            hero.say "Are you saying you don’t trust me?"
            samantha.say "You know I wouldn’t! I’m saying we should be extra careful."
            hero.say "Alright, alright."
            "We both take the desk in slowly and set in down inside. Samantha sighs in relief."
            $ DESK = False
    return

label samantha_event_02:
    $ samantha_love_max = 60
    $ samantha.set_flag("story",2)
    $ samantha.set_flag("engaged",True)
    "Coming through the glass doors of the bakery, I could already see how crowded it was."
    "This place was a local hangout next to the coffee shop and always had a lively atmosphere- it was a good change of pace."
    "I stood in line behind a few other people and squinted at the chalkboard menu."
    "Even though I’d been here a million times, I still scan the familiar menu everytime I come in- and promptly order the same thing I always do."
    "Eventually it was my turn to order."
    show samantha casual normal
    samantha.say "Hello! What can I get for ya- [hero.name]!"
    show samantha casual happy
    hero.say "Hey. I didn’t know you were working today."
    show samantha casual normal
    samantha.say "Yup! I’m covering for my friend’s shift."
    samantha.say "She called in this morning sick; The poor girl sounded terrible."
    hero.say "Sounds pretty bad."
    samantha.say "Oh, I’m sure she’ll be fine. Besides, I like working here."
    samantha.say "Anyhow, what would you like? Same thing?"
    hero.say "No! I’ll take..."
    menu:
        "The usual.":
            hero.say "A chilled espresso- but with an extra sugar this time."
            "Samantha covers her mouth and giggles at me."
            "That’s what you call different? Alright! Coming right up."
        "Something new.":
            hero.say "Um... green tea and... a blueberry muffin."
            "Samantha grins and claps her hands happily."
            samantha.say "Feeling adventurous are we? Right away!"
            $ samantha.love += 1
    hide samantha
    $ renpy.pause(1)
    show samantha casual normal
    samantha.say "Here you go!"
    "Samantha hands me a crisp brown bag with the inky, black bakery logo painted on the front. I hand her a few dollars and coins to pay."
    hero.say "Thanks, Sam! I’ll see you later-"
    samantha.say "Wait! I have my break in a few minutes."
    samantha.say "We can sit down and talk a little!"
    menu:
        "No thanks.":
            hero.say "Sorry, but I can only stay for a little while."
            show samantha casual sad
            samantha.say "Aw, that’s too bad."
            samantha.say "It was good seeing you, then!"
            $ samantha.love -= 1
            hide samantha
            return
        "Sure!":
            samantha.say "Yaay! Pick a seat for us and I’ll be over before you know it."
            "I nod my head and turn to find a seat, choosing one next to the window."
            scene bg bakery
    show samantha casual normal
    "Samantha hops out from behind the counter with a large brown bag and a steaming cup in the other. She pulls out the chair on the other side of the table and sits down."
    samantha.say "So~"
    hero.say "... So what?"
    samantha.say "Tell me all about your roommates!"
    samantha.say "You didn’t say too much last time, so how’s it going?"
    hero.say "They’re... interesting?"
    samantha.say "Don’t give me that! Tell me the what you think of them!"
    hero.say "They’re..."
    menu:
        "Entertaining.":
            hero.say "They’re not bad or anything. Bree’s a complete nerd and plays video games all the time."
            samantha.say "You say that like you don’t do the same thing."
            hero.say "I don’t as much anymore!"
            samantha.say "What about the other one? Sasha, right?"
            hero.say "Yeah. I don’t think she likes me that much."
            samantha.say "Aw, don’t say that!"
            samantha.say "I’m sure she’ll warm up to you."
            $ samantha.love += 1
        "Just roommates.":
            hero.say "That’s all they are. As long as they pay their share, I don’t really care what they do."
            samantha.say "You should at least get to know them a little bit!"
            samantha.say "Who knows, maybe you’ll like them more than you think."
            "Samantha winks at me and I roll my eyes. All she does is lightly laugh at my response."
        "Pretty attractive.":
            samantha.say "Ooh~ so you are interested in something."
            hero.say "Don’t say it like that! But yeah, Bree and Sasha are more than good looking."
            samantha.say "Don’t be afraid to ask a girl to hook you up~ I can be an A+ wingwoman when I want to be."
            $ samantha.love += 1
    "We both sip our drinks in a comfortable silence. She pulls out a bagel and cookies out from her bag and happily chomps on her sweets."
    "We talk for a while longer before another employee calls out to Samantha and tells her to get back to service."
    samantha.say "Aw, I have to go. Wait-!"
    "Samantha jumps forward and grabs onto my hands."
    samantha.say "Do you want to help me move the rest of my stuff in tonight?"
    samantha.say "Ryan’s working tonight so he won’t be home until I’m asleep."
    samantha.say "It would be great to surprise him with a finished home!"
    hero.say "I don’t know, Sam..."
    samantha.say "I’ll buy you some more coffee- and how about a slice of our cake?"
    menu:
        "I’ve got other plans.":
            hero.say "Sorry, but I need to get a few things done today. And I have work tomorrow so I can’t stay out too late."
            show samantha casual sad
            samantha.say "Aw, that’s too bad."
            samantha.say "Okay, I understand. Thanks for sitting with me though!"
            samantha.say "It was fun talking."
            "Samantha stands up and waves at me, returning back to her spot at the counter. I get up and head back outside."
            $ samantha.love -= 1
            hide samantha
            return
        "Alright. I’ll come over later today.":
            show samantha casual happy
            samantha.say "Yaay! Thank you so much! I’ll see you after work."
            python:
                t = 21 - game.hour
                game.pass_time(t)
    scene bg black
    with dissolve
    $ renpy.pause(1)
    pause 1.0
    scene bg street
    with dissolve
    show samantha casual normal
    "She is standing out in the middle of the street next to a pile of boxes and a small, dark mahogany desk."
    hero.say "What’s with all the stuff out here?"
    samantha.say "The moving truck just dumped the rest outside and I haven’t seen the since. Can you believe that?"
    "I rose an eyebrow in suspicion but accepted the explanation. There was probably more to it- I’ll just assume Ryan pissed them off. "
    hero.say "That sucks! We should move this stuff in before it gets too late then."
    samantha.say "Great! Grab whatever you want, all I need is for it to be inside."
    "Samantha grabs a stack of medium sized boxes and made her way inside."
    samantha.say "The doors open! So don’t worry about that."
    "I stared at the pile of boxes, wondering where to start."
    "Some of the boxes seemed pretty heavy, and I didn’t want to risk breaking anything if I dropped it."
    "Not to mention, that would be humiliating in front of Samantha. Where should I start?"
    hide samantha
    $ LB = True
    $ HB = True
    $ DESK = True
    python:
        while DESK or HB or LB:
            renpy.call_in_new_context("samantha_move_in")
    show samantha casual happy
    samantha.say "Whoo!"
    samantha.say "Thanks for the taking that stuff in. You were a big help!"
    hero.say "Yeah, no problem. Happy to get this out of your way- but don’t think that means I’ll forget about that free coffee."
    show samantha casual normal
    samantha.say "I’m a woman of my word."
    "We stare at each other for a moment and I could see a distressed look rise up in her eyes."
    hero.say "Something wrong."
    "A minute passes as she tries to bring the words out, but instead she grabs onto my hands."
    samantha.say "You have to promise not to tell anyone."
    hero.say "..."
    hero.say "Of course."
    samantha.say "Well..."
    "Samantha lifts her hand and shows me her fingers."
    "It’s only then that I notice the shiny, gold ring gracing her fourth digit."
    "Looking back up at her face, I see cheerful tears in her eyes."
    show samantha casual blush
    samantha.say "Ryan proposed!"
    hero.say "..."
    "I didn’t know what to say. My heart sank at the news. Was Ryan officially taking Sam away from me?"
    samantha.say "He told me to keep it a secret for now, but I can’t hold it in any longer!"
    menu:
        "Be supportive":
            hero.say "... That’s great, Sam! I know you’ll be happy together."
            show samantha casual happy
            samantha.say "Thank you! I’m so lucky to have him."
            hero.say "I better be invited to the wedding."
            samantha.say "Haha, absolutely. You’ll be first on the list!"
            play sound "sd/cell_vibrate.mp3"
            "My phone vibrates in my pocket and I check the time- it was getting pretty late. I wondered what was holding up Ryan for so long?"
            samantha.say "I’ve kept you for too long, haven’t I? I’m sorry! You should get home soon."
            hero.say "You’re right. I have work tomorrow, so I’ll head out."
            "We both head to the door and Samantha sees me out, but not before pulling me into a tight hug."
            samantha.say "Thank you so much, [hero.name]!"
            $ samantha.love += 2
        "Be disproving":
            hero.say "I don’t know... don’t you think you’re too young to be jumping into that? And you just moved in together. What if you don’t like it?"
            show samantha casual angry
            samantha.say "What do you mean? We love each other. That’s all that matters, right?"
            hero.say "I don’t think you guys are thinking straight."
            "Samantha had a pained expression of betrayal. She’d trusted me with something she’d been holding back and here I was spitting all over her dream."
            samantha.say "I’ve always wanted to be with him like this. I’m happy, he’s happy and that’s all I need. Maybe you should leave. Thanks for all the help today."
            "Without another word, she walks me to the door and before I can say goodbye, it’s already shut tight behind me."
            $ samantha.love -= 2
    hide samantha
    return

label samantha_wedding_flag:
    if samantha.get_flag_value("story") < 4:
        $ samantha.set_flag("nocheat",True)
    if samantha.get_flag_value("story") < 5:
        $ samantha.set_flag("story",5)
        $ samantha.set_flag("storyB",1)
    return

label samantha_pregnant_flag:
    $ samantha.set_flag("pregnant",1,mod="+")
    return

label samantha_event_03:
    $ samantha_love_max = 80
    $ samantha.set_flag("story",3)
    $ samantha.set_flag("weddingtime",True,7,hook="samantha_wedding_flag")
    "As I walk into the park and look around, there are groups of people hanging out."
    show samantha normal
    "Suddenly, I spot Samantha sitting alone at a table under a tree."
    "She’s hunched over a book with papers scattered all over the surface."
    "I come up next to her, but she doesn’t seem to noticed, heavily entranced over the work in front of her."
    "Peering over her shoulder, I can see scribbles of pencil and markings."
    "She still hadn’t noticed me yet."
    menu:
        "Hey, Samantha.":
            show samantha happy
            "Samantha raises her head and looks back at me, smiling warmly."
            samantha.say "Hi, [hero.name]! Fancy seeing you here."
        "Scare":
            "I quickly bring my hands down on her shoulders and I can feel her jump in surprise."
            "The pencil in her hand jerked and made a long mark over a line of writing."
            samantha.say "Eep!"
            "I chuckle lightly at her reaction."
            "My grin fell a little when I saw that she looked upset."
            samantha.say "[hero.name]?! That’s not funny!"
            "She leans back and attempts to swat me away, but I move out of her reach."
            hero.say "Sorry, sorry!"
            $ samantha.love -= 1
            "I sit down across from her sheepishly."
    hero.say "What are you working on?"
    show samantha normal
    samantha.say "Just some homework."
    "Her face was tense with frustration."
    "She didn’t seem to be having an easy time."
    menu:
        "You look like you’re having trouble.":
            samantha.say "No, I’m...!"
            "She struggled to say something but eventually deflated."
            "She didn’t seem very happy with my observation."
            samantha.say "I guess... if you know anything about the subject, do you think you could help me out?"
            $ samantha.love -= 1
        "Sounds difficult. Need any help?":
            "Sam purses her lips but end it turns warm and relaxed."
            samantha.say "You know what... yeah. I could use some pointers. Thanks!"
            $ samantha.love += 1
        "Homework doesn’t sound fun. Good luck with that!":
            samantha.say "Yeah... thanks. I’ll see you later then."
            $ samantha.love -= 1
            hide samantha
            return
    "Sam hands me the paper she’d been writing on. Staring down at the sheet, it was covered in notes and numbering problems."
    if hero.knowledge >= 25:
        "It looked like statistics. I remembered it was one of the core classes she was taking, so she must not have liked it as much since it was required."
        hero.say "Stats, right? I remember taking that class. I didn’t like it too much. But, I guess I didn’t like a lot of my classes now that I think about it."
        samantha.say "Yeah! I don’t like it too much either."
        hero.say "Alright... let’s start here."
        "I take Samantha’s pencil and lightly tap it to one of the numbers on the paper in front of me. Sam leans forward over the table to see."
        "Her blonde hair curtains over her face and she has her arms crossed under her breasts."
        hero.say "Uhm..."
        "I try not to let my eyes wander down and redirect my focus."
        hero.say "Well, your first mistake is here..."
        scene bg park
        show samantha normal
        hero.say "Get it?"
        "Samantha’s eyes had been trained on me the entire time. It was nice to have her unbreakable attention, even if it was usually reserved for Ryan."
        samantha.say "I think so."
        "I hand her the pencil and she gently takes it from me as if I’d somehow blessed it."
        hero.say "Try it out on the next problem."
        "She nods and a look of determination crosses over her face. She begins slowly writing out her answer. When she’s finished, she turns the paper back over to me."
        "Looking it over, I can tell that it’s wrong."
        menu:
            "Were you listening to me at all?":
                $ samantha.love -= 1
                $ samantha.sub += 5
                show samantha sad
                samantha.say "I was! I’m sorry. I just don’t understand it, I guess."
                hero.say "Try to pay attention this time."
                "I re-explain what I can, faster this time. She seems to become more confused, so I slow down."
                hero.say "Understand?"
                "She grabs her pencil and moves onto the next problem. She does better, but still makes a few mistakes."
                hero.say "No... try again."
                "Sam groans and runs a hand through her hair."
                samantha.say "I don’t think I can do this!"
                "She starts packing up her things and closes her books."
                hero.say "What? Can’t we try it one more time."
                samantha.say "No, it’s alright. I’ll stay after class and see if one of the teachers can explain it."
                hero.say "Stay after? Don’t you have work in the evening?"
                samantha.say "Yes, but I can’t afford to fail this course. I need my grades high to keep my parents happy, you know?"
                hero.say "Oh, alright. Sorry I couldn’t help you then."
                samantha.say "It’s okay! I appreciate the thought."
            "Good try, but you should do it like this.":
                "I correct her answer easily and explain each step."
                samantha.say "Oh...! I got it. Thanks!"
                hero.say "Do the next one."
                samantha.say "Okay..."
                samantha.say "..."
                samantha.say "Like this?"
                "I look over her work."
                hero.say "Yeah, that’s great! Nice."
                "She happily claps her hands and her face is practically glowing."
                samantha.say "Yayy! I think I can do it now. Thank you so much!"
                hero.say "No problem."
                samantha.say "Seriously~ You should be a teacher or something."
                hero.say "Haha... I don’t think it suits me much."
        hero.say "... Wasn’t Ryan supposed to be studying with you?"
        samantha.say "Oh. He’s been pretty busy lately. He hasn’t been coming home at night and I’m worried that he might be overworking himself. I didn’t want to bother him."
        hero.say "That sucks. You guys should be with each other more."
        menu:
            "You can always come to me if you need help.":
                show samantha happy
                "Samantha beams and I can see a blush rise on her cheeks."
                samantha.say "Thanks, [hero.name]. I really appreciate it."
                $ samantha.love += 2
            "Ask Ryan to help you next time.":
                samantha.say "You’re right. I’m sorry if I bothered you."
                menu:
                    "You didn’t bother me.":
                        hero.say "No, it was fun, really. I just think you should get with him more since you guys are getting married."
                        samantha.say "Yeah! That’s true. You always know what to say, huh?"
                        $ samantha.love += 1
                    "Stay silent.":
                        samantha.say "I’ll stay after class next time. Maybe a teacher will have time for me."
                        $ samantha.love -= 1
        show samantha normal
        samantha.say "Well, I should get going."
    else:
        "I didn’t really know what I was looking at. It had to be some sort of math, right? Numbers and symbols littered the page, not really connecting in my brain."
        hero.say "Uhm... math?"
        samantha.say "Yup! I know it’s not really your thing, so you don’t have to help me."
        "I would act offended at her words, but I knew there was nothing malicious behind her tone. Besides, she was right."
        "She was also giving me a way out of this."
        hero.say "No, I can still help you! It’ll just take me a bit longer. But two heads are better than one, right?"
        samantha.say "Alright, yeah! Let’s do this!"
        "I internally berate myself. I should have taken the easy way out- there was no way this could end well."
        samantha.say "Do you know how to do this part? I keep messing up."
        "She points down at a seemingly random space on the page. I stare past her finger, trying to think of an answer."
        menu:
            "Change the subject.":
                hero.say "Hmm, yeah... why’d you come all the way out here to work on this, anyway?"
                "Sam raises an eyebrow at me, but answers."
                samantha.say "Because I don’t like being cooped up in my house all day! I can’t just go between university, the bakery and home."
                samantha.say "I would go crazy! Ryan isn’t home that often at any rate."
                samantha.say "..."
                samantha.say "You have no idea, do you?"
                hero.say "What? I- uhm- ... no."
                "Surprisingly, Samantha giggles at me."
                samantha.say "Well, it’s sweet of you to have offered."
                samantha.say "I wonder if I could just ask one of my teachers. But they’re always busy."
                hero.say "What about Ryan?"
                samantha.say "He leaves in the morning for work and has been coming home late. I don’t want to stress him out."
                hero.say "C’mon, Sam. You’re the one person who couldn’t stress him out. You said he was going to study with you anyway."
                samantha.say "Alright, you have a point."
                samantha.say "I’ll ask him next time! Thanks, [hero.name]!"
            "Think of an answer.":
                hero.say "Hmm..."
                if hero.charm >= 25:
                    hero.say "Try using these and make them the dividend."
                    samantha.say "Will that work?"
                    hero.say "Probably."
                    show samantha happy
                    "Samantha giggles at my smooth answer, but does my suggestion anyway."
                    samantha.say "Nope! That doesn’t look right."
                    hero.say "Aw, well, that’s my contribution."
                    samantha.say "Quite the attempt!"
                    hero.say "What can I say? I’m good at what I do."
                    "Samantha and I laugh and she closes her book with a sigh."
                    samantha.say "What are you up to? I didn’t expect to see you today."
                    hero.say "Oh, just looking for someone to hang out with. Lucky I found you."
                    samantha.say "Aren’t you! Well, at least you can entertain me out of my homework, hm?"
                    hero.say "I wouldn’t put it like that. We should go hang out somewhere else if you don’t want to work."
                    samantha.say "Tempting! But I should get home soon."
                    $ samantha.love += 5
                else:
                    hero.say "Uhm... you could try those- numbers? Why are there letters?"
                    show samantha happy
                    "Samantha laughs and pushes a strand of hair behind her ear."
                    samantha.say "You’re good at a lot of things, [hero.name], but statistics is not one of them."
                    hero.say "Ah, I’m hurt!"
                    "She rolls her eyes playfully and closes her books and packs up. She seems to have accepted that she wouldn’t be getting it done today."
                    hero.say "But, seriously. Sorry I can’t help you."
                    samantha.say "Don’t worry about it. I should know how to do this ny now. But I can barely pay attention! I can’t stop thinking about Ryan."
                    samantha.say "He wants to get married soon and I’m excited to start planning."
                    hero.say "Soon?"
                    samantha.say "He wants everything set up in a few months."
                    hero.say "A few months?! That doesn’t make sense."
                    samantha.say "Of course it does! He loves me. I want to be his wife soon, too."
                    "I shake my head but don’t say anything this time. If they really did want to move fast then nothing I could say would stop them for a second."
                    samantha.say "Well, I should get going."
    show samantha normal
    hero.say "Alright. I’ll see you later?"
    samantha.say "Definitely! I need to go shopping, so we can meet up then. I need a few things for the new home."
    "Shopping with Samantha usually meant buying books or clothes. Not the most exciting thing to do, but I was okay with it as long as she didn’t take forever."
    hero.say "Sure... sounds good."
    "She must have noticed my lack of enthusiasm, putting her hands on her hips."
    samantha.say "I’m also going out to party. You know, drinking, dancing- how about that?"
    hero.say "I can definitely do that."
    samantha.say "That’s what I thought. But you should join me for a little shopping if you have the time. I’m not going to the usual place We’ll have fun!"
    "She winked at me and I simply blinked back in confusion."
    "I guess I would find out what that meant next time we met."
    samantha.say "I’ll see you then, [hero.name]!"
    "She gathered her things in her arms and headed for the entrance with a wave. I waved back, watching her go."
    "I slumped back to the table, a boredom coming over me. What would I do now?"
    return

label samantha_event_04:
    $ samantha.set_flag("story",4)
    $ samantha.set_flag("ryancheats",True)
    "The nightclub was more crowded than I had expected."
    "I think it opened about an hour ago, but here people were, rocking to the music with drinks in hand."
    "I inched around the dance floor to the open bar in the back."
    "Sitting down, I order a drink and wait to be served."
    "I absentmindedly browse my phone, scrolling through my contacts."
    "Maybe I should call Sam to hang out again."
    "That would certainly lighten things up."
    "But she was probably with Ryan."
    show ryan casual smile
    ryan_say "Hey. Can I get you something to drink?"
    "As if reading my mind, Ryan’s voice popped up nearby."
    "My head snapped up, seeing him on the other side of the long bar next to a busty girl with silky black hair."
    unknown_girl_say "Ryan! I didn’t think I’d see you today."
    "The girl stands up and throws her arms around Ryan."
    "I couldn’t help the suspicion that rose in me."
    "What was going on?"
    show ryan casual smile
    ryan_say "Of course, baby. I can’t just leave you here sober."
    "The girl giggled, a small hand coming to cover her mouth."
    "A blush covered her face as the bartender slid a bright colored drink over to them."
    "The girl took the drink in one hand and grabbed at his arms with the other, pressing it between her breasts."
    unknown_girl_say "What have you been up to all week? I haven’t seen you for a few nights."
    ryan_say "Oh, ya know. Working."
    unknown_girl_say "You work too much. Spend more time with me!"
    ryan_say "How am I supposed to spoil you then?"
    "The girl giggled again and pressed against him more."
    unknown_girl_say "How about I just wait at your house? It would save you the trip and we could have fun all night~"
    ryan_say "Nah- you wouldn’t like my shitty apartment. Besides, I have roommates, so I don’t want them to seduce you away from me."
    unknown_girl_say "Ryan! No one could take me away from you."
    "I stared with wide eyes at the scene before me."
    "There was no way this was actually happening."
    "Sure, Ryan was a douchebag, but he and Samantha were the happiest people I knew..."
    "but apparently not."
    "As the two talked more, I could feel anger replace the suspicion."
    "How can he do this to Sam?"
    "How can anyone do this to sweet girl like her?"
    "The bartender gave me my drink, but I held it with numb hands."
    "There is no way Samantha would believe me if I just told her about this."
    "I stared blankly at my phone and back up at Ryan."
    "Making an easy decision, I lifted my phone and opened the camera."
    "Ryan was so attentive to the girl leaning over him that he didn’t even notice."
    "I snap a few photos."
    "I couldn’t just send these to her without saying anything, could I?"
    "She would break down."
    "I had to be there for her."
    "I lifted the phone to my ear after dialing her number."
    "..."
    "Voicemail. Was her phone off?"
    "I’d have to find her later then."
    "I threw a few dollars onto the counter with a tip and slid out of my seat."
    hide ryan
    "I practically ran out of the club, feeling like Ryan might see me if I stayed any longer."
    "I had to find Sam."
    return

label samantha_event_05:
    $ samantha_love_max = 100
    $ samantha.set_flag("story",5)
    show samantha
    "Do I really want to do this?"
    "Her heart will be broken."
    "She loves Ryan with every part of her body."
    "I will only be hurting her."
    "I can’t stand to see her cry over everything."
    menu:
        "Show Her the Pictures":
            samantha.say "..."
            samantha.say "Is something wrong?"
            hero.say "Sam, I-"
            "How should I say it?"
            hero.say "I was at the nightclub the other day."
            samantha.say "Hmm~? Meet anyone nice?"
            hero.say "I saw Ryan..."
            hero.say "With another girl."
            samantha.say "... That’s not funny."
            hero.say "I’m serious."
            show samantha angry
            samantha.say "Bullshit!"
            samantha.say "Don’t say something like that!"
            "I pull out my phone and unlock it."
            "I tap open the photo album and hand it to her."
            "She stares down at the picture, expression still firm."
            "She blinks rapidly and finally frowns."
            show samantha sad
            samantha.say "This isn’t real."
            samantha.say "I...don’t understand."
            "She hands me back my phone...."
            "I don’t say anything until her eyes wet with tears."
            hero.say "Oh, Sam-"
            "She drops her head into her hands and sobs."
            "My heart stops."
            "What do I do?"
            "I decide to pull her into a side hug and she immediately leans into me."
            samantha.say "Tell me it isn’t real! Please!"
            "I don’t say anything and let her cry."
            samantha.say "I- I have to go."
            "She sniffs and roughly stands from where we sat."
            hero.say "Wait- Sam!"
            "I get up and breath a sigh."
            "If she wants to talk about it again, she will. I don't doubt that."
            $ samantha.set_flag("storyA",1)
            $ HIDDEN.append("samantha")
        "Let Her Be Happy":
            "There was no way I can do this to her."
            "It's better to let her think Ryan is faithful to her, isn't it?"
            "Gripping my phone tightly, I walk away without saying a word, letting her stay in her beautiful ignorance."
            $ samantha.set_flag("storyB",1)
    hide samantha
    return

label samantha_event_A01:
    $ samantha.set_flag("nokiss", False)
    play sound "sd/cell_vibrate.mp3"
    "I’m distracted for a moment- my phones is buzzing in my pocket."
    "The contact name is Samantha."
    hero.say "Hello? Sam?"
    samantha.say "He-ey there."
    "..."
    "That didn’t sound good."
    hero.say "Samantha? Are you okay?"
    samantha.say "Never been better. I want to see you."
    hero.say "What?"
    samantha.say "Come here!"
    hero.say "... Where are you?"
    samantha.say "I’m outside your house. I knocked but no one will open the door. Open up! Open-n up!"
    hero.say "... Okay. I’ll be right there."
    play sound "sd/dialtone.mp3"
    show samantha sad
    "I stare at her. Her cheeks are stained red and she smelled like..."
    hero.say "Are you drunk?"
    samantha.say "Ju-ust a little~ I’m a good girl though."
    "Before I know what’s happening, she leans heavily onto me, burying her face in my shirt."
    hero.say "Uh, Samantha?"
    samantha.say "You still love me don’t you?"
    samantha.say "Tell me you love me."
    menu:
        "I still love you.":
            "Samantha giggles, but it turns into a sob."
            samantha.say "I know you do, I know you do."
            $ samantha.love += 2
            $ samantha.set_flag("sex",1,"permanent","+")
            $ samantha.set_flag("storyA",2)
            $ HIDDEN.remove("samantha")
        "Say Nothing":
            "Samantha sobs into my shirt and I could feel the tears soaking through."
            samantha.say "You do! I know you do!"
            hero.say "Samantha, you know I'll always be your friend..."
            "I take her to the couch and we sit there until she cries herself to sleep."
            $ samantha.set_flag("storyA",2)
            $ HIDDEN.remove("samantha")
            return
    hero.say "Come on, Sam. Wait in my room and I’ll get you some water."
    "I take her lazy nod as a yes and lead her to my door."
    scene bg bedroom1
    show samantha sad
    "She sits on my bed with a hazy blank stare."
    hero.say "I’ll be right back."
    hide samantha
    scene bg kitchen
    "I grab a glass from the cabinet and fill it with water at the sink."
    "I didn’t really know how to deal with a drunk Samantha."
    "Especially a sad one."
    "I didn’t know what the hell to do."
    scene bg bedroom1
    hero.say "Here. I got you some-"
    show samantha underwear blush
    "I cut myself off and almost drop the water."
    "There was Samantha, laying on my bed with just her bra and tugging at her panties."
    samantha.say "You’re so sweet! Come here and let me thank you!"
    hero.say "You... you’re drunk. You’ll regret this later."
    "It was taking everything in me to hold myself back from jumping into bed with her."
    samantha.say "I need you! You want to make me feel better, don’t you?"
    "I hesitated. Samantha seemed to noticed, and pulled her panties down to her knees."
    "My legs carried me faster than my brain could think."
    "When I came to the edge of the bed, she spread her legs and wrapped them around my waist."
    samantha.say "Take all that stuff off, won’t you?"
    "I looked down and realized she was talking about my clothes."
    "I numbly unbuttoned my jeans and threw my shirt across my bedroom."
    "Apparently I was going too slow, because she tugged on me with her legs and I fell on top of her."
    "With my elbows either side of her head, I could feel her hot breath ghosting across my face."
    "The unique smell of alcohol tinged her scent."
    samantha.say "You’ll make me happy, won’t you?"
    samantha.say "Be rough, like my baby."
    samantha.say "Do what you want with me."
    "Her baby? Was she talking about Ryan?"
    menu:
        "Let her lead":
            "I didn’t reply, instead gently pressing my lips onto hers."
            "She froze at first, her eyes wide."
            "Eventually she melted into me."
            "I could feel her throw her arms around my neck and my chest swelled."
            "I finally had her and she was mine to love."
            hero.say "I’ll treat you right."
            "I pulled her up by her waist higher up on the bed."
            "She let me drag her with ease."
            "Only her breasts were covered by now, her panties thrown somewhere on the floor when she tugged me on top of her."
            "I gently reached behind her back and unhook her bra."
            "She pushes herself up a little to help."
            "Once it’s off, her large breasts spill out."
            "Her nipples were pierced with simple rings."
            samantha.say "I wore them just for you~"
            "I didn’t know if she was being sincere or was too drunk to think straight."
            "Nonetheless, I dipped my mouth down onto one of the rings and sucked smoothly."
            "A soft moan sounded above me. I took that as a good sign."
            "I took more of her breast into my mouth and sucked harder. Her back arched and I moved with her."
            "I made my hands busy by groping at her sides and hips, going lower and lower until I reached the heat of her vagina."
            "Sam gasps above me and opens her legs as far as she can when I test a finger at her opening. I stop for a moment, feeling metal. Ryan really did have her pierce everything."
            "I toy with it for a second before rubbing a knuckle against her clit."
            "It’s already slick and wet."
            samantha.say "[hero.name]!"
            samantha.say "Let me help you, too."
            "Before I can react, she flips me over and the next thing I know I’m on my back."
            "Her perfect hands snake down to my member and I hold back a moan when she expertly grasps it and squeezes gently."
            "Her arms move up and down."
            "One hand goes down and massages the base and I can’t keep the noises back this time."
            samantha.say "I’ll get ready for you."
            "It’s practically a whisper, like she talking to herself."
            "She takes her hands off me and shoves two fingers into herself, stretching her entrance easily."
            "I look of discomfort comes across her face for a moment, but it doesn’t stop her from inserting more digits."
            "My tongue darts out to wet my lips."
            "I could feel myself get harder at the sight."
            "There was something about her shiny, blonde hair draped over her shoulders and the blush that had spread from her face to her whole body that made her undeniably beautiful."
            "She was taking care of me more than I was taking care of her, wasn’t she?"
            "Well, whatever she wanted."
            if hero.has_condom():
                menu:
                    "Use a condom":
                        $ CONDOM = True
                        $ hero.use_condom()
                        "I put a condom on then push inside of her."
                    "Do it raw":
                        $ CONDOM = False
                        "I spit into my hand, try to cover my dick as much as I can and push inside of her."
            else:
                $ CONDOM = False
                "I spit into my hand, try to cover my dick as much as I can and push inside of her."
            hide samantha
            show samantha cowgirl both
            samantha.say "Ready, sweetie?"
            "I grab her hips and position her above my erection."
            "I slowly lower her on, and she groans as I fill her up."
            show samantha cowgirl fuck blush
            "I give her a moment to adjust, but she gets used to it quickly."
            show samantha cowgirl fx orgasm
            "I jerk my own hips slightly and she takes the hint. We both move back and forth together, slapping loudly as I move in and out."
            show samantha cowgirl fx orgasm2
            "The heat becomes overwhelming and she’s satisfyingly tight. Eventually, I feel the climax coming."
            if not CONDOM:
                "Before I can warn her and pull out, she leans down and licks at my lips."
                show samantha cowgirl orgasm2 cum
                "As I open my mouth to let her in, I flood inside of her and she loudly gasps."
            else:
                "She leans down and licks at my lips."
                show samantha cowgirl orgasm2 cum
                "As I open my mouth to let her in, I flood inside the condom and she loudly gasps."
            "We’re both breathing heavily."
            show samantha naked blush
            "Samantha lays on top of my chest and slowly raises herself off of me."
            "I see tears come to her eyes again and get worried."
            "My concern instantly disappears when she speaks."
            samantha.say "Thank you. Thank you for telling me about him."
            "I only pat her back in response."
            "We stay that way until her breath evens out and she’s lightly snoring on top of me."
            "Feeling content, I close my eyes with her."
        "Take her":
            "Well, with that kind of permission, there was no way I was backing down."
            "I knew what I wanted."
            "I gripped her hips tightly and crawled on top of her."
            "I shove my clothes off the side of the bed."
            show samantha miss dickout
            "She spreads her legs for me and I immediately dive in."
            "I reach into the drawer beside my bed and pull out a clean bottle of lotion."
            "I pour some into my palm and lather it onto my already hardening dick."
            "With the leftover lotion on my fingers, I prepare her sloppily, my eagerness taking a hold of me."
            show samantha miss pussy
            "Samantha gasps above me as I enter inside of her."
            "Her walls are hot and smooth."

            "I notice a shine just above and see a piercing gracing her red clit."


            "I thrust in easily."
            "Sam’s hands tangle in her hair as she screams in pleasure."
            samantha.say "Harder!"
            "I was shocked at her request at first, but move myself in and out of her quickly, smacking against her ass with each thrust."

            "Her nipples were hard and her piercings stood up straight."
            "I let my hands grab onto her pillow-like breasts, her boobs easily filling each hand and more."
            show samantha miss inside
            "After a while of us both panting and bobbing back and forth, I finally climax and spill inside of her."
            show samantha miss inside cumeyes
            samantha.say "[hero.name]!"
            "When I finish I pull out and collapse on top of her, resting my head on her chest."
            "When I look up at her, she’s staring up blankly at the ceiling, but with a hint of satisfaction in her eyes."
            "Slowly, she closes them, and I do the same."
            if not samantha.get_flag_value("pill") and not samantha.get_flag_value("pregnant") and (randint(1,3) == 1 or "hung" in hero.skills):
                $ samantha.set_flag("pregnant",1)
    hide samantha
    return

label samantha_event_A02:
    $ samantha.set_flag("storyA",3)
    if samantha_love_max < 150:
        $ samantha_love_max = 150
    $ samantha.set_flag("nodate",False)
    $ samantha.set_flag("nokiss",False)
    $ samantha.set_flag("engaged",False)
    show samantha happy
    samantha.say "[hero.name]!"
    "Sam comes towards me from the counter, hanging up her apron."
    "She has a purse slung over her shoulder and a paper bag with the bakery logo plastered on the front in the other."
    "I smile nervously."
    hero.say "Hey."
    show samantha normal
    samantha.say "Don’t look so nervous!"
    "I have some news."
    hero.say "News?"
    samantha.say "Yup! Walk with me?"
    "I nod and stand up."
    "Pushing my chair in and grabbing my cup, I follow her out the door."
    scene bg mall
    "She gripping tightly at the bakery bag and pursing her lips."
    "Was something wrong?"
    hero.say "What’s up?"
    samantha.say "..."
    samantha.say "I broke up with Ryan."
    "My brain short circuits for a moment."
    "The guy she’s been falling all over for the past who knows how many years is gone?"
    "Dropped?"
    samantha.say "Don’t look at me like that!"
    samantha.say "I thought a lot about what you said."
    "I asked Ryan about it when I got home."
    "He tried to deny it at first, but when I said you had pictures he... fell apart."
    "I don’t know what to say."
    hero.say "Are you okay?"
    samantha.say "I’m okay."
    samantha.say "Better than okay."
    samantha.say "I feel... angry- and upset."
    samantha.say "But I’m glad I found out."
    hero.say "You? Angry? How scary."
    "She smacks me on the shoulder but gives me a smile."
    "I can tell she’s still sad about the whole situation, but she’s taking it better than I thought."
    "You know, after the whole mental breakdown part."
    samantha.say "I think I’ve made a decision."
    hero.say "Oh?"
    samantha.say "I... I want to go on a date with you."
    "If I was short circuiting before, I was shutting down this time."
    "Was I hearing her right?"
    "There was no way."
    "She seemed to notice my speechlessness."
    samantha.say "You’ve always been there for me."
    samantha.say "You’re honest, you spend time with me..."
    samantha.say "I really like you, [hero.name]."
    hero.say "I- I don’t know what to say."
    samantha.say "Oh! I’m sorry. Did I read things wrong?"
    menu:
        "Yes, I'd love to go out with you":
            "I’d love to go out with you."
            $ samantha.love += 1
            hero.say "Sam... I’d love to go on a date with you."
            samantha.say "Really? Oh thank you!"
        "No, I don't see you that way":
            "I don’t know if I like you like that."
            $ samantha.love -= 5
            hero.say "...I’m not sure about us."
            samantha.say "Oh. I understand. I’m sorry."
            "What am I doing... I can't do that to her..."
            hero.say "But I am willing to give it a try."
            return
    hero.say "What about Ryan?"
    hero.say "He’s probably not going to accept it that easily."
    samantha.say "I don’t care."
    samantha.say "No means no."
    samantha.say "He hasn’t been home in a few days anyway."
    hero.say "..."
    hero.say "Maybe we can try. I’ll go on a date with you."
    samantha.say "Really? Alright! Thank you! You won’t regret it, I promise."
    "I knew I wouldn’t."
    "Samantha was too sweet to make anyone regret anything- except making Ryan regret ever losing her."
    hero.say "Are you sure you’re ready? That you’ve had enough time?"
    samantha.say "I think that the sooner I forget about Ryan, the better I’ll feel."
    hero.say "Fair enough."
    samantha.say "Yay~! Let’s go!"
    hero.say "What? Right now?"
    samantha.say "Yes, right now! I’m off work and you’re free, right?"
    hero.say "Yeah."
    samantha.say "So, let’s do it!"
    samantha.say "Who knows when the next time we’ll both be free like this?"
    samantha.say "We both have work and I have university."
    samantha.say "It’s a good time!"
    hero.say "Alright, then, let’s go. Have a place in mind?"
    samantha.say "Um... I’ll admit, I didn’t really think this through."
    samantha.say "I didn’t think I’d make it this far."
    "She didn’t think she’d make it this far? With me?"
    hero.say "That’s okay. We can think of somewhere to go."
    samantha.say "Like where?"
    menu:
        "Movie Theatre":
            hero.say "We could watch a movie?"
            samantha.say "Ooh! Good idea! What’s showing?"
            hero.say "I’m not too sure. Let’s go and find out."
            scene bg cinema
            "The theatre has a good crowd today."
            "A new movie must have come out that I didn’t hear about."
            samantha.say "I forgot! That new horror movie came out yesterday."
            hero.say "Want to see that? It has to be good with all these people around."
            samantha.say "Um... alright. We can see that one."
            "She looks a little pale, but I don’t really register it until we’re at the booth buying tickets."
            "We make out way to our seats and sit near the front."
            hero.say "Are you going to be okay? Should we see something else?"
            samantha.say "No! I’m okay. It’s just a movie."
            "I can tell she’s lying, but I can’t help but admit that her denial is kind of cute."
            "After a few minutes of waiting, the previews begin. Boring trailers flash past the screen, only a few catching my attention."
            "The lights dim and the conversation dies down."
            "A typical horror movie title plasters itself in front of us."
            samantha.say "This doesn’t sound too bad."
            "The movie has a slow start. A couple move into a house and slowly realize that it’s haunted. It’s nothing too exciting, but the first scare has Samantha jumping in her seat next to me."
            samantha.say "Oh my gosh!"
            "The film continues. Gore and blood flow not too soon after."
            "I look over; Samantha seems a little green in the face."
            "Her hands are gripping the arm rests."
            "I lay my hand on top of hers. She jolts in surprise for a moment but immediately relaxs, lacing her fingers with mine."
            "She takes to burying her face into my shoulder for the rest of the movie."
            "The credits roll."
            samantha.say "Is it over?"
            hero.say "Yeah. That scary?"
            samantha.say "... It wasn’t scary."
            hero.say "Whatever you say. Let’s head out."
            "Samantha nods and we stand up, filing out with the rest of the crowd. She hangs onto my arm until we get outside."
        "Shopping":
            samantha.say "Sure! I need to stop by the clothes store anyway, so good choice!"
            scene bg clothesshop
            "By the time we get to the clothes store, Samantha already has a few other bags in her hands from stopping by the bookstore."
            "When we walk in, it’s pretty empty, save for the clerk leaning boredly on the checkout counter."
            samantha.say "Hey!"
            hero.say "What?"
            samantha.say "You should choose something for me?"
            hero.say "Really? I don’t have much of a fashion sense."
            samantha.say "Have some faith! I want to see what you come up with."
            samantha.say "Don’t take too long!"
            "With that, she goes to her own aisle in the female section, grabbing a shopping cart on the way."
            "Where should I even start?"
            $ MODEST = False
            $ SEXY = False
            $ SWIM = False
            menu:
                "Modest top":
                    "There’s a red blouse hanging daintily on a featured shelf near the front."
                    "It’s frilly with lace on the shoulders."
                    "It looks like it would fit her well."
                    $ MODEST = True
                "Daring swimsuit":
                    "Making my way to the water area, swimsuits of all shapes and sizes cover the walls and racks."
                    "My eye catches a purple suit; very very daring, I don't know if any sane woman would wear it."
                    $ SWIM = True
                    "Maybe we could go swimming sometime."
                    "She probably already had something for it, but I couldn’t help but think it would look good on her even if she wouldn't even think of wearing it."
                "Sexy top":
                    "There’s a crop top with an open back, tying together at the bottom on one of the racks."
                    "Would Sam even wear something like that?"
                    "No point in not trying. Besides, if she didn’t like it, she could just tell me to put it back."
                    $ SEXY = True
            "I hold up my choice for Samantha to see once we meet up again."
            "Her cart is piled with jeans and shirts."
            samantha.say "Ooh~!"
            if MODEST:
                samantha.say "I can’t believe you said you don’t know fashion! This one is pretty!"
            elif SWIM:
                samantha.say "I almost forgot!"
                samantha.say "I needed a new swimsuit."
                if not samantha.love >= 75 or not samantha.sub >= 25 or not hero.charm >= 50:
                    samantha.say "But this one is a little bit too much."
                    samantha.say "Anyway..."
                else:
                    samantha.say "If you think I would look good in it I might wear it, but it's showing a lot of skin..."
                    $ samantha.set_flag("sexyswimsuit")
                samantha.say "We have to go swimming sometime."
                samantha.say "Thanks, [hero.name]!"
            elif SEXY:
                samantha.say "..."
                samantha.say "I like it. And I’m sure you do too."
                "I almost miss the wink she throws me and promptly choke on air."
            samantha.say "Alright, well I’m ready! Thank you so much for helping me out."
        "Restaurant" if game.hour >= 11 and game.hour <= 13:
            hero.say "There’s that restaurant down the street."
            samantha.say "As much as I love eating at the bakery, real food sounds like a good idea."
            hero.say "Heresy!"
            samantha.say "Shut up!"
            scene bg highclassrestaurant
            "We’re seated quickly at a nice table."
            "I’m glad we got here early; more people were already starting to file in."
            "We both order drinks and stare at the menu."
            hero.say "What are you getting?"
            samantha.say "Hmm."
            samantha.say "How about we order for each other! We can both try something new."
            hero.say "Oh. Sure."
            samantha.say "Yayy! Get something good!"
            "I look back down at the menu, but my mind suddenly goes blank. What would Sam want to eat?"
            menu:
                "Spaghetti":
                    "Seemed simple enough. Why not?"
                    "The waitress comes over and takes our order, a pad and pencil in hand. I order a plate of spaghetti for Samantha."
                    samantha.say "Can I get... the chicken casserole?"
                    "Interesting. I don’t think I’ve ever had that before. I shrug at her, but she smiles at me."
                "Hamburger":
                    "everyone loves hamburgers, right?"
                    "The waitress comes over and takes our order, a pad and pencil in hand. I get an order of french fries and a hamburger for Samantha."
                    samantha.say "Can I get... the chicken casserole?"
                    "Interesting. I don’t think I’ve ever had that before. I shrug at her, but she gives me a warm grin."
                    samantha.say "Thanks, [hero.name]! I love some good comfort food."
                "Salmon":
                    "I can’t remember if she likes seafood or not. I know this restaurant doesn’t make bad fish, so it wouldn’t hurt to try."
                    "The waitress comes over and takes our order, a pad and pencil in hand. I order a platter of salmon for Samantha."
                    samantha.say "Can I get... the chicken casserole?"
                    "Interesting. I don’t think I’ve ever had that before. I shrug at her. She gives me a half-hearted smile- oops. Does she not like fish?"
                    "Once our food comes out, we finish it quickly. My chicken casserole is good, but I don’t think I’d get it regularly. The waitress comes over with the check and I pull out my wallet. As I lay down the cash, Sam snatches the bill and pull it to her chest."
                    hero.say "Sam-"
                    samantha.say "Half and half! At least!"
                    "I sigh, but eventually give in when I realize that she wouldn’t be giving it back until I agreed. Her expression is content when the waitress picks it up and thanks us for coming."
    scene bg street
    "Samantha and I stand outside of her house."
    "There’s no car in the driveway, so I assume Ryan’s out doing... whatever he does with his time."
    "Walking her home was surprisingly comfortable despite the silence."
    "She insisted on holding my hand the whole way here."
    samantha.say "That was fun!"
    hero.say "Yeah, it was."
    samantha.say "We should do that more often."
    samantha.say "..."
    samantha.say "Thanks, [hero.name]."
    hero.say "Hm? For what?"
    samantha.say "For being here."
    "And coming out with me today."
    "I was nervous that you would say no."
    samantha.say "I... really like you, [hero.name]."
    "Suddenly, her eyelids are fluttering and she’s leaning in."
    "This was... strange."
    "But I liked it."
    "I didn’t know what I was waiting for."
    "My long time crush was finally accepting me."
    "I close the distance."
    "Her lips are as plump and soft as they look."
    "My hand rests on her hip and I feel her arms wrap around my neck."
    "It only lasts for a few seconds, but it’s enough for Sam’s face to go completely red."
    "I probably look the same."
    samantha.say "I’ll see you later, [hero.name]."
    "My head is fuzzy- christ, how old am I? I’m acting like a kid, dizzy from romance. I manage to raise my hand and wave."
    hero.say "See ya."
    "She giggles and gives me one more peck, this time on the cheek."
    "The next thing I know, I’m standing alone on her porch, staring at the closed door in front of me."
    hide samantha
    return

label samantha_event_B01:
    $ samantha.set_flag("storyB",2)
    $ samantha_love_max = 120
    "Time to go to Sam and Ryan's wedding."
    scene bg church
    "Church bells ring loudly, piercing my ears as if they personally wanted to shame me."
    "Samantha’s wedding day came quickly- much too quickly."
    if not samantha.get_flag_value("nocheat"):
        "I can’t stop thinking about Ryan."
        "He was a lying cheat, but I didn’t say anything."
        "But, this was for the best, right?"
        "Sam is happy and that’s all that matters to me."
    unknown_girl_say "Oh my gosh! [hero.name], is that really you?"
    show natalie teaser
    "I turn to see one of Samantha’s friends, dressed up in the requested colours."
    "She looked familiar, but I only could bring up vague memories."
    unknown_girl_say "I haven’t seen you since ages! How have you been?"
    hero.say "Uh... great."
    "I was great."
    "Fantastic."
    unknown_girl_say "Good!"
    unknown_girl_say "Can you believe those two are finally getting married?"
    unknown_girl_say "It seems like only yesterday that they were fawning over each other in first year."
    menu:
        "Support":
            hero.say "Yeah."
            hero.say "Sam looks really happy."
            hero.say "She’s been waiting for this for a long time."
            "She swoons at me, like I’m the one getting married."
            unknown_girl_say "They’re so sweet!"
        "Oppose":
            hero.say "Don’t you think they’re going a little fast?"
            hero.say "They’re way too young to be getting into something so serious."
            unknown_girl_say "What!?"
            unknown_girl_say "If anyone should get married on the spot, it’s them!"
            unknown_girl_say "Ryan is the perfect man for her- loving, sweet... he’ll give her everything she needs."
            "Ouch."
    unknown_girl_say "I saw Sam’s dress earlier."
    unknown_girl_say "She is a goddess!"
    unknown_girl_say "Ryan’s got it good."
    hero.say "Oh. Are you a bridesmaid?"
    unknown_girl_say "Yup!"
    unknown_girl_say "I couldn’t even think of turning her down when she asked me."
    "To be honest, I was kind of assuming she would ask me to have some sort of role, too. Ryan probably had something to do with it."
    hero.say "... Sounds nice."
    unknown_girl_say "I heard you three lived together for a while."
    "She leaned in like she was telling a secret."
    unknown_girl_say "It wasn’t too loud was it?"
    "Why the hell was everyone so straightforward with this kind of thing?"
    hero.say "Wha-?! No!"
    unknown_girl_say "They totally were!"
    "I groan, looking around for other people to talk to."
    "Everyone else is engaged in conversation, excited about the couple to be."
    "Guess this is what I’m stuck with."
    menu:
        "Ask about their friendship":
            "How long have you known Samantha?"
            unknown_girl_say "Hmm... since middle school, I think."
            unknown_girl_say "I met her in social studies."
            unknown_girl_say "I was out sick for a long time, and she helped me catch up- best friends ever since!"
            hero.say "Sounds like something she would do."
            hero.say "She’s a sweet girl."
            unknown_girl_say "Ha! In more ways than one."
            unknown_girl_say "That girl has a strong sweet tooth."
            hero.say "Yeah- she doesn’t work at the bakery for nothing."
            hero.say "Sometimes I think she’d even work there if they paid her in desserts."
            unknown_girl_say "Or just cinnamon rolls."
            unknown_girl_say "I remember she brought one for lunch everyday."
            unknown_girl_say "Then her mom wouldn’t let her anymore because she’d always come home with a sugar rush."
            unknown_girl_say "Sam was so cute!"
        "Ask about the decoration":
            hero.say "Did someone help her plan this whole thing?"
            if not samantha.get_flag_value("nocheat"):
                hero.say "Ryan couldn’t have been very helpful. He’s always- ... working."
                "I try not to choke on the last word."
            unknown_girl_say "I did!"
            unknown_girl_say "At least, I was one of them."
            unknown_girl_say "Samantha’s mom helped her through a lot of it."
            hero.say "That’s good."
            unknown_girl_say "Yeah! But I have to say, we didn’t do much."
            unknown_girl_say "We just opened up some doors that led her to the prize!"
            unknown_girl_say "I absolutely love the colours she chose."
            unknown_girl_say "And the absolutely fit her too."
            "I take a good look around- the church is decorated in white and royal gold colours."
            "It’s simple, but stands out."
            "The colours are classy, but the rest of the decorations that I managed to spot in the reception hall when I came in were pretty tame."
            hero.say "I think it matches her really well."
        "Ask about the food":
            hero.say "Do you know what food they'll be serving"
            unknown_girl_say "Of course, that girl chose the sweetest items on the menu."
            unknown_girl_say "Duck with chocolate sauce, mashed potatoes, and salad."
            unknown_girl_say "But, between you and me, I’m pretty sure Ryan talked her into that last one."
            hero.say "Chocolate sauce?"
            unknown_girl_say "Yep. Weird, but the fanciest sweet thing she could find."
            unknown_girl_say "And trust me, she looked over that menu for hours."
            unknown_girl_say "She really wants everything to be perfect."
    hero.say "Do you know what time everything starts?"
    "She looks down at the watch on her wrist and hums."
    unknown_girl_say "Should be starting really soon."
    unknown_girl_say "We’ll need to find our seats."
    "Not a moment after, a man wearing religious clothes gets our attention, telling us to get ready."
    hide natalie
    "I get to my seat easily."
    "Samantha’s friend- whatever her name was- rushes outside, hooking her arm around a groomsman who I can’t get a good look at before the doors close."
    "Ryan stands at the front, hands twitching nervously, but he has a wide grin on his face."
    "If I didn’t know better, I would call it a blatant smirk, but I push the thought as far back in my mind as I can."
    "It’s loud in the hall for a long moment, before it quiets down and piano music fills the space."
    "I hold my breath."
    "Why did I come here?"
    "There was no way I could watch this."
    "What was I thinking?"
    "Before I could get up and bolt, pairs start walking through elegantly to the front."
    "I can feel something building in my chest."
    "Guilt? Regret? I couldn’t tell."
    "The music sounds broken in my ears."
    "Was the pianist feeling okay?"
    "I quickly glance around."
    "No one else seems bothered."
    "Was I feeling okay?"
    "My heart jumps in my throat when the tune changes and the doors open wide."
    "The crowd turns back to see the bride: Samantha."
    show samantha wedding blush
    "I try not to look."
    "I fail."
    "I have to stop myself from gasping."
    "She’s wearing a gorgeous short white dress, very simple but incredibly classy."
    "My eyes follow her down the aisle."
    "She catches my eye."
    "She gives me a smile full of hope and innocence."
    "My lips struggle for a moment."
    menu:
        "Smile Back":
            "I force my mouth to twitch up in a smile, giving her a quick thumbs up."
            "Her eyes twinkle."
        "Look Away":
            "I quickly look away, focusing my attention on the bridesmaids."
            "I can barely look at her without feeling guilty."
            "The priest began speaking, filtering half heartedly through my ears."
            "It felt like I was watching this through someone else’s perspective."
            "..."
    "Vows are being said."
    "Samantha looks teary eyed."
    samantha.say "Ryan~"
    "She chokes and grabs at his hands, lacing their fingers together."
    samantha.say "I’ve felt connected to you ever since I saw you."
    samantha.say "When I met you in first year, I knew I wanted to be with you forever."
    samantha.say "You’ve treated me with more love and kindness than I deserve."
    samantha.say "I can only hope that I can repay you someday."
    "Oh, Samantha."
    "You deserve so much more than you think."
    "Before I knew it they’re kissing."
    "People are clapping and whistling in the seats next to me."
    "At least she was happy."
    hide samantha
    scene bg highclassrestaurant
    "I’m sit at one of the many circular tables in the hall, a ceramic plate in front of me with a slab of duck covered in a brown sauce- I suppose that’s the chocolate."
    "People are dancing at the middle of the floor."
    "The music keeps switching between upbeat pop and rock music."
    "A strange combination."
    "I couldn’t tell where Sam was at this point."
    "She had immediately gone to dance with Ryan once formalities were done with."
    "What should I do now..."
    $ BATHROOM = False
    menu:
        "Go for a walk" if "samantha_event_04" in DONE:
            "As much as I told myself that I was skulking around on the landing of the metal fire escape at the back of the wedding venue to get some fresh air, I knew I wasn't even fooling myself."
            "Even the excuse of needing to sneak a cigarette would have been enough to make me able to accept my own logic."
            "But as it was, all I could do was admit to myself that I really didn't want to be here in the first place."
            "And that I was trying to spend as little time around the other guests as I could possibly manage."
            "And who was I to Sam and Ryan anyway?"
            "Nothing but a former housemate that they'd probably invited as an afterthought."
            "The fact that I hated his guts and still kind of held a torch for her was my concern alone."
            "Even if the jerk had been cheating on her, right up to the so-called bug day - this was still the start of a new life for them."
            "The last thing they'd want was me hanging around, with the stench of the past all over me."
            "I was just trying to pull myself together and walk back into the building, when I heard the sound of the door behind me suddenly opening."
            show samantha wedding
            "I confess that I jumped a little, but then the figure that came rushing out onto the small landing wasn't in any greatly composed state either."
            hero.say "Sam...what in the hell are you doing out here?"
            "She looks edgy and more than a little dishevelled, streaks and smudges in her make-up give tell-tale hints that she's recently been crying."
            "But that's not as notable as the fact that she's already in her wedding dress, hair all done up for the ceremony."
            "At times like this, I always feel that I should be a million miles away from selfish thoughts of a carnal nature."
            "But god, Samantha looks beautiful in that dress."
            hero.say "Isn't the wedding about to start?"
            "I hate to say this one, but..."
            hero.say "Won't Ryan be worried where you are?"
            "Samantha looks at me for a moment, as though she doesn't quite recognise me or understand what I'm saying."
            "Then she shakes her head and seems to come back into the moment."
            samantha.say "Fuck the wedding...and fuck Ryan too!"
            "She realises the irony of her last statement, and begins to laugh almost crazily."
            show samantha wedding sad
            "But after only a couple of seconds, the laughs turn into sobs, and she throws her arms around my neck."
            "I reutrn the embrace, a little more slowly, but with genuine conviction and sympathy."
            samantha.say "Oh, [hero.name]...is it true?"
            hero.say "Sam, I really wish I could say it wasn't...but it is."
            samantha.say "Bastard..."
            "She hisses the word into my shoulder bitterly."
            "I should be thinking about Sam right now..."
            "Well, I am - but..."
            "I really should be feeling sorry for her and trying to be a good friend in her time of need."
            "Instead, all I can think of is how good she feels agaisnt me...how amazing the scent of her hair smells..."
            "After maybe a minute of us holding each other, she lifts her head and regards me."
            "She's looking at me with those huge, slumbrous blue eyes and long lashes now."
            samantha.say "[hero.name]...you'd never do that to me, would you...not if you loved me?"
            samantha.say "Please, I just need to know that it's not me..."
            samantha.say "That all guys aren't like him..."
            "I'm only human, and I can't say what I'd do were the circumstances putting me in Ryan's place."
            "But that's not the kind of harsh honesty Sam needs right now."
            hero.say "It's not you, Sam - any man would be crazy to do that to you."
            hero.say "He's just a scumbag...and he doesn't realise how lucky he is to have you."
            "Samantha smiles weakly through her tears, clearly cheered by what I've said."
            samantha.say "Thank you, [hero.name]...I feel so gutted by all of this...I guess I just needed to talk to a friend."
            "Yeah, because that's all I've ever wanted to be - the friend, the shoulder to cry on!"
            show samantha wedding blush
            samantha.say "You've always been a good friend to me, [hero.name]."
            "What's this now?"
            "I hear a subtle change in the tone of Sam's voice, as though she were pulling herself together and seeing things from a new angle all of a sudden."
            samantha.say "A really good friend...and I haven't ever returned the favour...not really..."
            "Were still almost embracing at this point, and rather than backing off, Sam instead presses herself closer against me."
            samantha.say "Maybe I could change all that...starting right now?"
            "Oh shit - I can feel her hand on my crotch!"
            menu:
                "Push her back":
                    hero.say "Sam, think about this - are you really being sensible here?"
                    samantha.say "He fucked another woman behind my back, [hero.name]."
                    samantha.say "And he was just going to marry me without telling me that!"
                    "I can sense the venom creeping into her voice now, the anger that she's been suppressing at what Ryan did behind her back."
                    samantha.say "If he can do that, then why can't I?!?"
                    hero.say "You're not seeing things clearly right now, Sam..."
                    samantha.say "What's the matter, [hero.name]...don't you like what's on offer?"
                    samantha.say "Didn't you ever look at me back then and wonder what it'd be like to fuck me?"
                    "Hell - why do girls only talk to me like this when I'm trying to be the good guy?"
                    hero.say "Sam, I'd be lying if I said no to that."
                    hero.say "If you'd asked me that before, I'd have said yes in an instant."
                    hero.say "I still would - if you weren't about to get married..."
                    "Sam's embrace loosens a little, as some of the intensity leaves her eyes to be replaced by sadness."
                    hero.say "Please, Sam - if we ever do have a chance...not like this, don't let it be like this!"
                    hero.say "If you turn me into the same kind of guy as Ryan - how long will it be before you hate me like you do him?"
                    samantha.say "Oh, [hero.name]...you're too good for your own good."
                    samantha.say "And you're probably too good for me too!"
                    "Oh yeah, I'm a goddamn saint!"
                    "The patron saint of talking himself out of a sure thing!"
                    $ samantha.set_flag("nokiss", False)
                    $ samantha.set_flag("nodate", False)
                    $ samantha.set_flag("storyD",1)
                    $ samantha.set_flag("storyB",0)
                "Accept Samantha":
                    "What the hell?"
                    "Maybe, under the circumstances, it's the best thing for her to do?"
                    "Then she can go through with this whole fucking charade at least knowing that she got one back on the prick."
                    "Honestly, how selfless am I?"
                    hero.say "Sam...it'd be my pleasure to let you!"
                    "Sam's eyes flash at this, and her smile is so wicked that it's almost enough to get me hard all on its own."
                    "A moment later, she's gathering up the skirts of her dress and kneeling down on the landing in front of me."
                    "I catch a glimpse of white stockings and garters, and it reminds me of just how astonishing Sam's body happens to be."
                    "Sam opens my flies and pulls out my dick like a woman on a mission, grinning and shooting me glances as she does so."
                    "I can see from her expression just how much she's getting off on the playing the part of the bad girl right now."
                    "And her enthusiasm is certainly infectious."
                    "I'm hard before she has my cock anywhere near her mouth, and she gives me one last look before she begins."
                    show samantha bj2 lick
                    "The look is one that says this was inevitable, that we were always destined to do something like this, when the time was right."
                    "I can't say I feel the same, or that I ever thought this would happen."
                    show samantha bj2 lick wet
                    "Sure, I imagined it - but I never expected to be doing this with Sam."
                    "Especially on her wedding day, mere minutes before the ceremony!"
                    show samantha suck
                    "She closes her lips around the head of my cock and begins to caress it with her tongue."
                    "I can feel her teeth almost as much as her lips and tongue, and she's trying to make up for her unease with enthusiasm."
                    show samantha suck closed
                    "It's not the best blow-job I've ever had, and Sam's technique leaves a lot to be desired."
                    "But on the flip side, I'm getting oral from a girl that I thought was going to be out of my life forever, and with an utter prick too."
                    show samantha suck open2
                    "Not to mention the fact that I'm actually getting blown by a bride-to-be right before she takes her wedding vows!"
                    "And those factors more than make up for it."
                    "In the end, it's more the sight of her down there and the knowledge of what's behind all of this that makes me cum."
                    "Rather than Sam's willing, but not very stellar abilities."
                    show samantha bj2 suck cum
                    "I lose myself in her mouth, watching her struggle to keep from spitting out my cum and keep from swallowing it on instinct."
                    "At first I can't imagine why she seems to be holding it in her mouth, almost gargling with it."
                    show samantha bj2 suck cum tits
                    "But then, as the reminder of it slips down her throat, she notes my puzzled expression and smiles again."
                    hide samantha
                    show samantha bj2 tits
                    samantha.say "I want you to be on my lips when he kisses me at the end of the ceremony."
                    samantha.say "I want to pay him back by having his bride taste of another man's cum when he does that!"
                    hero.say "What can I say - I can't think of a more deserving guy!"
                    $ samantha.set_flag("nokiss", False)
                    $ samantha.set_flag("nodate", False)
                    $ samantha.set_flag("storyD",1)
                    $ samantha.set_flag("storyB",0)
                    hide samantha
            show samantha wedding
            "With that, Sam straightens out her dress and gives me a wan smile."
            samantha.say "Wish me luck, [hero.name]?"
            hero.say "Good luck, Sam."
            "I don't say it, but I mentally add 'you're going to need it'."
        "Go to the bathroom":
            $ BATHROOM = True
            "I stand up to go to the bathroom."
            "I could really use some time to myself- freshen up a little."
            "The restroom is down the hall from my table, so it’s a short walk."
            scene bg publicbathroom
            "When I swing open the door with the typical men’s logo on it, I’m grateful that it’s empty."
            "Standing in front of the mirror, I stare at myself, shifting left and right."
            "The bags under my eyes compliment my suit well. After all, I can’t exactly afford a tailored one at the moment, and I’m pretty sure this is the only time I’ll be using it- so, it’s rented."
            "It looks slightly worn, but it’s not too bad. Not in my opinion at least."
            "I straighten my tie and turn to one of the stalls across from the urinals."
            "The stall door creaks open with little force and I lock it behind me."
            "I flip the seat down heavily sit on top of it."
            "Taking a deep breath, I pull out my phone."
            "If Samantha ever caught me looking bored at my table, there was no way she would let me live it down."
            play sound "sd/cell_vibrate.mp3"
            "I blink in surprise when it vibrates."
            bree.say "heyoo~"
            bree.say "how’s your wedding? <33"
            "The second Bree saw me bring in a plastic wrapped suit through the living room, she demanded to know what I was ‘getting all classy’ for."
            "Strangely enough, she helped me get ready despite my resistance."
            "Even Sashe threw in her own opinion as I was walking out- though it was a lot less constructive."
            hero.say "It’s not my wedding"
            bree.say "sure sure"
            bree.say "how’s ‘Samantha’s’ wedding?"
            menu:
                "Fine":
                    hero.say "It’s going fine. Samantha looks happy about it."
                    bree.say "xD"
                    bree.say "‘fine’ is not usually a great word for a wedding ya know"
                    hero.say "whatever"
                "I Want to go Home":
                    $ bree.love += 5
                    bree.say "aww poor baby!"
            bree.say "i’ll make you some hot cocoa when you get back to cheer you up"
            hero.say "fuck off"
            bree.say ";D"
            "The door to the bathroom slamming open tears my attention away from Bree."
            "I don’t think much of it- until a strange giggle makes me wonder if I’m in the right place."
            ryan_say "Shh."
            unknown_girl_say "I can give it to you better, sweetie."
            ryan_say "Prove it."
            "What the fuck. Was that Ryan? No way. Not at his wedding."
            "But there he was, clearly through the crack in my stall, along with that bridesmaid from earlier."
            "Something unzips."
            unknown_girl_say "You’re so... composed! Not even Samantha can keep a treasure like you."
            ryan_say "Shut up and suck it."
            "No, no way."
            "I am not sitting through Ryan getting a blowjob in a shitty restaurant bathroom."
            "My hand touches the lock, but pauses."
            "I can’t just walk out and pretend like I didn’t see anything."
            "Ryan would get angry, threaten to keep me quite."
            "He would wonder why I wouldn’t say anything to Samantha."
            "I didn’t need that on top of everything else."
            if not samantha.get_flag_value("ryancheats"):
                "There is no way Samantha would believe me if I just told her about this."
                "I stare blankly at my phone and back up at Ryan."
                "Making an easy decision, I lift my phone and open the camera."
                "I snap a few photos."
                "I can’t just send these to her without saying anything, can I?"
                "She would break down."
                "I have to be there for her."
                $ samantha.set_flag("ryancheats",True)
            ryan_say "Hnng-"
            "A wet sound filled the bathroom followed by a loud pop."
            "I cover my ears to block out the girl’s moans."
            "This is officially the worst wedding I’ve ever been to."
            "My phone vibrates in my hand, and it makes my heart stop for a few seconds."
            "When the two don’t stop, I sigh in relief."
            "Apparently everything sounds louder when you feel like you’re going to die at any moment."
            "It’s another text from Bree."
            "I briefly consider responding, and accidently glance up."
            show ryan natalie blowjob
            "Through the crack, I can see Ryan’s hands tangled through the girl’s hair and her lips firmly locked onto his member."
            "Her nose is buried deep into his pubic hair, and it looks like she’s taking him all the way to the base."
            "Does she have a gag reflex?!"
            hide ryan
            "As fast as I look up, I look back down."
            "I decide to just fix my eyes on the floor, trying to ignore the two right in front of my door."
            "I don’t know how much time passes, but by the time I finish counting every square tile one the floor, the bathroom door shuts again and it’s once again silent."
            "Fuck me."
        "Dance":
            "I might as well see what’s going on on the main floor. Maybe I’d get a chance to talk to Samantha."
    scene bg highclassrestaurant
    show natalie teaser
    unknown_girl_say "That was so exciting!"
    "I jump in surprise at her sudden presence, breaking me out of my thoughts."
    "She plops down in the chair next to me, leaning forward on the table with her elbows."
    unknown_girl_say "And romantic!"
    unknown_girl_say "I wish I had someone to treat me like that, don’t you?"
    hero.say "Um... yeah, I guess."
    if BATHROOM:
        "I stare at her warily, the image of Ryan’s dick shoved far down her throat at the forefront of my mind."
        "I can’t help but notice that her lips were more plump and red than when I first saw her when I got here."
    unknown_girl_say "The food’s really good!"
    unknown_girl_say "I’m a little surprised to be honest."
    unknown_girl_say "..."
    unknown_girl_say "Wanna dance with me?"
    "I look up at her. She stares at me with a slight blush on her face. Is she being serious?"
    hero.say "I don’t know. I don’t really dance-"
    "She suddenly grabs my arm and pulls me up before I can react."
    unknown_girl_say "That’s okay! I don’t either. But we can both try!"
    "The middle of the hall was filled with darkened mood lights and dancing couples."
    "The music playing turns somewhat slow and mellow."
    "She puts her hands on her hips as if she were expecting something."
    "Didn’t I just say I didn’t know how to do this crap?"
    "I wrack my brain for some sort of reference."
    "Movies? Sure. I nervously put my hands up in the formal dance position."
    "She smirks, takes my hands and puts the other on her hip. We swayed back and forth."
    "She seems to be enjoying it, but I can’t help but feel awkward."
    "It didn’t feel right. She’s smaller, more sporadic."
    "Samantha and Ryan were somewhere around here."
    "I want to talk to her- congratulate her or something."
    "At the same time, I don’t want to see them so in love."
    hide natalie
    show samantha wedding happy
    samantha.say "[hero.name]!"
    "Speak of the devil."
    samantha.say "I’m so glad to see you! Thank you so much for coming."
    "She puts a gentle hand on my shoulder."
    "Her friend backs away from me with a huff."
    "I finally relax."
    hero.say "Hey, Sam."
    hide samantha
    show natalie teaser
    unknown_girl_say "Sam! You’re so beautiful! Look at you!"
    "Her cheeks tinge red and she set a soft hand on her face."
    hide natalie
    show samantha wedding happy
    samantha.say "Thank you! You look great too. Thanks for being my bridesmaid... and helping me put things together."
    hide samantha
    show natalie teaser
    unknown_girl_say "This is all you! No more ‘thank you’s- enjoy yourself."
    hide natalie
    show samantha wedding happy
    samantha.say "I will- in fact~"
    "Samantha turns to me."
    samantha.say "May I have this dance?"
    hero.say "..."
    menu:
        "Yes":
            "Of Course"
            "She claps her hands gleefully."
            samantha.say "Yay~! I hope you don’t mind, Natalie."
            "Natalie? ... Oh."
            hide samantha
            show natalie teaser
            natalie_say "He’s yours!"
            "Natalie winks at Sam, but I can see her hesitation."
            if not "natalie" in GIRLS:
                show screen message(title="Teaser",what="Natalie is only a teaser right now, she will be fully added to the game later on.")
                pause
                hide screen message
            hide natalie
            show samantha wedding happy
            "I turn to Sam, who’s already moving closer."
            "I automatically put my hand on her hip and she tenderly takes my other hand."
            hero.say "Having a good night?"
            "She laughs, a genuine smile coming across her face. It’s beautiful."
            samantha.say "You wouldn’t believe. This has been... my dream. I can’t believe it’s happening right now."
            hero.say "Ha! I can. You guys were all over each other when we still lived together."
            samantha.say "You know what I mean."
            samantha.say "..."
            samantha.say "You look sad."
            hero.say "I- I’m not. I’m happy for you."
            "Samantha frowns at me. I blink rapidly, trying to control my expression."
            hero.say "Don’t worry about me. This is your big night- let’s have some fun."
            "It looks like she wants to say more, but she shakes her head and gets closer."
            hero.say "I heard it took quite a lot of work to throw this thing together so fast."
            samantha.say "Ugh. Don’t get me started. I’m used to sleepless night from college, but this was something else!"
            samantha.say "What do you think for a bunch of rush planning?"
            menu:
                "It's beautiful":
                    hero.say "I think you did a great job. You look fantastic, the food is good... you should be proud of yourself."
                    show samantha wedding blush
                    "A blush presents itself above her light makeup."
                    samantha.say "Thank you. You’re so sweet!"
                "It could have used some more work.":
                    hero.say "It could use some more love."
                    samantha.say "Of course it could! But there was no time."
                    hero.say "I wouldn’t worry about it. Everyone’s enjoying themselves and we’re here now."
                    samantha.say "Good point."
            "The music changes to a traditional slow dance and I find myself almost hugging her, swaying back and forth with the flowing music."
            "The night ends with her head on my chest, eyes closed."
            "The guilt eventually subsides as we melt together in the middle of the dance floor."
            "Her soft blonde hair is tickling at my chin, but I can’t pull away."
            "She’s warm and light."
            "I hope she can’t hear my heart pounding in my chest."
            "The night comes to a calm end, dancing with my best friend in the middle of the dance floor."
        "Ask about Ryan":
            show samantha wedding
            hero.say "I can’t steal away the bride on her wedding night."
            "Shouldn’t you be dancing with Ryan?"
            samantha.say "I’ve been with Ryan all night!"
            samantha.say "I want to say hi to my friends."
            "She playfully tugs at my arm, but I pull away."
            "Her face falls."
            hide samantha
            show natalie teaser
            natalie_say "I think I see Ryan over there!"
            natalie_say "You should go snatch him up before another girl gets to him."
            hide natalie
            show ryan tux smile
            "I follow her line of sight to see Ryan talking to another girl, getting far too close for comfort."
            if not samantha.get_flag_value("nocheat"):
                "Sam giggles, but my chest burns with anger that I force down, knowing what he was probably doing."
                "During his wedding."
            hide ryan
            show samantha wedding happy
            samantha.say "Alright, alright."
            natalie_say "Quick! I hear a slow dance starting!"
            hide natalie
            show samantha wedding happy
            samantha.say "Ooh! But, you owe me a dance once all this is over, [hero.name]!"
            hero.say "..."
            samantha.say "Promise!"
            hero.say "Fine. I promise."
            "She grins wide, then scuttles over to Ryan, getting his attention. Ryan looks down at her, his face morphing into kindness. I move back to Sam’s friend."
            hide samantha
            show natalie teaser
            natalie_say "They’re so cute. You’ll keep dancing with me, right?"
            hero.say "Um-"
            "She gets closer to me before I can answer, forcing me into the slow dance."
            "We move around the hall for a while. She’s talking, but I’m not really focused."
            "I only stare over her back, watching Ryan and Samantha hold each other tightly."
            natalie_say "Hey- are you listening?"
            hero.say "Sorry, what?"
            natalie_say "What are you so distracted by? Are you not into me or something?"
            hero.say "No, that’s not it, - ... um."
            "Shit, what’s her name? I don't even remember went I met her, my mind can’t even pull up the first letter. Wendy? Irene?"
            natalie_say "... Natalie!"
            "Not event close."
            hero.say "Sorry. I-"
            natalie_say "No, whatever. I can tell you’re not interested."
            hero.say "..."
            hero.say "I mean, you’re not wrong."
            "Natalie’s mouth hangs open as if I’d personally offended her."
            "She makes an upset little screech before slapping me on the shoulder with little force and turns on her heel."
            if not "natalie" in GIRLS:
                show screen message(title="Teaser",what="Natalie is only a teaser right now, she will be fully added to the game later on.")
                pause
                hide screen message
            hide natalie
            hero.say "... At least that’s over."
            "I move back to my seat, alone once again. I taste the untouched duck."
            "It’s... sweet. But not in a bad way."
            "Sam really did make a good choice."
            "A waiter spots me and comes around to fill my tall glass with pale champagne."
            "I mutter a thanks."
            "Not my choice of drink, but it would be good enough for now."
            "I start gulping it down, hoping to feel the familiar buzz in the back of my mind."
            "The sooner it came, the better."
    return

label samantha_event_B02:
    $ samantha.set_flag("storyB",3)
    $ samantha_love_max = 140
    $ samantha.set_flag("nokiss", False)
    samantha.say "[hero.name]!"
    "I recognize Samantha’s voice behind me easily."
    show samantha
    "Once I spot her, my eyes dart to the shiny new ring on her finger, sparkling under the light."
    "She comes up to me and grabs my arm."
    samantha.say "How are you?"
    hero.say "You know- working."
    show samantha sad
    "Sam pushes out her lip in a pout."
    "She’s trying to be playful, but I can see something else hiding beneath."
    "Gloom? It didn’t look good on her."
    hero.say "Something wrong?"
    samantha.say "Hm? What do you mean?"
    hero.say "I’ve known you long enough to see when you’re sad."
    hero.say "You know you can talk to me, right?"
    "She’s silent for a long moment, adjusting her pressure on my arm, squeezing dejectedly."
    samantha.say "It’s just..."
    samantha.say "I- I thought that once we got married, Ryan would be around more."
    samantha.say "That we’d finally be a real family; eating meals together, falling asleep in each others arms- but he’s never home."
    hero.say "Oh. I’m sorry."
    samantha.say "Haha! It’s not your fault."
    hero.say "Have you talked to him about it?"
    samantha.say "I’m kind of scared to."
    "My expression must be something like concerned, because she instantly raises her arms in denial."
    samantha.say "Not like that!"
    samantha.say "Never like that."
    samantha.say "He’s always so busy."
    samantha.say "I’m afraid that if I tell him to spend more time with me that he’ll think I’m being... possessive."
    samantha.say "I don’t want that! I’ve always let him have his freedom."
    samantha.say "I’ve never been that overbearing girlfriend, but... what if he thinks I’ve changed just because we’re married now?"
    hero.say "What? You’re afraid he’d leave you if you ask him for something?"
    samantha.say "No, no, not leave. It’s complicated- but yes."
    hero.say "Seriously!? That guy would do anything for you."
    "Okay, probably not anything. But she needs the encouragement."
    hero.say "If he’s neglecting you, you should talk to him."
    samantha.say "He’s not neglecting me!"
    hero.say "It sure sounds like he is."
    samantha.say "... Fine. I’ll talk to him. But he is not neglecting me!"
    "I shake my head and don’t answer. Whatever you say, Sam."
    samantha.say "Anyway~ I wanted to hang out with you."
    hero.say "Ha! With me?"
    samantha.say "Yes! Don’t say it like that."
    samantha.say "I’ve been meaning to pick up some novels from the bookstore in the mall. Will you go with me?"
    hero.say "Yeah, alright."
    samantha.say "Yay!"
    hide samantha
    scene bg bookstore
    "I find myself between shelves of books, looking blankly at titles and covers."
    "Nothing was really catching my attention."
    show samantha
    samantha.say "[hero.name]! What do you think of this one?"
    "Sam rushes at me with a book in hand from the children’s section. It’s large and colourful, with about ten pages max."
    menu:
        "Why are you looking for kids books?":
            hero.say "Aren’t these a little young for you?"
            samantha.say "They’re not for reading! They’re for studying. You know I want to write children’s books."
            hero.say "Oh yeah."
        "Take Book":
            "I turn the book over in my hands. It’s got an abstract art style with vibrant colours and strange characters."
    hero.say "It’s... nice?"
    samantha.say "That’s all you got? You can do better than that~"
    if hero.knowledge >= 50:
        "I stare flip open the book and analyze the pages. The paper was the usual overly thick texture that most kids books had."
        hero.say "I guess..."
        hero.say "The art is different. But I don’t think it matches your style. You have a softer appeal."
        samantha.say "Hmm."
        hero.say "As for the writing, it’s got an interesting story as far as that goes- but I think you could study the theme and moral ending."
        "Sam nods along attentively with my words. It felt good to have her listen."
        samantha.say "I take it that means it’s a good choice?"
        hero.say "Sure."
        "She gives me a feigner salute and tucks it under her arm."
    else:
        "I stare blankly at the cover. The amount of colours makes my head swim, not used to the brightness. Compared to my room, this was practically a rainbow."
        hero.say "It’s got... a lot... of colours?"
        samantha.say "Quite the articulate, aren’t you?"
        hero.say "Shut up!"
        hero.say "..."
        hero.say "I like it."
        "Sam nods her head dutifully and tucks it under her arm."
    samantha.say "So? Are you getting anything?"
    hero.say "I guess I will while I’m here."
    samantha.say "Good! I’m going to keep looking around."
    hide samantha
    "I’m left by myself as she retreats back to the children’s section, hunting for more books. I didn’t really know where to start."
    $ r = 0
    menu:
        "Cooking":
            "Pictures of delicious food and pristine recipes litter the covers of every book in the aisle. I grab at the first one that catches my eye."
            hero.say "Baking?"
            "I turn the pages quickly, skimming through the words. Complicated desserts that I could never probably perfect stare back at me with intimidation."
            "I take the book up to the counter to pay. Sam’s already up there waiting for me, plastic bags in hand."
            $ hero.gain_item(Consumable("cooking book", money_cost = 100, effects = [("skill","cooking"),("time",4)], limit = "week"))
            $ r = 1
        "Sports":
            "Football, baseball, soccer... every sport I could imagine was laid out in front of me. Some were magazines, some were thick books examining every aspect of the game."
            "My hand hovers over a magazine, covering a broad area of each one."
            "I grab the magazine, the flimsy pages flopping around in my hand. I walk up to the counter, digging out my wallet."
            $ hero.gain_item(Consumable("fitness book", money_cost = 100, effects = [("fitness",2),("time",4)], limit = "week"))
            $ r = 2
        "Fiction":
            "The fantasy and science fiction call my name. The newest publishers grace the shelf with shiny, new, hardback covers."
            "I flip over the back of one, reading the summary. Dragons, space, battles... what’s more to love?"
            "The decision is easy. The book has my name on it before I even set it down in front of the store clerk to pay."
            $ hero.gain_item(Consumable("charm book", money_cost = 100, effects = [("charm",2),("time",4)], limit = "week"))
            $ r = 3
    show samantha
    samantha.say "Find what you were looking for?"
    hero.say "Yup!"
    "I wave the single book in front of her and she stares at it intently."
    if r == 1:
        "Sam’s face lights up instantly."
        samantha.say "You have to bake me something! Look at all these recipes. Good choice!"
        hero.say "..."
        hero.say "You work at a bakery."
        samantha.say "Excuses!"
    elif r == 2:
        samantha.say "You’re a sports junkie, hm?"
        hero.say "Junkie is a strong word."
        samantha.say "Sure, sure. Maybe you’ll finally learn how to play darts with me."
        hero.say "I don’t think that’s covered in here."
    elif r == 3:
        samantha.say "Ooh! Exciting! I should have expected that, considering your room."
        hero.say "Hey! My room looks great."
        samantha.say "If your version of great also means nerdy then, yeah, it’s great."
    samantha.say "Thanks for coming with me! This was fun."
    hero.say "No problem. Are you heading home?"
    samantha.say "... Yeah, I guess I am."
    "She looks sad again. Was she really that lonely?"
    hero.say "Aw, Sam."
    samantha.say "I-"
    samantha.say "..."
    "My heart sinks when tears start running down her cheeks. Oh shit."
    "I pull her into a hug. She wraps her arms around my torso."
    hero.say "Want to hang at my house instead?"
    "I can feel her nod her head in the crook of my neck."
    hero.say "Alright. Let’s go."
    hide samantha
    scene bg livingroom
    show samantha at left
    "Samantha is sitting on the couch, looking through her new book. The tears have long since dried."
    "I’m in the kitchen making her some sweet tea."
    "Once I drop the bag into the steaming water and add copious amounts of sugar, I carefully make my way back to where she sits."
    "When I turn the corner, I see Bree has come down from her room."
    show bree casual at right
    bree.say "Hiya! Did [hero.name] really bring home a girl?! He’s growing up so fast!"
    hero.say "Bree-"
    if not game.get_flag_value("samanthaknowsbree"):
        $ game.set_flag("samanthaknowsbree")
        bree.say "You look familiar. Did you help Ryan find this house for me?"
        hero.say "Bree-"
        "Despite her incessant talking, Samantha doesn’t seem bothered. So, I just set down her tea on the coffee table in front of her."
        samantha.say "Yeah, that’s me."
        bree.say "That means- you just got married, right?"
        samantha.say "Yup!"
        bree.say "Ha! I can see why [hero.name] was so depressed."
        hero.say "Bree! Okay, go back to your little hermit hole."
        bree.say "Hermit hole!? If that’s what you think of it, then you haven’t even had a glimpse at my game collection. More like paradise, you sad sap!"
    else:
        samantha.say "Hi, Bree."
        bree.say "Hi."
        bree.say "I'll be in my bedroom, don't do anything I wouldn't do."
    hide bree
    show samantha at center
    "With that, Bree retreats back up the stairs. I try not to let my face heat up."
    hero.say "I have no idea what she’s talking about."
    "Samantha simply giggles, a hand lightly covering her mouth."
    samantha.say "She seems like a lively girl. Are you glad she’s your roommate?"
    hero.say "I suppose you guys could have done worse."
    samantha.say "Don’t be mean! She’s pretty."
    hero.say "Whatever."
    samantha.say "I mean it! You guys would be cute together."
    hero.say "You’re funny."
    "She rolls her eyes and gives up. Picking up the cup of tea, she takes a sip."
    samantha.say "Not bad."
    hero.say "Ouch."
    samantha.say "Wha-! It’s good. Don’t get all upset. It just needs a little more sugar."
    hero.say "There are, like, three teaspoons in there."
    samantha.say "Mh hmm. Like I said, it needs more sugar."
    "A moment passes in silence as she drinks the rest of her tea."
    hero.say "So, What can we do to cheer you up?"
    samantha.say "I don’t know. What’cha got around here?"
    menu:
        "Bake Something" if r == 1 or "cooking" in hero.skills:
            hero.say "We could bake something."
            if r ==1:
                samantha.say "Ooh! Putting that book to use, I see."
                "I pick up the book from where I’d tossed it on the coffee table and look through for simple recipes."
            hero.say "Cupcakes?"
            samantha.say "Yes! Let’s do it!"
            hide samantha
            scene bg kitchen
            show samantha
            "Samantha rushes past me into the kitchen. I hear clanking pots and opening drawers already. I follow her."
            samantha.say "Eggs, vanilla, baking powder-"
            if r ==1:
                hero.say "Whoa- wait, you haven’t even seen the recipe yet."
                samantha.say "I work at a bakery. I know how to make cupcakes."
                "I shrug. Good point. I close the cookbook and set it on the counter. I find a few large mixing bowls and set them next to the ingredients."
            samantha.say "Mix these, please!"
            "She says ‘please’ but it sounds more like a command. Nonetheless, I take the ingredients she shoves at me and mindlessly pour them into a bowl, whisking them together."
            "She does the same, mixing up the dry stuff with a fork."
            samantha.say "Hmm... where’s the flour?"
            hero.say "Uh, on the top shelf, I think."
            "Samantha goes to the shelf I point at. It’s a few inches taller than her. I don’t think she can reach and she tries anyway, standing on her toes."
            hero.say "Do you need-"
            samantha.say "Eeek!"
            "A puff of white in the corner of my vision has me whipping around. Samantha stands, arms still raised above her to get the bag."
            "She’s covered from head to toe in dusty flour. The floor wasn’t looking much better. I can’t help it- I start laughing."
            samantha.say "Are you laughing?!"
            "I try to get a hold of myself- I really do. Before I can, Samantha grabs a pile of flour off the floor and blows it right into my face."
            "I was lucky my eyes were closed."
            hero.say "Wha-?! What the fuck?!"
            "Now she’s laughing."
            samantha.say "You’re right! It is really funny!"
            "Wiping at my face, I get a good look at the mess. This was going to be a nightmare to clean up."
            hero.say "Is there any left?"
            samantha.say "..."
            samantha.say "Yep! There enough left in the bag."
            "She picks up the remains of the flour and pours in into the bowl."
            "Samantha’s a mess, but she’s beaming; and that’s all that matters."
            scene bg black
            with dissolve
            pause 1.0
            scene bg kitchen
            with dissolve
            show samantha
            "Samantha pulls the cupcakes out of the oven. They look perfect with her watchful eye. The bottom floor of the house smells fantastic."
            "She sets down the hot tray on top of the counter to let them cool. She shakes her arms, still covered in white power."
            hero.say "Want me to find you some extra clothes? I don’t think Bree will mind."
            samantha.say "No, it’s alright. This was my fault anyway."
            hero.say "Oh, come on. You don’t want to walk home like that, do you?"
            samantha.say "... You have a point. Alright."
            "I let her stay with the cupcakes and walk upstairs."
            hide samantha
            scene bg black
            with dissolve
            $ renpy.pause(1)
            scene bg secondfloor
            with dissolve
            "I knock lightly on her door. No answer. I knock louder. There’s a crashing sound from the other side and the door flings open."
            scene bg bedroom2
            show bree casual
            bree.say "This better be good! I’m in the middle of a fight-"
            "She abruptly stops at the sight of my face, holding her headphones in one hand. I must not have washed my face enough.Goddammit Samantha."
            bree.say "What the hell are you guys doing?"
            hero.say "Can I borrow some clothes for Samantha?"
            bree.say "Having fun down there? Sure, but you better not mess them up with your dirty foreplay. I want these back!"
            hero.say "That’s not-!"
            "Bree shoves a pile of clothes into my hands and shuts the door in my face. That girl would be the end of me."
            hide bree
            scene bg black
            with dissolve
            $ renpy.pause(1)
            scene bg kitchen
            with dissolve
            show samantha
            hero.say "Here."
            samantha.say "Thanks. Oh! You should tell Bree I said thank you. I think I have to go, though."
            hero.say "Oh... okay, no problem."
            samantha.say "I’m sorry! Ryan texted me and said he was home and... we have a few things to talk about. Thank you so much for having me over."
            hero.say "You’re always welcome here."
            "A wide smile graces her face. I let her change in the bathroom, then walk her to the door."
            "She gives me a small wave- then pulls me into a hug. I watch her go."
        "have drinks":
            hero.say "I think there’s still some wine left if Sasha hasn’t gotten to it yet."
            samantha.say "Sounds like a plan."
            "We both move to the kitchen. I open up a cupboard and pull out a half full bottle of red wine."
            "Sam gets two glasses, still remembering where things were last time she was here."
            "I tilt the bottle and fill each glass to the brim. Samantha nods in approval. She takes a long drink. I do the same."
            hero.say "It can’t all be bad. What are some good things going on with you two?"
            samantha.say "Well... the night of the wedding, he took me to bed and made love. It was the most passion he’s had for a while."
            hero.say "Oh-"
            samantha.say "He’s been getting really dominant lately. I can’t say I hate it."
            hero.say "Not really what I meant, but good start."
            "She giggles and takes another gulp."
            samantha.say "He gave me a stack of new books when he finally got home yesterday. I haven’t started them yet, but they look good."
            hero.say "That’s nice."
            samantha.say "Hmm."
            "The air is tense, but it slowly unravels as we drink more."
            menu:
                "University":
                    hero.say "How’s the studying going? Doing any better with that stuff?"
                    samantha.say "I haven’t had too much time to work on it lately, but my grades are rising at least. God, I hate math."
                    hero.say "Ditto."
                    samantha.say "My literature classes are really great, though. We get to write an essay on story structure."
                    hero.say "Really? How’s that going?"
                    samantha.say "I’m finished!"
                    hero.say "Oh."
                "Work":
                    hero.say "Still loving the bakery?"
                    samantha.say "How is that even a question?! Of course I do."
                    samantha.say "Oh, I’m so excited for next week. We’re getting new recipes in as a standard."
                    hero.say "What are they?"
                    samantha.say "Guess! They’re my favourite."
                    menu:
                        "Tiramisu":
                            samantha.say "Nope! But that’s a great idea. I should suggest that."
                            samantha.say "We’re adding fresh cinnamon rolls to the menu! The bakery’s going to smell so good."
                            hero.say "It already does."
                        "Cinnamon Rolls":
                            samantha.say "Yes, yes! You remembered!"
                            hero.say "You had them all over the house. Of course I remember."
                        "Funnel Cake":
                            samantha.say "It’s a bakery, not a fair!"
                            hero.say "What, are you saying you don’t like those?"
                            samantha.say "No! That’s not what I mean. Cinnamon rolls! We’re going to start making cinnamon rolls."
                "Fun":
                    hero.say "What do you do all day? Y’know, other than obsess over Ryan."
                    "She gives a playful glare, but answers anyway."
                    samantha.say "Darts... writing. I like hanging out with you! Does that count?"
                    hero.say "..."
                    hero.say "Yeah, I guess it does."
            "A sudden buzzing grabs both of our attention: Samantha’s phone. She pulls it out of her back pocket."
            samantha.say "Ryan sent me a text."
            samantha.say "He says he’s home!"
            hero.say "Are you saying you’re leaving?"
            "She looks up at me with large eyes, pleading for forgiveness."
            samantha.say "I’m sorry!"
            hero.say "No, it’s fine. As long as you have a talk with him!"
            samantha.say "..."
            hero.say "Sam! You have to!"
            samantha.say "Alright! I will."
            hero.say "Good."
            "She finishes her glass and sets in on the counter. I walk her to the door."
            samantha.say "Thanks for having me over, [hero.name]. I really appreciate it."
            hero.say "Anytime."
            "Samantha gives me a friendly wave goodbye and steps off the porch. I smile and close the door behind her."
    return

label samantha_event_B03:
    $ samantha_love_max = 160
    "My phone buzzes suddenly in my back pocket. When I open it up, Samantha’s name blares at me from the screen; it’s a text."
    samantha.say "Hey"
    hero.say "Hey. What’s up?"
    samantha.say "Nothing much"
    samantha.say "Can I come over?"
    hero.say "Right now?"
    samantha.say "Yes"
    samantha.say "My house is just really empty right now"
    samantha.say "I don’t know what to do"
    menu:
        "Of Course You Can":
            hero.say "Yeah. You can come over."
            samantha.say "Thanks"
            samantha.say "I really appreciate that you’ve been here for me."
            $ a = True
        "Too Busy":
            hero.say "Sorry, Sam. I’m really busy right now."
            hero.say "Maybe next time?"
            samantha.say "Alright. Sorry for bothering you."
            $ a = False
    scene bg black
    with dissolve
    pause 1.0
    scene bg livingroom
    with dissolve
    "I’m broken out of my thoughts by a knock at the door."
    scene bg black
    with fade
    scene bg house rain
    show samantha casual sad
    with wiperight
    if a:
        hero.say "Hey, Sam."
        samantha.say "Hi, [hero.name]. Thanks for letting me come."
    else:
        hero.say "Sam?"
        samantha.say "Hi..."
        samantha.say "I’m sorry. I know you said you were busy, but..."
        samantha.say "I just need some company right now."
        hero.say "Oh. Alright."
    scene bg livingroom
    "I take Samantha into the living room. She stands nervously, rubbing her hands, looking at the stairs as if she’s worried someone will walk in."
    hero.say "Are you alright?"
    samantha.say "I- um-"
    "Tears drop down her cheeks one by one. I don’t know what to say."
    hero.say "Want to go somewhere else?"
    "She nods her head, furiously dabbing at her eyes with the edge of her sleeve. We move to my room. By the time we get there, she’s full blown sobbing."
    scene bg black
    with dissolve
    pause 1.0
    scene bg bedroom1
    with dissolve
    show samantha casual sad
    hero.say "..."
    menu:
        "What’s wrong?":
            hero.say "Sam... are you okay? Did something happen?"
            samantha.say "I- I..."
            samantha.say "I don’t- I- "
            "She doesn’t seem ready to talk, so I try to give her some space."
        "Let Her Cry":
            "..."
    "I let her sit on my bed and take my place beside her. She leans on my shoulder and I wrap an arm around her."
    samantha.say "I talked to Ryan."
    "My insides freeze. Is that why she’s crying? Before she says another word, rage start building up in my throat."
    samantha.say "I talked to him- I really tried. When I asked why he was never home he got upset."
    samantha.say "I said I wanted us to spend more time together. Ryan... Ryan said that just because I was his wife now doesn’t mean I get to control him."
    samantha.say "That was a couple days ago. He hasn’t been home since."
    "Ryan... left? No, he didn’t leave. He would be back, I’m sure of it."
    "He was a douchebag, but he wouldn’t just up and leave Samantha if they had a little argument."
    hero.say "Sam, I’m so sorry."
    samantha.say "I shouldn’t have brought it up. This is all my fault."
    hero.say "Hey! Don’t say that- this is in no way your fault. Ryan’s a dick and that’s the end of it."
    samantha.say "No, it is! I was... too aggressive. I made him upset. I should have been calmer about it."
    "That was blatantly untrue. Samantha was the kindest girl I’ve ever met. If anyone had been aggressive, it was Ryan."
    "No debate. I don’t think Samantha could even raise her voice sometimes."
    hero.say "That’s not true. I know it didn’t happen like that and you know it too."
    "She doesn’t answer, but shakes her head. I take her hands in mine; their shaking and pale. It was hard to watch, my throat constricting in concern."
    hero.say "Listen to me; we’re going to forget about Ryan for tonight. He doesn’t deserve for you to think about him."
    samantha.say "But-"
    hero.say "No ‘but’s. You’re going to think about yourself for once."
    samantha.say "... I can’t. I’m sorry."
    hero.say "You have to. If not for you, then do it for me."
    samantha.say "I don’t know how."
    "My mind races. What can I do? How can I distract her?"
    samantha.say "..."
    samantha.say "Mmph-!"
    "The next thing I know... I lean in to kiss her."
    "And promptly give myself a heart attack. What am I thinking? This would only make things worse. I’d be lucky if she didn’t walk out on me right now."
    hero.say "Oh god- I’m so sorry! I don’t-"
    "Her eyes are glassy for a moment. I blink, and her lips are back on mine, but I didn’t start it this time."
    "My hands snake up into her blonde locks. It’s soft and clean, as if she spent the entire day brushing it out of boredom."
    "My blood boils as I realize she probably did purely out of anxiety."
    "Her tongue prods at my lips. I breathe in, taking in her tongue with the sudden lack of air. The muscle is unbelievably soft."
    "I can taste the salt in her tears mixed with warm, sweet saliva."
    "Samantha’s hands find the front of my chest. She’s stuck between grabbing blindly and coherently exploring every curve and dip of my body."
    "I need to do the same. I lift my hands under her shirt, touching her bare back. I find the strap of her bra easily, plucking at it absently with one hand."
    "The other traces along each bone of her spine, slowly getting lower and lower."
    "She gasps into my mouth once I reach her waistband. I slip my fingers underneath, tugging lightly."
    "At the same time, her hands are at my hips, gripping tightly. My lower half becomes warm and my jeans strain against my crotch."
    "The hand I have on her strap fumbles for a moment before undoing the clasp. Samantha’s bra comes loose and falls down her front."
    "My shirt comes off in the next second."
    samantha.say "[hero.name]!"
    "Samantha’s shirt comes over her head, her bra hitting the floor. Her large breasts lay perfectly round in front of me."
    "I push her back onto the covers and immediately take one of her nipples into my mouth. She gasps above me."
    "My tongue shoots out of my mouth and hits something hard. A piercing?"
    "My mind briefly brings up images of our time at the sex shop- yep. Definitely a piercing."
    menu:
        "Play With the Piercing":
            "Making my mind, I loop my tongue around the metal and suck hard."
            samantha.say "Hhng-!"
            "My teeth clack against the ring. I pull up, to the side. She’s writhing underneath me."
            "The mix of skin and metal make my face heat in anticipation."
            "My hands twitch, needing something to do. One snakes under her hip, grasping at her plump ass."
            "The other plays with the other nipple piercing, rubbing circles around it teasingly."








    samantha.say "[hero.name]! Please! I need-"
    "Samantha pulls down her pants, pushing them off of the bed."
    "Her fingers are expertly unbuttoning my jeans and the building pressure is finally released as mine fall to the floor as well, boxers following suite."
    "My length points to the ceiling, not wanting to wait any longer."
    "I spread her thighs and she obediently opens them for me. My skin is hot, radiating warmth."
    "It’s almost suffocating. The only thing keeping me from her was the thin cloth covering her lower half."
    "I push my nose into her panties, her scent making me dizzy."
    "There’s a damp spot staining through; I pull back. Her legs are thick and beckoning me back down."
    "I lower my face into her thighs. I nip at her panties and pull hard with my teeth until they’re at her knees."
    "Going back up, she’s already wetter, leaking anxiously and breathing hard. I’m doing the same."
    menu:
        "Foreplay":
            "Deciding to give her the pleasure she needs, my tongue darts out and licks at her vagina. It’s hot and she twitches below me."
            samantha.say "Oh my god!"
            "Her words spur me on. My eyes lock onto her clit; I dive in, mouth latching onto her."
            "Her taste is unique and her smell is intoxicating. It’s nothing like I’d ever experienced."
            "Her hips wiggle under me in pleasure. She tugs hard at my hair."
            "I ignore her grunt of disappointment as I lean back, gulping down a breath. Before she can recover, I shove my fingers into my mouth, get them wet, and am opening her up."
            samantha.say "I need you, I need you!"
            hero.say "You’ll have me."
            "One finger, two, three. I scissor the digits, stretching her insides."
            "I spit on my hand and rub my cock, my own eagerness taking over."
            hero.say "Ready? Are you alright?"
            samantha.say "Get inside of me."
            "I don’t need anymore encouragement. I line myself up and slowly push inside of her, watching her face the entire time."
            "The heat completely engulfs me. She’s tight, her walls gripping at me, swallowing me whole."
            "I push in and out, blinking away the buzz in my mind. My hips do the work, searching for much needed friction."
        "Fuck":
            pass
    "The hardness in between my legs can’t be ignored any longer."
    $ CONDOM = False
    if hero.has_condom():
        menu:
            "Use a condom":
                $ CONDOM = True
                $ hero.use_condom()
                "I put a condom on then push inside of her."
            "Do it raw":
                "I spit into my hand, try to cover my dick as much as I can and push inside of her."
    samantha.say "Agh- ahh!"
    "I only hesitate for a moment, but when my brain registers her cries as desire instead of pain, I keep going. Her wetness helps guide me along."
    "She’s warm, and I need more. I push in and out hard, our bodies slapping together in passion; the sound mixes with our moans."
    "Her insides grip at me, sucking me inside of her like nothing else. I realize my eyes are screwed shut and pry them open."
    "Samantha’s face is slack with indulgence. Her face is red along with her chest. Her breasts bounce with each thrust, nipples hard."
    samantha.say "Ah... [hero.name]."
    show samantha reverse
    "I’m slipped over onto my back, dizzy. When I come to my senses, she’s on top of me her ass facing me."
    "I groan at the action."
    "Taking control, she bounces up and down. My dick is as hard as it will go, and I’m at the edge."
    "My hands find their way to her hips. My fingers dig into her skin, her plush flesh easily giving way."
    "I can feel it coming. The pressure builds low. I need release."
    hero.say "Sam! I- I’m gonna-"
    "She leans up and captures my lips, swallowing my words. We’re still united as she wraps her tongue around mine."
    "My limbs go limp, my lower half spasms. I can feel myself gasping, can feel Sam do the same into my mouth, but I can’t hear it."
    show samantha reverse orgasm
    "There’s a rushing in my ears, my vision blackens at the edges at the overwhelming satisfaction."
    menu:
        "Pull Out":
            "As much as I don’t want to, something in the back of my mind is tugging at me."
            "I slip out of her slick tunnel just in time as hot semen spills out of me and stains her inner thighs."
            samantha.say "Ah- [hero.name]. You’re so warm."
            "Her cheeks are still burning red, but her eyes are drooping."
            "She runs a shaky hand through my tangled hair and pulls me up for another kiss."
            "Samantha’s lips are plush, her mouth just as soft."
            "It’s almost like I’m dreaming- but I’m definitely not."
            "I feel tired- Sam really wore me out."
            "I collapse next to her on the bed and she looks over at me."
            "I clear my throat."
            hero.say "Um-"
            samantha.say "Shh."
            hero.say "But-"
            samantha.say "The second I start thinking about what we just did, I’ll freak out. I just want to... enjoy this."
            hero.say "... Alright."
            "Samantha’s shoulders relax and she turns onto my chest, breathing in deeply."
            "I can’t really help the increasing weight of my eyes."
            "Darkness settles over my mind, Sam as my welcoming blanket."
        "Cum Inside":
            show samantha reverse orgasm cum
            if not CONDOM:
                "I spill into her."
                if (randint(1,3) == 1 or "hung" in hero.skills):
                    $ HIDDEN.append("samantha")
                    $ samantha.set_flag("storyB",4)
                    $ samantha.set_flag("pregnant",1)
            else:
                "I spill into the condom."
            "The pressure finally comes loose, unwinding. My hearing slowly returns and I find myself staring at my ceiling, breathing heavy."
            "Sam is on top of me, collapsed. Her boobs push into my chest, and I feel warm for a whole different reason."
            "My crush from the past- I’ve finally won her back."
            "My arms wrap around her back. We’re both exhausted. Her hair is everywhere, strands falling over my face, even more so when she buries her face into my neck."
            "I can’t bring myself to care, focusing on the heaviness of my eyelids."
            "I fall into darkness, happily embracing the sleep that comes shortly after."
    scene bg black
    with dissolve
    pause 1.0
    hide samantha
    scene bg black with fade
    $ renpy.pause(0.1)
    scene bg bedroom1
    show samantha naked
    samantha.say "..."
    samantha.say "Ew."
    "Samantha’s hands move over my chest."
    "I hear her moving on top of the covers uncomfortably."
    samantha.say "Ew."
    "Her words finally break through the haze of sleep."
    "My eyes flutter open to see her not looking at me- thank god- but at her legs."
    "Oh yeah. We never did clean up, did we?"
    hero.say "Ew? It’s not that bad."
    "Sam looks up at me with a mix of disgust and a half hearted glare."
    samantha.say "When it’s cold and sticky, it is!"
    hero.say "Okay. Point taken."
    hero.say "The bathroom should be open if you wanna... clean up."
    "Samantha nods."
    samantha.say "A shower would be nice."
    "Despite sitting up slowly, black skirts at the edge of my vision."
    "I wait a moment for the head rush to pass, and when it does, Sam’s standing at the edge of my bed."
    "She’s trying not to let her thighs rub together as she walks but... in her case, that’s kind of impossible."
    "When she gets to the door, she hesitates for a moment, before grabbing a stray blanket and wrapping it around herself and leaves the room."
    "That leaves me with my thoughts."
    "I should feel bad for Ryan- and I do, for some extent."
    "He let himself lose the perfect girl. That was his fault."
    "If a sweet girl like Sam would let her loyalty fall through, he must have really been a dick these past weeks."
    "Maybe I could finally tell her what I saw with Ryan... was this a good time?"
    "I don’t think any time is ‘good’. But I felt more confidence now. She wanted to be with me, right?"
    "A few minutes pass, and I throw on yesterday’s clothes- I’ll just shower after her."
    "Pulling the t-shirt over my head, I furrow my brows at the growing conflict."
    "There’s no way I would get through telling Samantha about Ryan without her breaking down into tears."
    "I never want to see her like that. Maybe I really should just keep it to myself."
    "Before I can make up my mind, my bedroom door swings open. Sam’s hair is damp, dripping with water, and pulled into a ponytail, with a fluffy white towel wrapped around her chest."
    "She looks much happier now that she’s clean."
    "But when her eyes land on me, they grow harder as if she doesn’t know what to say."
    "I don’t know what to say. We definitely can’t just leave it like this."
    "She starts pulling on the clothes she had on last night."
    menu:
        "Tell her Ryan cheated" if samantha.get_flag_value("ryancheats"):
            hero.say "Sam... we need to talk."
            samantha.say "You’re right. We shouldn’t have done this."
            hero.say "No! I mean- yes. But, no. Not about that."
            samantha.say "What do you mean?"
            "I realize just saying it won’t convince her, especially after last night."
            "I grab my phone off of the nightstand, remembering the picture I took."
            samantha.say "Is something wrong?"
            hero.say "I think I know why Ryan’s been so distant."
            "Samantha looks confused, but doesn’t say anything. I swipe open my phone, my finger hovering over the picture from the bar."
            hero.say "I saw Ryan at the bar. With another girl."
            samantha.say "..."
            "I turn the screen to her, the dark image lighting up her paled face. Her pupils dilate when she spots Ryan."
            samantha.say "..."
            samantha.say "When did this happen?"
            "I open my mouth to answer, but quickly close it in realization."
            samantha.say "How long have you known about this?"
            hero.say "Um... for a while."
            samantha.say "You’ve known about this... and you didn’t tell me?"
            "Guilt washes over me at her words."
            samantha.say "I just got married! And you didn’t even tell me before the wedding."
            menu:
                "You’re not much better":
                    "I suddenly feel upset. Does she know where she is right now?"
                    hero.say "Do you think you’re much better than him? You just went behind his back."
                    hero.say "You can’t be mad when you do the same thing to him."
                    samantha.say "I- that’s not-!"
                    "I seem to have hit her hard. Her wide eyes shine with guilt."
                    samantha.say "No, no..."
                    "Tears start pouring down her face with now end. She forcefully wipes at her cheeks, but to no avail as it’s only replaced with more."
                    "Samantha snatches her phone from somewhere off the ground, where it must have fallen with her clothes."
                    hero.say "Sam- wait!"
                    "But the door is already shutting behind her. I jump off the bed and chase after her."
                    "By the time I get to the hallway, I hear the front door slamming. Shit."
                    $ samantha.love -= 20
                    $ samantha.set_flag("nokiss", False)
                    $ samantha.set_flag("nodate", False)
                    $ samantha.set_flag("storyD",1)
                "I’m sorry":
                    hero.say "You’re right. I’m sorry. Really, Sam, I’m so sorry I didn’t tell you."
                    samantha.say "What the hell, [hero.name]? What were you thinking?"
                    hero.say "I was thinking that I wanted you to be happy. I didn’t want to let Ryan bring you down like that."
                    "She goes silent at that, and eventually sighs. Samantha sits next to me on the bed. I try not to look at her, until I hear a sob."
                    hero.say "Oh, Sam."
                    "I put an arm around her. She dives into my shoulder and cries."
                    samantha.say "What do I do, [hero.name]? I- I don’t know what to do anymore."
                    hero.say "Whatever you think is right. I want you to be happy. That’s all that matters."
                    "We stay there for a while after that. Her sniffles fill the room as the sun rises into the night, but I finally feel that weight lift off of my chest."
                    $ samantha.set_flag("storyE",1)
                    $ samantha.set_flag("storyB",0)
                    if "samantha" in HIDDEN:
                        $ HIDDEN.remove("samantha")
        "Say nothing":
            if samantha.get_flag_value("ryancheats"):
                "It’s better to not say anything."
                "If Ryan couldn’t handle it himself, then why should I be the one to break the bad news?"
                "His commitment issues were officially not my problem."
            samantha.say "[hero.name],"
            "I look up at the mention of my name."
            samantha.say "We need to talk."
            "I’m already dreading this conversation."
            hero.say "Yeah... I know."
            samantha.say "About Ryan-"
            hero.say "If you want to tell him about this, you can."
            hero.say "I won’t be mad. You can blame all of this on me."
            samantha.say "No, no! This is just as much my fault."
            samantha.say "I just... don’t know what to say. I feel guilty for betraying him like this, but I also want you."
            hero.say "... me?"
            samantha.say "Yes, you. I want all of this to work out. I don’t want anyone to be upset."
            "I especially don’t want you and Ryan to lose your friendship because of me."
            "‘Friendship’ is a strong word, but I don’t correct her."
            "She goes quiet, seemingly lost. I terrible idea pops into my head and I’m suggesting it before I can shut the fuck up."
            hero.say "You know what would help you guys fix things?"
            samantha.say "Hm?"
            hero.say "Mix things up. Tell him you want something new."
            samantha.say "Like what?"
            hero.say "How about a threesome?"
            "That might work, for Ryan at least. He can find another girl to take to bed with Samantha. That would probably peak his interest."
            samantha.say "..."
            "Did I overstep my bounds? Now that I think about it, Sam doesn’t want to hear about other girls-"
            samantha.say "Are you sure?"
            hero.say "Yeah, why not."
            samantha.say "You really think Ryan would be into that?"
            hero.say "I have no doubts."
            "Samantha stares at me, narrowing her eyes. I feel relieved that she didn’t get angry at my proposal."
            samantha.say "I guess I don’t mind... this could work."
            hero.say "Sweet."
            samantha.say "I... I’ll call him right now. I should see him at home!"
            hero.say "Uh, okay."
            samantha.say "Thanks, [hero.name]! I’ll let you know what he says."
            hero.say "You really don’t need to do that-"
            "She’s already gone, phone pressed up against her ear."
            "What have I done? Did I just tell Sam to have sex with more people that weren’t me? I should advocate for myself more often."
            "I ignore the feeling in the back of my mind that’s telling me it was a bad idea."
            if samantha.get_flag_value("ryancheats"):
                "Ryan would definitely agree, and he would probably bring along that girl I saw him with at the bar. Oops."
            $ samantha.set_flag("threesome",1)
            $ samantha.set_flag("storyC",1)
    return

label samantha_event_E01:
    $ samantha.set_flag("storyA",2)
    $ samantha.set_flag("storyE",2)
    $ samantha.set_flag("nodate",False)
    $ samantha.set_flag("nokiss",False)
    $ samantha.set_flag("divorced",True)
    $ samantha.set_flag("engaged",False)
    $ samantha_love_max = 170
    "My phone buzzes violently on my bedside table."
    "I’m already pulling on my clothes as I swipe the screen to check."
    "It’s Samantha. I pick my phone up and move to respond."
    "I don’t really know what to say."
    "She... wants to meet me at the park."
    "My eyes dart up to the time at the top of the screen."
    "I’ve got time."
    "I quickly accept."
    "She says thanks and doesn’t explain more than that."
    "I don’t ask for more, afraid she might back out if I pressure her."
    "Ever since I told her Ryan cheated, I’ve felt bad that I made her so upset- but a relief of weight I didn’t even know was there lifted off my chest the moment I admitted it."
    scene bg street
    "The second it’s time to meet Sam, I’m out the door and down the street in only a few minutes."
    scene bg park
    "I get to the park fast, and find myself panting as I get to the footpath leading into the area."
    show samantha
    "I spot Samantha’s golden hair easily."
    "It looks like she hasn’t found a spot to settle down yet."
    hero.say "Sam!"
    "She spins around, her eyes wide. We move towards each other and meet in the middle."
    samantha.say "..."
    samantha.say "Hi, [hero.name]."
    hero.say "Hey..."
    hero.say "How have you been?"
    samantha.say "Okay, I guess."
    hero.say "Good, good."
    "An awkward silence stretches between us. Samantha shakes her head lightly before looking up at me."
    samantha.say "Look, I’ll get to the point. I’m still upset that you didn’t tell me about Ryan sooner."
    samantha.say "But I want to thank you. You might not have told me at all, but you did."
    "I don’t respond, deciding to let her speak."
    samantha.say "And I... want to break up with him."
    hero.say "I- oh."
    hero.say "Really?"
    samantha.say "Yes, really. I don’t want to be with him anymore if he’s going around with other women. I... I didn’t want to believe it at first. But..."
    show samantha sad
    "Samantha starts to tear up and before I can even try to console her, she pulls herself together."
    hero.say "What?"
    samantha.say "I was heading out for work the other day. As I was leaving, I saw a girl at the door asking for him."
    samantha.say "Ryan said it was just a coworker who lived down the street looking to get a ride."
    samantha.say "But... it was the same girl in the picture you showed me."
    "Oh. She actually comes to their house? That’s... low."
    hero.say "Aw, I’m sorry, Sam."
    samantha.say "No, no. It’s okay. I should have seen it before."
    hero.say "There’s no way you could have. He just pretended to love you-"
    hide samantha
    show ryan casual angry
    ryan_say "Shut up!"
    "Samantha’s eyes move to look behind me and before I turn to look, I already know who it is."
    hide ryan
    show samantha angry
    samantha.say "Ryan?! Did you follow me here?"
    "Ryan’s face is red with anger. He ignores Samantha and comes straight up to me."
    hide samantha
    show ryan casual angry
    ryan_say "How dare you?! Why would you tell her? What the hell is wrong with you?!"
    hero.say "What’s wrong with me?"
    "As I talk, Ryan shoves at my shoulder, making me stumble back slightly."
    hide ryan
    show samantha angry
    samantha.say "Ryan! Stop it!"
    hero.say "You don’t deserve her."
    hide samantha
    show ryan casual angry
    ryan_say "Shut up! She’s my wife, you homewrecker!"
    "He shoves me again, but this time I expect it, not budging."
    hide ryan
    show samantha angry
    samantha.say "Ryan! We’re done! Are you even listening?!"
    hide samantha
    show ryan casual angry
    ryan_say "Shut it, Samantha!"
    "Ryan’s rage turns to her."
    menu:
        "Fight":
            "I don’t even have to think about it."
            "I pull my fist back and aim straight for his face."
            "He apparently doesn’t expect me to actually throw a punch, so it lands head on."
            "Ryan stumbles back, shock plastered on his now bloodied face. Red pours out of his nose and onto his lips. My knuckles start to sting and ache from the impact."
            if hero.fitness >= 50:
                "Ryan charges at me but I side step him before he can shove his elbow into me. I lift my foot and aim a hard kick at his side, making him step back and hunch over."
                "He recovers faster than I expect, gathering himself easily. Before he can come at me again, I rush forward and aim my fist right at his chest. It lands and his breath wheezes out painfully."
                "Ryan coughs and tries to get the air back. I roughly push him to the ground and he keels over submissively."
                hide ryan
                show samantha angry
                samantha.say "[hero.name]! Ryan! Stop, please!"
                "Sam’s voice breaks me out of my stupor. The adrenaline is rushing past my ears and making my arms shake, so I’m surprised I even heard her."
                "I back up, and Ryan stays on the ground. As he catches his breath, he glares up at me with unbridled hatred."
                show samantha
                "Samantha grabs my hand and starts to drag me away. I don’t fight it. We leave Ryan there, but I think he’s learned not to come near her again."
                hide samantha
            else:
                "Ryan charges at me and shoves his elbow into my ribs. I wheeze, feeling something crack on impact."
                hide ryan
                show samantha angry
                samantha.say "Stop! Please!"
                "I try to straighten but wince. A fist to the side straightens my back for me as my body twitches away. Another fist comes, but I manage to block with the side of my arm. Is it really blocking if you still feel the pain, though?"
                "I push back at Ryan as hard as I can. He slips on the mud under his feet and lands on his side. He hisses in pain and stands back up."
                "Before I can react, Samantha launches herself in front of me, arms out protectively."
                "Ryan doesn’t seem deterred, coming closer and raising his fist."
                "But at last he falters. His eyes soften at Sam and he lowers his arm."
                "Ryan shakes his head roughly and turns away. He stops for a long moment, looking like he wants to say something. And he leaves."
                "It’s quiet for a long moment before I sit down heavily on the ground, wincing at the ache in my ribs."
                show samantha
                samantha.say "[hero.name]! Oh my gosh... are you okay?"
                hero.say "It’s okay. I’m fine."
                "Maybe. I might have to stop by the clinic on the way back home, but I’m not going to die."
                samantha.say "I’m so sorry this happened!"
                "Sam looks like she’s about to burst into tears again and I can practically see the guilt blanketing over her."
                hero.say "Sam. This isn’t your fault. This is in no way your fault."
                "Sam shakily nods her head unconvincingly. She instead stares at me, searching for something."
                hero.say "What-"
                "I’m cut off as she leans forward, pressing her lips into mine."
                samantha.say "... Thank you."
                "It’s a whisper, but I hear her loud and clear."
                hide samantha
        "Leave":
            "I block his vision and back up."
            hero.say "Ryan. You need to calm down."
            ryan_say "Fuck you!"
            "I gesture for Samantha to start leaving and she takes the hint."
            hide ryan
    return

label samantha_event_C01:
    $ samantha.set_flag("storyC",2)
    $ samantha_love_max = 170
    play sound "sd/cell_vibrate.mp3"
    samantha.say "Hey, [hero.name]!"
    hero.say "hey"
    samantha.say "How’s your morning?"
    hero.say "fine. yours?"
    samantha.say "Good!"
    samantha.say "I have another question for you."
    hero.say "shoot"
    samantha.say "Do you like my piercings?"
    menu:
        "They’re great":
            $ samantha.love += 1
            hero.say "they’re fine with me. it’s sexy on you."
            samantha.say "Wow! Thanks <3"
        "I’d rather you not wear them":
            $ samantha.love -= 1
            hero.say "i don’t know. they don’t really suit you."
            samantha.say "Oh. Alright then."
    samantha.say "Hmm~"
    samantha.say "How many girls have you had sex with?"
    hero.say "..."
    hero.say "whoa. over text?"
    samantha.say "It’s important!"
    hero.say "well..."
    menu:
        "I can’t even count":
            $ samantha.love -= 1
            hero.say "i can’t really give a number. too many to count."
            samantha.say "Oh..."
        "A few":
            $ samantha.love += 1
            hero.say "a few here and there."
            samantha.say "Oh. Who?"
            hero.say "no."
            samantha.say "Okay. Sorry."
        "Just you":
            hero.say "Honestly, just you."
            samantha.say "..."
            samantha.say "Really?"
            samantha.say "That’s... so sweet, [hero.name]!"
            $ samantha.love += 2
    samantha.say "So."
    samantha.say "Do you mind incense or candles?"
    hero.say "sam?"
    samantha.say "Yes?"
    hero.say "why are you asking me all this?"
    samantha.say "Because I need to know! We all do!"
    hero.say "what??"
    samantha.say "My shift starts in a few minutes, I’ll have to talk to you later."
    "But let me know!"
    "..."
    "I don’t know what that’s supposed to mean. These questions about my... preferences haven’t stopped. At first, I was fine with answering them."
    "I thought she was mostly curious and I’m not going to say no if she wants to spend another night with me."
    "But now it’s a little too much. Maybe I should visit her once she’s done with work and ask her what this is all about."
    return

label samantha_event_C02:
    $ samantha_love_max = 180
    "The bakery has the usual smell; cinnamon, sugar, and freshly baked cakes."
    "It’s welcoming enough as I open the glass doors."
    "I don’t see Samantha at the counter- she must be in the kitchen today."
    "I check the time on my phone- only ten minutes until she’s off work."
    "I guess I can wait at one of the tables."
    "Before I take a seat near one of the windows,I order a small cup of coffee."
    "The chair lightly scrapes the floor as I pull it out and sit."
    "Now all there is to do it wait."
    show ryan casual annoyed
    ryan_say "You."
    "I look up. Ryan? What was he doing here?"
    hero.say "Me?"
    ryan_say "You."
    "He takes the chair at the opposite side of the table and sits. Um-"
    ryan_say "What do you think you’re doing?"
    "I blink slowly. I try to wrack my brain, thinking of anything I could have done wrong within the last week."
    "Other than fucking his wife, but it’s not like he doesn’t deserve it."
    hero.say "... Sitting?"
    "He doesn’t seem to like that response."
    ryan_say "No. Are you serious?"
    hero.say "Can you explain please?"
    "He leans in, as if to tell me a secret."
    ryan_say "You. You told Sam a threesome was a good idea."
    "Oh."
    hero.say "She was asking for advice."
    ryan_say "And you tell her shit like that?!"
    hero.say "It was just a suggestion, dude."
    ryan_say "And now she’s got it in her head that it’s a good idea!"
    hero.say "Are you of all people saying you wouldn’t be into a threesome?"
    ryan_say "Where the hell would you get the idea that I would want to do that with-"
    hide ryan
    show samantha
    samantha.say "Ryan!"
    "Sam appears at the side of our table, apron still on and flour dusting her cheeks. She notices me."
    samantha.say "[hero.name]! You’re here too?"
    hero.say "Yeah... I just wanted to talk to you."
    samantha.say "Oh! Me too."
    "She clasps her hands together and looks at me, as if waiting for me to start."
    hero.say "Uh...-"
    "It wouldn’t be a good idea to have this conversation in front of Ryan."
    hero.say "Maybe we could go somewhere more... private?"
    "Ryan looks like he wants to say something, but Samantha cuts him off."
    samantha.say "Sure! How about we all head home and we can talk there."
    hero.say "That seems a little-"
    hide samantha
    show ryan casual annoyed
    ryan_say "No. I agree. We can get a few things settled there."
    "I’m surprised when Ryan speaks. Now I was intrigued."
    hero.say "... Fine."
    ryan_say "Good."
    "He stands, a smug look plastered on his face. Samantha smiles at me and gets up after him."
    hide ryan
    show samantha
    samantha.say "Let’s get there!"
    "She grabs my hand and pulls me up, her touch lingering."
    hide samantha
    show ryan casual angry
    "Ryan’s smug expression turns into a glare."
    hide ryan
    scene bg street
    "We all pile into Ryan’s car- which I would never admit is nicer than mine but it is- and quickly make our way to their house."
    "The atmosphere is tense, almost making me want to leap out of the car at the next light."
    "Sam doesn’t seem to register it at all, tapping away on her phone with a satisfied smile."
    "We come to a stop in my driveway."
    "Ryan kills the ignition and immediately gets out."
    show samantha
    samantha.say "Let’s go!"
    "I nod, nerves starting to get to me. I get out anyway."
    hide samantha
    scene bg livingroom
    "We all get through the front door and pile into the living room."
    show samantha
    "Samantha gestures to the sofa."
    "I reluctantly take a seat."
    "Ryan sits across from me in the armchair with Sam next to me on the cushion."
    samantha.say "So-"
    hide samantha
    show ryan casual annoyed
    ryan_say "Are you stupid?"
    "I blink in confusion."
    "Ryan’s usually insulting me but most of the time with clear reason."
    hero.say "Um...?"
    "I look between both of them rapidly."
    hero.say "Are you seriously that upset about the threesome thing?"
    hero.say "Because you didn’t have to take that seriously-"
    ryan_say "Why the hell wouldn’t I take that seriously?!"
    hide ryan
    show samantha angry
    samantha.say "Ryan! When I said I wanted to us to talk with [hero.name] you said you would hear everyone out. Now is that time!"
    "Ryan deflates, leaning back in his chair."
    hide samantha
    show ryan casual annoyed
    ryan_say "Fine. Whatever."
    ryan_say "I just want to know... you’re not joking about this? You really want to? Because it’s not funny."
    "My brain whirs, trying to piece this together. What?"
    hide ryan
    show samantha
    "Samantha laces her fingers together and puts her hands on her lap."
    samantha.say "He was very serious! I was surprised too, but this is a good idea, Ryan!"
    "Oh."
    hero.say "Wait-"
    menu:
        "I’m interested":
            "That’s... not what I meant. Not at all. But if they’re really asking..."
            hero.say "Uh, yeah. I’m interested."
            "Samantha’s face softens."
            samantha.say "See! I told you he meant it."
            hide samantha
            show ryan casual annoyed
            ryan_say "..."
            ryan_say "Alright."
            hero.say "Alright?"
            ryan_say "Whatever. Sam has rules though."
            hide ryan
            show samantha
            samantha.say "It’s not rules! It’s more like... a checklist."
            hero.say "Wait. So is that why you’ve been asking me all those questions lately?"
            "Samantha sheepishly nods."
            samantha.say "I’m sorry. I didn’t make that sound very clear, did I?"
            samantha.say "But now that we’re all in agreement...!"
            "Sam takes a printed sheet out of her purse."
            "She hands it to me, and I take it gingerly."
            "I quickly scan it, and my eyes widen."
            "Pretty much all of the questions she’s asked me over the past few days are accumulated here along with other- and more medically inclined."
            "Stuff about past partners, STDs-"
            samantha.say "I want you to fill that back so Ryan and I can know how to go about things!"
            samantha.say "Once you do we can... schedule something when we’re all free."
            "As I look up from the sheet, Samantha winks at me. A shiver goes down my spine. Looks like I have homework."
            $ samantha.set_flag("storyC",3)
            hide samantha
        "That’s not what I meant":
            hero.say "No. No, no. That’s not what I meant. Not in a million years."
            "Sam’s eyes widen and the glare falls back onto Ryan’s face, though a hint of smugness comes with it too."
            hero.say "I meant- like- ya know? With another girl!"
            samantha.say "Another... girl?"
            "Samantha seems conflicted with that idea, as if it’s never occurred to her. She turns to Ryan with genuine curiosity."
            samantha.say "Would you...?"
            "She pauses, not knowing how to ask. Ryan seems to take this as a challenge."
            hide samantha
            show ryan casual angry
            ryan_say "Really?! You think I’d want to be with any other girl than Sam? You must not be paying attention, [hero.name]."
            ryan_say "Thanks, but no thanks- your advice is unnecessary."
            hero.say "Wait- are you-?"
            ryan_say "I think it’s best if you leave."
            hero.say "What?!"
            hide ryan
            show samantha sad
            samantha.say "Ryan! He didn’t mean it in a bad way!"
            hide samantha
            show ryan casual angry
            ryan_say "I don’t care, Sam! [hero.name], get out!"
            "I don’t need more of an invitation to leave. I promptly stand and head for the door."
            hero.say "See you later, Sam."
            "It comes out as a mutter to her but Ryan hears anyway."
            ryan_say "Uh, no, you won’t. Stay away from my wife."
            "Responses well up in my chest, begging to be let out. But I already made my decision."
            "I grab the door handle and shove it open. I quickly slam it behind me, wishing I could put more force behind it."
            "I take a deep breath as I stand on their porch. That was... awkward, to say the least."
            "Sam seemed to understand what I meant, but Ryan’s being an asshole."
            "What else is new?"
            hide ryan
    return

label samantha_event_C03:
    scene bg livingroom
    "I stand by the doorway awkwardly, waiting for my two guests to arrive."
    "I can’t remember the exact course of events leading up to this moment, in fact, I can’t quite convince myself that I’m not dreaming, but a cautionary pinch of my arm puts those fears to rest."
    "Time seems to be moving oddly slowly, the soft ticking of the clock in the background almost painful to hear."
    "Tick. Tick."
    "I briefly consider just taking it down, getting rid of the batteries to provide me some comfort, but I’m well aware I’d just end up checking my phone every few seconds anyway."
    "Tick. Tick."
    "That doesn’t mean I’m not annoyed of course, but I’m mostly just nervous. This is going to be… A weird, weird afternoon."
    "Tick. Tick."
    "Are they late? I can’t remember any-more whether she said three fifteen or three thirty, it doesn’t really matter I suppose, but..."
    "In place of the familiar tick of the clock, I hear someone at the door, hitting the doorbell before I could swing it open to face them."
    show ryan casual annoyed at right
    show samantha casual at left
    "Ryan and Samantha stand on the other side, Samantha’s finger still on the doorbell, and I quickly realise how awkward I look."
    "I offer a wavy smile to try and relieve the tension, Ryan shaking his head while Samantha returns it with a genuine grin that puts all my worries at ease."
    "The two quickly step inside and Ryan leads us to my bedroom before I could suggest anything else, he seems either overly eager to start, or get it over with."
    scene bg bedroom1
    show ryan casual annoyed at right
    show samantha casual at left
    "Samantha simply follows along, content to do as she’s told, and I don’t want to start an argument now of all times so I do the same."
    "There’s a few moments of silence when we all find ourselves by my bed, each of us knew exactly where this was going but it seemed like none knew how to start."
    hide ryan
    hide samantha
    show samantha kiss casual
    "Not wanting to let Ryan show me up, and also finding myself drawn irresistibly to Samantha’s lips by now, I step forwards and quickly pull her into a kiss."
    "I pull her body against mine, letting her press her mounds against my chest, letting me feel her heat radiating off her even through our layers of clothing."
    "She gasps but quickly begins to return my advances, leaving Ryan the neglected third wheel, a fact which pleases me greatly."
    "I let him watch as I touch and claim his mate, my hands gripping her waist tightly, venturing down to grope her ass through her clothing."
    "My hands knead and squeeze her curvaceous form as I push her forwards, nudging her closer and closer to the bed as Ryan can do nothing but watch."
    "Soon enough we topple over, landing with a pomf on the bedsheets, though we barely leave one another’s embrace, eventually parting only so I can begin lifting my shirt over my head."
    "I see Ryan step forwards out of the corner of my eye, mimicking my movements and planting his lips on Samantha’s mouth, and while she kisses back with passion, she’s soon turned her attention back to me as I begin undressing her too."
    "Her top is the first to go, her heaving breasts falling out into the open, protected only by her bra but I quickly rectify that problem, leaving her erect nipples to be tickled by the cool air."
    "I let my lips roam her flesh, trailing slowly down from her neck to her breasts and then lower still as I quickly slip the rest of her clothes from her body, drawing a yelp, a shudder, and a moan for my efforts."
    "I take my time exploring her, savouring her body, circling my tongue around her nipples even, leaving her soaking and needy in no time."
    "I lie back and let her return the favour, her fingers fumbling with my belt for a few moments but eventually dragging my pants from me in no time."
    "Her erect nipples brush tantalisingly against my naked chest, sending shivers down my spine before finally my cock is released from it’s denim prison."
    "I can tell from the sparkle in Samantha’s eyes alone that she wasn’t expecting my size, let alone her gasp when she’s suddenly face to face with my member."
    "I glance across to Ryan and find he’s stripped down too, and the sight of Samantha moaning and writhing, even if it was under my touch, has him similarly ready to go."
    "Looking to Samantha for guidance, I find her glancing between the two of us quickly, I can practically see the cogs turning in her mind for exactly what position she wants to adopt for the two of us."
    "Eventually, she seems to have made up her mind, motioning for Ryan to come closer as she began to straddle me, positioning her ass above my waist."
    "I lie back and wait, my cock twitching in anticipation in the open air."
    "It isn’t hard to see why she chose to straddle me over Ryan, I’m noticeably larger than he is down below and from the moment we arrived I’ve been fawning over her much more than he had."
    show samantha mmf
    "I shiver as her cunt lightly brushes up against my rod, and smirk as I watch her do the same, Ryan rushing over to her side and ungracefully thrusting his cock towards her face."
    "Samantha almost outright ignores him for a few seconds as she braces herself, looking down towards me and grinning."
    "Slowly, she let her hips fall, my cock pressing against her tight entrance for a few almost agonising moments before her slit relented, opening and letting me slip inside, her well lubricated tunnels immediately squeezing me tightly."
    "We both gasp, and after a few seconds to grow accustomed to the sensation, to the dripping juices running down my length, to the hot, fleshy walls milking my cock, I begin thrusting, pushing Samantha to start bouncing in place."
    "She does exactly that, her ass lifting and falling as her tits began bouncing in a way incredibly pleasing to the eye."
    hide samantha
    show samantha mmf ryan closed2 suck
    "As she does, she leans over and envelops Ryan’s length in one too, her nose quickly pushing down to tickle Ryan’s waist."
    "I focus more on the way her ass slaps into my legs with each bounce though, the way that if I pushed my hips forwards just right I could make her squeal with pleasure even now, just as we’ve gotten started."
    "Samantha seems to be enjoying herself already, and I certainly know I aim to please, so, gripping her waist, I slowly begin picking up the pace."
    "She moans and splutters around Ryan’s cock as I expertly pleasure her, her knees already beginning to waver and grow weak under my efforts."
    "I groan as I begin to lose myself in the sea of ecstasy Samantha has already thrown herself into, my cock sliding in and out with more ease after every thrust."
    "I can feel her pussy moulding to my shape, learning my cock’s size and form and milking it more effectively as a result."
    "Her flesh quickly relents under my grip as I play with her ass, giving it one or two playful slaps even as I thrust."
    "My hands send shock-waves through her body, her fat pooling in all the right places."
    "I let my other hand grasp her breasts, beginning to knead and play with them again, twisting and pulling her nipples in just the right way to make her moan around Ryan’s cock."
    "She’s clearly struggling to focus on the blowjob thanks to my ministrations, a fact I find flares a twisted sort of pleasure within me."
    "I begin to make it my effort to distract her as much as possible, to make her squeal and moan and whimper and anything else to stop her tongue with it’s no doubt expert service of Ryan’s pitiful member."
    "Her wet, sopping cunt suddenly finds itself the victim of my vicious attack as I suddenly begin thrusting furiously at different angles, varying my speed, finding the perfect spots to make her shudder and scream."
    "It doesn’t take long before Samantha is absolute putty in my hands, her pussy clamping down and spasming around my rod and her attention entirely focused on me rather than her husband."
    "He continues to thrust pitifully into her mouth but it’s clear that Samantha’s no longer servicing him with passion, instead focusing on pushing her weight down further on me, taking me deeper and deeper."
    show samantha mmf ryan mouth
    "Despite this Ryan is still the first to cum, shooting his small load down her throat then backing off to leave us to it."
    hide samantha
    show samantha mmf tongue
    "I can’t tell if Samantha is even aware of his absence any-more, but with nothing left to muffle them her cries fill the room more than ever."
    "We keep up our frantic, passionate lovemaking for a short while longer, but with each of us giving it our all, neither bothering to restrain ourselves in the slightest, it’s only a matter of time before orgasm arrives."
    show samantha mmf up
    "It hits fast and hard, my vision turning white as I pump my thick, sticky load into her womb, officially marking her as mine."
    "I feel her body tense, spasm as she lets loose one final cry, finally having pushed her over the edge."
    show samantha mmf pussy
    "As my cock twitches her pussy spasms, working to milk me for every last drop, granting me an orgasm so intense I very nearly pass out."
    "Eventually though, as all good things do, it comes to an end, Samantha collapsing on top of me and the two of us lying there, panting in each other’s arms."
    "I nearly forget about Ryan entirely until eventually, after recovering, Samantha pushes herself up and grins at him, telling him about what a good idea this had been and how much fun she’d had."
    "I smirk at him behind her back, and offer a cocky wink before he gets a chance to turn away, and soon enough, the two were gone, leaving me alone with my satisfaction."
    return

label samantha_event_B04:
    $ samantha.set_flag("storyB",5)
    $ samantha_love_max = 180
    $ HIDDEN.remove("samantha")
    $ samantha.set_flag("tellpregnant",2)
    play sound "sd/cell_vibrate.mp3"
    "..."
    play sound "sd/cell_vibrate.mp3"
    "It vibrates again."
    "Whoever it is can wait."
    "I shove the phone into my pocket..."
    scene bg livingroom
    "I can hear the rain from inside."
    "Where was my umbrella?"
    "I look around the front for a few moments before I conclude one of my roommates used it or lost it somewhere."
    "Sighing, I turn the knob and pull open the door."
    show samantha pregnant casual sad
    "..."
    samantha.say "... [hero.name]."
    "Samantha stands outside in the rain, barely covered by the porch roof."
    "Her hair is wet and her clothes are dotted with raindrops."
    "She’s shivering, arms wrapped around her middle."
    hero.say "Sam? What are you doing here?"
    "I didn’t really understand."
    "I was almost expecting to never see her again at this point."
    "But here she is."
    "Inspecting closer, I realize she probably walked here."
    samantha.say "I need to talk to you."
    "The idea of work flew out of my mind."
    "I stepped aside, letting her in. She was being..."
    "Unusually serious."
    "It was hard to tell if she was going to give me horrible news or not."
    "I start walking to the couch, figuring she’d want to sit down."
    "She stays by the door."
    "I stare at her for a few long seconds."
    samantha.say "I... um."
    samantha.say "I’m pregnant."
    "..."
    "What?"
    hero.say "Oh."
    hero.say "Congratulations."
    "It slips out before I can process what she even says."
    "Her lack of expression gives me the much needed time to come to terms."
    hero.say "Oh."
    "By the way she’s been talking about Ryan, it doesn’t sound like they’ve been spending a lot of personal time together."
    "Now that I think about it, we didn’t even use a condom."
    hero.say "You think it’s mine?"
    samantha.say "I don’t know."
    "I take a few steps closer to her."
    "It looks like she wants to back away and the wall behind her stops her."
    hero.say "Sam I-..."
    "What can I even say?"
    "It’s like I can physically feel my world crashing down around me."
    "Did I just... ruin Sam’s marriage?"
    "Or worse, her life?"
    "It’s no use thinking like this."
    hero.say "I’ll get you a towel."
    "Before she can say anything else, I rush to the linen closet and grab one of our fluffiest towels."
    "When I come back, she’s still standing in the same spot."
    "I hand it to her. Samantha takes it silently and holds it numbly in her hands."
    hero.say "What are you going to do with it?"
    samantha.say "What?"
    hero.say "I mean... do you have a plan?"
    samantha.say "I just ran here from my fucking home. Does it sound like I have a plan?"
    "I don’t think I’ve ever heard her swear before."
    "It sounds wrong coming out of her mouth."
    hero.say "I’m so sorry, Sam."
    samantha.say "I don’t want to hear it. This... I’m just as guilty as you. I can’t lie to Ryan- I won’t."
    samantha.say "I just want to know... if it really is yours, will you be here? Or am I going to be alone?"
    hero.say "Sam..."
    menu:
        "I’ll be there.":
            hero.say "Every step of the way, Samantha. I wouldn’t leave you like that."
            "Sam nods, tears finally falling from her lashes, mixing with heavy rain. She rushes forward and throws her arms around me."
            samantha.say "Thank you- thank you."
            hero.say "Here’s what we’ll do, okay? We’ll set up an appointment for you and get a real strategy. Then we can go from there."
            samantha.say "Okay."
            hero.say "Do you... want to keep it? With Ryan?"
            samantha.say "Keeping it? That’s not even a question. I can’t just get rid of it."
            samantha.say "It’s not some trash left over- this is a person. If Ryan wants one or not, I’m keeping it."
            hero.say "I- alright."
            play sound "sd/cell_vibrate.mp3"
            "My phone buzzes in my back pocket. I quickly turn my phone off."
            hero.say "Do you want to stay here? You could probably do with some de-stressing. Tea?"
            samantha.say "..."
            samantha.say "Sure."
            "Her sobs were subsiding the more we talked. Samantha’s face was contorted, trying not to have a full blown freak out."
            hero.say "I don’t want you to worry about Ryan, okay. I’ll take everything for you- we can say it’s my fault. That you weren’t in the right mind."
            samantha.say "No. I feel guilty enough. I have to tell Ryan, and I will."
            hero.say "Alright. If you need me there, I will be."
            samantha.say "Thank you."
            "I get Samantha settled on the couch and go to make tea for her."
            "As I grab spoonful after spoonful of sugar, I try not to overthink this, or think at all."
            "If it wasn’t mine, then there was nothing to worry about other than Ryan being pissed with me."
            if not samantha.get_flag_value("nocheat"):
                "At the same time, I still had dirt on him."
                "Pulling that out could result in a less than pretty black eye, but... okay, I’m definitely overthinking."
                "What Samantha needs is someone to lean on. If I had to be that person, then so be it."
        "There’s no way.":
            hero.say "Sam- what? There’s no way either of us can do this. Not even you and Ryan."
            hero.say "You’re still studying in university, I need roommates to pay for my house, and you just got married. Where is this money going to come from?"
            samantha.say "..."
            hero.say "I think you should work this out with Ryan. You two are a couple. You have parents that can help you out. It’s better if I stay out of this."
            samantha.say "Even if it’s yours?"
            hero.say "..."
            hero.say "I-"
            samantha.say "I get it. Goodbye, [hero.name]."
            "Before I can stop her, she’s back out the door, running down my street. I fucked up, didn’t I?"
    return

label samantha_are_you_sick:
    call samantha_greet from _call_samantha_greet_1
    samantha.say "Seriously, do something, you look like you are dying..."
    if samantha.love() > 80:
        samantha.say "You wants me to play doctor ?"
        $ samantha.love += 1
    elif samantha.love() > 120:
        samantha.say "I could be your sexy nurse..."
        $ samantha.love += 1
        if not samantha.get_flag_value("storyA"):
            samantha.say "Just kidding, don't get your hopes up."
    $ samantha.love += 1
    return

label samantha_buy_dress:
    show samantha
    "Samantha is looking at a sexy dress with hesitating eyes..."
    call samantha_greet from _call_samantha_greet_2
    samantha.say "That dress is gorgeous, but I can't afford it."
    if hero.money >= 100:
        $ result = renpy.display_menu([("Propose to buy it",1),("Say nothing",2)])
        if result == 1:
            hero.say "I'll get it for you..."
            if samantha.love() > 40:
                samantha.say "Thank you so much [hero.name] !"
                $ hero.money -= 100
                $ samantha.love += 2
            elif samantha.love > 20:
                samantha.say "I can't accept it but thanks for the offer."
                $ samantha.love += 1
            else:
                "Samantha smiles at me."
                samantha.say "Go get a girlfriend to buy clothes to instead of me."
                $ samantha.love += 1
        else:
            samantha.say "Maybe next month..."
            $ samantha.love -= 1
    else:
        samantha.say "It wouldn't be wise..."
    hide samantha
    return

label samantha_forgot_money:
    show samantha
    samantha.say "Fuck !"
    hero.say "What's up Samantha?"
    $ samantha.set_flag("greeting",True,"day")
    samantha.say "I forgot my money."
    if hero.money >= 50:
        $ result = renpy.display_menu([("Propose to help",1),("Say nothing",2)])
        if result == 1:
            hero.say "Don't worry, I'll pay for you."
            samantha.say "Thanks, you are a true friend."
            $ hero.money -= 50
            $ samantha.love += 1
        else:
            samantha.say "I'll have to make them write it on my tab..."
            $ samantha.love -= 1
    else:
        samantha.say "I'll have to make them write it on my tab..."
    hide samantha
    return

label samantha_kiss_me:
    call samantha_greet from _call_samantha_greet_3
    show samantha
    $ k = True
    if samantha.get_flag_value("storyA") and not samantha.get_flag_value("kiss"):
        "Samantha looks at me longingly."
        if not samantha.love() >= 160:
            $ k = False
    if not samantha.get_flag_value("kiss") and k:
        "Samantha seems to hesitate a little, then leans toward me, she obviously tries to kiss me."
        $ result = renpy.display_menu([("Kiss her",1),("Don't kiss her",2)])
        if result == 1:
            hide samantha
            show expression "samantha kiss "+samantha.get_clothes()
            "Samantha kisses me soflty but hungrily. The time stops for a few heartbeat."
            "Then we part..."
            hide expression "samantha kiss "+samantha.get_clothes()
            show samantha
            hero.say "What was that all about ?"
            if not samantha.get_flag_value("storyA"):
                samantha.say "Oh my god... Why did I do that... Ryan..."
            else:
                samantha.say "Face it tiger, you just hit the jackpot!"
            $ samantha.set_flag("kiss",1,"permanent","+")
            $ samantha.love += 1
        elif result == 2:
            "Samantha looks hurt when I push her away."
            $ samantha.love -= 1
    elif k:
        hide samantha
        show expression "samantha kiss "+samantha.get_clothes()
        "Samantha walks toward me and kisses me."
        hide expression "samantha kiss "+samantha.get_clothes()
        show samantha
        if not samantha.get_flag_value("storyA"):
            samantha.say "I should seriously stop doing that..."
        $ samantha.set_flag("kiss",1,"permanent","+")
        $ samantha.love += 1
    hide samantha
    return

label samantha_fuck_date:
    scene bg bedroom1
    show samantha
    play music "music/the_money_shot.mp3" loop
    if not samantha.get_flag_value("datesex"):
        $ samantha.set_flag("datesex",True)
        "Sam smiles with a sort of nostalgic whimsy as she casually strolls around my room."
        "Her hands behind her back, humming to herself a little."
        samantha.say "Oh, [hero.name], it’s like I never even moved. This room is just like before."
        if "luxury bed" in hero.inventory:
            hero.say "Hey, I changed got a new bed!"
            "She giggles. "
            samantha.say "Oh, silly, I meant just how you decorated. You haven’t changed one bit."
            hero.say "I thought that’s one reason you decided to go out with me."
            "She nods at that, her smile warm and genuine."
            samantha.say "Well, you aren’t wrong."
            samantha.say "But I also chose you because you are a solid foundation in this crazy world."
            samantha.say "And you know what?"
            samantha.say "I think you need a nice reward for being there for me during the tough times."
    hero.say "Well, Sam, we’re here. What would you like to do?"
    samantha.say "Oh, [hero.name],"
    samantha.say "Such a gentleman."
    samantha.say "But we’re in your house, so we get to do what you want."
    samantha.say "Though... let me give you something to think about first."
    show samantha naked
    "With that, she removes her clothes, letting me see her wonderful body underneath."
    if not samantha.get_flag_value("sex"):
        samantha.say "Sorry if the piercings look tacky..."
        samantha.say "Ryan... he had me get them."
        "Having lived with her for a bit, I could get glimpses here and there if I wanted, but to be the reason she undresses, hands behind her back to keep her arms from obstructing my view, that is a new feeling..."
        menu:
            "I like them":
                hero.say "Oh, not at all. They’re great!"
                samantha.say "Oh, I’m so glad you like them!"
                "she says, bouncing gently, which causes those wonderful breasts to jiggle delightfully."
                $ samantha.love += 1
            "I don't like them":
                hero.say "Yeah, maybe you should get rid of them."
                hero.say "Start fresh. Don’t worry, though, I’ll be gentle around there."
                samantha.say "Okay, [hero.name]. For you, I’ll get rid of them."
    $ samantha.set_flag("sex",1,"permanent","+")
    if samantha.get_flag_value("pregnant") >= 9:
        "Samantha’s already bountiful breasts swell with the burden of motherhood."
        "Her belly’s round and pregnant form almost enough to make fall just at how amazing she looks."
        samantha.say "You like it, [hero.name]?"
        samantha.say "This is all for you and all because of you."
        "She caresses her stomach, looking downward over her body."
        samantha.say "I’ll be a perfect mother, if that is what you want me to be, but for now, I’ll be your pregnancy fetish."
        "Well, then! I can’t say no to that. Let’s get going!"
        $ samantha.love += 1
    "I get undressed myself, knowing we won’t be needing clothes where we’re going."
    samantha.say "Just let me know what you want, and I’ll do it for you"
    hero.say "Come here. let’s see you use that mouth for something else other than praising me."
    "I lay back on the bed, my hands behind my head as I watch her."
    hero.say "Come and get my cock."
    hide samantha
    show samantha bj open
    if samantha.get_flag_value("pregnant") >= 9:
        "Samantha takes a deep breath and slides down in between my legs, going a little slowly as she carefully tries to keep her baby safe from any harm."
    "She brushes her fingers gently up along my thighs. Her large breasts squish against the mattress."
    "As she looks down over my already hardened shaft, ready to take her mouth."
    " But as she smiles down at it, she then looks up to me, the face she makes showing how her shy side melts away to a look of pure excitement and joy."
    samantha.say "[hero.name], let’s make this a little more interesting than a simple little blowjob."
    "Just as she says this, she lifts up a bit, cupping her hands under her motherly breasts and sliding my cock in between those warm and soft tits of hers."
    samantha.say "How does this feel? Do you like it?"
    "As she squeezes herself, the swollen and filled jugs swish around my cock with a heavier weight."
    if samantha.get_flag_value("pregnant") >= 9:
        "From her actions, little trickles of milk roll down, glistening her body and making a wet and sticky mess of my crotch."
    $ FACIAL = ""
    menu:
        "Mouth":
            hero.say "I want your mouth."
            "She giggles."
            samantha.say "Oh, I’m so glad to hear that!"
            "Then she sets off to work."
            "As she rubs her breasts up and down along my shaft, the hunger in her eyes is almost too much to bear."
            show samantha bj closed suck
            "She’s a thirsty girl, and she lets her tongue lick over my head."
            "She swirls over it a moment, getting the head nice and wet before she kisses me with those wonderful and soft lips of hers."
            "All the while as she does this, she glances up at me, making sure that I’m having a good time."
            "All the while, she lets out those loud and thirsty grunts, accenting each action with a louder, perhaps performance, moan."
            "Perhaps she is making sure I have a good time."
            "I am sure to let her know I am, and that only makes her go faster, to try harder."
            "Soon, a simple suckle goes into a full-blown suck as her cheeks collapse in from the vacuum pressure of her blowjob."
            "I groan, lifting my hips a bit as she quickens the pace of her tits, fucking my cock with her wonderful bouncy chest."
            "Soon, her focus becomes so powerful that she hungrily sucks me off as she squishes her body up against my own, her own growls and grunts rising up."
            if samantha.get_flag_value("pregnant") >= 9:
                "Her tits make a mess of my bed as she fondles herself, not seeming to care bout all that she spills out."
            menu:
                "Stop her":
                    hero.say "He... Hey!"
                    hero.say "Slow down a bit. I’m not done with you, yet!"
                    hide samantha
                    show samantha bj open
                    "She pulls her lips away with a smack and smiles, licking them as she pushes herself up."
                    if samantha.get_flag_value("pregnant") >= 9:
                        "She gives her sensitive breasts one last rub as she stands there."
                    samantha.say "Alright then. What do you want to do next? I’m ready to please!"
                "Don't stop her":
                    menu:
                        "Cum in her mouth":
                            "She just can’t be satisfied until my cock unleashes its cumload inside her throat, and I’m not one to displease such a lady."
                            show samantha bj suck cumshot both
                            "Her eyes roll back, her cries reach a fever pitch as I fire off into her."
                            "Soon, she pulls away, a sticky trail between my head and her lips as she shudders, wiping the remainder off of her chin."
                            samantha.say "Wow... [hero.name], you must have loved it! I’m so glad to make you happy!"
                        "Cum on her face":
                            "I reach for her hair, stroking her head tenderly."
                            hero.say "H.. Hey... get some air, already!"
                            "She obeys, pulling her mouth back with a pop."
                            "But what’s done is done, and I can’t hold back."
                            hide samantha
                            show samantha bj cumshot surprise
                            "Suddenly, ropey white strands of cum shoot out from my cock and over her face, staining her cheeks, nose, and lips. "
                            hide samantha
                            show samantha bj cumface
                            "She turns a bright red, but I smile down at her, offering her a hand."
                            samantha.say "Do you like seeing me like this [hero.name]? Well, I’m glad I could make you finish!"
                            hero.say "You look wonderful."
                            samantha.say "As long as you like it, I’d be happy to look like that. Alright?"
                            "I chuckle."
                            $ FACIAL = " facial "
                    hide samantha
                    if not hero.fitness >= 50:
                        $ samantha.love -= 5
                        $ samantha.sub -= 5
                        call samantha_sleep_date_fuck from _call_samantha_sleep_date_fuck
                        return
                    else:
                        $ samantha.sub += 1
        "Tits":

            "Laying back on the bed, I give her but one simple request."
            hero.say "I want to keep fucking them wonderful tits of yours."
            samantha.say "Oh, you really like these tits, don’t you [hero.name]?"
            samantha.say "Is ths what you really want?"
            if samantha.get_flag_value("pregnant") >= 9:
                samantha.say "Is this why you got me pregnant? You just wanted me to get larger and lactate, is that right?"
                hero.say "Well, it’s certainly not something I dislike about knocking you up!"
                samantha.say "Then, I’m happy to give it to you. Oh, so very happy!"
            "Samantha scoots in, her large breasts squishing up against my body."
            if samantha.get_flag_value("pregnant") >= 9:
                "Little squirts of milk rolling down her chest as she settles in, making sure not to harm the baby as she gets up against the bed."
                "She slides her hands over to the sides of her wondrous mounds, squeezing the soft and supple flesh, wincing slightly as those sore and swollen mounds are played with, and lining up both sides to wrap around my hardened pole."
                "Her breasts are warm and soft and nearly envelope my entire shaft, but they feel so wonderful having become so heavy with mother’s milk."
                "She shifts and rolls those beauties with her fingers, groping herself in the process, spreading the staining milk over her body as she lets her skin slide up and down along my own."
            else:
                "She slides her hands over to the sides of her wondrous mounds, squeezing the soft and supple flesh, and lining up both sides to wrap around my hardened pole."
                "The pressure of the weighted breasts only add to my pleasure, and they nearly envelope my whole cock, but she keeps the head poking out, perhaps as a tease."
                "She shifts and rolls those beauties with her fingers, groping herself in the process."
            samantha.say "You feel so wonderful, [hero.name]. I’m so happy I get to please you with these!"
            menu:
                "Don't stop her":
                    "There’s no way a guy like me could ever compete with tits like those."
                    "Try as I might, she’s just too wonderful, running those amazing breasts up and down my meat, showing off the kinkiness of her lactating beauties."
                    "What else would happen but me erupting all over her!?"
                    hide samantha
                    show samantha bj cumshot
                    "My cum spurts up all over her face and covers between her tits, but despite all that, she doesn’t get mad."
                    show samantha bj cumface cumchest
                    "She gasps, then she smiles, and she pulls away."
                    samantha.say "I’m so happy I could make you enjoy that, [hero.name]."
                    $ FACIAL = " facial "
                    if not hero.fitness >= 50:
                        $ samantha.love -= 5
                        $ samantha.sub -= 5
                        call samantha_sleep_date_fuck from _call_samantha_sleep_date_fuck_1
                        return
                    else:
                        $ samantha.sub += 1
                "Stop her":
                    hero.say "Samantha... you’re wonderful. Just... please, hold back a moment."
                    "Samantha frowns, pulling her wonderful breasts away from my body."
                    samantha.say "Aw, [hero.name], did I... did I disappoint?"
                    hero.say "No! Not at all! Just that. I want to do so much more with you!"
                    samantha.say "W... what? Oh my! Of course! What though?"
    if hero.has_condom():
        menu:
            "Use a condom":
                $ CONDOM = " condom "
                $ hero.use_condom()
            "Do it raw":
                $ CONDOM = ""
    else:
        $ CONDOM = ""
    menu:
        "Fuck her doggy":
            $ BLINDFOLD = ""
            $ BEADS = ""
            $ DILDO = ""
            "I push myself up, sitting on the bed on my knees."
            hero.say "Come over here. Crawl up on the bed."
            samantha.say "Oooh, yes, sir, [hero.name]!"
            show expression "samantha doggy none"+FACIAL
            "Samantha says, making her way to the middle of the mattress, palms running along the sides of the bed to get her bearings..."
            samantha.say "I can guess what we’re doing now!"
            if samantha.get_flag_value("pregnant") >= 9:
                "The way her belly and her tits accent her profile makes the submissive position all the more hot."
            if "anal beads" in hero.inventory or "dildo" in hero.inventory or "blindfold" in hero.inventory:
                menu:
                    "Use some toy":
                        menu:
                            "Anal beads" if "anal beads" in hero.inventory:
                                call samantha_date_fuck_beads from _call_samantha_date_fuck_beads
                            "Dildo" if "dildo" in hero.inventory:
                                call samantha_date_fuck_dildo from _call_samantha_date_fuck_dildo
                            "Blindfold" if "blindfold" in hero.inventory:
                                call samantha_date_fuck_blindfold from _call_samantha_date_fuck_blindfold
                    "Don't use toys":
                        hero.say "You’re probably right,"
            else:
                hero.say "You’re probably right,"
            show expression "samantha doggy out"+FACIAL+BEADS+BLINDFOLD+DILDO+CONDOM
            "I shuffle around her and soon face her from behind."
            hero.say "Always want to do it doggy style. You ever done it before?"
            samantha.say "For you, I’ll do anything!"
            "She looks over her shoulder with that devoted smile she always have and nodding quickly, grabbing the covers in her anticipation."
            "So, I go in, looming over her, my arms wrapping around her body."
            if samantha.get_flag_value("pregnant") >= 9:
                "I grab onto her tits, fondling them, squeezing them, letting the milk spill out and roll over my fingers and over her skin."
                "She gasps, pushing her chest out, her nipples hardening under my palms as I work my way over her. "
                samantha.say "Aah, [hero.name] milk me... I’m so swollen!"
                "Once I am done with her tits, I slide my sticky and wet hand downward, drying myself off over her smooth and supple skin."
                "Soon, my palm finds its way over her pregnant body, and I swirl my hand over the mound I had made within her."
                "New life, created by me!"
                "The perfect biological achievement a man can accomplish, and within a mother who would do anything for me."
            $ FUCK = ""
            menu:
                "Pussy" if not DILDO:
                    "Meanwhile, my cock rests between her asscheeks."
                    show expression "samantha doggy"+FACIAL+BEADS+BLINDFOLD+DILDO+CONDOM
                    "I slide the length down between those wonderful curves, soon finding her womanhood."
                    "With a thrust, I take her, and she squeaks as I penetrate."
                    "My chest presses up against her naked back, our bodies warming each other as I rut away like a wild animal."
                    if BEADS:
                        menu:
                            "Take the beads out":
                                call samantha_date_fuck_beads_out from _call_samantha_date_fuck_beads_out
                            "Don't":
                                pass
                    show expression "samantha doggy"+FACIAL+BEADS+BLINDFOLD+DILDO+CONDOM
                    "She lifts her hips against my body, grinding away as if she is in heat herself, and perhaps, in a way we are."
                    if samantha.get_flag_value("pregnant") >= 9:
                        "Which, for a pregnant woman, would make her quite the insatiable monster!"
                    "It has been a long time coming, and I’m glad I get to have her."
                "Ass" if not BEADS:
                    $ FUCK = " anal "
                    "My cock rests between her asscheeks before I slide the length down between that crack of hers."
                    show expression "samantha doggy "+FUCK+FACIAL+BEADS+BLINDFOLD+DILDO+CONDOM
                    "She squeaks as my cock presses itself up against her hole."
                    samantha.say "Ah,[hero.name], my ass?"
                    hero.say "Your ass is mine"
                    samantha.say "Mmm, yes, you’re right. It is yours. All of my body is. All for your pleasure!"
                    "I take that pleasure, thrusting inside of her, spreading her apart as I fill her forbidden hole."
                    if DILDO:
                        menu:
                            "Take the vibrator out":
                                call samantha_date_fuck_dildo_out from _call_samantha_date_fuck_dildo_out
                            "Don't":
                                pass
                    show expression "samantha doggy "+FUCK+FACIAL+BEADS+BLINDFOLD+DILDO+CONDOM
                    "I press up against her naked back, our bodies heated in our animialistic fucking."
                    "This is for my own pleasure, but her groans underneath of my body prove that she too loves taking it up the ass, even if it is for my own desires."
                    "She lifts her hips up, begging for more, and I give it, plunging deeper into her."
            menu:
                "Cum inside":
                    "With a few more thrusts, I soon find myself slamming up into her."
                    hero.say "I’m going to cum now, Samantha."
                    samantha.say "Oh, [hero.name], please!"
                    show expression "samantha doggy cumshot"+FUCK+FACIAL+BEADS+BLINDFOLD+DILDO+CONDOM
                    if CONDOM:
                        "With a gasp, I soon find myself releasing, spurting out into the condom as I hold her down."
                        "She’s mine now, and she smiles, her cheek against the bed, drooling."
                        "I pull out, the rubber filled with my creamy goodness as I look over my conquest with a satisfied grin."
                    elif samantha.love <= 180 and samantha.get_flag_value("pregnant") < 6 and not FUCK==" anal ":
                        $ samantha.love -= 20
                        samantha.say "Ugh...ugh...you...you came in me!"
                        samantha.say "...you came inside of me!"
                        "I'm still in her when she says this."
                        hero.say "What can I say...I wanted you to have something to remember me by!"
                        "Sam surprises me by giving me a swift slap across the face and dragging herself out from under me."
                        samantha.say "Asshole - it'd serve you right if you got me pregnant!"
                        if not samantha.get_flag_value("pill") and not samantha.get_flag_value("pregnant") and not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills) and not FUCK==" anal ":
                            $ samantha.set_flag("pregnant",1)
                    else:
                        "With a gasp, I soon find myself releasing, spurting out into her as I hold her down."
                        "She’s mine now, and she smiles, her cheek against the bed, drooling."
                        "I pull out, her hole filled with my creamy goodness as I look over my conquest with a satisfied grin."
                        if not samantha.get_flag_value("pill") and not samantha.get_flag_value("pregnant") and not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills) and not FUCK==" anal ":
                            $ samantha.set_flag("pregnant",1)
                    $ CUM = ""
                    show expression "samantha doggy none"+CUM+FACIAL+BEADS+BLINDFOLD+DILDO
                "Cum outside" if not CONDOM:
                    show expression "samantha doggy cumshot out "+FACIAL+BEADS+BLINDFOLD+DILDO+CONDOM
                    "Finding myself ready, I pull myself out, but I don’t leave her with nothing."
                    "When I release, I shoot off onto her lower back and her butt, making her glisten with my expulsions."
                    if samantha.get_flag_value("pregnant") >= 9:
                        "After all, I’ve already conquered her inside, why not mark her outside?"
                    $ CUM = " asscum bodycum"
            show expression "samantha doggy none "+CUM+FACIAL+BEADS+BLINDFOLD+DILDO
            "After holding onto her a bit, I whisper into her ear."
            hero.say "You like it when I take control?"
            samantha.say "Oh, I like it when you’re happy!"
            hide expression "samantha doggy none "+CUM+FACIAL+BEADS+BLINDFOLD+DILDO
        "Fuck her missionary" if "samantha_event_B01" in DONE:
            if not CONDOM:
                show samantha miss pussy
            else:
                show samantha miss condom
            if FACIAL:
                show samantha miss cumface
            "When I push myself into Sam, it's slowly and gently, so that I can feel every moment of the experience."
            "Looking down on her as I do so, I can see the sensations spreading through her entire body at the same time."
            "My thrusts and motions are not translated into painful or taxing pangs, but rather they seem to create sympathetic ripples in her."
            "Sam moves beneath me in harmony, enjoying every moment of my presence inside of her."
            "At one moment her eyes are closed in seeming bliss, the next they open slowly and regard me with an almost sleepy delight."
            "As beautiful as I thought she was before this, she becomes even more so as she betrays her intimate pleasure through the expression upon her face."
            "Sam begins to massage her breasts again, reminding me of the sensation this gave me, even whilst my cock is deep inside of her."
            show samantha miss closedeyes
            "She's panting now, building steadily in terms of her own pleasure."
            "Locks of her dirty-blonde hair begin to fall across her face as she rolls her head."
            "I can see sweat standing out on her forehead, neck and chest - a bead rolling over the curve of her belly."
            "Suddenly, all of these elements come together, and I see Sam in her entirety, become aware of how deep I am and how desperate she makes me."
            "That's it - I can't hold back any longer!"
            if CONDOM:
                "That little bit of foresight now means that I can stay right where I am as I finally cum."
                "My muscles jerk and buck, translating the physical manifestation of my orgasm into yet more pleasure for Sam."
                "She feels every last moment of my climax, clinging tightly to me as I try to push yet further into her."
                "I'm flattered and delighted in equal measure when she begins to cum herself."
                "We end together, slick with each other's sweat and still entangled in every way possible for two human bodies to be united as one."
            else:
                menu:
                    "Pull out":
                        "Somehow, despite the chaos going on inside of my head, I manage to remember to pull out before I cum."
                        "Sam writhes and moans in disappointment as I do so, her hands instinctively flying to her pussy to keep herself going."
                        show samantha miss normaleyes outside
                        "All I can do now is kneel over her and watch as my cum spatters down and over her."
                        show samantha miss normaleyes outside2
                        "Belly, breasts and face all get their fair share of the droplets, and Sam yelps in surprise as she's showered."
                        "But she soon recovers her composure, wiping the cum over her breasts and belly with one hand, even as she brings herself off with the other."
                    "Cum inside":
                        "I can sense from Sam's body language that she's suddenly aware of the fact that I'm on the brink and inside of her without protection."
                        "She begins to wriggle and squirm beneath me, as if trying to sepeaate herself from me before I can lose it."
                        "But by this time she's so entangled with me that she simply can't manage to escape of her own volition."
                        "And I'm not about to oblige her by stopping what I'm doing in order to climb off of her either."
                        samantha.say "Ah...ah...you're going to...cum inside of me..."
                        "The desperation in her voice means that her words have the opposite effect to what she intended."
                        "A second later, I lose myself in her."
                        if not samantha.get_flag_value("pill") and not samantha.get_flag_value("pregnant") and not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills):
                            $ samantha.set_flag("pregnant",1)
                        if samantha.love <= 180 and samantha.get_flag_value("pregnant") < 6:
                            $ samantha.love -= 20
                            samantha.say "Ugh...ugh...you...you came in me!"
                            samantha.say "...you came inside of me!"
                            "I'm still in her when she says this."
                            hero.say "What can I say...I wanted you to have something to remember me by!"
                            "Sam surprises me by giving me a swift slap across the face and dragging herself out from under me."
                            samantha.say "Asshole - it'd serve you right if you got me pregnant!"
                        else:
                            show samantha miss cumeyes inside
                            samantha.say "OH FUCK!"
                            samantha.say "OH YES...FUCK ME...PLEASE!!!"
                            "Funny, that's what I thought I'd been doing!"
                            "Far from being mad at me for cuming inside of her unprotected, Sam seems to be swept away by the feeling."
                            "She's kneading her breasts like they were balls of dough."
                            "And her legs are wrapped around me so tight that it's actually getting a little hard to breathe."
                            "She's not going to let go or stop demanding to be pleasured until she cums herself."
                            "So I hurry to oblige."
                            "By now I'm almost pushing Sam back into the pillows and the headboard, starting to feel fatigue creeping into my limbs."
                            "Luckily, she's almost there, and just needs that last push over the edge."
                            show samantha miss ahegao
                            "She cums with her head half-buried in the heaped pillows so that her cries are almost muffled and lost beneath them."
    scene bg bedroom1
    show samantha naked
    "Both of us lay collapsed upon the bed, an entire session where I was in full control spending both of us."
    "She smiles as she turns towards me, and gives me a great hug, pressing her chest up against my body."
    samantha.say "Oh, did you enjoy yourself?"
    menu:
        "Yes":
            hero.say "You bet, I did! You were great!"
            samantha.say "Oh, you’re so wonderful. Thank you."
            "She says, sighing, nuzzling up to me and just enjoying our time together."
            $ samantha.love += 1
        "No":
            hero.say "Actually, it wasn’t all that good, really."
            samantha.say "W... what?"
            hero.say "Yeah, you were just so bland, not wanting to please yourself, just wanting to please me."
            hero.say "Where’s the spirit?"
            samantha.say "I..."
            "She goes silent."
            hero.say "Well, that’s that, I guess, unless you want to do something else..?"
            samantha.say "I’m... I’m going to have to think about it."
            "she turns away, curling up in my bed."
            $ samantha.love -= 5
    hide samantha
    call samantha_sleep_date_fuck from _call_samantha_sleep_date_fuck_2
    return

label samantha_date_fuck_blindfold:
    hero.say "I want to try something a little different now, too. Take a look at this!"
    "With that, I reach over towards my drawer, pulling out a blindfold."
    "Samantha bites her lip at the sight of it."
    samantha.say "You want to blind me, [hero.name]?"
    hero.say "It’ll heighten your pleasure and I’ll get to do whatever I want without you seeing what it is."
    if samantha.sub >= 10:
        samantha.say "Oh, oh my..."
        "I reach around her head, putting the cloth over her face. She sighs as I tie it around the beack of her head."
        hero.say "There you go, can you see?"
        samantha.say "Nothing at all!"
        $ samantha.sub += 1
        $ BLINDFOLD = " blind "
    else:
        samantha.say "Maybe some other time."
    return

label samantha_date_fuck_beads:
    "I clamber away, pulling out the set of anal beads from my drawer."
    "Samantha lets a curious coo out as I tell her my plan."
    if samantha.sub >= 20:
        hero.say "Spread your legs. Your ass, too"
        "She spreads apart, reaching down over her thighs, her fingers digging into her cheeks."
        "She pulls them apart, showing off her puckered pink star."
        samantha.say "H-here it is, [hero.name]. I hope its not too terrible for you."
        hero.say "Oh, it’s perfect."
        "I pour the lube over the beads, making them glisten."
        hero.say "Just keep holding on. I’m coming in."
        "The beads glisten in my hand as I get down in front of the bed."
        "Samantha breathes steadily, waiting for what is to come."
        "First comes the smallest bead, which meets resistance."
        "Samantha gasps, her toes curling, her body shuddering."
        "I roll the bead around her hole a moment before I push in."
        "Her ass swallows it, and she tilts her head back, sighing happily."
        samantha.say "[hero.name], it’s inside., I-"
        "I push the next one up against her hole, larger than the first."
        "She bites her lip and squeals as she feels it forcing its way inside, but after a moment of coaxing, Samantha swallows it up."
        samantha.say "Do... do you like seeing my ass take your beads, [hero.name]?"
        "I answer her by adding in the next one."
        "One after another, larger and larger beads make their way inside her body."
        "Her mouth hangs open as she takes in those beads, until finally, we are done, leaving her with a trail of beads sticking out of her ass."
        $ samantha.sub += 1
        $ BEADS = " beads "
    else:
        samantha.say "Maybe some other time."
    return

label samantha_date_fuck_beads_out:
    "It’s time to take the beads out, I think, so I grab hold and prepare for extraction."
    menu:
        "Rough":
            "With a tug, I yank the beads back."
            "Multiple little balls plop out in quick succession."
            "Samantha screams as she fels her body expel the little spheres and then she falls to the bed, her hands gripping the sheets."
            samantha.say "O... oh fuck! [hero.name] so rough!"
            $ samantha.sub += 1
        "Gentle":
            "One at a time, I pull the beads out."
            "Just like when it took them in, Samantha’s exit spreads, letting the shining bead spit out of it."
            "I pull gently once the first on exits, but each successive one comes out easier and easier, until finally, I pull out the final one, placing the beads aside and getting a nice look at Samantha’s open hole."
            samantha.say "Ah... [hero.name] that was so nice..."
            $ samantha.love += 1
    $ BEADS = ""
    return

label samantha_date_fuck_dildo:
    hero.say "Spread your legs."
    "She does as I command."
    hero.say "Let me see how much you want me."
    "She understands me, her fingers pressing against her moistened lips, spreading them apart and giving me a view of her wanting womanhood."
    hero.say "Amazing,"
    samantha.say "[hero.name], This is just for you, as long as you want it."
    hero.say "Oh, I want it, alright."
    "I say, pouring a little bit of lube over the massive plastic dong."
    hero.say "But I’m not going to take it, not yet."
    "She shudders at that, feeling the ominous air around her over the vibrator."
    "I soon take it, pressing the tip into her wanting warmth."
    "It eagerly swallows it up, her walls stretching to accomodate its amazing size."
    "With a cry, she reaches down, wrapping her hands around it."
    samantha.say "Aah, [hero.name]!"
    "Go ahead, put it in... keep it in, but first..."
    "I flip the switch, and the buzzing fills the air of my room."
    "Immediately, Samantha squirms around under the shock of the intense stimulation."
    hero.say "And you’re going to keep it inside you until I tell you to pull it out. Got it."
    samantha.say "Y... yes, [hero.name]!"
    $ samantha.sub += 1
    $ DILDO = " dildo "
    return

label samantha_date_fuck_dildo_out:
    hero.say "Samantha, it’s time to pull it out."
    samantha.say "Ah.. Ah, thank you. I don’t... mmm, I don’t think I could have lasted much longer."
    "Samantha reaches down with one hand, gripping onto the soaked, humming plastic."
    "With a final loud gasp, she pulls it free, letting it roll and clatter to the floor, a sloppy mess."
    "This leaves Samantha there, panting heavily, her tongue out, looking like a horny animal. "
    samantha.say "Ah... ah.... J... just for.... For you...!"
    $ DILDO = ""
    return

label samantha_sleep_date_fuck:
    scene bg bedroom1
    if not samantha.get_flag_value("pregnant") > 6 or samantha.get_flag_value("tellpregnant"):
        show samantha naked
        samantha.say "Mm.. want me to spend the night?"
        menu:
            "No":
                $ r = False
                hero.say "No, you shouldn't; I have to get up early tomorrow,"
                "The sex was beyond incredible."
                "Frowning a little, Sasha straightens and shrugs, then goes to collect her robe from where she'd let it fall earlier."
                samantha.say "Alright. Sleep well."
                "She then heads up the stairs."
                $ samantha.love -= 3
            "Yes":
                $ r = True
                hero.say "Absolutely."
                "I say, my voice a little shaky."
                "I pull out with a reluctant sigh, then turn toward the bed."
                "We curl up spooning together in bed, drifting toward sleep."
                samantha.say "Sweet dreams."
                hero.say "You too."
                $ samantha.love += 3
        $ renpy.call_in_new_context("sleep")
    else:
        $ renpy.call_in_new_context("sleep")
        "When I come to, my head feels heavy."
        "The soft sheets underneath me slowly bring my sleep addled mind forward."
        "I open my eyes, blinking rapidly and see the ceiling of my room."
        "When did I fall asleep?"
        show samantha naked
        "A body shifts next to me- Samantha."
        "She ended up curled into my side, gripping my arm."
        "She must have fallen asleep too."
        "Seems like she’s waking up."
        samantha.say "[hero.name]?"
        hero.say "Hmm...?"
        "All I can do it grunt in response while trying to rev up the motor to my mouth."
        "She shakes me."
        samantha.say "[hero.name]?"
        hero.say "Yeah? What?"
        "I rub a hand across my eyes, then the rest of my face, forcing myself to wake up."
        samantha.say "I have to go to work in a few minutes."
        "The bed shifts and she slips off the side, raising her arms above her head in a stretch."
        samantha.say "Thanks for letting me stay over."
        "I sit up."
        hero.say "Yeah, no problem."
        show samantha
        "Sam shoves on her shirt and starts to look for her bag."
        hero.say "It’s by the door."
        samantha.say "Oh! Thanks!"
        "She picks it up and slings it over her shoulder. I guess it’s time to start the day. Unfortunately. I move to get to the bathroom, wanting to get in before Sasha."
        samantha.say "Hey... [hero.name]?"
        "I look over at Sam who’s hesitating by the door. She’s having trouble looking me in the eye."
        hero.say "What’s up?"
        samantha.say "How do you feel about... kids?"
        menu:
            "They’re okay":
                "That’s a weird question. But..."
                hero.say "They’re alright. It’s not like I know any?"
                samantha.say "Oh..."
                show samantha happy
                "She suddenly smiles, looking much more confident."
                samantha.say "That’s not what I meant but... I’m glad to hear that."
                "With that, she opens the door and leaves."
                hero.say "... Okay?"
                $ samantha.set_flag("tellpregnant",1)
                $ samantha.love += 1
            "I love them":
                "That’s a weird question. But..."
                hero.say "I love kids."
                samantha.say "Great!"
                show samantha happy
                "She suddenly smiles, looking much more confident."
                samantha.say "I’m glad to hear that."
                "With that, she opens the door and leaves."
                hero.say "... Okay?"
                $ samantha.set_flag("tellpregnant",1)
                $ samantha.love += 5
            "I can’t stand kids.":
                $ samantha.love -= 10
                hero.say "Kids are... not my thing. I can’t really stand them."
                "Samantha’s lips purse. Otherwise I can’t read her expression, but her tone gives it away."
                show samantha angry
                samantha.say "Oh... okay then."
                "She makes a move to leave, but I stop her."
                hero.say "Wait! What’s wrong?"
                "She lets her bag drop back to the ground and crosses her arms. This can’t be good."
                samantha.say "You know I want kids... someday... right?"
                "Oh yeah. I think she mentioned that at some point. Maybe when she was still with Ryan? And she’s always wanted to be a children’s book author too."
                hero.say "We can... figure something else out."
                samantha.say "What?!"
                "I wince when she raises her voice. Her eyes look sad and her eyebrows are angry."
                samantha.say "Are you serious?! What does that even mean?"
                hero.say "What?"
                samantha.say "‘Figuring something else out’. What is that supposed to mean?"
                "She makes air quotes with her fingers as she repeats what I said."
                hero.say "Well... ya know. We could always get a dog. Or a cat?"
                "This just seems to upset her more."
                samantha.say "A dog is not the same thing as a baby!"
                hero.say "You’re right. A dog is a lot quieter."
                "Her mouth falls open, as if she’s offended."
                samantha.say "I can’t believe you right now!"
                hero.say "I’m sorry, Sam. I just don’t want kids. Is that so bad?"
                samantha.say "I’m pregnant!"
                "Her shout cuts through the tense room air. What?"
                hero.say "You’re what?"
                "Samantha angrily picks up her bag and forcefully opens it. She digs around for a moment before pulling something out and throwing it at me. It hits me in the chest."
                samantha.say "I think I need some space."
                "Samantha mutters before leaving. I don’t stop her this time."
                "Numbly, my fingers reach for the white stick she threw at me. I instantly know what it is."
                "I quickly turn over the pregnancy test and my heart falls through my chest."
                "Two stripes."
                $ samantha.set_flag("tellpregnant",2)
    return

label samantha_preg_talk:
    $ samantha.set_flag("tellpregnant",2)
    "A knock on the front door gets my attention."
    "I want to ignore it and don’t move for a few long seconds. But the knocking persists."
    hero.say "Alright, alright."
    "I reluctantly rise from my spot on the couch and head to the door. I flip the gold painted lock and come face to face with Samantha."
    hero.say "Sam?"
    "She stands on the porch with soft eyes and small, white box in her hands with the bakery logo."
    show samantha
    samantha.say "Hi! I’m sorry, I didn’t tell you I was coming over, did I?"
    samantha.say "I got super caught up at work! Is this okay?"
    "She already knows what I’m going to say."
    hero.say "Yeah, sure. Come on in."
    "I stand aside and hold the door wider, letting her walk in. She seems a little nervous, clutching at her box tighter."
    hero.say "What’s that?"
    "I gesture to her box."
    samantha.say "Oh. Just something I made at work."
    samantha.say "It’s for you!"
    "Sam shoves the box at me after I shut the door. I fumble but take it from her."
    samantha.say "I’m going to get some water!"
    "She exclaims before heading to the kitchen. This all seems... suspicious."
    "I start to follow behind her but slow as I open the lid. I come to a full stop."
    "Inside is a rather large cupcake, the top covered in two colours of icing- one half is pink and the other is blue. A white question mark is painted on the middle."
    hero.say "..."
    hero.say "Sam?"
    "I pick up the pace, getting to the kitchen. Sam is waiting at the counter, cheeks dusted red and waiting for me. On the surface in front of her is a long, white stick."
    hero.say "Are you...?"
    "I can’t seem to form words. I know what’s happening, I just can’t seem to process it."
    samantha.say "[hero.name]... I’m pregnant!"
    "She taps a perfect nail on the pregnancy test and two little pink stripes stare back at me."
    hero.say "This is..."
    "I don’t know what to say."
    menu:
        "Hug Her":
            show samantha happy
            $ samantha.love += 5
            "I rush forward and gather her into my arms. She seems surprised at first but melts into me."
            samantha.say "... So you’re okay with all this?"
            hero.say "Hell yes, I am."
            "Sam pulls away and the warmth is gone. But once I see her happy tears, the warmth blooms in my chest this time."
            samantha.say "You’re going to be a great father, [hero.name]!"
            samantha.say "Thank you..."
            "She goes back into my arms and I hold her. A future children’s book writer, baker, and beautiful girlfriend? She would be a great mother, too."
        "Back Away":
            show samantha sad
            "Panic rises in my chest as soon as I get over the shock. My hands shake and I shift away from her."
            "Samantha’s face visibly falls."
            samantha.say "[hero.name]?"
            hero.say "I- I’m sorry. Is this what you meant the other morning?"
            samantha.say "... Yeah, I just... maybe I should have told you then."
            "I set the cupcake down on the counter next to the positive pregnancy test."
            samantha.say "W-What’s wrong?"
            hero.say "I just..."
            "I don’t really know how to word this."
            hero.say "I don’t really think we’re ready for this."
            "Samantha seems sad but has a spark of understanding in her eyes. Her mouth twitches as she struggles for a response."
            samantha.say "Maybe... but we can become ready for it. I’m willing to try."
            hero.say "What if it doesn’t work out?"
            "Samantha steps forward and takes my hand, gripping it tightly. Her fingers are warm."
            samantha.say "I won’t let it not work out. If we’re both willing to try, we can do anything."
            "I look down, but she doesn’t let my eyes reach the floor."
            samantha.say "Please? Try for me. I promise everything will be okay."
            "I stare back at the sloppy cupcake on the counter. Globs of icing hang off the side and the question mark is shaky. She must have really been worried about coming to me with this."
            hero.say "Alright. Let’s do it. We can do it."
            show samantha happy
            "Sam’s face lights up with joy. She lurches forward and wraps her arms around my neck. I catch her, squeezing her back."
        "Tell her it's probably Ryan's":
            hero.say "Are you sure it's not Ryan's?"
            show samantha angry
            samantha.say "[hero.name]!"
            samantha.say "You fucking jerk!"
            hero.say "I think you should leave..."
            hero.say "I am pretty sure it's not mine."
            samantha.say "I never thought you would do that..."
            show samantha angry
            samantha.say "I never want to see you again!"
            $ HIDDEN.append("samantha")
            $ hero.smartphone_contacts.remove("samantha")
            $ samantha.set_flag("storyA",100)
            $ samantha.set_flag("storyB",100)
            $ samantha.set_flag("storyC",100)
            $ samantha.set_flag("storyD",100)
            $ samantha.set_flag("storyE",100)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
