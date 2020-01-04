layeredimage bg bedroom4:
    if game.hour >= 20 or game.hour <= 5:
        "bedroom4_night"
    else:
        "bedroom4_day"

init -2 python:
    Room(**{
        "name":"bedroom4",
        "exits": ["livingroom", "secondfloor","kitchen","pool", "bedroom1", "bedroom2","bedroom3","bathroom"],
        "alternate_exits": ["secondfloor"],
        "display_name": "My bedroom",
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "masturbate_bree",
        "fun": 1,
        "duration":1,
        "max_girls":0,
        "label":["masturbate_bree"],
        "icon":"masturbate",
        "game_conditions": {
            "room":["bedroom4"],
            "min_energy":0,
            "min_hunger":0,
            "min_grooming":0,
            "max_fun":3,
            "flag_female":0
            },
        "display_name": "Masturbate",
        "once_day": True
        })

label masturbate_bree:
    "I don't know about you, but there are just some nights when I know that I'm going to make my excuses to my housemates and slope off to bed earlier than normal for the sake of a wank."
    "Whether or not they have any clue as to what I'm doing, I really don't know - but my guess would be that they probably do the exact same thing themselves too."
    "I sometimes wonder if there have ever been nights on which all, or at least two of us were doing it at the same time, all without the knowledge of the others."
    "If I'm going to be completely honest, I've also thought about what I'd do if I had the chance to spy on either Sasha or Mike while they pleasured themselves."
    "The idea's pretty hot - but then I've wondered what it would add to the experience for me if I knew that one of them was watching me too..."
    "Anyway, I'm fairly certain that there's no one watching me tonight."
    "Which is all for the good - as I have quite the itch to scratch before I'll even think about sleeping."
    "Shut away in the sanctuary of my room, I quickly strip off my shorts and top before clambering into the bed."
    "Lying back and spreading myself out on the bedclothes, my mind begins to turn to the practicalities of the pleasurable task ahead."
    "Now then, decisions, decisions...what am I going to use tonight?"
    "There's always the most immediate option, using nothing but my own fingers."
    "But sometimes it can be nice to have a bit of a helping hand along the way too!"
    "Rolling onto my belly, I reach for the nearest drawer in my bedside table."
    "After a little fumbling around, I roll back with what I was looking for clutched in my hands."
    "I know that Sasha's kind of cornered the market around these parts with her reputation for being 'Little Miss Sex-Toys' and all that."
    "But if you ask me, there's something to be said for quality over quantity."
    "Especially when it comes to matters of the bedroom variety."
    "reclining on my side and propping myself up on one elbow, I gaze over the three dildos that I've retrieved from the drawer."
    "The first one is only about five and a half inches long, but it's a sweet little vibrator pink and good for a thrill all the same."
    "Next is an altogether more manly affair, measuring about eight inches and a bit more realistic in texture and feel."
    "I'll confess, this second one is kind of my go-to choice when I just want to get down to it without much fuss."
    "But then I have the big boy - all twelve inches of the shiny black dildo that I like to call 'King Dong'!"
    "Ah...every one of them looks so tempting."
    "I can imagine them all feeling so good once they're inside of me..."
    menu:
        "Use my fingers":
            "You know, they all look so good that I just can't decide!"
            "So I won't - I'll fall back on my own fingers instead."
            "Squeezing a little lube between my fingers and thumb, I make sure that it's warm before I allow my hand to travel downwards."
            "I slide it over the curve of my belly, and then down the inside of my thigh with a slow, methodical care."
            "There'd be nothing to stop me from making straight for the ultimate goal, but I kind of enjoy the anticipation of inching ever closer."
            "Also, this way I get to feel the tingling that's building up inside of me as the tips of my fingers draw ever closer."
            "But I still have to decide exactly where they're going to end their journey."
            menu:
                "Finger my pussy":
                    show bree mast finger
                    if game.get_flag_value("morality") >= 30:
                        $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                        $ game.set_flag("morality",1,mod="-")
                    "By the time my fingers are creeping between my thighs, I already know that I'm not going to be able to go any further."
                    "Just the sensation of their touch coming within inches of the skin that surrounds my pussy makes me sigh and instantly want more."
                    "And as this is all about giving myself permission to feel pure, guiltless pleasure - why resist such an honest and natural urge?"
                    "Stroking my fingers down either side of my outer lips, I can feel the gentle prickling of the shaved skin like tiny pinpricks."
                    "But the feeling that mirrors this from within my pussy is enough to make me sigh again, instantly applying more pressure in sympathy."
                    "Even before my fingers have ventured any further than the very edge of those soft, pink folds, I can already feel the slick warmth from within."
                    "This means that, by the time I first take a gentle, almost tentative stroke further inside, I feel it open like a moist, hot flower."
                    "The rhythm that now takes me over is purely instinctual, as I'm following nothing other than what's giving me the greatest amount of pleasure."
                    "When the resistance of my pussy has melted to a sufficient degree, I need no urging to push my fingers in as deep as I'm able."
                    "I start out slowly, sinking them in and just holding them there for a moment."
                    "Feeling the muscles quiver and writhe in sympathy, I begin to move them more quickly now."
                    "A few seconds later, my thumb had found the perfect angle to start stroking my clit."
                    "And now things really begin to get intense."
                    "Drawing my legs up to spread myself wider open still, my free hand wanders all over my body."
                    "Inevitably, it settles upon my chest, kneading and squeezing at one of my breasts in effort to release a measure of the tension building within me."
                    "By now, my fingers are moving so fast that I can actually hear the sounds that they're making inside of my pussy."
                    "I hadn't noticed before now, by what were gentle sighs have now become almost breathless pants."
                    "Even now I can feel the orgasm building inside of me, beginning a cascade from which I can't hope to escape."
                    "Unable to stop myself, I almost scream out loud as I cum, curling into a ball to better preserve the sensations."
                    if game.get_flag_value("pussyTraining") < 5:
                        $ game.set_flag("pussyTraining",1,mod="+")
                "Finger my ass" if game.get_flag_value("morality") < 0:
                    show bree mast finger ass
                    if game.get_flag_value("morality") >= -10:
                        $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                        $ game.set_flag("morality",1,mod="-")
                    "I'm just about to let my fingers creep ever closer to the first folds of my pussy, when a wicked thought strikes me."
                    "Walking my dry hand over my thigh and then down the curve of my buttock, I use it to spread my cheeks apart a little."
                    "The hand that's been well lubricated follows, taking advantage of the way in which my ass is now open to it."
                    "I may not be able to see just where it is as well as I might had it been playing with my pussy."
                    "But all the same, it doesn't take me long to find what I'm looking for, and gently trace out the circle of my rear hole with a fingertip."
                    "Unable to rely upon the thrill of what I'm about to do to make the hole nice and wet for me, I have to be gentler and more subtle."
                    "And so I begin with only one finger, lightly probing the puckered muscle of the sphincter."
                    "At first, I push no more than an inch inside, feeling the pull of the muscles as they begin to draw the digit in."
                    "But for all of my subtlety, I can already feel the sensation of my ass being violated a little at a time."
                    "As soon as I'm able, I push a second finger in and feel the delight intensify."
                    "Already my breathing is getting heavier and I feel like panting as I push yet another finger up there too."
                    "It feels as though I've reached a tipping point now, where it's easier to press on than to pull out again."
                    "Where before I was gently feeding a little at a time into my ass, it seems to be greedily swallowing ever more with each passing second."
                    "There's no need to keep my buttocks parted any longer, and so my other hand finds its way to my previously neglected pussy."
                    "Soon I have a hand working away at both, making me gasp and sweat from the sensations of two different holes at once."
                    "Even if I wanted to keep on going like this for much longer, I don't think I could resist the orgasm that I can already feel approaching."
                    "In the end, I can't be sure whether it's playing with my ass or my pussy that finally makes me cum."
                    "But either way, I find myself curled up into a ball in the middle of the bed as the climax washes over me."
                    if game.get_flag_value("assTraining") < 5:
                        $ game.set_flag("assTraining",1,mod="+")
        "Use the small vibrator" if hero.has_item("vibrator"):
            "You know what they say - size isn't everything!"
            "I've had enough fun in the past with the smallest of the dildos that I own to be sure it's a good choice for tonight."
            "Plucking the chosen toy from the bed, I squeeze a generous amount of lube into the palm of my hand and then spread it up and down the rubbery shaft."
            "But then it strikes me - now that I've made my choice, just what am I going to do with it?"
            menu:
                "Use it in my pussy":
                    "I'm not in the mood to reinvent the wheel tonight, and so when I can feel my pussy almost crying out for the vibrator in my hand, I choose to listen."
                    "Teasing the lips by rubbing the phallus around both sides, it's almost as though shouldn't have bothered to lube the thing up in the first place."
                    "Almost as soon as there's the slightest hint of it coming close to my pussy, I can already feel the folds becoming slick with anticipation."
                    "I turn the thing on, already feeling the vibrations from it travelling through my abdomen."
                    "When I finally come to slide the head of the dildo between my lips, it almost sinks into as though my pussy wants to eat the thing whole."
                    if game.get_flag_value("pussyTraining") >= 5:
                        show bree mast small
                        if game.get_flag_value("morality") >= 20:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        "I push the vibrator in slowly but steadily, enjoying every moment of feeling it sink into me."
                        "The sensation is made all the more intense by the revelation of just how hungry my body seems to be for it."
                        "Has it really been that long since I let go and indulged myself like this?"
                        "Already I can feel a flood of pleasure spreading out from my pussy, setting every inch of my skin on fire."
                        "And this only seems to intensify as begin, almost gingerly, to move the vibrator in and out."
                        "Soon my entire body is moving in time to the rhythm that the toy sets for me."
                        "I swear that even my breathing in and out is in perfect synchronisation to the vibrator pulling out and then plunging back into my pussy."
                        "Unable to recall just how long I've been using the thing on myself, I press on, working myself into a sweaty mess atop the already sodden sheets."
                        "By now I can almost hear the sound of the toy slipping in and out of me as loudly as I can my own moans of pleasure."
                        "At this rate, I don't think that I can hope to hold on much longer."
                        "And soon after that thought occurs to me, I'm proven right."
                        "The orgasm is intense, strong enough to make me lose hold of the vibrator, leaving it inside of me as I cum."
                        "I curl into a ball in the middle of the bed, both hands clutching helplessly at my groin, unable to pull the thing out."
                        "Again and again, I feel the walls of my pussy clench against it as I yelp in exquisite pleasure."
                        if game.get_flag_value("pussyTraining") < 10:
                            $ game.set_flag("pussyTraining",1,mod="+")
                    else:
                        show bree mast small pain
                        "Almost as soon as I begin to push the vibrator into myself, I can feel that there's something wrong."
                        "Instead of it just sinking in as I'd hoped that it would, the walls of my vagina seem to be resistant."
                        "They stubbornly refuse to yield, and no matter how hard I try, the vibrator will not slide in there."
                        "The problem is that my enthusiasm has already overtaken my awareness, and I don't stop trying until it's too late."
                        "I can now feel pain in the place of pleasure."
                        "At the very moment that I regain enough control to be able to think clearly, all but tear the vibrator out of my pussy."
                        "Curling into a ball with the weight of the pain and frustration that I'm feeling, I can almost sense the moment when the mood finally dies."
                "Use it in my ass" if game.get_flag_value("morality") < 0:
                    "As much as I can feel my pussy almost crying out for the vibrator, I'm just in one of those contrary moods tonight."
                    "And so I reach around with my free hand and part my buttocks just enough for the vibrator to squeeze between them."
                    "Using my fingers as a guide, I push the head of the toy towards the tight hole, knowing I'll need to force it to begin with."
                    "There's a moment of discomfort, but then I can feel the muscles of my ass pulling at the head of the vibrator, drawing it in."
                    "It's at this moment that I turn it on and begin to feel the sensation of it pulsing in my back-passage."
                    if game.get_flag_value("assTraining") >= 5:
                        if game.get_flag_value("morality") >= -20:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        show bree mast small ass
                        "Almost as soon as I can feel the vibrator sinking ever deeper into my ass, I feel myself melting inside."
                        "This would have been amazing to feel in my pussy, but there's just so much more that I can take this way."
                        "Where the toy would have been meeting the walls of my vagina, here it could almost be swallowed whole and lost forever."
                        "In fact, it's almost a struggle to keep in mind that I need to hold onto the thing!"
                        "With the vibrator well and truly inside of me, I no longer need a hand to part my buttocks."
                        "And so the newly-freed fingers soon find their way back around to my now sorely neglected pussy."
                        "With them stroking away, I'm now working at myself from both sides at once, quickly feeling the intensity of my pleasure increase as a result."
                        "But while my pussy's being played with, it's around the back where the most overpowering sensations are coming from."
                        "The muscles of my ass are twinging and twitching almost constantly now, causing the rest of my body to follow suit."
                        "Even the smallest movement sends shivers radiating outwards, reaching as far as my fingers and toes."
                        "I'm panting now, the sensation of what's happening to my ass almost dictating every breath I take."
                        "And the only other sound that I can hear is the slithering of the vibrator as it goes in and out of me, over and again."
                        "In the end, I can't be sure if I cum from the effects of the toy or the way it's making me stroke desperately at my clit."
                        "But either way I have no choice but to curl into a tight ball as the orgasm overtakes me."
                        "The last thing I can feel, as it fades, is the vibrator, as it slips slowly out of my slack and still twitching ass."
                        if game.get_flag_value("assTraining") < 10:
                            $ game.set_flag("assTraining",1,mod="+")
                    else:
                        show bree mast small pain ass
                        "Almost as soon as I begin to push the vibrator into my ass, something just doesn't feel right."
                        "I'd hoped that it would just sink in, as if the muscles of my ass were melting at its touch."
                        "But instead they remain taught and stiff, as if trying to actively push it out again."
                        "Caught up in the moment, I don't realise this really isn't going to happen until it's too late."
                        "Already I can feel the inevitable pain building down there."
                        "It's all that I can do to tear the thing out of my ass."
                        "The moment ruined, I can't help moaning softly, in agony and disappointment."
                "Suck it" if game.get_flag_value("morality") < 25:
                    "You know, this thing just looks so damn good that I could almost eat it..."
                    "I bring the vibrator to my lips, licking and gently kissing the tip as I turn it on."
                    "Instantly I feel the shivering motion of it against my tongue, which sends a thrill shuddering down my spine."
                    "Without another thought on the matter, I wrap my lips around the vibrator and begin to push it slowly into my mouth."
                    if game.get_flag_value("mouthTraining") >= 5:
                        if game.get_flag_value("morality") >= 10:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        show bree mast small mouth
                        "The moment that I can feel the sensation of the vibrator slipping into my mouth, I know I've made the right decision."
                        "There's no sensation of choking or the toy being simply too much for me to handle."
                        "Instead it feels as though every muscle and fibre in my jaw and throat are parting to let it through."
                        "I almost greedily push more of the vibrator's length into my mouth as soon as I'm able."
                        "And before too long, I can actually feel it pressing against the back of my throat."
                        "As I push it down further still, I can't help thinking that I must look like a perverted sword-swallower right about now!"
                        "But I'm so hungry for the thing that nothing can keep me from going as far as I'm able."
                        "Soon the muscles of my throat are working at the vibrator, trembling in sympathy with its movements."
                        "This deeper twitch and twinge of my muscles sends my free hand slinking straight to my pussy."
                        "Which I find wet and almost weeping with arousal, begging to be stroked in time to the movements of the vibrator."
                        "The toy is so deep in my throat by now that I'm having to breathe through my nose the whole time."
                        "This in turn exaggerates the sounds of my pleasure, turning them into almost feral noises that I grunt out whenever the chance arises."
                        "I don't know how much longer I can keep this up, as I'm already starting to feel light-headed..."
                        "So to feel myself beginning to cum a moment later is a welcome relief."
                        "Collapsing onto the bed, I almost yank the vibrator out of my mouth, breathing in ragged gasps as I do so."
                        "Unable to do anything more, I simply lie back and let the orgasm take me."
                        if game.get_flag_value("mouthTraining") < 10:
                            $ game.set_flag("mouthTraining",1,mod="+")
                    else:
                        show bree mast small pain mouth
                        "While it felt great when I was just playing with it in my mouth, the feeling doesn't last long."
                        "Almost the same moment the vibrator touches the back of my throat, things start to go wrong, and badly."
                        "Choking and retching at the obstruction in my airway, I can feel my gag-reflex kick in with a vengeance."
                        "A few seconds later, I throw up the contents of my stomach onto myself and the bedclothes."
                        "Which, as I'm sure you can imagine, rather kills the mood for me tonight!"
                        if game.get_flag_value("mouthTraining") < 5:
                            $ game.set_flag("mouthTraining",1,mod="+")
        "Use the medium dildo" if hero.has_item("dildo"):
            "I think I'll be safest with an old friend!"
            "I've had enough fun in the past with the medium-sized of the dildo that I don't hesitate to pick that one."
            "I squeeze a generous amount of lube into the palm of my hand and then spread it up and down the rubbery shaft, already enjoying the sensation."
            "Now, just where should it go?"
            menu:
                "Use it in my pussy":
                    "The way my pussy's feeling right now, there's only one place that this thing is going."
                    "I'm already so slick down there that the lube on the dildo almost feels like overkill as I begin to rub it against my lips."
                    "Almost without having to try, the head slips between them, as if it's greedily wanting to swallow the thing whole."
                    "It feels like the dildo's melting into me, becoming liquid as it enters my body."
                    if game.get_flag_value("pussyTraining") >= 10:
                        if game.get_flag_value("morality") >= 10:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        show bree mast medium
                        "It's not long before the dildo is as far into my pussy as it can possibly go."
                        "Every inch that it creeps further into me sees that pleasure that I can feel from it become ever more intense."
                        "When it reaches the limit and can go no further, that still doesn't seem to stop the sensations from mounting."
                        "Before I got started, I had no idea how much I wanted this, how much my body needed it."
                        "Part of me daren't move the dildo now that it's so deep inside, fearing to feel yet more."
                        "But another part of me is just too curious and needy to be able to keep from beginning to slowly move it."
                        "I'm rewarded the very second that I do so, with a new wave of sensations flooding me, each more intense than the last."
                        "My moans have been pretty quiet up to this moment, more subtle purrs than anything else."
                        "Now they begin to steadily mount, in sympathy to the increasing speed with which the dildo moves in and out."
                        "I find myself almost desperately trying to part the lips of my pussy further, as if this will let the toy sink in deeper still."
                        "The dildo is slick against my fingers, threatening to slip away thanks to the mixture of sweat, lube and other things on the palm of my hand."
                        "Yet somehow I managed to keep a hold of it, rather than losing it like a slippery bar of soap."
                        "Almost ramming the thing home by now, I can feel myself building towards a peak."
                        "And when it comes over me, the last thing that I feel is the dildo slithering out and onto the bed."
                        "I can still feel the warmth that my body's given it beneath me, as I curl up from the intensity of my orgasm."
                        if game.get_flag_value("pussyTraining") < 15:
                            $ game.set_flag("pussyTraining",1,mod="+")
                    else:
                        show bree mast medium pain
                        "I'd expected this to be plain sailing, especially with the mood that simply handling the dildo's gotten me in."
                        "But instead I soon find that my pussy seems to have ideas all of its own tonight."
                        "Even with the lube on the toy, the lips simply refuse to be moved."
                        "Maybe I was too wrapped up in what I thought I wanted to be able to know what I actually did."
                        "Whatever the cause, the result is a serious amount of pain."
                        "I toss the dildo aside before I hurt myself more seriously, biting down on my frustration as I do so."
                "Use it in my ass" if game.get_flag_value("morality") < 0:
                    "Taking it in the pussy would be nice, but somehow I feel a bit more perverse than usual tonight."
                    "Manoeuvring the dildo around the back, I begin to push it between my buttocks."
                    "I brace myself, knowing that this is going to be uncomfortable to begin with."
                    "But then I can feel the muscles back there start to move in response to its presence."
                    "Any moment now, they should start to pull it in."
                    if game.get_flag_value("assTraining") >= 10:
                        if game.get_flag_value("morality") >= -30:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        show bree mast medium ass
                        "While it took some encouragement to get started, a few moments later, the muscles of my ass all but eat up the dildo."
                        "It feels almost like I have to hold onto the thing firmly or else have it pulled from my slick fingers."
                        "Needless to say, the sensation that accompanies this is exquisite in the extreme."
                        "The combination of delightful pain from the stretching and relaxing of the muscles is simply euphoric."
                        "And the feeling of having the toy up there is something in of itself as well."
                        "My entire body seems to be quivering in sympathy to the way in which my ass is straining."
                        "Even before I start to work the dildo in and out, I can already feel myself flushing with pleasure."
                        "My free hand finds my pussy without as much as a conscious thought, stroking the outer lips and threatening to slip further inside."
                        "Soon the motions of the dildo round the back and the fingers in my front are working almost as one."
                        "Together, they're more than enough to make my legs begin to twitch and almost spasm."
                        "I can't help crossing and uncrossing them, unable to tell whether the movement is an effort to push things out or else keep them in."
                        "The same waves spreading out through my body are enough to set me yelping and crying in sympathy."
                        "Each new twinge that I feel sees me letting out a breathy moan and then biting my lip in an effort to relieve myself even a little."
                        "In the end, I have no idea whether I'm bringing myself off with the dildo or my own fingers."
                        "Maybe it's both, and then maybe it doesn't matter nearly as much as the fact that I can feel myself starting to cum."
                        "Unable to do any more, I feel my hands curl into tight fists as the orgasm takes me."
                        if game.get_flag_value("assTraining") < 15:
                            $ game.set_flag("assTraining",1,mod="+")
                    else:
                        show bree mast medium pain ass
                        "Something's wrong - even though there's bound to be some resistance, pushing the dildo into my ass shouldn't be this hard."
                        "But no matter how I try, the muscles of my ass simply refuse to play along."
                        "I should have known better than to push it, but I guess I'm so caught up in the moment that I keep on trying all the same."
                        "Soon the mounting sensation of pain is just too much, and I have to give in and just drop the toy onto the bed beside me."
                        "There's no salvaging this or trying with another point of entry, the mood's been killed off completely."
                        "Filled with pain and not a little frustration, I lie back and bite my lip in helpless annoyance."
                "Suck it" if game.get_flag_value("morality") < 25:
                    "I think of both my pussy and my ass, but then smile as I decide upon my mouth instead"
                    "Bringing the dildo up to my lips, the tip of my tongue pokes out in anticipation."
                    "Unable to wait another moment, I begin to push the toy slowly into my waiting mouth."
                    if game.get_flag_value("mouthTraining") >= 10:
                        if game.get_flag_value("morality") >= 0:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        show bree mast medium mouth
                        "I can feel every bump and contour of the dildo as I slide it into my mouth."
                        "Somehow it feels so much more erotic and exciting to have the thing between these lips than in my pussy or ass."
                        "Just the thought of what I must look like right now is enough to make me lick and caress the dildo all the more."
                        "As I only need one hand to keep the toy in place, the other soon finds my pussy."
                        "The fingers mimic the motions of the dildo as it pushes in and out of my mouth, stroking the folds with an equally intense need."
                        "But all the same, it's the feeling of the phallus between my lips that's really getting me off right now."
                        "I'm not the world's greatest expert when it comes to deep throat, but I know how to do it without gagging."
                        "And so I have no trouble relaxing the muscles of my throat and letting the dildo slip down still further."
                        "As soon as those same muscles begin to contract around the toy, I'm taken to another level by the sensation."
                        "I can't help but feel as though my entire mouth and throat have been transformed into a pussy."
                        "It's a freaky thought, I know - but for a moment, I'm immensely turned on by the idea of having one in place of my mouth."
                        "Imagining feeling it get wet in anticipation of being penetrated, the moist streams running down my chin."
                        "All before someone plunged a desperately hard cock in there and fucked it..."
                        "At the intensity of this thought, I can feel myself cuming."
                        "I gasp for breath once the dildo is out of my mouth, and only a little for the sake of catching my breath."
                        if game.get_flag_value("mouthTraining") < 15:
                            $ game.set_flag("mouthTraining",1,mod="+")
                    else:
                        show bree mast medium pain mouth
                        "I manage to get the dildo perhaps half of its length into my mouth, but no further."
                        "Already I can feel that there's resistance to pushing any more of it in there."
                        "And what I've already swallowed is not resting well, either."
                        "I only just manage to get the thing out before I start coughing and retching."
                        "It emerges with strings of thick spit dripping from it and dropping onto the bedclothes."
                        "Finally, I throw up a little in my mouth, but manage to swallow it back down again."
                        "With eyes streaming tears and the taste of bile still in my mouth, for some reason I seem to lose all interest in pleasuring myself any further."
        "Use the large dildo" if hero.has_item("large dildo"):
            "What the hell - I think I'll play the part of King Dong's most loyal and obliging subject!"
            "Go hard or go home, right?"
            "Of course, I have a little more time to think about my options as I lube up the dildo's impressive length."
            "I wonder what part of his adoring realm King Dong should grace with a visit tonight?"
            menu:
                "Use it in my pussy":
                    "With the dildo waving and wobbling in my hands, it almost feels like a divining-rod that's searching for my pussy."
                    "Which is just as well, as right now, that particular part of my anatomy is simply begging to be found."
                    "Gingerly I turn the toy upside down and push it towards the lips between my thighs."
                    "I can almost feel myself quivering with anticipation as I do so..."
                    if game.get_flag_value("pussyTraining") >= 15:
                        if game.get_flag_value("morality") >= 0:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        show bree mast big ahegao
                        "I have no choice but to turn the massive dildo upside down and hold it with both hands."
                        "This makes me feel like some kind of kinky warrior woman from a fantasy movie, wielding a mighty weapon to slay a magical beast."
                        "And while that might sound like an odd way to describe my pussy, it's feeling pretty fierce at the moment!"
                        "I move one hand down the shaft and closer to the head, using it to push the tip inside of me."
                        "The combination of the dildo's weight, all of the lube and how much my body wants this means there's only a token resistance at first."
                        "And then the lips of my pussy part slowly, allowing the dildo to inch its way into me."
                        "For a while it's nothing but excitement and ecstasy, as ever more of the length sinks in."
                        "But all too soon I feel it reaching the limits, filling me and being able to go no further."
                        "I feel a measure of frustration at this, wanting to push it further still and keep the same sensation going."
                        "With both hands still gripping the shaft, I begin to work the dildo inside of me with more vigour than before."
                        "If I can't have any more of it in me, then what's inside already will just have to work that much harder."
                        "Before the frustration can overtake me, I channel the energy into pushing the shaft in and out of my pussy."
                        "It's weight and girth are all brought to bear upon the most sensitive part of my body, and the effect is immediate."
                        "I find myself biting my lip so suddenly and with such force that the copper tang of blood fills my mouth."
                        "Still biting my lip when the orgasm comes, I fear for a moment that I've bitten straight through."
                        "But that doesn't stop me keeping my mouth shut as I whine and moan my way through the orgasm which follows."
                        if game.get_flag_value("pussyTraining") < 20:
                            $ game.set_flag("pussyTraining",1,mod="+")
                    else:
                        show bree mast big pain
                        "I don't know if my mind was so set on the large dildo that I just failed to notice that my pussy was not, or there was still some other unknown barrier in place."
                        "But either way, it doesn't take me long to realise that my most intimate parts are just not going to get with the plan."
                        "Even with both hands and all of that lube, the head still slithers around and shoots off to the side each time I try to push it inside."
                        "I guess that I just over-faced myself - though that does nothing to help with the frustration that I feel as I abandon my plans for some solitary fun."
                "Use it in my ass" if game.get_flag_value("morality") < 0:
                    "Even as the obvious idea of using the dildo in my pussy presents itself, I can almost feel a mischievous grin spreading across my face."
                    "What if I were to buck the trend and use the toy on another part of my body instead?"
                    "Instantly intrigued and more than a little turned on at the notion, I guide the dildo behind me and between my buttocks."
                    "With one hand on the head and the other on the bottom, I hunt for my asshole with the forefinger of the former."
                    if game.get_flag_value("assTraining") >= 15:
                        if game.get_flag_value("morality") >= -40:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        show bree mast big ahegao ass
                        "At first, it feels nothing short of ridiculous, as I struggle to feed the head of the dildo into me reluctant ass."
                        "It writhes and wriggles like a rebellious snake thanks to the lube on it and my hands, threatening to slip out of my grip on more than one occasion."
                        "This means that I'm probably too rough on the muscles of my anus as a result, worrying little about them as I force the thing inside."
                        "When I finally manage to do that, the pain is immediate and more than I had anticipated."
                        "But I've come this far, and so I grit my teeth before pushing on regardless."
                        "Inch by inch, ever more of the dildo creeps into my back-passage thanks to my own stubborn efforts."
                        "And as it does so, some form of sensual alchemy transmutes the pain I'm feeling in my muscles to an exquisite delight."
                        "Now each new increment of the shaft being forced into me results in new and delightful feelings spreading outwards from my ass."
                        "This is where the advantage of choosing to use this hole over the other one in close proximity becomes apparent."
                        "Where I would have been reaching the limits of just how much my pussy could take, there's no such problem with my backside."
                        "By now, almost all of the length that I can safely let it take is well and truly inside of me."
                        "And yet still I can feel the muscles pulling on the thing, making me worry that, if I'm not careful, it could actually get stuck up there!"
                        "Ironically, it's this worrying that makes me begin to desperately pull the dildo out of my ass sets off my inevitable orgasm."
                        "As I struggle to retrieve the thing from the iron grip of my ass, I find myself pulling with ever more force and determination."
                        "And then, all of a sudden, my anus gives up the prize, meaning that it's almost torn out of there with surprising speed."
                        "The sheer sensation of this is enough to send me curling into a tight little ball in the middle of the bed."
                        "Once there, all I can do is whimper and twinge in sympathy with the twitching muscles of my tender backside."
                        if game.get_flag_value("assTraining") < 20:
                            $ game.set_flag("assTraining",1,mod="+")
                    else:
                        show bree mast big pain ass
                        "Perhaps it's on account of how clumsily I have to work the dildo around and into my ass that things begin to go wrong."
                        "But whatever the true reason, I soon feel like someone trying to force a lubed-up snake into a drainpipe whilst blindfolded."
                        "When I finally do manage to push the thing in no more than an inch, it twists and turns, poking the sides of my ass painfully."
                        "It's not too long before I'm bruised, exhausted and too frustrated to do any more."
                        "Cursing myself for choosing the largest and therefore most awkward of the three toys, I realise that the itch just isn't going to get scratched tonight."
                "Suck it" if game.get_flag_value("morality") < 25:
                    "This might seem like the least obvious choice of all, but something just won't let me get the notion of sucking on the massive dildo out of my head."
                    "Ah, what the hell - so long as I'm careful, there's not that much chance of anything going wrong, is there?"
                    "Gingerly, I raise the head to my lips, licking them nervously as I do so."
                    "And then, I start to push it slowly into my waiting mouth."
                    if game.get_flag_value("mouthTraining") >= 15:
                        if game.get_flag_value("morality") >= -10:
                            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
                            $ game.set_flag("morality",1,mod="-")
                        show bree mast big ahegao mouth
                        "Carefully taking the first couple of inches into my mouth, I wait to check that I can breathe before I go any further."
                        "Duly satisfied, I begin to feed in more as soon as I'm able."
                        "The fun doesn't truly start at this stage in the process, as there's far too much of it to play with in my mouth."
                        "Only when I can start to take the head and some of the shaft into my throat do things begin to get really interesting."
                        "Now I'm not the world's expert when it comes to deep throat, but I can hang when it comes to that kind of thing."
                        "And I'm already wondering just how much of this thing I can safely take before it gets out of hand..."
                        "I can feel the muscles of my throat start to contract around the shaft of the dildo as it inches ever further down."
                        "The sensation is so intense and exciting that my free hand slides down between my legs without as much as a conscious thought."
                        "While my throat works on the dildo, my fingers begin to stroke the lips of my pussy in sympathy."
                        "Soon each contraction is matched by a delving into the soft, slick folds."
                        "I can't be sure which feeds the other more, but soon I find myself working both my throat and pussy with serious intensity."
                        "If my throat were clear of obstruction, the sound of my moaning and sighing would no doubt be filling the room."
                        "But as it is, all I can hear is the muffled sounds that I'm managing to make."
                        "That, and the liquid noises that my fingertips are making at the same time between my hot, slippery thighs."
                        "When the inevitable orgasm does come over me, it's all that I can do to tear the dildo out of my mouth in time."
                        "Drenched in sweat and gasping for breath, I collapse onto the bed and let the throes of my climax take me."
                        if game.get_flag_value("mouthTraining") < 20:
                            $ game.set_flag("mouthTraining",1,mod="+")
                    else:
                        show bree mast big mouth pain
                        "I'm no amateur when it comes to blow-jobs and having large objects in my mouth."
                        "But all the same, I can soon tell that I've over-faced myself this time."
                        "The head of the dildo strays off course, jabbing me in the back of the throat and making me gag."
                        "Immediately I cough up half of my last meal, which is impeded in its exit by the dildo still in my mouth."
                        "All I can do is swallow again as soon as the toy is out of my mouth, tasting the vomit in my throat the whole time."
                        "Needless to say, that kills my passion for the night, and I go to bed feeling nausious and frustrated in the extreme."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
