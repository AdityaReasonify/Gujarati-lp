# -*- coding: utf-8 -*-
import json, io, os

ADULT = ("The chief guest is a slight, thin-framed man of about fifty in a plain white cotton kurta "
         "and white dhoti with brown leather chappals, narrow shoulders, a small neat moustache and "
         "short grey-flecked hair; his face is an ordinary illustrated face, not the likeness of any "
         "real person.")

BOY = ("The boy is thin and small for his age, about twelve, with short-cropped black hair and a "
       "narrow face; he wears a loose white cotton shirt and a white dhoti, and inside the wrestling "
       "ground he is bare-chested with the dhoti hitched up and tucked between the legs in the "
       "kachhoto style.")

NANDU = ("The other boy is two or three years older and solidly built, his skin darkened and faintly "
         "glinting under a film of sweat and red dust, wearing only a cloth langot; he is drawn as "
         "strong and capable, never comic.")

USTAD = ("The ustad is a broad, heavy-set older man with a thick greying moustache, bare-chested "
         "above a white dhoti wrapped and tucked, seated cross-legged on a low wooden platform.")

VADIL = ("The boy's elderly guardian is a lean old man with white stubble and a bald crown, in a "
         "white dhoti, a long white kurta and a cotton shoulder cloth.")

AKHADA = ("The wrestling ground is an open earthen compound in old Surat in South Gujarat: a "
          "rectangular pit about three feet deep of loose red-brown dug earth, a smooth wooden "
          "mallakhamb pole planted upright in the ground, a mud-plastered wall with a small niche "
          "holding an orange-smeared Hanuman image and a marigold garland, a clay water pot standing "
          "in the shade, an old neem tree overhead and the curved clay-tiled roofs of the old town "
          "beyond the wall.")

HOME = ("The house is an old Surat wooden town house: a raised stone platform running along the "
        "front wall, carved wooden pillars and brackets, curved clay roof tiles, a rope-strung "
        "wooden cot and a small brass oil lamp.")

STYLE = "Soft digital watercolour, vibrant textbook illustration style, 16:9."

NEG_BASE = ("photorealistic faces, anime style, western-only setting, Roman script labels, "
            "Devanagari script labels, generic Bollywood styling, north-Indian-only architecture, "
            "watermark, blurry, cluttered background, anachronistic objects, caricature or "
            "exaggerated cartoon gag, comic-strip speech bubbles, motivational poster layout, text "
            "banner with a moral, portrait likeness of a real named person, modern gym equipment, "
            "sumo or Japanese wrestling imagery, blood or injury, mocking or humiliating depiction "
            "of the wrestlers")


def bar(s):
    return ('At the bottom of the frame a plain narrator bar carries exactly this one line of text, '
            'lettered in Gujarati script and in no other script: "%s". No other writing appears '
            'anywhere in the picture.' % s)


media = []

# ---------------- T1 ----------------
media.append({
 "topic_id": "M1.S1.T1",
 "concept_id": "M1.S1.T1.C1",
 "id": "M1.S1.T1.C1.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "મંચ પરથી અપાતાં વખાણ",
 "description": "અખાડાના સ્નેહસંમેલનના મંચ પર પહેલવાન જેવા લાગતા સંચાલક ઊભા થઈને બોલે છે અને બાજુની ખુરશીમાં દૂબળા મુખ્ય મહેમાન હાથ જોડીને સાંભળે છે.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M1.S1.T1.C1",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "ચિત્ર બતાવીને પહેલાં પૂછો કે મંચ પર ઊભેલા ભાઈ કેવા દેખાય છે ને ખુરશીમાં બેઠેલા મહેમાન કેવા; પછી જ સંચાલકનું છેલ્લું વાક્ય વાંચો, જેથી બાળક જાતે જુએ કે વખાણ જેવા લાગતા શબ્દોમાં દયા છુપાયેલી છે.",
 "negative_prompt": NEG_BASE + ", lettering on the cloth backdrop, trophy or medal ceremony, "
                    "microphone stand crowded with logos",
 "generation_prompt": (
   "A small-town Gujarat wrestling club's annual social gathering, indoors under a tin-sheet roof on "
   "a warm afternoon. On a low stage spread with a striped cotton mat stand two folding steel chairs "
   "and a small table with a cloth-covered table microphone, a steel water jug and a tumbler. A "
   "heavy-set, thickly built club organiser of about forty-five in a white kurta and dhoti, a thick "
   "marigold garland round his neck, stands at the microphone with one blunt hand raised, speaking "
   "haltingly, his weight shifted awkwardly onto one leg. Seated in the chair beside him is the "
   "chief guest, also garlanded, hands folded in his lap, listening with a polite, slightly stiff "
   "smile. " + ADULT + " Below the stage, wrestlers and boys in white sit cross-legged on the floor "
   "on a cotton mat; a plain unmarked cloth backdrop hangs behind, with a small framed Hanuman "
   "picture and a marigold garland on the side wall. " + bar("અખાડાના સ્નેહસંમેલનમાં મુખ્ય મહેમાનનાં વખાણ") +
   " " + STYLE)
})

# ---------------- T2 ----------------
media.append({
 "topic_id": "M1.S1.T2",
 "concept_id": "M1.S1.T2.C3",
 "id": "M1.S1.T2.C3.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "પહેલવાનોને સાધના કરતા જોતો લેખક",
 "description": "કસરત ન કરનારો દૂબળો માણસ અખાડાની કિનારે ઊભો રહીને પહેલવાનોને વ્યાયામની સાધના કરતા ધ્યાનથી જુએ છે.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M1.S1.T2.C3",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "ચિત્રમાં કોણ કસરત કરે છે ને કોણ માત્ર જુએ છે એ પૂછો; આ પ્રસંગમાં લેખક કસરતનો વિરોધ નથી કરતા, પોતે કરતા નથી એટલું જ કબૂલે છે — એ ભેદ ચિત્ર પરથી જ ઊભો કરો.",
 "negative_prompt": NEG_BASE + ", the thin man exercising or wrestling, medals, before-and-after "
                    "body comparison",
 "generation_prompt": (
   "Early morning at an open-air wrestling ground in an old South Gujarat town, low golden light and "
   "dust in the air. " + AKHADA + " Two strong young wrestlers in langots are training on the packed "
   "earth beside the pit: one is midway through a floor exercise, palms and toes on the ground and "
   "body dipping forward; the other grips the wooden mallakhamb pole and pulls himself up along it. "
   "They are drawn with dignity, absorbed in their work. At the edge of the ground, a little apart, "
   "stands a visitor watching them intently with his hands clasped behind his back, clean and "
   "completely unsuited to the place. " + ADULT + " His chappals are dusty from the walk; he has not "
   "taken off a single garment. " + bar("લેખકે પહેલવાનોને સાધના કરતા જોયા છે") + " " + STYLE)
})

# ---------------- T3 ----------------
media.append({
 "topic_id": "M2.S2.T3",
 "concept_id": "M2.S2.T3.C4",
 "id": "M2.S2.T3.C4.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "ઓટલા પર મળેલો હુકમ",
 "description": "સાંજે ઘરના ઓટલા પર ખાટલામાં બેઠેલા વડીલ આંગળી ઊંચી કરીને દૂબળા છોકરાને કાલથી અખાડે જવાનું કહે છે.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M2.S2.T3.C4",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "ચિત્ર બતાવીને પૂછો કે છોકરાના મોં પર શું દેખાય છે; નિર્ણય વડીલે લીધો છે ને છોકરાને પૂછ્યું જ નથી, એ વાત ચિત્ર પરથી કઢાવીને પછી સંવાદ વાંચો.",
 "negative_prompt": NEG_BASE + ", angry shouting or corporal punishment, scolding with a stick, "
                    "modern furniture",
 "generation_prompt": (
   "Evening on the raised front platform of an old wooden town house in Surat, South Gujarat, warm "
   "lamplight and a deep blue street beyond. " + HOME + " An elderly guardian sits on the rope cot, "
   "leaning forward with one index finger raised, giving an instruction in a firm but not unkind "
   "voice. " + VADIL + " Standing in front of him on the platform is a thin boy, arms at his sides, "
   "head tilted, his face full of puzzled objection, plainly about to ask a question. " + BOY + " "
   "In the lane just below, two sturdier neighbourhood boys wait, one swinging a small cloth bundle. "
   "A brass oil lamp burns in the wall niche; curved clay roof tiles and carved wooden brackets "
   "frame the scene. " + bar("કાલથી અખાડે જવાનું છે — વડીલનો હુકમ") + " " + STYLE)
})

# ---------------- T4 ----------------
media.append({
 "topic_id": "M2.S2.T4",
 "concept_id": "M2.S2.T4.C5",
 "id": "M2.S2.T4.C5.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "ઉસ્તાદ સામે કુસ્તીની માગણી",
 "description": "અખાડામાં પહેલા જ દિવસે કછોટો મારીને ઊભેલો દૂબળો છોકરો ઉસ્તાદ સામે કુસ્તીની જીદ કરે છે અને ઉસ્તાદ નવાઈ પામીને જુએ છે.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M2.S2.T4.C5",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "ચિત્રમાં છોકરાનું શરીર ને એની માગણી વચ્ચેનું અંતર બતાવો; ઉસ્તાદે કહેલો સાચો ક્રમ — પહેલાં દંડ-બેઠક ને મલખમ — ચિત્રમાં દેખાતા મલખમના થાંભલા તરફ આંગળી ચીંધીને યાદ કરાવો.",
 "negative_prompt": NEG_BASE + ", an actual wrestling bout in progress, mocking the boy's thin body, "
                    "audience laughing at him",
 "generation_prompt": (
   "Morning at an open-air wrestling ground in old Surat, South Gujarat. " + AKHADA + " The ustad "
   "sits cross-legged on his low wooden platform in the shade, eyebrows lifted high and one hand "
   "half-raised in genuine surprise at what he has just been told. " + USTAD + " Standing squarely "
   "in front of him, chin up and shoulders pulled back with absurd confidence, is a very thin boy "
   "who has just stripped for the ground. " + BOY + " His folded white shirt lies on the wooden "
   "platform beside the ustad. Behind them the mallakhamb pole and, further off, two older boys "
   "pausing in their exercise to look across. Dust hangs in the slanting morning light. " +
   bar("કુસ્તી તો છેક છેલ્લે આવે.") + " " + STYLE)
})

# ---------------- T5 ----------------
media.append({
 "topic_id": "M2.S3.T5",
 "concept_id": "M2.S3.T5.C6",
 "id": "M2.S3.T5.C6.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "ખાડામાં ઊતરીને ગોટલો",
 "description": "ત્રણેક ફૂટ ઊંડા ખાડામાં મોટો છોકરો હાથ વાળીને પોતાનો ગોટલો બતાવે છે અને દૂબળો છોકરો પોતાનો પાતળો હાથ વાળીને એની નકલ કરે છે.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M2.S3.T5.C6",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "પહેલાં ચિત્રમાં ખાડો બતાવો ને પૂછો કે આ ખાડાને પાઠમાં શું કહ્યું છે; ‘અખાડો’ના બે અર્થ ચિત્ર પરથી ખૂલે પછી જ લેખકનું વાક્ય વાંચો, અને કોઈ અલંકારનું નામ ન પાડો.",
 "negative_prompt": NEG_BASE + ", bodybuilder posing contest, gym mirror, exaggerated cartoon "
                    "muscles, humiliation of either boy",
 "generation_prompt": (
   "Inside a rectangular pit about three feet deep, dug out of red-brown earth and freshly turned "
   "so the soil lies loose and crumbly; a long-handled iron shovel lies dropped where it fell at the "
   "pit's edge. Two boys stand facing each other down in the pit. The older one has bent his right "
   "arm at the elbow towards his shoulder and is pressing the risen muscle with his left hand, "
   "showing it off with an open, teasing grin. " + NANDU + " Opposite him, copying the gesture "
   "exactly and peering down at his own bent arm with earnest concentration, is a much thinner boy "
   "on whose arm only a small soft swelling has appeared. " + BOY + " Seen over the rim of the pit: "
   "the packed earth of the ground, a wooden mallakhamb pole, a mud-plastered wall with a small "
   "niche holding an orange-smeared Hanuman image and a marigold garland, an old neem tree and the "
   "curved clay-tiled roofs of an old South Gujarat town. " + bar("જોયો આ ગોટલો ?") + " " + STYLE)
})

# ---------------- T6 ----------------
media.append({
 "topic_id": "M2.S3.T6",
 "concept_id": "M2.S3.T6.C7",
 "id": "M2.S3.T6.C7.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "અડક્યા પહેલાં જ ચત્તો",
 "description": "કુસ્તી માટે ધસી આવતો છોકરો અડકે તે પહેલાં જ દૂબળો છોકરો ખાડામાં શાંતિથી ચત્તો સૂઈ જાય છે અને સામેવાળો નવાઈ પામીને અધવચ્ચે અટકી જાય છે.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M2.S3.T6.C7",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "ચિત્રમાં બંને વચ્ચેનું અંતર બતાવીને પૂછો કે કોણે કોને પાડ્યો; ‘ચીત’ શબ્દ અહીં જ ગ્લોસ કરો — ચત્તા સૂઈ જવું — અને પછી સંવાદ વાંચીને ‘હું હાર્યો’ કોણ બોલે છે તે નક્કી કરાવો.",
 "negative_prompt": NEG_BASE + ", violent throw or slam, pain or crying, blood, dramatic action-film "
                    "pose, sumo ring",
 "generation_prompt": (
   "Inside a rectangular earth pit about three feet deep in an old South Gujarat wrestling ground, "
   "dust hanging in the morning light. A very thin boy lies flat on his back on the loose red-brown "
   "earth, entirely unhurt and quite calm, arms straight at his sides, eyes open, looking up with a "
   "mild, matter-of-fact expression as though this were the normal thing to do. " + BOY + " A step "
   "and a half away, a stronger older boy has stopped dead in the middle of his charge, knees bent "
   "in a wrestler's crouch, both palms still on his thighs, mouth open and eyebrows high in complete "
   "astonishment. " + NANDU + " Neither has touched the other and there is a clear gap of open earth "
   "between them. Above the rim of the pit, the ustad watches from his low wooden platform in the "
   "shade of a neem tree; a mud wall carries a small niche with an orange-smeared Hanuman image and "
   "a marigold garland. " + bar("ચીત !") + " " + STYLE)
})

# ---------------- T7 ----------------
media.append({
 "topic_id": "M3.S4.T7",
 "concept_id": "M3.S4.T7.C9",
 "id": "M3.S4.T7.C9.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "ઉસ્તાદ છોકરાનું મોં તપાસે છે",
 "description": "દંડબેઠકનો અર્થ પોતાની રીતે સમજીને બોલી ગયેલા છોકરાના મોં સામે ઉસ્તાદ ધારીને જુએ છે કે એ મજાક કરે છે કે સાચે જ જાણતો નથી.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M3.S4.T7.C9",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "ચિત્રમાં ઉસ્તાદની નજર છોકરાના મોં પર છે તે બતાવો ને પૂછો કે એ શું શોધે છે; અહીં જ ‘દંડ’ ને ‘બેઠક’ના રોજિંદા અર્થ અને કસરતના અર્થ સામસામે મૂકો, પણ લેખકનું વાક્ય સુધારો નહિ.",
 "negative_prompt": NEG_BASE + ", a boy actually holding a stick or sitting on a chair, thought "
                    "bubble showing an imagined scene, split-screen joke panel",
 "generation_prompt": (
   "Morning at an open-air wrestling ground in old Surat, South Gujarat, dust and low golden light. "
   + AKHADA + " The ustad has leaned forward from his low wooden platform and is studying the face "
   "of the boy standing in front of him, head slightly turned, eyes narrowed, searching for a smile "
   "that is not there. " + USTAD + " The boy stands with his hands behind his back, bare-chested, "
   "his expression open, mild and completely serious, without the smallest trace of a joke. " + BOY +
   " Behind them, out of focus, other boys move about the packed earth beside the mallakhamb pole. "
   "The moment is quiet and held: two faces, one searching, one blank. " +
   bar("અલ્યા ! તને તો કાંઈ જ ખબર નથી.") + " " + STYLE)
})

# ---------------- T8 ----------------
media.append({
 "topic_id": "M3.S4.T8",
 "concept_id": "M3.S4.T8.C10",
 "id": "M3.S4.T8.C10.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "દંડ ને બેઠકનું નિરીક્ષણ",
 "description": "દંડ પીલતા ને બેઠક કરતા મજબૂત ભાઈઓની બાજુમાં ઊભો રહીને દૂબળો છોકરો કપાળે કરચલી પાડીને એકીટશે જોઈ રહ્યો છે.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M3.S4.T8.C10",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "ચિત્રમાં કસરત કરનારા બરાબર ને કુશળતાથી કસરત કરે છે એ પહેલાં નોંધાવો; હાસ્ય કસરત કરનારાઓ પર નથી, જોનારા છોકરાની અણસમજ પર છે — એ ભેદ અહીં જ સ્પષ્ટ કરો.",
 "negative_prompt": NEG_BASE + ", the exercising men shown as foolish or clumsy, laughing crowd, "
                    "exaggerated grimaces on the wrestlers, cartoon sweat drops as a gag",
 "generation_prompt": (
   "Morning at an open-air wrestling ground in old Surat, South Gujarat. " + AKHADA + " In the "
   "foreground three strong young men in langots are doing floor push-up exercises in a neat row: "
   "palms flat and toes braced on the packed earth, bodies dipping low and the head pushed forward "
   "between the arms, then rising again. Just beyond them two other men are midway through deep "
   "squats, half-risen, thigh muscles taut, faces set with effort. They are all drawn as skilled, "
   "strong and dignified, performing the exercise correctly. Standing to one side, close enough to "
   "be in the way, a very thin boy watches them with his hands clasped behind his back, brow "
   "furrowed, head tilted, utterly baffled by what he is seeing; his is the only comic face in the "
   "picture. " + BOY + " " + bar("દંડ ને બેઠક કરનારાઓને જોઈ રહ્યો") + " " + STYLE)
})

# ---------------- T9 ----------------
media.append({
 "topic_id": "M3.S5.T9",
 "concept_id": "M3.S5.T9.C11",
 "id": "M3.S5.T9.C11.IMG1",
 "type": "image",
 "subtype": "illustration",
 "title": "વડીલને અપાયેલો ટૂંકો જવાબ",
 "description": "સાંજે ઘરના ઓટલા પર ખાટલામાં બેઠેલા વડીલના પ્રશ્નનો છોકરો સાવ સ્વસ્થ ચહેરે ટૂંકો જવાબ આપે છે.",
 "image_url": "",
 "aspect_ratio": "16:9",
 "home_concept_id": "M3.S5.T9.C11",
 "objective_id": None,
 "image_category": "illustration",
 "teaching_notes": "ચિત્રમાં છોકરાના ચહેરાની સ્વસ્થતા બતાવો ને પૂછો કે એણે વડીલને શું નથી કહ્યું; ‘વાક્યમાં કર્તા અધ્યાહાર હતો’ એ પુસ્તકના પોતાના શબ્દો છે — ત્યાંથી જ સમજાવો, ઉપદેશ ઉમેર્યા વિના.",
 "negative_prompt": NEG_BASE + ", a lie being exposed, wagging finger, guilt or shame on the boy's "
                    "face, moral lesson tableau",
 "generation_prompt": (
   "Evening on the raised front platform of an old wooden town house in Surat, South Gujarat, warm "
   "lamplight, a deep blue street and a first star beyond. " + HOME + " The elderly guardian sits on "
   "the rope cot, one hand resting on his knee, mid-question, looking up at the boy with plain, "
   "satisfied interest. " + VADIL + " The boy stands in front of him, back in his white shirt, hair "
   "a little damp at the temples, hands clasped behind his back, answering in three words with a "
   "wholly untroubled, respectful face. " + BOY + " A brass oil lamp burns in the wall niche and "
   "throws both their shadows onto the carved wooden pillar. Nothing dramatic is happening: it is a "
   "quiet doorstep exchange at the end of a day. " + bar("પરસેવો થાય ત્યાં સુધી.") + " " + STYLE)
})

out = {
 "media": media,
 "2d_tool": None,
 "reuse_report": {"scenes": 9, "reused": 0, "authored": 9, "rejected": []}
}

p = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch03/09_media.json"
with io.open(p, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("wrote", p, os.path.getsize(p))
