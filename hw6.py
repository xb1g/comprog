import random

class thaigen:
    def __init__(self):
        self.lastpos = None

    def get(self):
        consonant = random.choice(thc)
        self.lastpos = consonant[0]
        return consonant[0]

    def get_answer(self):
        for consonant in thc:
            if consonant.startswith(self.lastpos):
                return [consonant[0], consonant[1], *consonant[2:].split()]

thc = [
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

# Example usage:
gen = thaigen()
consonant = gen.get()
print("Random consonant:", consonant)
print("Answer:", gen.get_answer())

