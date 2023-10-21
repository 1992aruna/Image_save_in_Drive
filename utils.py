# Keyword options on selection of list or button 
lang_list=["english", "tamil", "hindi", "telugu", "malayalam", "kannada"]

design_list={"english":["inivitation", "poster", "social media post", "advertisement", "presentation"],
             "tamil":["அழைப்பு", "சுவரொட்டி", "சமூக ஊடக இடுகை", "விளம்பரம்", "விளக்கக்காட்சி"]
             }
function_list={"english":["wedding", "birthday", "anniversary", "religious activity", "retirement", "orbiturary", "party", "events"],
               "tamil":["திருமணம்", "பிறந்தநாள்", "ஆண்டுவிழா", "மத செயல்பாடு", "ஓய்வு", "இறப்பு", "பார்ட்டி", "நிகழ்ச்சிகள்"]
             }
religion_list={"english":["christian", "hindu", "muslim", "non religious"],
               "tamil":["கிறிஸ்தவ மதம்", "இந்து மதம்", "இஸ்லாம் மதம்", "மதம் இல்லாதவர்"]}

religion_denomination_list={"english":["roman catholic", "protestant", "csi", "benthocoast"],
                 "tamil":["ரோமன் கத்தோலிக்க", "புராட்டஸ்டன்ட்", "சிஎஸ்ஐ", "பெந்தோகோஸ்ட்"]
                }
design_type_list={"english":["wedding", "engagement", "reception", "sangeeth", "bachelorete party", "bulk design"],
                  "tamil":["திருமணம்", "நிச்சயதார்த்தம்", "வரவேற்பு", "சங்கீத்", "பேச்சலரேட் பார்ட்டி", "மொத்த வடிவமைப்பு"]}
# design_list = {"english":["social media post","banner"],
#                "tamil":["சமூக ஊடக இடுகை", "பதாகை"]}
# design_place_list={"english":["With details and without photo", "With bride and groom single photo",
#                                "With bride and groom seperate photo", "With 3 photos (Bride Photo , Bridegroom Photo)"],
#                 #   "tamil":["திருமணம்", "நிச்சயதார்த்தம்", "வரவேற்பு", "சங்கீத்", "பேச்சலரேட் பார்ட்டி", "மொத்த வடிவமைப்பு"]
#                   }

place_list={"english":["with details", "without photo", "single photo", "seperate photo", "3 photos"]}

bday_theme_list={"english":["Avengers", "Butterfly", "Chocolate", "Disney Princess", "Hulk", "Ice cream", "Jungle", "Monster", "Shark"],
                 "tamil":["அவெஞ்சர்ஸ்", "வண்ணத்துப்பூச்சி", "சாக்லேட்", "டிஸ்னி பிரின்சஸ்", "ஹல்க்", "ஐஸ்கிரீம்", "காடு", "மான்ஸ்டர்", "ஷார்க்"]}
# bday_theme_list=["Avengers", "Butterfly", "Chocolate", "Disney Princess", "Hulk", "Ice cream", "Jungle", "Monster", "Shark"]
bday_color_list={"english":["Pink", "Blue", "Red", "Green", "Black", "White", "Purple", "Aquamarine", "Yellow"],
                 "tamil":["இளஞ்சிவப்பு", "நீலம்", "சிவப்பு", "பச்சை", "கருப்பு", "வெள்ளை", "ஊதா", "அக்வாமரைன்", "மஞ்சள்"]}

bday_relation_list={"english":["Father", "Mother", "Daughter", "Son", "Sister", "Brother", "Wife", "Twins", "Cousin", "Friend"],
                    "tamil":["அப்பா", "அம்மா", "மகள்", "மகன்", "சகோதரி", "சகோதரன்", "மனைவி", "இரட்டையர்கள்", "அண்ணன்/அக்கா", "நண்பர்"]}

bday_invitation_list={"english":["without photo", "with a single photo", "person photo and family"],
                      "tamil":["புகைப்படம் இல்லாமல்", "ஒரு புகைப்படத்துடன்", "நபர் புகைப்படம் மற்றும் குடும்பம்"]}
# A function changing when a particular keyword strikes

def keyword_node(text):
        state="None"

        if text in ["birthday","Birth day","birthday poster","birthday design","birthday card","birthday wish","birth day wish","birth day poster","son birthday","baby birthday","பிறந்த நாள்", "பிறந்த நாள்", "பிறந்தநாள் போஸ்டர்", "பிறந்தநாள் வடிவமைப்பு", "பிறந்தநாள் அட்டை", "பிறந்தநாள் வாழ்த்துக்கள்", "பிறந்த நாள் வாழ்த்துக்கள்", "பிறந்தநாள் போஸ்டர்", "மகன் பிறந்த நாள்", "குழந்தை பிறந்த நாள்"]:
            state="post_name"
        elif text in ["wish","good morning", "good night", "good night","வாழ்த்துக்கள்","காலை வணக்கம்", "நல்ல இரவு", "நல்ல இரவு"]:
            state="wish"

        elif text in ["congratulation","congratulations","congrats","congrat","thank","thanks","வாழ்த்துக்கள்", "வாழ்த்துக்கள்", "வாழ்த்துக்கள்", "வாழ்த்துக்கள்", "நன்றி", "நன்றி"]:
            state="post_name"

        elif text in ["welcome","arriving","arrive","வரவேற்கிறேன்","வருகிறேன்","வந்தேன்"]:
            state="post_name"

        elif text in ["achievement","achieve","சாதனை","சாதனை"]:
            state="post_name"

        elif text in ["quote","self quote","my mind","my thoughts","vision","message","மேற்கோள்", "சுய மேற்கோள்", "என் மனம்", "என் எண்ணங்கள்", "பார்வை", "செய்தி"]:
            state="self_quote"

        elif text in ["work","வேலை"]:
            state="work"

        return state