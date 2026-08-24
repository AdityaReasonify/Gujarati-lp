# Global Content Rules — enforced by every authoring agent

1. **विधा essence is a hard gate.** The active profile's **avoid** list outranks any other
   instinct. A नीति दोहा may be moralised; a भक्ति पद may not be turned into a lesson about lying;
   a नonsense-adjacent or humorous passage may not be given a शिक्षा it does not carry.

2. **Verbatim before explanation.** No topic ships without an exact Devanagari `original_chunk`.

3. **Never invent.** No अलंकार, no तुक pattern, no biographical fact that is not in the text
   (`no_hallucination_policy.md`).

4. **No numbers in display text.** Never `छंद 2`, `प्रश्न 4`, `अभ्यास 3.1` inside a `topic_name`,
   `explanation`, `real_life_example`, summary, bullet or recall prompt. Say `दूसरे छंद में`,
   `पहली टेक`, `पाठ-अभ्यास का पहला भाग`. Numbers survive only in ids and provenance fields.

5. **The child's voice, the child's world.** Teaching fields are 55–90 words of simple खड़ी बोली
   addressed to an eleven-year-old, with an Indian real-life anchor
   (`teaching_voice_hi.md`).

6. **Gloss at the point of use.** Hard words are explained where they appear, not only in a list
   (`shabd_gloss.md`).

7. **अभ्यास is never a topic.** मेरी समझ से / सोच-विचार के लिए / भाषा की बात / कविता की रचना /
   आपकी बात / मिलकर करें मिलान belong to `exercise_solutions.json` alone.

8. **Three-tier summaries strictly increase**: `brief_summary` < `summary` < `detailed_summary`.
   They are three depths of the same account, not three different accounts.

9. **One image per reading scene; at most one interactive tool per chapter.** A borrowed image
   must genuinely match its scene; when nothing matches, author a prompt (`agents/09_media_planning.md`).

10. **Respect the text's world.** मल्हार chapters carry religion, region, caste-adjacent social
    detail, disability, and war. Present them as the chapter does — with dignity, without
    stereotype, without turning a devotional text into a comparative-religion lesson or a
    regional custom into a curiosity. Where the chapter names a real community
    (भील-भिलाला, सत्रिया, बिहू), name it accurately and never generically as "tribal people".

11. **Phase 2 is the shape.** Root `objectives[]` registry, `concepts[]` under every topic,
    concept-scoped media ids, `RQ{n}` recall ids (`phase2_contract.md`). A field that does not
    exist in that contract does not go in the plan.
