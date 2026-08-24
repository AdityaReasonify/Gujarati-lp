# Global Content Rules — enforced by every authoring agent

1. **સ્વરૂપ essence is a hard gate.** The active profile's **avoid** list outranks any other
   instinct. A નીતિ દુહો may be moralised; a ભક્તિ પદ may not be turned into a lesson about lying;
   a nonsense-adjacent or humorous passage may not be given a બોધ it does not carry.

2. **Verbatim before explanation.** No topic ships without an exact Gujarati-script
   `original_chunk`, transcribed faithfully from the rendered page (the GSEB PDFs carry no
   text layer).

3. **Never invent.** No અલંકાર, no પ્રાસ pattern, no biographical fact that is not in the text
   (`no_hallucination_policy.md`).

4. **No numbers in display text.** Never `કડી 2`, `પ્રશ્ન 4`, `સ્વાધ્યાય 3.1` inside a `topic_name`,
   `explanation`, `real_life_example`, summary, bullet or recall prompt. Say `બીજી કડીમાં`,
   `પહેલી ટેક`, `સ્વાધ્યાયનો પહેલો ભાગ`. Numbers survive only in ids and provenance fields.

5. **The child's voice, the child's world.** Teaching fields are 55–90 words of simple spoken
   શિષ્ટ ગુજરાતી addressed to a child of THIS standard (std 6–10), with an Indian real-life anchor
   (`teaching_voice_gu.md`).

6. **Gloss at the point of use.** Hard words are explained where they appear, not only in a list;
   for a second-language child, more everyday words genuinely need it
   (`shabd_gloss.md`).

7. **સ્વાધ્યાય is never a topic.** નીચેના પ્રશ્નોના ઉત્તર લખો / ખાલી જગ્યા પૂરો / જોડકાં જોડો /
   સમાનાર્થી-વિરુદ્ધાર્થી શબ્દો / રૂઢિપ્રયોગ / વાક્યપ્રયોગ / પ્રવૃત્તિ — every printed સ્વાધ્યાય sub-block
   (exact headings from Agent 1's inventory, never assumed) belongs to
   `exercise_solutions.json` alone.

8. **Three-tier summaries strictly increase**: `brief_summary` < `summary` < `detailed_summary`.
   They are three depths of the same account, not three different accounts.

9. **One image per reading scene; at most one interactive tool per chapter.** A borrowed image
   must genuinely match its scene; when nothing matches, author a prompt — and no Gujarati frame
   pool exists yet, so every scene gets an authored prompt (`agents/09_media_planning.md`).

10. **Respect the text's world.** GSEB Gujarati readers carry religion, region, community,
    disability, and struggle. Present them as the chapter does — with dignity, without
    stereotype. A devotional પદ or ભજન — નરસિંહ, મીરાં, and the Jain, Swaminarayan and sufi
    traditions alike — is literature with a living tradition behind it; teach its ભાવ and craft,
    never turn it into a comparative-religion lesson. A Kutch or Saurashtra practice is a custom
    with its own logic, never a curiosity. Where the chapter names a real community — the
    આદિવાસી communities of ડાંગ, the રબારી and ભરવાડ pastoral communities — name it accurately
    and never generically as "tribal people".

11. **Phase 2 is the shape.** Root `objectives[]` registry, `concepts[]` under every topic,
    concept-scoped media ids, `RQ{n}` recall ids (`phase2_contract.md`). A field that does not
    exist in that contract does not go in the plan.
