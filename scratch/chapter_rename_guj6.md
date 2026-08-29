# chapterMaster rename — Gujarati Std 6 (ChapterId 753-767)

Gujarati names are the printed chapter titles, taken verbatim from each plan's `chapter_name`
(which the LP2 rows already carry correctly).

| ChapterId | Ch | Current (English) | Rename to (Gujarati) |
|---|---|---|---|
| 753 | 1 | Ek J Dalna Pankhi | એક જ ડાળનાં પંખી |
| 754 | 2 | Chotaduk | ચોટડૂક |
| 755 | 3 | Ban To Tyare J Chhutshe | બાણ તો ત્યારે જ છૂટશે... |
| 756 | 4 | Avyo Mehulo | આવ્યો મેહુલો |
| 757 | 5 | Vijalirani | વીજળીરાણી |
| 758 | 6 | Sanskare Sarjyu Swarg | સંસ્કારે સર્જ્યું સ્વર્ગ |
| 759 | 7 | Chokkhaina sardar | ચોખ્ખાઈના સરદાર |
| 760 | 8 | Mamano Patra | મામાનો પત્ર |
| 761 | 9 | Garvi Gujaratno Garbo | ગરવી ગુજરાતનો ગરબો |
| 762 | 10 | Sathi Mare Bar | સાથી મારે બાર |
| 763 | 11 | Kamni Maja Ne Majanu Kam | કામની મજા ને મજાનું કામ |
| 764 | 12 | Ajabgajabno Melo | અજબગજબનો મેળો |
| 765 | 13 | Surya Sudhi Pahonchay | સૂર્ય સુધી પહોંચાય ? |
| 766 | 14 | Ek Chhokro Risano | એક છોકરો રિસાણો |
| 767 | 15 | Lo Pathri Mari Vat | લો, પાથરી મારી વાત |

## SQL (run against the education DB yourself — I did not execute this)

```sql
UPDATE public."chapterMaster" SET "ChapterName" = v.name
FROM (VALUES
  (753, 'એક જ ડાળનાં પંખી'),
  (754, 'ચોટડૂક'),
  (755, 'બાણ તો ત્યારે જ છૂટશે...'),
  (756, 'આવ્યો મેહુલો'),
  (757, 'વીજળીરાણી'),
  (758, 'સંસ્કારે સર્જ્યું સ્વર્ગ'),
  (759, 'ચોખ્ખાઈના સરદાર'),
  (760, 'મામાનો પત્ર'),
  (761, 'ગરવી ગુજરાતનો ગરબો'),
  (762, 'સાથી મારે બાર'),
  (763, 'કામની મજા ને મજાનું કામ'),
  (764, 'અજબગજબનો મેળો'),
  (765, 'સૂર્ય સુધી પહોંચાય ?'),
  (766, 'એક છોકરો રિસાણો'),
  (767, 'લો, પાથરી મારી વાત')
) AS v(id, name)
WHERE "chapterMaster"."ChapterId" = v.id;
```
