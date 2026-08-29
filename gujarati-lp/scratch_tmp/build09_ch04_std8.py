# -*- coding: utf-8 -*-
import json, io, os

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch04/09_media.json"

BASE_NEG = ("photorealistic faces, anime style, western-only setting, Roman script labels, "
            "Devanagari script labels, generic Bollywood styling, north-Indian-only architecture, "
            "watermark, blurry, cluttered background, anachronistic objects, "
            "numerals or digits anywhere in the frame, comic-strip speech bubbles, "
            "motivational poster layout, text banner with a moral, moral lesson panel, "
            "caricature or exaggerated cartoon gag")
MED_NEG = (", blood, wounds or surgical imagery, exposed brain or anatomy, frightening horror "
           "lighting, distressing or pitiful depiction of a sick child, labelled anatomical diagram, "
           "medical infographic with callouts, brand logos on equipment")
BEE_NEG = (", cartoon bee with a human face or clothing, giant monster insect, swarm attack, "
           "a child being stung, a child reaching into or disturbing a hive, "
           "labelled bee-anatomy diagram, honey brand packaging or product advertisement")

BOY = ("The boy is thin and about thirteen, with short black hair, a narrow face, "
       "large dark eyes and light brown skin. ")
BOY_HOSP = BOY + "In hospital he wears a loose pale-blue cotton hospital pyjama set. "
MOTHER = ("The mother is about forty, of medium height, in a plain dull-green cotton sari with a "
          "narrow border, her hair pulled back in a low bun and a small red bindi on her forehead. ")
FATHER = ("The father is about forty-five, of medium build, in a light blue half-sleeved shirt and "
          "grey trousers, with short greying hair and thin metal spectacles. ")
SISTER = ("The elder sister is about twenty, in a green cotton kurta over churidar with a light "
          "dupatta, her long hair in a single plait. ")
ELDER = ("The family elder is a lean old man of about seventy in a white kurta and white dhoti, "
         "with white stubble, a bald crown and a cotton cloth over one shoulder. ")
DOCTOR = ("The neurologist is a calm man of about fifty in a white coat over a formal shirt and "
          "trousers, with short grey-flecked hair, metal-rimmed spectacles and a stethoscope round "
          "his neck. ")
NURSE = ("The nurse is a cheerful woman of about forty-five in a white nurse's uniform sari with a "
         "folded white cap and her hair in a bun. ")
HOSP_ROOM = ("The hospital room is a small plain room in a town hospital in Gujarat: cream "
             "distempered walls, a green rexine-covered iron bed with a thin mattress, a steel "
             "bedside stool holding a stainless-steel water jug and tumbler, a drip stand, a wall "
             "air-conditioner box, and one wide window with a plain metal frame. ")
VIEW = ("Through the window, across a narrow street, stands a plain three-storey concrete building "
        "with flat terraces, black plastic water tanks, clothes drying on a line and a broad "
        "concrete ledge; beyond it the low roofs of a Gujarati town with curved clay tiles, a neem "
        "tree, a whitewashed chabutaro bird-feeder on its pillar in the small chowk below, and a "
        "red-and-white state transport bus standing in the street. ")
STYLE = "Soft digital watercolour, vibrant textbook illustration style, 16:9."

def bar(line):
    return ("At the bottom of the frame a plain cream narrator bar carries exactly this one line of "
            "text, lettered in Gujarati script and in no other script: “" + line + "”. "
            "No other writing appears anywhere in the picture. ")

media = []

def add(topic_id, concept_id, title, description, teaching_notes, neg_extra, prompt):
    media.append({
        "topic_id": topic_id,
        "concept_id": concept_id,
        "id": concept_id + ".IMG1",
        "type": "image",
        "subtype": "illustration",
        "title": title,
        "description": description,
        "image_url": "",
        "aspect_ratio": "16:9",
        "home_concept_id": concept_id,
        "objective_id": None,
        "image_category": "illustration",
        "teaching_notes": teaching_notes,
        "negative_prompt": BASE_NEG + neg_extra,
        "generation_prompt": prompt,
    })

# ---------------- T1 ----------------
add("M1.S1.T1", "M1.S1.T1.C1",
    "થાકીને સોફા પર પડેલો સ્વપ્નિલ",
    "નિશાળેથી આવીને દફતર ફેંકી સોફા પર આડા પડેલા છોકરાએ બે હાથે માથું પકડ્યું છે અને મમ્મી પાણીનો ગ્લાસ લઈને એની સામે ઝૂકે છે.",
    "ચિત્ર બન્યા પહેલાં પણ વર્ગને પૂછો — આ ચિત્રમાં કઈ કઈ નિશાની દેખાય છે ? ફેંકેલું દફતર, અધૂરાં કઢાયેલાં શૂઝ, માંડ પિવાયેલું પાણી, પકડેલું માથું — બાળકો પાસે એ જ ક્રમમાં બોલાવો, અને પછી પૂછો કે લેખકે બીમારીનું નામ ક્યાંય લખ્યું છે ખરું ?",
    MED_NEG,
    "Late afternoon in the front room of an ordinary middle-class home in a Gujarati town: a "
    "polished wooden swing seat hanging on chains from the ceiling in one corner, a speckled "
    "terrazzo floor, a low wooden table, cotton curtains half drawn at a window, and a tulsi plant "
    "in a clay pot on the window ledge outside. A thin boy has thrown himself sideways along a "
    "brown fabric sofa, still in his plain school uniform of a white half-sleeved shirt and navy "
    "blue shorts, both hands pressed hard to his temples, eyes squeezed shut, his face tight with "
    "pain and his shoulders drawn in as if shivering. " + BOY +
    "A cloth school bag lies where it was flung on the floor, and one black school shoe is half off "
    "his foot. His mother leans over him, one knee on the floor, holding out a steel tumbler of "
    "water with a worried, watchful face; her other hand hovers near his forehead. " + MOTHER +
    "Warm low afternoon light through the curtains, an anxious quiet mood. " +
    bar("મારું માથુ સખત દુખે છે.") + STYLE)

# ---------------- T2 ----------------
add("M1.S2.T2", "M1.S2.T2.C2",
    "પલંગ પાસે ઊંચા થયેલા જીવ",
    "હૉસ્પિટલના ઓરડામાં ઇન્જેકશન પછી સૂઈ ગયેલા છોકરાની પથારી પાસે ડૉક્ટર કેટ-સ્કેનની ફિલ્મ અજવાળા સામે ધરે છે અને ઘરનાં બધાં ચિંતાભર્યા મોઢે જુએ છે.",
    "ચિત્રમાં દરેક ચહેરો બતાવીને પૂછો — કોનો જીવ ઊંચો થયો છે ? પછી ‘જીવ ઊંચો થવો’નો પાઠમાં છપાયેલો અર્થ — ઉચાટ થવો, ચિંતા થવી — બોલાવીને ચિત્રમાં દેખાતી બે-ત્રણ નિશાની સાથે જોડો; ફિલ્મમાં શું દેખાય છે એની કલ્પના ઉમેરવા દેવી નહીં.",
    MED_NEG,
    "Night in a small hospital room in a town in Gujarat. " + HOSP_ROOM +
    "A thin boy lies asleep on the bed under a white sheet, his face slack and calm, a thin drip "
    "line taped to one arm. " + BOY_HOSP +
    "Standing at the head of the bed, a doctor holds a dark scan film up against a small wall "
    "light-box; the image on the film is kept soft, grey and indistinct, with no writing on it. "
    "The doctor is a young duty doctor of about thirty in a white coat over blue scrubs, one arm "
    "raised to the light-box, his expression serious. Clustered at the foot of the bed stand the "
    "boy's father, still holding a mobile phone at his side, the boy's mother with both hands "
    "pressed together at her mouth, and a young woman of about twenty; behind them a lean elderly "
    "man rests a steadying hand on the mother's shoulder and speaks quietly. " + FATHER + MOTHER +
    SISTER + ELDER +
    "Through the window, a white ambulance van stands in the lit hospital compound below. Cool "
    "hospital light, faces tense and hushed. " +
    bar("કેટ-સ્કેનમાં મગજમાં ગાંઠ દેખાઈ.") + STYLE)

# ---------------- T3 ----------------
add("M1.S2.T3", "M1.S2.T3.C3",
    "ડૉક્ટરે બતાવેલો દવાનો રસ્તો",
    "રિપોર્ટ્સ હાથમાં લઈને ન્યૂરોલૉજિસ્ટ પલંગ પાસે ઊભા રહી સમજાવે છે અને સાંભળતાં સાંભળતાં મમ્મીનું મોં પડી જાય છે.",
    "પહેલાં ચિત્રમાં મમ્મીનું મોં બતાવો, પછી પાઠમાં છપાયેલો ‘મોં પડી જવું — મોં ફિક્કું પડી જવું’ અર્થ બોલાવો, અને છેલ્લે પૂછો — મોં પડી ગયું તોય એ કેમ તૈયાર થયાં ? જવાબ પાઠના શબ્દોમાં જ શોધાવો.",
    MED_NEG,
    "Late morning in a small hospital room in a town in Gujarat. " + HOSP_ROOM +
    "A neurologist stands beside the bed holding an open folder of report papers in one hand, the "
    "other hand lifted with the fingers slightly spread as he explains something carefully; his "
    "manner is gentle and unhurried. " + DOCTOR +
    "A thin boy sits propped against two pillows on the bed, listening, his head turned towards the "
    "doctor. " + BOY_HOSP +
    "The boy's mother stands close to the bedside with one hand gripping the iron bed rail; her "
    "face has gone pale and slack, the corners of her mouth pulled down, though she is nodding. " +
    MOTHER + "The boy's father stands just behind her, arms folded, listening hard. " + FATHER +
    "A brown paper report envelope and a folded scan film lie on the bedside stool. Plain daylight "
    "through the window, a grave but not frightening mood. " +
    bar("દવા આપીને ગાંઠ ઓગાળવાના પ્રયત્નો કરીશું.") + STYLE)

# ---------------- T4 ----------------
add("M1.S3.T4", "M1.S3.T4.C4",
    "માથે ફરતો માનો હાથ",
    "લાંબા કંટાળાભર્યા બપોરે પથારીમાં પડેલા છોકરાના માથા પર મમ્મી હળવેથી હાથ ફેરવે છે અને બાજુમાં વાંચવાનું બંધ પડેલું પુસ્તક ઊંધું પડ્યું છે.",
    "ચિત્રમાં દેખાતી કંટાળાની બે નિશાની — બંધ પડેલું પુસ્તક ને ખાલી છત તાકતી નજર — બાળકો પાસે શોધાવો, પછી પૂછો કે પાઠમાં છોકરાને એવું કેમ લાગ્યું કે દવા નહીં પણ માનો હાથ એને સાજો કરી રહ્યો છે ?",
    MED_NEG,
    "A long, still afternoon in a small hospital room in a town in Gujarat. " + HOSP_ROOM +
    "A thin boy lies flat on the bed with his head on a pillow, arms loose at his sides, staring up "
    "at the ceiling with a bored, listless expression. " + BOY_HOSP +
    "His mother sits on the edge of the bed, turned towards him, passing her hand lightly over his "
    "forehead and hair; she is speaking softly and her face is calm and tender. " + MOTHER +
    "On the bedside stool stand a stainless-steel three-tier tiffin carrier brought from home, a "
    "water tumbler and a small strip of tablets. A closed book lies face down and pushed aside on "
    "the bed. The window is shut, the wall air-conditioner running. Quiet golden afternoon light "
    "falling in one slab across the bed; the mood is slow and tired but warm. " +
    bar("માનો હાથ સાજો કરી રહ્યો છે.") + STYLE)

# ---------------- T5 ----------------
add("M2.S4.T5", "M2.S4.T5.C5",
    "ખૂલેલી બારી અને દૂરબીન",
    "નર્સે ખોલી આપેલી બારીએ ઊભા રહીને છોકરો દૂરબીન માંડે છે અને સામેના મકાનના ઉપલા માળની પાળી નીચે લટકતો મોટો મધપૂડો દેખાય છે.",
    "ચિત્રમાં છોકરો ક્યાં ઊભો છે એ ખાસ બતાવો — બારીની અંદર, દૂરથી, દૂરબીનથી. પછી પૂછો કે માખીઓ ઓરડામાં આવી ત્યારે એણે પહેલાં શું કર્યું હતું; સાચા મધપૂડા પાસે જવાનું નહીં, દૂરથી જોવાનું — એ વાત અહીં જ કહી દો.",
    BEE_NEG,
    "Morning in a small hospital room in a town in Gujarat. " + HOSP_ROOM +
    "The wide window has just been pushed open and fresh air moves the curtain. A thin boy stands "
    "at the open window in his hospital clothes, up on the balls of his feet, holding a pair of "
    "small black binoculars to his eyes with both hands, his whole body leaning towards the view; "
    "his mouth is open in surprise. " + BOY_HOSP +
    "A nurse stands beside him with one hand still on the window latch, smiling indulgently. " +
    NURSE + VIEW +
    "Under the broad concrete ledge of the facing building's upper floor hangs a large brown "
    "honeycomb, clearly visible, with a haze of tiny honeybees moving around it. Two or three bees "
    "have drifted near the open window. Clear bright morning light, an eager curious mood. " +
    bar("બારી ખૂલી ને સામે મધપૂડો દેખાયો.") + STYLE)

# ---------------- T6 ----------------
add("M2.S5.T6", "M2.S5.T6.C7",
    "પૂડા પર ભમતી માખીનું નૃત્ય",
    "તડકામાં લટકતા મધપૂડાની સપાટી પર ફૂલ શોધીને પાછી ફરેલી ભમતી મધમાખી આંટા લેતું નૃત્ય કરે છે અને આજુબાજુ ઊભેલી કામગરી માખીઓ એની સામે ફરીને જુએ છે.",
    "ચિત્રમાં નાચતી માખી ને એની સામે ફરેલી માખીઓ બતાવીને પૂછો — આ નૃત્યથી બીજી માખીઓને શું ખબર પડે છે ? જવાબમાં પાઠના બે જ મુદ્દા બોલાવો : દિશા સૂરજનાં કિરણો સાથેના ખૂણાથી, અને અંતર નૃત્ય ધીમું છે કે ઝડપી એના પરથી.",
    BEE_NEG,
    "A very close view, in bright mid-morning sunlight, of the surface of a large wild honeycomb "
    "hanging under a broad concrete ledge on the upper floor of a plain building in a Gujarati "
    "town. The comb is a warm brown sheet of six-sided wax cells, some capped, some glistening, "
    "and dozens of honeybees are crowded over it. In the centre of the comb one bee is dancing on "
    "the wax: her body is tilted at a slant, her abdomen shivering, and her looping curved path "
    "over the surface is shown as a faint pale trail of light that doubles back on itself in a soft "
    "curl. The bees around her have all turned to face her, antennae forward, standing still and "
    "attentive, while other bees keep crawling in and out at the edges of the comb. Slanting golden "
    "sun-rays come in from one side and fall across the dancing bee, and a few loose pollen grains "
    "cling to her hind legs. Out of focus far beyond the ledge lie the flat terraces of the town "
    "and a distant blur of yellow flowering fields. The bees are drawn as real honeybees, "
    "beautifully detailed, never as cartoon characters. Bright, busy, wonder-struck mood. " +
    bar("નૃત્ય કરીને એ દિશા ને અંતર કહી દે છે.") + STYLE)

# ---------------- T7 ----------------
add("M2.S5.T7", "M2.S5.T7.C8",
    "ફૂલ પર બેઠેલી મધમાખી",
    "ખેતરના ફૂલ પર બેઠેલી મધમાખીના પગે પરાગકણ ચોંટ્યા છે, પાછળ એ જ ખેતરમાં કપાસ ને બાજરીના ડૂંડાં ઝૂકે છે અને આગળ પથ્થર પર મધની નાનકડી શીશી તડકામાં ચમકે છે.",
    "ચિત્રમાં માખીના પગ પરના પરાગકણ પર આંગળી મુકાવો ને પૂછો — માખી અહીં કયું કામ ‘જાણે અજાણ્યે’ કરી રહી છે ? પછી પાછળનાં ફળ-અનાજ ને આગળની મધની શીશી જોડીને પાઠનું વાક્ય શોધાવો; મધ વિશે પાઠમાં ન લખેલી કોઈ વાત ઉમેરવી નહીં.",
    BEE_NEG,
    "Early morning in an open field on the edge of a village in Gujarat. In sharp close-up in the "
    "middle of the frame, a single honeybee has settled on a pale cream-and-pink cotton flower; her "
    "hind legs carry two fat golden-orange lumps of pollen and a dusting of pollen grains lies "
    "along her furry back. The bee is drawn as a real honeybee, beautifully detailed, never as a "
    "cartoon character. Behind her, slightly out of focus, the same field runs back in rows: cotton "
    "plants with a few burst white bolls, and beyond them a strip of bajra with heavy grain ears "
    "bending over, then a thorn fence, a lone neem tree and a low mud-plastered farm hut with a "
    "curved clay-tiled roof. In the near foreground, on a flat grey stone at the edge of the field, "
    "stands a small clear glass bottle of dark amber honey with a wooden stopper, the low sun "
    "shining through it and throwing a warm patch of light on the stone. Fresh dew, long soft "
    "shadows, a calm and grateful mood. " +
    bar("મધ ઔષધી તરીકે ઉપયોગી છે.") + STYLE)

# ---------------- T8 ----------------
add("M3.S6.T8", "M3.S6.T8.C9",
    "આંગળી પર બેઠેલી દોસ્ત",
    "પથારીમાં બેઠેલા છોકરાએ હાથ લંબાવ્યો છે, એક મધમાખી એની આંગળી પર બેઠી છે અને બીજી આંગળીના ટેરવે મધનું ઝીણું ટીપું ચમકે છે.",
    "ચિત્રમાં છોકરાના મોઢા પરનો ડર ગયો ને મજા આવી એ બદલાવ બતાવો, અને સાથે વર્ગને ચોખ્ખું કહો — વાર્તામાં બને છે એટલે સાચી મધમાખીને હાથ ધરવો કે અડવું નહીં, અને ચામડી પર ચોંટેલું કશું પણ ચાખવું નહીં; સાચી માખી પોતાનો બચાવ કરવા કરડે છે.",
    BEE_NEG,
    "Bright morning in a small hospital room in a town in Gujarat. " + HOSP_ROOM +
    "The window is wide open and light pours in. A thin boy sits upright on the bed, his legs "
    "crossed under him, one arm stretched out straight and steady in front of him with the palm "
    "turned up and the fingers open. On the tip of his index finger a single honeybee has settled, "
    "small and calm; on the tip of his middle finger sits one tiny glistening bead of golden honey, "
    "catching the light. His face is lit with quiet delight and wonder, eyes wide, lips just "
    "parted, not a trace of fear. " + BOY_HOSP +
    "Four or five more honeybees drift in slow loops around the room and near his head, drawn as "
    "real honeybees, beautifully detailed, never as cartoon characters and never menacing. Through "
    "the open window, across the narrow street, the broad concrete ledge of the facing building "
    "carries the large brown honeycomb. A pair of small black binoculars lies on the bedsheet "
    "beside him. Warm still air, a hushed and magical mood. " +
    bar("આંગળીને ટેરવે મધનું ટીપું.") + STYLE)

# ---------------- T9 ----------------
add("M3.S7.T9", "M3.S7.T9.C10",
    "ખાલી પડેલી સામેની દીવાલ",
    "રજા મળ્યાના સમાચાર પછી બારી ખોલીને જુએ છે તો સામેની પાળી નીચે મધપૂડો નથી, ખાલી ડાઘ છે અને બે-ત્રણ મધમાખી બારી પાસે આંટા મારે છે.",
    "ચિત્રમાં એક બાજુ છોકરાની સાજા થવાની ખુશી ને બીજી બાજુ ખાલી પડેલી પાળી — બન્ને સાથે બતાવો, અને પૂછો કે એની નિરાશાનું કારણ પાઠમાં કોણે અને કયા શબ્દોમાં જણાવ્યું ?",
    BEE_NEG,
    "Late morning in a small hospital room in a town in Gujarat. " + HOSP_ROOM +
    "A thin boy stands alone at the window, which he has just pushed open; one hand is still on the "
    "window frame and he is leaning out slightly, looking across the street. His shoulders have "
    "dropped and his face is fallen and disappointed, the smile gone out of it. " + BOY_HOSP +
    "On the bed behind him lie a folded blanket, a packed cloth bag and his binoculars, ready to go "
    "home. " + VIEW +
    "The broad concrete ledge of the facing building is bare: where the honeycomb hung there is now "
    "only a dark stain and a few scraps of wax on the concrete. Two or three honeybees circle "
    "slowly in the air just outside his open window, drawn as real honeybees, beautifully detailed, "
    "never as cartoon characters. Flat bright daylight, an emptied, wistful mood. " +
    bar("બારી ખોલી તો મધપૂડો ગાયબ.") + STYLE)

# ---------------- T10 ----------------
add("M3.S8.T10", "M3.S8.T10.C11",
    "કાનમાં કહેવાયેલી વાત",
    "હૉસ્પિટલના પગથિયાં ઊતરતાં ચૂપચાપ ચાલતા છોકરાના કાનમાં મોટી બહેન ધીમેથી કશુંક કહે છે અને એનું મોઢું એકદમ ખીલી ઊઠે છે.",
    "ચિત્રમાં પહેલાં એનું ચૂપ ચાલવું ને પછી ખીલી ઊઠેલું મોઢું બતાવીને પૂછો — બહેને કાનમાં કહેલી વાત સાંભળીને એને પેલી બે મધમાખી વિશે શું સમજાયું ? જવાબ પાઠના છેલ્લા ફકરાના શબ્દોમાં જ બોલાવો.",
    BEE_NEG,
    "Late morning on the front steps of a small town hospital in Gujarat: a cream-painted building "
    "with a plain porch on concrete pillars, a few potted plants along the steps, an autorickshaw "
    "and a red-and-white state transport bus in the street beyond, a whitewashed chabutaro "
    "bird-feeder on its pillar in the chowk across the road, and low town roofs of curved clay "
    "tiles behind it. A thin boy, discharged and back in home clothes — a blue checked "
    "half-sleeved shirt and grey trousers — is walking down the steps with his family, a little "
    "apart from them, his hands in his pockets and his face still turned back and preoccupied. " +
    BOY +
    "A young woman of about twenty has bent close to his ear from behind, one hand cupped beside "
    "her mouth, whispering something with a mischievous smile. " + SISTER +
    "The boy has stopped mid-step and swung his head round towards her; his eyes are huge and his "
    "whole face has just lit up with astonished joy. Behind them the boy's father carries a cloth "
    "bag and the boy's mother carries a steel tiffin carrier, both smiling. " + FATHER + MOTHER +
    "Bright open daylight, a lifting, happy mood. " +
    bar("આપણા ઘરની સામેના ઝાડ પર એક મધપૂડો બની રહ્યો છે.") + STYLE)

TOOL_SPEC = (
 "બાળક જાતે ચલાવે એવું એક જ ઇન્ટરેક્ટિવ ચિત્ર — ‘ભમતી માખી શું કહી ગઈ ?’. પડદો બે ભાગમાં : ડાબી બાજુ "
 "ઉપરથી દેખાતું ખેતર-ગામ, જેમાં જુદી જુદી જગ્યાએ ફૂલોના ઝુંડ પડ્યાં છે; જમણી બાજુ પાળી નીચે લટકતા "
 "મધપૂડાની સપાટી, જેના પર ભમતી મધમાખી ને ચારે બાજુ કામગરી મધમાખીઓ ઊભી છે. આકાશમાં સૂરજ દેખાય છે ને "
 "એનાં કિરણો પૂડા પર પડે છે. પહેલું : બાળક ડાબી બાજુના નકશા પર કોઈ પણ એક ફૂલઝુંડ પર આંગળી મૂકે — એ જ "
 "ઘડીએ જમણી બાજુ ભમતી માખી પૂડાની સપાટી પર નાચવા માંડે છે, ને એનો આંટો પાઠમાં કહ્યું છે તેમ ‘ળ’ જેવો "
 "દોરાય છે. બીજું : બાળક ફૂલઝુંડ સૂરજની આ બાજુ કે પેલી બાજુ ખસેડે — તો પૂડા પરના નૃત્યનો ખૂણો સૂરજનાં "
 "કિરણોની સામે એટલો જ ફરે છે, ને કામગરી માખીઓ ઊડીને જે દિશામાં જાય છે તે દિશા પણ સાથે જ ફરે છે. એટલે "
 "બાળક પોતે જુએ છે કે દિશા ખૂણા સાથે બંધાયેલી છે. ત્રીજું : બાળક ફૂલઝુંડ પૂડાથી દૂર ખેંચે તો નૃત્ય ધીમું "
 "પડતું જાય છે, ને પાસે લાવે તો ઝડપી થતું જાય છે — બાળક જાતે ધીમા-ઝડપીનો સંબંધ અંતર સાથે જોડે છે. "
 "ચોથું : ‘હવે તમે કહો’ બટન દબાવતાં ફૂલઝુંડ સંતાઈ જાય છે ને ફક્ત નૃત્ય ચાલુ રહે છે; બાળક નકશા પર જ્યાં "
 "એને લાગે ત્યાં આંગળી મૂકે, ને પછી ફૂલઝુંડ પાછું દેખાય — બરાબર હોય તો કામગરી માખીઓ ઊડીને ત્યાં પહોંચે "
 "છે, ખોટું હોય તો નૃત્ય ફરી એક વાર ધીમેથી બતાવાય છે. પડદા પરના બધા શબ્દો પાઠના પોતાના જ રહે — ભમતી "
 "મધમાખી, કામગરી મધમાખી, નૃત્ય, ખૂણો, સૂરજનાં કિરણો, દિશા, અંતર, ધીમું, ઝડપી. પડદા પર કોઈ આંકડો, કોઈ "
 "અંશ-માપ કે કોઈ અંગ્રેજી-દેવનાગરી લખાણ ન આવે, અને માખીના શરીરની આકૃતિ કે નામનિર્દેશવાળી વૈજ્ઞાનિક "
 "આકૃતિ પડદા પર ન મૂકવી."
)

doc = {
 "media": media,
 "2d_tool": {"topic_id": "M2.S5.T6", "spec": TOOL_SPEC},
 "reuse_report": {"scenes": 10, "reused": 0, "authored": 10, "rejected": []},
}

with io.open(OUT, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("wrote", OUT, len(media))
