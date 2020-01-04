init 1 python:
    class MorganPicker(Picker):
        def __call__(self, attr):
            attr = super(MorganPicker, self).__call__(attr)
            return attr
        
        def outfits(self, attr):
            attr = Picker.outfits(self, attr)
            male = morgan.get_flag_value('male')
            
            if male < 60:
                attr.add('head2')
                if 'head1' in attr: attr.remove('head1')
            if male < 40:
                attr.add('makeup')
            
            if 'casual' in attr:
                if male >= 80:
                    attr.add('blackjacket')
                    attr.add('camopants')
                    if not 'collar' in attr:
                        attr.add('necklace')
                elif male >= 60:
                    attr.add('bluesweater')
                    attr.add('blackpants')
                    if not 'collar' in attr:
                        attr.add('necklace')
                elif male >= 50:
                    attr.add('blackjacket')
                    attr.add('blackpants')
                    if not 'collar' in attr:
                        attr.add('necklace')
                elif male >= 20:
                    attr.add('redhalf')
                    attr.add('blackskirt')
                else:
                    attr.add('whitetank')
                    attr.add('blueskirt')
            elif 'date' in attr:
                print 'date'
                if male >= 80:
                    attr.add('tux')
                    attr.add('blackpants')
                elif male >= 60:
                    attr.add('bluejacket')
                    attr.add('blackpants')
                elif male >= 40:
                    attr.add('blacktube')
                    attr.add('blackshorts')
                    if not 'collar' in attr:
                        attr.add('necklace')
                elif male >= 20:
                    attr.add('blacktube')
                    attr.add('blackmini')
                    if not 'collar' in attr:
                        attr.add('necklace')
                else:
                    attr.add('dotdress')
                    attr.add('nopants')
                    if not 'collar' in attr:
                        attr.add('necklace')
            elif 'sport' in attr:
                if male >= 60:
                    attr.add('stripedworkout')
                    attr.add('sweatpants')
                elif male >= 50:
                    attr.add('sweatshirt')
                    attr.add('sweatpants')
                elif male >= 20:
                    attr.add('blacksport')
                    attr.add('blacktights')
                else:
                    attr.add('tightsport')
                    attr.add('blacktights')
            elif 'swimsuit' in attr:
                if male >= 60:
                    attr.add('blueblackswimsuit')
                    attr.add('nopants')
                elif male >= 20:
                    attr.add('blueswimtop')
                    attr.add('redbluebikinibottom')
                else:
                    attr.add('bluebikinitop')
                    attr.add('bluebikinibottom')
            return attr

init 1:
    layeredimage morgan:
        attribute_function MorganPicker(morgan)


        group position auto

        attribute pregnant if_any "a":
            "morgan_pregnant_a"
        attribute pregnant if_any "b":
            "morgan_pregnant_b"

        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"          


        group outfit:
            attribute casual null
            attribute sport null
            attribute date null
            attribute swimsuit null
            attribute naked null
            attribute sexyswimsuit null
            attribute tape null

        group top auto variant "a" if_any "a"
        group top auto variant "b" if_any "b"
        group top auto variant "a_pregnant" if_all ["a", "pregnant"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"]
        group bot auto variant "a" if_any "a":
            attribute nopants null
        group bot auto variant "b" if_any "b":
            attribute nopants null
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute nopants null
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute nopants null

        group head auto:
            attribute head1 default


        attribute makeup null
        group exp auto:
            attribute normal default
        group exp auto variant "makeup" if_any "makeup":
            attribute normal default

        group facepiercings multiple auto variant "a" if_any "a"
        group facepiercings multiple auto variant "b" if_any "b"          

        group acc multiple auto  variant "a" if_any "a"
        group acc multiple auto  variant "b" if_any "b"

    layeredimage morgan smartphone:
        always "morgan_smartphone"

    layeredimage morgan kiss:
        group outfit auto:
            attribute casual null default
            attribute naked null
            attribute date null
            attribute sport null
            attribute sexyswimsuit null
            attribute swimsuit null
            attribute underwear null
            attribute work null

    layeredimage morgan missionary:
        attribute_function XrayPicker(morgan)
        attribute cum null
        group bg auto:
            attribute bedroom default

        always:
            "morgan_missionary_body"


        always:
            if_any ["male60"]
            "morgan_missionary_hair"
        always:
            if_not ["male60"]
            "morgan_missionary_hair2"

        attribute pregnant:
            "morgan_missionary_pregnant" 

        group exp auto if_any "male40":
            attribute normal default
        group exp auto variant "makeup" if_not "male40":
            attribute normal default

        group man auto:
            attribute out default

        group xray auto:
            if_any "xray"
            if_not "condom"
            attribute none null default

        attribute condom:
            if_any "vaginal"
            "morgan_missionary_condom"

        group cum auto:
            if_any "cum"
            if_not "condom"

        attribute shake:
            "morgan_missionary_fx_shake"

        if morgan.get_piercings("nipples"):
            "morgan_missionary_piercings_nipples"

        if morgan.get_piercings("lips"):
            "morgan_missionary_piercings_lips"

        if morgan.get_piercings("nose"):
            "morgan_missionary_piercings_nose"

        if morgan.get_piercings("navel") and not morgan.get_flag_value("pregnant") >= 9:
            "morgan_missionary_piercings_navel"

        if morgan.get_piercings("navel") and morgan.get_flag_value("pregnant") >= 9:
            "morgan_missionary_piercings_navel_pregnant"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
