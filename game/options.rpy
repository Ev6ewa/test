












define config.name = _("Love & Sex : Second Base - Public Edition")




define gui.show_name = True




define config.version = "19.12.2"





define gui.about = _("")






define build.name = "LoSeSb-Public"






define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = None
define config.window_hide_transition = None







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "LoSe_19_10-1512630773"



define build.itch_project = "andrealphus/love-sex-second-base"






define config.window_icon = "gui/window_icon.png"






init python:




















    patreon = True
    if patreon:
        config.name = _("Love & Sex : Second Base - Patreon Edition")
        build.name = "LoSeSb-Patreon"


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)
    build.classify('game/**.xcf', None)
    build.classify('geany_project.pj', None)
    build.classify('game/elite.rpyc', None)
    build.classify('game/debug_tools.rpyc', None)
    build.classify('ideas.txt', None)
    build.classify('game/**.txt', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.grl', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.yaml', 'archive')
    if not patreon:
        build.classify('game/ch/audrey/**', None)
        build.classify('game/ch/kleio/**', None)
        build.classify('game/ch/lexi/**', None)
        build.classify('game/ch/palla/**', None)
        build.classify('game/ch/shiori/**', None)
        build.classify('game/ch/kylie/**', None)
        build.classify('game/ch/lavish/**', None)
        build.classify('game/ch/alexis/**', None)
        build.classify('game/ch/morgan/**', None)
        build.classify('game/ch/cassidy/**', None)
        build.classify('game/ch/victor/**', None)
        build.classify('game/ch/emma/**', None)
    build.classify('game/temp/**', None)



    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
