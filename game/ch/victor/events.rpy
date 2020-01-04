init python:

    Event(**{
        "name":"victor_event_01",
        "label": ["victor_event_01"],
        "duration": 2,
        "game_conditions":{"room":["nightclub"], "days_played":7, "flag_female":1},
        "do_once": True,
        "quit": True,
        })

label victor_event_01:
    scene bg nightclub
    "I clocked the group of scary-looking guys in dark suits almost as soon as we were in the nightclub, filling most of the secluded booths in the VIP area."
    "They were all shaven heads and mean stares, as though they thought everyone in the place was trying to lean over their shoulders and hear their conversations."
    "But I've seen so many wannabe gangsters hanging around in clubs before that I just plain ignored them and got on with enjoying myself instead."
    "I figure that whatever they're up to, it's nothing at all to do with me, and if I leave them alone they should at least return the favour."
    "But as the night goes on, I can't help casting my glance over to them from the relative safety of the dancefloor."
    "And every time that I do so, it feels as if their numbers have increased since I last look, like they keep multiplying the second that I look away again."
    "I try to push them out of my mind and just keep on dancing, but they're giving me such a creepy vibe that pretty soon I can't think of anything else."
    show victor fly
    "It's then that I see another guy in a suit across the dancefloor, one that stands out from the rest."
    "While they all look like Eastern European mobsters, this guy's got long black hair, a stubbly beard and cheekbones to die for."
    "I can feel my heart beating a little faster at the sight of him, he's just got such almost film-star looks."
    "His eyes are dark and intense, and he looks like he spends most of his time brooding over how much the world hurt him in the past..."
    "While I'm busy mooning over him, I hardly notice that he's walking intently towards the gangster-types in the VIP area."
    "They're already rising from their seats and some of them seem to be disappearing into the crowd at his approach."
    "I see the dark-haired guy's gaze flick left and right as he notes their movements, and his right hand slip under his jacket."
    "Oh fuck - surely not!"
    show victor firefight
    "Before I can see what he pulls out in his hand, I feel someone grab me from behind."
    "My scream isn't enough to cover the sound of guns being fired close by me."
    "And soon my scream is just one among many as panic spreads throughout the club at the sudden gunfight."
    "I'm dragged roughly backwards, and all that I can see of the person holding me hostage are his arms."
    "One of his black suited wrapped around my neck, the other is holding a huge pistol out in front of me."
    "Apart from that, all I can gather of him is the smell of his cheap cologne and the sound of his rough voice as he curses in what sounds to me like Russian."
    "I'm jerked this way and that as he struggles to point his gun at the dark-haired man."
    "His target seems to never be still, constantly weaving here and there amongst the crowd."
    "I can see a gun in his hand too, and he's firing as though he never ran out of bullets."
    "Every one of his shots seems to result in another gangster screaming in pain and falling to the floor at his feet."
    "The guy holding me is swearing now, and firing almost desperately at the dark-haired man as he sees his friends being cut down one by one before his very eyes."
    "Every time he pulls the trigger, the proximity of my head to his gun means that my ears ring and my vision swims from the explosive force of the shot."
    "Thus far, the dark-haired man seems to have been ignorant of my own captor."
    "But now a shot from his gun almost finds its mark, clipping his ear and causing him to finally turn in our direction."
    "He seems to dive to one side and raise his own gun to fire back at the same time."
    "I swear that I can see a small explosion of fire emerge from the barrel of his gun as the bullet intended for my captor emerges."
    "Time seems to slow to a crawl as the bullet travels through the air towards me."
    "And I'm utterly convinced that it'll hit me, not the gangster using me as a human shield."
    show victor firefight headshot
    "Then time returns to its normal flow, and I hear a sickening sound that I can only think is the bullet entering my skull and turning my brain instantly to a bloody pulp."
    "I feel no pain at all, but then that would probably make sense as I don't have time to do so."
    "Gravity pulls me down and I feel myself falling onto the nightclub floor, believing that the lights now above me are the last thing I'll ever see."
    "So I just lie there and wait for the inevitable to happen..."
    hide victor
    show victor wounded gun
    "But it doesn't - and then I see a face looming over me."
    man2_say "Hey, are you okay?"
    "It's the dark-haired man, looking down at me with concern written all over his face."
    "Wow - he's even cuter close up!"
    hero.say "You...you shot me!"
    "He shakes his head."
    man2_say "Ahh...no, I was shooting at him."
    "I follow the direction in which his finger is pointing, looking over my shoulder until I can see the man I'm currently laid atop."
    "It's the same guy that grabbed me, only now he has a bloody, smoking hole right between his eyes."
    hero.say "Arrggh...shit!"
    man2_say "Erm...are you gonna be alright?"
    "I'm laid on the corpse of a dead mobster in the middle the carnage caused by a full-scale nightclub shoot-out."
    "How in the hell am I supposed to ever be alright again?"
    "Somehow, when I look back at the dark-haired man with eyes like saucers and almost hyperventilating, he takes this as an affirmative answer."
    man2_say "Okay, good - look, I have to get the hell out of here, like right now!"
    hide victor
    "With that, he stands up and hurries to the closest fire exit, slipping out of the door and disappearing into the night."
    "I look after him for a moment, before realising that I'm still sitting on the other guy's rapidly cooling corpse."
    "Shrieking once more, I clamber off it and get as far away as I can."
    "All the time I'm wondering about the dark-haired stranger - just who he is and what his story could be."
    "Well, that and if I can ever take enough showers to feel clean again..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
