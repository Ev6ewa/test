layeredimage bg beach:
    if game.hour >= 20 or game.hour <= 5:
        "beach_night"
    else:
        "beach_day"

init -2 python:
    Room(**{
        "name":"beach",
        "bg": "beach",
        "display_name": "Beach",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "required_item": ["swimsuit", "vehicule"],
        "open_seasons":"1",
        "travel_time":2,
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"swimsuit"
        })

    Activity(**{
        "name":"swim_beach",
        "fun": 1,
        "fitness": 1,
        "duration": 2,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_grooming":3,"min_fun":3,"room":["beach"]},
        "display_name": "Swim",
        "icon":"swim",
        "say":[
            "I go for a swim in the sea...",
            "Swimming is good for what I have."
            ]
        })

    Activity(**{
        "name":"train_beach",
        "label": ["train_beach"],
        "fun": -5,
        "energy": -5,
        "hunger": -5,
        "grooming": -5,
        "fitness": 1,
        "duration": 6,
        "money_cost": 100,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_grooming":3,"min_fun":3,"room":["beach"], "flagmin_masterStory":1, "not_skill":"martial_arts","flag_female":0,"hours":(10,16)},
        "display_name": "Train",
        "icon": False
        })

    Event(**{
        "name": "bree_meet_the_master",
        "label": ["bree_meet_the_master"],
        "duration": 1,
        "game_conditions": {
            "days": "246",
            "hours":(10,16),
            "room":["beach"],
            "flag_masterStory":0,
            "flag_female":1,
            "chances":50
            },
        "do_once": False,
        "once_week": True
        })

    Event(**{
        "name": "mike_meet_the_master",
        "label": ["mike_meet_the_master"],
        "duration": 1,
        "game_conditions": {
            "days": "246",
            "hours":(10,16),
            "room":["beach"],
            "flag_female":0,
            "chances":50,
            "not_skill": "martial_arts"
            },
        "do_once": True
        })

    Event(**{
        "name": "beach_graduation",
        "label": ["beach_graduation"],
        "duration": 1,
        "game_conditions": {
            "days": "246",
            "hours":(10,16),
            "room":["beach"],
            "flag_female":0,
            "flag_masterStory":11,
            "not_skill": "martial_arts"
            },
        "do_once": True
        })

    Event(**{
        "name": "shark_attack",
        "label": ["shark_attack"],
        "game_conditions": {
            "hours":(22,6),
            "room":["beach"],
            "activity":"swim_beach",
            "flag_female":0,
            },
        "do_once": True
        })

label shark_attack:
    scene bg beach
    "I've almost made it to the point where the waves are crashing onto the sand, when I hear the sound of a vague and distant cry."
    "Glancing over my shoulder, I can see what looks like a lifeguard as she runs towards me down the beach in slow motion."
    "I groan and shake my head, thinking that I really don't have the time or patience for being lectured by some extra from Baywatch."
    "A quick look at how far away she is from me in comparison to the sea convinces me that I can be in the water long before she's even close."
    "I can always claim ignornace afterwards, say that she was just too far away for me to hear what she was trying to say."
    "My mind made up, I trot the last couple of feet into the lapping waves and then dive in as soon as the water becomes deep enough to do so."
    "Being a pretty strong swimmer, it doesn't take me long to get pretty far out, even before the lifeguard arrives at the edge of the water herself."
    "Now I have the sound of the waves to drown her out as well, and I make a point of not looking back over my shoulder as I swim further out."
    "But it's not long before I can make out a new sound that's loud enough to heard even over that of the waves."
    "It sounds like something big ploughing its way through the water behind me, and it's catching up fast."
    "Thinking that it's most likely more lifeguards, maybe on jet-skis or some kind of small boat, I decide that the game's up."
    show shark attack
    "I glance back over my shoulder, ready to give myself up and claim ignorance."
    "And it's then that I see something that instantly makes me pollute the small part of the sea in which I'm currently floating."
    "It's a shark, huge, ugly and like something out of cinematic nightmare."
    "And it's bearing down on me with its mouth wide open."
    "Bead-like black eyes stare at me over the gaping red maw and row after row of jagged, razor-sharp teeth."
    "I'm not frozen in place by the fear, but it does make me panic and reduce my strokes to a pathetic doggy-paddle."
    "I try with all of my might to push myself faster through the water, but everything happens so fast."
    "The shape of the shark looms over me, it's jaws closing faster than I ever thought it was possible for something to large to move."
    "There's no pain, but only because there isn't time for me to make sense of what's happening."
    "Everything is churning, white water and a red that isn't the shark's gaping mouth."
    "And then there's nothing but black..."
    $ renpy.full_restart()
    return

label beach_graduation:
    show master happy glasses
    "When I arrive at the beach and start looking for the Master, my head is already filled with guesses at what today's humiliating task might be."
    "But when I find him standing on the sand, hands behind his back and a huge grin on his face at the sight of me, I get the impression something's up."
    "It's not the fact that he's smiling that does it, as he must be pleased with himself for having pocketed a couple of hundred dollars of my money for his dodgy lessons."
    "I'm more intrigued by the way that he just stands there, making no move to beckon me this way or that, or else proffer the instrument of my daily torture."
    hero.say "Shall we get started, Master?"
    hero.say "I'm ready for today's lesson!"
    "Yeah, because that hundred dollars is just burning a hole in my pocket!"
    "The Master lets out a chuckle and gives me an approving nod."
    master_say "I am heartened by you enthusiasm, my boy."
    master_say "But there will be no lesson today, nor tomorrow, nor the day after that either."
    "Although I'm glad to hear that he won't be draining the contents of my bank account any longer, I'm still quite taken aback by the finality of the statement."
    "I honestly don't feel as though I've learnt that much from his lessons, let alone enough for them to come to an abrupt end."
    hero.say "Really, master?"
    "He nods curtly."
    master_say "I have taught you all that I can...well, all that I can be bothered to."
    master_say "There's actually quite a lot more that I could teach you, but something's come up, and I have to attend to it."
    master_say "So I'm fast-tracking you to graduation - I'm pretty sure I've taught you all that you need to know...probably."
    "I guess that all I can do is shrug and go along with what he's saying."
    hero.say "Yes, Master - thank you."
    show master glasses normal b
    "The Master nods for a moment, and then suddenly adopts what looks rather like one of the stances guys use in martial arts movies."
    hero.say "Erm, Master...what are you doing?"
    master_say "Now your skills are complete, my pupil - it is time for you to show me what you have learned!"
    "Is he serious?"
    "Oh god, he really does look serious!"
    "Licking my lips and gritting my teeth, I try to copy his stance."
    "I'm paying him for this shit, so he has to go easy on me, right?"
    "The Master makes some kind of whooping cry and comes at me with that uncanny speed and agility he shows on occasions."
    "I only just have time to see his fist coming from the left, and duck out of the way..."
    "Which allows him to neatly kick me straight in the groin."
    "Instantly I collapse onto the sand, curling up into a ball as I try to keep from vomiting."
    hero.say "You...you just kicked me in the balls...what kind of a martial art is that?!?"
    "The Master smiles down at me as I roll around in agony."
    master_say "When I said there were no more lessons, I lied."
    master_say "This is the last lesson I will teach you, my boy."
    master_say "No amount of fancy martial arts is a match for a good, hard kick to the balls."
    master_say "Goodbye, and good luck, my pupil!"
    hide master
    "And with that, he walks off, chuckling to himself at my expense, in every possible sense of the word."
    "All I can do is lie there, clutching my groin and trying not to puke."
    $ hero.skills.append("martial_arts")
    return

label train_beach:
    $ re = randint(1,5)
    show master glasses
    if re == 1:
        master_say "There you are, my pupil!"
        "I swear that there was no one in sight for as far as the eye can see when I turned my back a moment ago."
        "And that's how I justify jumping out of my skin and screaming like a little girl at the sound of the Master's voice."
        hero.say "Arrggh!"
        "He smiles in amusement at my being taken completely by surprise, unable to hide the fact that he's pleased with himself at getting such a reaction."
        master_say "First things first!"
        "He holds out his hand in silence, waiting until I pull out a wad of notes and press it into his palm."
        master_say "Very good - now the doors of the spiritual temple are open!"
        "I shake my head as I watch him pocket my money, wondering again if I haven't made a big mistake in trusting the old goat."
        master_say "Today, will work on your balance."
        "He turns and points to some of the pilings that run down the beach and into the sea."
        "Now this is something that I can relate to - everyone's seen the famous movie scene, haven't they?"
        "The one where the bullied kid learns that explosive kick by balancing on a piling just like those ones?"
        "The Master seems to notice my enthusiasm, and nods in approval."
        master_say "Shoes off, climb up - quickly now!"
        "Suddenly feeling a surge of excitement that comes mostly from retro eighties movies, I hurry to do as I'm told."
        "It's only when I actually get up there that I see the sheer amount of rough and splintered wood that I'm about to stand on with bare feet."
        hero.say "Erm...are you sure about this?"
        master_say "No questions - do as I say!"
        "At an honest guess, I'd say I manage to stay up there for all of five or six seconds before I simply can't take the pain any longer."
        "Falling off and rolling in the sand whilst wailing in agony, I hear the Master laughing at my expense for a second time."
        master_say "Congratulations, boy - you have learned the TRUE subject of today's lesson."
        master_say "If someone tells you to do something stupid - don't do it!"
        "He wanders off, still chuckling to himself as he leaves me to walk back to the car on all fours, cursing him for all I'm worth."
    elif re == 2:
        "I find the Master already standing on the beach as I trudge towards him, his back turned as he stares out to sea."
        master_say "Good morning, my boy."
        "Without turning around, his hand reaches out and he rubs his fingers together in anticipation."
        "I let out a resigned sigh and pull out the roll of notes to pay for today's lesson."
        "The Master gives a gleeful little laugh at the feel of the money in the palm of his hand and then nods."
        master_say "Today, you will learn all about endurance and patience."
        "From somewhere unseen, he produces a shovel and hands it to me."
        master_say "First of all - dig a hole, right here, five feet deep!"
        "He points to the sand by his feet, clearly meaning for me to literally dig the hole he just described."
        "I nod to show that I'm on the same page as him, and begin to dig as quickly as I can."
        "As soon as I have the hole dug, he points to the bottom with a bony finger."
        master_say "Now, get in the hole."
        "I look at him for a moment, just in case I heard him wrong."
        master_say "In the hole - NOW!"
        "The sudden yell makes me jump and hurry to obey as I scuttle into the hole."
        "As soon as I'm in there and looking up at him, the Master grabs to shovel and starts to drop the sand back into the hole."
        "I start to protest, but he silences he with a raised hand, and I so keep silent while he buries me up to my neck."
        master_say "Now, as the tide comes in, you will learn to be as enduring as the sea itself!"
        hero.say "Wait... what?!?"
        "Already I can see the tide fast approaching, rushing towards me as I'm trapped beneath the sand."
        "The first couple of waves don't quite reach my mouth, meaning that I can still shout for help."
        hero.say "Get me out of here!"
        master_say "If you truly believe that you can endure, the you will!"
        "The next waves are higher, almost filling my mouth with salt water as I yell at the Master for help."
        hero.say "Ack...gah...help me!"
        master_say "Mind over matter - endure!"
        hero.say "Endure my ass - get me out of here you crazy old bastard!"
        "I don't know if the reality of the situation dawns on the Master, or if he simply sees the chance of another hundred dollars slipping beneath the waves."
        "Either way, he scurries over and starts to dig my arms out of the sand."
        "With them free, I can finally drag myself out of the sand, still coughing and panting."
        master_say "Well, I think that was a lesson well learnt!"
        "In that moment, it's all I can do to keep from grabbing the shovel and swinging it at his head."
    elif re == 3:
        "I find the Master sitting cross-legged on the sand, apparently awaiting my arrival."
        "He has nothing at all with him, save for a gaudily-coloured bucket and spade, the kind a kid would bring to the beach."
        "I look at him expectantly, waiting for him to enlighten me either as to what today's lesson will be, or at least why he has the bucket and spade at his side."
        "The old man looks up at me with a grin on his face, and then holds up the palm of one hand, pointing to it with the index finger of his other."
        "I roll my eyes and produce the crumpled wad of bills to pay for the lesson, placing it in his eager hand."
        "Once the money has been stashed away about his person, the Master leaps to his feet in one spry motion."
        master_say "Good morning, my young pupil."
        master_say "Today's lesson will teach you how, by focusing on the smallest of details, one can come to understand the world at large!"
        master_say "In the time of the Samurai, those legendary Japanese warriors would arrange flowers for the very same reason and to the very same end."
        "I glance around the beach, seeing nothing in any direction save for sand and sea."
        hero.say "But, there are no flowers around here!"
        "At this, the Master grins and thrusts out a hand holding the bucket and spade."
        master_say "That, my boy, is why you will be making sand-castles instead!"
        "As much as I protest, the Master silences my objections and insists."
        master_say "Arranging flowers, building sand-castles - there is no difference."
        master_say "Now do as you are bid!"
        "Resentfully, I set about filling the bucket with sand and tipping it upside down onto the ground."
        "My first attempts all crumble and disintegrate without exception, at which the Master lambastes my efforts."
        "Things get better when I hit a vein of wetter sand, the my next series of castles hold together almost completely."
        "By the time I'm feeling like I've got the hang of it, the Master is grudging in his praise, but seems proud of the progress I've made in such a short time."
        "It's only when I finally stand up and work the kinks out of my back that the sense of achievement drains away."
        "Now I can see the steady stream of surfers, joggers and dog-walkers passing by and hardly trying to hide the signs of their amusement at what they see."
        "A grown man, making sand-castles at the behest of a crazy-looking old coot!"
    elif re == 4:
        "The Master meets me on the beach, but then waves for me to follow him as he makes his way towards the rockier portion of its length."
        "Picking his way over the uneven terrain, he leads me by perhaps a dozen or so rock-pools, gazing into each as he passes them."
        "Suddenly, he stops and becomes utterly fixated on one that, to me at least, looks little different to any of the previous ones."
        "I manage to catch his eye, and cock my head towards the pool that has him so fascinated, hoping to be enlightened as to just why."
        "He gives me a characteristic grin, and shakes his head as he holds out his hand."
        "I grudgingly hand over the money for the lesson, and watch as his smile grows broader still."
        master_say "Look deep into the rock-pool, my boy - tell me what you see."
        "Wanting to get value for money, I do as I'm told."
        hero.say "All I see are a couple of crabs, Master."
        hero.say "Nothing special, really..."
        master_say "Nothing special, nothing special!"
        "The Master splutters in exasperation at my answer."
        master_say "A crab is nature's most perfect analogy of the armoured warrior, boy!"
        "He squats down on his haunches and holds his hands up in the air, then starts to scuttle left and right around the edge of the rock-pool."
        "For a moment I honestly think that he's finally succumbed to creeping senility."
        "But as he starts to snap his fingers and thumbs together, I realise that he's trying to imitate a crab."
        master_say "The crab moves with cunning and speed, and his armour is matched in potency by the snip-snapping of his claws!"
        master_say "To understand his method of fighting, you must spar with him take him prisoner - you must capture him!"
        "The Master points at the rock-pool, and I find myself fishing around in the water a few moments later."
        "But the crabs are elusive and in their natural element, so have little trouble evading my clumsy grasp."
        "Most that I catch are unlucky enough to pinch one of my fingers and be flung out of the water when I yelp in pain."
        "I wonder where these unfortunate crustaceans are ending up, and stop to look around for them."
        "It's then that I see the Master, a bucket in his hand into which he's dropping the crabs that he plucks off of the rocks."
        "He sees me watching him with a frown on my face, and he gives me a shrug and a grin in response."
        master_say "As well as being nature's answer to the armoured warrior, they're also very tasty in a soup or stew!"
        "Before I can say something suitably waspish in return, I yelp as yet another crab latches onto my finger."
        "At this, the Master runs over, eagerly holding out his bucket before him."
    else:
        "I've walked up and down the beach a good few times before I finally manage to hear the sound of someone hissing at me from the dunes."
        "A quick scan of the closest of them shows me the face of the Master, leering at me from between two clumps of tall grass."
        "He waves me over, and I oblige him, stepping up my pace when I realise that he's urging me to come as quickly as I can."
        "Once I'm in amongst the dunes and squatting down next to him, I open my mouth to ask him just why we're hiding in here."
        "But he holds up a hand to silence my question even before I manage to get the words out."
        "Then I'm greeted by the familiar gesture of the hand reaching out for his money before he'll let us go any further."
        "Resentfully I hand over another portion of my hard-earned cash, and watch it disappear into his shirt pocket, never to be seen again."
        master_say "Today, our lesson will be one of stealth and evasion."
        "He reaches down into the grass at his feet and retrieves a camera that had apparently been there the whole time."
        master_say "Your task will be to emulate the mythical skills of the ninja."
        master_say "Specifically by taking this camera and capturing images of the unsuspecting bathers on the beach."
        "I narrow my eyes at this, wondering if I has more to do with sleaze than stealth."
        hero.say "Should I be looking for any type of bather in particular?"
        "The Master doesn't seem to see the obvious snare I've set for him, and nods intently."
        master_say "You should try to get the best shots you can of the young ladies in their bikinis."
        master_say "It's a scientific fact that a woman between the ages of eighteen and twenty-five possesses the most acute hearing of any human being."
        master_say "So they should prove the most challenging of all!"
        "Muttering under my breath about frauds and dirty old perverts, I crawl off through the dunes."
        "If I make it back from this one without being arrested as a Peeping Tom, I vow to test the Master's own hearing too."
        "Specifically by trying to sneak up on him and crack his skull with his own camera."
    $ game.set_flag("masterStory",1,mod="+")
    return

label mike_meet_the_master:
    "I don't normally spend much of my free time at the beach, but the weather was just so good today that I couldn't resist the temptation to pay a visit."
    "Of course, the great conditions mean that it's crawling with people by the time I arrive and try to weave my way to within at least a hundred feet of the water."
    "I spend most of my time twisting this way and that as I avoid a person coming one way and then have to dodge one coming in the opposite direction a moment later."
    "By my own estimation, I'm doing quite well up until the point that fate conspires to humiliate me in front of the beach-going crowds."
    "It's really nobody's fault, I just happen to be stepping aside for a couple of real beefcakes, when I slip on something underfoot and sprawl flat on my face."
    "The beefy guys don't even see me go down, and consequently one of them accidentally kicks sand in my face as he walks past where I'm laid out."
    "As I splutter and cough with a mouthful of sand, the little knot of girls sitting closest to me can't help but burst out in laughter at my predicament."
    "Picking myself up and dusting off as much of the sand as I can manage, I see that they're shrugging in sympathy at the same time too."
    "Hey, I can understand that - I guess it was pretty funny, even if it did happen to me."
    "I shrug back and set off on my way again, trying to put the whole incident behind me and just get on with my day at the beach."
    "But as I draw near the dunes that border the beach itself, I hear a voice calling out to me."
    geezer_say "Psst...hey, you!"
    show master glasses
    "I stop and survey the nearest dunes, and for my trouble I'm rewarded with the sight of a bald-headed old guy staring intently out at me from behind them."
    "He's wearing sunglasses and beach clothes, and is otherwise unremarkable save for his long, white goatee beard and moustaches."
    "Looking left and right first to make sure there's no one else around, I point to myself."
    geezer_say "Yeah, I mean you, kid - come over here!"
    "Intrigued enough to see what the strange old man has to say for himself, so I oblige him."
    "As soon as I'm within a few feet of him, the old man scuttles out of the dunes and begins to look me up and down."
    geezer_say "I saw what happened back there, son - I was watching the whole time!"
    "I'm about to ask him what he means by that, and why he was hidden in the dunes in the first place."
    "But then without warning, he jabs me in the chest with a bony finger."
    geezer_say "That's right, I saw those muscle-bound bullies shove you onto your ass in the sand."
    hero.say "Well, I actually kind of fell..."
    "The old man brushes my explanation aside with a shake of his hand."
    geezer_say "It's time you stopped making excuses, son!"
    geezer_say "I saw those girls laughing at you too!"
    geezer_say "The one's with the strappy bikinis and the huge...sunglasses sitting on the red towels!"
    hero.say "I was having a chuckle right along with them..."
    "Again, he waves me to silence."
    geezer_say "What you need, my boy, is someone to teach you how to defend yourself!"
    hero.say "I have taken some self-defence classes at the gym..."
    geezer_say "I'm talking about the ancient martial arts, son!"
    geezer_say "I am known as 'The Master' - you need to learn, and I can teach you!"
    "He pauses and gives a little cough before continuing on."
    master_say "For the very reasonable sum of one hundred dollars per lesson..."
    menu:
        "Refuse":
            hero.say "A hundred dollars per lesson - that's daylight robbery, you silly old fart!"
            "The old man seems genuinely taken aback, probably because he's used to gullible morons falling for his patter."
            master_say "Don't be foolish, my boy - this is a once-in-a-lifetime opportunity!"
            "I shake my head at his persistence, but start to walk away all the same."
            hero.say "Pardon me for saying so, but I always thought you found masters of martial arts in impressive dojos."
            hero.say "Not squatting in the dunes by the beach where they can see young skin on show and still toss themselves off without being seen!"
            hide master
            "I can still hear him protesting as I round the curve of the beach and begin to leave him behind."
            "Chuckling to myself at the guy's audacity, I try to turn my attention to relaxing like I always intended to."
        "Accept":
            "Part of me is sceptical about his claims, but then aren't the movies full of martial arts masters that lead pretty normal, boring lives?"
            "I mean, that Miyagi guy was a plumber, wasn't he?"
            "Dismissing the old man's claims out of hand might be a big mistake."
            hero.say "Okay, 'Master', or whatever you say people call you - I'll give you a shot."
            "At this, a smile spreads across the old man's wrinkled face."
            master_say "Ah, trust me, son - you won't regret this!"
            "I look at him sideways, still not totally willing to trust him."
            hero.say "I'd better not, because if this all turns out to be a crock of shit, I'll want my money back!"
            "The old man cackles and shakes his head at my words."
            master_say "That's good, boy - I'll teach you to stand up for yourself, just like that!"
            master_say "But don't worry about the money, this is more important than such petty material concerns."
            master_say "When I'm through with you, your mind and body will have been honed into a deadly weapon!"
            master_say "No one will ever kick sand in your face again!"
            "I give this declaration the best smile that I can summon, which is still pretty nervous."
            hero.say "Okay, great...when do we get started?"
            master_say "Meet me here when you are ready, my boy - and we will begin!"
            hide master
            "With that, he turns on his heel and disappears back into the dunes once more."
            "As I watch him go, I can't help wondering just what I'm getting into here!"
            $ game.set_flag("masterStory",1)
    "Most people just go to the beach to relax, but it's just my luck that I go along there and attract every nut job within a two-mile radius."
    return

label bree_meet_the_master:
    scene bg beach
    "It's not often that I get to spend any serious time down at the beach these days, what with work and my studies and everything else in a modern girl's life."
    "So when I do, I'm not one of those people who likes to spend all of their time messing around in the more crowded spots with the casual beach-goers."
    "I have a couple of more out-of-the-way spots that I always make a bee-line for, places where it's quiet and yet good for whatever particular pass-time I have in mind."
    "Today, that's sun-bathing, and so I make my way straight to a familiar path that leads behind the sand-dunes for about a half-mile or so."
    "If I take the right turn off and onto the beach itself, I'll find myself on a pristine spot of sand that catches the rays for the best part of the day."
    "There's usually no one else back here at this time of day, save for the really rare dog-walker."
    show master perv glasses
    "And so when I see someone up ahead that's just standing sideways on to me and looking out over the beach beyond the dunes, it comes as somewhat of a surprise."
    "Maybe it's because I wasn't expecting to see anyone at all that I seem to find him instantly intriguing."
    "But then there's also the fact that he's a pretty memorable character to consider as well."
    "As I get closer, I can see that he's an older guy, his pate bare from baldness rather than being shaved."
    "In fact, apart from his bushy white eyebrows, the only other hair on his head is a long, bushy goatee beard and moustaches that almost completely cover his mouth."
    "He has on pretty typical beach clothes, a blue shirt and tan shorts, as well as sandals."
    "It's when I take a look at his sunglasses that I realise he's actually craning his neck to see something on the other side of the dunes."
    "I can't make it out myself, but as I get closer, I see that his mouth is hanging open and his breathing is loud and heavy."
    "Shrugging it off, I guess that he must have been jogging, or at least walking at a pace and then stopped when something caught his eye."
    "By the time I get level with the old man, I glance over in the hope of seeing what's got him so entranced."
    "Over his shoulder, I see that there's a slight gap in the dunes."
    "Not enough to see the entirety of the beach - but more than enough to see the couple of dozen young girls sunbathing in their bikinis!"
    "That's when it dawns on me that the dirty old geezer is actually watching the rows of unsuspecting girls."
    "Which would account for both his intense interest and heavy breathing."
    menu:
        "Do nothing":
            hide master
            "The last thing that I want to do today is surprise a geriatric pervert in the middle of indulging himself like that."
            "So I simply turn my attention back to the path in front of me and quicken my pace as much as I dare without it looking obvious."
            "Pretty soon I leave the old man behind, and once he's out of sight, I feel that I can slow down again."
            "I make it to the spot where I was hoping to sunbathe soon afterwards, and spread my towel out on the sand."
            "But almost the same moment that I'm finished rubbing the sunscreen into my body, a thought occurs to me."
            "If the old perv's in the habit of sneaking around behind the dunes at the beach, he might well know about this spot too!"
            "Suddenly I can't shake the feeling that he could be lurking somewhere right now, leering at my glistening limbs, flat belly and perky chest."
            "I glance around as my paranoia takes hold, but there's no sign of anyone, nor any sunlight glinting off of a bald head either."
            "Laying down on my towel, I still don't feel entirely happy with the situation."
            "I resolve to put up with the inconvenience of tan-lines for the sake of the knowledge that didn't give the creep a free eyeful too."
            "In the end I don't stay as long as I would otherwise have done, and instead scuttle off home via another route perhaps an hour later."
        "Scold him" if game.get_flag_value("morality") >= 25:
            if game.get_flag_value("female"):
                $ NOTIFICATIONS.append(["{image=ui/icon_good.png}+1",2])
            $ game.set_flag("morality",1,mod="+")
            "The fact that I could so easily have been one of those poor, unsuspecting girls on the beach right now makes my blood boil."
            "And a guy as old as that one should really know better - I mean, most of those girls are young enough to be his granddaughters."
            "Oh my god - what if one of them IS his granddaughter and he's perving over her without knowing it?!?"
            "I can't just walk on by, I have to do something about it!"
            bree.say "Hey, just what do you think you're doing, buddy?"
            show master normal glasses
            "At the sound of my voice, the old man literally jumps a couple of feet in the air."
            "Which is quite an impressive feat for a man of his evidently advanced years."
            "His head shoots to the left and then the right as he searches for the source of the scolding."
            "And then, painfully slowly, he turns around to regard me with the guilty expression of a man that's been well and truly caught in the act."
            geezer_say "Ah...erm...were you talking to me, young lady?"
            "At the audible attempt at charm in his tone, I instantly cross my arms over my chest and fix him with a stern, disapproving look."
            "The old man clocks this immediately, and looks suitably sheepish in response."
            bree.say "Don't you 'young lady' me, you filthy old goat!"
            bree.say "You know exactly what you were doing just now - and so do I!"
            "He bobs up and down on the spot a little, and then casts a glance over his shoulder, as if seeing the view of the nubile young sunbather for the first time."
            geezer_say "Oh...oh...I see...I see what the source of your confusion is now!"
            "He lets out a nervous laugh as he rubs the back of his head and gives me what he clearly thinks is an innocent smile."
            bree.say "The only person confused here is you, if you think I don't know you were perving on those poor, unsuspecting girls over there!"
            "Ar this, the old man waves both of his hands at me in a desperate attempt to dismiss my accusations."
            geezer_say "No, no, no - that's not it at all!"
            geezer_say "While it might look like I was staring at those young ladies in their skimpy little bikinis..."
            "At the mention of bikinis, he seems to lose track of what he was saying for a moment, and has to actually shake his head to get back on track again."
            geezer_say "As I was saying - while it might look like I was staring at those young ladies, I was really doing nothing of the sort."
            "All I can offer in way of an answer is a derisive snort."
            geezer_say "No, really - you see I am a martial artist of some considerable skill and notoriety."
            geezer_say "And it's become my habit to come to this deserted part of the beach and train the muscles of my eyes by staring out to sea for hours on end!"
            "I shake my head in disbelief, scarcely able to credit the bullshit story he's spinning for me."
            bree.say "Martial artist, I don't think so - piss artist, more like!"
            bree.say "I'll give you two choices, grandad - either bugger off now, or else I call the police and see what they have to say about your crazy excuses!"
            "For all his claims of being a martial artist, the old man gulps and begins to sweat pretty quickly at the mention of my calling the police."
            "He glances this way and that for a moment, as if not sure of what to do, and then darts into the deeper dunes at the back of the path and disappears."
            hide master
            "Left alone, I'm not sure that I want to go on to the spot I'd picked for sunbathing now after all."
            "The thought that he might still be hanging around somewhere is creeping me out, and so I decide to turn around and retrace my steps instead."
        "Flirt with him" if game.get_flag_value("morality") <= -25:
            if game.get_flag_value("female"):
                $ NOTIFICATIONS.append(["{image=ui/icon_good.png}-1",2])
            $ game.set_flag("morality",1,mod="-")
            "While I'm contemplating whether to tear a strip off of the old pervert or else just walk on by, a strange notion suddenly occurs to me."
            "The old man seems pretty harmless, he's well-dressed and quite well-groomed too, and it's not like he's exposing himself or anything like that."
            "In fact, if I'd passed him in the street, I wouldn't have been freaked out by him in the slightest."
            "Maybe he just innocently stopped to look out over the sea and happened to be struck by how beautiful the sunbathers looked?"
            "I mean, it'd be patronising to think that such an old person shouldn't be turned on by the sight of young, hot flesh on show, wouldn't it?"
            "In fact, I can't help feeling a little jealous of those girls on the beach in an odd kind of way."
            "They could be responsible for stirring so many glorious memories in the bosom of this sweet, innocent old man, reminding him of his past glories."
            "When you look at it like that, it's almost poetic!"
            "And anyway, I'm willing to bet that I could stir more wonderful memories in the old coot than those air-headed little bimbos anyway!"
            bree.say "Well hello there!"
            "At the sound of my voice, the old man literally jumps a couple of feet in the air."
            "Which is quite an impressive feat for a man of his evidently advanced years."
            "His head shoots to the left and then the right as he searches for the source of the voice."
            "And then, painfully slowly, he turns around to regard me with the guilty expression of a man that's been well and truly caught in the act."
            show master normal glasses
            geezer_say "Ah...erm...were you talking to me, young lady?"
            "I smile broadly, trying to assure him that he's not being raked over the coals."
            bree.say "Well, I don't see anyone else around here - do you?"
            "The old man rubs the back of his head and licks his lips as he properly looks me over for the first time."
            "I can't honestly say that I blame him for the way that he swallows slowly."
            show master perv glasses at left
            show bree sexyswimsuit at right
            "After all, I have got on my skimpiest white bikini, the one with the top that's mostly strap and the bottoms that's all but a thong."
            "Crossing my arms over my chest, I make sure to squeeze my breasts tightly as I do so, making them bulge visibly."
            "Though I can't see them, I'm sure the old man's eyes are doing the same thing behind his sunglasses too."
            "His adam's apple bobs up and down in silent appreciation of what he's seeing and the fact that it's up close."
            geezer_say "This...this isn't what it looks like!"
            "I raise a quizzical eyebrow at this, as if I'm not fully convinced."
            bree.say "Okay - what is it that this should look like?"
            "The old man gulps again, and glances around one last time before he tries to explain himself."
            geezer_say "Well...you see...I happen to be a martial artist, one of some considerable skill and notoriety."
            "This is sounding better by the moment!"
            geezer_say "And I need to train the muscles of my eyeballs like any others in my body."
            geezer_say "So I've taken to coming here and staring out to sea for that very purpose."
            "Aww, it's so cute that he thinks he needs to cook up such a crazy excuse for just looking at some young girls at the beach!"
            bree.say "But you need to train them to look at stuff close up too, don't you?"
            "The old man looks totally nonplussed by the question, until I squeeze my chest just a little tighter for his benefit."
            geezer_say "Oh...yes, yes - that's exactly so, and you're such a perceptive young lady to realise that fact too!"
            bree.say "And you'd need to see something pretty intricate to watch, yeah?"
            "At this, he nods eagerly."
            bree.say "Say, something like a girl putting on sunscreen, maybe?"
            "By now, his head is bobbing up and down like a jack-in-the-box."
            bree.say "So if I were to, say...put my own sunscreen on right here, rather than when I get to my favourite spot on the beach..."
            bree.say "I'd actually be doing you a favour, right?"
            geezer_say "I..I'd be greatly obliged to you, young lady!"
            bree.say "Well, when you put it like that - do I really have a choice?"
            "Smiling to myself, I put down my bag and pull out the bottle of sunscreen inside."
            "I squeeze a generous amount into the palm of one hand, and then get to work."
            "Starting from my feet, I smooth the white cream into each leg, drawing my hands upwards in long, smooth motions."
            "Upon reaching my backside, I make a point of kneading each buttock as I work the sunscreen in."
            "I do my belly next, and then stroke the sides of my body until I reach my breasts."
            "Here, I turn my back on the old man so that I can undo my bikini top."
            "I look back over my shoulder as I slide my hands under the top and work the cream into my breasts."
            "The sight of him almost turned to stone as he strains to see as much as possible makes me grin with genuine amusement."
            "I can also see a bulge in his shorts that seems to suggest he's in pretty good shape as far as that department's concerned."
            "There's only my arms and neck to take care of now, and I wrap these up nice and quick."
            "I think he's had all the little treats he deserves for now anyway."
            "Fastening the back of my bikini top, I offer the old man a little wave before I shoulder my bag and set off on my way."
            bree.say "Hope that helped?"
            "The old man nods with almost crazed enthusiasm as he watches me go."
            bree.say "Oh, I'm so glad to hear that - maybe I'll see you around here again some time?"
            hide master
            hide bree
            "His nodding continues as I walk away down the path and he slowly disappears from sight."
    "Honestly, some of the people that you meet on an innocent trip to the beach!"
    "You really couldn't make this shit up."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
