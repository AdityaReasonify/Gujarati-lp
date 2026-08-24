# -*- coding: utf-8 -*-
import json, io, os

FLOCK = ("The same small flock appears: one bright green rose-ringed parakeet with a curved red beak, "
         "two small brown house sparrows with grey heads, one glossy black house crow with a grey collar, "
         "one red-vented bulbul with a small black crest, and one common myna with a yellow patch behind the eye.")

STYLE = "Soft digital watercolour, vibrant textbook illustration style, 16:9."

NEG = ("photorealistic faces, anime style, western-only setting, Roman script labels, "
       "Devanagari script labels, generic Bollywood styling, north-Indian-only architecture, watermark, "
       "blurry, cluttered background, anachronistic objects, motivational poster layout, "
       "text banner with a moral, slogan lettering, speech bubbles, birds wearing human clothes, "
       "cartoon mascot styling, numerals or digits in any script, multiple panels or collage, "
       "snow, pine forest, European songbirds")

p1 = ("Early morning in the open square of a village in central Gujarat. A broad neem tree stands at one side, "
      "and one long low branch of it reaches right across the picture. Behind the tree are low houses roofed with "
      "curved clay tiles, a raised stone platform running along one wall, and a tall whitewashed pillared "
      "bird-feeding tower with a small domed top and a round grain tray. Six birds are perched along that single "
      "branch, packed close together wing to wing in one row, all facing the same way, beaks open and calling. "
      + FLOCK + " High in the pale blue sky above the same branch two more birds of these kinds are flying with "
      "wings spread wide, and a third is gliding steeply back down towards the branch, so the eye travels up to the "
      "sky and back down to the branch. Warm low sunlight, a little dust in the air, a few small neem leaves drifting "
      "down. Along the bottom of the picture runs a plain cream narrator bar carrying one line of Gujarati script, "
      "lettered exactly: અમે સહુ એક જ ડાળનાં પંખી. " + STYLE)

p2 = ("A heavy monsoon shower over the edge of a pearl-millet field in Saurashtra. A single neem tree stands at the "
      "field's edge with one thick branch dipping under the rain; behind it rows of tall pearl millet bend and drip, "
      "a low round stone well has a rope and an iron bucket on its rim, and a wooden bullock cart is parked under a "
      "rusted tin awning. The birds have taken shelter along the branch. " + FLOCK + " In the middle of the branch the "
      "two sparrows are quarrelling beak to beak, wings flared and feathers raised; the parakeet has hopped right away "
      "to the thin far end of the branch and sits alone with its back turned; the crow, the bulbul and the myna sit "
      "pressed shoulder to shoulder under the leaves, dry and calm, watching the quarrel. Grey rain-streaked sky, "
      "silver lines of rain, puddles below with rings spreading in them. Along the bottom of the picture runs a plain "
      "cream narrator bar carrying one line of Gujarati script, lettered exactly: તોયે નિરંતર રહેતાં સંપી. " + STYLE)

p3 = ("Dawn on the green hill slopes of the Dang in southern Gujarat. In the foreground the ground dips into a wide "
      "shallow grassy hollow that curves open like a lap, wet with dew; mist lies in the folds of the valley below, "
      "small terraced finger-millet fields are cut into the far slope, a clump of tall bamboo leans in at one side, "
      "and a single empty woven bamboo basket rests beside a narrow footpath. Standing on the bare earth and grass of "
      "that hollow, in a loose ring, six birds sing together with beaks open and throats lifted. " + FLOCK + " Across "
      "the brightening sky above them a long strung-out line of the same kinds of birds flies steadily in one "
      "direction, wings beating together, clearly travelling somewhere. First gold light on wet grass, no people in "
      "the picture. Along the bottom of the picture runs a plain cream narrator bar carrying one line of Gujarati "
      "script, lettered exactly: જીવન કેરા પ્રવાસનાં સંગી. " + STYLE)

media = [
 {"topic_id":"M1.S1.T1","concept_id":"M1.S1.T1.C1","id":"M1.S1.T1.C1.IMG1","type":"image",
  "subtype":"illustration",
  "title":"એક જ ડાળ પર સૌ પંખી",
  "description":"ગામના ચોકમાં લીમડાની એક લાંબી ડાળ પર પાંખે પાંખ મળીને બેઠેલાં પંખી, ને ઉપર આભમાં ઊડતાં ને પાછાં નીચે આવતાં પંખી.",
  "image_url":"","aspect_ratio":"16:9","home_concept_id":"M1.S1.T1.C1","objective_id":None,
  "image_category":"illustration",
  "teaching_notes":"ચિત્ર બતાવીને પહેલાં ડાળ અને તેના પર બેઠેલાં પંખી ગણાવો — બોલનારાં આ પંખી પોતે છે તે અહીં જ ઠસાવો. પછી ઉપર ઊડતાં ને પાછાં નીચે આવતાં પંખી પર આંગળી મુકાવીને 'વિહરીએ કદી આભમાં ઊંચે' ને 'ઊડી-ઊડી કદી આવીએ નીચે' સાથે જોડો. નીચેની પટ્ટીની પંક્તિ આખા વર્ગ પાસે સાથે બોલાવો.",
  "negative_prompt":NEG,
  "generation_prompt":p1},
 {"topic_id":"M1.S1.T2","concept_id":"M1.S1.T2.C3","id":"M1.S1.T2.C3.IMG1","type":"image",
  "subtype":"illustration",
  "title":"ઝઘડો, ને તોયે સંગાથ",
  "description":"વરસાદમાં ડાળ પર બે ચકલી ચાંચે ચાંચ લડે છે, પોપટ છેડે જઈને એકલો બેઠો છે, ને બાકીનાં પંખી પાસે પાસે સાથે બેઠાં છે.",
  "image_url":"","aspect_ratio":"16:9","home_concept_id":"M1.S1.T2.C3","objective_id":None,
  "image_category":"illustration",
  "teaching_notes":"પહેલાં લડતાં પંખી અને છેડે એકલા બેઠેલા પંખી પર બાળકો પાસે આંગળી મુકાવો; પછી પાસે પાસે બેઠેલાં પંખી બતાવો. બંને વસ્તુ એક જ ડાળ પર દેખાય છે — 'તોયે' શબ્દ ક્યાં વળાંક લે છે તે વર્ગને પૂછો. ચિત્રમાં વરસાદ છે, એટલે સાથે રહેવાની વાત સહેલાઈથી પકડાય છે.",
  "negative_prompt":NEG,
  "generation_prompt":p2},
 {"topic_id":"M1.S2.T3","concept_id":"M1.S2.T3.C4","id":"M1.S2.T3.C4.IMG1","type":"image",
  "subtype":"illustration",
  "title":"ધરતીના ખોળે ગાન",
  "description":"ડુંગરના લીલા ખોળા જેવા ખાડામાં ઊભાં રહી ગાતાં પંખી, ને ઉપર આકાશમાં હારબંધ ઊડતાં સંગી પંખી.",
  "image_url":"","aspect_ratio":"16:9","home_concept_id":"M1.S2.T3.C4","objective_id":None,
  "image_category":"illustration",
  "teaching_notes":"ધરતીનો આ ખાડો ખોળા જેવો દેખાય છે — એ બતાવીને 'ધરતીને ખોળે' ચિત્ર છે, હકીકત નથી એમ સમજાવો. પછી ચાંચ ખોલીને ગાતાં પંખી પર અને ઉપર હારબંધ ઊડતાં પંખી પર નજર ફેરવાવીને 'સંગી' એટલે સાથી એ વાત વાળો. છેલ્લે આ કડી ચિત્ર સામે જોઈને વર્ગમાં ગવડાવો.",
  "negative_prompt":NEG,
  "generation_prompt":p3},
]

out = {
 "agent":"09_media_planning",
 "chapter_id":"gseb_eng_gujarati6_ch1",
 "plan_id":"gseb_eng_gujarati6_ch1_v1",
 "media":media,
 "2d_tool":None,
 "reuse_report":{"scenes":3,"reused":0,"authored":3,"rejected":[]},
 "notes":[
  "reuse step dormant: કોઈ ગુજરાતી frame pool નથી, એટલે ત્રણેય scene માટે image_url \"\" અને authored, self-contained generation_prompt લખ્યો છે. reused 0, authored 3, rejected [] — કશું score કર્યું નથી, હિન્દી/CBSE frame ઉધાર લીધો નથી.",
  "scenes = 3, 05_with_content.json માંથી ગણ્યા: M1.S1.T1, M1.S1.T2, M1.S2.T3 — ત્રણેયનું available_content_types ['image'] છે. કોઈ સ્વાધ્યાય બ્લોક, પ્રવેશક-પેટી, શબ્દાર્થ-પેટી કે અંતિમ 'અમે એક જ...' ચોકઠું media પામતું નથી (topic જ નથી).",
  "media id concept-scoped છે અને concept-અંક chapter-continuous છે: M1.S1.T1.C1.IMG1, M1.S1.T2.C3.IMG1, M1.S2.T3.C4.IMG1. M1.S1.T1 ને બે concepts (C1, C2) છે પણ એક જ scene = એક જ image, એટલે frame topic ના પહેલા concept C1 પર મૂક્યો છે; ચિત્ર બંને concepts ને પહોંચે છે — ડાળ પરનું 'અમે સહુ' (C1) અને ઊંચે-નીચેની ઉડાન (C2). C2 ને બીજું image આપ્યું નથી (એક scene, એક image).",
  "2d_tool null: નવ પંક્તિના ગેય બાળગીતમાં બાળક ચલાવી શકે એવી કોઈ સ્તર-બદ્ધ પ્રક્રિયા કે માર્ગ છપાયો નથી. બદલાય શું તે કહી ન શકાય, એટલે એ image છે, tool નથી.",
  "ઊર્મિકાવ્ય-ગીતનો media prior પળાયો છે — દરેક frame એ કડીનું પોતાનું ચિત્ર છે, બોધનું નહિ: પહેલી કડીની ડાળ ને ઉડાનનો ફેરો, બીજી કડીનો ઝઘડો ને છતાં પાસે બેઠેલાં પંખી, ત્રીજી કડીનો ધરતીનો ખોળો ને હારબંધ ઊડતા સંગી. કોઈ frame બીજા frame ને આગળ ચલાવતો નથી અને એકેયમાં બોધ લખાયો નથી.",
  "anchoring test: દરેક prompt એ જ topic ના original_chunk ના શબ્દો પરથી ચીતરાયો છે — ડાળ/પંખી/આભ/ઊંચે/નીચે (T1), લડીએ-વઢીએ/જુદાં/સાથે (T2), ધરતી-ખોળે/ગાન/પ્રવાસ-સંગી (T3). પાના પર ન છપાયું હોય એવું કશું ઉમેર્યું નથી; કવિનું ચિત્ર, નામ કે જીવન-વિગત કોઈ frame માં નથી.",
  "ટેકનું શૉર્ટહૅન્ડ '- એક જ.' કોઈ પણ narrator bar માં નથી; narrator bar માં કાવ્યના પાના પરની આખી પંક્તિ જ છે — 'અમે સહુ એક જ ડાળનાં પંખી.', 'તોયે નિરંતર રહેતાં સંપી.', 'જીવન કેરા પ્રવાસનાં સંગી.' — જેમ છપાઈ છે તેમ, 'કેરા' સહિત. સ્વાધ્યાયના શબ્દ-બદલી બ્લોકનું જુદું રૂપ ક્યાંય વાપર્યું નથી.",
  "Gujarati anchoring અને spread: ત્રણ frames ત્રણ જુદા પ્રદેશ લે છે — મધ્ય ગુજરાતનો ગામ-ચોક (નળિયાંવાળાં છાપરાં, ઓટલો, ચબૂતરો), સૌરાષ્ટ્રનું બાજરીનું ખેતર ચોમાસાના ઝાપટામાં (કૂવો, બળદગાડું, પતરાનું છાપરું), અને દક્ષિણ ગુજરાતના ડાંગના ડુંગર-ઢોળાવ (નાગલીનાં પગથિયાં-ખેતર, વાંસ, વાંસની ટોપલી). કોઈ frame માં માણસ કે પહેરવેશ ચીતર્યો નથી, એટલે કોઈ સમુદાયને પોશાક બનાવી દેવાનું જોખમ જ ઊભું થતું નથી.",
  "પંખીની ઓળખ ત્રણેય prompt માં એક જ વાક્યથી સ્થિર રાખી છે (પોપટ, બે ચકલી, કાગડો, બુલબુલ, મેના) — 'આગળના ચિત્ર જેવું' એવો ઉલ્લેખ ક્યાંય નથી, કારણ કે image model પાસે બીજું કશું context નથી.",
  "negative_prompt માં ફરજિયાત યાદી ઉપરાંત આ સ્વરૂપની પોતાની ના ઉમેરી છે — motivational poster layout, text banner with a moral, slogan lettering, speech bubbles, birds wearing human clothes — અને અંક/ડિજિટ પણ નકાર્યા છે (display text માં અંક નહિ)."
 ]
}

path = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch01/09_media.json"
with io.open(path,"w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=1)
    f.write("\n")
print("written",path, os.path.getsize(path))
