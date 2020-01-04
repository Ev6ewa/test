init -15 python:
    Activity(**{
        "name": "fuck_mike_female",
        "display_name": "fuck",
        "label":["ACTIVE_GIRL_fuck_ROOM_female"],
        "duration": 1,
        "game_conditions": {"hours":(20,25), "activity":"interact", "label":"ACTIVE_GIRL_fuck_ROOM_female", "flag_female":1},
        "girls_conditions": {
            "mike":{
                "min_love":150,
                "not_activity":["sleep"],
                "flagmin_sex":2,
                "active":True
                }
            },
        "once_day": "ACTIVE_GIRL",
        "icon": "fuck",
        })

label mike_fuck_bathroom_female:
    $ mike.set_flag("sex",1,"permanent","+")
    if sasha.room == game.room and not "sasha" in HIDDEN and sasha.get_flag_value("sex") >= 3:
        menu:
            "Should Sasha join in ?"
            "Yes":
                call shower_ffm_female
                return
            "No":
                $ sasha.love -= 2
    scene bg bathroom
    "Pulling off my top and kicking off my shorts, my feet hardly make a sound as I pad over to the shower door and open it with infinite care not to make as much as a sound."
    "The first thing that Mike knows about me being there is the sensation of my hands, as they reach out and grab his already soapy dick."
    show mike naked
    mike.say "Whoa - what the fuck?!?"
    "He jumps backwards in surprise, almost slipping on the wet floor of the shower as he does so."
    "As he tries to steady himself on the equally slick tiled walls, I can't help but giggle at his state of surprise."
    hero.say "Don't shit yourself, Mike - it's only me!"
    mike.say "Yeah, Bree...I can see that!"
    mike.say "You just made me jump, that's all."
    "I keep a hold of his cock as he talks, enjoying the sensation of just how slippery it feels between my fingers."
    hero.say "Hmm...seems like at least one part of you's glad to see me!"
    "I'm not making it up just for the sake of teasing him."
    "I can already feel it stiffening in my hand."
    mike.say "Well...yeah, of course I am."
    mike.say "But I was just trying to take a shower, that's all!"
    "I keep on laughing at whatever he says, shaking my head a little as I do so."
    "By now I'm standing so close to Mike that my nipples are starting to brush against his chest."
    "The sensation is beginning to have pretty much the same effect on me as my fondling of his cock is on Mike."
    "I might have snuck in here with mischief more on my mind than anything else, but I can already feel that I need more."
    "Not scratching that itch now will only end up with me lying in bed, feeling frustrated for most of the night."
    "Sure, I could easily take care of my self - but it's never as satisfying when you know what you could have had the real thing instead."
    hero.say "Oh come on, Mike - you can take a shower anytime."
    hero.say "You can only take me when I let you..."
    "I lean in and kiss him, full and slow on the lips."
    "He responds after perhaps a couple of seconds, wrapping his arms around me and leaning into the kiss."
    "I have his cock between my thighs now, working it up and down until it comes tantalisingly close to my neatly-shaved pussy."
    "Finally, once we're well into the thing and pressed against each other like a couple of amorous seals, Mike starts to wake up to just what's happening."
    "I can feel his hands begin to travel all over my body, exploring me as if he's never laid a finger on me before this moment."
    "It thrills me to my core whenever his touch passes over one of the seriously sensitive parts that are within his reach."
    "But even when he's doing nothing supposedly more erotic than stroking my arms or running his hands through my hair, the effect is almost the same."
    "By now I feel as though I'm going to beg if he doesn't do more, and soon."
    show bree showersex wet
    hero.say "Ah...Mike...put it inside of me...please!"
    "I twist in his arms, taking advantage of the fact that we're both slippery from the water."
    "Only stopping when I have his belly to my back, I grind my backside into his groin, too desperate for him to be in any way subtle."
    "He responds to me by looping his larger, more muscular arms under my own."
    "And then he pulls me backwards with a sudden and quite unexpected show of strength."
    "Taken by surprise, I have mere moments to guess at what's going on before I'm almost literally impaled."
    "Mike controls me with surprising ease, making sure that I go nowhere save for straight onto his eagerly awaiting cock."
    "Using his greater height and holding me at just the right angle, I sink down onto him gradually."
    "Even though I'm already slick down there and have been wanting this the whole while, there's still a degree of resistance."
    "But of course this only serves to make the sensation of his head stubbornly forcing it's way into me all the more intense."
    "The whole time it takes him to push into me as deeply as he's able can't be more than maybe ten seconds."
    "Yet to me it seems to stretch on into far longer, as the seconds become elastic and the feelings from down there matter more than the passage of time."
    "Mike holds me there, once he's buried himself as deep as he can go, tensed and stiff as an iron bar."
    "I can feel him starting to push me up against the wall, using it to make the angle at which he's inside all the more acute."
    "And then he begins to move, proving to me that I'd been wrong to think things couldn't get any better than they already were."
    "Only his lower body actually becomes animated, the rest of him tasked with holding me firmly in place."
    "But is it ever enough to make the entirety of mine feel like it's suddenly come to life on a whole new level."
    show bree showersex wet speed
    "I can't keep myself from beginning to moan and cry at the way in which he's making me feel as he thrusts in and out of me."
    "Flushed from the heat inside of the shower and the intensity of having him inside of me, I seem to be burning up more intensely with each moment that passes."
    "Soon I can sense the first tell-tale signs that Mike is getting ever closer to cuming."
    "His pace not only quickens still more, but becomes almost frantic as he tries to extract as much pleasure from me as possible before the inevitable happens."
    "And he begins to grunt with the continued effort of it all, like an animal fast approaching the end of its endurance."
    "As his body bucks and twinges, I can feel him trying to separate himself from me, fearful of the consequences if he does not."
    hero.say "No...Mike..."
    hero.say "Stay inside of me!"
    "Somehow he manages to hear and obey my last, gasped instructions mere moments before he's taken by his climax."
    "It can be touch and go as to whether a guy going off inside of me can push me over the edge."
    "But this time there was just no room for doubt, and Mike sets me off like one match lighting another."
    "I'm actually crying out now, unable to keep myself from doing so as my orgasm takes me and takes over all at once."
    "My legs give way, their muscles suddenly refusing to support my weight, and I'm grateful for Mike supporting me the whole time."
    "In all honesty, his support is also for the sake of keeping his cock in me until the very last possible moment, but I'm still grateful all the same."
    "We stay there, locked in an embrace until the last motes of strength has fled from out limbs and all there is left to do is collapse."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
