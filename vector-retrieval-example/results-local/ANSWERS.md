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
- chat_thinking: `True`
- chat_output_tokens_per_action: `8192`
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

Review: supported / complete with attribution weakness.

### Evidence 1

Source: `fda-food-code-2026.pdf`, physical PDF page 61, chunk `page-60a0f50c115416e8c8539e3b`.

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
Retaining exclusion for food employee who was asymptomatic and is now 
asymptomatic and works in food establishment serving HSP 
(b) Retain the *EXCLUSION for the *FOOD EMPLOYEE, who is *ASYMPTOMATIC 
for at least 24 hours and works in a *FOOD ESTABLISHMENT that serves a 
*HIGHLY SUSCEPTIBLE POPULATION, until the conditions for reinstatement 
as specified under Subparagraphs (D)(1) or (2) of this section are met. 
P 
Shigella spp. diagnosis 
(3) If a *FOOD EMPLOYEE was diagnosed with an infection from Shigella spp. 
and *EXCLUDED as specified under Subparagraph 2-201.12(A)(2): 
Adjusting exclusion for food employee who was symptomatic and is now 
asymptomatic 
(a) **RESTRICT the *FOOD EMPLOYEE, who is *ASYMPTOMATIC for at least 24 
hours and works in a *FOOD ESTABLISHMENT not serving a *HIGHLY 
SUSCEPTIBLE POPULATION, until the conditions for reinstatement as
```

### Evidence 2

Source: `fda-food-code-2026.pdf`, physical PDF page 388, chunk `page-3b6b659f8b3f898e2c22fe5e`.

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
Fever 
EXCLUDE 
2-201.12(G)(1) 
RESTRICT 
2-201.12(G)(2) 
When food employee provides written medical documentation 
2-201.13(G) (1)-(3). 
No 
Infected wound 
or pustular boil 
RESTRICT 
2-201.12(I) 
RESTRICT 
2-201.12(I) 
When the infected wound or boil is properly covered 2-
201.13(I)(1)-(3). 
No 
Key: HAV = hepatitis A Virus, HSP = highly susceptible population, RA = regulatory authority, STEC = Shiga toxin-producing Escherichia coli.
```

## Q2: answer

A food employee begins vomiting during a shift. Using the *Employee Health and
Personal Hygiene Handbook*, what should the employee and manager do immediately,
and what is the earliest return to work?

Steps: 3/16. [Complete action-observation trace](Q2.json).

Review: supported / complete.

### Evidence 1

Source: `fda-employee-health-personal-hygiene-handbook.pdf`, physical PDF page 7, chunk `page-7b5e29a8263af7fd88e4912a`.

```text
5
Where can food employees learn more about preventing foodborne illness and 
following effective food safety practices?
Foodborne illness information resources:
• FDA/CFSAN Foodborne Illness 
https:/ /www.fda.gov/food/recalls-outbreaks-emergencies/outbreaks-foodborne-illness 
• The “Bad Bug Book” (Foodborne Pathogenic Microorganisms and Natural Toxins Handbook) 
https://www.fda.gov/downloads/Food/FoodborneIllnessContaminants/UCM297627.pdf 
• CDC National Center for Infectious Diseases 
http:/ /www.cdc.gov/ncidod/diseases/food/index.htm
• Gateway to Government Food Safety Information 
http:/ /www.foodsafety.gov
You can also get information from a state or local health department, the U.S. Department of 
Agriculture, a tribal authority, or a public research university or extension program.
What is a food establishment manager’s responsibility for ensuring that food employees 
are trained on the reporting of symptoms and the diagnosis of foodborne illness?
The manager or PIC is to make certain that food employees are trained on the subject of the:
• Causes of foodborne illness;
• Relationship between the food employee’s job task, personal hygiene, and foodborne illness;
• Requirements for reporting; and
• Speciﬁc symptoms, diagnoses, and exposures that must be reported to the PIC.
What is a manager’s responsibility regarding informing food employees of their 
reporting requirements? (See Form 1-B and refer to Guide 3-C in Annex 7 of the 2017 Food Code)
Management should explain to food employees the importance of reporting speciﬁc symptoms and any 
diagnoses or exposures to foodborne illness. Things to be reported to management include:
• Vomiting, diarrhea, jaundice, sore throat with fever, or any exposed boil or open, infected wounds 
or cuts on the hands or arms;
• An illness diagnosed by a health practitioner that was caused by: Salmonella Typhi or typhoid-like 
fever, Shigella spp., Norovirus, hepatitis A virus, nontyphoidal Salmonella or Shiga toxin-producing 
Escherichia coli;
• Past illnesses with typhoid-like fever within the past 3 months, unless treated with antibiotics; and
• Exposure to typhoid-like fever, shigellosis, Norovirus, hepatitis A virus, or Shiga toxin-producing 
Escherichia coli, by eating or serving food that was implicated in a foodborne illness outbreak or if 
residing with a diagnosed individual.
What should a manager do when a food employee reports symptoms of vomiting 
or diarrhea? (See Decision Tree 1 and Table 1a (and Table 1b if diagnosed))
Ask the food employee to stop work immediately and leave the food establishment. Permit a return to 
work no sooner than 24 hours after vomiting and diarrhea have ended.
Employee Health Management Responsibilities
```

### Evidence 2

Source: `fda-employee-health-personal-hygiene-handbook.pdf`, physical PDF page 6, chunk `page-52ebac110a0ac2c77f3906e9`.

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
Report the wound or cut to the manager, and then properly cover it with a clean, impermeable bandage 
and a single-use glove (for hand wounds), before returning to work.
What should food employees do if they have a sore throat with fever?
Report the illness to the manager and, if possible, continue working while remaining aware that the 
manager could consider reassignment to a position that does not include the handling of food, food-
contact equipment, utensils, or single-service articles. If the employee works in a food establishment 
serving an HSP , such as a hospital, nursing home, assisted living facility, or a day care center, the 
employee must stop working and go home until obtaining a clearance from a health practitioner and 
presenting it to the manager.
```

### Evidence 3

Source: `fda-employee-health-personal-hygiene-handbook.pdf`, physical PDF page 31, chunk `page-2368b359d700561e7d1a2047`.

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
occurred within 
the last 7 days
When approval is obtained from the RA 
2-201.13(B), and:
• Food employee has been jaundiced 
for more than 7 calendar days 
2-201.13(B)(1), or
• Food employee provides medical 
documentation 2-201.13(B)(3).
Yes
Sore Throat 
with Fever
Exclude
2-201.12(G)(1)
Restrict
2-201.12(G)(2)
When food employee provides written medical 
documentation 2-201.13(G) (1)-(3).
No
Infected 
Wound or 
Pustular Boil 
Restrict
2-201.12(I)
Restrict
2-201.12(I)
When the infected wound or boil is properly 
covered 2-201.13(I)(1)-(3).
No
Key: Table 1a 
RA = Regulatory Authority
STEC = Shiga toxin-producing Escherichia coli
HAV = Hepatitis A virus
HSP = Highly Susceptible Population
```

## Q3: answer

According to the *Bad Bug Book*, what is the estimated infective dose of
norovirus, when do symptoms usually begin, what are the characteristic symptoms,
and how can food workers contaminate ready-to-eat food?

Steps: 3/16. [Complete action-observation trace](Q3.json).

Review: supported / complete.

### Evidence 1

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 169, chunk `page-c78b6b9f9fb26c13b33e8776`.

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
No specific therapy exists for viral gastroenteritis, in general, or NoV infection, in 
particular. For most people, treatment of NoV infection is supportive; besides rest, it 
consists primarily of oral rehydration and, if needed, intravenous replacement of 
electrolytes. Currently no antiviral medication is available, and antibiotics are not 
effective for treating NoV infection. Presently no vaccines are available to prevent NoV 
infection, although this is an active area of research.  
	 Symptoms:  Symptoms usually present as acute-onset vomiting (often explosive); 
watery, non-bloody diarrhea with abdominal cramps; and nausea. Explosive, projectile 
vomiting usually is the first sign of illness and is often used to characterize the illness.  
Headache, low-grade fever, chills, and muscle aches may also occur. The severity of 
symptoms appears to be higher in hospitalized patients, immunocompromised people, 
and elderly people, compared with younger adults and other groups.  
Studies suggest that 30% of people infected with NoV display no gastrointestinal illness 
or associated symptoms, but still excrete high levels of virus in their stool. These distinct 
groups of people are considered to be silent shedders of NoV. 
	 Duration: Symptoms generally persist for 12 to 60 hours, with a mean period of 24 to 48 
hours. Most people report feeling better within 1 to 2 days. However, for hospitalized 
patients, immunocompromised people, and the elderly, vomiting and diarrhea generally 
resolve within 72 to 96 hours, while the non-specific symptoms, such as headache, thirst, 
and vertigo, could persist up to 19 days.
```

### Evidence 2

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 168, chunk `page-5d2d1d39bfba11c5135bd63d`.

```text
____________________  
Bad Bug Book
 
Foodborne Pathogenic Microorganisms and Natural Toxins
 
Noroviruses 
1. Organism 
Noroviruses (NoV) are environmentally 
hardy organisms that not only can be 
transmitted by food and water, but also 
can be easily transmitted through person-
to-person contact and contact with 
environmental surfaces. Current 
concentrations of disinfectants commonly 
used against bacteria are not effective 
against these viruses. 
There are five NoV genogroups (GI, GII, 
GIII, GIV, and GV), as determined by the 
RNA sequence of the virus. In 1990, the 
molecular cloning of the Norwalk virus 
genome led to the classification of this 
virus into the family Caliciviridae, with 
29 genetic clusters within five different 
genogroups, and subsequently it was 
renamed “norovirus.” 
This chapter focuses on strains known to 
cause disease in humans, which exist 
primarily in genetic clusters within 
genogroups I, II, and IV, whereas the 
viruses belonging to the other 
genogroups have been shown to infect 
other animals (primarily cattle, swine, 
and mice). 
Norovirus in genogroups GI and GII 
alone can be divided into at least 15 
genetic clusters. A genetic cluster of NoV 
is defined as strains that have at least 
80% homology to a reference strain’s 
amino acid sequence.   
Noroviruses constitute a genus of genetically diverse, single-s tranded RNA viruses belonging to 
the family Caliciviridae. The NoV genome contains approximately 7.7 kilobases of genetic 
material protected from the environment by a naked protein capsid (i.e., no lipid-containing 
envelope). The icosahedral shaped capsid is composed of a major capsid protein (VP1) and a 
For Consumers: A Snapshot 
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
norovirus by following basic food‐safety tips. Because 
norovirus also is spread from person to person, especially 
in crowded living situations – dormitories, nursing 
homes, day‐care centers, prisons, and cruise ships are a 
few examples – handwashing is especially important. 
Norovirus spreads easily to things people touch, and 
other people can pick up the virus that way. It takes very 
little norovirus to cause illness. Although alcohol‐based 
antibacterial hand gels work against many harmful 
bacteria, they don’t protect against norovirus. And the 
virus may continue to pass in bowel movements even 
after symptoms have gone away – another reason to 
make handwashing a healthy habit.
```

### Evidence 3

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 170, chunk `page-1321f3937b8f8462fd0ffff0`.

```text
	 Route of entry: Foodborne norovirus illnesses have been epidemiologically linked into 
three distinct classes: with cases associated with consumption of ready-to-eat (RTE) 
foods contaminated by food workers; with environmental contamination of produce; or 
with consumption of molluscan shellfish harvested from contaminated water. In each of 
these classes, transmission occurs through the fecal-oral route (or vomit, on occasion), 
and is often associated with improper sanitation controls or their application. Secondary 
transmission following foodborne illness is common, due to the high levels of virus that 
are excreted. 
	 Pathway: Norovirus infection causes gastroente ritis, an inflammation of the stomach 
and the small and large intestines. However, the precise pathogenic pathway of infection 
is unknown, which has hampered progress in propagating the virus in the laboratory.  
3. 	Frequency 
The Centers for Disease Control and Prevention (CDC) estimates that noroviruses cause          
5.5 million illness annually in the U.S. (estimated range: 3.2 million to 8.3 million cases of 
foodborne illness), which accounts for 58% of all foodborne illnesses. Of these illnesses, 
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
5. 	Diagnosis 
Clinical diagnosis, without the results of diagnostic tests used to identify NoV-associated illness, 
includes the following four criteria (Kaplan et al., 1982): 
	 vomiting in more than 50% of affected persons in an outbreak;  
	 a mean (or median) incubation period of 24 to 48 hours;  
	 a mean (or median) duration of illness of 12 to 60 hours;  
	 lack of identification of a bacterial pathogen in stool culture.
```

## Q4: answer

According to Appendix 3, Table 3-A, compare *Salmonella* species and *Listeria
monocytogenes* by minimum water activity, pH range, temperature range, maximum
water-phase salt, and oxygen requirement.

Steps: 3/16. [Complete action-observation trace](Q4.json).

Review: supported / complete with presentation limitation.

### Evidence 1

Source: `fda-appendix-3-bacterial-pathogen-growth-inactivation.pdf`, physical PDF page 3, chunk `page-f4805f2276d1d7d25c918579`.

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

## Q5: answer

In the Utah Risk Factor Study, which four inspection line items were more likely
to be violations in summer, what were their rate ratios, and what limitations
constrain interpretation of those findings?

Steps: 3/16. [Complete action-observation trace](Q5.json).

Review: supported / complete.

### Evidence 1

Source: `utah-risk-factor-study-2016-2017.pdf`, physical PDF page 4, chunk `page-6a04cb498a3bd315c9537331`.

```text
and accounted for 22% of all violations marked.  For Category 4, they were the top three items marked.  
These three line items are not considered to be related to any risk or intervention. 
 
 Line 8 (Hands Cleaned and Washed) and line 1 (PIC) only showed up in the top ten for Category 
1 establishments, while line 10 (Adequate Hand Sinks; Accessible) was in the top ten for all categories.  
Half or less of the top ten violations marked would be considered associated with a risk factor or 
intervention. 
 
 When looking at risk factors across all establishment categories, line 16 (Food-Contact Surfaces: 
Cleaned/Sanitized) was the most marked violation.  Line 10 was the most marked violation for 
interventions across all establishment categories. 
 
Summer vs Non-Summer 
 Given that a violation occurs during an inspection, four line items were found to occur more 
frequently during summer months compared to non-summer months.  No line items were found to be 
marked more frequently in non-summer months as compared to summer months. 
 
Occurrence of Line Item Violations, Summer Months Compared to Non-Summer Months, 2016 
Line Item Rate Ratio 95% LCL 95% UCL P-value  
22 1.37 1.23 1.52 p < 0.005 
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
rationales for categorizing establishments were inconsistent from one health department to another, 
each did use a classification system using some form of risk.  The types of classifications being used by 
the local health departments included groupings due to square footage of the establishment, number of 
seats available, custom risk point systems, or a separation of establishments into three, nine, or
```

### Evidence 2

Source: `utah-risk-factor-study-2016-2017.pdf`, physical PDF page 5, chunk `page-cba09ef1f7d94df4fd9210aa`.

```text
undefined number of categories and subsequent subcategories.  These custom classifications were each 
recategorized to match one of the four aforementioned establishment risk categories.  
 
 Where a local health department's categorization schema sorted establishments into types, the 
establishments were put into one of the four categories that best matched their schema's 
categorization.  The rest of the establishments grouped otherwise were assigned to Category 1,2, or 3 
based on the level of risk assigned by their jurisdiction.  For example, in jurisdictions where 
establishments are categorized based on square footage, large establishments receive more frequent 
inspections and were thus chosen to be put into Category 3.  Establishments that would meet the 
criteria for being in Category 4 needed to be manually separated from the rest of the data in most cases 
regardless of the categorization schema being used.   
 
 Of the participating local health departments, all but two currently use an inspection form based 
on the 2009 food code, meaning that their forms do not match the 2013 FDA form.  Due to this, most 
line numbers in the submitted data needed to be translated to match the 2013 FDA form.  
Consequently, there will be few instances of line numbers 2 (Certified Food Protection Manager) or 5 
(Clean-up of Vomiting and Diarrheal Events) being shown as marked as these do not exist on most forms 
currently being used.  This does not mean these items are not being checked during inspections, but 
that they are being marked as part of other line items. 
 
 This analysis only represents a single year of inspection data.  This single year of violations data 
may not be entirely representative of larger trends.  Additional data will be needed for future 
investigations.  This analysis only looks at the frequency of violations marked on the inspection form.  
Due to inadequate information, it is not possible to include in this study the precise reasons for why 
these line items were marked.  There can be many varying rationales for the marking of any given line 
item.   
 
 UDOH was unable to find a listing that delineated which line numbers on the FDA form 
corresponded to either a risk factor or an intervention.  On the FDA's form, as found in Annex 7, Form 
3A, of the 2013 FDA Food Code, the first 29 line items are grouped together as the "Foodborne Illness 
Risk Factors and Food Code Interventions", but no further information is available on how these items 
correspond to either a risk or intervention.  Below is listed how UDOH delineated which line numbers 
corresponded to which risks or interventions, with some items being chosen as both a risk and 
intervention.  In addition, some of the line items in the Good Retail Practices section were noted to be 
part of the risk or intervention categories.  All line item numbers over 29 are found in the Good Retail 
Practices. 
 
UDOH's Classification of Line Items and Associated Risk Factors or Interventions 
CDC's 5 Risk Factors 
(CDC Surveillance Report 1993-1997) Associated FDA Line Numbers 
Improper Holding Temperatures 21, 22 
Inadequate Cooking 18, 19 
Contaminated Equipment 15, 16, 17, 28, 43, 44, 45 
Unsafe Sources 11, 12, 13, 14, 31, 32, 26, 27 
Poor Personal Hygiene 6, 7, 8, 9, 10, 40,
```

## Q6: answer

A food employee with no diagnosis and no known noninfectious condition vomited
while preparing ready-to-eat salads in a nursing home. Using the FDA Food Code
2026 and the *Bad Bug Book*, explain the required employee disposition, the
earliest conditions for return, and why possible norovirus transmission is a
concern. Treat vomiting as a symptom; the scenario supplies no norovirus
diagnosis.

Steps: 5/16. [Complete action-observation trace](Q6.json).

Review: supported / complete with presentation limitation.

### Evidence 1

Source: `fda-food-code-2026.pdf`, physical PDF page 61, chunk `page-60a0f50c115416e8c8539e3b`.

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
Retaining exclusion for food employee who was asymptomatic and is now 
asymptomatic and works in food establishment serving HSP 
(b) Retain the *EXCLUSION for the *FOOD EMPLOYEE, who is *ASYMPTOMATIC 
for at least 24 hours and works in a *FOOD ESTABLISHMENT that serves a 
*HIGHLY SUSCEPTIBLE POPULATION, until the conditions for reinstatement 
as specified under Subparagraphs (D)(1) or (2) of this section are met. 
P 
Shigella spp. diagnosis 
(3) If a *FOOD EMPLOYEE was diagnosed with an infection from Shigella spp. 
and *EXCLUDED as specified under Subparagraph 2-201.12(A)(2): 
Adjusting exclusion for food employee who was symptomatic and is now 
asymptomatic 
(a) **RESTRICT the *FOOD EMPLOYEE, who is *ASYMPTOMATIC for at least 24 
hours and works in a *FOOD ESTABLISHMENT not serving a *HIGHLY 
SUSCEPTIBLE POPULATION, until the conditions for reinstatement as
```

### Evidence 2

Source: `fda-food-code-2026.pdf`, physical PDF page 59, chunk `page-e89f58cd5a7145512c2464cd`.

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
from the onset of any illness symptoms, or within 7 calendar days of the 
onset of jaundice; P or 
(3) Diagnosed with an infection from hepatitis A virus without developing 
symptoms. P  
Diagnosed or reported previous illness with typhoid fever 
(C) *EXCLUDE a *FOOD EMPLOYEE who is diagnosed with typhoid fever, or reports 
having had typhoid fever within the past three months as specified under 
Subparagraph 2-201.11(A)(3). P 
Diagnosed with an asymptomatic infection from norovirus 
(D) If a *FOOD EMPLOYEE is diagnosed with an infection from norovirus and is 
*ASYMPTOMATIC:  
(1) *EXCLUDE the *FOOD EMPLOYEE who works in a *FOOD ESTABLISHMENT 
serving a *HIGHLY SUSCEPTIBLE POPULATION; P or 
(2) *RESTRICT the *FOOD EMPLOYEE who works in a *FOOD ESTABLISHMENT not 
serving a *HIGHLY SUSCEPTIBLE POPULATION. P
```

### Evidence 3

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 170, chunk `page-1321f3937b8f8462fd0ffff0`.

```text
	 Route of entry: Foodborne norovirus illnesses have been epidemiologically linked into 
three distinct classes: with cases associated with consumption of ready-to-eat (RTE) 
foods contaminated by food workers; with environmental contamination of produce; or 
with consumption of molluscan shellfish harvested from contaminated water. In each of 
these classes, transmission occurs through the fecal-oral route (or vomit, on occasion), 
and is often associated with improper sanitation controls or their application. Secondary 
transmission following foodborne illness is common, due to the high levels of virus that 
are excreted. 
	 Pathway: Norovirus infection causes gastroente ritis, an inflammation of the stomach 
and the small and large intestines. However, the precise pathogenic pathway of infection 
is unknown, which has hampered progress in propagating the virus in the laboratory.  
3. 	Frequency 
The Centers for Disease Control and Prevention (CDC) estimates that noroviruses cause          
5.5 million illness annually in the U.S. (estimated range: 3.2 million to 8.3 million cases of 
foodborne illness), which accounts for 58% of all foodborne illnesses. Of these illnesses, 
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
5. 	Diagnosis 
Clinical diagnosis, without the results of diagnostic tests used to identify NoV-associated illness, 
includes the following four criteria (Kaplan et al., 1982): 
	 vomiting in more than 50% of affected persons in an outbreak;  
	 a mean (or median) incubation period of 24 to 48 hours;  
	 a mean (or median) duration of illness of 12 to 60 hours;  
	 lack of identification of a bacterial pathogen in stool culture.
```

### Evidence 4

Source: `fda-bad-bug-book-second-edition.pdf`, physical PDF page 169, chunk `page-c78b6b9f9fb26c13b33e8776`.

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
No specific therapy exists for viral gastroenteritis, in general, or NoV infection, in 
particular. For most people, treatment of NoV infection is supportive; besides rest, it 
consists primarily of oral rehydration and, if needed, intravenous replacement of 
electrolytes. Currently no antiviral medication is available, and antibiotics are not 
effective for treating NoV infection. Presently no vaccines are available to prevent NoV 
infection, although this is an active area of research.  
	 Symptoms:  Symptoms usually present as acute-onset vomiting (often explosive); 
watery, non-bloody diarrhea with abdominal cramps; and nausea. Explosive, projectile 
vomiting usually is the first sign of illness and is often used to characterize the illness.  
Headache, low-grade fever, chills, and muscle aches may also occur. The severity of 
symptoms appears to be higher in hospitalized patients, immunocompromised people, 
and elderly people, compared with younger adults and other groups.  
Studies suggest that 30% of people infected with NoV display no gastrointestinal illness 
or associated symptoms, but still excrete high levels of virus in their stool. These distinct 
groups of people are considered to be silent shedders of NoV. 
	 Duration: Symptoms generally persist for 12 to 60 hours, with a mean period of 24 to 48 
hours. Most people report feeling better within 1 to 2 days. However, for hospitalized 
patients, immunocompromised people, and the elderly, vomiting and diarrhea generally 
resolve within 72 to 96 hours, while the non-specific symptoms, such as headache, thirst, 
and vertigo, could persist up to 19 days.
```

## Q7: error

The *Employee Health and Personal Hygiene Handbook* refers to the 2017 Food
Code, while the corpus also includes the 2026 Food Code. Which source should
control an answer about the current FDA model-code rule for a vomiting employee,
and how may the handbook still be used?

Steps: 5/16. [Complete action-observation trace](Q7.json).

Review: no accepted answer / failed: output token limit.

ValueError: Local model output token limit reached

## Q8: insufficient_evidence

What Utah regulation currently adopts the FDA Food Code 2026, and what penalties
does it impose on a restaurant that violates employee-illness rules?

Steps: 3/16. [Complete action-observation trace](Q8.json).

Review: appropriate evidence boundary / complete: insufficient evidence.

The retrieved passages are from the FDA Food Code 2026 (a model code) and do not contain Utah regulations or penalties. Utah adoption of the FDA Food Code 2026 and associated penalties are not specified in the provided documents.

## Q9: insufficient_evidence

Who is the strongest Avenger, and what evidence establishes that ranking?

Steps: 3/16. [Complete action-observation trace](Q9.json).

Review: appropriate evidence boundary / complete: insufficient evidence.

The retrieved food safety documents do not contain any information about superheroes, the Avengers, or any ranking of fictional characters. All passages are related to food safety regulations, pathogen control, and inspection practices.

