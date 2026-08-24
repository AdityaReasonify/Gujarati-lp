# -*- coding: utf-8 -*-
import json, hashlib, os

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch09"
src = os.path.join(D, "02_structure.json")
sha = hashlib.sha256(open(src, "rb").read()).hexdigest()

validation = {
  "agent": "04_mapping_convergence",
  "chapter_id": "gseb_eng_gujarati6_ch9",
  "chapter_name": "ગરવી ગુજરાતનો ગરબો",
  "grade": 6,
  "level": "standard",
  "pass_number": 1,
  "status": "pass",
  "checks": {
    "genre_fidelity": {
      "pass": True,
      "genre": "માહિતીપ્રદ ગદ્ય",
      "active_genre_profiles": ["mahitiprad_gadya.md"],
      "explanation_unit_declared": "એક માહિતી-ખંડ",
      "explanation_unit_used": "એક માહિતી-ખંડ",
      "verse_units_in_00": {"kadi": 0, "duha": 0, "pad": 0, "tek_occurrences": 0, "ghatna": 0},
      "mahiti_khand_markers_in_00": 13,
      "topics": 13,
      "notes": [
        "01_meta.json declares explanation_unit 'એક માહિતી-ખંડ' and 02_structure.json cuts on exactly that unit. The marker list rebuilt from the 13 topics' source_markers is character-identical, in order, to the 13 [[માહિતી-ખંડ: …]] markers read from 00_chapter_normalized.md — 1:1, no marker merged, none swallowed, no topic invented without a marker. This also matches 01_meta.json.structure_inventory.mahiti_khand = 13.",
        "No verse units exist in this chapter — 0 [[કડી]] / [[દુહો]] / [[પદ]] / [[ટેક]] / [[ઘટના]] markers in 00_chapter_normalized.md, matching 01_meta.json.structure_inventory. The દુહો-not-merged, પદ-not-split and changed-words-ટેક rules are therefore vacuously satisfied, not waived.",
        "Not a mixed chapter: one profile, genre_confidence 'high'. The drop-the-frame test holds on the printed page — remove the નવરાત્રી evening and પૂર્વીદીદી's article and the whole payload still stands (ગરબો = છિદ્રો પાડેલો માટીનો ઘડો, ગર્ભદીપ → ગર્ભો → ગરબો, the ગરબો/ગરબી ભેદ, મંજીરાંનૃત્ય, હીંચનૃત્ય, ટિપ્પણીનૃત્ય). The blue પ્રવેશપેટી names a ભેદ to be delivered, and the સ્વાધ્યાય carries two of this profile's own diagnostic blocks — the identification block 'કૌંસમાં આપેલા શબ્દો જે વાક્યોને લાગુ પડતા હોય તેની સામે લખો.' and the loanword hunt 'આ પાઠમાં કેટલાક અંગ્રેજી ભાષાના શબ્દો વપરાયા છે…' — with no event-ordering block anywhere. A1's genre, lens (તથ્ય + પરંપરા + જિજ્ઞાસા) and guiding question all match mahitiprad_gadya.md.",
        "Avoid-1 (re-teaching the frame as a વાર્તા) holds structurally: no topic carries topic_category 'climax' (categories are introduction ×1, core ×10, transition ×1, resolution ×1); no topic_name, concept_name or objective_text turns on a character's choice or names a વળાંક; 01_meta.json.structure_inventory.ghatna = 0. topic_type is CONCEPT throughout and STORY_TELLING is deliberately unused.",
        "Avoid-2 (cutting by speaker turn) holds on both halves. Arithmetic: 13 topics < 38 quoted speaker turns counted in 00_chapter_normalized.md — strictly less, as the profile requires. Substantive: no boundary falls at a mere change of speaker. Three topics (M1.S2.T3, M2.S6.T11, M2.S6.T12) deliberately hold more than one speaker turn so that a question and its answer stay together, and પપ્પાનો long expository turn in M2.S5.T9 is not split at all.",
        "Avoid-3 (cutting by page or paragraph) holds: 29 printed paragraphs are carried by 13 topics, and every topic_name and concept_name names the fact, practice or ભેદ it teaches — the origin of folk dance, the pot with holes, the word's journey, the symbol, the ગરબો/ગરબી ભેદ, the book, three regional dances, the tool's name, the closing. None is 'the next part of the chapter'. The remaining field-level half of Avoid-3 (first sentence of each explanation) is Agent 12's and is not yet authored.",
        "Avoid-11 (માર્ગદર્શક લેખ order/addressee) is not applicable — this is the narrative-frame sub-form named by the profile for std-6 ch 9, not the how-to sub-form.",
        "Avoid-12 (figures_of_speech) is not yet checkable: original_chunk and figures_of_speech are Agent 5 / Agent 12 fields and are empty by design at this stage.",
        "The quoted garbo couplet in the last sentence ('કેસરિયો રંગ તને લાગ્યો અલ્યા, ગરબા ! કેસરિયો રંગ તને લાગ્યો રે લોલ !') is an in-prose quotation, not a separately printed કૃતિ — no કડી marker, no ટેક, no poet line. A2 correctly kept it inside M2.S7.T13.C17 rather than opening a POEM topic or declaring the chapter mixed. Verified against _renders/page-3.png."
      ]
    },
    "coverage": {
      "pass": True,
      "scenes": 13,
      "topics": 13,
      "concepts": 17,
      "exercise_blocks_in_inventory": 19,
      "exercise_blocks_cut_as_topics": 0,
      "notes": [
        "Every reading scene became a topic, in printed order: all 13 [[માહિતી-ખંડ: …]] markers appear exactly once across the 13 topics' source_markers, and the rebuilt sequence is character-identical to the file's, with no gaps and no reordering.",
        "The pre-reading opener is a topic: M1.S1.T1 'નવરાત્રીની રાત ને પૂર્વીદીદીનું આગમન', topic_category 'introduction'. This is the profile's own named case for this chapter — 'The frame's opening is a real માહિતી-ખંડ when it sets up why the facts are being told — પૂર્વીદીદી needing an article on Gujarat's folk dances (std-6 ch 9). Mark it topic_category: introduction.'",
        "The frame's closing is a topic: M2.S7.T13 'અધૂરી રહેલી વાત ને કેસરિયો રંગ', topic_category 'resolution'. A2 kept its topic_type as CONCEPT rather than REVIEW and argued it: no in-text wrap is printed — પપ્પા are called away, the telling is left unfinished with a promise, and everyone rises to sing. That is a frame closing, not a summary of the facts taught, so REVIEW (which emits as 'summary') would misdescribe it. This validator agrees; the resolution category carries the role, and the chapter genuinely has no printed wrap.",
        "No સ્વાધ્યાય block became a topic. All 19 verbatim_heading entries of 01_meta.json.exercise_inventory were cross-checked against all 13 topic_name values and all 13 source_markers / source_span plans: zero matches, and no [[સ્વાધ્યાય: …]] marker appears in any topic's source_markers. The 19 printed blocks in 00_chapter_normalized.md equal the 19 inventory entries and all belong to Agent 10. The string 'સ્વાધ્યાય' occurs in 02_structure.json only inside counts.non_text_markers_not_cut and two provenance notes — never in a topic.",
        "Printed apparatus is correctly excluded from the cut and is not a coverage gap: the blue teacher-addressed પ્રવેશપેટી (00 marks it 'વાચનદૃશ્ય નથી, સ્વાધ્યાય નથી'), the શબ્દાર્થ box on printed page 58, and the chapter-final green 'અલ્પવિરામ અને અવતરણચિહ્ન' grammar box. The [[લેખક-નામ]] slot holds only '- સંકલિત' — an attribution line, not a student-facing લેખક-પરિચય paragraph — so declining to make it a CONCEPT topic is correct for std 6.",
        "The single [[ચિત્ર: …]] marker on printed page 55 is page matter, not a reading scene, and correctly opens no topic ('Printed photographs … are page matter, not reading scenes'). Agent 9 may draw on it for M1.S1.T1.C1; સ્વાધ્યાય block fifteen asks the child to describe it.",
        "No topic covers text that no marker claims. Every source_span is quoted from inside a [[માહિતી-ખંડ]] stretch on printed pages 55–57, and no span reaches into the પ્રવેશપેટી, શબ્દાર્થ, સ્વાધ્યાય or વ્યાકરણ matter. The one pre-topic hook is declared and correct: the 'સાચે જ આજે તો ઘણું બધું જાણવા મળ્યું… પ્રાદેશિક લોકનૃત્યો પણ હશે જ ને ?' paragraph sits under the ગરબો/ગરબી marker in 00 but raises the regional-dance question, so it is carried to the NEXT topic (M2.S5.T8) per cutting rule — 'a pre-topic hook belongs to the NEXT topic'.",
        "Concept coverage: 17 concepts over 13 topics. Four topics carry two concepts each (M1.S1.T1, M2.S6.T11, M2.S6.T12, M2.S7.T13) and none carries a third, which is the profile's 'two concepts in one topic, never a third'."
      ]
    },
    "objectives": {
      "pass": True,
      "count": 13,
      "notes": [
        "Root objectives[] exists with O1–O13, all objective_id values unique. strand_to_objective_map covers every legacy_id L1–L13 exactly once, its targets are unique, and every target resolves to a registered objective_id. Single strand L / ભાષા અને સાહિત્ય, as Gujarati literature requires.",
        "Every home_topic_id resolves to a topic in this tree (M1.S1.T1 … M2.S7.T13) and all 17 anchor ids resolve to concepts in this tree; zero unresolved references. Every topic carries objective_ids, every one resolves to the registry, and every registered objective is pointed at by exactly one topic. Each concept's objective_id also resolves. All depends_on values resolve to topics in this tree.",
        "Objectives are text-grounded and chapter-specific — each names something printed only in this chapter (અંબેચોકની નવરાત્રી and પૂર્વીદીદીનો લેખ, નદીને કિનારે સંસ્કૃતિનું પારણું, શક્તિપૂજા, 'ગરબો કોરાવ્યો', ગર્ભદીપ → ગર્ભો → ગરબો, ઘડાનો ગર્ભ ને આદ્યશક્તિ, ગરબી એટલે લાકડાની માંડવડી, the book 'ગુજરાતનાં લોકનૃત્યો', નળકાંઠાના પઢારો, ગાગર-હીંચ, શ્રમહારી ને ચોરવાડ, ટિપ્પણી ને પ્રભાતિયું, પપ્પાનું વચન). None could be pasted into another chapter. All thirteen sit in the 12–30 Gujarati-word band (measured 17–21).",
        "The objectives serve the teaching_lens તથ્ય + પરંપરા + જિજ્ઞાસા and cover all three limbs of the guiding_question: where the word came from (O4, O5, O6), what separates a ગરબો from a ગરબી (O7), and how each region builds its own dance (O9, O10, O11, O12). Ten ask the child to find or explain a printed fact; the three Analyze objectives (O6, O7, O11) stay strictly inside what the text itself states.",
        "No craft label appears in any objective_text — no અલંકાર, છંદ, સમાસ or literary-form name — which is the std-6 ceiling. The objectives ask the child to find, tell, order and compare, never to name a device.",
        "Ids match reference/naming_conventions.md: modules M1–M2, segments S1–S7 and topics T1–T13 dotted and continuous with no restarts; concepts C1–C17 chapter-continuous in traversal order (so M2.S7.T13 legitimately carries C16 and C17 — the concept counter running ahead of the topic counter is the contract's rule, not a gap). bloom_level is capitalised (Remember / Understand / Analyze) as the phase-2 contract requires for objectives. No M1.S1.T1.P1-style objective code appears anywhere in the file, and no .SR{n} recall id. No digit appears in any module_name, segment_name, topic_name or concept_name.",
        "topic_type 'CONCEPT' is correct for an intermediate file: reference/phase2_contract.md reserves the closed server enum (instructional | summary | assessment) for the emitted plans and mandates the authored values POEM | STORY_TELLING | CONCEPT | REVIEW in Agents 02–13, mapped by Agents 14/15."
      ]
    }
  },
  "blocking": [],
  "owner": None,
  "notes": [
    "MEASURED CONFLICT WITH A PROFILE CLAUSE THAT NAMES THIS CHAPTER, RESOLVED IN FAVOUR OF THE PRINTED PAGE — recorded loudly for Agent 13. mahitiprad_gadya.md's Explanation-unit section says: 'A printed litany is ONE fact-cluster, not many topics… twelve topics of one word each is a cut error. The same holds for std-6 ch 9's list of regional dances.' A2 cut the regional dances into four topics (M2.S5.T9 મંજીરાંનૃત્ય, M2.S5.T10 હીંચનૃત્ય, M2.S6.T11 ટિપ્પણી as શ્રમહારી નૃત્ય, M2.S6.T12 the ટિપ્પણી tool and the all-night જમાવટ), surfaced the tension itself, and did not hide it. This validator does not treat it as a block, for a reason read off the render rather than argued: THIS CHAPTER PRINTS NO LITANY OF REGIONAL DANCES. Each dance gets developed running exposition — મંજીરાંનૃત્ય with પઢારો, નળકાંઠો and એકતારો/તબલાં/કાંસીજોડ/બગલિયું; હીંચ with ગાગર and ભાલ/કાઠિયાવાડ; ટિપ્પણી with ચોરવાડ, the meaning of શ્રમહારી, the tool's construction and ભજનથી પ્રભાતિયા સુધીની આખી રાત. The std-7 ch 4 case the clause generalises from is a genuine one-word list (બાર વરસાદ-શબ્દો); nothing of that shape exists here. The same profile's governing rule — 'One fact-cluster… per topic' and 'Where the prose walks a sequence, each stage is a topic' — orders exactly the cut A2 made, and merging the four would produce one overstuffed topic that no single image, no single objective and no per-topic recall ladder could serve. A1 independently reached the same reading on the rendered page and gave each its own [[માહિતી-ખંડ]] marker. The chapter-specific page evidence governs the general prior.",
    "Render opened, and why. This validator worked from 00_chapter_normalized.md, 01_meta.json and 02_structure.json for everything except one question the transcription cannot answer: whether the regional dances are PRINTED as a list (which would trigger the litany clause above) or as running paragraphs. That is a layout question, so exactly one PNG was opened — _renders/page-3.png (printed page 57). Finding: continuous dialogue paragraphs in body type, no bullets, no numbering, no tabular or enumerated setting anywhere; the dances are separated only by speaker paragraphs, and each carries several sentences of fact. The transcription in 00_chapter_normalized.md matches the render line for line over that page, including the closing couplet. The render was not re-generated, altered or deleted.",
    "Non-blocking, for Agent 12 — the two-form spellings A2 recorded are real and printed, and must survive: 'ટિપ્પણી નૃત્ય' and 'ટિપ્પણીનૃત્ય' both occur, and so do 'હલકા કંઠે' and 'હલકથી'. Confirmed on _renders/page-3.png. Agent 5 transcribes as printed; nobody normalises them.",
    "Non-blocking, id contract: topics carry objective_ids but not yet the mirrored inline learning_objectives[] copy the phase-2 contract requires (the same object plus image_examples: []). That mirror is Agent 12/14 work and is correctly absent from a structure-only file; flagged so it is not lost. When it is written, the two objective_text strings must stay identical character for character.",
    "Non-blocking, uneven topic length — the printed structure, not a bad cut: M1.S3.T5 is a single printed line (the whole word-journey is one sentence) while M2.S7.T13 runs seven short paragraphs of rapid dialogue. Agent 12 must not pad a short topic's explanation with anything from outside the chapter (Avoid-4).",
    "Non-blocking, sensitivity carried forward for Agents 8 and 12: નવરાત્રી, માતાજી, આદ્યશક્તિ and શક્તિપૂજા are living devotion and are taught as the chapter presents them, never as comparative religion. The પઢાર community is named in the printed text (M2.S5.T9) and must be named that way, never as a generic 'આદિવાસી' or 'tribal'. નળકાંઠો, ભાલપ્રદેશ, કાઠિયાવાડ, સૌરાષ્ટ્ર and ચોરવાડ પંથક are used as printed. The chapter's own statement that ગરબો is sung mostly by સ્ત્રીઓ and ગરબી only by પુરુષો (M1.S4.T7) is reported as the text reports it, with nothing added and no debate opened.",
    "Non-blocking, for Agent 9: the profile allows at most one 2d_tool per chapter and this chapter has no process chain that earns one — it is a fact-cluster chapter, not a walk-through. One image per માહિતી-ખંડ, each showing the practice being done, is the right media shape here.",
    "Context-routing note: the run context supplied no_hallucination_policy.md and global_content_rules.md, but this agent's spec also cites reference/loop_protocol.md, reference/explanation_unit_map.md, reference/phase2_contract.md, reference/naming_conventions.md and the active genre profile. All exist in the repository and were read in full from disk (profiles/genres/mahitiprad_gadya.md for the profile) rather than guessed at; nothing in this verdict rests on assumed contents. reference/explanation_unit_map.md was consulted only through the profile's own restatement of cutting rules 1–5, which the profile quotes verbatim.",
    "Ids are frozen from this verdict. 04_converged.json is a convergence record naming 02_structure.json and its sha256, not a copy of the structure payload — downstream agents read 02_structure.json for structure and 04_converged.json only to confirm convergence."
  ]
}

converged = {
  "converged": True,
  "source": "02_structure.json",
  "sha256": sha,
  "verdict": "pass",
  "notes": [
    "This is a convergence record, not a copy of the structure. Read 02_structure.json for the tree, the objectives registry and every id; read this file only to confirm that ids are frozen.",
    "Frozen at Agent 4 pass 1, no re-run needed: 2 modules, 7 segments, 13 topics, 17 concepts, 13 objectives (O1–O13, strand L).",
    "All 13 [[માહિતી-ખંડ: …]] markers of 00_chapter_normalized.md are covered in printed order, 1:1 with the 13 topics. None of the 19 સ્વાધ્યાય blocks became a topic.",
    "Genre માહિતીપ્રદ ગદ્ય, profile mahitiprad_gadya.md, explanation unit 'એક માહિતી-ખંડ', lens તથ્ય + પરંપરા + જિજ્ઞાસા — all as declared in 01_meta.json.",
    "One recorded deviation from a profile prior, resolved in favour of the printed page and carried in 04_validation.json: the four regional-dance topics. The chapter prints no litany of dances (verified on _renders/page-3.png), so the profile's litany clause does not bite. Agent 13 should carry this note, not re-open it.",
    "The inline learning_objectives[] mirror of each topic's objective_ids is still owed by Agent 12/14; its absence here is by design, not a gap."
  ]
}

json.dump(validation, open(os.path.join(D, "04_validation.json"), "w", encoding="utf8"),
          ensure_ascii=False, indent=2)
json.dump(converged, open(os.path.join(D, "04_converged.json"), "w", encoding="utf8"),
          ensure_ascii=False, indent=2)
print("sha256", sha)
print("wrote 04_validation.json, 04_converged.json")
