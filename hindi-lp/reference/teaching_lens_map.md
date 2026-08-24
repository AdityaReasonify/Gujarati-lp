# Teaching Lens Map (Step 2) — विधा → the lens that teaches it

The **lens** is the question the whole chapter is taught through. It is set once at Agent 1 from
the diagnosed विधा, recorded in `01_meta.json` as `teaching_lens` + `guiding_question`, and every
`explanation` afterwards serves it.

| विधा | Lens | Guiding question (the engine) |
|---|---|---|
| **प्रकृति / देशभक्ति काव्य** | चित्र + भाव + अलंकार | कवि किन चित्रों से अपना भाव जगाता है? |
| **नीति-काव्य / दोहा** | अनुभव की सीख + दृष्टांत | कवि किस रोज़मर्रा के दृश्य से जीवन की बात कहता है? |
| **भक्ति-पद** | भाव + संबंध + लोक-भाषा की मिठास | भक्त और भगवान का यह रिश्ता कैसा है? |
| **वीर-रस काव्य** | ओज + गति + चरित्र | लय और शब्द मिलकर वीरता का भाव कैसे जगाते हैं? |
| **कहानी** | घटना + पात्र + मोड़ | पात्र का कौन-सा चुनाव कहानी को मोड़ देता है? |
| **संस्मरण / जीवनी** | स्मृति + स्वर + मूल्य | किन क्षणों ने इस जीवन को याद रखने लायक़ बनाया? |
| **सूचनात्मक / सांस्कृतिक गद्य** | तथ्य + परंपरा + जिज्ञासा | यह परंपरा या तथ्य हमें अपने देश के बारे में क्या बताता है? |
| **संवाद / निबंध** | तर्क + दृष्टिकोण + ज़िम्मेदारी | दोनों पक्ष क्या कहते हैं, और मुझसे क्या चाहते हैं? |

## How the lens is used

- **Agent 2** writes objectives that serve the lens — an objective that could belong to any
  chapter is a bad objective.
- **Agent 12** writes each `explanation` through the lens. In a नीति दोहा the explanation ends at
  the सीख; in a भक्ति पद it ends at the भाव, and a सीख forced onto it is a hard fail.
- **Agent 13** checks that the chapter's `guiding_question` is actually answered by the sequence
  of topics — if reading all the explanations in order does not answer it, the lens or the cut is
  wrong.

## The lens is not a template

Two chapters of the same विधा have the same lens but different guiding questions, because the
question is derived from **this** text. `जलाते चलो` and `मातृभूमि` are both देशभक्ति काव्य; one
asks what a small light can do, the other what makes a land one's own. Deriving the guiding
question from the profile instead of from the chapter is the mistake this file exists to prevent.
