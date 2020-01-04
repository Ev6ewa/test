layeredimage bg gym:
    always:
        "gym"

init -2 python:
    Room(**{
        "name":"gym",
        "hours":(10,20),
        "display_name": "Gym",
        "exits": ["map", "mma"],
        "alternate_exits": ["map","mma"],
        "required_item": "sport clothes",
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"sport"
        })


    Activity(**{
        "name": "buymembership",
        "duration": 0,
        "money_cost": 50,
        "icon":"membershipcard",
        "game_conditions": {"flag_gymmember":0, "room":["gym"]},
        "display_name": "Buy a membership",
        "label": ["buymembership"]
        })

    Activity(**{
        "name": "train_hard",
        "energy": -2,
        "grooming": -2,
        "fitness": 4,
        "icon":"workout_hard",
        "duration": 3,
        "game_conditions": {"min_energy":5,"min_hunger":5,"min_fun":5,"flag_gymmember":True, "room":["gym"]},
        "display_name": "Heavy training",
        "label": ["training"],
        "say": [
                "Lifting lead... Well has long has it increases my chances to get laid.",
                "34... 35... 36... 37... 38...\nOh shit !",
                "I love watching women train while I do my own training, it's like the smell when you are cooking."
                ]
        })

    Activity(**{
        "name": "train",
        "energy": -1,
        "grooming": -1,
        "fitness": 2,
        "icon":"workout",
        "duration": 2,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_fun":3,"flag_gymmember":True, "room":["gym"]},
        "display_name": "Light training",
        "label": ["training"],
        "say": [
                "Well, I am more hanging out here than training...",
                "Time for a sweat."
                ]
        })

    Event(**{
        "name": "gym_out",
        "label": ["gym_out"],
        "duration": 0,
        "priority": 1000,
        "required_item":"not_sport clothes",
        "game_conditions": {
            "room":["gym"],
            },
        "do_once": False,
        "once_hour":False,
        })

    Activity(**{
        "name": "work_gym",
        "money_gain": (["fitness"],(0.5,)),
        "duration": 4,
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"flag_job":"gym","room":["gym"]},
        "display_name": "Work",
        "icon":"work",
        "say": [
            "Working the desk at the gym is nowhere near as much fun as working out at the gym."
            ]
        })

    Event(**{
        "name": "ayesha_teaser",
        "label": ["ayesha_teaser"],
        "duration": 0,
        "game_conditions":{"room":["gym"], "flag_female":0, "days":"3"},
        "girls_conditions": {"hanna":{"present":True, "valid":True}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })        

label ayesha_teaser:
    scene bg gym
    "You always notice a new face at the gym, and for the most part, all they justify is a quick glance on account of their novelty."
    "Okay, if it's a particularly cute girl or a guy that you're instantly jealous of."
    "Then you might sneak a couple more glances when you think they're not looking."
    "But on this occasion, I was quite literally stopped in my tracks by the sight of someone new."
    "I tend to avoid the boxing ring and the matts where the meatheads and MMA freaks work-out."
    "Maybe it's just me, but there's not much in it for me watching a pair of angry, buzz-cut guys in lycra shorts grinding on each other."
    "So this means that when I walk by that part of the gym, I'm usually not really paying much attention."
    "I can see that there are two people sparring in the ring right now."
    "One's a regular that I vaguely recognise from among the other angry buzz-cut guys in shorts."
    "The other's hidden by the first guy, and all I can see of them is that they're pretty much handing him his own ass in there!"
    show ayesha teaser normal
    "It's only when I get further away that I can see the other person sparring is actually a girl."
    "But what a girl!"
    "She must be at least six feet in height and built like an amazon."
    "Dressed in black lycra shorts and a bra-top, her dark brown skin is slick with sweat from exertion, and her ebony braids whip back and forth as she moves."
    "I watch transfixed, as she demolishes the formidable guy she's sparring with, taking him apart piece-by-piece."
    hide ayesha
    show hanna teaser normal
    hanna.say "Like watching a lioness toy with her next meal, isn't it?"
    "I tear my eyes away from the action in the ring and see that Hanna's walked up beside me while I was distracted."
    hero.say "Uh...yeah...that pretty much sums it up!"
    "Hanna chuckles and shakes her head at my evident fascination."
    hanna.say "For the record, her name's Ayesha."
    hanna.say "She only just started training here about a week or two ago."
    hanna.say "And word in the locker-room is that most of the beefcakes are already afraid of stepping into the ring with her!"
    "I shake my head as I look back to see the guy in the ring go down under a flurry of blows."
    "And then I gulp in genuine astonishment as I see Ayesha follow him down, sit astride his chest and begin to pummel him on the ring canvas."
    hero.say "She's...she's quite something!"
    hero.say "What is she - some kind of MMA fighter or martial artist, or something?"
    "Hanna shrugs at the question, shaking her head again."
    hanna.say "I don't know about any of that stuff."
    hanna.say "But someone that's had the privilege of being on the receiving end of her ground and pound told me that she's a wrestler."
    hero.say "A wrestler?"
    hero.say "Which kind - amateur or fake?"
    "Hanna looks me in the eye before she answers, her expression becoming serious for a moment."
    hanna.say "The latter - but I wouldn't let her hear you call it that!"
    "I shrug, sure that I can't possibly be overheard while Ayesha's still sparring."
    hero.say "Fake then - strange when she looks so tough in there!"
    hide hanna
    "Hanna rolls her eyes at my dismissive comment and walks away, leaving me standing alone again."
    "I take a last look round the gym and turn to head for the showers."
    ayesha_say "HEY, FUCK-FACE!"
    show ayesha teaser angry
    "I turn around, an expression on my face that makes me look like I've been slapped hard with a wet fish."
    ayesha_say "Yeah, you - don't stand there with that dumb look on your fucking face!"
    ayesha_say "Who else am I gonna be shouting at, asshole?!?"
    "I continue to gape silently as I see Ayesha striding towards me, pulling off her MMA gloves with a face like thunder."
    ayesha_say "You're a little man with a real big mouth, you know that?"
    "Oh shit - did she actually hear what I just said?"
    ayesha_say "Where in the hell to you get off calling how I make a living fucking FAKE?!?"
    "As if there's a need to underline the fact that she did hear me just now, Ayesha thumps me in the chest with the flat of her hand."
    "I'm not prepared for the strength of the blow at all, and it sends me staggering back a couple of feet."
    "The pain is pretty bad, but I feel like she's also knocked the air out of my lungs too."
    "I just have enough time to see her advancing on me again and make up my mind as to what my next move should be."
    menu:
        "Stand up to her":
            "I've been abused, verbally and physically, in front of the entire gym, which makes me see red."
            "As Ayesha comes towards me, I pull myself up and meet her with all the force that I can muster."
            hero.say "Back off, you muscle-bound bitch!"
            "I make sure to get in her face as much as possible as I say this, trying to ignore the good few inches that she has on me in height."
            hero.say "This is the twenty-first century, in case, being a throwback cavewoman, you hadn't noticed."
            hero.say "Don't think for a second that I won't fight back if you pick a fight with me!"
            show ayesha teaser normal
            "Though she doesn't back down one iota at this, I see a slight raise of an eyebrow and the hint of a smile from Ayesha."
            ayesha_say "Is that so?"
            ayesha_say "Well, maybe next time you think about running your dick-licker around me, you should keep it shut and see me in the ring instead?"
            ayesha_say "Think about it, tough guy!"
            hide ayesha
            "And with that, she breezes past me towards the women's locker-room."
            "I rub the back of my neck, puzzling over her sudden change in attitude."
            "Was she really that mad, or was she just feeling me out to see if I'd stand up for myself?"
        "Apologise":
            "Ayesha looks so powerful and imposing as she towers over me that I can't help but cower away from her."
            hero.say "Okay, okay...I'm sorry for what I said!"
            hero.say "It was dumb of me, and I just didn't think...please don't hurt me!"
            "I look at Ayesha from behind the shield of my own hands."
            "And I'm surprised to see her angry expression soften as she looks at me."
            hero.say "Please...I don't know any martial arts or wrestling stuff..."
            show ayesha teaser blush
            ayesha_say "It's okay, I'm not going to hurt you."
            ayesha_say "I was just...mad...that's all."
            "As the anger leaves her face, I begin to see how beautiful Ayesha actually is up close."
            "She has deep, dark eyes and a sensual mouth that's somehow a little sad in its aspect."
            ayesha_say "You should keep comments like that to yourself, you know?"
            "I nod hesitantly."
            ayesha_say "Whatever you might think about wrestling, it's what I do to put food on the table, man."
            ayesha_say "It might not be as legit as you like your fights to be, but it's fucking hard on the body."
            "I nod furiously, and she nods once to acknowledge my own."
            hide ayesha
            "All of that said, she walks past me, towards the women's locker-room."
    "Once I'm showered and changed, I hurry out of the gym, hoping not to bump into Ayesha a second time."
    "But as I pass the reception desk, Hanna calls me over, waving something in her hand."
    show hanna
    hanna.say "Hey, Ayesha asked me to give you these!"
    "I take what she's holding out to me, already dreading just what they might turn out to be."
    hanna.say "It's tickets to her next wrestling show - front row as well."
    hanna.say "I guess someone made an impression on our resident amazon, eh?"
    "I can't help but groan, both at the look on Hanna's face and the prospect of seeing Ayesha wrestle."
    "But do I really have a choice of whether to go along to the show or not?"
    return

label gym_out:
    "I need to buy a training outfit to be able to come here."
    $ game.room = "map"
    return

label buymembership:
    $ game.set_flag("gymmember", True, 7)
    return

label training:
    python:
        hero.fun += hero.fitness()/20-1
        successes = []
        for girl in ROOMS["gym"].get_present_girls():
            if hero.fitness()*2 > girl.love:
                successes.append(girl)
                girl.love += 1
    if successes and hero.fitness >= 10:
        if len(successes) == 1:
            "[successes[0].name] can't takes her eyes off mewhile I workout."
        else:
            "The girls can't take their eyes off me while I workout."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
