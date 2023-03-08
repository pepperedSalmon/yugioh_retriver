from statistics import mean
def name_format(card_name,LINE_WIDTH):
    card_name = str(card_name)
    b1 = ""
    b2 = ""
    b3 = ""
    if len(card_name) < LINE_WIDTH:
        for i in range(LINE_WIDTH - len(card_name)):
                b1+=" "
        for i in range(LINE_WIDTH):
            b2+=" "
        f1 = card_name + b1
        f2 = b2
    elif len(card_name) < 2 * LINE_WIDTH:
         for i in range(2 * LINE_WIDTH - len(card_name)):
                b2+=" "
         f1 = card_name[0:LINE_WIDTH]
         f2 = card_name[LINE_WIDTH:len(card_name)] + b2
    else:
        f1 = card_name[0:LINE_WIDTH]
        f2 = card_name[LINE_WIDTH:LINE_WIDTH * 2]
    return [f1,f2]
def level_format(card_rank,LINE_WIDTH=10):
    try:
        i_rank = int(card_rank)
    except ValueError:
        i_rank = LINE_WIDTH + 1     
        
    b1 = ""
    r1 = ""
    if i_rank <= LINE_WIDTH:
        for i in range(LINE_WIDTH - i_rank):
            b1+=" "
        for i in range(i_rank): 
            r1+="*"
        f_rank = b1 + r1
        return f_rank
    else:
        for i in range(LINE_WIDTH):
            b1+=" "
        return b1

class YugiohCard:
    '''This object describes a Yugioh card at a high level'''
    def __init__(self,name,frame,rarity,card_set,text="N/A",s_frame="Monster",img_url="",position="face down"):
        self.name = name
        self.frame = frame
        self.rarity = rarity
        self.card_set = card_set
        self.text = text
        self.position = position
        self.s_frame = s_frame
        self.img_url=img_url

    def reveal(self):
        print(self.name)

class MonsterCard(YugiohCard):
    '''This object is a child of Yugioh cards'''
    def __init__(self,name,frame,rarity,card_set,text,atribute,monster_type,level,_atk,_def,s_frame="Monster",img_url="", position="face down"):
        super().__init__(name,frame,rarity,card_set,text,s_frame="Monster",img_url="",position="face down")
        self.atribute = atribute
        self.moster_type = monster_type
        self.level = level
        self._atk = _atk
        self._def = _def
        self.s_frame=s_frame
        self.img_url=img_url
    def str_img(self):
        fname = name_format(self.name,16)
        if self.position.lower() == "set":
            fd00 = "   .............   "
            fd01 = "  :             :  "           
            fd02 = "  :             :  "
            fd03 = "  :             :  "
            fd04 = "  :             :  "
            fd05 = " _:_____________:_ "
            fd06 = "|    _________    |"
            fd07 = "|   /         \   |"
            fd08 = "|  |           |  |"
            fd09 = "|   \_________/   |"
            fd10 = "|_________________|"
            fd = [fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
            return fd
        elif self.position.lower() == "face up": 
            f_atk = name_format(self._atk,4)
            f_def = name_format(self._def,4)
            f_level = level_format(self.level)
            mz00 = "  ________________ "
            mz01 = f" |{fname[0]}|"
            mz02 = f" |{fname[1]}|"
            mz03 = f" |    {f_level}  |"
            mz04 = " |   __________   |"
            mz05 = " |  |          |  |"
            mz06 = " |  |          |  |"
            mz07 = " |  |__________|  |"
            mz08 = f" | ATK {f_atk[0]}       |"
            mz09 = f" | DEF {f_def[0]}       |"
            mz10 = " |________________|"
            if mz02 == " |                |":
                mz02 = mz03
                mz03 = mz04
                mz04 = mz05
            mz = [mz00,mz01,mz02,mz03,mz04,mz05,mz06,mz07,mz08,mz09,mz10]
            return mz
        elif self.position.lower() == "face up def":
            f_atk = name_format(self._atk,4)
            f_def = name_format(self._def,4)
            f_level = level_format(self.level)
            mz00 = "  ...............  "  
            mz01 = f"{fname[0]}:  "         
            mz02 = f"  :   {f_level}:  "
            mz03 = f"  :   ATK: {f_atk[0]} :  "
            mz04 = f"  :   DEF: {f_def[0]} :  "
            mz05 = " _:_____________:_ "
            mz06 = "|  ______   ..... |"
            mz07 = "| |      |  :   : |"
            mz08 = "| |      |  :   : |"
            mz09 = "| |______|  :...: |"
            mz10 = "|_________________|"
            mz = [mz00,mz01,mz02,mz03,mz04,mz05,mz06,mz07,mz08,mz09,mz10]
            return mz
        elif self.position.lower() == "face down":
            fd00 = "  ________________ " 
            fd01 = " |      ____      |"  
            fd02 = " |     /    \     |"
            fd03 = " |    |      |    |"
            fd04 = " |    |      |    |"
            fd05 = " |    |      |    |"
            fd06 = " |    |      |    |"
            fd07 = " |    |      |    |"
            fd08 = " |    |      |    |"
            fd09 = " |     \____/     |"
            fd10 = " |________________|" 
            fd = [fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
            return fd
        pass
         
class SpellTrapCard(YugiohCard):
    '''This Object describs a Yugioh Spell or Trap Cards '''
    def __init__(self,name,frame,rarity,card_set,text,card_icon,s_frame="Spell Trap",img_url="", position="face down"):
        super().__init__(name,frame,rarity,card_set,text,s_frame="Spell Trap",img_url="",position="face down")
        self.card_icon = card_icon
        self.s_frame=s_frame
        self.img_url=img_url
    def str_img(self):
        fname = name_format(self.name,16)
        if self.position.lower() == "set" or self.position.lower() == "face down":
            fd00 = "  ________________ " 
            fd01 = " |      ____      |"  
            fd02 = " |     /    \     |"
            fd03 = " |    |      |    |"
            fd04 = " |    |      |    |"
            fd05 = " |    |      |    |"
            fd06 = " |    |      |    |"
            fd07 = " |    |      |    |"
            fd08 = " |    |      |    |"
            fd09 = " |     \____/     |"
            fd10 = " |________________|" 
            fd = [fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
            return fd
        elif self.position.lower() == "face up": 
            if self.frame.lower() == "trap card":  
                mz00 = "  _________________ "
                mz01 = f" |{fname[0]}|"
                mz02 = f" |{fname[1]}|"
                mz03 = " |   _________Trap|"
                mz04 = " |  |          |  |"
                mz05 = " |  |          |  |"
                mz06 = " |  |          |  |"
                mz07 = " |  |__________|  |"
                mz08 = " | .............  |"
                mz09 = " | :...........:  |"
                mz10 = " |________________|"
                if mz02 == " |                |":
                    mz02 = " |            Trap|"
                    mz03 = " |   __________   |"
                mz = [mz00,mz01,mz02,mz03,mz04,mz05,mz06,mz07,mz08,mz09,mz10]
                return mz
            elif card.frame.lower() == "spell card":            
                mz00 = "  ________________ "
                mz01 = f" |{fname[0]}|"
                mz02 = f" |{fname[1]}|"
                mz03 = " |   ________Spell|"
                mz04 = " |  |          |  |"
                mz05 = " |  |          |  |"
                mz06 = " |  |          |  |"
                mz07 = " |  |__________|  |"
                mz08 = " | .............  |"
                mz09 = " | :...........:  |"
                mz10 = " |________________|"
                if mz02 == " |                |":
                    mz02 = " |           Spell|"
                    mz03 = " |   __________   |"
                mz = [mz00,mz01,mz02,mz03,mz04,mz05,mz06,mz07,mz08,mz09,mz10]
                return mz
                pass
