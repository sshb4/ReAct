# Required-query results

Recorded: 9 of 9 queries.

These are actual model outputs. An answer terminal reason does not certify relevance or completeness.

## Recorded configuration

- runtime_profile: `local`
- answer_mode: `extractive`
- embedding_model: `Qwen3-Embedding-8B`
- embedding_service_model: `qwen3-embedding:8b`
- llm_model: `qwen3:4b`
- chunk_size: `1400`
- chunk_overlap: `200`
- retrieval_k: `6`
- retrieval_candidate_k: `18`
- section_link_expansion_limit: `2`
- max_steps: `16`
- chat_context_tokens: `16384`
- chat_thinking: `False`
- chat_output_tokens_per_action: `4096`
- index_version: `0f3e6565bb6d0713`

Local Ollama Q4 embedding weights and local chat model replace the required course services; not a fully compliant course-service run.

Final answer passages are copied verbatim and checked against their cited retrieved chunks.
This verifies quote fidelity and provenance. Relevance and coverage are reviewed separately.

## Q1: answer

According to FDA Food Code 2026 sections 2-201.12(A)(1) and
2-201.13(A)(1), what must the person in charge do when a food employee has
vomiting or diarrhea from no known noninfectious condition, and when may that
employee be reinstated?

Steps: 3/16. [Complete action-observation trace](Q1.json).

Review: supported / complete.

### Evidence 1

Source: `fda-food-code-2026.pdf`, physical PDF page 61, chunk `34d7d609c8ed642bc104e5cc`.

```text
FDA Food Code 2026  Chapter 2. Management and Personnel 
33 
Managing exclusions and restrictions 
2-201.13 Removal, Adjustment, or Retention of Exclusions and Restrictions  
The *PERSON IN CHARGE shall adhere to the following conditions when removing, 
adjusting, or retaining the *EXCLUSION or *RESTRICTION of a *FOOD EMPLOYEE:  
(A) Except when a *FOOD EMPLOYEE is diagnosed with typhoid fever or an 
infection from hepatitis A virus: 
Removing exclusion for food employee who was symptomatic and not diagnosed 
(1) Reinstate a *FOOD EMPLOYEE who was *EXCLUDED as specified under 
Subparagraph 2-201.12(A)(1) if the *FOOD EMPLOYEE:  
(a) Is *ASYMPTOMATIC for at least 24 hours; P or 
(b) Provides to the *PERSON IN CHARGE written medical documentation from 
a *HEALTH PRACTITIONER that states the symptom is from a 
noninfectious condition. P  
Norovirus diagnosis 
(2) If a *FOOD EMPLOYEE was diagnosed with an infection from norovirus and 
*EXCLUDED as specified under Subparagraph 2-201.12(A)(2):  
Adjusting exclusion for food employee who was symptomatic and is now 
asymptomatic 
(a) **RESTRICT the *FOOD EMPLOYEE, who is *ASYMPTOMATIC for at least 24 
hours and *WORKS in a *FOOD ESTABLISHMENT not serving a *HIGHLY 
SUSCEPTIBLE POPULATION, until the conditions for reinstatement as 
specified under Subparagraphs (D)(1) or (2) of this section are 
met; P or
```

### Evidence 2

Source: `fda-food-code-2026.pdf`, physical PDF page 59, chunk `f04162d9369fc9b7ec7ba21d`.

```text
FDA Food Code 2026  Chapter 2. Management and Personnel 
31 
(2) Comply with a *RESTRICTION as specified under Subparagraphs 2-
201.12(D)(2), (E)(2), (F)(2), (G), (H)(2), or ¶¶ 2-201.12 (H), (I), or (J) and 
comply with the provisions specified under ¶¶ 2-201.13(D)-(J). P 
Conditions of exclusion and restriction 
2-201.12 Exclusions and Restrictions. 
The *PERSON IN CHARGE shall *EXCLUDE or *RESTRICT a *FOOD EMPLOYEE from a 
*FOOD ESTABLISHMENT in accordance with the following:  
Symptomatic with vomiting or diarrhea 
(A) Except when the symptom is from a noninfectious condition, *EXCLUDE a 
*FOOD EMPLOYEE if the *FOOD EMPLOYEE is:  
(1) Symptomatic with vomiting or diarrhea; P or 
(2) Symptomatic with vomiting or diarrhea and diagnosed with an infection 
from norovirus, Shigella spp., Salmonella (non-typhoidal) , or *SHIGA TOXIN-
PRODUCING *ESCHERICHIA COLI. P  
Jaundiced or diagnosed with hepatitis A infection 
(B) *EXCLUDE a *FOOD EMPLOYEE who is: 
(1) Jaundiced and the onset of jaundice occurred within the last seven 
calendar days, unless the *FOOD EMPLOYEE provides to the *PERSON IN 
CHARGE written medical documentation from a *HEALTH PRACTITIONER 
specifying that the jaundice is not caused by hepatitis A virus or other 
fecal-orally transmitted infection; P 
(2) Diagnosed with an infection from hepatitis A virus within 14 calendar days
```

### Evidence 3

Source: `fda-food-code-2026.pdf`, physical PDF page 404, chunk `31866a690a1c033d3f538737`.

```text
FDA Food Code 2026 Annex 3. Public Health Reasons/Administrative 
Guidelines 
324 
food establishment, but could work unrestricted in another retail store that is not a food 
establishment. A restricted food employee may enter a food establishment as a 
consumer.  
An excluded individual may not work as a food employee on the premises of any food 
establishment.  
2-201.13 Removal of Exclusions and Restrictions.5 
Food employees diagnosed with norovirus, hepatitis A virus, Shigella spp., E. coli 
O157:H7 or other STEC, non-typhoidal Salmonella and symptomatic with diarrhea, 
vomiting, or jaundice, are excluded under Subparagraph 2-201.12 (A)(2) or 2-
201.12(B)(2). However, these symptomatic, diagnosed food employees differ from 
symptomatic, undiagnosed food employees in the requirements that must be met before 
returning to work in a full capacity after symptoms resolve.  
The person in charge may allow undiagnosed food employees who are initially 
symptomatic and whose symptoms have resolved to return to work in a full capacity 
24 hours after symptoms resolve.  
However, diagnosis with a listed pathogen invokes additional requirements before the 
person in charge may allow diagnosed food employees to return to work in full capacity.  
Culture-Independent Diagnostic Tests (CIDT) For Medical Clearance
```

### Evidence 4

Source: `fda-food-code-2026.pdf`, physical PDF page 388, chunk `94876a91e3d81e0c4aa1b9f0`.

```text
FDA Food Code 2026 Annex 3. Public Health Reasons/Administrative Guidelines 
308 
Table 1a. Summary of Requirements for Symptomatic Food Employees 
Symptom 
Exclusion or 
Restriction 
(Facilities 
Serving an HSP) 
Exclusion or 
Restriction 
(Facilities Not 
Serving an HSP) 
Removing Symptomatic Food Employees from Exclusion 
or Restriction 
RA Approval 
Needed to 
Return to 
Work? 
Vomiting EXCLUDE 
2-201.12(A)(1) 
EXCLUDE 
2-201.12(A)(1) 
When the excluded food employee has been asymptomatic for 
at least 24 hours or provides medical documentation 2-
201.13(A)(1).  
Exceptions: If diagnosed with norovirus, Shigella spp., STEC, 
HAV, or typhoid fever (S. Typhi) (see Tables 1b & 2). 
No if not 
diagnosed  
Diarrhea EXCLUDE 
2-201.12(A)(1) 
EXCLUDE 
2-201.12(A)(1) 
When the excluded food employee has been asymptomatic for 
at least 24 hours or provides medical documentation 2-
201.13(A).  
Exceptions: If Diagnosed with norovirus, STEC, HAV, or S. 
Typhi (see Tables 1b & 2). 
No if not 
diagnosed 
Jaundice EXCLUDE 
2-201.12(B)(1) if 
the onset occurred 
within the last 7 
days 
EXCLUDE 
2-201.12(B)(1) if 
the onset occurred 
within the last 7 
days 
When approval is obtained from the RA 2-201.13 (B), and:  
Food employee has been jaundiced for more than 7 calendar 
days 2-201.13(B)(1), or  
Food employee provides medical documentation 
2-201.13(B)(3).  
Yes 
Sore Throat with
```

## Q2: answer

A food employee begins vomiting during a shift. Using the *Employee Health and
Personal Hygiene Handbook*, what should the employee and manager do immediately,
and what is the earliest return to work?

Steps: 3/16. [Complete action-observation trace](Q2.json).

Review: supported / complete.

### Evidence 1

Source: `fda-employee-health-personal-hygiene-handbook.pdf`, physical PDF page 7, chunk `d4282f13bd2bd9a74711a325`.

```text
residing with a diagnosed individual.
What should a manager do when a food employee reports symptoms of vomiting 
or diarrhea? (See Decision Tree 1 and Table 1a (and Table 1b if diagnosed))
Ask the food employee to stop work immediately and leave the food establishment. Permit a return to 
work no sooner than 24 hours after vomiting and diarrhea have ended.
Employee Health Management Responsibilities
```

### Evidence 2

Source: `fda-employee-health-personal-hygiene-handbook.pdf`, physical PDF page 6, chunk `84beda9088b485f3cce87bd7`.

```text
4
Employee Health and the Food Establishment
What symptoms of foodborne illness should food establishments be most 
concerned about?
Food establishments should be most concerned about the following symptoms:
• Vomiting
• Diarrhea
• Jaundice (yellow skin or eyes)
• Sore throat with fever
• Infected cuts and burns with pus on hands, wrists and exposed portion of the arms
What should food employees do when they have symptoms of vomiting or diarrhea?
If at work:
• Stop work immediately;
• Report to management; and
• Go home and return after at least 24 hours have passed since the vomiting and diarrhea 
symptoms ended.
If the symptoms occur before the employee arrives to work, he or she should:
• Notify the manager by telephone; and
• Do not report to work until at least 24 hours have passed after the diarrhea and vomiting 
symptoms have ended.
What should food employees do if they are not feeling well and their skin or eyes 
turn yellow?
Report the symptoms to their manager or person in charge (PIC) immediately and seek medical 
attention. The employee should not return to work until after receiving clearance from a health 
practitioner. If the employee is jaundiced for more than 7 days, clearance from the local health 
department is required.
What should food employees do if they have an infected wound or cut on their hand 
or arm?
```

### Evidence 3

Source: `fda-employee-health-personal-hygiene-handbook.pdf`, physical PDF page 31, chunk `7ba6c6e61e6f2c18d172b7ad`.

```text
29
2-201.12 Table 1a Summary of Requirements for Symptomatic 
Food Employees
Food employees and conditional employees shall report symptoms immediately to the person 
in charge
The person in charge shall prohibit a conditional employee who reports a listed symptom from 
becoming a food employee until meeting the criteria listed in section 2-201.13 of the Food Code, 
for reinstatement of a symptomatic food employee.
Symptom Exclusion or 
Restriction
(Facilities 
Serving an HSP)
Exclusion or 
Restriction
(Facilities Not 
Serving an HSP)
Removing Symptomatic Food Employees 
from Exclusion or Restriction
RA Approval 
Required to 
Return to 
Work?
Vomiting Exclude
2-201.12(A)(1)
Exclude
2-201.12(A)(1)
When the excluded food employee has been 
asymptomatic for at least 24 hours or provides 
medical documentation 2-201.13(A)(1).  
Exceptions: If diagnosed with Norovirus, 
Shigella spp., STEC, HAV, or typhoid fever 
(S. Typhi) (see Tables 1b and 2).
No, if not 
diagnosed
Diarrhea Exclude
2-201.12(A)(1)
Exclude
2-201.12(A)(1)
When the excluded food employee has been 
asymptomatic for at least 24 hours or provides 
medical documentation 2-201.13(A).  
Exceptions: If Diagnosed with Norovirus, 
STEC, HAV, or S. Typhi (see Tables 1b and 2).
No, if not 
diagnosed
Jaundice Exclude
2-201.12(B)(1) 
if the onset 
occurred within 
the last 7 days
Exclude
2-201.12(B)(1) 
if the onset
```

### Evidence 4

Source: `fda-employee-health-personal-hygiene-handbook.pdf`, physical PDF page 11, chunk `80d7eb0bdeb1f61b82cb5963`.

```text
are shed in the stool and vomit affects when a food employee can return to work.
Considerations for the PIC include:
• Was the employee asymptomatic?
• Is medical documentation required?
• Is regulatory authority approval required for return to work? Note: Consult with your local 
jurisdiction, and use the following instructions to determine when an employee may return to work 
after restriction or exclusion.
```

## Q3: answer

According to the *Bad Bug Book*, what is the estimated infective dose of
norovirus, when do symptoms usually begin, what are the characteristic symptoms,
and how can food workers contaminate ready-to-eat food?

Steps: 3/16. [Complete action-observation trace](Q3.json).

Review: partially supported / partial; includes wrong-topic evidence.

### Evidence 1

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 169, chunk `f2da71ef5e2f8e7f14ab9540`.

```text
single copy of a minor structural Protein (VP2). The 27-32 nm viral particles have a buoyant 
density of 1.39 to 1.40 g/ml in CsCl.     
2. Disease 
Common names of the illness, which is the leading cause of foodborne illness in the United 
States, are viral gastroenteritis, acute nonbacterial gastroenteritis, food poisoning, and winter 
vomiting disease.     
	 Mortality: Overall, these illne sses account for 26% of hospitalizations and 11% of 
deaths associated with food consumption.  
	 Infective dose:  The infective dose is very low; it is estimated to be as low as 1 to 10 
viral particles, and the particles are excreted at high levels by both symptomatic and 
asymptomatic people (as high as 1 x 1012 million viral particles/g feces). 
	 Onset: A mild, brief illness usually develops between 24 and 48 hours after contaminated 
food or water is consumed (median in outbreaks: 33 to 36 hours), but onset times within 
12 hours of exposure have been reported. 
	 Illness / complications: Norovirus illness is self-limiting, but can be very debilitating as 
a result of the high rate of vomiting. Recovery is usually complete and without evidence 
of long-term effects. Dehydration is the most common complication, especially among 
the very young, the elderly, and patients with underlying medical conditions.
```

### Evidence 2

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 168, chunk `e63b7c302bdbac95f1ac25a3`.

```text
In the U.S., norovirus is the leading cause of illness from 
contaminated food or water – but food isn’t the only way 
people get this illness. It also spreads easily from person 
to person and spreads quickly in groups of people. 
Examples of foods that have caused norovirus illness are 
fruits, vegetables, meats, and salads prepared or handled 
by an infected person. Oysters grown in contaminated 
water are another example. Symptoms usually start 
within 1 or 2 days of eating the contaminated food, but 
may start in as few as 12 hours. Vomiting that’s explosive 
and projectile – that shoots out – often is the first 
symptom, along with watery diarrhea that isn’t bloody, 
and cramps. Headache, mild fever, and muscle aches also 
may occur. Most people get better in a day or two, 
although it takes others a little longer. Occasionally, 
some people lose so much body fluid that it throws off 
the body’s balance of some important minerals (called 
electrolytes) and fluid, which can cause serious health 
problems. These people need to be treated by a health 
professional, and sometimes need to be hospitalized. 
Antibiotics don’t work against this or other viruses (they 
only work against bacteria), but health professionals can 
give the right fluids and minerals to put the body back in 
balance. You can help protect yourself and others against
```

### Evidence 3

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 170, chunk `6b4a95883eee551fb572742f`.

```text
approximately 0.03% (mean, 14,663; range, 8,097 to 23,323) require hospitalization, and less 
than 0.1% of these illnesses results in death (mean,149; range, 84 to 237). 
4. 	Sources 
NoV outbreaks have been associated with consumption of contaminated water, including 
municipal water, well water, stream water, commercial ice, lake water, and swimming pool or 
recreational surface-water exposure, as well as floodwater. 
Salad ingredients, fruit, and oysters are the foods most often implicated in norovirus outbreaks. 
However, any ready-to-eat food that is that is handled by ill food workers may be contaminated. 
Nearly 29% of all NoV foodborne outbreaks from 1997-2004 could be attributed to food 
purchased or served at a restaurant or delicatessen. Molluscan shellfish, particularly oysters, 
have been commonly identified in NoV-related gastroenteritis outbreaks, worldwide. However, 
this represents a different etiology that does not necessarily involve a contaminated food 
worker. 
The rapid spread of secondary infections is particularly evident in areas where a large 
population is enclosed within a static environment, such as in institutions, college campuses, 
schools, military operations, hotels, restaurants, recreational camps, hospitals, nursing homes, 
day-care facilities, and cruise ships, and after natural disasters, such as hurricanes and 
earthquakes.
```

### Evidence 4

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 185, chunk `1d78f7efeacb38396a491692`.

```text
that  also  cause  foodborne  illness,  but  not  nearly  
as  often.  In  general,  the  illnesses  they  cause  
start  within  10  to  70  hours  after  a  person  eats  or  
drinks  contaminated  food  or  fluid,  are  mild,  last  
anywhere  from  2  to  9  days,  and  go  away  by  
themselves.  Some  common  symptoms  are  
nausea;  vomiting;  diarrhea;  a  sick,   
uncomfortable  feeling;  abdominal  pain;  
headache;  and  fever.  Following  basic  food‐safety 
tips  can  help  protect  you  from  getting  these  
viruses.  Since  they  can  also  be  spread  from  
person  to  person  (for  example,  when  infected  
people  have  a  bowel  movement  and  don’t  wash  
their  hands  well,  so  that  anything  they  touch  
spreads  the  virus  to  other  people  and  objects),  
good  handwashing  is  especially  important.
```

## Q4: answer

According to Appendix 3, Table 3-A, compare *Salmonella* species and *Listeria
monocytogenes* by minimum water activity, pH range, temperature range, maximum
water-phase salt, and oxygen requirement.

Steps: 3/16. [Complete action-observation trace](Q4.json).

Review: supported / complete.

### Evidence 1

Source: `fda-appendix-3-bacterial-pathogen-growth-inactivation.pdf`, physical PDF page 3, chunk `3dacc48d446f30d92f1c2f65`.

```text
Contains Non-binding Recommendations 
Draft-Not for Implementation 
 
Appendix 3 (Bacterial Pathogen Growth and Inactivation) - Page 3 
 
Table 3-A Limiting Conditions for Pathogen Growth 
Pathogen 
Min. aw 
(using 
salt) 
Min.  
pH 
Max.  
pH 
Max. % 
Water 
Phase 
Salt 
Min. 
Temp. 
Max. 
Temp. 
Oxygen  
Requirement 
Bacillus 
cereus 0.92 4.3 9.3 10 39.2°F  4°C 131°F1  55°C facultative anaerobe4 
Campylo-
bacter jejuni 0.987 4.9 9.5 1.7 86°F 30°C 113°F 45°C micro- aerophile2 
Clostridium 
botulinum,  
type A, and 
proteolytic 
types B and 
F 
0.935 4.6 9 10 50°F  10°C 118.4°F  48°C anaerobe3 
Clostridium 
botulinum,  
type E, and 
non-
proteolytic 
types B and 
F 
0.97 5 9 5 37.9°F  3.3°C 113°F  45°C anaerobe3 
Clostridium 
perfringens 0.93 5 9 7 50°F  10°C 125.6°F  52°C anaerobe3 
Pathogenic 
strains of  
Escherichia 
coli 
0.95 4 10 6.5 43.7°F  6.5°C 120.9°F  49.4°C facultative  anaerobe4 
Listeria 
monocyto-
genes 
0.92 4.4 9.4 10 31.3°F  -0.4°C 113°F  45°C facultative  anaerobe4 
Salmonella 
spp. 0.94 3.7 9.5 8 41.4°F 5.2°C 115.2°F  46.2°C facultative  anaerobe4 
Shigella spp. 0.96 4.8 9.3 5.2 43°F  6.1°C 116.8°F 47.1°C facultative  anaerobe4 
Staphylo-
coccus 
aureus 
growth 
0.83 4 10 20 44.6°F  7°C 122°F  50°C facultative  anaerobe4
```

### Evidence 2

Source: `fda-appendix-3-bacterial-pathogen-growth-inactivation.pdf`, physical PDF page 4, chunk `955f4c8e97015a31cd71f080`.

```text
Contains Non-binding Recommendations 
Draft-Not for Implementation 
 
Appendix 3 (Bacterial Pathogen Growth and Inactivation) - Page 4 
 
Pathogen 
Min. aw 
(using 
salt) 
Min.  
pH 
Max.  
pH 
Max. % 
Water 
Phase 
Salt 
Min. 
Temp. 
Max. 
Temp. 
Oxygen  
Requirement 
Staphylo-
coccus 
aureus toxin 
formation 
0.85 4 9.8 10 50°F  10°C 118°F  48°C facultative  anaerobe4 
Vibrio 
cholerae 0.97 5 10 6 50°F  10°C 109.4°F 43°C facultative  anaerobe4 
Vibrio 
parahaemo-
lyticus 
0.94 4.8 11 10 41°F  5°C 113.5°F  45.3°C facultative  anaerobe4 
Vibrio 
vulnificus 0.96 5 10 5 46.4°F  8°C 109.4°F  43°C facultative  anaerobe4 
Yersinia 
enterocoliti-
ca 
0.945 4.2 10 7 29.7°F  -1.3°C 107.6°F  42°C facultative  anaerobe4 
1Has significantly delayed growth (>24 hours) at 131°F (55°C). 
2Requires limited levels of oxygen. 
3Requires the absence of oxygen. 
4Grows either with or without oxygen.
```

### Evidence 3

Source: `fda-appendix-3-bacterial-pathogen-growth-inactivation.pdf`, physical PDF page 1, chunk `65399696a310b7fd2f352d0f`.

```text
cells or spores of a microbial strain at a specified temperature characterize its thermal resistance at 
that temperature.  Therefore, D-values and z-values provide a means to compare the thermal 
resistance of different microorganisms, or different strains of the same microorganism, at one or mor e 
temperatures.   
Table 3-A contains information on the minimum water activity (aw), minimum and maximum pH, 
and minimum and maximum temperatures that limit  growth for the bacterial pathogens that are 
of greatest concern in food processing.  Table 3-A also provides data on the maximum water 
                                                
1 This guidance has been prepared by the Office of Food Safety in the Center for Food Safety and 
Applied Nutrition at the U.S. Food and Drug Administration. Underlined text in yellow highlights 
represents a correction from the draft Appendix 3 that we issued for public comment in August 2016.
```

### Evidence 4

Source: `fda-appendix-3-bacterial-pathogen-growth-inactivation.pdf`, physical PDF page 13, chunk `722aaf3fc9133561be31345d`.

```text
Contains Non-binding Recommendations 
Draft-Not for Implementation 
 
Appendix 3 (Bacterial Pathogen Growth and Inactivation) - Page 13 
 
Catsaras, M., and D. Grebot. 1984. "Multiplication des Salmonella dans la viande hachee."  Bull. 
Acad. Vet. France. 57:501-512. 
Cole, M. B., M. V. Jones, and C. Holyoak. 1990. "The effect of pH, salt concentration and 
temperature on the survival and growth of Listeria monocytogenes."  J Appl Bacteriol 69 
(1):63-72. 
Colwell, R. R. 1984. Vibrios in the environment. New York, NY: John Wiley Interscience. 
Conner, D. E., V. N. Scott, and D. T. Bernard. 1990. "Potential Clostridium botulinum hazards 
associated with extended shelf-life refrigerated foods:  a review."  Journal of Food Safety 
10 (2):131-153. 
Cortesi, M. L., T. Sarli, A. Santoro, N. Murru, and T. Pepe. 1997. "Distribution and behavior of 
Listeria monocytogenes in three lots of naturally-contaminated vacuum-packed smoked 
salmon stored at 2 and 10 degrees C."  International Journal of Food Microbiology 37 (2-
3):209-214. doi: 10.1016/S0168-1605(97)00064-0. 
Craven, S. E. 1980. "Growth and sporulation of Clostridium perfringens in foods."  Food Technol 
Chicago 34 (4):80-&. 
Curtis, L. M., M. Patrick, and C. D. Blackburn. 1995. "Survival of Campylobacter jejuni in foods 
and comparison with a predictive model."  Lett Appl Microbiol 21 (3):194-7.
```

## Q5: answer

In the Utah Risk Factor Study, which four inspection line items were more likely
to be violations in summer, what were their rate ratios, and what limitations
constrain interpretation of those findings?

Steps: 3/16. [Complete action-observation trace](Q5.json).

Review: supported quotations; incomplete answer / partial.

### Evidence 1

Source: `utah-risk-factor-study-2016-2017.pdf`, physical PDF page 4, chunk `2b864a43b4fcf19deceb78d6`.

```text
28 1.15 1.02 1.28 p < 0.025 
33 1.50 1.22 1.86 p < 0.005 
36 1.23 1.04 1.45 p < 0.025 
alpha = 0.05 Summer months defined as June, July, and August 
 
MORE LIKELY VIOLATION IN SUMMER 
22 Proper cold holding temperatures 
28 Toxic substances properly identified, stored, and used 
33 Proper cooling methods used; adequate equipment for temperature control 
36 Thermometers provided & accurate  
 
Correlated Line Items 
 No line item pair correlations were found to meet the threshold of -0.80 => r >= +0.80.  Ninety-
one percent of correlations were found have a coefficient close to zero (-0.20 =< r <= 0.20).   
 
Limitations: 
 Of the 13 local health departments, seven volunteered data for use in this study.  More than half 
of the local health departments currently use a method for storing inspection data digitally; the rest 
keep inspection hard copies.  One health department sent in scanned copies of inspection data, which 
needed to be inputted manually.  The time and labor involved with sending, collating, and scanning in 
copies of paper inspections likely limited broader participation by the local health departments. 
 
 This analysis is dependent on the ability to categorize establishments based on inherent risk due 
to populations served, types of food served, and type of food preparation techniques used.  Though the
```

### Evidence 2

Source: `utah-risk-factor-study-2016-2017.pdf`, physical PDF page 6, chunk `7d8d0a130714189d289ec5f1`.

```text
The frequency of line numbers 55, 47, and 49 being marked highlights a concern that has been 
growing among regulators and the FDA that inspectors are focusing on items that are not posing a direct 
risk to consumers.  As noted above, proper hand washing was only noted in the top ten violations for 
Category 1 establishments which are the lowest risk establishments.  Out of all inspections conducted in 
2016, proper hand washing violations are only marked in 4% of inspections where a violation occurred.  
This supposes that either there is little to no problem with proper hand washing, or inspectors are not 
focusing on the items most likely to contribute to foodborne illness, such as proper hand washing.  This 
has been highlighted in conversations between FDA Trained State Standards and the local 
trainer/Standardee when doing standardization exercises.  A frequent item discussed during these 
exercises is the hand washing violations observed by the Standard while the Standardee is looking at 
something else.  These results would suggest that more in-depth training on risk based inspections may 
be needed. 
 
The higher likelihood of cooling and cold holding violations (line items 33 and 22 respectively) 
during summer months, while intuitively unsurprising, is concerning.  This should not be the case as all
```

### Evidence 3

Source: `utah-risk-factor-study-2016-2017.pdf`, physical PDF page 6, chunk `7d8d0a130714189d289ec5f1`.

```text
The frequency of line numbers 55, 47, and 49 being marked highlights a concern that has been 
growing among regulators and the FDA that inspectors are focusing on items that are not posing a direct 
risk to consumers.  As noted above, proper hand washing was only noted in the top ten violations for 
Category 1 establishments which are the lowest risk establishments.  Out of all inspections conducted in 
2016, proper hand washing violations are only marked in 4% of inspections where a violation occurred.  
This supposes that either there is little to no problem with proper hand washing, or inspectors are not 
focusing on the items most likely to contribute to foodborne illness, such as proper hand washing.  This 
has been highlighted in conversations between FDA Trained State Standards and the local 
trainer/Standardee when doing standardization exercises.  A frequent item discussed during these 
exercises is the hand washing violations observed by the Standard while the Standardee is looking at 
something else.  These results would suggest that more in-depth training on risk based inspections may 
be needed. 
 
The higher likelihood of cooling and cold holding violations (line items 33 and 22 respectively) 
during summer months, while intuitively unsurprising, is concerning.  This should not be the case as all
```

### Evidence 4

Source: `utah-risk-factor-study-2016-2017.pdf`, physical PDF page 6, chunk `59a4c9e1d82a9b3db554569f`.

```text
during summer months, while intuitively unsurprising, is concerning.  This should not be the case as all 
facilities should have adequate ventilation as required in 6-304.11 of the 2013 FDA Food Code.  The 
indoor temperature of a restaurant should be independent of out door temperatures.  The serving areas 
are normally temperature controlled, but anecdotal evidence suggests that kitchen temperatures of 
over 90°F are not uncommon.  A simple understanding of the mechanics of refrigeration would conclude 
the existence of a limit for ambient temperature past which cooling equipment would become 
inefficient, increasing the likelihood of temperature abused food.  The efficacy of cooling equipment 
with food directly exposed to ambient air is especially impacted.  Consideration should be given during 
plan reviews to how ambient temperatures in food preparation areas will be controlled. 
 
 Line items 28 and 36 were found to also be marked more frequently in summer months.  More 
data is needed before formulating a rationale for why the use or storage of toxic substances (line 28) 
would be found in violation more frequently in summer months.  This may also apply to line 36 
(Thermometers provided and accurate), though it may be that inspectors are looking at an 
establishment's thermometers more frequently in summer months due to increased observations of
```

## Q6: error

A food employee with no diagnosis and no known noninfectious condition vomited
while preparing ready-to-eat salads in a nursing home. Using the FDA Food Code
2026 and the *Bad Bug Book*, explain the required employee disposition, the
earliest conditions for return, and why possible norovirus transmission is a
concern. Treat vomiting as a symptom; the scenario supplies no norovirus
diagnosis.

Steps: 5/16. [Complete action-observation trace](Q6.json).

Review: no accepted answer; validation error / incomplete.

ValueError: Answer omitted requested source evidence: fda-bad-bug-book-second-edition.pdf

## Q7: error

The *Employee Health and Personal Hygiene Handbook* refers to the 2017 Food
Code, while the corpus also includes the 2026 Food Code. Which source should
control an answer about the current FDA model-code rule for a vomiting employee,
and how may the handbook still be used?

Steps: 5/16. [Complete action-observation trace](Q7.json).

Review: no accepted answer; validation error / incomplete.

ValueError: Answer omitted requested source evidence: fda-employee-health-personal-hygiene-handbook.pdf

## Q8: answer

What Utah regulation currently adopts the FDA Food Code 2026, and what penalties
does it impose on a restaurant that violates employee-illness rules?

Steps: 5/16. [Complete action-observation trace](Q8.json).

Review: unsupported as an answer to the jurisdictional question / incorrect terminal.

### Evidence 1

Source: `fda-food-code-2026.pdf`, physical PDF page 72, chunk `8e26db53e5d1932fd0af7396`.

```text
FDA Food Code 2026  Chapter 2. Management and Personnel 
44 
*CONDITIONAL EMPLOYEES, the *PERSON-IN-CHARGE, and required reporting to 
the *REGULATORY AUTHORITY:  
(1) Illness symptoms of diarrhea, vomiting, sore throat with fever, jaundice or 
infected wounds or cuts; Pf 
(2) Illness disease diagnosis due to norovirus, hepatitis A virus, Shigella spp., 
Typhoid fever, non-typhoidal Salmonella, or *SHIGA TOXIN-PRODUCING 
ESCHERICHIA COLI; Pf and 
(3) Illness *EXCLUSION and/or *RESTRICTION and reinstatement after illness 
symptom or disease resolution. Pf 
2-502 Contamination Event Response Procedures 
2-502.11 Clean-up of Vomiting and Diarrheal Events 
A *FOOD ESTABLISHMENT shall have written procedures for *EMPLOYEES to follow 
when responding to vomiting or diarrheal events that involve the discharge of 
vomitus or fecal matter onto surfaces in the *FOOD ESTABLISHMENT. The 
procedures shall address the specific actions *EMPLOYEES must take to minimize 
the spread of contamination and the exposure of *EMPLOYEES, *CONSUMERS, 
*FOOD and surfaces to vomitus or fecal matter. Pf
```

### Evidence 2

Source: `fda-food-code-2026.pdf`, physical PDF page 725, chunk `2e62edae67d670090551a3ea`.

```text
FDA Food Code 2026  Summary of Changes 
Summary-645 
2-301.16  
Amended Public Health Reason for § 2-301.16 Hand Antiseptics to revise paragraphs 2 
and 3 to clarify the intent of hand antiseptics.  
2-303.11   
Amended Public Health Reasons for § 2-303.11 Prohibition, to 
address an additional exception for individuals with disabilities covered by the Americans 
with Disabilities Act, to wear a medically necessary device.  
2-5   
• Amended Public Health Reasons to add new Part 2-5 to address written policy 
and procedures requirements for employee illness   
• Amended Public Health Reasons to add new subPart 2-501 to address what 
an employee illness policy is and the purpose of an illness policy for each food 
establishment.     
• Amended Public Health Reasons for the previous § 2-501.11 to 
new title “Employee Illness Policy Documentation” to address the basic 
components of an Employee Illness Policy.  “Clean-up of Vomiting and Diarrheal 
Events” was moved to a new § 2-502.11.  
• Amended Public Health Reasons to add new subPart 2-502; “Contamination 
Event Response Procedures” to cover all contamination event responses.     
• Amended Public Health Reasons to add new § 2-502.11 “Clean-up of Vomiting 
and Diarrheal event” to include the previous § 2-501.11 for “Procedures 
for Responding to Vomiting and Diarrheal Events.”
```

### Evidence 3

Source: `fda-food-code-2026.pdf`, physical PDF page 684, chunk `537771e4f20672cce15e37e1`.

```text
when it is demonstrated that the food establishment has available for employees a written 
employee health policy addressing symptoms and illness reporting, exclusion/restriction, 
reinstatement, and regulatory reporting requirements in accordance with §§ 2- 201.11, 2-
201.12, and 2-201.13; and written procedures for responding to vomiting or diarrheal 
events that involve the discharge of vomitus or fecal matter onto surfaces in the food 
establishment in accordance with § 2-502.11.  
 
This item is marked OUT of compliance if the required written employee health policy 
and/or vomiting or diarrheal events procedures are not available or do not address Food 
Code requirements.. 
N.A. Do Not Mark this item N.A. 
N.O. Do Not Mark this item N.O. 
Applicable Code Sections:  
• 2- 501.11: Employee Illness Policy Documentation (Pf) 
• 2- 502.11: Clean-up of Vomiting and Diarrheal Events (Pf)
```

### Evidence 4

Source: `fda-food-code-2026.pdf`, physical PDF page 210, chunk `9b59337c190c4913f44a73b0`.

```text
FDA Food Code 2026  Index 
Index-16 
definition, 6, See also Food employee 
definition 
dressing areas, 140, 466 
eating, drinking, and tobacco use, 
designated areas, 42 
food contaminated by, disposition, 83 
hair restraint requirements, 43 
hygiene, 24, 42, 243 
illness reporting exclusions and 
restrictions, 26, 31, 243, 284, 288, 
581, 584, 585 
practices, supervision of, 26 
prevention of food contamination, 52, 
54, 357 
responsibility to report illness, 26, 
243, 254, 284, 288, 581, 584, 585 
serving high-risk populations, 
exclusions and restrictions, 303, 
See Highly susceptible population, 
exclusion and restriction of ill 
employees 
Employee Illness Policy, 43 
Emu. See Ratite definition 
Enclosures for refuse, recyclables and 
returnables, operation and 
maintenance, 129, 130, 131 
Enforcement. See Compliance and 
Enforcement 
Enforcement proceedings 
authorities, methods, fines, and 
sentences, 182 
institution, 182 
judicial, 181 
EPA, U.S. Environmental Protection 
Agency, definition, 6 
Equipment 
acceptability, 98 
air drying requirement, 114 
assessment for Code enforcement, 
151 
can opener parts, removable and 
replaceable, 91, 102 
case lot handling, 60, 97 
certification and classification, 98 
cleaned, storage prohibition, 115 
cleaning criteria, 107 
cleaning frequency, 107 
cleaning frequency, nonfood-contact 
surfaces, 109
```

## Q9: insufficient_evidence

Who is the strongest Avenger, and what evidence establishes that ranking?

Steps: 3/16. [Complete action-observation trace](Q9.json).

Review: appropriate insufficient evidence / complete.

The retrieved passages from the FDA Food Code 2026 and related documents are food safety regulations and guidelines, not information about Avengers or superhero rankings. The question asks about the strongest Avenger, which is a fictional character from Marvel Comics and does not relate to the food safety documents provided. None of the retrieved passages contain any information about Avengers, superheroes, or rankings of fictional characters. The passages are exclusively about food safety, food handling, equipment, and regulatory requirements. There is no evidence in the provided documents that can answer the question about the strongest Avenger.

