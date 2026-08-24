# -*- coding: utf-8 -*-
import json, io, os

STYLE = "Soft digital watercolour, vibrant textbook illustration style, 16:9."

NEG_BASE = ("photorealistic faces, anime style, western-only setting, Roman script labels, "
            "Devanagari script labels, generic Bollywood styling, north-Indian-only architecture, "
            "watermark, blurry, cluttered background, anachronistic objects, motivational poster "
            "layout, text banner with a moral, devotional poster art, idol or deity figure, halo, "
            "temple calendar art, praying hands, any lettering other than the single Gujarati "
            "narrator line, numerals anywhere in the picture")


def bar(line):
    return ("At the very bottom of the picture a narrow horizontal narrator bar in a soft cream "
            "tone carries exactly this Gujarati line, lettered in clean Gujarati script and "
            "nothing else: " + line + " . There is no other writing anywhere in the image.")


media = []

# ---------------- M1.S1.T1.C1 ----------------
media.append({
    "topic_id": "M1.S1.T1",
    "concept_id": "M1.S1.T1.C1",
    "id": "M1.S1.T1.C1.IMG1",
    "type": "image",
    "subtype": "illustration",
    "title": "સૂરજ ઊગે ને સરોવર જાગે",
    "description": "નદીકિનારે વહેલી સવાર — પાણી પર ઊગતો સૂરજ, ઉપર આકાશમાં ઝાંખો રહી ગયેલો ચાંદો, પાછળ પહોળું સરોવર, ને ઘાટના પગથિયે ઊભાં રહીને જોતાં બાળક.",
    "image_url": "",
    "aspect_ratio": "16:9",
    "home_concept_id": "M1.S1.T1.C1",
    "objective_id": None,
    "image_category": "illustration",
    "teaching_notes": "ચિત્ર બતાવીને પહેલાં પુછો — 'આમાં શું શું દેખાય છે ?' — ને બાળકો પાસે નામ બોલાવો; સૂરજ, ચાંદો, નદી ને સરોવર ચારેય એમના મોઢેથી નીકળે પછી જ આરંભની પંક્તિઓ ગાઈને એ જ ચીજો પંક્તિમાં શોધાવો. ચિત્ર હજી બન્યું નથી ત્યાં સુધી આ જ દૃશ્ય શબ્દોમાં ધીમે ધીમે વર્ણવો અથવા વર્ગની બારીની બહાર જોવડાવીને પુછો કે અત્યારે આકાશમાં શું શું દેખાય છે.",
    "negative_prompt": NEG_BASE + ", temple or shrine, a god figure in the sky, sun drawn with a smiling face, boats crowded on the water",
    "generation_prompt": (
        "A wide riverside morning in central Gujarat, a few minutes after sunrise: a broad slow "
        "river fills the lower half of the frame, worn stone bathing steps of an old village "
        "landing descending into it, and beyond a low earth embankment a large open lake shines "
        "in the same light. The orange sun sits low over the water and its long reflection breaks "
        "into ripples; high in the same soft pink-and-blue sky a pale white crescent moon is still "
        "faintly visible. On the bank stand low houses roofed with curved clay tiles, a raised "
        "stone platform running along one wall, and a big neem tree; brass and steel water pots "
        "rest on one step. A girl of about eleven in a plain blue-and-white school uniform, a "
        "cloth bag on her shoulder, stands still on a middle step looking up at the sky with one "
        "hand shading her eyes; lower down an older woman in a plain cotton saree dips a pot. Two "
        "white egrets stand at the water's edge. The mood is calm, unhurried and full of quiet "
        "wonder; warm golden light with cool blue shadows. " + bar("સુંદર સરિતા ને સરોવર") + " " + STYLE),
})

# ---------------- M1.S2.T2.C2 ----------------
media.append({
    "topic_id": "M1.S2.T2",
    "concept_id": "M1.S2.T2.C2",
    "id": "M1.S2.T2.C2.IMG1",
    "type": "image",
    "subtype": "illustration",
    "title": "પરોઢે ઝાકળભીનું વન ને ડુંગર",
    "description": "ડુંગરની ધારે પરોઢ ફૂટે છે — નીચે ધુમ્મસમાં ડૂબેલું ગાઢ વન, ઘરના આંગણે ફૂલોનો નાનો ક્યારો, ને આકાશના ઉપલા ખૂણે રાતના છેલ્લા બે તારા હજી ઝાંખા દેખાય છે.",
    "image_url": "",
    "aspect_ratio": "16:9",
    "home_concept_id": "M1.S2.T2.C2",
    "objective_id": None,
    "image_category": "illustration",
    "teaching_notes": "ચિત્રમાં એક બાજુ હજી રાત બાકી છે ને બીજી બાજુ સવાર ફૂટે છે — બાળકોને એ બે ભાગ આંગળી મૂકીને બતાવવા કહો, પછી કડીની પહેલી પંક્તિ ગાઓ એટલે સામસામી જોડી જાતે સમજાશે. વન ને ક્યારો પણ સામસામે બતાવો: એક જાતે ઊગેલું, બીજું કોઈએ વાવેલું. ચિત્ર બન્યું ન હોય ત્યાં સુધી બાળકોને પુછો કે એ પોતે વહેલી સવારે ઊઠ્યાં હોય ત્યારે બહાર શું શું દેખાય છે.",
    "negative_prompt": NEG_BASE + ", snow-capped Himalayan peaks, alpine conifers, pine forest, tourist viewpoint railing, tribal costume as decoration",
    "generation_prompt": (
        "First light in the forested hills of the Dang in southern Gujarat: white mist lies in the "
        "valley, dense teak and bamboo forest covers the slopes, and a tall dark ridge rises "
        "behind with the sky above it turning pink and gold; at the very top of the sky one or two "
        "last stars are still faintly visible in the fading dark blue. In the foreground, at the "
        "edge of a small hill village, a carefully tended patch of garden — marigolds, a tulsi "
        "plant in a clay pot on a low platform, a papaya tree, a hedge of stones — sits in front "
        "of a house with mud-plastered walls and a sloping roof of curved clay tiles. A boy of "
        "about eleven in a plain school uniform stands at the garden's edge holding a steel "
        "tumbler, looking out at the ridge; a hen and her chicks peck near his feet, thin smoke "
        "rises from one roof, dew beads on the leaves. Fresh, cool, expectant, very quiet. "
        + bar("સુંદર વન, ઉપવન, ગિરિવર") + " " + STYLE),
})

# ---------------- M1.S2.T3.C3 ----------------
media.append({
    "topic_id": "M1.S2.T3",
    "concept_id": "M1.S2.T3.C3",
    "id": "M1.S2.T3.C3.IMG1",
    "type": "image",
    "subtype": "illustration",
    "title": "તળાવમાં માછલી, ઉપર પંખી",
    "description": "ગામના તળાવનું છીછરું ચોખ્ખું પાણી — નીચે સરકતી નાની માછલીઓ, કિનારે એક પગે ઊભેલો બગલો, ને હવા એટલી ધીમી કે પાણી લગભગ અરીસા જેવું સપાટ છે.",
    "image_url": "",
    "aspect_ratio": "16:9",
    "home_concept_id": "M1.S2.T3.C3",
    "objective_id": None,
    "image_category": "illustration",
    "teaching_notes": "આ ચિત્રમાં પવન દેખાતો નથી, પણ વર્તાય છે — પાણી પરની ઝીણી લહેર ને બાળકના ઊડતા વાળ બતાવીને પુછો કે 'પવન ક્યાં દેખાય છે ?' પછી કડી ગાઓ, એટલે માછલી–પંખી–ધરતી–સમીર ચારેય ચિત્રમાં જડશે. ચિત્ર બન્યું ન હોય ત્યાં સુધી બાળકોને આંખ મીંચીને વર્ગમાં આવતી ધીમી હવા અનુભવવા કહો.",
    "negative_prompt": NEG_BASE + ", fishing net, caught or dead fish, caged bird, aquarium, stormy water, plastic litter",
    "generation_prompt": (
        "A still village pond in north Gujarat in mid-morning: at the near edge the shallow water "
        "is clear enough to see three or four small silver fish gliding over a sandy bottom, and "
        "the surface beyond is almost mirror-flat with only the faintest ripple crossing it. A "
        "white egret stands on one leg in the shallows and a small blue kingfisher waits on a low "
        "branch; a few birds cross the pale warm sky. The pond is edged with cut stone steps; "
        "behind it stand low houses with curved clay-tile roofs, a tall carved wooden bird-feeder "
        "tower on a pillar with its little house-shaped top full of pigeons, a thorny babul tree, "
        "and a bullock cart resting under a tin awning. Two children of about eleven in plain "
        "school uniforms crouch at the water's edge, one pointing down at the fish, their hair "
        "just lifted by the slow warm breeze. Peaceful, bright, unhurried. "
        + bar("સુંદર ધરતી, શાંત સમીર") + " " + STYLE),
})

# ---------------- M2.S3.T4.C4 ----------------
media.append({
    "topic_id": "M2.S3.T4",
    "concept_id": "M2.S3.T4.C4",
    "id": "M2.S3.T4.C4.IMG1",
    "type": "image",
    "subtype": "illustration",
    "title": "ધાબા પરથી દેખાતું આખું આભ",
    "description": "રાતે ધાબા પર ખાટલા ઢાળીને પડેલાં બાળકો ઉપર તારાથી ભરેલું પહોળું આભ પથરાયેલું છે, ને એની સામે ધાબું ને માણસો સાવ નાનાં લાગે છે.",
    "image_url": "",
    "aspect_ratio": "16:9",
    "home_concept_id": "M2.S3.T4.C4",
    "objective_id": None,
    "image_category": "illustration",
    "teaching_notes": "ચિત્રમાં આભ કેટલી જગ્યા રોકે છે ને માણસ કેટલી — એ સરખાવવા કહો; મોટા આભ સામે નાનું લાગવું એ જ આ કડીની ખરી લાગણી છે. પછી પુછો કે ચિત્રમાં જે દેખાય છે તે તો તારા ને આભ છે, પણ કવિ એની સાથે બીજું શું શું સુંદર કહે છે ? ચિત્ર બન્યું ન હોય ત્યાં સુધી બાળકોને ઘેર જઈ રાતે એક વાર આકાશ સામે જોઈને આવવાનું કહો.",
    "negative_prompt": NEG_BASE + ", telescope, planets or rings, spaceship, rocket, cartoon constellation lines, city skyline with neon, full moon washing out the stars",
    "generation_prompt": (
        "Night on the flat rooftop terrace of a small town house in Kutch, western Gujarat: most "
        "of the frame is an enormous deep indigo sky crowded with stars, with the faint pale band "
        "of the Milky Way arching across it. Below, along the bottom, a low whitewashed parapet, "
        "two woven rope cots with thin quilts, a clay water pot with a steel tumbler on its lid, "
        "and a small overhead water tank. A girl of about eleven lies on her back on one cot with "
        "her arms behind her head; a boy sits up beside her pointing straight up; a grandmother in "
        "a plain cotton saree sits on the parapet edge with a shawl. Flat rooftops and one or two "
        "tin-sheet roofs stretch away into the dark, a single dim yellow bulb over a distant "
        "doorway, no other lights. Vast, hushed, full of wonder, the people small against the sky. "
        + bar("સુંદર તારા, આભ વિશાળ") + " " + STYLE),
})

# ---------------- M2.S3.T5.C5 ----------------
media.append({
    "topic_id": "M2.S3.T5",
    "concept_id": "M2.S3.T5.C5",
    "id": "M2.S3.T5.C5.IMG1",
    "type": "image",
    "subtype": "illustration",
    "title": "આખો વર્ગ સાથે ગાય છે",
    "description": "વર્ગખંડમાં બાળકો પોતાની પાટલી પાસે ઊભાં થઈને એકસાથે ગીત ગાય છે — મોં ખૂલેલાં, ચહેરા ખીલેલા, ને શિક્ષક હાથથી તાલ આપે છે.",
    "image_url": "",
    "aspect_ratio": "16:9",
    "home_concept_id": "M2.S3.T5.C5",
    "objective_id": None,
    "image_category": "illustration",
    "teaching_notes": "આ ચિત્ર છેલ્લી કડી માટે છે, એટલે એને વર્ગમાં ખરેખર ઊભા થઈને ગાવાની ક્ષણ સાથે જોડો — ચિત્ર બતાવો, પછી બધાં ઊભાં થઈને એ જ રીતે ગાય. ગાયા પછી પુછો કે ચિત્રમાં કેટલા ચહેરા જુદા જુદા દેખાય છે; કવિ છેલ્લે માણસ પર આવીને અટકે છે એ વાત આ ચહેરાઓમાંથી જ કઢાવો, બહારથી ન કહો.",
    "negative_prompt": NEG_BASE + ", writing or diagrams on the blackboard, exam or test scene, flag or political imagery, uniformed rows standing at attention, portrait of a leader on the wall",
    "generation_prompt": (
        "A government primary school classroom in a Gujarati town, late morning: about a dozen "
        "children of eleven or twelve in plain blue-and-white uniforms stand at their worn wooden "
        "benches singing together — mouths open mid-word, faces bright, three of them clapping the "
        "beat, one small boy up on his toes, a girl at the back with her head tilted back. A young "
        "teacher in a simple cotton saree stands at the front keeping time with one raised hand. "
        "The dark green blackboard behind her has been wiped completely clean and is empty, with a "
        "wooden duster and a piece of chalk on its ledge. A barred window on the left shows a neem "
        "tree outside and throws warm stripes of sunlight across the stone floor; cloth school bags "
        "hang on wall hooks; a steel water pot with a tumbler stands by the door. Warm, alive, "
        "everyone together in one sound. " + bar("સુંદર હૈયું ને માનવ") + " " + STYLE),
})

out = {
    "media": media,
    "2d_tool": None,
    "reuse_report": {"scenes": 5, "reused": 0, "authored": 5, "rejected": []},
}

path = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch01/09_media.json"
with io.open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", path, os.path.getsize(path))
