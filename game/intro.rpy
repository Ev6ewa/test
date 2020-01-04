label showroom:
    scene bg livingroom
    python:
        import time
        p = "a"
        for t in ["", "pregnant", "boobjob", "boobjob haircut pregnant"]:  
            for o in ["casual","casual2","date","rope","rpg","sexyswimsuit"]:
                for e in ["blush", "normal"]:
                    renpy.show("sasha "+p+" "+t+" "+o+" "+e, at_list=[right])
                    if not o in ["casual2", "rope"]:
                        renpy.show("bree "+p+" "+o+" "+e, at_list=[left])
                    elif o == "casual2":
                        renpy.show("bree bowsette joke", at_list=[left])
                    renpy.pause(0.1)
                    renpy.hide("sasha "+p+" "+t+" "+o+" "+e)
                    renpy.hide("bree bowsette joke")
                    renpy.hide("bree "+p+" "+o+" "+e)

        p = "b"
        for t in ["", "haircut", "boobjob haircut"]:  
            for o in ["swimsuit", "sleep", "sport", "towel", "underwear", "naked"]:
                for e in ["happy", "angry","sad"]:
                    renpy.show("sasha "+p+" "+t+" "+o+" "+e, at_list=[right])
                    if not o in ["casual2", "rope"]:
                        renpy.show("bree "+p+" "+o+" "+e, at_list=[left])
                    renpy.pause(0.1)
                    renpy.hide("sasha "+p+" "+t+" "+o+" "+e)
                    renpy.hide("bree "+p+" "+o+" "+e)
    return


label intro:
    $ HIDE_UI = True

    stop music fadeout .5
    play music "music/TRG_Banks/lost_in_the_city.mp3" fadeout .5
    scene bg black with fade
    call screen choose_sex
    if _return == 0:
        $ d = "Mike"
        $ b = "Seeker"
        $ HIDDEN.append("mike")
        $ HIDDEN.append("bedroom6")
        $ HIDDEN.append("bedroom4")
    else:
        $ d = "Bree"
        $ b = "Cheese"
        $ HIDDEN.append("bree")
        $ HIDDEN.append("office")
        $ HIDDEN.append("bedroom2")
        $ HIDDEN.append("bedroom1")
        $ game.set_flag("female",1)
    python:
        heroname = renpy.input("What is your name?", default=d)
        family_name = renpy.input("What is your family name?", default=b)
        hero = Hero(heroname, family_name)
        if not game.get_flag_value("female"):
            hero.smartphone_contacts.append("samantha")
    if not persistent.skip_tutorial:
        andre_say "Hi [hero.name]."
        andre_say "Please allow me to introduce myself..."
        andre_say "I am Andrealphus, Demon Lord of Lust, Duke of Debauchery, I am one of the Seven Lords of Sin, and honestly..."
        andre_say "I am the only one that is any fun."
        andre_say "Just kidding, I am the Dev for that little game you are playing, that's all."
        andre_say "First of all, thank you for playing my game and I really hope you enjoy it as much as I enjoy making it."
        andre_say "Second if you feel like helping out you can join my {a=https://www.patreon.com/Andrealphus}patreon{/a} or just buy me a {a=https://ko-fi.com/andrealphusgames}coffee{/a}."
        andre_say "Now, to help you start in 'Love & Sex' I'll give you a few pointers."
        show tutorial1 with dissolve
        andre_say "This is your livingroom, one of many rooms in the game world."
        show tutorial2 with dissolve
        andre_say "On the top left of the room you can see your {b}Needs{/b} because, yes you need to eat, sleep, clean yourself and have a little fun."
        andre_say "{image=ui/icon_energy_white.png} {b}Energy{/b} shows you how much stamina you have left before needing to rest."
        andre_say "{image=ui/icon_hunger_white.png} {b}Hunger{/b} shows you how hungry you are."
        andre_say "{image=ui/icon_grooming_white.png} {b}Grooming{/b} shows you how smelly and dirty you are."
        andre_say "{image=ui/icon_fun_white.png} {b}Fun{/b} lets you know how bored you are."
        andre_say "Don't let them go too low as when they get low you lose the ability to perform more and more {b}Actions{/b}."
        show tutorial3 with dissolve
        andre_say "Near the {b}Needs{/b} you can see your {b}Attributes{/b}, some girls find some {b}Attributes{/b} more pleasing and some {b}Actions{/b} requires high {b}Attributes{/b}."
        andre_say "{image=ui/icon_knowledge.png} {b}Knowledge{/b} is an accurate evaluation of your intellect."
        andre_say "{image=ui/icon_fitness.png} {b}Fitness{/b} evaluates your physical abilities."
        andre_say "{image=ui/icon_charm.png} {b}Charm{/b} is your charisma."
        andre_say "I advise you to raise your {b}Attributes{/b} as soon as you can, because for now they are rather low."
        show tutorial4 with dissolve
        andre_say "After the {b}Attributes{/b}, you can see your {b}Money{/b}, girls likes gifts and be taken to dates so this is quite a priority."
        andre_say "With {b}Money{/b} you can also buy clothes and accessories that will improve your {b}Attributes{/b}, some girls prefer certain clothes over others."
        andre_say "You can only change clothes from your {b}Inventory{/b} in your bedroom."
        show tutorial5 with dissolve
        andre_say "After the {b}Money{/b}, you can see a handy {b}Calendar{/b}."
        andre_say "In the game, the year is devided in 4 months of 30 days, with your usual holidays and birthdays."
        andre_say "Some {b}Actions{/b} are restricted by the time of day or the current month."
        andre_say "Sometimes below {b}Needs{/b} you will see a progress bar, it is used in several ways."
        andre_say "To show you if you have done your share of the chores while at home.\nTo display how far you are from your next promotion at work.\n To indicate how much a girl is having fun during a date"
        show tutorial6 with dissolve
        andre_say "At the bottom right resides the {b}Actions{/b} menu it shows you all the activities you can do in a given room."
        andre_say "It will not show you the {b}Actions{/b} you can't do, for example if you lack {b}Money{/b}, {b}Needs{/b} or {b}Attributes{/b}."
        show tutorial7 with dissolve
        andre_say "At the bottom left you will find the {b}Exits{/b} menu it shows you all the {b}Rooms{/b} you can access from the current one."
        show tutorial8 with dissolve
        andre_say "This is {b}Bree{/b} she is a girl, cute and sexy, your goal is to fuck her or another being of her species."
        show tutorial9 with dissolve
        andre_say "This is the {b}Interaction{/b} screen, you can choose what to discuss or do with a girl on that screen."
        show tutorial10 with dissolve
        andre_say "As I am pretty nice for a Game Dev I uploaded a nice app to your phone."
        andre_say "Once you get a girl's number you will be able to see her {image=ui/icon_love_vsmall.png} {b}Love{/b} and {image=ui/icon_sub_vsmall.png} {b}Kink{/b}."
        andre_say "That should be useful don't you think?."
        scene bg black with fade
        andre_say "And don't hesitate to change the grindiness and randomness of the game in the preferences to suit your tastes."
        andre_say "Now good luck in your virtual 'Love & Sex' life, and please fuck them all, the kinkier the better."
        $ persistent.skip_tutorial = True
    if game.get_flag_value("female"):
        call female_intro from _call_female_intro
    else:
        scene bg office
        "My eyes hurt."
        "I've been staring at this computer screen for what feels like an eternity by now, mindlessly tapping away at my keyboard."
        "Words fill the sheet in front of me, more than I needed, or was expected to write."
        "In my mindless trance I barely comprehend the sound of footsteps behind me, approaching with haste."
        show aletta teaser
        aletta_say "Your shift's over, what are you still doing here?"
        "The sound of my boss's voice snap me from my screen."
        "I turn to meet her gaze, rather than disappointed or angry, she simply seems curious."
        hero.say "Working, Boss."
        "I've never been a particularly hard worker. I did what was asked of me, and then moved on, but today was different."
        "I looked back to the screen quickly, attempting to hide in my work yet again."
        aletta_say "The day's over, go home, I'm not having some worker's union on my ass for unpaid overtime."
        "I groan."
        "Aletta's always been a good boss, fair and understanding."
        "She runs the place with an iron fist, but doesn't mistreat her employees."
        "I get the impression she genuinely cares for us."
        hero.say "Whatever you say, Boss..."
        "With an exaggerated rolling of her eyes, Aletta turned and began back towards her office."
        "I spend a moment admiring her behind as she does so, tightly wrapped in her dress skirt."
        hide aletta teaser
        "Reluctantly, I hit save and close down my computer."
        "I gaze into the empty black void of the screen for a few moments, before sliding from my desk, grabbing my jacket and beginning towards the door."
        show audrey teaser
        audrey_say "Wait! Take me with you!"
        "I'm stopped in my tracks by my coworker, Audrey, leaping in front of me, clasping onto my shirt with a pleading look in her eyes."
        "Audrey's nice, but she's trouble."
        "She's always getting into all sorts of mess, and expects me to help her clean it up."
        "I don't know why Aletta doesn't fire her already to be honest, she clearly don't find Audrey's uselessness endearing."
        "Although, Audrey has been working more nights lately."
        "Maybe Aletta is trying to punish her in some way?"
        "Whatever, it isn't any of my business."
        hero.say "Sorry Audrey, I have to go."
        audrey_say "Come on! I'll make it worth your time~!"
        "That was another thing about Audrey, she had the nasty habit of flirting excessively with any male coworker."
        "From what I know, she's never landed."
        hero.say "Bye Audrey."
        "I quickly pry the woman from my arm, hurrying to the exit post haste before they could stop me."
        audrey_say "I'll never forget this!"
        hide audrey
        if not "audrey" in GIRLS:
            show screen message(title="Patreon Edition",what="Audrey is only available in the Patreon Edition of the game.\nVisit {a=https://www.patreon.com/Andrealphus}patreon.com/Andrealphus{/a} to become a patron and get to know her better.")
            pause
            hide screen message
        scene bg street with fade
        "I trudge out onto the street, the bitter cold hitting me like a brick wall as I pause to get my bearings."
        "I'm lucky my house is nearby to work, it means I can walk to and from in no time at all."
        "Today though, that feels like more of a curse than a blessing."
        "It started with the call at lunch..."
        scene bg black with fade
        play sound "sd/cell_vibrate.mp3"
        pause 1.0
        hero.say "Hey Samantha."
        samantha_say "Hey."
        samantha_say "We moved out."
        hero.say "Wait, you what?"
        samantha_say "We moved out!"
        samantha_say "Ryan asked me and whisked me away, it was so romantic!"
        hero.say "What about me? What about your things?"
        samantha_say "Ryan already packed, and we put out an ad on your behalf for a new roommate!"
        hero.say "Woah, just hold on a minute."
        hero.say "Put on Ryan, Samantha."
        "I could hear a few seconds of silence and distant murmuring through my phone, before..."
        ryan_say "Sup?"
        hero.say "What the hell are you doing, man?"
        hero.say "I can't afford rent on my own!"
        ryan_say "Woah, calm down, Samantha just told you we're already looking for a replacement."
        hero.say "That's not the point!"
        hero.say "You didn't think to warn me?"
        ryan_say "You don't understand spontaneity, do you? No wonder Samantha chose me."
        hero.say "Woah, low blow Ryan."
        ryan_say "Whatever dude, later."
        hero.say "Wait!"
        play sound "sd/dialtone.mp3"
        scene bg street with fade
        "Ryan was my old college friend. We were pretty close for a while, so rented an house together after graduating."
        "When the landlord increased our rent, we had to look for a third roommate, and found Samantha."
        "Both of us were clearly interested from the start, and it quickly turned into a contest."
        "Ryan won."
        "He turned into a real douche after that, and would rub his victory in my face at every possible moment. Samantha didn't seem to even notice."
        "I was still reeling from being dumped by my girlfriend, Alexis, at the time, so it really hurt."
        "I caught her sneaking around banging strangers behind my back, it was... Rough for a while."
        "Now, all I've got waiting for me is a large, empty place I can't afford to live in."
        "I'd rather be working all night."
        "Huh, who's this?"
        scene bg house
        show bree
        "A strange woman stands outside my door, hammering the doorbell even though it was clear nobody's home."
        "She seems annoyed, as though the occupant of the home she was trying to enter has wronged her somehow."
        hero.say "Can I help you?"
        "She turns to me as I speak, and I have to admit, I was struck by her beauty."
        unknown_girl_say "Oh, hey. You know who lives here? I'm supposed to meet them but I don't think they're in."
        "There was one likelihood that stood out above all others in my mind, she must have arranged to meet me here with Ryan."
        "He knew what time I get home from work, so probably told her to wait for me then."
        "I feel a slight twinge of guilt as I realise that my moping around made her stand around in the cold for god knows how long."
        hero.say "Oh, that's me."
        hero.say "You here for the place?"
        "I don't question how quickly she responded to the advertisement."
        unknown_girl_say "Oh, yeah! I'm Bree, I take it you're my potential roommate?"
        "She doesn't seem all that mad for making her wait at least, and quickly took my outstretched hand to give a quick shake."
        "I'm given pause by how soft her skin is, but I shake it off. I don't want another Samantha here, even if she is really hot."
        hero.say "Yeah, that's me."
        bree.say "Nice to meet you!"
        hero.say "Likewise."
        hero.say "Come on in..."
        hero.say "I'll show you around."
        hide bree
        scene bg livingroom
        show bree
        with fade
        bree.say "Wow, this place is pretty nice!"
        "I nod. It's even got a communal pool, for the price I'm lucky. And, well now she is too."
        bree.say "When can I move in?"
        "Woah, hold on a minute."
        hero.say "Move in?"
        hero.say "I've known you for less than a minute!"
        hero.say "Shouldn't we like, ask questions and get to know each other first?"
        bree.say "Oh, OK!"
        bree.say "In that case, tell me about yourself!"
        hero.say "Well, that's kinda vague..."
        bree.say "Then... Do you do like sport?"
        menu:
            "Martial Arts":
                hero.say "I do martial arts."
                $ hero.skills.append("martial_arts")
                $ hero.fitness += 3
                bree.say "Oh, cool! You'll have to show me some moves sometime!"
            "Golf":
                hero.say "I am an accomplished golfer."
                $ hero.skills.append("golf")
                $ hero.fitness += 2
                $ hero.charm += 1
                bree.say "Really? You don't seem like a golfer."
                hero.say "What, not a middle aged businessman in a suit?"
                bree.say "Exactly!"
                "I shake my head dramatically, before moving on."
            "Cooking":
                hero.say "Does cooking count?"
                $ hero.charm += 2
                $ hero.knowledge += 1
                $ hero.skills.append("cooking")
                bree.say "Cooking? Well, it's not really a sport..."
                bree.say "But I'll forget about that if you make me something good!"
                "I can already tell she's going to be a handful."
            "Dancing":
                hero.say "Not really, closest I get is dancing."
                $ hero.charm += 2
                $ hero.fitness += 1
                $ hero.skills.append("dance")
                bree.say "Ooh, how romantic."
            "Guns":
                hero.say "I love shooting and guns."
                $ hero.charm += 2
                $ hero.fitness += 1
                $ hero.skills.append("shooting")
                bree.say "..."
            "No, I don't":
                hero.say "I'm not really the sporty type."
                $ hero.knowledge += 1
                $ hero.charm += 1
                $ hero.fitness += 1
                bree.say "Hehe, same here. Give me a good video game or a book any day of the week."
        bree.say "So I'll go get my things!"
        hero.say "H-Hold on a minute!"
        hero.say "That was one question!"
        bree.say "Yeah, and now we know each other better! Great!"
        bree.say "Which room is mine?"
        play sound "sd/doorbell.mp3"
        "But, I don't have a choice, turning to call through the door before answering."
        hide bree
        scene bg black
        with fade
        scene bg house
        show sasha
        with wiperight
        hero.say "Hello?"
        unknown_girl_say "Hey, I'm here for the roommate position?"
        "Another? Just what was in that ad to attract them so quickly?"
        hero.say "Yeah, come in."
        "I step away from the door, waiting for the stranger to enter as Bree seems to grow curious."
        scene bg livingroom
        show bree at right
        show sasha at left
        with fade
        bree.say "Is that our new roommate?"
        "I sigh. It's clear arguing with her is futile, and it isn't like I've got much choice, rent is just around the corner and I don't have nearly enough to live here on my own."
        "I give a silent nod, which clearly excites Bree."
        "She gives the air a quick fist pump when she thinks I'm not looking."
        "The girl on the other side must have been hesitating, because it took a moment for the door to the room opened."

        "Another stunning girl stands in the entrance, although her demeanor is much darker than Bree's already."
        unknown_girl_say "I got the right place?"
        "Why she waited to ask until after she'd opened the door was beyond me."
        hero.say "Yeah, nice to meet you."

        bree.say "And I'm Bree!"
        bree.say "Are you going to be moving in too?"

        unknown_girl_say "The ad said three bedrooms, so yeah."
        "I push aside that nagging in the back of my mind, annoyed that they seem to have decided they're living here without even asking."
        "It's true that the place is technically three bedrooms, but me and Ryan made one of the rooms into a gym when him and Samantha hooked up."
        "She was sleeping with him after all, no need to leave a room to waste."
        "That reminds me though, all of that equipment was Ryan's, it's probably all gone now..."
        "I groan quietly to myself at the realisation that I'll have to start paying for the gym too."

        unknown_girl_say "Ugh, if it's such a big deal I'll find somewhere else."
        "Seeming to misunderstand my groan as being directed towards her, the new girl turned and began to head back towards the door."
        "I reach out quickly to grasp her arm to stop her in their tracks."
        hero.say "Wait!"
        "I find myself cowering however, as she slowly turned her head to meet me."
        "Her gaze was terrifying, I could have sworn it alone could have driven me to the verge of death."
        "I wordlessly, slowly released her, extending my arms in an apologetic manner as I backed away."
        hero.say "I-I mean, I wasn't groaning at you."
        unknown_girl_say "Touch me again like that, and I'll end you."
        "Jeez, what was with this girl?"
        hero.say "Yeah! OK, no touching, got it!"
        "I'm glad Bree finds this whole situation funny, I can see her holding back laughter from out of the corner of my vision."
        unknown_girl_say "Good, then we've reached an understanding. I'm Sasha, you can call me Sasha."
        bree.say "Nice to meet you, Sasha."
        hero.say "Yeah, likewise."
        "'Nice' was an overstatement, but being rude would be dangerous with a girl like that."

        bree.say "Alright, anything else you need from me?"
        "There's so many questions, I don't know where to begin, so I simply start with what seems obvious."
        hero.say "I'll need your current job for the leasing contract."
        bree.say "I'm a student full time."
        "That gives me slight pause, but I make a mental note of it anyway."
        "I wonder how a student can afford to stay in a place like this, even with three people, and good price for the size, it isn't cheap."

        sasha.say "Before you ask, I work at a clothing store at the mall."
        "I can imagine it now, gothic architecture and only black clothes."
        "The staff would be pretentious and all have names like 'Winter'."
        "Everything would be expensive to make up for the fact that nobody but goths cares about it, so sales are low."
        "But hey, I don't care how she makes her money as long as I don't have to cover her ass with rent."

        bree.say "What do you do?"
        hero.say "I work as a code monkey in a local company."
        sasha.say "That doesn't sound like the most inspiring job."
        hero.say "That's because it isn't."
        bree.say "Then, how do you unwind?"
        bree.say "You gotta have a hobby or two to relax with."
        $ p = False
        menu:
            "Video Games":
                hero.say "I play a lot of video games."
                $ hero.fitness += 1
                $ hero.charm += 1
                $ hero.knowledge += 1
                $ hero.skills.append("video_games")
                bree.say "Oh, nice! I shoulda made you for a fellow gamer!"
                sasha.say "You both play video games?"
                hero.say "Apparently. Do you?"
                sasha.say "No thanks, I have grown up hobbies."
                hero.say "Like what?"
            "Fitness":
                hero.say "I love running and working out."
                $ hero.fitness += 3
                bree.say "I coulda guessed that."
                "I strike a heroic pose, which draws a laugh out of Bree."
                "Maybe she won't be so bad after all, she seems like fun."
                "Sasha on the other hand, grimaces as I flex."
                sasha.say "Working out isn't a hobby."
                hero.say "Oh yeah? Then what do you do?"
            "Partying":
                $ p = True
                hero.say "I am a bit of a party animal."
                $ hero.charm += 3
                bree.say "You mean, clubs and stuff?"
                sasha.say "Yeah, that's what he said."
                bree.say "I never liked clubs, too loud."
                hero.say "I love a good night out."
                "Was... Was that a smile? On Sasha?"
                "It only lasted for a moment, but I could have sworn I saw one..."
                bree.say "What about you, Sasha? You do anything fun?"
            "Working":
                hero.say "I am very good at my work."
                $ hero.skills.append("work")
                bree.say "That's a bit boring..."
                hero.say "What about you then, Sasha?"
            "Reading":
                hero.say "I like to stay home with a good book."
                $ hero.knowledge += 3
                bree.say "Ooh, I like books."
                "Sasha gives a loud scoff at Bree's statement, clearly skeptical."
                hero.say "What about you then, Sasha?"
            "Playing guitar":
                hero.say "I started playing guitar when I was little."
                $ hero.charm += 3
                $ hero.skills.append("guitar")
                sasha.say "Pretty sure you play mainly commercial mainstream crap."
                "Sasha's comment put a dead stop to the conversation."
                "...."
                hero.say "What about you then, Sasha?"
            "Not really":
                hero.say "Little bit of this and a little bit of that."
                $ hero.knowledge += 1
                $ hero.charm += 1
                $ hero.fitness += 1
                sasha.say "That's not much of an answer."
                bree.say "Yeah..."
                "Quickly, I move to deflect attention before they start prying."
                hero.say "What about you then, Sasha?"
        sasha.say "I drink."
        sasha.say "A lot."
        hero.say "That's your hobby?"
        sasha.say "Well I also listen to heavy metal on full blast, but I guess I'll have to drop that one."
        "Thank god, I didn't need noise complaints on top of everything else."
        "A short, awkward lull in conversation followed, before I decided to break it with an obvious question."
        hero.say "You said you're a student, right Bree? What do you study?"
        bree.say "Oh, I'm studying to be a doctor."
        hero.say "Really? Friend of mine just graduated medical school."
        "Wait, maybe telling her that was a bad idea."
        "I don't want Ryan stealing away another hot roommate."
        bree.say "Oh wow, tell him I said congrats! It's tough."
        "Fortunately for me, Bree doesn't seem all that interested in meeting him, letting the conversation move on without another hiccup."
        bree.say "Nobody's perfect sooooo..."
        bree.say "Can you tell us something bad or shameful about you?"
        $ BAD = True
        menu:
            "No, nothing...":
                hero.say "Must be one of those rare perfect ones..."
                bree.say "You are no fun..."
                sasha.say "Pussy..."
                $ BAD = False
            "I am unlucky":
                hero.say "I am pretty unlucky..."
                $ hero.skills.append("unlucky")
            "I have some big debt.":
                hero.say "I am in debt."
                $ game.set_flag("debt",True)
            "Animals hate me":
                hero.say "I am not really an animal person, they don't like me at all."
                $ game.set_flag("animalhated",True)
        if BAD:
            sasha.say "So? Do anything of note, or is corporate lackey all there is to you?"
            "That hit deeper than Sasha realised, but I did a good job covering it up with a fake, confident demeanor."
            menu:
                "I won a marathon":
                    hero.say "I won a marathon once."
                    $ hero.fitness += 3
                    bree.say "Wow, that's really impressive!"
                    hero.say "Thanks Bree, took a lot of work."
                    "Ryan helped me train for it, he was so pissed when I beat him."
                "I am a people person":
                    hero.say "I was the most liked person in all of my classes."
                    $ hero.charm += 3
                    sasha.say "Wow, way to brag."
                    bree.say "Hey, you asked him!"
                    hero.say "Don't fight you two."
                    "In unison, the pair turned to face me."
                    bree_sasha "She started it!"
                    "What am I going to do with these two...?"
                "I won a eating contest":
                    hero.say "I won a burger eating contest."
                    hero.say "Twice."
                    $ hero.fitness += 1
                    $ hero.charm += 1
                    $ hero.knowledge += 1
                    $ hero.skills.append("iron_stomach")
                    sasha.say "I am not sure you should be proud of that."
                    hero.say "Really? Because I am proud. Really proud."
                    "Bree at the very least seems impressed, although Sasha clearly isn't."
                "I am pretty lucky" if not "unlucky" in hero.skills:
                    hero.say "I won the lottery once."
                    $ hero.skills.append("luck")
                    $ hero.money += 500
                    bree.say "Wow! So you can take care of all the rent, right?"
                    hero.say "Oh, it uh, wasn't that much."
                    sasha.say "Wow, what an accomplishment."
                "I was the best in my class.":
                    hero.say "I was the top of my class coming out of college."
                    $ hero.knowledge += 3
                    sasha.say "Wow, nerd."
                    "Sasha acts as though she isn't impressed, but I think I can see through her facade this time. Bree clearly doesn't."
                    bree.say "Hey, he's a hard worker! Don't take that away from him."
                    sasha.say "Clearly didn't do him any good with the job he's got."
                    "Ouch..."
                    "Even Bree didn't rush to my rescue for that one. That just makes it worse."
                "I don't sleep":
                    hero.say "I once stayed awake for a week straight."
                    $ hero.skills.append("no_sleep")
                    $ hero.knowledge += 2
                    sasha.say "And...?"
                    hero.say "And what?"
                    sasha.say "If that's the best accomplishment you can think of, I'm sorry for you."
                    hero.say "..."
                    "OK she's got a point."
                "I am hung":
                    hero.say "My exes nicknamed me the horse."
                    $ hero.charm += 2
                    $ hero.fitness += 1
                    $ hero.skills.append("hung")
                    sasha.say "Oh, gross."
                    "The pair visibly cringed at my comment, each reeling backwards in disgust."
                    "I just wore a dumb smile."
                    "It was true, I was larger than most and an animal in the sack, it's one of my best features in fact."
                    bree.say "Can we just... Forget you ever said that and move on?"
                    sasha.say "Seconded."
                    hero.say "Guys..."
                    "I was about to object, but a glare from Sasha cuts me short, so I sigh, and nod in agreement."
        bree.say "Well, now we all know each other, is it decided?"
        hero.say "Hmm?"
        "Wait, I DO get the choice?"
        "Both had been so pushy that I'd just accepted them staying here, but suddenly Bree threw the question back at me."
        "Well, Bree seems nice enough, and Sasha is pushy and rude, but I doubt just us two would be able to handle the rent."
        if p:
            "Besides, it looks like she might be interested in going clubbing sometime, maybe she isn't as bad as she makes herself look."
        hero.say "Sure, welcome to the place."
        "Bree silently fist pumps the air again, clearly excited to be here, although this time didn't try to hide it."
        "Sasha however, does try to conceal her joy with being accepted. She might not like us two, but it's a nice place after all."
        "I grin at the slight beginnings of a smile on her lips, but turn away before they can see me."
        hero.say "Alright, couple of things before we start."
        hero.say "The rent and bills are paid on mondays..."
        hero.say "I'd say $100 from each of us will cover them."
        hero.say "Be sure to have the money ready or you're just going to piss the rest of us off when we have to pay extra."
        hero.say "One of the bedrooms hasn't got any furniture in it, so-"
        sasha.say "I'll take that one."
        "I'm cut short by Sasha's interruption, but shrug it off. It solves that problem after all."
        hero.say "Then uh... I think that's it."
        bree.say "Great! That means I can make you help me with my things!"
        hero.say "Wait, I never agreed to that."
        bree.say "Aww, come on! They're all outside already!"
        sasha.say "If you brought them all yourself, why'd you need his help?"
        bree.say "He's a guy! They're supposed to help damsels in distress."
        sasha.say "Whatever, I'm out."
        hero.say "Where are you going?"
        sasha.say "Where'd you think? I didn't bring all my shit with me."
        sasha.say "I didn't come here assuming I'd be given the room like Bree did."
        bree.say "But I was right!"
        sasha.say "Yeah. Later."
        "I watch Sasha stroll back out of the door and down the street."
        "She had a point, what would Bree have done if they didn't get the room?"
        bree.say "Hey?"
        hero.say "Yes...?"
        bree.say "Why're you just staring at the door?"
        hero.say "Just... Thinking."
        bree.say "Well~ That energy would be better used coming to get my stuff, come on!"
        "I'm caught by surprise as Bree grasps my wrist, dragging me towards the door before I can resist."
        "I've not known Bree for long, but I can tell it'd be futile to complain."
        "Begrudgingly, I drag the many, many large suitcases she'd stashed around the side of the house."
        "She must have either tried not to seem too eager, or knew I'd never have helped if I knew just how much she'd come with."
        "By the time I'm finished, Bree is beaming at me, but everything hurts and I'm too tired to appreciate her thanks."
        "I throw myself onto my bed with a soft thump, and soon drift away to thoughts of the future."
        "Today has taken some twists and turns, but if one thing's for certain, life from now is going to be an adventure..."
        "With friends and roommates like mine, how couldn't it be?"
        $ HIDE_UI = False
        hide bree
        hide sasha
        scene bg black with fade
    return

label female_intro:
    scene bg coffeeshop
    "The interior of the coffee shop is bustling and loud, like it always is near the end of a workday."
    "I can hardly hear it. My heart is pounding in my ears."
    "I’m lucky to find a seat in this clamor, but there’s one open near the window, and I pull it out and flop my messenger bag onto the table, taking a long hard swig of my coffee."
    "It’s too hot. It burns my tongue with that familiar immediate numbing feeling, and I try not to make a scene as I suck in a few quick puffs of cooling air before swallowing it down."
    "No time to dwell on it. I pull out my laptop and set it on top of my bag, swinging it open."
    "It brings up my login screen, prompting me for my name."
    "[hero.name]. That’s me."
    "The webcam blinks for a second while the laptop scans my face, then the screen goes bright, opening up onto my desktop."
    "I click the browser immediately, impatiently tapping a fingernail against my touchpad while I wait for my laptop to finish waking up."
    "I’m done."
    "Finito."
    "I’d thought I’d been done for a while now, but I didn’t know what truly, completely done felt like until today."
    "I have the worst roommate on the planet. Name something you’ve heard in threads of roommate horror stories, and mine has done it."
    "I’m almost completely convinced she’s actually a goblin who’s been seeking out my family for years to enact some centuries-old curse, and of course, she found me."
    "She’s inhuman. This afternoon, after I finished brushing her actual toenail clippings off my bed after being stabbed by them when I flopped down onto what should have been my space..."
    "...my sanctuary, she had the nerve to step into my doorway, dripping toothpaste-y slobber onto my carpet while she brushed (at 3pm!) and casually reminded me that our lease is up and we should renew."
    "Good luck with that."
    "My browser window finally finishes loading, and I click the search bar and immediately type in ‘available apartments’ and my zipcode."
    "If there’s anything -- anything at all -- available for me to GTFO as soon as possible, she’s renewing that lease on her own."
    "In fact, even if there’s nothing available at all, I’m considering a stint of homelessness just to be out of her immediate area. Forever."
    "I click a webpage when the results come up, my eyes falling immediately to the first, newest listing."
    "It’s not an apartment at all, but a house for rent. Three bedrooms, yadda yadda, seeking two roommates, sure, and--"
    "Oh, wow."
    "I lean myself forward a little, though I’ve got near perfect vision, just to make sure I’m seeing that number right."
    "This might be the winner right off the bat. A house, no stomping upstairs neighbors, a pool, and the square-footage is definitely more than our current place… for that much?"
    "I whip my cell phone out of my pocket and dial the number listed, already hooked. I need some answers."
    "A male’s voice picks up after the second ring."
    ryan_say "Y’ello? This is Ryan. "
    hero.say "Hey! So I’m looking at the listing you put up, and I’m just wondering if this is, like, a typo or--?"
    ryan_say "Nope, not a typo. That’ll be your rent, split three ways. It’s a pretty sweet deal."
    "Yeah it is!"
    hero.say "Great! So do I, uh, like need to bring you guys anything, like a background check, or--"
    ryan_say "Nope, you sound great for the position already."
    "I’m not entirely sure what that means, but I’m a little too starstruck by the prospect of this place to dwell on it."
    ryan_say "Why don’t you stop by and check the place out?"
    hero.say "Like, right now?"
    "I can tell that my voice has raised a pitch in my excitement, and for the briefest moment am aware of the fact that I’m being over-eager. But I cannot let this place pass me by. This is my salvation! I’m out!"
    ryan_say "Yeah, why not? You can swing by around uhh--"
    "There’s a pause, where I assume he checks the time."
    ryan_say "Oh, around now, actually. Homeboy should be ready to meet you by the time you’re there."
    hero.say "Great! Perfect!"
    "I can feel a beaming, helpless grin across my face, and hope nobody’s staring at me. Balancing my phone between my cheek and my shoulder, I snap my laptop closed and shove it away, gathering my bag back onto my shoulder."
    hero.say "I’ll be right over then! Bye!"
    "My cellphone beeps in confirmation as I tap the end call button and lock it, shoving it into my bag and snatching my coffee before I turn and practically bolt out of the shop."
    scene bg street
    "It’s cold outside, and my breath puffs out before my lips as I alternate between a powerwalk and, admittedly, brief stints of giddy jogging on my way to the apartment."
    "Finally, breathing a little heavily from the exertion, I stop in front of a quaint, pretty house, letting my gaze trail up it to the gloomy evening sky."
    "My attention falls back to my phone screen, opened to a GPS page where my blinking blue dot is settled just beside the destination marker."
    "I can feel it already."
    scene bg house
    "This is my new home. Excitement bubbles back up in my chest, and, flashing my best, beaming smile, I jog up the front steps, pressing the doorbell and waiting for my salvation to swing the door open."
    "But it… doesn’t."
    "Doorbell must be broken. No prob. Been in a couple places like that."
    "Readjusting my bag onto my shoulder a little, I clear my throat and rap my knuckles against the door, calling out as clearly as I can."
    hero.say "Hey! I’m here about the rooms?"
    "Nothing."
    "My smile fades a bit as a minute passes, while I give them time to get to the door."
    "Maybe they’re old, anyway. I immediately assumed they’d be my age, but they don’t necessarily have to be. Maybe it’s Ryan’s grandpa or something, looking to fill some empty space?"
    "I leave enough time for even the creakiest of old men to get to their feet and waddle over to the door before I huff an exasperated breath and let my weak smile fade to a frown."
    "Maybe they’re in the shower."
    "I lean on the doorbell a few times, trying to catch their attention, or wake them up."
    "After a few minutes, I double check my GPS, and the address, and match the map to the image on the real estate site… this is the place, I’m almost positive."
    "Plus, I feel it, deep in my bones. My new room is in there. I’ll be waking up with beaming sunlight through my window and birds chirping and I’ll be free and happy and far, far away from my current place and my current state."
    "This is the one. It has to be."
    "I don’t know how long I spend alternating between the doorbell, yelling, and pounding my fist on the front door."
    "Probably an embarrassingly long time, honestly, before I finally consider that I should maybe call Ryan again."
    "I’m just desperate. I need this. I need it. I pound my fist one last time in frustration against the door, but before I can pull my phone back out to try calling Ryan a voice comes from behind me."
    show mike casual
    mike_say "Can I help you?"
    "The frustration inside me that had been steadily bubbling into anger dissipates in an instant, and I whirl back to face the source of the voice."
    "It’s a young man, standing in clothing that says he just got off work. He blinks at me, which I take for confusion. Maybe he’s a neighbor or something."
    hero.say "Oh, hey."
    "I adjust the strap of my bag again on my shoulder, propping a hand on my opposite hip."
    hero.say "You know who lives here? I’m supposed to meet them, but I don’t think they’re in."
    "He’s quiet, for the briefest moments, as he seems to process what I’ve said."
    mike_say "Oh… That’s me."
    "He makes his way down the front walk towards me, and hope thrills back up through my spine, immediately renewing the light to my eyes and the smile on my face."
    mike_say "You here for the place?"
    hero.say "Oh, yeah!"
    "I clear my throat to try to control my voice, at least to not sound so manic about it. Don’t want to scare him off before I even get my foot in the door."
    hero.say "I’m [hero.name]. I take it you’re Mike?"
    "He reaches out his hand to give the formal greeting handshake, and I take it eagerly, giving it a firm, single shake while he sort of limply obliges, like he’s still stuck trying to catch up to what’s going on."
    "I wonder, briefly, if Ryan even told him I was stopping by, but don’t dwell on it too much."
    mike_say "Yeah, that’s me."
    "I decide to just carry the interaction for him. Poor guy might be tuckered from work."
    "That’s fine. I’ve got the energy for both of us."
    hero.say "Nice to meet you!"
    "He gives a nod."
    mike_say "Likewise."
    "He reaches into his pocket and steps up beside me, and I move to allow him space to the front door as he pulls out a jingling set of keys."
    mike_say "Here, come on in. I’ll show you around."
    "I could dance through the doorway behind him, I’m so elated."
    "But I control myself, for now."
    scene bg livingroom
    "When I’m behind the closed door of my bedroom, I can do all the dancing I need to. Just keep it together."
    hero.say "Wow,"
    "I breathe, stepping past him and letting my gaze sweep across the room, taking it all in."
    hero.say "This place is pretty nice!"
    "I can picture myself, draped across that couch."
    "Playing video games on that tv."
    "This is it, for sure. No questions. This is home, sweet home. Ryan and his perfectly timed ad are my salvation, and this is paradise."
    "I whirl back around to face Mike where he stands, still lingering near the doorway."
    "Ryan already said I was perfect, no further investigation needed, and even if it’s maybe a little bit childish I take that as fact, speaking the next sentence through my eager smile."
    hero.say "When can I move in?"
    show mike casual
    "Mike blinks at me a second, looking like he’s reeling a bit from the whiplash."
    "Maybe I’m moving a little fast for him. But, hey, if he’s going to be my roommate, he’d better learn to keep the hell up with me!"
    mike_say "Move in?"
    "he repeats."
    mike_say "I’ve known you for less than a minute!"
    "He seems to fumble a bit over his words, like he’s trying to salvage something of normalcy out of this."
    mike_say "Should we, like, ask questions and get to know each other, or something?"
    hero.say "Okay, shoot."
    "Mike hesitates again, obviously not ready to be put in that situation."
    "In attempt to lighten the mood a little bit, I giggle and bring my hands up into finger guns."
    hero.say "C’mon, Desperado."
    "I feign firing my guns at him, resisting the pew pew, though they sound in my head."
    "He seems to gather himself a little bit."
    mike_say "I dunno, uhh… I guess, what would you say is the worst thing you’ve ever done?"
    "I can tell that that’s the best he can do as a single question to gauge my character. He’s obviously never been the interviewer for a rental applicant before. The way he’s flustered by this is kind of cute."
    menu:
        "I stole something once… but I gave it back.":
            hero.say "Well…"
            "I shift my weight a little bit and clear my throat. I don’t really like talking about these kinds of cringey memories. They make my ears feel like they’re burning, for some reason."
            "But, he asked, and I’m trying to make a good impression, so…"
            hero.say "One time when I was like nine, my parents took me to this garden store. And there were these little fairy garden decorations, and on one of them the little fairy statue had broken off, and I shoved it into my pocket and took it."
            "I swallow hard and shoot my eyes back up to his face, realizing suddenly that I’d dropped it in a mirroring childlike shame."
            mike_say "Really?"
            hero.say "I brought it back, though!"
            "I quickly amend."
            hero.say "I tried to play with it for a little while, but I felt so terrible the whole time, even though it was so pretty. I started crying and made my parents bring me back to return it."
            "Mike laughs, folding his arms and scanning me up and down."
            "A peeved huff escapes me, but a smile crosses my face helplessly anyway as I see the humor in the situation."
            hero.say "The store… laughed at me, too."
            hero.say "They thought it was really cute."
            mike_say "So what you’re saying is, you’re an insufferably good girl?"
            hero.say "I was a criminal!"
            "My protest seems to fall on deaf ears as he shakes his head in what seems like disapproval."
            "Is being a good kid such a bad thing, anyway?"
            $ NOTIFICATIONS.append(["{image=ui/icon_good.png}+10",2])
            $ game.set_flag("morality",10,mod="+")
        "Yuck. Don’t you have any less… personal questions?":
            "I wrinkle my nose."
            hero.say "That’s digging kind of deep right off the bat, huh?"
            "I see Mike shift his weight, uncomfortable, and I snicker a little bit at him."
            hero.say "Kind of a hard-hitting first date question. You don’t do this much, huh?"
            "Mike throws his arms up a little bit in frustration before letting them fall back to his sides."
            mike_say "Kind of got thrown into this. Didn’t have a ton of time to prepare."
            "Aw. Poor guy."
        "Hehe… You don’t want to know.":
            "A wicked smile curls at one corner of my lips, and I lid my eyes a little, giving a mischievous chuckle deep in my chest."
            hero.say "Don’t ask questions you can’t handle the answers to."
            "Mike seems a little taken aback by this, his eyes widening a little bit."
            mike_say "I, uh… that bad, huh?"
            "I shut my eyes breezily and shrug, turning a little bit away from him."
            hero.say "Look, it wasn’t murder or arson, so there’s nothing for you to worry about, right?"
            "Mike seems unsure."
            hero.say "Well,"
            "I decide to flip his game back on him."
            hero.say "What about you?"
            mike_say "Huh?"
            "I fold my arms, popping out a hip casually as I look him up and down."
            hero.say "What’s the worst thing you’ve done, then. Isn’t it more important that I know?"
            "He frowned a bit."
            mike_say "Why would it be more important for you?"
            hero.say "Well, what if you’re like, an abuser, or a sexual deviant? What if you’re just trying to lure pretty young girls into your lair so you can tie us up at night and drag us into your dungeon? Huh?"
            "I was joking at first, but the more I talk, the more I start to freak myself out."
            hero.say "On the phone your friend said I sounded ‘perfect,’ it’s ‘cause I’m young and female, isn’t it?"
            "Mike seems completely speechless, holding up his hands as if as some kind of shield against my accusations."
            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}-10",2])
            $ game.set_flag("morality",10,mod="-")
    "Before he can say anything, though, there’s a knock at the door behind him, and both of our attentions turn suddenly toward it."
    unknown_girl_say "Hello?"
    "It’s a female voice."
    "Mike turns back to me, as if it might be my doing that she’s here."
    "But I only hold out a hand, presenting the new voice as more evidence to my claims. See? Another young hot piece of meat, huh?"
    show sasha casual at right
    show mike casual at left
    "I see Mike gulp as he pulls the door open to reveal a dark-haired young woman on the other side, her arms folded in a confident stance."
    mike_say "Hello?"
    unknown_girl_say "Hey. I’m here for the roommate position."
    "She looks like she doesn’t take crap from anyone."
    "If I was freaking myself out about Mike being out to take advantage of us, I feel a little more secure seeing her standing there."
    "I’m no pushover, myself, but with this goth rocker chick at my side, we can kick this dude’s ass into oblivion if he tries it. No doubt."
    mike_say "Uh, yeah. Come in. I was just showing--"
    hero.say "Me to my room,"
    "I cut in, stepping forward and holding my hand out to greet this new girl."
    hero.say "Hey! You must be our new roommate."
    "There’s no look of devious glee in Mike’s eyes at the prospect of the two of us moving in. In fact, he looks a little shaken and overwhelmed, like a skittish kitten in a room where too much is going on."
    "Somehow I highly doubt he’s going to be taking advantage of anyone."
    unknown_girl_say "Sasha,"
    "She shakes it back with me, firm and confident, in the way Mike hadn’t."
    "I get the feeling everything’s going to go real smoothly for me here."
    hero.say "So."
    "I bring my gaze back up to Mike, and Sasha steps aside to face him as well, putting him on the spot."
    hero.say "Where’s our paperwork then, big boy?"
    "He seems to accept that he’s lost control of the situation. With a sigh, he brings a hand up to massage the bridge of his nose and nods."
    mike_say "Yeah, I’ll… need to go print that out, I guess."
    sasha.say "Sounds good."
    hero.say "Yeah, I’ll go start packing!"
    sasha.say "I’ll get my things, too."
    mike_say "I guess I’ll have that ready when you guys get back…?"
    hero.say "Tomorrow,"
    "There was no question that I’d have my things packed up and ready to get out of the hellhole of my current apartment by tonight, but I figured I’d give the poor kid some time to recuperate first."
    mike_say "Tomorrow,"
    "He stands aside as Sasha steps past him and out the door, and I skip happily out behind her, breaking into a jog immediately down the sidewalk toward my place."
    scene bg black with fade
    "I can’t wait."
    "I think I even like the two of them already."
    "I click the tip of the pen back into its holster, dropping it onto the table beside my paperwork."
    "It feels so much easier to breathe here, like a huge weight has been lifted off my chest."
    "I knew I hated my last place, but I didn’t realize just how much it was affecting me until it was finally over."
    scene bg kitchen with fade
    hero.say "So, that’s that, then?"
    show mike casual
    "I glance back up to where Mike is sitting opposite me at the table."
    "He looks a little less exhausted than he had yesterday. Sleeping on it definitely did him some favors."
    mike_say "Yeah, I guess that’s it then."
    "He motions vaguely toward the rest of the room with the hand not lazily propping up his jaw."
    mike_say "Welcome home."
    "I can feel my face light up like a disney princess, and it takes all of my strength not to squeal with glee."
    "Home. Home! This place is my home now."
    "And Mike and Sasha… maybe we won’t be the best of best friends, I won’t be that naive. But I can tell I’m gonna at least get along with them."
    "Or, at least, I assume I will, based off our short encounter. It’s gonna be great. Nothing like my ex-roommate and that hellhole."
    "My voice is a little bit quiet, like a kid asking about their birthday present, when I speak next."
    hero.say "Which room is mine?"
    "A knock at the door interrupts before Mike can answer me, and my heart leaps again with renewed excitement."
    mike_say "That’s probably Sasha,"
    show bg house
    show mike casual at left
    show sasha box normal at right
    "There’s a stack of boxes with shapely legs on the other side of it, and after a moment, Mike grabs the top half of the mountain from her, revealing her pretty face."
    "She blows a tuft of hair off of her forehead before shifting her gaze past him over to me."
    sasha.say "Hey, earlybirds. Did I miss the party?"
    "Okay, so I was kind of excited. I’d been bouncing on the edge of my bed ready to head over this morning, practically before the sun even rose."
    "But I’d managed to control myself enough to drive around town a bit after I’d packed my car, get myself a coffee, then a breakfast from the other side of the city, just to kill time and let Mike sleep."
    "I didn’t even tell my roommate I was leaving. I taped a note on her door telling her that I wasn’t renewing, and wishing her good luck finding either a replacement or a new place."
    "Thank God Sasha took the last room in this place. How mortified would I have been if she had shown up here, ringing the doorbell about the ad?"
    "A physical shudder rolls down my spine as Mike moves over and sets the boxes he’s carrying onto the edge of the table to bear some of the weight."
    "Sasha stands unbothered by the door, holding hers with seemingly no problem."
    "What a badass. I cant’t help feeling a bit of an envycrush building in me."
    "I really want to be good friends with her. Alright, I admit it. It feels like first days at new schools all over again, scoping out the ‘cool kids’ and wishing shamelessly that they’d end up thinking I was cool, too."
    scene bg secondfloor
    show mike casual at left
    show sasha casual2 at right
    mike_say "Okay, well, there’s actually some bad news,"
    "Mike huffs, glancing toward the stairway and motioning with his head toward the floor above us."
    mike_say "Your rooms are up there, but one of them’s gonna be completely emptied--"
    sasha.say "I’ll take that one."
    hide sasha
    mike_say "--oh. Okay, that works."
    "Works for me, too."
    "I hop up out of my seat, rarin’ and ready to get this show on the road."
    hero.say "So the other one’s mine, then?"
    mike_say "All yours."
    scene bg bedroom2
    "I don’t waste any time before making my way over to my things, hoisting one backpack over my shoulder and grabbing the handle of a rolling suitcase in the other hand."
    "There weren’t a ton of things I needed to bring, honestly."
    "My last place had been pre-furnished, too, so I’d only had knick-knacks and a few personal items that I’d needed to pack."
    "I’d managed to fit all of it into two backpacks, two suitcases, a purse, a laundry bag, and my messenger bag, and admittedly most of what filled them were my clothes."
    "It’s easy to unpack my necessities once I hike all of my belongings up into my room, flopping myself back onto my bed and reveling for a moment in the feeling of fresh surroundings and fresh starts."
    "I breathe it in, just for a bit, closing my eyes and drawing a slow, deep, filling breath in through my nose, before huffing it out and hopping back to my feet."
    "Within the hour, I’ve got my place set up -- laptop set neatly on the desk, plugged in and charging, my gaming mouse and headset waiting on either side of it."
    "My trinkets, memories from old friends and from home, are set up appealingly across the top of my dresser and the odd shelf here and there, making the place look already like it’s lived in and welcoming."
    "I’ll deal with the clothes later. That’s always my least favorite part of cleaning up, and admittedly it’s pretty likely I’ll be dressing myself out of my suitcases for a bit before I get my act together and put stuff into the closet and dresser."
    "But for now, I can hardly wait to start exploring. I wonder if Sasha’s done unpacking yet? Maybe they need help with something. What’s Mike doing right now?"
    "Maybe I can check out that pool I saw in the ad."
    $ sasha_love_max = 30
    $ sasha.set_flag("story",1)
    $ HIDE_UI = False
    hide mike
    hide sasha
    scene bg black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
