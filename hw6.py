import random

class thaigen:
    def __init__(self):
        self.thc = [
    "กMgor gai",
    "ขHkho khai",
    "ฃHkho khuat (not used)",
    "คLkho khwai",
    "ฅLkho khon (not used)",
    "ฆLkho rakhang",
    "งMngo ngu",
    "จHjoor jaan",
    "ฉHcho ching",
    "ชMcho chang",
    "ซLso so",
    "ฌLso cheer",
    "ญLyo ying",
    "ฎMdo chada",
    "ฏMto patak",
    "ฐHtho than",
    "ฑLtho montho",
    "ฒLtho phuthao",
    "ณLno nen",
    "ดMdo dek",
    "ตMto tao",
    "ถHtho thung",
    "ทLtho thahan",
    "ธLtho thong",
    "นLno nu",
    "บMbo baimai",
    "ปMpo pla",
    "ผHpho phueng",
    "ฝHfo fa",
    "พLpho phan",
    "ฟLfo fan",
    "ภLpho sam-phao",
    "มLmo ma",
    "ยLyo yak",
    "รLro rua",
    "ลLlo ling",
    "วLwo waen",
    "ศHso sala",
    "ษHso rusi",
    "สHso suea",
    "หHho hip",
    "ฬLlo chula",
    "อMo ang",
    "ฮLho nokhuk"
]

        self.lastpos = None
    def get(self):
        #if the list is empty..
        if not self.thc:
            return " "

        #get a random position
        rpos = random.randint(0, len(self.thc)-1)
        self.lastpos = rpos
        #get a line from thc from that position
        line = self.thc[rpos]
        #get the consonant
        return line[0]


    def get_answer(self):
        #if the list is empty..
        if not self.thc:
            return [" "," ",""]
        #get the line of lastpos
        line = self.thc[self.lastpos]
        return [ line[0], line[1], line[2:] ]

    def dont_ask_this(self, cons):
        #removes the consonant from thc so that it won't be asked again
        #look for the consonant cons in thc
        for line in self.thc:
            if cons in line:
                #print("removing "+cons)
                self.thc.remove(line)

    def howmany(self):
        return len(self.thc)

    def reset(self):
        self.__init__()


# Example usage:
gen = thaigen()

while gen.howmany() >= 0:
    if gen.howmany() == 0:
        print("No more consonants left.")
        print('reset? (y/n)')
        ans = input()
        if ans == 'y':
            gen.reset()
            print ("Reset done.")
            print("How many left:", gen.howmany())
            continue
        else:
            break

    consonant = gen.get()
    print("Random consonant:", consonant)
    print("Random consonant:", gen.get_answer())
    input("Press Enter to continue...")
    gen.dont_ask_this(consonant)
    print("How many left:", gen.howmany())
# print("Random consonant:", consonant)
# print("Random consonant:", gen.get_answer())
# gen.dont_ask_this(consonant)
# print("How many left:", gen.howmany())

# print("Answer:", gen.get_answer())

