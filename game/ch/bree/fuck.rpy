init -15 python:
    Activity(**{
        "name": "fuck_bree",
        "display_name": "fuck",
        "label":["ACTIVE_GIRL_fuck_ROOM"],
        "duration": 1,
        "game_conditions": {"hours":(20,25), "activity":"interact", "label":"ACTIVE_GIRL_fuck_ROOM", "flag_female":0},
        "girls_conditions": {
            "bree":{
                "min_love":150,
                "not_activity":["sleep"],
                "flagmin_sex":2,
                "active":True
                }
            },
        "once_day": "ACTIVE_GIRL",
        "icon": "fuck",
        })

    Activity(**{
        "name": "fuck_bree_beach",
        "display_name": "fuck",
        "label":["ACTIVE_GIRL_fuck_ROOM"],
        "duration": 1,
        "game_conditions": {"hours":(14,18), "activity":"interact", "label":"ACTIVE_GIRL_fuck_ROOM", "flag_female":0, "room":["beach","date_beach"]},
        "girls_conditions": {
            "bree":{
                "min_love":150,
                "not_activity":["sleep"],
                "flagmin_sex":2,
                "active":True
                }
            },
        "once_day": "ACTIVE_GIRL",
        "icon": "fuck",
        })

label bree_fuck_bathroom:
    scene bg bathroom
    show bree naked






    "I pull the shower-curtain aside and step in behind her, the first thing Bree knows about it is the sensation of my cock against her backside."
    "She lets out a yelp of surprise, throwing her arms up and allowing me to step forwards and wrap my arms around her."
    hero.say "Surprise, Bree!"
    bree.say "Oh, [hero.name] - you scared the life out of me!"
    "She's leaning back into me by now, letting me take a little of her weight."
    hero.say "I'm sorry, Bree...would you like me to get out of your hair?"
    "I run my hands over her thighs as I say this, letting her feel my dick up against her buttocks."
    "She lets out a chuckle, and I feel her reach around to stroke my cock."
    bree.say "No...you're here now, so you might as well stay and let me help you get cleaned up!"
    if game.get_flag_value("homeharem") and sasha.room == game.room and not "sasha" in HIDDEN and not sasha.get_flag_value("cheated"):
        show sasha at left
        show bree at right
        sasha.say "Can I join in?"
        menu:
            "Yes":
                hero.say "That would be great."
                call shower_ffm
                $ bree.love += 2
                $ sasha.love += 2
                $ sasha.set_flag("lesbian",1,mod="+")
                $ bree.set_flag("lesbian",1,mod="+")
                return
            "No":
                $ sasha.love -= 2
                hero.say "Sorry, I wanna be alone with Bree a little."
                hide sasha































    show bree showersex wet
    if bree.get_flag_value("pregnant") >= 9:
        "Aware of just how delicate Bree's condition is right now, I loop one arm under hers to hold her up."
        "The other I use to reach around and cradle her belly so that I can support her and make sure she won't slip while we make love."
        "Though she's bent like a bow, I move my legs and abdomen to bring my cock into a position where I can find my way into Bree."
        "I enter her slowly and with infinite care, caressing her swollen belly as she sinks onto me."
    elif bree.get_flag_value("collared"):
        "I'm more than ready to have my way with Bree by now, and she needs to be taken in hand to make that happen."
        "I seize her arms with one of my own and grab hold of her collar firmly with the other."
        "Forced against the wall, breasts and belly pressed to the tiles, Bree yelps as she feels me searching for her pussy."
        "Almost as soon as I find it, I thrust myself into her, enjoying the sounds that she makes as I do so."
    else:
        "I can already feel Bree slipping and sliding around thanks to the fact that we're both so wet from the shower."
        "Not wanting to be chasing her around like a bar of slick soap, I put my arms under hers and pin them against my chest."
        "At the same time, I push my groin forwards, lifting her just enough to make it easier for my cock to snake between her legs and find her pussy."
        "Pushing myself as deep into her as I can go, Bree's belly and breasts are pressed up against the tiled wall."
    "The warmth of the water and the steam rising around us seems to make the act all the more intense and enjoyable."
    "I settle into a steady rhythm that Bree mirrors, meaning that we both move as one, our bodies taking and giving in almost equal measures."
    "Bree has her head thrown back by now, resting on my shoulder and sending her hair falling down my back."
    "I can feel the water running through it, turning her locks into heavy tendrils, as it flows like a river through it."
    "Bree's legs twine with my own, as though she's trying to climb upwards and let me come yet further into her."
    "I want to pick her up, but there's nowhere to go but up against the wall, and she's already almost pressed too close to it."
    "So instead I redouble the intensity of my thrusts, making Bree keep up as even as she begins to pant quite dramatically."
    "I can't blame her for that - the heat in the shower is starting to become almost overwhelming."
    "We've been kept from realising this by the fact that, as much as we might be sweating right now, the water is just washing it straight away."
    "I begin to feel Bree's muscles getting weaker with each moment that passes, as if the heat is leaching her strength away."
    "More and more I start to find myself supporting her, rather than simply holding onto her."
    "And I can't help worrying that she will pass out if I don't do something sooner, rather than later."
    show bree showersex wet speed
    menu:
        "Cum inside":
            "I can feel myself getting overcome by the heat in the exact same way as Bree."
            "And I realise that, if I up the pace now, I can maybe cum before I have to admit defeat and carry her out of the shower in a dead faint."
            bree.say "[hero.name]...I'm feeling...feeling light-headed!"
            "I try to pretend like I can't hear Bree's warning, instead keeping myself going the whole time."
            bree.say "Please...[hero.name]...I can see weird shit flashing...before my...eyes!"
            "It's perhaps a second after this last plea that I cum."
            "Even though she's out of it, Bree feels the full force of the orgasm."
            "For a moment, she seems to go limp in my arms and I'm convinced that she's passed out."
            "But then she shudders and manages to support some of her own weight once more."
            if (randint(1,3) == 1 or "hung" in hero.skills) and not bree.get_flag_value("pregnant") and not bree.get_flag_value("pill"):
                $ bree.set_flag("pregnant",1)













    "Bree shudders and looks around her, as if not sure how she came to be so disoriented in the middle of the bathroom."
    scene bg bathroom
    show bree naked blush
    bree.say "Oooh, [hero.name]...I feel so dizzy - what happened?"
    hero.say "You blacked out for a couple of seconds back there, Bree."
    hero.say "I only just managed to catch you in time, otherwise you could have had a nasty fall!"
    "Well, if she doesn't recall my rather selfish efforts to cum before she passed out, I'm not going to be the one to remind her."
    "Bree shakes her head, clearly still feeling the effects of being overcome by the heat."
    $ bree.love += 1
    bree.say "Maybe next time, we should think about the benefits of taking a COLD shower, yeah?"
    "I shrug and nod in agreement, just happy not to have been caught out putting my own orgasm before Bree's bodily well-being."
    return


label bree_fuck_livingroom:
label bree_fuck_kitchen:
label bree_fuck_pool:
label bree_fuck_bedroom1:
label bree_fuck_bedroom2:
label bree_fuck_bedroom3:
label bree_fuck_secondfloor:
label bree_fuck_home:
    show bree
    hero.say "Hey, wanna come and have fun in my bedroom ?"
    bree.say "Sure."
    if game.get_flag_value("homeharem") and sasha.room == game.room and not "sasha" in HIDDEN and not sasha.get_flag_value("cheated"):
        show sasha at left
        show bree at right
        sasha.say "Can I join in?"
        menu:
            "Yes":
                hero.say "That would be great."
                call bree_sasha_threesome from _call_bree_sasha_threesome
            "No":
                $ sasha.love -= 2
                hero.say "Sorry, I wanna be alone with Bree a little."
                hide sasha
                call bree_fuck_date from _call_bree_fuck_date_1
    else:
        call bree_fuck_date from _call_bree_fuck_date
    return

label bree_fuck_beach:
label bree_fuck_date_beach:
    show bree
    "I know that Bree and I are both really fond of the beach, slipping off there whenever the season and the weather are right and we have enough free time on our hands."
    "But the weird thing is that in all of the time we've been living together, we've never really made an effort to go to the beach together."
    "Maybe it's just that urge you get to run off and do something on your own whenever you really want get away from the daily grind and relax."
    "I honestly don't think either of us has been deliberately avoiding going there with the other - well, at least I haven't."
    "So today, when I decided that I was intent upon another day at the beach, I made a point of coming straight out and asking Bree if she wanted to tag along."
    "My suspicions that we'd just been overlooking the possibility before now seemed to be confirmed."
    "It only took Bree a couple of seconds to think about it before nodding and hurrying to collect her beach stuff."
    "And then we were into the car and off."
    "Once we pull up in the car park a little way from where the dunes begin, I can see Bree glancing around as if she's looking for someone."
    "Normally I'd be starting to get jealous at this point, wondering if she had a crush on some tanned beach-bum or surfer type that I don't know about."
    "But she looks nervous and maybe even a little embarrassed, so much so that I soon forget any suspicions that I might have had out of concern."
    hero.say "Bree, are you feeling okay?"
    bree.say "What...oh, yeah...I'm fine."
    hero.say "You sure?"
    hero.say "You look like something's bugging you!"
    "Bree shakes her head, her expression becoming visibly more calm and collected as she does so."
    bree.say "Oh, it's nothing really - just some weird guy I bumped into the last time I was here."
    "She punctuates the statement with a dismissive wave of her hand, which I find less than convincing."
    bree.say "And anyway, it's not a problem today, now is it?"
    bree.say "Because I have you here with me for company, [hero.name]."
    "I just nod and smile, already envisioning the muscle-bound admirer that's just waiting to kick sand in my face and bury me up to my neck as the tide's coming in."
    "I'm already wearing my shorts and a T-shirt when we start to make our way across the sand, carrying my few things under one arm."
    "Bree's likewise carrying little, but keeping the swimsuit she's chosen to wear hidden beneath a sarong that's tied over one of her shoulders."
    "Happy to let her pick the spot where we spread our towels, I trudge through the warm sand a little behind her."
    "And all while I'm enjoying a little of her behind, if you'll forgive me the awful pun."
    "Eventually, after walking past literally dozens of free spots that seemed more than adequate to my eyes, Bree settles on one that looks no different to any of the others."
    "We drop our stuff down and spread out the towels next to each other, after which I whip off my T-shirt, eager to get down to the serious business of doing nothing in the sun."
    "But I note that Bree doesn't seem to be in anywhere near as much of a hurry, as she shakes her head at my hastiness."
    "I begin to feel a little insulted by this, but the thought disappears from my mind, along with pretty much everything else, a moment later."
    "All of which happens because Bree puts a hand up to the knot that's tying her sarong in place and undoes it deftly."
    "In one smooth motion, the entire thing falls away and reveals the skimpy, white bikini that she's wearing underneath."
    "The move reminds me of the unveiling ceremonies that they have for works of art, and Bree certainly qualifies as one of those."
    "She seems to note my appreciation of her outfit and she finally sits down on her towel beside me."
    "At least I think that's what the knowing smile on her face is on account of..."
    "I watch as she reaches into her bag and pulls out a bottle of sun-cream, already shielding her eyes from the glaze of the rays beating down on us."
    menu:
        "Watch":
            "Bree squeezes a good-sized dollop of the greasy, white cream into the palm of her hand and begins to rub it up her arms."
            "The sound, the colour and the stuff being all over Bree's hands instantly puts me in mind of the most inappropriate things possible."
            "But then how can I be expected to think of literally anything else, especially when I'm sitting so close to her and watching every move she makes?"
            "Bree may well be conscientiously covering every inch of her exposed skin with a generous amount of cream for the sake of her health."
            "Though from my point of view it looks like nothing more than her deliberately oiling herself up in front of me."
            "I watch in rapt silence as her shoulders, chest and stomach all begin to glisten temptingly in the sun."
            "And then she'd moving on to her hips, thighs, calves and feet - enough to make a leg fetishist openly weep."
            "Once she's finally covered from head to toe, Bree lies back on her towel, the cream making her almost shimmer in the sunlight."
        "Help":
            $ bree.love += 1
            hero.say "Hey, Bree - why don't you let me get that for you?"
            "Bree regards me with a raised eyebrow, clearly not believing that my motives are purely altruistic in nature."
            "But then she shrugs and gives me a languid smile, tossing the sun-cream to me so that I have to struggle to catch it."
            bree.say "Sure, why not?"
            bree.say "Get rubbing, [hero.name] - and don't skimp on the cream!"
            "I squeeze a generous amount of sun-cream onto the palm of my hand as Bree rolls obligingly onto her belly."
            "The temptation would be to go straight for her more than inviting buttocks."
            "But I manage to restrain myself enough to begin in the more sensible and less pervy staring point of Bree's shoulders and the nape of her neck."
            "Bree sighs and lets out appreciative oohs and aahs as I work the cream into her skin."
            "The noises she's making might sound perfectly innocent to any casual passer-by, but I know that she's deliberately teasing me the whole time."
            "This only gets worse as I make my way down her back and start working my way over her buttocks and lower."
            "By now Bree's sighs have almost turned into genuine moans of pleasure."
            "Clearly she's enjoying teasing me all the while I'm massaging the cream into parts of her body that are making me so hot under the collar - even though I'm not even wearing one."
            "By the time I've finished the job, Bree rolls onto her side and looks herself up and down, as if admiring the job I've done."
    "Bree chuckles at my quite obvious state of discomfort after what I've just been witness to."
    bree.say "[hero.name], are YOU feeling okay?"
    "She takes great amusement in turning my question from earlier around on me."
    bree.say "Maybe I could help you out by returning the favour?"
    bree.say "Is there something of yours that I could rub?"
    "As if her tone of voice wasn't enough to impress upon me the true meaning of her words, Bree reaches out and stokes my now painfully visible erection through my shorts."
    "I glance this way and that, my face making it clear how much I want to take her up on the offer, but noting the sheer number of other people around us on the beach."
    "Bree picks up on the source of my reluctance almost instantly, a knowing smile spreading across her face as she shakes her head."
    bree.say "Oh no, don't you worry about anyone seeing us."
    bree.say "Trust me - I know a place that's just perfect for what I have in mind!"
    hero.say "Erm, okay...if you say so."
    "Bree's smile grows even wider and becomes intriguingly mischirvous as she takes my hand and almost pulls me to my feet."
    "I hurry to follow as she leads me further up the beach and away from the shoreline, up to the point where the sand becomes dunes that are covered in long grass."
    "But rather than the dunes and the grass, I begin to see that Bree's actually making straight for a line of wooden beach-huts."
    "Once we reach them, Bree wastes no time in walking around the back of them and choosing a particular spot for what she intends to do."
    "Even without taking the time to really study all of the angles, I'm pretty certain that we won't be seen from here."
    "In fact, I'd guess that the only way someone could spot us would be to actually walk around the back in the same way we just did."
    "While I'm definitely intrigued as to just how Bree came to know about this place, I keep my interest to myself."
    "I can't think of a better way to ruin the moment and cheat myself out of something that promises to be enjoyable in the extreme by suddenly asking a load of awkward questions."
    "Instead I give Bree what I hope is an encouraging smile and allow her to back me up against the plank wall of the nearest beach-hut."
    "She takes hold of the waistband of my shorts, tugging them suddenly down so that my erection is pulled down and then released like a spring."
    show beach bj mike
    if bree.get_flag_value("sexyswimsuit"):
        show beach bj sexyswimsuit
    else:
        show beach bj swimsuit
    "Giggling at my expression of discomfort, Bree takes my cock in one hand and beings to stroke it whilst making the same kind of sound you might use to comfort a child in pain."
    "She keeps on stroking the shaft as she gets down onto her knees, the motion slowly turning into an ever more vigorous rubbing the whole time."
    "By now her soothing tones have taken on a distinctly more hungry, almost carnal tone."
    show beach bj blowjob
    "Bree surprises me then by almost making a lunge to bite at the head of my cock, seizing it between her teeth and encircling it with her tongue at the same time."
    "This level of intensity only increases as she starts to take me deeper into her mouth in what feel like mouthfuls being swallowed by a hungry animal."
    "I've never seen Bree like this before, certainly never felt her like this before."
    "It's almost as though she's doing this because she feels that she had something to prove."
    "But what that is and to whom she had to prove it, I have no idea."
    "She's certainly proving to me that she has a wild side, and I'm glad of the hut wall to support me, so intense is the feeling of her lips and tongue on my cock."
    "I can feel her starting to squeeze my balls now, just when I thought that there was nothing more she could do to ramp up the pressure."
    "I'm honestly trying to keep my mouth shut, biting at my lip when I want to be shouting out loud."
    "Instead I make to with balling one of my hands into a fist and pounding it against the planks of the wall, hoping that it's sturdy enough to take the abuse."
    "If she takes me any deeper now, I'll literally be in her throat!"
    "And that's the thought that breaks me and lets Bree know that I'm starting to cum."
    show beach bj handjob cum
    "Quickly and deliberately, she releases me from her mouth so that she can receive the full effect of the orgasm."
    "Rather than being caught off guard when the cum spatters across her face, Bree seems to relish the sensation, even opening her mouth to catch what she can of it."
    "I look down at her, still panting and exhausted as I let the wall do most of the work of keeping me on my feet."
    bree.say "I don't suppose you remembered to bring something for me to clean up with?"
    "Bree laughs as I shake my head, already beginning to lick at the cum on her lips as she does her best to make herself look presentable again."
    hide bree
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
