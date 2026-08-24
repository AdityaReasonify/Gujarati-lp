# -*- coding: utf-8 -*-
import json, os

BAKO = ("Bako is a slim eleven-year-old Gujarati village boy with short cropped black hair, "
        "a round open face, a bright yellow-green half-sleeved t-shirt, purple knee-length shorts "
        "and bare feet.")
STYLE = "Soft digital watercolour, vibrant textbook illustration style, 16:9."

NEG_BASE = ("photorealistic faces, anime style, western-only setting, Roman script labels, "
            "Devanagari script labels, generic Bollywood styling, north-Indian-only architecture, "
            "watermark, blurry, cluttered background, anachronistic objects")
NEG_STORY = ("comic-strip panels, several moments shown in one frame, speech bubbles, "
             "motivational poster layout, text banner with a moral, caption lettering other than "
             "the narrator bar")

def bar(s):
    return ('A narrow cream narrator bar runs across the bottom of the frame carrying exactly this '
            'one line of Gujarati script and no other lettering anywhere in the picture: "%s". ' % s)

media = []

def add(topic_id, concept_id, title, description, teaching_notes, prompt, neg_extra):
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
        "negative_prompt": NEG_BASE + ", " + neg_extra,
        "generation_prompt": prompt,
    })

# ---------------- M1.S1.T1.C1 ----------------
add(
 "M1.S1.T1", "M1.S1.T1.C1",
 "નદીકાંઠે પગ ઝબોળતો બકો",
 "શાળાએથી પાછા વળતાં નદીકાંઠાની રેતમાં બેસી બંને પગ વહેતા પાણીમાં બોળીને નદી જોઈ રહેલો છોકરો, ને સામે કાંઠે નળિયાંવાળાં ઘરવાળું ગામ.",
 "શિક્ષક માટે : ચિત્ર બતાવીને પહેલાં નામ ઓળખાવો — આ છોકરાનું નામ બકો, ને આ નદીનું નામ કનક. પછી પૂછો કે છોકરો રોજ અહીં કેમ થોભતો હશે; બાળકો 'નદીની જબરી પ્રીત' જાતે બોલે ત્યાં અટકીને પાઠની પહેલી લીટીઓ સાથે સરખાવો.",
 ("A shallow clear river curving past the edge of a small inland Gujarati village on a warm "
  "late afternoon. On the far bank stand low whitewashed houses roofed with curved terracotta "
  "clay tiles, a raised stone platform running along one wall, a brass water pot left on it, and "
  "low scrub hills far behind where the river comes from. A thorny babul tree with tiny yellow "
  "puffs leans over the near bank; the near bank itself is pale river sand with tufts of grass. "
  + BAKO + " He sits on the sandy edge with both feet dipped in the running water, a plain cloth "
  "school bag lying flat beside him, his head tilted, watching the ripples with an open trusting "
  "smile. Sunlight glints on the moving water. "
  + bar("બકાને નદીની જબરી પ્રીત.") + STYLE),
 NEG_STORY),

# ---------------- M1.S1.T2.C2 ----------------
add(
 "M1.S1.T2", "M1.S1.T2.C2",
 "પગની પીડા ને આંખમાં આંસુ",
 "નદીકાંઠે બેસી એક પગ બંને હાથે પકડીને પીડાથી મોઢું બગાડતો છોકરો, ગાલ પર આંસુ, ને પાસે વહેતું પાણી.",
 "શિક્ષક માટે : ચિત્રમાં કાંટો દેખાતો નથી — એ જ ઠીક છે, કારણ કે પાઠ પણ કાંટો કેવો હતો એ કહેતો નથી. બાળકોને પૂછો કે છોકરાનું ધ્યાન ક્યાં હતું ને પગ નીચે કેમ ન જોવાયું; પછી 'ટાઢક થઈ, પણ પીડા ન ગઈ' — એ 'પણ' પર ભાર મૂકીને વંચાવો.",
 ("Late afternoon on the sandy bank of a shallow village river in inland Gujarat, the water "
  "running clear over pebbles, a thorny babul tree behind and low clay-tiled village roofs small "
  "in the distance. " + BAKO + " He sits doubled forward on the wet sand at the water's edge, "
  "his left foot still resting in the shallow water, his right foot lifted and gripped in both "
  "hands, face screwed up in pain with eyebrows pulled together, one bright tear on his cheek, "
  "his cloth school bag dropped beside him. No plant, branch or object touches the foot; the hurt "
  "is shown only in his face and his grip. Warm, gentle light, tender mood, sympathetic not comic. "
  + bar("થોડીક ટાઢક થઈ, પણ પીડા ન ગઈ.") + STYLE),
 NEG_STORY + ", visible thorn or spike, blood, wound close-up, exaggerated crying face"),

# ---------------- M1.S2.T3.C3 ----------------
add(
 "M1.S2.T3", "M1.S2.T3.C3",
 "બાવળની ડાળે બંધાયેલી માછલી છૂટે છે",
 "પંજા ઊંચા કરીને બાવળની ડાળ પર દોરીથી બંધાયેલી સોનેરી-રૂપેરી માછલીની ગાંઠ હળવે હાથે છોડતો છોકરો.",
 "શિક્ષક માટે : ચિત્ર બતાવીને પૂછો — આ અવાજ બીજા કોઈને કેમ ન સંભળાયો ? પાઠનું વાક્ય 'કદી જૂઠું બોલી ન હોય એવી વ્યક્તિ જ એનો અવાજ સાંભળી શકે' ફરી વંચાવો ને એમાંના 'જ' પર આંગળી મુકાવો. કોણે માછલી બાંધી હતી એ પાઠ કહેતો નથી, એટલે એ પ્રશ્ન ખુલ્લો જ રહેવા દો.",
 ("The sandy bank of a shallow village river in inland Gujarat at golden hour. A thorny babul "
  "tree leans over the water; from one low branch a small fish with gold-and-silver scales hangs "
  "tied by a thin twisted cord, its tail curling, its eye turned towards the boy. " + BAKO +
  " He stands on tiptoe on the sand, both arms stretched up, fingertips working gently at the "
  "knot of the cord, his face careful and concentrated, tongue just showing at the corner of his "
  "mouth. A faint warm shimmer of light has begun around the fish's scales. Behind him the river "
  "runs clear and low clay-tiled village roofs sit small on the far bank. Wonder-struck, quiet mood. "
  + bar("બકા ! મને છોડાવ ને !") + STYLE),
 NEG_STORY + ", fishing rod, net, hook, cruelty, dead fish, aquarium"),

# ---------------- M1.S2.T4.C4 ----------------
add(
 "M1.S2.T4", "M1.S2.T4.C4",
 "પરી વિદ્યા શિખવાડે છે",
 "નદીકાંઠાની રેતમાં પરી ઘૂંટણિયે બેસીને છોકરાને એક ચમત્કારી વિદ્યા શિખવાડે છે, ને છોકરો ધ્યાનથી સાંભળે છે.",
 "શિક્ષક માટે : ચિત્ર બતાવીને પહેલાં 'વિદ્યા' શબ્દ ચોખ્ખો કરો — અહીં એનો અર્થ ભણતર નહિ, પણ શીખવા મળેલી જાદુઈ કળા. પછી પાઠમાંથી વિદ્યાનો નિયમ પોતાના શબ્દોમાં કહેવડાવો. વિદ્યા ક્યાં વપરાશે એ હજી ન કહો — એ આગળની ઘટનાઓમાં આવે છે.",
 ("Evening light on the sandy bank of a shallow village river in inland Gujarat, a thorny babul "
  "tree behind, the water catching the last orange light, low clay-tiled village roofs small on "
  "the far bank. A slender young fairy kneels on the sand facing the boy: she has a long black "
  "braid, small translucent wings, and wears a pale-gold and silver Gujarati chaniya-choli with a "
  "light gauzy odhani, her outline faintly luminous as if she is made partly of light. She holds "
  "one hand raised with the index finger lifted, teaching, her face warm and pleased. " + BAKO +
  " He sits cross-legged on the sand a step away, both healed feet flat and easy, leaning "
  "forward, listening with wide attentive eyes and slightly parted lips. Soft golden sparks drift "
  "in the air between them. Gentle, magical, entirely human-scaled mood. "
  + bar("એ વિદ્યા ચમત્કારી હતી.") + STYLE),
 NEG_STORY + ", deity iconography, halo, temple or shrine, idol, devotional poster art, "
 "western fairy-tale castle, glitter-toy doll styling"),

# ---------------- M2.S3.T5.C6 ----------------
add(
 "M2.S3.T5", "M2.S3.T5.C6",
 "અધ્ધર પગે થંભેલું બગલું",
 "છીછરા પાણીમાં એક પગ ને ચાંચ અધ્ધર રાખીને જડ થઈ ગયેલું સફેદ બગલું, નાસી છૂટતું નાનું માછલું, ને કાંઠેથી આંગળી ચીંધીને બોલતો છોકરો.",
 "શિક્ષક માટે : ચિત્રમાં બગલું ખરાબ પક્ષી નથી — એ તો એનું કામ કરતું હતું. બાળકોને પૂછો કે છોકરાએ કેમ બોલવું પડ્યું, ને જવાબમાં 'એને માછલીની દયા આવી' પાઠમાંથી શોધાવો. 'અધ્ધર' શબ્દ અહીં પહેલી વાર આવે છે — ચિત્ર સામે રાખીને એનો અર્થ પકડાવો.",
 ("The shallow edge of a village river in inland Gujarat, morning light, pale sand and reed "
  "tufts along the bank, a thorny babul tree at one side and low clay-tiled roofs far behind. A "
  "tall white egret stands in the shallow water utterly motionless in an impossible pose: one "
  "leg lifted clear of the surface, neck curved and long beak angled down at the water, every "
  "feather still, its eye wide as if caught mid-movement. Just below it a small silver fish darts "
  "away through the ripples towards deeper water. " + BAKO + " He stands on the grassy near bank, "
  "right arm thrown up with the index finger pointing straight at the bird, mouth open having "
  "just called out, his whole body leaning forward with delight and surprise. Water rings spread "
  "where the fish turned. Bright, playful, astonished mood. "
  + bar("માછલું બચીને નાસી ગયું.") + STYLE),
 NEG_STORY + ", bird shown as villain, injured or bleeding bird, hunting scene"),

# ---------------- M2.S3.T6.C7 ----------------
add(
 "M2.S3.T6", "M2.S3.T6.C7",
 "ફળિયામાં થંભી ગયેલો ભમરડાવાળો હાથ",
 "ફળિયામાં ભમરડો ફેંકવા જતો છોકરો હાથ અધ્ધર જ થંભી ગયો છે, દોરી હવામાં લટકે છે, ને આજુબાજુનાં બાળકો હસતાં જુએ છે.",
 "શિક્ષક માટે : 'જાળ' એટલે અહીં ભમરડા પર વીંટવાની દોરી — ચિત્રમાં એ ખાસ બતાવીને માછલી પકડવાની જાળ સાથેની ગૂંચ ઉકેલો. પછી પૂછો કે થંભી ગયેલા છોકરાને શું થયું હશે; એની મજાક ન થાય એનું ધ્યાન રાખો, પાઠ પોતે આ આખા પ્રસંગને 'ગમ્મત' કહે છે.",
 ("The open earthen courtyard of a Gujarati village house in the middle of the day: a low house "
  "behind roofed with curved terracotta clay tiles, a raised stone platform along its front wall, "
  "a hanging clay water pot in a rope sling, a wooden cot stood on its side, a tulsi pot in one "
  "corner and a stray hen pecking near the wall. In the centre a barefoot village boy of about "
  "eleven in a red half-sleeved shirt and blue shorts stands frozen exactly as he was: his right "
  "arm flung up and back in the middle of a throw, absolutely still, a wooden spinning top held "
  "in his fingers with its winding string trailing loose in the air, his face startled and close "
  "to tears, drawn with sympathy and never as mockery. " + BAKO + " He stands a few steps away "
  "with one hand still half-raised, looking a little alarmed at what he has done. Three other "
  "village children in ordinary cotton clothes crowd behind him, laughing and pointing, one "
  "clapping. Warm dusty light, lively mood. "
  + bar("ભોપાનો હાથ સ્થિર થઈ ગયો.") + STYLE),
 NEG_STORY + ", fishing net, bullying, humiliation, cruel laughter, caricatured crying face"),

# ---------------- M2.S4.T7.C9 ----------------
add(
 "M2.S4.T7", "M2.S4.T7.C9",
 "અધ્ધર તોળાયેલો વાઘ ને ના પાડતો હાથ",
 "જંગલની કોરે કૂદતાં જ હવામાં અધ્ધર થંભી ગયેલો વાઘ, સામે બંદૂક નીચી કરાવવા હાથ ઊંચો કરતો છોકરો, ને જોવા ઊમટેલાં ગામલોકો.",
 "શિક્ષક માટે : આ પાઠનો વળાંક છે. ચિત્રમાં બે વસ્તુ સાથે બતાવો — હવામાં થંભેલો વાઘ, ને છોકરાનો ખેડૂતો તરફ ઊંચો થયેલો હાથ. પૂછો કે વાઘ થંભી ગયા પછી છોકરાએ શું નક્કી કર્યું; જવાબમાં પાઠની લીટી 'બકાએ ખેડૂતોને બંદૂક ન વાપરવા દીધી' શોધાવો. વાઘને ખરાબ કહેવાની જરૂર નથી.",
 ("The scrubby edge of a forest beside a village in inland Gujarat, mid-morning: dry golden grass, "
  "thorny babul and teak scrub, a red-earth path, and low clay-tiled village houses visible across "
  "the fields on the right. A full-grown tiger hangs completely motionless in the air above the "
  "grass, caught in the middle of its leap with all four legs stretched, tail streaming behind, "
  "mouth open — suspended, touching nothing, clearly frozen rather than falling. " + BAKO +
  " He stands facing it in the foreground, his left hand raised flat and firm towards two young "
  "farmers who have reined in their horses just behind him; the farmers, in cotton shirts and "
  "dhotis with cloth turbans, are lowering their long guns at his signal, muzzles pointed to the "
  "ground. A crowd of villagers has come running along the path to look; two small children ride "
  "on their fathers' shoulders and reach out to touch the tiger's back and tail. Excitement mixed "
  "with wonder, nobody afraid. "
  + bar("બકાએ ખેડૂતોને બંદૂક ન વાપરવા દીધી.") + STYLE),
 NEG_STORY + ", gun being fired, muzzle flash, blood, wounded animal, hunting trophy, "
 "tiger drawn as a demon, roaring horror-movie framing"),

# ---------------- M2.S4.T8.C10 ----------------
add(
 "M2.S4.T8", "M2.S4.T8.C10",
 "ઉઘાડા પાંજરામાં જતો વાઘ",
 "જંગલની કોરે મુકાયેલા લોખંડના પાંજરાનો દરવાજો ઉઘાડો છે, વાઘ સીધો એમાં ચાલ્યો જાય છે, ને વનવિભાગના માણસો દૂર ઊભા જુએ છે.",
 "શિક્ષક માટે : બાળકોને લાગે છે કે 'છૂટડૂક' બોલતાં વાઘ છૂટીને ભાગી ગયો હશે. ચિત્ર સામે રાખીને ક્રમ ગોઠવાવો — દરવાજો ઉઘાડ્યો, માણસો દૂર ઊભા રહ્યા, પછી શબ્દ બોલાયો, ને વાઘ સીધો પાંજરામાં. પાંજરું ત્યાં કઈ રીતે પહોંચ્યું એ પાઠ કહેતો નથી, એટલે એ ઉમેરવું નહિ.",
 ("The scrubby edge of a forest beside a village in inland Gujarat, dry golden grass and thorny "
  "babul, red-earth ground, low clay-tiled village roofs far away across the fields. A large "
  "barred iron cage stands on the ground with its heavy door swung wide open. A full-grown tiger "
  "is walking calmly and directly into the open cage, its head and shoulders already inside, tail "
  "low, unhurried, as if drawn straight in. Several forest-department men in khaki-green uniforms "
  "and caps stand well back at a safe distance, watching, one holding the rope of the door. "
  + BAKO + " He stands to one side in the middle ground, one hand still lifted, having just "
  "spoken, his face steady and serious. Village people watch from further back along the path. "
  "Clear midday light, tense but calm mood, nobody attacking anyone. "
  + bar("વાઘ સીધો જ પાંજરામાં આવી ગયો.") + STYLE),
 NEG_STORY + ", tranquiliser dart, blood, whips, ropes around the animal, circus imagery, "
 "cruelty, zoo signage"),

# ---------------- M2.S5.T9.C11 ----------------
add(
 "M2.S5.T9", "M2.S5.T9.C11",
 "ગામને મળ્યું બોરનું પાણી",
 "ગામના ચોકમાં નવા બોરના હૅન્ડપંપમાંથી પાણી પડે છે, બેડાં ને ડોલ ભરાય છે, ને છોકરાં પાણીમાં હાથ ધરે છે.",
 "શિક્ષક માટે : પહેલાં 'બોર' શબ્દ ચોખ્ખો કરો — ખાવાનું બોર નહિ, પણ જમીનમાં ઊંડે ઉતારેલો સાંકડો કૂવો; ચિત્ર એ ભૂલ સીધી ઉકેલી આપશે. પછી પૂછો કે મળેલી રકમનું છોકરાએ શું કર્યું. ગામને પાણીની તકલીફ કેમ હતી એ પાઠમાં લખ્યું નથી, એટલે એનું કારણ ઉમેરવું નહિ.",
 ("The open chowk of a small inland Gujarati village in the bright morning: low houses roofed "
  "with curved terracotta clay tiles around the square, a raised stone platform along one wall, a "
  "neem tree throwing shade, a bullock cart parked under a tin awning and a millet field visible "
  "beyond the last house. In the centre a newly installed hand pump over a borewell stands on a "
  "fresh concrete platform; a clear rope of water is gushing from its spout into a round brass "
  "water pot. Village women in ordinary cotton saris are lining up their brass and steel water "
  "pots and buckets, one laughing as her pot overflows; two small children hold their hands under "
  "the falling water and a third drinks from cupped palms. " + BAKO + " He stands at the edge of "
  "the group, working the pump handle with both hands, grinning. Bright, joyful, ordinary-day mood. "
  + bar("બકાએ ગામમાં બોર કરાવી આપ્યો.") + STYLE),
 NEG_STORY + ", cracked parched earth, drought imagery, charity-appeal framing, NGO poster, "
 "donation cheque"),

out = {
  "media": media,
  "2d_tool": None,
  "reuse_report": {"scenes": 9, "reused": 0, "authored": 9, "rejected": []}
}

path = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch02/09_media.json"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", path, "media nodes:", len(media))
