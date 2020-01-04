label kleio_talk_love:
    show kleio
    kleio.say "I mean, what is love, really?"
    hero.say "What do you mean?"
    "Kleio leans back, scoffing off the idea almost entirely."
    kleio.say "It just feels like—I dunno, a sham I guess?"
    kleio.say "Like, people put all this pressure on people and their relationship to be that perfect thing, the best one possible, their soulmate—blech—and it just feels so disingenuous, you know?"
    kleio.say "A product of, at best, a materialistic society, and, at worst, a way to make sure the spirits of the general public are always disappointed."
    menu:
        "Disagree":
            "I shuffle, feeling somewhat uncomfortable. I was raised on the idea that there’s one person out there for you."
            "Although, I’m not one hundred percent sure I really believe in soulmates, I definitely think there’s someone out there for me, designed to perfectly reflect me."
            "Hesitantly, I decide to explain this to her."
            hero.say "I dunno, Kleio. I can see where you’re coming from, but honestly, I do think that someone is out there for me."
            hero.say "Like, someone who really cares about me, reflects me honestly—sort of like a soulmate, I guess?"
            "She snorts, clearly amused."
            kleio.say "So you’re an idealist, huh? The world hasn’t broken you yet?"
            "Her words sting, but I don’t back down."
            hero.say "No. No, I guess not."
            "She sighs, staying silent for a moment. The pause is pregnant, uncomfortable."
            "Finally, she decides to break the silence, her voice much lower, and more far away than usual."
            kleio.say "I envy you, and your optimism. I used to be like you, [hero.name]."
            hero.say "And then what happened?"
            kleio.say "I learned the lesson that my parents always wanted to teach me: life isn’t fair."
            kleio.say "You get your heart broken, you get your dreams stomped on and your aspirations shrivel into dust."
            kleio.say "In a perfect world, yeah, I think soulmates would exist."
            kleio.say "But, our world is far from perfect, and I’ve had my heart broken one too many times to keep my hopes up."
            kleio.say "Frankly, It’s exhausting."
            hero.say "So, what, then? You just close yourself off, don’t let yourself feel things for people?"
            kleio.say "No, I mean I do, I just—you’re not gonna get it, [hero.name]. You’ll know when you know."
            hero.say "So, now I just have to wait on getting my heart broken?"
            kleio.say "I hope it doesn’t happen to you. But hope hasn’t gotten me very far yet, so...I don’t know."
            kleio.say "It’s basically inevitable, I guess."
            hero.say "Yeah..."
        "Agree":
            "I find myself letting out a small sigh of relief. Honestly, I hate the idea of soulmates, and it’s refreshing to hear that there isn’t any pressure in—well, whatever it is going on between us."
            "It’s just Kleio and I—no pressure."
            hero.say "It’s refreshing to hear that, in a weird way."
            kleio.say "Really? Most people find it depressing."
            hero.say "I mean, I guess it totally can be that way, but, honestly, it’s an insane amount of pressure to place on yourself and a relationship if you really believe in true love."
            hero.say "Plus, can you imagine how depressed you’d be all the time if you weren’t in a relationship?"
            hero.say "It’s much easier to just let things happen and the chips fall as they may."
            kleio.say "Thank god you agree."
            kleio.say "So many people have tried to change my mind on this, and, honestly, it just gets exhausting and weird."
            kleio.say "Relationships shouldn’t be based on some spiritual feeling or direction from the cosmos or the Great Beyond or whatever—they should be built on compatibility and communication and, basically, doing the best you can with what you’ve god."
            "I stifle a laugh, and, on instinct reach over to grab her hand."
            hero.say "Guess the Beatles had it wrong, huh? All you need is not love."
            "She smiles, looking down on our hands, but, for a brief moment, an expression I can’t read flashes across her face, before she returns to her familiar, smirking grin."
            kleio.say "Yeah. Exactly."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_sex:
    show kleio
    hero.say "Hey Kleio? Can I ask you a question."
    kleio.say "Depends. What kind of question?"
    "I squirm. It’s a question I’ve wanted to ask her for a while, but I’ve never been completely sure how she was going to take it."
    hero.say "It’s kind of a personal question."
    kleio.say "Well, then let’s just get it over with."
    hero.say "I’m sorry if this offends you, I just—I have to ask. How many people have you had sex with?"
    "Kleio lets out a loud, annoyed sigh, as though she had had this conversation a million times before, and was not in the mood for rehashing it."
    kleio.say "Look, [hero.name], I know some people take sex so damned seriously."
    kleio.say "I used to be one of them—I think every girl was one of them, at some point."
    "I raise an eyebrow, but stay silent, allowing her to go on."
    kleio.say "As I got older, though, I realized I was placing so much of my self-worth on how many people wanted to have sex with me, and my sex appeal, as though that was what determined and dictated my personality."
    kleio.say "On top of that, with me liking both men and women, the constant pressure on me to have these ulta-serious, very meaningful sexual encounters, lest I was looking for attention or not really bisexual, got too much for me."
    kleio.say "So, finally, I let all that bullshit go. Sex is sex, and I don’t place this inherent weight or meaning on any of it."
    kleio.say "It’s just a physical encounter between two people—any other weight I place on it is entirely at my discretion."
    menu:
        "Insist":
            hero.say "I appreciate that Kleio, but you didn’t answer my question."
            show kleio angry
            "Kleio lets out an annoyed groan, rolling her eyes."
            kleio.say "Didn’t I, though? The answer is I don’t know."
            "I could not hide my shock. She had no idea?"
            kleio.say "I know that may be too hard for your sexless pea-brain to comprehend, but it’s the truth. Take it as you will."
            "Uncomfortable and ashamed, I drop the topic, giving Kleio the space she needed, and mentally making a note to go get myself tested as soon as I can."
            $ kleio.love -= 1
        "Let go" if hero.charm >= 25:
            hero.say "You know, Kleio, that’s a really powerful perspective. I’m sorry I asked, and thank you for sharing."
            "Kleio looks at me sideways."
            kleio.say "So you don’t mind?"
            hero.say "So long as you’re being safe and you’re happy, who am I to judge?"
            "Kleio lets out a breath, and I catch the hint of a smile growing across her face."
            kleio.say "Yeah. Exactly. That’s how it should be, I think. Thank you for being understanding."
            hero.say "Anytime. And thank you for sharing."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_politics:
    show kleio
    kleio.say "Do you seriously want to talk about this? Now?"
    kleio.say "Isn’t there some sort of unspoken rule that people just don’t talk about politics?"
    hero.say "I mean, I guess sometimes it’s not a good idea. But it can also be beneficial to talk about them."
    hero.say "Healthy discussion is, well, healthy, and I think we’re both mature enough to handle it."
    kleio.say "Whatever you say, lover boy. Talk away."
    menu:
        "I am a conservative":
            hero.say "Well, I guess you could say I’ve been a conservative my whole life, so..."
            show kleio angry
            "Kleio doesn’t even allow me to finish my sentence before she snorts and rolls her eyes."
            kleio.say "Oh, God, are you serious?"
            "I shuffle uncomfortably. I knew she would have a bad reaction, but it still made me feel gross."
            hero.say "Yes, Kleio, I’m 100% serious. I know it’s not the popular opinion, or the politically correct opinion, but it’s my opinion."
            kleio.say "You realize I’m bisexual, right?"
            hero.say "Yes, I do?"
            kleio.say "And that I’m vegan, and have tattoos, and part Native American, right?"
            kleio.say "And that I literally go to protests, and talk about them often?"
            kleio.say "And that I say I’m feminist?"
            kleio.say "Jesus, [hero.name], why are you even fucking around me if everything you believe is the antithesis of who I am?"
            hero.say "I don’t exclude people from myself just because I don’t necessarily agree with everything they do. I think that’s immature, and, besides, I don’t think politics is that big of a deal."
            kleio.say "It’s a big deal when your beliefs concern my existence."
            hero.say "Kleio, I don’t want to argue with you."
            kleio.say "Whatever, [hero.name]. Forget I asked, and keep living in your damn bubble. Maybe I can pop it someday."
            $ kleio.love -= 1
        "I am a liberal":
            hero.say "What else do you expect from a 20-something living in an apartment in a big city, playing in a band where I have to crossdress? I’m a liberal."
            "Kleio sighs, a sigh suspiciously tinged with relief, and smirks."
            kleio.say "I’m glad to hear that. Not that I don’t respect everyone, but, well, I don’t think everyone respects me."
            hero.say "Well, I definitely do. In fact, I think you’re the coolest goddamned person I’ve ever met."
            "Her smirk breaks into a full smile, surprised by my honesty."
            kleio.say "Thank you, [hero.name]. You aren’t too shabby yourself."
            "Both of us smile now, relieved to exit this conversation as gracefully, and as quickly, as we can."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_food:
    show kleio
    hero.say "What’s your favorite food, Kleio?"
    "Kleio looks at me, bewildered, hiding a smile."
    kleio.say "My favorite food? What is this, an interview?"
    hero.say "I’m just curious! I’m not much of a cook, but maybe, if it’s something simple, I can make it for you sometime."
    "She laughs, but I can tell that what I said had an impact on her. Hiding a blush, she begins to explain."
    kleio.say "Well, it sounds stupid, but when I was a kid, we grew up really poor."
    kleio.say "Like, really, really poor."
    kleio.say "Trailer park trash, I guess you could call us."
    kleio.say "So most of my childhood meals were just, like McDonald’s, or whatever was fast and cheap and easy to get."
    kleio.say "But, sometimes, if there was a special occasion, my mom would make this amazing soup."
    kleio.say "It was called three sisters soup, which I thought was after my sisters and I, but it turns out it was a traditional native American dish my grandmother taught her."
    kleio.say "It was basically just corn, squash, and beans, but honestly, to me, it tasted like fine dining."
    "I still think about that soup sometimes."
    "A lot, actually."
    menu:
        "I can take you to fast food":
            hero.say "Well, I can’t really make soup, but we can always go out to fast food whenever you want."
            "Kleio laughs, but flinches, her eyes looking sort of far away. I realize that my joke hit her a little too close to home."
            kleio.say "Yeah, of course, [hero.name]. I love fast food—reminds me of my childhood."
            "Her voice is light, but the hurt within it is unmistakable. Feeling ashamed, I turn my head, waiting for the conversation to drop."
        "I can cook for you." if "cooking" in hero.skills:
            hero.say "I’ll see what I can do. It probably won’t be as good as home’s, but I want to try—for you."
            show kleio happy
            "For a moment, Kleio’s face lights up with pure, child-like delight, before I see the cynical, adult her return, clouding her excitement."
            kleio.say "Well, I hope you’ll try—my mom is a pretty damn good cook, and it’d be hard to beat her."
            hero.say "I’ll do my best for you, one day—you’ll see. I promise."
            "Slyly, she looks up at me."
            kleio.say "Pinkie promise?"
            "I sigh, sticking out my pinkie to meet hers."
            hero.say "I pinkie promise, from the very bottom of my heart, that I will try to make three sisters soup as well as your mom did for you one day."
            kleio.say "Good. I’m holding you to that, you know?"
            hero.say "I know/ I’d hoped you would."
            "Smiling to herself, Kleio turns away, not allowing me to see the child-like delight forming unabashed on her grinning face."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_travels:
    show kleio
    "I ant to go volunteer in africa."
    $ kleio.love += 1
    hide kleio
    return

label kleio_talk_tv:
    show kleio
    "Tv is a druc used to keep the people under control."
    $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_sports:
    show kleio
    "I don't see why we should glorify stupid people that just know how to throw a ball."
    hide kleio
    return

label kleio_talk_fashion:
    show kleio
    "I look over at Kleio, her clothes so different and eye-catching, tears in strange places and colors so muddles, skin showing in every place you’d expect it to show and more..."
    "Before I even realize it, I have my mouth open, asking a question I didn’t even realize I had."
    hero.say "Kleio, why do you dress the way that you do?"
    "Kleio turns to face me, an eyebrow arched in suspicion."
    kleio.say "What do you mean?"
    "I stumble, desperate to not offend her, but also desperate to know, to really get inside her head."
    hero.say "I mean, you always wear these really grungy clothes, and they’re always, like, black or grey with these really bright pops of colors, and they always have tears in them, and, I mean, I get fashion, I do, but like...why?"
    "Kleio hides a smile, looking slightly irritated but also strangely amused."
    kleio.say "It’s just how I’ve always been, I guess."
    "I’ve never been the type of girl to wear dresses or baby pink or whatever else girls are wearing these days—I like my hair short and I like my tattoos and skin showing, and I like that, when people look at me, they know, one hundred percent, that I couldn’t give less of a fuck about what they think."
    menu:
        "What’s wrong with girls in pink dresses?":
            "Her words shock me. In my panic to relate, the only words that come to mind are, probably, the worst words I could have possibly said."
            hero.say "What’s wrong with girls in pink dresses?"
            show kleio angry
            "Kleio scowls, realizing that, in my panic, I missed her point entirely."
            kleio.say "Nothing, dumbass. That’s just not who I am, and it never will be."
            "And, if you’re looking for that kind of girl, you had better start looking elsewhere, because you aren’t going to find her here."
            "I panic even more, struggling to back peddle."
            hero.say "No, no, Kleio, that’s not what I meant—"
            "She turns and looks back at me, her eyes empty and void of any emotion."
            kleio.say "It’s whatever, [hero.name]. I know what you meant."
            $ kleio.love -= 1
        "You look badass":
            "Her words almost seem to empower me, and, almost unconsciously, I find my hand pulling at a small hole in my jeans, wishing it was bigger, wishing I had more to show and as powerful of a reason to show it."
            "Quietly, I look at Kleio, her confidence rushing out of her pores, infecting me, as she waited for a reaction."
            hero.say "Kleio, that’s the most badass thing I’ve ever heard."
            "Kleio grins wildly, even doing a small spin to show off her outfit for that day, allowing my eyes to rake over her body, unabashed."
            kleio.say "Good. That’s the goal, isn’t it? Come on, lover boy, I can see it in your eyes—you want some cool clothes, too, don’t you?"
            "Gulping, I nod, and Kleio grins even wider, allowing the emotion to nearly take over her face as she reaches out to take my hand."
            kleio.say "Well, then we have no time to waste. Come on, then—let’s go get you some kickass fucking ripped jeans."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_books:
    show kleio
    "Kleio looks me dead in the eye, her face unreadable."
    kleio.say "You think I’m stupid, don’t you? Or, at least, that I think education is like, pointless, or whatever, don’t you?"
    menu:
        "Disagree" if hero.charm >= 25:
            hero.say "No! Of course not! I just wanted to read, Kleio. I’m sure you love to read—what’s you favorite book?"
            "Kleio rolls her eyes, but her unreadable anger seems to have subsided somewhat."
            kleio.say "You’re not going to believe me."
            hero.say "Of course I will. Who lies about their favorite book?"
            kleio.say "People always think that I’m lying about mine."
            hero.say "Well, I won’t. Pinkie swear. What is it?"
            "Kleio sighs, looking away from me before she’s able to answer."
            kleio.say "East of Eden."
            "My confusion is evident on my face. From her reaction, I was expecting something a little more juvenile. But East of Eden?"
            hero.say "The Steinbeck novel?"
            kleio.say "See! You don’t believe me."
            hero.say "No! No, I do—I promise. I was just a little surprised is all—the way you were talking, I thought you were about to say, like, a comic book or something like that."
            "She smiles shyly, clearly embarrassed."
            kleio.say "No, although I like those too. I guess people just seem to think that having tattoos takes away your ability to read, or something. I don’t know—people just never believe me."
            hero.say "Well, I do, and, for the record, East of Eden is a beautiful book. It’s easy to see why it’s your favorite."
            "Kleio smiles, nodding along, before gesturing back to my book, allowing me to finish up my novel."
            $ kleio.love += 1
        "Say nothing":
            "I hesitate, not quite knowing how to react. Before I can come up with an excuse, Kleio’s eyes rage as she cuts me off."
            kleio.say "So I’m right! You think I’m stupid!"
            hero.say "I just—Kleio, you have to understand—every interaction I’ve had with people who look like you dropped out of high school."
            hero.say "They hate school—it’s nothing against you, I just figured you were the same."
            "Kleio rolls her eyes, refusing to look at me."
            kleio.say "Didn’t they teach you in school not to judge a book by its cover? For the record, I have a degree in English, and my favorite novel is East of Eden."
            hero.say "I probably know more about books and academia than you do... Does that satisfy you a little bit?"
            "Ashamed, I duck my head."
            hero.say "I’m sorry, Kleio. I shouldn’t have stereotyped you like that."
            kleio.say "Damn right you shouldn’t have. Go back to your damn book—sorry I bothered you."
            "I return to my book, but I find myself unable to focus, the white-hot shame flaring deep in my chest at my hurtful words."
            $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_people:
    show kleio
    "People are plain stupid."
    hide kleio
    return

label kleio_talk_computers:
    show kleio
    "A tool to keep us under surveillance."
    $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_music:
    show kleio
    hero.say "Kleio, why do you like the music that you like?"
    "Kleio turns to face me, looking almost puzzled as to why I would ask such a question to her."
    kleio.say "Uh, isn’t it obvious?"
    "She gestures her hands out to her clothes, as though that will better explain the situation. I see what she’s getting at—her short hair, her studded clothes, her tattoos—it’s obvious that her music taste matches the aesthetic she’s going for."
    "But that misses the point of my question entirely—it points to how she shows she enjoys it, but doesn’t actually answer why. Tentatively, I swallow, readying myself to attempt explaining this to her."
    hero.say "I get that you’re into punk and alternative stuff and whatever—it’s obvious. But Kleio, that just indicates to everyone else that you enjoy it. But it doesn’t actually tell me why."
    kleio.say "Can’t the answer be that I just like the look of it?"
    hero.say "It can be, but I don’t want to believe that you’re that shallow. You care about your music too much just to listen to it for your fashion sense."
    "Kleio rolls her eyes, but I can see my words get to her. Sighing, she slowly begins to explain."
    kleio.say "I don’t know. When I was a kid, I was ridiculed for any number of things—my heritage, my fashion choices, my sexuality—anything those kids could latch onto to tease me for, they would."
    kleio.say "My music became my armor, shielding me from the world in a way I couldn’t have done for myself. In a way, although it physically made me a loner, it emotionally made me realize I wasn’t alone."
    kleio.say "I feel like I owe my life to punk, hardcore rock music, in a way. Without it, I wouldn’t be the kickass person I am today. Does that make any sense?"
    $ kleio.love += 1
    menu:
        "Yes":
            hero.say "I think that’s awesome Kleio. Much better reason than mine for liking any kind of rock music—I just like guitars"
            "Kleio smiles, allowing me, for a brief moment, inside her walls."
            kleio.say "Yeah, well, it’s kinda silly crediting your life to a musical genre, but, what can I say. Plus, I’d have to agree with you—the guitars are pretty sick."
            "I smile back at her, leaning into her vulnerability and embracing it, hoping that she knows that, no matter how bad things get, she can always be her pop-punk self with me."
        "No":
            hero.say "I get why you did it then, but don’t you think you’d outgrow that tendency eventually?"
            "Kleio rolls her eyes, turning away from me, grumbling."
            kleio.say "I didn’t expect you to understand."
            hero.say "That wasn’t a slight against you, Kleio. I just figured that everyone outgrew their childhood armor, that’s all."
            "Spinning to face me, eyes flaring, I realize too late that my words have hit closer to home than I intended."
            kleio.say "Is it too much for your tiny dick brain to imagine that I’d want to dedicate some part of my life to the music that made me feel like it was okay to be me?"
            kleio.say "Yes? Alright, great, good thing that’s established."
            hero.say "Kleio, I—"
            kleio.say "Just shut up, [hero.name]."
            $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_birthday:
    show kleio
    "Thank you for remembering."
    $ kleio.love += 3
    hide kleio
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
