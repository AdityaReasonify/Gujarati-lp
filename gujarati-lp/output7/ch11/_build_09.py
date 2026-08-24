# -*- coding: utf-8 -*-
import json, io, os

STYLE = ("Soft digital watercolour, vibrant textbook illustration style, warm daylight palette, 16:9. "
         "A plain cream narrator bar runs along the bottom edge of the frame carrying exactly this one "
         "line of Gujarati text, lettered in clean Gujarati script and nothing else: ")

GURU = ("The teacher is a lean elderly man of about sixty with a long white beard, a shaved head, a "
        "saffron-ochre cotton robe worn over one shoulder, a tall wooden staff and bare feet.")
CHELA = ("The disciple is a young man of about eighteen with a round face, a shaved head with a small "
         "tuft of hair at the back, a plain pale-ochre cloth wrapped over one shoulder and bare feet.")
CHELA_FAT = CHELA[:-1] + ", now visibly well fed, round-bellied and glossy-cheeked."
KING = ("The king is a plump man of about fifty in a green-and-gold brocade long coat and a jewelled "
        "saffron turban with a small plume, with a thick curled moustache.")
VANIK = ("The merchant is a stout man of about forty-five in a white dhoti, a long white coat and a "
         "red-bordered turban, with a gold hoop in one ear.")
KADIYO = ("The mason is a wiry man of about thirty-five in a short dhoti with a checked cloth tied round "
          "his head, a trowel in his hand and dried lime dust on his forearms.")
GARO = ("The mortar mixer is a broad-shouldered man of about forty, bare-chested with his dhoti rolled "
        "above the knee, dried mud on his hands and shins and a long wooden mixing hoe over his shoulder.")
PAKHALI = ("The water carrier is a wiry man of about thirty with a large stitched leather water bag slung "
           "across his back, a soaked shoulder cloth and a short dhoti.")
MULLA = ("The thin elderly townsman is a slight, upright man in a plain white long shirt, loose white "
         "trousers, a small white cap and a neatly trimmed grey beard, walking with quiet dignity.")
GUARDS = ("The two town guards wear plain white tunics, red waist sashes and folded turbans, and each "
          "carries a bamboo staff.")
TOWN = ("a nineteenth-century Gujarati town: low houses roofed with curved clay tiles, raised stone "
        "sitting-platforms running along the house fronts, carved wooden brackets under the upper storeys")

NEG_BASE = ("photorealistic faces, anime style, western-only setting, Roman script labels, Devanagari "
            "script labels, generic Bollywood styling, north-Indian-only architecture, watermark, blurry, "
            "cluttered background, anachronistic objects, digits or numerals anywhere in the frame, "
            "modern clothing, plastic objects, motivational poster layout, text banner with a moral, "
            "moral lesson panel, caricature or mockery of any religious or occupational community")
NEG_DARK = (", blood, gore, injured or crushed bodies, a body impaled on the stake, any depicted "
            "execution, horror imagery")

media = []

def node(topic_id, concept_id, title, desc, notes, prompt, neg):
    media.append({
        "topic_id": topic_id,
        "concept_id": concept_id,
        "id": concept_id + ".IMG1",
        "type": "image",
        "subtype": "illustration",
        "title": title,
        "description": desc,
        "image_url": "",
        "aspect_ratio": "16:9",
        "home_concept_id": concept_id,
        "objective_id": None,
        "image_category": "illustration",
        "teaching_notes": notes,
        "negative_prompt": neg,
        "generation_prompt": prompt,
    })

# ---------------- T1 ----------------
node(
 "M1.S1.T1", "M1.S1.T1.C1",
 "એક જ ભાવે વેચાતું બજાર",
 "નગરીના ચોકમાં ભાજીની ટોપલી ને ખાજાંનો થાળ સામસામે, બંને પાસે એક જ ત્રાજવું, એક જ કાટલું ને પડખે એક જ ટકો, ને છેડે ગાદીએ બેઠેલો ગંડુ રાજા.",
 "ચિત્ર બને ત્યાં સુધી આ દૃશ્ય બોલીને વર્ગમાં ઊભું કરો — બે ટોપલી, બે સરખાં ત્રાજવાં ને પડખે એક જ ટકો — ને પછી બાળકોને પૂછો કે ભાજી ને ખાજાં એક જ ભાવે વેચાતાં હોય તો ખરીદનારને શું લાગે.",
 ("A market square at mid-morning in " + TOWN + ", with a tall whitewashed pillared bird-feeder tower "
  "standing at the centre of the square and pigeons on its ledge. Two neighbouring stalls face the "
  "viewer under cloth awnings: one heaped with fresh green leafy vegetables in cane baskets, the other "
  "with trays of pale flaky sweet pastries. In front of each stall stands an identical brass balance "
  "scale holding the same single stone weight, and beside each scale one small copper coin lies on the "
  "spread cloth. Between the two stalls a woman shopper in a red-bordered cotton sari stands with one "
  "hand on each basket, looking back and forth in comic disbelief. At the edge of the square " + KING +
  " He sits cross-legged on a low cushioned platform under a scalloped cloth canopy, grinning vacantly "
  "while a servant fans him with a long-handled fan. A bullock cart rests under a thatched awning and a "
  "neem tree shades one corner. " + STYLE + "ટકે શેર ભાજી ટકે શેર ખાજાં."),
 NEG_BASE + ", price boards, written signboards, shop lettering",
)

# ---------------- T2 ----------------
node(
 "M1.S2.T2", "M1.S2.T2.C2",
 "હાટથી લીધેલી સુખડી",
 "હાટને ઓટલે ઊભેલો શિષ્ય એક હાથે લોટનું પોટલું આપે છે ને બીજા હાથે પાંદડે વીંટેલી સુખડી લે છે; શેરીને છેડે લીમડા નીચે ગુરુ જોઈ રહ્યા છે.",
 "ચિત્ર બને ત્યાં સુધી વર્ગને આ ક્ષણ કલ્પવા કહો — એક હાથે આટો ગયો ને બીજા હાથે સુખડી આવી — ને પછી પૂછો કે શિષ્યને એમાં ‘ખૂબ ખાટ્યો’ કેમ લાગ્યું.",
 ("The shopfront of a grain-and-sweets seller, raised on a stone platform in a narrow lane of " + TOWN +
  ". " + CHELA + " He stands at the shop step, handing over an open cloth bundle of pale wheat flour with "
  "one hand while the shopkeeper — a lean man of about fifty in a white dhoti and a folded white turban, "
  "sitting cross-legged behind his low counter — places a leaf-wrapped block of dark crumbly sweet into "
  "the disciple's other hand. A brass balance scale hangs from the shop beam with a stone weight in one "
  "pan; earthen jars, cane baskets and stacked leaf-plates line the shelves behind. At the far end of the "
  "lane " + GURU + " He waits under a neem tree, both hands on his staff, watching. A stray dog sleeps on "
  "the stone platform and morning light slants down the lane. " + STYLE + "લીધી સુખડી હાટથી આપી આટો"),
 NEG_BASE + ", price boards, written signboards, shop lettering",
)

# ---------------- T3 ----------------
node(
 "M1.S2.T3", "M1.S2.T3.C3",
 "સાંજે ગુરુની ના",
 "સાંજે ગામના દરવાજા ભણી લાકડી ચીંધીને ઊભેલા ગુરુ, ને સામે ઓટલે સુખડી લઈને બેઠેલો શિષ્ય માથું ધુણાવીને ના પાડે છે.",
 "ચિત્ર બને ત્યાં સુધી બે ઊભાં પાત્રો શબ્દોથી દોરી બતાવો — એક જવાનું કહે છે, બીજો રહેવા માગે છે — ને પછી પૂછો કે ગુરુને આ નગરીની કઈ વાતથી બીક લાગે છે.",
 ("Evening light in " + TOWN + ", at the arched town gate at the end of the lane, with the open red-earth "
  "road and low thorn scrub visible beyond it. " + GURU + " He stands in the middle of the lane, his body "
  "already turned towards the gate, one arm stretched out and his staff pointing down the road out of "
  "town, his face urgent. " + CHELA + " He sits comfortably on a raised stone sitting-platform against the "
  "house wall, the leaf-wrapped block of sweet open on his knee and a piece of it halfway to his mouth, "
  "shaking his head and lifting his free palm in cheerful refusal. Lamps are being lit in a doorway "
  "behind him, a woman draws water from a clay pot stand, and the sky is going violet above the "
  "clay-tile roofs. " + STYLE + "ચલો સધ ચેલા જવું ગામ બીજે."),
 NEG_BASE,
)

# ---------------- T4 ----------------
node(
 "M2.S3.T4", "M2.S3.T4.C5",
 "પ્રભાતે પડેલી ભીંત",
 "સવારે વણિકના ઘરની પડી ગયેલી ભીંતનો ઈંટ-માટીનો ઢગલો ને પાયા પાસે ખોદેલું બાકોરું; પડખે હાથ ઊંચા કરીને ફરિયાદ કરતી ડોશી ને દરવાજે ઊભેલો વણિક.",
 "ચિત્ર બને ત્યાં સુધી ઢગલો, ધૂળ ને ખોદેલું બાકોરું જ વર્ણવો — કશું બિહામણું નહીં — ને પછી પૂછો કે ડોશીની ફરિયાદ સાંભળ્યા પછી સજા કોના પર ઠરી.",
 ("Early morning light in a lane of " + TOWN + ". The side wall of a merchant's two-storey house has "
  "collapsed into a heap of mud bricks and dust; a freshly dug hole gapes at the base of the part of the "
  "wall still standing and an iron digging bar lies abandoned on the rubble. Nobody is under the bricks "
  "and nothing gruesome is shown. Neighbours in white dhotis and cotton saris crowd at a distance with "
  "hands over their mouths. In the foreground a small stooped old woman in a coarse dark-maroon sari with "
  "a worn shoulder cloth raises both hands, wailing, towards two town guards. " + GUARDS + " " + VANIK +
  " He stands in his own doorway staring at the rubble with his hands spread wide. Dust still hangs in "
  "the slanting light, a clay water pot stand sits by the door and a crow watches from the tiled roof. " +
  STYLE + "તહાં ભીંત તૂટી પડી, ચોર દબાયા ચાર."),
 NEG_BASE + NEG_DARK,
)

# ---------------- T5 ----------------
node(
 "M2.S3.T5", "M2.S3.T5.C6",
 "વણિકનો બચાવ",
 "દરબારના ચોકમાં હાથ જોડીને ઊભેલો વણિક એક હાથ લંબાવીને કડિયા તરફ ચીંધે છે, ને હાથમાં થાપી લઈને ઊભેલો કડિયો મોં ખોલીને જોઈ રહે છે.",
 "ચિત્ર બને ત્યાં સુધી ચીંધાતી આંગળી પર ધ્યાન ખેંચો ને પૂછો કે વણિક પોતાના પરથી વાંક કઈ રીતે ખસેડે છે — અહીં ‘ખોડ’ એટલે ભૂલ, વાંક.",
 ("Late morning in the open courtyard where " + TOWN.split(':')[0] + " holds its court of justice: a "
  "scalloped cloth canopy stretched on painted wooden poles over a whitewashed dais, clay-tile roofs and "
  "carved wooden brackets rising behind, a raised stone sitting-platform along one wall. " + KING +
  " He sits cross-legged on the low cushioned platform, leaning forward with one eyebrow raised. Before "
  "him " + VANIK + " He stands with his palms half joined but one arm flung out to the side, pointing "
  "accusingly at the mason. " + KADIYO + " The mason stands a few steps away, mouth open in astonishment, "
  "his free hand on his chest. A few broken mud bricks lie on the ground between them. Townsfolk in white "
  "dhotis and cotton saris watch from the edge of the courtyard, and a servant with a long-handled fan "
  "stands behind the platform. " + STYLE + "ખરેખર એમાં નથી, મારો ખોડ લગાર."),
 NEG_BASE + NEG_DARK,
)

# ---------------- T6 ----------------
node(
 "M2.S4.T6", "M2.S4.T6.C7",
 "ચીંધાતી આંગળીઓની હાર",
 "દરબારના એ જ ચોકમાં એક જ ક્ષણે કડિયો ગારો કરનાર તરફ ને ગારો કરનાર પખાલી તરફ આંગળી ચીંધે છે, ને પખાલીનું મોં આશ્ચર્યથી ખૂલે છે.",
 "ચિત્ર બને ત્યાં સુધી ત્રણ બાળકોને ઊભાં રાખીને આ સાંકળ ભજવાવો ને પછી પૂછો કે વાંક એક જણ પરથી બીજા પર ખસતો ખસતો છેલ્લે ક્યાં જઈને અટકે છે.",
 ("Midday in the same open courtyard of justice in " + TOWN + ", the scalloped cloth canopy on painted "
  "poles over the whitewashed dais. Three men stand in a diagonal line across the foreground, each caught "
  "in the same instant turning and pointing at the next. " + KADIYO + " He points back over his shoulder "
  "at the mortar mixer. " + GARO + " The mortar mixer has already swung round, his muddy arm flung out "
  "towards the water carrier. " + PAKHALI + " The water carrier stands last, his mouth opening in "
  "surprise, one hand rising in protest. A shallow pit of wet grey mortar and a spreading puddle of "
  "spilt water lie in the foreground with a mason's plumb line beside them. On the dais " + KING +
  " He watches with his chin propped on one hand, mildly entertained. Townsfolk lean in at the edges. " +
  STYLE + "ચૂક ગારો કરનારની, કડિયે કરી ઉચ્ચાર."),
 NEG_BASE + NEG_DARK,
)

# ---------------- T7 ----------------
node(
 "M2.S4.T7", "M2.S4.T7.C8",
 "પખાલીનું બહાનું",
 "રાજા હાથ ઊંચો કરીને હુકમ કરે છે ને પખાલી હાથ જોડીને રસ્તા ભણી ચીંધે છે, જ્યાં પાતળા શરીરના મુલ્લા શાંતિથી ચાલ્યા જાય છે.",
 "ચિત્ર બને ત્યાં સુધી કહો કે અહીં પણ વાંક બીજા પર ખસે છે; મુલ્લા પણ કડિયા ને પખાલીની જેમ ગામનું પોતાનું કામ કરતા એક માણસ છે, ને કાવ્યની મજાક તો નગરીના વિવેક વગરના ન્યાય પર છે.",
 ("Afternoon in the open courtyard of justice in " + TOWN + ", opening onto the lane beyond through a low "
  "arched gateway. " + KING + " He sits on his low cushioned platform under the scalloped canopy, one hand "
  "raised in an offhand, impatient command. " + PAKHALI + " He kneels on one knee before the platform with "
  "his palms joined, his face pleading, while his free hand points away through the archway down the "
  "sunlit lane. " + MULLA + " He walks past out there in the lane, a cloth-wrapped book under his arm, "
  "entirely unaware of the courtyard, drawn with warmth and respect. His empty leather water bag lies "
  "beside the kneeling water carrier next to a dark wet patch of spilt water on the paving. Townsfolk "
  "watch from the shade of a raised stone sitting-platform. " + STYLE +
  "પાણી અધિક તેથી પડ્યું, રાજા છાંડો રીસ."),
 NEG_BASE + NEG_DARK + ", stereotyped or comic depiction of a religious figure",
)

# ---------------- T8 ----------------
node(
 "M2.S5.T8", "M2.S5.T8.C10",
 "જાડા નરની શોધમાં",
 "સાંકડી શેરીના ઓટલે જમીને ઊંઘી ગયેલા તાજામાજા જોગીને જોઈને બે સિપાઈ અટકી જાય છે ને એકબીજાને કોણી મારીને ચીંધે છે.",
 "ચિત્ર બને ત્યાં સુધી આ એક જ ક્ષણ પર રહો — સિપાઈઓએ કોને શોધી કાઢ્યો — ને પછી પૂછો કે ‘જાડા નરને જોઈ’ એવો હુકમ કેમ કરવો પડ્યો.",
 ("Afternoon in a narrow lane of " + TOWN + ", washing hung on a line above and a cow chewing at a bundle "
  "of fodder by the wall. Two town guards have stopped short in mid-stride and are pointing at a young "
  "ascetic dozing on a raised stone sitting-platform after a heavy meal. " + GUARDS + " One guard nudges "
  "the other with his elbow, both grinning with the delight of a lucky find. " + CHELA_FAT + " He is "
  "sprawled asleep against the house wall with his hands folded on his stomach, an empty brass bowl "
  "tipped over beside him and a few crumbs of sweet on an open leaf. Afternoon shadow cuts across the "
  "lane, a clay water pot stand sits by a doorway, and clay-tile roofs close overhead. " + STYLE +
  "જોતા જોતા એ જડ્યો, જોગી જાડે અંગ,"),
 NEG_BASE + NEG_DARK,
)

# ---------------- T9 ----------------
node(
 "M3.S6.T9", "M3.S6.T9.C11",
 "શૂળી પાસે ગુરુની વાત",
 "ગામ બહાર ખુલ્લા મેદાનમાં ખોડેલા કોરા થાંભલા પાસે ઊભા રહીને ગુરુ હાથ ઊંચો કરીને રાજાને કંઈક કહે છે, ને રાજા ગાદી પરથી અધૂરો ઊભો થઈને ઝૂકે છે.",
 "ચિત્ર બને ત્યાં સુધી બે ચહેરા વર્ણવો — ગુરુની ઉતાવળ ને રાજાનો ચમકતો લોભ — ને પછી પૂછો કે ગુરુની વાત સાંભળીને રાજાના મનમાં શું બદલાયું.",
 ("Late afternoon on open ground just outside " + TOWN + ", with dry red earth, low thorn scrub, a stepped "
  "stone well to one side and the town's clay-tile roofs behind. A single tall bare wooden post with a "
  "blunt rounded top stands planted in the ground; nobody is on it, nothing hangs from it and nothing "
  "gruesome is shown. " + GURU + " He stands at the foot of the post with one palm raised and his face "
  "bright with urgent, confiding excitement, speaking upward and across to the king. " + KING + " He has "
  "half risen from his low cushioned platform under its canopy, leaning forward with sudden greedy "
  "interest, one hand gripping the cushion. " + CHELA_FAT + " He waits beside the post between two town "
  "guards, watching the teacher with dawning hope. " + GUARDS + " A crowd of townsfolk presses closer at "
  "the edges, and a flock of green parrots crosses the deep golden sky above. " + STYLE +
  "આ અવસર શૂળીએ ચઢે, વેગે મળે વિમાન."),
 NEG_BASE + NEG_DARK,
)

# ---------------- T10 ----------------
node(
 "M3.S6.T10", "M3.S6.T10.C12",
 "ચઢવાની હોડ",
 "સાંજે થાંભલા સાથે ટેકવેલી નિસરણીના પહેલા પગથિયે રાજાએ પગ મૂક્યો છે ને હાથ પાછળ કરીને સૌને હટાવે છે; ગુરુ, ચેલો ને આખું ટોળું હાથ ઊંચા કરીને ઊભાં છે.",
 "ચિત્ર બને ત્યાં સુધી હોડની આ ક્ષણ પર જ રહો — સૌ ચઢવા માગે છે — ને પછી પૂછો કે ગુરુની એક જ વાતથી આખા ગામનું મન કઈ રીતે ફરી ગયું.",
 ("Sunset on the open ground outside " + TOWN + ", long orange light and dust hanging in the air. The tall "
  "bare wooden post stands with a short wooden ladder leaning against it; nobody is on the post, nothing "
  "hangs from it and nothing gruesome is shown. " + KING + " He has jumped down from his platform and "
  "shoved to the front, his jewelled turban knocked askew, one foot planted on the bottom rung of the "
  "ladder and one arm thrown back to wave everybody else away, his face lit with triumphant greed. " +
  CHELA_FAT + " He stands just behind him with one hand up as if calling out to be allowed first. " +
  GURU + " He has his hand up too, being edged aside, a knowing glint in his eye. A crowd of townsfolk in "
  "white dhotis, cotton saris and folded turbans jostles behind them with hands raised, everyone wanting "
  "a turn. " + GUARDS + " The two guards steady the ladder, thoroughly bewildered. Clay-tile roofs and a "
  "stepped stone well stand dark against the low sun. " + STYLE +
  "અધિપતિ કહે, ‘‘ચઢીએ અમો, પૂરણ મળે પ્રતાપ.’’"),
 NEG_BASE + NEG_DARK,
)

tool = {
 "topic_id": "M3.S6.T10",
 "spec": (
   "Event-order strip (the one interactive of this chapter, and it is earned by the chapter's own printed "
   "ordering block, નીચેની પંક્તિઓ ઘટનાક્રમમાં ગોઠવીને ફરીથી લખો.). WHAT THE CHILD MANIPULATES: the seven "
   "verse lines that block prints appear as shuffled cards in a column on the left, each card showing one "
   "line in Gujarati script exactly as printed, identified by a small line-drawing icon — a fallen wall, a "
   "trowel, a hoe in wet mortar, a leather water bag, a walking figure, a raised palm at a bare post, a "
   "ladder — and never by a number. An empty vertical track runs down the right. The child drags a card "
   "into any slot on the track and may drag a placed card out again or swap two placed cards; nothing is "
   "typed. WHAT CHANGES WHEN THEY DO: the moment two neighbouring slots are both filled the strip draws a "
   "connecting arrow between them and colours it — green while that pair stands in the order the poem "
   "tells it, grey while it does not — so the chain of blame visibly builds or breaks link by link instead "
   "of being marked at the end. A card dropped where both its neighbours contradict it slides back to the "
   "left column with a soft shake. When every arrow on the track is green they join into one continuous "
   "line from the fallen wall to the ladder, and the strip replays the chain once from top to bottom, "
   "lighting each card in turn. Nothing is scored, no answer is ever revealed and the child may re-order "
   "as often as they like — the feedback is the colour of the arrows, not a verdict. On-screen Gujarati "
   "instruction, rendered exactly: પંક્તિઓને કાવ્યમાં જે ક્રમે બની તે ક્રમે ગોઠવો. The card text is the "
   "printed verse as the exercise page prints it and is never rewritten into modern Gujarati; the child's "
   "written answer to the block itself stays with the સ્વાધ્યાય deliverable."
 )
}

out = {
 "media": media,
 "2d_tool": tool,
 "reuse_report": {"scenes": 10, "reused": 0, "authored": 10, "rejected": []},
}

p = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch11/09_media.json"
with io.open(p, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("written", p, len(media))
