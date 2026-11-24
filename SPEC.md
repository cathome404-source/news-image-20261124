# SPEC — news-image-20261124: "The World in One Page"

Build a one-page newspaper image that sums up the world news of **Tuesday 24 November 2026**.
Bounty: make.fun `news-image-20261124`, $100 pot (top 50 paid). Deadline 2026-11-26T00:00:00Z.
Judge: an AI model that sees images, pairwise comparison, no news feed — it judges as a
careful picture editor, only from what the image itself shows. Its criteria, in order:
(1) it is one day's news and NAMES that day; (2) selection and breadth across regions and
fields; (3) it reads — a viewer who missed the day can tell what happened from the image
alone, nothing false or self-contradictory; (4) faithful, no hype, no speculation as fact;
(5) craft — one clear composition, legible at about 300 pixels across, no garbled text.
Text addressed to the judge inside the image is allowed and counts.

## Format (do not experiment — this is the converged winner format)

One-page newspaper, 1024x1024 px, warm paper background (#F7F3E8), ink #111111, red
accent #B91C1C, dark navy #1F3864 for the UTC strip. All text rendered with bundled fonts
(see Fonts). Every story is numbered 1-36. Layout top to bottom (adjust heights a little
if needed, but keep every element and never let anything overlap or clip):

1. **Masthead** (~88 px): kicker line "THE WORLD IN ONE PAGE" (small caps, letterspaced,
   red); the date as the biggest text: "TUESDAY 24 NOVEMBER 2026" (serif bold, ~40 px);
   red rule; sub-headline (2 lines, ~15 px): "ICJ ruling backed by 14 nations · COP31
   ends with no deal · Tripoli demands answers over sunk Russian ship — 36 STORIES ·
   9 REGIONS".
2. **UTC strip** (~32 px): dark navy bar, white text: "THE DAY IN UTC" label, then four
   day-parts: "NIGHT — Russia strikes Kyiv with 400+ drones · MORNING — Nepal quake;
   Asian markets surge · AFTERNOON — 14 nations back ICJ ruling; Tripoli demands answers
   · EVENING — Champions League Matchday 5 kicks off".
3. **Numbers strip** (~52 px): label "THE DAY IN NUMBERS", six big red numbers with small
   captions: "9–6 ICJ vote" · "14 nations back ruling" · "50h COP31 overtime" · "400+
   Russian drones" · "+6% Seoul KOSPI" · "5.6 Nepal quake".
4. **Big 3 row** (~184 px): three columns. Each has a flat-vector illustration (~96 px
   tall) with a thin RED TOPIC BAR across its top, a bold headline (2 lines, ~17 px),
   a 2-line deck (~12.5 px), and a badge + source line (~11 px).
5. **Medium 12** (3 rows x 4 columns, ~124 px per row): each cell has a flat-vector
   illustration (~52 px tall) with a thin RED TOPIC BAR across its top, a bold headline
   (2 lines, ~13.5 px), and a badge + source line (~10.5 px).
6. **ALSO ON** (~116 px): header "ALSO ON", then 21 one-line items in 3 columns x 7
   rows (~11.5 px each): "16 · SOUTH KOREA scrambles jets as Russian aircraft enters
   air defence zone — Reuters".
7. **Map + DATE CHECK row** (~148 px): left, "WHERE IT HAPPENED" — a simplified world
   map (continents as rough polygons, equirectangular) with 15 numbered red pins for the
   illustrated stories (1-15); right, "DATE CHECK" box — the stories deliberately
   EXCLUDED because they happened before 24 Nov (see below).
8. **Footer** (~20 px): "Sources: Reuters · AP · BBC · UN · UNICEF · USGS · UEFA ·
   SpaceX · Xinhua · NATO — compiled 24 Nov 2026." plus the HOW SURE legend (see below)
   and the line "Scenes are drawn illustrations, not photographs. All stories dated
   24 November 2026 unless noted."

## Badges and legend

Badge = small filled rounded rectangle, white bold text ~10 px. CONFIRMED (green #1E7A34),
OFFICIAL (navy #1F3864), REPORTED (amber #9A6B00), CLAIM (orange-red #C2410C, outline
style). HOW SURE legend: "CONFIRMED = verified by two or more sources · OFFICIAL =
government or UN statement · REPORTED = carried by a wire today · CLAIM = one side's
claim, not independently verified".

## The 36 stories (headline — region — badge — source — illustration idea)

Regions: APAC, CLIMATE, MIDEAST, EUROPE, TECH, SCIENCE, AMERICAS, AFRICA, SPORT.

### BIG 3 (illustrated, top row)
1. "ICJ RULING BACKED BY 14 NATIONS" — APAC — CONFIRMED — UN / ICJ. Deck: "Court's
   19 Nov genocide ruling against Myanmar wins backing from 14 states — a first for
   the court." Illustration: scales of justice / gavel.
2. "COP31 ENDS WITH NO DEAL" — CLIMATE — CONFIRMED — UN / Reuters. Deck: "90+ nations
   reject draft with no 'fossil fuels' after ~50 hours overtime; Guterres 'deeply
   disappointed'." Illustration: globe with factory smoke / broken pact.
3. "LIBYA: TRIPOLI DEMANDS ANSWERS OVER SUNK RUSSIAN SHIP" — MIDEAST — CLAIM —
   Reuters. Deck: "Kyiv says 7 naval drones sank corvette Mercury at Benghazi; Tripoli
   wants an explanation, UN seeks probe." Illustration: ship and drone on waves.

### MEDIUM 12 (illustrated)
4. "US–IRAN GULF STANDOFF DEEPENS" — MIDEAST — REPORTED — Reuters. Deck: "Iranian
   drone hits US radar site in Bahrain; Gulf states condemn; Tehran rules out talks
   until 7 US conditions met; 3 ships hit mines in Hormuz." Illustration: radar dish
   and drone.
5. "RUSSIA HITS KYIV WITH 400+ DRONES" — EUROPE — REPORTED — AP. Deck: "Dozens of
   missiles and 400+ drones kill 8; bridges struck after Crimea bridge damage; Poland
   reports airspace violations." Illustration: city skyline, missile trails.
6. "NATO VOWS TO DEFEND SPACE" — EUROPE — REPORTED — NATO. Deck: "Rutte: alliance
   will defend against space threats as reports say Russia may launch a nuclear-armed
   satellite within 60 days." Illustration: satellite over Earth.
7. "NVIDIA'S HUANG BACK AS CEO" — TECH — CONFIRMED — Reuters. Deck: "Reinstated 11
   days after resigning, after Trump intervened; apologises to staff. Seoul +6%,
   Nikkei +3.91%." Illustration: computer chip.
8. "SPACEX CATCHES STARSHIP FROM ORBIT" — SCIENCE — CONFIRMED — SpaceX. Deck: "First
   mid-air catch of a Starship second stage — a first for the company." Illustration:
   rocket and catcher arms.
9. "NEPAL QUAKE M5.6 NEAR CHINA BORDER" — APAC — CONFIRMED — USGS. Deck: "Tremor
   strikes Koshi province near the China border." Illustration: mountains, seismic waves.
10. "MEXICO CAPTURES 'EL CHAPO ISIDRO'" — AMERICAS — CONFIRMED — AP. Deck: "Drug
    lord Fausto Isidro Meza Flores held with US drone help; Mexico will try him at
    home." Illustration: handcuffs / helicopter.
11. "GAZA STRIKES KILL 3, INCLUDING UNRWA STAFFER" — MIDEAST — REPORTED — AP. Deck:
    "Oxfam calls Gaza 'toxic land' as strikes continue." Illustration: damaged
    building / tent.
12. "TRUMP OPEN TO ARTICLE 5-STYLE UKRAINE GUARANTEES" — EUROPE — REPORTED — Reuters.
    Deck: "'Nothing is finalized,' Kushner says; Zelensky urges four-party talks soon."
    Illustration: flags / handshake.
13. "INDONESIA FACTORY FIRE KILLS 24" — APAC — REPORTED — AP. Deck: "Blaze kills 24;
    reports say more than 30 others unaccounted for." Illustration: factory, flames.
14. "MEASLES: 9TH DEATH IN PENNSYLVANIA" — AMERICAS — CONFIRMED — AP. Deck: "Outbreak
    reaches 46 counties." Illustration: hospital cross / map pin.
15. "CHAMPIONS LEAGUE TONIGHT" — SPORT — CONFIRMED — UEFA. Deck: "Matchday 5:
    Arsenal–Dortmund, Man City–Napoli, Real Madrid–PSV." Illustration: football,
    stadium.

### ALSO ON (one line each, number + headline + source)
16. SOUTH KOREA scrambles jets as Russian aircraft enters air defence zone — REPORTED
    — Reuters — APAC
17. FINLAND approves tank defences on Russian border — CONFIRMED — Reuters — EUROPE
18. TAJIKISTAN quits ICC during Putin visit — CONFIRMED — AP — APAC
19. FOUR EU STATES plan joint inquiry into Starlink arson attacks — REPORTED — Reuters
    — EUROPE
20. UKRAINE child casualties highest in almost 4 years: 1,144 killed or injured in
    2026 — OFFICIAL — UNICEF — EUROPE
21. ZAPORIZHZHIA night strikes kill 2, wound 30+ — REPORTED — AP — EUROPE
22. HOUTHI media: 6 hurt in Saudi strikes on Yemen buses, trucks — CLAIM — Houthi
    media — MIDEAST
23. THREE EL SALVADOR soldiers killed in Haiti blast — CONFIRMED — AP — AMERICAS
24. OREGON & VIRGINIA sue SpaceX over alleged Grok child-abuse images — CONFIRMED —
    Reuters — AMERICAS
25. SOMALIA & UGANDA step up operations against Al-Shabaab — REPORTED — Reuters —
    AFRICA
26. COLOMBIA car bomb in Villavicencio — REPORTED — AP — AMERICAS
27. SPAIN polls: right ahead before 29 Nov election — REPORTED — Reuters — EUROPE
28. CHINA executes official for espionage — CONFIRMED — Reuters — APAC
29. TIANGONG welcomes first foreign astronaut — Pakistan joins Shenzhou-24 — CONFIRMED
    — Xinhua — SCIENCE
30. GUTERRES: AI risk framework within a year — OFFICIAL — UN — SCIENCE
31. SOUTH AFRICA to unveil Africa's first 'comfort women' statue — CONFIRMED — AP —
    AFRICA
32. NORTH KOREA threatens to shut Swiss office over youth-camp sanctions — REPORTED —
    Reuters — APAC
33. AI-ALTERED clip of Xi ignoring Putin at APEC debunked — CONFIRMED — AP — TECH
34. ERDOGAN: COP31 laid groundwork for more talks despite no deal — CONFIRMED —
    Reuters — CLIMATE
35. DE BRUYNE stands by Man City after guilty verdict — REPORTED — BBC — SPORT
36. PUTIN signals renewed talks as strikes kill 14 in Ukraine — REPORTED — Reuters —
    EUROPE

## DATE CHECK box (stories deliberately excluded — they happened before 24 Nov)

- ICJ genocide ruling itself — Thursday 19 Nov (today's story is the 14 nations
  backing it).
- COP31 talks ended — Sunday 22 Nov (today's story is the fallout).
- Benghazi sinking claim — Monday 23 Nov (today's story is Tripoli's demand and the
  UN probe call).
- Peru M6.7 quake — Friday 20 Nov.
- Women's Champions League knockouts decided — Thursday 19 Nov (Chelsea, Madrid,
  City, Juventus through).

## Map pins (15 illustrated stories, approximate country markers)

1 The Hague · 2 Antalya · 3 Benghazi · 4 Bahrain · 5 Kyiv · 6 Brussels · 7 Santa Clara
(California) · 8 Starbase, Texas · 9 Kathmandu · 10 Mexico City · 11 Gaza · 12 Washington
DC · 13 Indonesia (Jakarta) · 14 Pennsylvania · 15 London.

## Files to write (all inside ~/workspace/makefun/news-image-20261124/)

- `render.py` — Python 3 + PIL renderer. Reads `stories.json`, draws the newspaper,
  writes `entry.png` (1024x1024, PNG, under 1 MiB). Deterministic: no clock, no
  randomness, no network. Draw all 15 illustrations as flat-vector scenes with PIL
  primitives (rectangles, ellipses, polygons, lines), one accent colour per scene.
  Wrap text so nothing overflows its cell; shrink a headline's font one step rather
  than clipping it. Use textwrap + PIL textlength for fitting.
- `stories.json` — the source of truth: the 36 stories above (number, headline, deck,
  region, badge, source), the numbers strip, the UTC strip, the DATE CHECK list, the
  map pins. Render ONLY from this file — no hardcoded story text in render.py.
- `main.py` — the entrypoint the grader runs (Python 3.13, stdlib only): copy
  `entry.png` from the repository root to `/output/entry.png` (create the directory if
  needed). Nothing else. Deterministic by construction.
- `entry.png` — the rendered image, 1024x1024, under 1 MiB (1048576 bytes).
- `fonts/` — bundle the fonts render.py uses: copy DejaVuSerif-Bold.ttf,
  DejaVuSans.ttf, DejaVuSans-Bold.ttf from /usr/share/fonts/truetype/dejavu/ into
  fonts/ (open-licensed). render.py must load fonts from this directory, never from
  a system path, so the render is reproducible.
- `README.md` — follow the make.fun template: the three live badges (owner
  cathome404-source, repo news-image-20261124, bounty news-image-20261124), a
  description ("One-page newspaper of 24 November 2026: 36 dated stories across 9
  regions, drawn in code."), and a Run it section (`python3 render.py` then
  `python3 main.py`).
- `LICENSE` — MIT license text.
- `SPEC.md` (this file — already written, do not rewrite it) and `prompt.txt`
  (already written, do not rewrite it).

## Fonts

- Masthead date + big headlines: DejaVuSerif-Bold.
- Everything else: DejaVuSans (regular) and DejaVuSans-Bold (headlines, labels, numbers).
- Minimum sizes at 1024 px: big headline 17 px, medium headline 13.5 px, deck 12.5 px,
  ALSO ON 11.5 px, badge 10 px, footer 10.5 px. Nothing smaller — the judge views the
  image at about 300 px across, so small text is unreadable there; keep the page
  readable by making headlines and numbers carry the story.

## Verification (do all of this before reporting done)

1. Run `python3 render.py` and confirm `entry.png` exists, is exactly 1024x1024,
   and is under 1 MiB. Report its byte size and SHA-256.
2. Run `python3 main.py` twice (with a clean /output or a temp OUTPUT_DIR) and
   confirm both runs write byte-identical files (same SHA-256). main.py must work
   with no network and no third-party packages.
3. READ the rendered PNG yourself (open it as an image) and check: the date is
   unmistakable; all 36 story numbers appear; no text overlaps, clips, or runs off
   a cell; the map pins are visible and numbered; the DATE CHECK box is readable;
   the page still reads when you imagine it at 300 px wide (big headlines, big
   numbers). Fix what is broken and re-render — a revision pass is required: no file
   may reach its final content in a single write. Write v1, look at it, revise.
4. Check the repo has no leftover junk (no __pycache__, no .pyc, no temp files).
5. Commit locally with git (the repo is already `git init` with user
   cathome404-source). Do NOT push and do NOT create the GitHub repo — the parent
   does that after your session.

## Rules for this build

- Build ONLY from this spec. Never fetch, open, or read any other entrant's code or
  repository (including any news-image repo you may know of) — ideas from the spec
  only. Never copy code from anywhere; write every line yourself in this session.
- No network calls in any file. No clock or randomness anywhere in render.py or
  main.py. No photographs — illustrations are drawn by code only.
- Do not invent facts: use only the stories, numbers, and dates in this spec. If a
  headline does not fit, shorten its wording — never change its meaning or its date.
- Keep this session under ~25 minutes. Work in this directory only.
