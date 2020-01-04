screen message(what, title=""):
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        text title:
            size 30
            ypos -25
            xalign 0.5
            color "#ffffff"
            outlines [ (3,"#0099ff",0,0) ]
        text what:
            xalign 0.5
            ypos -25
            color "#ffffff"


screen calendar():
    on "show" action Hide("quick_menu")
    on "show" action Hide("say")

    add "smartphone"
    use ui
    vbox:
        xpos 475
        ypos 155
        xmaximum 445
        ymaximum 290

        xfill True
        label "Agenda" xalign 0.5
        for d in sorted(hero.appointments.keys())[:4]:
            for h in sorted(hero.appointments[d].keys()):
                for g in sorted(hero.appointments[d][h]):
                    if d == game.days_played:
                        $ s = "Date today at "
                    elif int(d) - game.days_played == 1:
                        $ s = "Date tomorrow at "
                    else:
                        $ s = "Date in "+str(int(d) - game.days_played)+" days at "
                    if g in GIRLS:
                        text s+str(h)+":00 with "+ GIRLS[g].name yalign 0.0
                    else:
                        text s+str(h)+":00 with "+ g.replace("_"," ").title() yalign 0.0
    frame:
        xpos 5
        ypos 715
        xanchor 'left'
        yanchor 'bottom'
        style_group "mm"
        has vbox:
            xalign 0.5
        textbutton "Cancel" clicked Return("None")


screen show_smartphone_info(girl):
    add "smartphone"
    use ui
    hbox:
        xpos 475
        ypos 155
        xmaximum 445
        ymaximum 290
        yfill True
        xfill True
        if renpy. has_image (girl.id+" smartphone"):
            add girl.id+" smartphone"
        vbox:
            xmaximum 220
            ymaximum 290
            xfill True
            vbox:
                xfill True
                text "Name : "+girl.name.capitalize() size 15
                if girl.status:
                    text "Status : "+girl.status.capitalize() size 15
                text "Age : "+str(girl.age) size 15
                if girl.get_flag_value("birthdayknown"):
                    text "Birthday : "+girl.birthday[0].capitalize()+ " " + str(girl.birthday[1]) size 15
                $ t = girl.get_flag_value("knowntraits")
                if t:
                    text "Traits : "+", ".join(t) size 15
            vbox:
                xfill True
                yalign 1.0
                spacing 2
                hbox:
                    spacing 5
                    yalign 0.0
                    python:
                        n = int((girl.love()/200.)*100)
                    add "ui/icon_love_vsmall.png" yalign 0.5
                    fixed:
                        ysize 25
                        bar value n range 100 ysize 25
                        text str(n)+"%" xalign 0.5 yalign 0.5
                hbox:
                    spacing 5
                    yalign 0.0
                    if girl.sub >= 0:
                        add "ui/icon_sub_vsmall.png" yalign 0.5
                    elif girl.sub < 0:
                        add "ui/icon_dom_vsmall.png" yalign 0.5
                    fixed:
                        ysize 25
                        if girl.sub >= 0:
                            bar value girl.sub() range 100 ysize 25
                            text str(girl.sub())+"%" xalign 0.5 yalign 0.5
                        elif girl.sub < 0:
                            bar value abs(girl.sub()) range 100 ysize 25
                            text str(abs(girl.sub()))+"%" xalign 0.5 yalign 0.5
                if girl.get_flag_value("lesbian"):
                    hbox:
                        spacing 5
                        yalign 0.0
                        python:
                            n = girl.get_flag_value("lesbian")*5
                            if n > 100:
                                n = 100
                            elif n< 0:
                                n = 0
                        add "ui/icon_les_vsmall.png" yalign 0.5
                        fixed:
                            ysize 25
                            bar value n range 100 ysize 25
                            text str(n)+"%" xalign 0.5 yalign 0.5
                if girl.get_flag_value("male"):
                    hbox:
                        spacing 5
                        yalign 0.0
                        python:
                            n = girl.get_flag_value("male")
                            if n > 100:
                                n = 100
                            elif n< 0:
                                n = 0
                        add "ui/icon_male_vsmall.png" yalign 0.5
                        fixed:
                            ysize 25
                            bar value n range 100 ysize 25
                            text str(n)+"%" xalign 0.5 yalign 0.5
                if girl.get_flag_value("yandere"):
                    hbox:
                        spacing 5
                        yalign 0.0
                        python:
                            n = girl.get_flag_value("yandere")
                            if n > 100:
                                n = 100
                            elif n < 0:
                                n = 0
                        add "ui/icon_yan_vsmall.png" yalign 0.5
                        fixed:
                            ysize 25
                            bar value n range 100 ysize 25
                            text str(n)+"%" xalign 0.5 yalign 0.5

transform rotate45:
    rotate -45

screen room(room):
    default h = False
    on "show" action Hide("quick_menu")
    on "show" action Hide("say")
    add "bg "+room.id
    default min = 0
    $ girls = room.get_present_girls()
    use ui
    hbox:
        xalign 0.5
        yalign 1.0
        yanchor "bottom"
        python:
            if min >= len(girls):min = 0
            shown_girls = girls[min:min+2]
        for g in shown_girls:
            if not g.get_activity()[1]["activity"] == "sleep" or game.get_flag_value("dateinprogress") == g:
                fixed:
                    yalign 1.0
                    yanchor "bottom"
                    xmaximum 550
                    ymaximum 720
                    add g.id xalign 0.5 yalign 1.0





    $ valid_activities = []
    $ ICONS = True
    for a in ACTIVITIES.values():
        if a.test():
            $ valid_activities.append(a)
            if not a.icon:
                $ ICONS = False
    if valid_activities or len(girls) > 2:
        frame:
            background None
            xpos 1275
            ypos 715
            xanchor 'right'
            yanchor 'bottom'
            $ f = [x for x in valid_activities if not x.icon]
            if not f:
                vbox:
                    spacing -14
                    box_reverse True
                    xsize 90
                    $ ali = 0
                    for idx, a in enumerate(sorted(valid_activities, key=lambda x: x.display_name)):
                        imagebutton:
                            auto a.icon+" %s"
                            hovered SetScreenVariable("h",((1205-(ali%2)*30,665-idx*46), a.display_name, "activity"))
                            unhovered SetScreenVariable("h",False)
                            action Return(a)
                            tooltip a.get_tooltip()
                            if ali%2 == 0:
                                xalign 1.0
                            else:
                                xalign 0.0
                        $ ali += 1
                    for g in shown_girls:
                        if not g.get_activity()[1]["activity"] == "sleep" or game.get_flag_value("dateinprogress") == g:
                            $ idx += 1
                            imagebutton:
                                auto g.id+" %s"
                                hovered SetScreenVariable("h",((1205-(ali%2)*30,665-idx*46), "Interact with "+g.name, "activity"))
                                unhovered SetScreenVariable("h",False)
                                action Return(g)
                                if ali%2 == 0:
                                    xalign 1.0
                                else:
                                    xalign 0.0
                            $ ali += 1
                    if len(girls)>2:
                        $ idx += 1
                        imagebutton:
                            auto "next %s"
                            hovered SetScreenVariable("h",((1205-(ali%2)*30,665-idx*46), "Look around", "activity"))
                            unhovered SetScreenVariable("h",False)
                            action SetScreenVariable("min",min+2)
                            if ali%2 == 0:
                                xalign 1.0
                            else:
                                xalign 0.0
                        $ ali += 1
            else:
                vbox:
                    xsize 200
                    for a in sorted(valid_activities, key=lambda x: x.name):
                        frame:
                            xfill True

                            $ name = a.display_name
                            $ name = name[0].upper() + name[1:]
                            textbutton name:
                                clicked Return(a)
                                tooltip a.get_tooltip()
                                xalign 0.5
                                ysize 35
                    for g in shown_girls:
                        if not g.get_activity()[1]["activity"] == "sleep" or game.get_flag_value("dateinprogress") == g:
                            frame:
                                xfill True
                                textbutton g.name:
                                    clicked Return(g)
                                    tooltip ["Interact with "+g.name]
                                    xalign 0.5
                                    ysize 35
                    if len(girls)>2:
                        frame:
                            xfill True

                            textbutton "Look around" clicked SetScreenVariable("min",min+2) xalign 0.5 ysize 35

    if h and h[2] == "room" and persistent.room_display == "h":
        frame:
            background None
            xsize 300
            yanchor "bottom"
            xpos h[0][0]
            ypos h[0][1]
            at rotate45
            text h[1] outlines [ (1, '#0099ff') ] color "#ffffff" xalign 0.0
    if h and h[2] == "room" and persistent.room_display == "v":
        frame:
            background None
            xsize 300
            xpos h[0][0]
            ypos h[0][1]
            text h[1] outlines [ (1, '#0099ff') ] color "#ffffff" xalign 0.0
    elif h and h[2] == "activity":
        frame:
            background None
            xanchor "right"
            xpos h[0][0]
            ypos h[0][1]
            text h[1] outlines [ (1, '#0099ff') ] color "#ffffff" xalign 0.0

    frame:
        xpos 5
        ypos 715
        xanchor 'left'
        yanchor 'bottom'
        style_group "m"
        if persistent.fast:
            $ rooms = [ROOMS[e] for e in room.exits if ROOMS.get(e,None) and ROOMS[e].test()]+[ROOMS[game.room]]

        else:
            $ rooms = [ROOMS[e] for e in sorted(room.alternate_exits) if ROOMS.get(e,None) and ROOMS[e].test()]+[ROOMS[game.room]]
        $ rooms = sorted(rooms, key=lambda x: x.display_name)
        if ROOMS["map"] in rooms:
            $ rooms.remove(ROOMS["map"])
            $ rooms = [ROOMS["map"]]+rooms
        if ROOMS["livingroom"] in rooms:
            $ rooms.remove(ROOMS["livingroom"])
            $ rooms = [ROOMS["livingroom"]]+rooms
        if ROOMS["mall"] in rooms:
            $ rooms.remove(ROOMS["mall"])
            $ rooms = [ROOMS["mall"]]+rooms




        if persistent.room_display == "h":
            hbox:
                spacing 1
                for idx, r in enumerate(rooms):
                    imagebutton:
                        auto "bg/"+r.id.replace("date_","")+"_button_%s.webp"
                        hovered SetScreenVariable("h",((90*idx,690), r.display_name.capitalize(), "room"))
                        unhovered SetScreenVariable("h",False)
                        if r.id != game.room:
                            clicked [SetVariable("game.room",r.id), Return()]
                        tooltip r.get_tooltip()
        else:
            vbox:
                box_reverse True
                spacing 1
                for idx, r in enumerate(rooms):
                    imagebutton:
                        auto "bg/"+r.id.replace("date_","")+"_button_%s.webp"
                        hovered SetScreenVariable("h",((100,670-51*idx), r.display_name.capitalize(), "room"))
                        unhovered SetScreenVariable("h",False)
                        if r.id != game.room:
                            clicked [SetVariable("game.room",r.id), Return()]
                        tooltip r.get_tooltip()

screen ui():
    tag menu
    timer 1 action clean_notifications repeat True
    use keynav

    if not HIDE_UI:
        if persistent.notifications == True:
            vbox:
                ypos 40
                xpos 1275
                xanchor "right"

                for n in NOTIFICATIONS[-10:]:
                    text n[0].capitalize():

                        color "#FFFFFF"
                        xalign 0.0
                        yalign 0.5
                        outlines [ (1,"#0099ff",0,0) ]

        hbox ypos 5 spacing 5 xalign 0.5:
            vbox spacing 5:
                hbox spacing 10:
                    frame:
                        xpadding 10
                        ypadding 5
                        has hbox spacing 5
                        for n in ["energy","hunger","grooming","fun"]:
                            $ val = str(hero[n]())
                            if val == "0":
                                $ c = "_red"
                            elif val in ["2","1","3"]:
                                $ c = "_orange"
                            else:
                                $ c = "_white"
                            add "ui/icon_"+n+c+".png" yalign 0.5 xalign 0.5
                            vbox xmaximum 35 xfill True:
                                label val text_size 22
                    if game.get_flag_value("female"):
                        frame:
                            xpadding 10
                            ypadding 5
                            has hbox spacing 5
                            $ val = game.get_flag_value("morality")
                            if val >= 0:
                                $ ico = "good"
                            else:
                                $ ico = "bad"
                            add "ui/icon_"+ico+".png" yalign 0.5 xalign 0.5
                            vbox xmaximum 35 xfill True:
                                label str(abs(val)) text_size 22

                    frame:
                        xpadding 10
                        ypadding 5
                        has hbox spacing 5
                        for a in ["knowledge","fitness","charm"]:
                            add "ui/icon_"+a+".png" yalign 0.5
                            $ val = str(hero[a]())
                            vbox xmaximum 45 xfill True:
                                label val text_size 22
                    python:
                        money = str(hero.money)
                        if len(money) > 6:
                            money = money[0:-6]+"M"
                        elif len(money) > 3:
                            money = money[0:-3]+"K"
                    frame:
                        xpadding 10
                        ypadding 5
                        has hbox spacing 5
                        add "ui/icon_money.png" yalign 0.5
                        vbox xmaximum 80 xfill True:
                            label money+" $" text_size 22
                    frame:
                        xpadding 10
                        ypadding 5
                        has hbox spacing 10
                        python:
                            season = game.get_season()
                            icon = "ui/icon_"+season+".png"
                        add icon yalign 0.5
                        $ date = str(game.day)
                        vbox xmaximum 25 xfill True:
                            label date text_size 22
                        python:
                            icon = "ui/icon_day_"+str(game.get_week_day())+".png"
                        add icon yalign 0.5
                        $ hour = str(game.hour)+":00"
                        vbox xmaximum 75 xfill True yalign 0.5:
                            label hour text_size 22
                        if game.hour > 7 and game.hour <= 20:
                            add "ui/icon_day.png" yalign 0.5
                        else:
                            add "ui/icon_night.png" yalign 0.5
                hbox:
                    spacing 5
                    xsize 945
                    if GetTooltip():
                        frame:
                            xsize 653
                            ysize 35
                            xalign 0.5
                            has hbox:
                                xalign 0.5
                                spacing 10
                            for t in GetTooltip():
                                text t color "#FFFFFF" xalign 0.5






                    if game.get_flag_value("dateinprogress") or game.room in ["studio"] and game.get_flag_value("bandpractice") or game.room in ["kitchen","livingroom","bedroom1","bedroom2","bedroom3","bathroom","bedroom1","pool","secondfloor"] and game.get_flag_value("chores") < 100 or game.room in ["office","personal", "alettaoffice"] and game.get_flag_value("worksatisfaction") or game.get_flag_value("alarm_clock") and game.room == "bedroom1":
                        vbox:
                            xalign 0.5
                            xsize 287
                            if game.get_flag_value("dateinprogress"):
                                frame:
                                    ysize 35
                                    has hbox xmaximum 287 spacing 5 ysize 25 yalign 0.5
                                    label "Date" yalign 0.5 text_size 22
                                    $ score = game.get_flag_value("datescore")
                                    $ if score > 100: score = 100
                                    $ if score < 0: score = 0
                                    fixed:
                                        ysize 25
                                        bar value score range 100 ysize 25
                                        text str(score)+"%" xalign 0.5 yalign 0.5
                            elif game.room in ["studio"] and game.get_flag_value("bandpractice"):
                                frame:
                                    ysize 35
                                    has hbox xmaximum 287 spacing 5 ysize 25 yalign 0.5
                                    label "Practice" yalign 0.5 text_size 22
                                    $ score = game.get_flag_value("bandpractice")
                                    $ if score > 100: score = 100
                                    fixed:
                                        ysize 25
                                        bar value score range 100 ysize 25
                                        text str(score)+"%" xalign 0.5 yalign 0.5
                            elif game.room in ["kitchen","livingroom","bedroom1","bedroom2","bedroom3","bathroom","bedroom1","pool","secondfloor"] and game.get_flag_value("chores") < 100:
                                frame:
                                    ysize 35
                                    has hbox xmaximum 287 spacing 5 ysize 25 yalign 0.5
                                    label "Chores" yalign 0.5 text_size 22
                                    $ score = game.get_flag_value("chores")
                                    $ if score > 100: score = 100
                                    fixed:
                                        ysize 25
                                        bar value score range 100 ysize 25
                                        text str(score)+"%" xalign 0.5 yalign 0.5
                            elif game.room in ["office","personal", "alettaoffice"] and game.get_flag_value("worksatisfaction") and not game.get_flag_value('underinvestigation'):
                                frame:
                                    ysize 35
                                    has hbox xmaximum 287 spacing 5 ysize 25 yalign 0.5
                                    label "Promotion" yalign 0.5 text_size 22
                                    python:
                                        score = game.get_flag_value("worksatisfaction")
                                        end = WORK_DIF if not game.get_flag_value("promoted") else WORK_DIF_2
                                        percent = str(score*2) if not game.get_flag_value("promoted") else str(score)
                                        if score > end: score = end
                                    fixed:
                                        ysize 25
                                        bar value score range end ysize 25
                                        text percent+"%" xalign 0.5 yalign 0.5
                            elif game.room in ["office", "personal", "alettaoffice"] and game.get_flag_value("underinvestigation"):
                                frame:
                                    ysize 35
                                    has hbox xmaximum 287 spacing 5 ysize 25 yalign 0.5
                                    label "Investigation" yalign 0.5 text_size 22
                                    $ score = game.get_flag_value("workinvestigation")
                                    $ if score > 100: score = 100
                                    fixed:
                                        ysize 25
                                        bar value score range 100 ysize 25
                                        text str(score)+"%" xalign 0.5 yalign 0.5
                            if game.get_flag_value("alarm_clock") and game.room == "bedroom1":
                                hbox spacing 10:
                                    frame:
                                        ysize 35
                                        xsize 287
                                        $ score = game.get_flag_value("alarm_time")
                                        label "Alarm time : "+str(score)+":00" text_size 22 yalign 0.5

screen select_activity(valid_activities):
    default h = False
    on "show" action Hide("quick_menu")
    on "show" action Hide("say")

    use ui

    frame:
        background None
        xpos 1275
        ypos 715
        xanchor 'right'
        yanchor 'bottom'
        $ f = [x for x in valid_activities if not x.icon]
        if not f:
            vbox:
                spacing -14
                box_reverse True
                xsize 90
                $ ali = 0
                $ idx = 0
                imagebutton:
                    auto "cancel %s"
                    hovered SetScreenVariable("h",((1205-(ali%2)*30,665-idx*46), "Cancel", "activity"))
                    unhovered SetScreenVariable("h",False)
                    action Return("cancel")
                    if ali%2 == 0:
                        xalign 1.0
                    else:
                        xalign 0.0
                $ ali += 1
                for idx, a in enumerate(sorted(valid_activities, key=lambda x: x.display_name)):
                    imagebutton:
                        auto a.icon+" %s"
                        hovered SetScreenVariable("h",((1205-(ali%2)*30,665-(idx+1)*46), a.display_name, "activity"))
                        unhovered SetScreenVariable("h",False)
                        action Return(a)
                        tooltip a.get_tooltip()
                        if ali%2 == 0:
                            xalign 1.0
                        else:
                            xalign 0.0
                    $ ali += 1


        else:
            vbox:
                xsize 200
                for a in sorted(valid_activities, key=lambda x: x.name):
                    frame:
                        xfill True

                        $ name = a.display_name
                        $ name = name[0].upper() + name[1:]
                        textbutton name:
                            clicked Return(a)
                            tooltip a.get_tooltip()
                            xalign 0.5
                            ysize 35
                frame:
                    xfill True
                    textbutton "Cancel" clicked Return("cancel") ysize 35 xalign 0.5

    if h and h[2] == "activity":
        frame:
            background None
            xanchor "right"
            xpos h[0][0]
            ypos h[0][1]
            text h[1] outlines [ (1, '#0099ff') ] color "#ffffff" xalign 0.0

screen select(choices, title="", cancel="None", cap=True):
    on "show" action Hide("quick_menu")
    on "show" action Hide("say")

    use ui

    frame:
        xpos 5
        ypos 715
        xanchor 'left'
        yanchor 'bottom'
        xsize 330
        has vbox:
            spacing -5
            xfill True
        if title:
            label title.capitalize() xalign 0.5
        $ choices.sort()
        for sub in choices:
            hbox:
                xfill True
                if isinstance(sub,tuple):
                    if cap:
                        $ t = sub[0].capitalize()
                    else:
                        $ t = sub[0]
                    textbutton t:
                        clicked Return(sub[1])
                        ysize 35
                        xalign 0.5
                        if hasattr(sub[1], "get_tooltip"):
                            tooltip sub[1].get_tooltip()
                else:
                    if cap:
                        $ t = sub.capitalize()
                    else:
                        $ t = sub
                    textbutton t clicked Return(sub) ysize 35 xalign 0.5
        textbutton "Cancel" clicked Return(cancel) ysize 35 xalign 0.5

screen inventory():
    tag menu
    on "show" action Hide("quick_menu")
    on "show" action Hide("say")
    use ui

    frame xpos 5 ypos 715 xanchor 'left' yanchor 'bottom':
        has vbox
        textbutton "Back" clicked Return("exit")

    hbox xalign 0.5 ypos 45 spacing 5:
        vbox spacing 5:
            frame size_group "bb" xalign 0.5:
                label "EQUIPMENT" xalign 0.5
            if hero.inventory:
                frame size_group "bb":
                    has vbox
                    for e in hero.equipment.keys():
                        hbox ymaximum 29 yfill True xmaximum 300 xfill True:
                            label e.capitalize() yalign 0.5
                            $ i = hero.equipment[e]
                            if not i:
                                $ i = str(i)
                            else:
                                $ i = i.display_name.capitalize()
                            text i xalign 1.0 color "#FFFFFF"

        vbox spacing 5:
            frame size_group "bb" xalign 0.5:
                label "INVENTORY" xalign 0.5
            if hero.inventory:
                frame size_group "bb":
                    has viewport id "vp":
                        scrollbars "vertical"
                        draggable True
                        mousewheel True
                        xmaximum 460
                        ymaximum 625
                    vbox:
                        $ items = hero.inventory.keys()
                        for item in sorted(items):
                            hbox ymaximum 29 yfill True xmaximum 300 xfill True:
                                $ item = hero.inventory[item]
                                $ t = item.display_name.capitalize()
                                if item.nbr > 1:
                                    $ t += " ("+str(item.nbr)+")"
                                label t yalign 0.5
                                if isinstance(item, Equip):
                                    if item in hero.equipment.values() and game.room in ["bedroom1","bedroom4"]:
                                        textbutton "Unequip" clicked Return(item) xalign 1.0
                                    elif game.room in ["bedroom1","bedroom4"]:
                                        textbutton "Equip" clicked Return(item) xalign 1.0
                                elif isinstance(item, Consumable) and not game.get_flag_value(item.name):
                                    textbutton "Use" clicked Return(item) xalign 1.0

screen choose_sex():
    frame:
        xalign 0.5
        yalign 0.1
        has vbox
        text "Choose your character":
            size 30
            ypos -25
            xalign 0.5
            color "#ffffff"
            outlines [ (3,"#0099ff",0,0) ]
        text "Would you like to play a man or a woman?":
            xalign 0.5
            ypos -25
            color "#ffffff"
    hbox:
        xfill True
        yalign 1.0
        imagebutton:
            xalign 0.25
            auto "ui/female_button_%s.png"
            action Return(1)
        imagebutton:
            xalign 0.75
            auto "ui/male_button_%s.png"
            action Return(0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
