layeredimage bg date_pub:
    always:
        "pub"

init -2 python:
    Room(**{
        "name":"date_pub",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "Pub",
        "hours": (20,24),
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Date(
        "pub",
        display_name="pub",
        money_cost=30,
        game_conditions={"valid_room":"date_pub"},
        clothes = "casual",
        love_gain = 2,
        )

    Activity(**{
        "name": "date_play_darts",
        "duration": 1,
        "fun":1,
        "icon": "darts",
        "display_name": "Play darts",
        "game_conditions": {"room":["date_pub"]},
        "label": ["date_play_darts"],
        "once_day": True
        })


    Activity(**{
        "name": "buy_a_round",
        "duration": 1,
        "fun":1,
        "icon": "round",
        "money_cost":50,
        "display_name": "Buy a round",
        "game_conditions": {"room":["date_pub"]},
        "label": ["date_buy_a_round"],
        "once_day": True
        })

    Activity(**{
        "name": "date_pub_play_pool",
        "duration": 1,
        "fun":1,
        "icon": "pool",
        "display_name": "Play pool",
        "game_conditions": {"room":["date_pub"]},
        "label": ["date_pub_play_pool"],
        "once_day": True
        })

    Activity(**{
        "name": "eat_a_burger_date",
        "duration": 0,
        "hunger": 7,
        "money_cost": 25,
        "icon":"burger",
        "once_day": True,
        "game_conditions": {"min_hunger":0,"room":["date_pub"]},
        "display_name": "Eat a burger",
        "label": "eat_a_burger_date"
        })

label date_pub_random_events:
    scene bg park
    show expression date_girl.id
    $ r = randint(1,10)
    if r <= 1:
        "After a while, I notice a girl at the next table smiling at me."
        "The fact that I'm clearly on a date doesn't seem to discourage her in the least."
        "[date_girl.name] seems to have noticed her attentions too."
        menu:
            "Blow the other girl off":
                hero.say "Can you believe this girl!"
                hero.say "Is she shameless or what?"
            "Flirt back":
                hero.say "Hey there, were you trying to get my attention?"
                hero.say "Because it's all yours right now!"
                if date_girl.has_trait("submissive"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] blushes at the sight of me paying attention to another girl in front of her."
                    "But she just smiles helplessly and watches all the same."
                elif date_girl.has_trait("yandere"):
                    $ game.set_flag("datescore",10,1,"-")
                    $ date_girl.set_flag("yandere",1,mod="+")
                    "[date_girl.name]'s eyes flare with anger at the mere sight of the other girl as she flirts with me."
                    "But I'm relieved to see that almost all of her ire is directed at the girl, rather than me!"
    elif r <= 2:
        "The table across from us suddenly goes from being empty to filled by a couple and their noisy kids."
        "[date_girl.name] glances over at the ensuing chaos and din, and then back at me."
        menu:
            "Suggest moving":
                hero.say "Urgh...maybe we should move somewhere a little quieter?"
                if date_girl.has_trait("family"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] looks at me as though I just said something offensive, and slowly shakes her head."
                elif date_girl.has_trait("not_family"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] nods in agreement, smiling more than a little at my annoyance."
                else:
                    "[date_girl.name] shrugs, as if she's not particularly bothered either way."
            "Fawn over the kids":
                hero.say "Aww, it must be so rewarding to have kids!"
                if date_girl.has_trait("family"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] gives the little family an adoring gaze and then another one to me."
                elif date_girl.has_trait("not_family"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] frowns, looking at me like I have smoking turds hanging out of my mouth."
                else:
                    $ game.set_flag("datescore",5,1,"-")
                    "[date_girl.name] shakes her head, as if saying she couldn't care less."
    elif r <= 3:
        "Waiting to be served at the bar, a girl jumps ahead of me as soon as the bartender asks who's next."
        "[date_girl.name] stares at the queue-jumper and then looks at me, clearly wondering if I'm going to let it go."
        menu:
            "Protest":
                hero.say "Excuse me - I think you'll find I was ahead of you!"
                if date_girl.has_trait("dominant"):
                    $ game.set_flag("datescore",10,1,"+")
                    "The girl looks surprised and apologises, making [date_girl.name] smile and give me a look of approval."
                elif date_girl.has_trait("bitchy"):
                    $ game.set_flag("datescore",10,1,"+")
                    "The girl seems taken aback and lets me go before her, but [date_girl.name] eyes her up and makes a huffy, disapproving sound all the same."
                else:
                    "The girl apologises and steps aside, but [date_girl.name]'s face says that I could have just let the matter drop."
            "Let it go":
                hero.say "Whatever - the place isn't that busy anyway."
                if date_girl.has_trait("dominant"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] shakes her head, as if annoyed at my not standing up for myself."
                elif date_girl.has_trait("bitchy"):
                    $ game.set_flag("datescore",10,1,"-")
                    "The queue-jumper gets her drinks before us, but [date_girl.name] deftly manages to elbow one of them over without being seen."
                    "As we walk away from the bar, I see [date_girl.name] grin at getting her revenge."
                else:
                    $ game.set_flag("datescore",5,1,"-")
                    "[date_girl.name] shakes her head."
    elif r <= 4:
        "We're chatting away when the weekly pub quiz begins in the background."
        "[date_girl.name] cocks her head at the first question, as if she's trying to come up with an answer."
        menu:
            "Answer seriously":
                "I know this one, so I just come straight out with the answer."
                if date_girl.has_trait("bookworm"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] looks at me with a smile, genuinely impressed with my show of knowledge."
                elif date_girl.has_trait("dumb"):
                    $ game.set_flag("datescore",5,1,"+")
                    "[date_girl.name] looks at me like she's surprised I know the answer."
                else:
                    "[date_girl.name] shrugs, as if she's not really that interested."
            "Answer jokingly":
                "I know this one, but I'd rather joke around, so I make a rude answer up instead."
                if date_girl.has_trait("bookworm"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] tuts and looks away, evidently finding my clowning childish."
                if date_girl.has_trait("dumb"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] laughs out loud, almost spraying me with a mouthful of her drink."
                else:
                    $ game.set_flag("datescore",5,1,"-")
                    "[date_girl.name] gives me a token smile, but doesn't seem all that impressed."
    elif r <= 5:
        "The drinks in front of us are getting dangerously close to being finished."
        "[date_girl.name] drains the last of hers and then looks at the empty glass and back at me."
        menu:
            "Offer to buy the next round":
                "I got the first round of drinks, but what the hell - I feel like treating her."
                hero.say "The next round's on me, okay?"
                if date_girl.has_trait("princess"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] practically beams at me, clearly loving that she's being spoiled."
                elif date_girl.has_trait("rebel") or date_girl.has_trait("dominant"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] looks at me like I'm patronising her, but doesn't object."
                else:
                    "[date_girl.name] nods casually, pointing to her glass to tell me she wants the same again."
            "Tell her it's her round":
                hero.say "I got the first drinks in, so these are on you!"
                if date_girl.has_trait("princess") or date_girl.has_trait("dominant"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] frowns and shakes her head - clearly she'd been expecting me to pick up her tab all night!"
                elif date_girl.has_trait("rebel"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] scoops up the glasses and heads for the bar without pause or hesitation."
                else:
                    $ game.set_flag("datescore",5,1,"-")
                    "[date_girl.name] shrugs and gets up, making her way to the bar."
    elif r <= 6:
        "Don't ask me how it comes up in casual conversation, but somehow I mention that I have a head-banger of a day awaiting me at work tomorrow morning."
        "[date_girl.name] glances down at the line of empty glasses already spread out before me and raises her eyebrows."
        menu:
            "Screw work":
                hero.say "But hey, fuck work, am I right?"
                if date_girl.has_trait("rebel"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] gives me a conspiratorial smile and holds up her drink for an impromptu toast."
                elif date_girl.has_trait("workaholic"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] shakes her head, as though she's watching the gradual descent of an alcoholic."
                else:
                    $ game.set_flag("datescore",5,1,"-")
                    "[date_girl.name] looks surprised at my comment and shakes her head with a smile."
            "I should be reigning it in":
                hero.say "Speaking of which, maybe I should switch to soft drinks from here on?"
                if date_girl.has_trait("rebel"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] rolls her eyes, clearly finding my comment utterly lame."
                elif date_girl.has_trait("workaholic"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] nods in approval, a new-found respect for me clear to see in her eyes."
                else:
                    "[date_girl.name] shrugs and shakes her head, as if to say 'whatever'."
    elif r <= 7:
        "I can smell the food the pub's serving, and it's making me ever more hungry with every passing moment."
        "Tossing [date_girl.name] a menu, I suggest that we order something."
        menu:
            "I want junk food":
                hero.say "I don't care what we get, so long as it's deep fried and covered in cheese!"
                if date_girl.has_trait("trashy"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] nods and smiles at this, as if I just read her mind."
                elif date_girl.has_trait("gourmand"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] looks at me in askance, as if I just suggested that we order road-kill in BBQ sauce."
                else:
                    "[date_girl.name] waves her hand to and fro, as if not convinced she wants exactly the same thing as I do."
            "I hope this is all ethically sourced":
                hero.say "I'm worried whether the food here is ethically sourced - nothing on the menu says that it is!"
                if date_girl.has_trait("trashy"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] looks confused, like I've suddenly started speaking a foreign language."
                elif date_girl.has_trait("gourmand"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] nods approvingly, wrinkling her nose as she sees that my concerns about the menu are legitimate."
                else:
                    $ game.set_flag("datescore",5,1,"-")
                    "[date_girl.name] smiles at me, her face saying that she thinks I'm being a little too fussy."
    elif r <= 8:
        "We've already made the mistake of sitting too close to the massive TV mounted on one of the pub's walls."
        "And when it erupts into life [date_girl.name] shoots me a glance as we both realise it's about to show a football game."
        menu:
            "Sweet, I love football":
                hero.say "Wow, that's lucky - I thought I was going to miss this game!"
                if date_girl.has_trait("sportsy"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] has to practically drag her eyes away from the pre-match hype."
                    "But when she finally does, it's to flash me a look of obvious approval."
                elif date_girl.has_trait("geek"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] glances around the pub, as if she wants to look at anything other than the TV...and me."
                else:
                    $ game.set_flag("datescore",5,1,"-")
                    "[date_girl.name] looks a little put out at the intrusion of the TV, but not like she's about to say so."
            "Why is it always bloody football":
                hero.say "Can you tell me why it's always football on in pubs, not an episode of Star Trek or some Star Wars film?"
                if date_girl.has_trait("sportsy"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] snorts at this and shakes her head, her look of disbelief questioning my manhood."
                elif date_girl.has_trait("geek"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] throws her hands up in the air and nods emphatically, as if I'm the first person ever to agree with her on this matter."
                else:
                    "[date_girl.name] shrugs, as though she thinks my suggestion would be nice, but also that it's not going to happen any time soon."
    elif r <= 9:
        "Checking my wallet before I go to the bar to get the next round in, I notice that I don't have any condoms in there."
        "When I get up and walk in the direction of the bathroom and not the bar [date_girl.name] raises her eyebrows, clearly wondering where I'm going."
        menu:
            "Admit to buying condoms":
                hero.say "I just realised I'm out of condoms - going to grab some from the machine in the men's room."
                if date_girl.has_trait("slutty"):
                    $ game.set_flag("datescore",10,1,"+")
                    "A flithy smile spreads across [date_girl.name]'s face, as she clearly likes the sound of where this is going."
                elif date_girl.has_trait("innocent"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] looks at me with a shocked expression, as if she's surprised such thing would even be on my mind right now."
                else:
                    "[date_girl.name] gives me a wry sideways glance and shakes her head, amused at my apparent confidence as to just how well the date is going."
            "Claim to need the bathroom":
                hero.say "Ah...just need to make a little space before I down another one!"
                if date_girl.has_trait("slutty"):
                    "[date_girl.name] waves me off as though she couldn't really care less."
                elif date_girl.has_trait("innocent"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] nods and smiles sweetly, clearly swallowing the excuse hook, line and sinker."
                else:
                    $ game.set_flag("datescore",5,1,"-")
                    "[date_girl.name] frowns and shakes her head, laughing at the fact that I've already given more information than she wanted."
    elif r <= 10:
        "I put the drinks down on the table and then fumble my change back into my wallet, but it's only then that I realise I've been short-changed at the bar."
        "[date_girl.name] sees what I'm doing and the expression on her face tells me that she instantly gets what's happened."
        menu:
            "Blow it off":
                hero.say "Ah, it's only a couple of bucks - who cares, right?"
                if date_girl.has_trait("poor"):
                    $ game.set_flag("datescore",10,1,"-")
                    "[date_girl.name] shakes her head, as though she doesn't appreciate me being so casual about money."
                else:
                    "[date_girl.name] shrugs indifferently, at my attitude towards my own money."
                    return
            "Go back and rectify the error":
                hero.say "Sorry, but I need to go back to the bar and see if they'll put this right."
                if date_girl.has_trait("poor"):
                    $ game.set_flag("datescore",10,1,"+")
                    "[date_girl.name] nods and smiles in agreement, clearly impressed at my frugality when it comes to money."
                else:
                    "[date_girl.name] shrugs and nods, not particularly concerned about my penny-pinching habits."
    hide expression date_girl.id
    return

label eat_a_burger_date:
    show expression "date pub burger "+game.active_girl.id
    if renpy.has_label(game.active_girl.id+"_eat_a_burger_date"):
        call expression game.active_girl.id+"_eat_a_burger_date"
    else:
        "We eat a burger together."
    hide expression "date pub burger "+game.active_girl.id
    if game.active_girl.has_trait("gourmand"):
        $ game.set_flag("datescore",5,1,"+")
    $ game.set_flag("datescore",5,"day","+")
    return

label date_buy_a_round:
    show expression "bar "+game.active_girl.id
    if renpy.has_label(game.active_girl.id+"_date_buy_a_round"):
        call expression game.active_girl.id+"_date_buy_a_round"
    else:
        "I pay a round of beers to the whole pub."
    hide expression "bar "+game.active_girl.id
    if game.active_girl.has_trait("rebel"):
        $ game.set_flag("datescore",5,1,"+")
    $ game.set_flag("datescore",5,"day","+")

    return

label date_pub_play_pool:
    show expression "pool "+game.active_girl.id
    if renpy.has_label(game.active_girl.id+"_date_pub_play_pool"):
        call expression game.active_girl.id+"_date_pub_play_pool"
    else:
        "We play a few games."
    if game.active_girl.has_trait("playful"):
        $ game.set_flag("datescore",5,"day","+")
    hide expression "pool "+game.active_girl.id
    return

label date_play_darts:
    show expression "date pub dart "+game.active_girl.id
    if renpy.has_label(game.active_girl.id+"_date_play_darts"):
        call expression game.active_girl.id+"_date_play_darts"
    else:
        "We play a few games."
    if game.active_girl.has_trait("playful"):
        $ game.set_flag("datescore",5,1,"+")
    hide expression "date pub dart "+game.active_girl.id
    return

label date_pub:
    show expression game.active_girl.id
    "We go to the pub."
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
