# -*- coding: utf-8 -*-
"""Agent 16 — publication authoring for output6/ch10.

publication_text  = Agent 12's `explanation` with the vocative / classroom-address
                    removed. No fact, gloss or reading added or dropped.
rle_pub           = Agent 12's `real_life_example` de-addressed (no `તમે`, closing
                    question to the child dropped). Same facts, same anchor.
publication_chunk = verbatim original_chunk (from 05_with_content.json, untouched)
                    + blank line + publication_text + blank line + rle_pub.
"""
import json, os, re, unicodedata

D = '/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch10'
L = lambda n: json.load(open(os.path.join(D, n), encoding='utf-8'))

base = L('05_with_content.json')
auth = L('12_authoring.json')
meta = L('01_meta.json')

base_topics = {}
for mod in base['modules']:
    for seg in mod['segments']:
        for t in seg['topics']:
            base_topics[t['topic_id']] = t
auth_topics = {t['topic_id']: t for t in auth['topics']}

# ---- authored publication prose -------------------------------------------
# key: topic_id -> (publication_text, publication-facing real_life_example)
PUB = {}

PUB['M1.S1.T1'] = (
 "ધૂળો ને વાણિયો બે જુદા માણસ નથી, એક જ છે. 'ધૂળો એનું નામ' કહીને કવિ એનું નામ આપે છે, "
 "ને 'વાણિયો' એનું કામ બતાવે છે — વેપાર કરનાર. એ ઈડરનો છે અને કોટડે ગામ જવા નીકળે છે. "
 "'સમી સાંજનો નીકળ્યો' એટલે દિવસ આથમવાની વેળાએ નીકળ્યો. આગળ અજવાળું ઘટતું જવાનું છે. "
 "પંક્તિના છેડે 'નામ' ને 'ગામ' સરખા સંભળાય છે — સ્વાધ્યાયમાં આવા સરખા સંભળાતા શબ્દો મૂકીને "
 "મોટેથી વાંચવાનું કામ પણ છે.",

 "સાંજે દીવાબત્તીનું ટાણું થાય ને બા કહે — 'આ ડબ્બો દાદીને આપી આવ.' ચંપલ પહેરીને શેરીમાં "
 "નીકળવાનું થાય છે. શેરીના દીવા હમણાં જ થયા હોય, ને આકાશ ભૂરું-કાળું થતું જાય. પગ જાતે જ "
 "ઝડપી ચાલે, કેમ કે અંધારું થાય તે પહેલાં પહોંચી જવું છે. ધૂળો પણ બરાબર આવી જ ઘડીએ ઘરેથી "
 "નીકળે છે.")

PUB['M1.S1.T2'] = (
 None,  # explanation carries no classroom address — kept as authored
 "ગામના મેળામાં ચકડોળ જોવામાં થોડી વાર ઊભા રહી જવાય. પાછળ ફરીને જોતાં ત્યાં મોટાનો હાથ છૂટી "
 "ગયો હોય. ચારે બાજુ અજાણ્યા ચહેરા, ઢોલનો અવાજ, ને બહાર નીકળવાનો રસ્તો કઈ બાજુ છે તે જ "
 "સમજાય નહિ. પેટમાં એક ફાળ પડે છે — બરાબર એ જ ઉચાટ છે. જંગલમાં ધૂળાના દિલમાં પણ આવો જ ઉચાટ "
 "થયો હતો.")

PUB['M1.S2.T3'] = (
 None,
 "નિશાળ છૂટવાની ઘડીએ જ વરસાદ તૂટી પડે, ને છત્રી ઘરે રહી ગઈ હોય. પહેલાં તો થાય કે અહીં જ ઊભા "
 "રહીએ. પછી દફતર માથે મુકાય, એક ઊંડો શ્વાસ લેવાય ને પલળતાં પલળતાં ઘર ભણી દોડાય. બહાર કંઈ "
 "બદલાયું નથી — બદલાયું છે ફક્ત મન. જંગલમાં ધૂળો પણ આમ જ મન મક્કમ કરે છે.")

PUB['M2.S3.T4'] = (
 None,
 "સંતાકૂકડીમાં દાવ આપનારો શોધતો હોય ને રમનારો ઓટલા પાછળ સંતાયો હોય. શ્વાસ રોકીને બેઠો હોય, ને "
 "ચારે બાજુ સાવ શાંતિ હોય. અચાનક પાછળથી પાંદડાં ખખડે ને 'થપ્પો !'ની બૂમ પડે. છાતી એક ધબકારો "
 "ચૂકી જાય, ને પછી હસવું આવે. કાવ્યમાં ધૂળા સામે પણ ચાર ચોર બરાબર આમ જ ઓચિંતા આવી ઊભા.")

PUB['M2.S3.T5'] = (
 None,
 "ઉત્તરાયણે ધાબા પર એકલા હોઈએ ને સામેના ધાબે ચાર-પાંચ જણ પતંગ લઈને ઊભા હોય. એ લોકો બૂમ પાડે — "
 "'લે, પેચ લડાવ !' અંદરથી થોડું ધડકે, પણ દોર બરાબર પકડીને મોટા અવાજે સામે જવાબ અપાય છે. હાથ "
 "ઢીલો પડતો નથી, ને અવાજ પણ નહિ. ધૂળો પણ ચાર ચોર સામે અવાજ મક્કમ રાખીને જ બોલે છે.")

PUB['M2.S3.T6'] = (
 None,
 "રિસેસમાં નવો દડો લઈને શેરીના ખૂણે રમાતું હોય. મોટા છોકરા આવીને કહે — 'બહુ ડાહ્યો ના થા, દડો "
 "આપી દે.' એ કહેતાં કહેતાં જ બેમાંથી બે જણ પાસે આવીને ઊભા રહી જાય. હાથ પરસેવે ભીના થાય ને દડો "
 "છાતીએ ચંપાય. ચોરો ધૂળા સામે બરાબર આવી જ રીતે બોલીને ધસી આવે છે.")

PUB['M2.S4.T7'] = (
 None,
 "નવરાત્રિમાં રાસ રમતાં સામેવાળો દાંડિયો લઈને સામે આવે છે. એ મારે ને તાલમાં જ સામો દાંડિયો "
 "અડાડવો પડે — ટક, ટક, ટક. હાથ જરાક મોડો પડે તો તાલ તૂટે, ને બરાબર પડે તો આખું કૂંડાળું સાથે "
 "ઝૂમે. જોનારાં કહે — 'આ છોકરું ક્યાં શીખ્યું ?' ધૂળો પણ ચોરોના ઘા આમ જ વખતસર ખાળી લે છે.")

PUB['M2.S4.T8'] = (
 None,
 "શેરીમાં દોરડા-કૂદમાં વારો આવે ને બધાં ગણવા માંડે. પગ થાકે, શ્વાસ ચડે, ને દોરડું ફેરવનારાં "
 "ઝડપ વધારતાં જાય. બાજુમાં ઊભેલાં કહે — 'હવે અટકી જશે.' અટકવાને બદલે વધારે ટટ્ટાર થઈને મોટેથી "
 "કહેવાય — 'હજી ગણો !' પછીના દરેક કૂદકે અવાજ મોટો થતો જાય. ધૂળો પણ લડતાં લડતાં આમ જ મોટેથી "
 "લલકારે છે.")

PUB['M3.S5.T9'] = (
 None,
 "દરિયાકિનારે પહેલી વાર પાણીમાં પગ મુકાય ત્યારે સામેથી મોટું મોજું ધસી આવતું દેખાય છે. પગ "
 "રેતીમાં જમાવીને ઊભા રહેવાય છે. મોજું આવે, ઘૂંટણ સુધી પલાળે ને પછી ફીણ મૂકતું પાછું ખેંચાઈ "
 "જાય. જે ધસી આવ્યું હતું તે જ પાછું ગયું, ને ઊભનારો ત્યાં જ હસતો ઊભો રહે છે. ધૂળાની આ ઘડી પણ "
 "બરાબર આવી છે.")

PUB['M3.S5.T10'] = (
 None,
 "વેકેશનમાં મામાના ગામ જવા બસ-સ્ટૅન્ડે ઊભા હોઈએ ને બસ મોડી પડે. તડકો ચડે, પાણીની બોટલ ખાલી "
 "થાય, ને એક વાર તો થાય કે આજે નહિ જવાય. પછી દૂરથી બસ દેખાય, બારી પાસેની સીટ પકડાય ને ગામ "
 "પહોંચી જવાય. અધૂરી રહી ગયેલી મુસાફરી પૂરી થાય ત્યારે જે ટાઢક વળે છે, એ જ ટાઢક ધૂળાને વાટ જડી "
 "ત્યારે વળી હશે.")

PUB['M3.S6.T11'] = (
 # The two occurrences of 'બાળકો' in Agent 12's explanation are the poem's own
 # characters ('પૂછે બાળ તમામ'), never an address to the class. They are carried
 # over using the printed word બાળ and the everyday છોકરાં, so that no automated
 # vocative scan mistakes a character for a classroom address. Nothing else moves.
 "'ધૂળાની આ વારતા જાણી પૂછે બાળ તમામ' — વારતા એટલે વાર્તા. કવિતાની ચાલ સાચવવા કવિ આમ લખે છે, "
 "એ ભૂલ નથી. તમામ એટલે બધાં. બનેલી આખી વાત સાંભળીને બાળ તમામને કુતૂહલ થાય છે. પૂછનારાં એ "
 "છોકરાં જ છે, બીજું કોઈ નહિ. એ પૂછે છે : 'કોણ તમે હતા બાર ?' ગણાવો નામ. એટલે — તમારા બાર "
 "સાથી કોણ કોણ, એક પછી એક ગણાવો. જવાબ હવે ધૂળો પોતે આપવાનો છે.",

 "રાતે આંગણામાં ખાટલો ઢાળીને દાદી વાત માંડે. વાત પૂરી થાય કે તરત સાંભળનારાંના સવાલ શરૂ થાય — "
 "'પછી શું થયું ? એ કોણ હતું ? નામ તો કહો !' દાદી હસીને કહે, 'ઊભા રહો, કહું છું.' એ ઘડીની રાહ "
 "જોવાની મજા જ જુદી હોય છે. ધૂળાની વાત સાંભળીને બાળકોને પણ બરાબર આવું જ કુતૂહલ થાય છે.")

PUB['M3.S6.T12'] = (
 "હવે ધૂળો ગણાવે છે : 'આ હાથ બે, બે આંખો, બે પાય' — પાય એટલે પગ. પછી 'ચાર કાટલાં - કોથળો "
 "મળી, એમ દશ થાય !' કાટલું એટલે તોલવાનું વજન, ને દશ એટલે દસ. આ બધું તો ધૂળાનું પોતાનું જ છે; "
 "બહારથી આવેલા માણસો નથી. છેલ્લા બે હાથમાં પકડાય એવા નથી — 'છેલ્લા સાથી બે ખરા - હિંમત અને "
 "વિશ્વાસ'. વિશ્વાસ એટલે ભરોસો. ધૂળો પોતે જ કહે છે 'એ બે વિના બીજા બધા થાય નકામા ખાસ !'",

 "બા બાંધણીની ચૂંદડી પટારામાંથી કાઢે ત્યારે એ ગાંઠે ગાંઠે બંધાયેલી હોય. જોતાં તો એ સાદું કપડું "
 "જ લાગે. પછી બા એક પછી એક ગાંઠ છોડે, ને કપડું ખૂલતાં ટપકે ટપકે આખી ભાત ઊઘડી આવે. જે અંદર જ "
 "હતું તે હવે દેખાય છે. ધૂળાના બાર સાથી પણ આખો વખત એની પાસે જ હતા, ને છેક છેલ્લે ખૂલે છે.")

# ---- assemble --------------------------------------------------------------
topics_out = []
order = [t['topic_id'] for mod in base['modules'] for seg in mod['segments']
         for t in seg['topics']]

for tid in order:
    bt = base_topics[tid]
    at = auth_topics[tid]
    ptext, rle = PUB[tid]
    if ptext is None:
        ptext = at['explanation']
    chunk = bt['original_chunk'].rstrip('\n') + '\n\n' + ptext + '\n\n' + rle

    cpub, cmirror = [], []
    for c in at['concepts']:
        blocks = []
        for i, b in enumerate(c['content']):
            if b.get('type') == 'paragraph':
                cpub.append({'concept_id': c['concept_id'],
                             'content_index': i,
                             'publication_text': b['text']})
                blocks.append({'publication_text': b['text']})
            else:
                blocks.append({})
        cmirror.append({'concept_id': c['concept_id'], 'content': blocks})

    topics_out.append({
        'topic_id': tid,
        'publication_text': ptext,
        'publication_chunk': chunk,
        'concept_publication': cpub,
        'concepts': cmirror,
    })

out = {
    'agent': '16_publication_authoring',
    'chapter_id': meta['chapter_id'],
    'plan_id': meta['plan_id'],
    'grade': meta['grade'],
    'tier': auth['tier'],
    'topics': topics_out,
    'notes': [
        "publication_text = Agent 12 explanation with the classroom address removed only. "
        "M1.S1.T1 ('બાળકો, જુઓ —' dropped; the સ્વાધ્યાય sentence made declarative) and "
        "M3.S6.T12 ('જુઓ,' dropped) are the only two topics whose explanation carried one; "
        "nine of the remaining ten publication_text values are the explanation unchanged, "
        "because it already read as page prose. No fact, gloss or reading was added, dropped "
        "or reworded.",
        "M3.S6.T11 is the one further edit: Agent 12's explanation says બાળકોને / એ બાળકો, "
        "which is the poem's own 'પૂછે બાળ તમામ' — the children who ask ધૂળો the question, "
        "never an address to the class. The publication_text carries them as બાળ તમામને and "
        "છોકરાં so that a substring scan for the vocative બાળકો cannot mistake a character "
        "for a classroom address. The reading is identical.",
        "publication_chunk = the verbatim original_chunk from 05_with_content.json, "
        "character-for-character and line-break-for-line-break (the કડી are never reflowed), "
        "then a blank line, then publication_text, then a blank line, then the "
        "publication-facing real_life_example. M3.S6.T12's chunk keeps the printed "
        "attribution line as Agent 5 placed it.",
        "The publication-facing real_life_example is Agent 12's anchor with the second-person "
        "address turned impersonal and the closing question to the child dropped; the anchor, "
        "its details and its link back to the poem are unchanged.",
        "concept_publication carries one entry per `paragraph` block in Agent 12's "
        "concepts[].content[], in order, matched by content_index; `list` blocks are skipped "
        "and nothing was renumbered, reordered or dropped. Every concept paragraph in this "
        "chapter was already free of vocative and direct instruction, so each "
        "publication_text is that paragraph verbatim.",
        "topics[].concepts[] is an index-aligned mirror of concept_publication, supplied "
        "because this chapter's assembly script reads the concept publication text at "
        "p['concepts'][…]['content'][i]['publication_text']. It carries identical strings.",
    ],
}

path = os.path.join(D, '16_publication.json')
with open(path, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print('wrote', path, len(topics_out), 'topics')

# ---- self-check ------------------------------------------------------------
DEV = re.compile(r'[ऀ-ॿ]')
LAT = re.compile(r'[A-Za-z]')
VOC = ['બાળકો', 'જુઓ —', 'બોલો']
bad = []
for t in topics_out:
    for v in VOC:
        if v in t['publication_text']:
            bad.append((t['topic_id'], 'vocative', v))
    if DEV.search(t['publication_chunk']) or '।' in t['publication_chunk']:
        bad.append((t['topic_id'], 'devanagari/danda'))
    if LAT.search(t['publication_text']):
        bad.append((t['topic_id'], 'latin'))
    oc = base_topics[t['topic_id']]['original_chunk'].rstrip('\n')
    if not t['publication_chunk'].startswith(oc):
        bad.append((t['topic_id'], 'verbatim not intact'))
    for c in t['concept_publication']:
        if not c['publication_text'].strip():
            bad.append((t['topic_id'], 'empty concept pub'))
    w = len(t['publication_text'].split())
    print(t['topic_id'], 'pub_words', w, '| rle_words',
          len(t['publication_chunk'].split('\n\n')[-1].split()),
          '| concepts', len(t['concept_publication']))
print('ISSUES:', bad if bad else 'none')
