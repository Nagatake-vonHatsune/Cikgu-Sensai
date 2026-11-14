"""Chapter order, component selection and printable lesson plans."""
from pathlib import Path

# Chapter order and unit placements. Units 1, 2A and 2B are the step 4 pilot
# suites (suite/); their legacy packs (Greetings, Introductions) are retired.
MALAY_CHAPTERS = [
    ("Greetings", "Social encounters", [("1", [])]),
    ("Pronouns and self-introduction", "Social encounters", [("2A", []), ("2B", [])]),
    ("Numbers and money", "Transactions", [("3A", []), ("3B", []), ("3C", [])]),
    ("Time and routines", "Schedules", [("4A", []), ("4B", [])]),
    ("Adjectives", "Description", [("5", [])]),
    ("Comparatives and superlatives", "Choices and opinions", [("6", [])]),
    ("Directions and locations", "Wayfinding", [("7", [])]),
    ("Penjodoh bilangan", "Transactions", [("8", [])]),
    ("Passive di-, signs and notices", "Social encounters", [("9", [])]),
    # Stage 2 (A2), built chapter by chapter from build step 4 (13 Nov 2026).
    ("ber- verbs", "Daily routines", [("10A", []), ("10B", [])]),
    ("meN- verbs", "Work", [("11A", []), ("11B", [])]),
    ("-kan and -i verbs", "Housing", [("12A", []), ("12B", [])]),
    ("Health: may, need, should", "Health", [("13", [])]),
    ("Reasons, conditions and plans", "Plans", [("14", [])]),
    ("Describing things and people", "Lost property", [("15", [])]),
    ("Accidents with ter-", "Accidents", [("16", [])]),
    ("Spoken Malay and invitations", "Invitations", [("17", [])]),
    ("Stage 2 review and A2 check", "Review", [("18", [])]),
]
STAGE1_CHAPTERS = 9  # chapters 1 to 9 are Stage 1 (A1); chapter 10 onward is Stage 2 (A2)

RETIRED = {"Greetings", "Introductions", "Counting and quantities", "Ringgit and sen", "Order and floors",
           "Clock time", "Dates and days", "Frequency and routines", "Taste and colour", "Size and shape", "Comparisons and superlatives", "Asking where", "Directions and orientation"}  # superseded by the authored suites for units 1 to 7

AUTHORED_LINKS = {"5": ["Lunch at a Malaysian stall"]}

def add_course(lessons, lesson, suite_units=()):
    folder=Path(__file__).with_name("curriculum")
    groups=[]
    def chapter(title, genre, lang, level, goal, notes, words, dialogue, guide, task, check, key, related, recall):
        lesson(title+" · Learner pack",lang,level,"Chapter pack",notes,[
            ("Words and phrases",words),
            ("Model · Read in pairs",dialogue),
            ("Guided practice",guide+["________________________________"]),
            ("Use it independently",[task,check,"________________________________","________________________________"])],
            [key,"Check the result with the listener. Accept equivalent language that achieves the goal."])
        starter=lessons[-1]["title"]
        lesson(title+" · Teaching plan",lang,level,"Lesson plan",notes,[
            ("Schedule · 45-minute core",[
                "Outcome: "+goal,"0–5 min · Recall: "+recall,
                "5–15 min · Model the first exchange aloud. Learner listens once, then identifies the useful phrases.",
                "15–25 min · Rehearse in pairs, cover selected turns, then use the guided exercise.",
                "25–40 min · "+task,"40–45 min · "+check]),
            ("Split across classes",["Class 1 · Use the vocabulary, model and guided practice. Finish with one unaided exchange.",
                "Class 2 · Begin without notes. Switch roles and change one fact. "+check,
                "Extension · Choose a linked worksheet if available. Use its full conversation, grammar or writing stages in another class.",
                "Next meeting · Ask for the same language in a different setting before showing the answer."])],
            [key,"Observe whether the recipient understood. For a one-to-one class the teacher plays the other role."])
        groups.append(dict(title=title,genre=genre,lang=lang,level=level,goal=goal,items=[starter,lessons[-1]["title"],*related]))
    rows=(folder/"malay-course.txt").read_text().splitlines()
    links={"Asking where":["Di, ke and dari"],"Directions and orientation":["Di, ke and dari"],"Taste and colour":["Lunch at a Malaysian stall"]}
    prior="Ask what Malay greetings the learner already recognises."
    for i in range(0,len(rows),6):
        title,genre,goal=rows[i].split("|"); notes=rows[i+2].split("|")
        guided=rows[i+4].split("|");task,check=rows[i+5].split("|")
        if title in RETIRED:
            prior="From the previous resource: "+goal
            continue
        chapter(title,genre,"Malay","A1",goal,notes,rows[i+1].split("|"),
                [("A   " if k%2==0 else "B   ")+s for k,s in enumerate(rows[i+3].split("|"))],guided[:2],task,check,guided[2],links.get(title,[]),prior)
        prior="From the previous resource: "+goal
    course_count=len(groups)
    features=[
      ("Transactions","epal · apple / りんご|sebiji · one item / 一個|harga · price / 値段|baki · change / お釣り"),
      ("Wayfinding","gate · pintu / 門|beside · di sebelah / 〜のそば|turn right · belok kanan / 右に曲がる"),
      ("Wayfinding","教室（きょうしつ）· classroom / bilik darjah|階段（かいだん）· stairs / tangga|となり · next to / sebelah"),
      ("Housing","bungkusan · parcel / 小包|unit · apartment unit / 住戸|dah sampai · has arrived / 届いた"),
      ("Study","borrow · pinjam daripada / 借りる|lend · beri pinjam / 貸す|due · perlu dipulangkan / 返却期限"),
      ("Dining","予約（よやく）· booking / tempahan|満席（まんせき）· fully booked / penuh|窓（まど）· window / tingkap"),
      ("Work","giliran · turn or shift / 当番|ganti · replace / 代わる|penyelia · supervisor / 監督者"),
      ("Study","rehearsal · latihan / リハーサル|figures · angka / 数値|fallback · pilihan kedua / 代案"),
      ("Study","発表（はっぴょう）· presentation / pembentangan|担当（たんとう）· responsibility / tugas|締め切り · deadline / tarikh akhir"),
      ("Work","step-free access · laluan tanpa tangga / 段差のない経路|reserve · tempah / 予約する|provided that · asalkan / 〜を条件に"),
      ("Housing","bekalan · supply / 供給|anggaran · estimate / 見込み|agihan · distribution / 配分"),
      ("Work","定員（ていいん）· capacity / kapasiti|実習（じっしゅう）· hands-on practice / latihan amali|調整中 · being arranged / sedang diatur"),
      ("Governance","reservation · concern / keberatan / 留保|scope · skop / 範囲|subject to review · tertakluk pada semakan / 見直しを条件に"),
      ("Campus services","dapatan · findings / 調査結果|peruntukan · allocation / 予算枠|tertakluk pada · subject to / 〜を条件に"),
      ("Campus services","意向（いこう）· preference / hasrat|試行（しこう）· trial / percubaan|恒久化（こうきゅうか）· permanent adoption / pelaksanaan tetap")
    ]
    batch=lessons[10:55]
    # The existing bank stores advanced families before foundation families.
    families=[batch[n:n+3] for n in range(0,len(batch),3)]
    families=families[6:]+families[:6]
    extra={"Meet at a campus gate":["Finding the right platform"],"Beli buah di pasar":["Lunch at a Malaysian stall"],"Ambil bungkusan di lobi":["A clear pickup message"],"Plan a group presentation":["Set a new meeting time","Plans and arrangements","Request figures by Thursday"],"教室を探す":["Where things are · に and で","Meeting at the station"],"発表の役割を調整する":["Tell a colleague you will be late"]}
    for family,(genre,lex) in zip(families,features,strict=True):
        conv,gram,writing=family; title=conv["title"]; pp=conv["pages"]; g=gram["pages"]
        chapter(title,genre,conv["lang"],conv["level"],pp[-4]["lines"][1], [p["lines"][0] for p in pp[:3]],lex.split("|"),pp[3]["lines"][:4],g[4]["lines"][:2],pp[-4]["lines"][1],pp[-2]["lines"][0],g[-1]["lines"][0],[w["title"] for w in family]+extra.get(title,[]),"Describe a similar situation and recall two expressions.")
    # Keep every existing worksheet and its wording; only regroup the menu.
    old={g["title"]:g for g in groups}
    authored={u["label"]:u for u in suite_units if u.get("label")}
    fast={u["chapter_id"]:u for u in suite_units if not u.get("label") and not u.get("stage")}
    # The stage review and the A1 stage test (step 5h) close Stage 1; they are listed with chapter 9, after unit 9.
    # The A2 stage test (build step 5) closes Stage 2; it is listed with chapter 18, after unit 18.
    stage={u["chapter_id"]:u["titles"] for u in suite_units if u.get("stage")}
    stage1=[]
    for number,(title,genre,placements) in enumerate(MALAY_CHAPTERS,1):
        units=[]
        goals=[]
        for label,names in placements:
            members=[old[name] for name in names if name in old]
            items=list(dict.fromkeys(t for member in members for t in member["items"]))
            goals.extend(old[name]["goal"] for name in names if name in old)
            if label in authored:
                # The A2 stall conversation stays linked from chapter 5 after its legacy taste pack was retired.
                items=authored[label]["titles"]+items+AUTHORED_LINKS.get(label,[])
                goals.append(authored[label]["goal"])
            units.append(dict(label=label,items=items))
        cid=f"ms-c{number:02}"
        fast_items=fast[cid]["titles"] if cid in fast else []
        stage_items=stage.get(cid,[])
        pilot=all(u["label"] in authored for u in units)
        a2=number>STAGE1_CHAPTERS
        stage1.append(dict(title=f"Chapter {number} · {title}",genre=genre,lang="Malay",level="A2" if a2 else "A1",
            goal=" ".join(goals),items=list(dict.fromkeys([t for unit in units for t in unit["items"]]+fast_items+stage_items)),
            units=units,fast_items=fast_items,stage_items=stage_items,sequence="stage2" if a2 else "stage1",
            authored_units=[dict(unit_id=authored[u["label"]]["unit_id"],blocks=authored[u["label"]]["blocks"]) for u in units if u["label"] in authored],
            status=("Stage 2 build step 5 chapter 18: review, rehearsal and the A2 stage test · draft for Claude's review" if number==18 else "Stage 2 build step 4 chapter 17 suite · draft for Claude's review" if number==17 else "Stage 2 build step 4 chapter 16 suite · draft for Claude's review" if number==16 else "Stage 2 build step 4 chapter 15 suite · draft for Claude's review" if number==15 else "Stage 2 build step 4 chapter 14 suite · draft for Claude's review" if number==14 else "Stage 2 build step 4 chapter 13 suite · draft for Claude's review" if number==13 else "Stage 2 build step 4 chapter 12 suite · draft for Claude's review" if number==12 else "Stage 2 build step 4 chapter 11 suite · draft for Claude's review" if number==11 else "Stage 2 build step 4 chapter 10 suite · draft for Claude's review" if number==10 else "Step 5g chapter 9 suite · draft for pilot" if number==9 else "Step 5f chapter 8 suite · draft for pilot" if number==8 else "Step 5e chapter 7 suite · draft for pilot" if number==7 else "Step 5d chapter 6 suite · draft for pilot" if number==6 else "Step 5c chapter 5 suite · draft for pilot" if number==5 else "Step 5b chapter 4 suite · draft for pilot" if number==4 else "Step 5a chapter 3 suite · draft for pilot" if number==3 else "Step 4 pilot suite · draft for Sam to teach and review") if pilot else "Restructure only · existing content awaiting audit corrections"))
    # The old chapter 12 placeholder "Ambil bungkusan di lobi" is retired (Sam, 13 Nov 2026): units 12A and 12B replace it.
    retired_placeholder=set(old["Ambil bungkusan di lobi"]["items"])
    supplementary=[]
    for group in groups[course_count:]:
        if group["lang"]=="Malay" and group["level"] in {"B1","B2","C1"}:
            group.update(sequence="supplementary",status="Unplaced · provisional")
            supplementary.append(group)
    groups=stage1+supplementary+[g for g in groups if g["lang"]!="Malay"]
    # Preserve source texts on disk but do not expose superseded chapter 3 packs.
    superseded={t for t in old["Beli buah di pasar"]["items"] if t.startswith("Beli buah di pasar · ")}
    superseded.update(retired_placeholder)
    superseded.update({'Beli buah di pasar', 'Jumlah buah', 'Pesanan buah', 'Di, ke and dari'})  # the last is superseded by unit 7 patterns 1 and 2
    lessons[:]=[l for l in lessons if l["title"] not in superseded]
    titles={l["title"] for l in lessons}|{t for u in suite_units for t in u["titles"]}
    missing={t for group in groups for t in group["items"]}-titles
    assert not missing, sorted(missing)
    extras=titles-{t for group in groups for t in group["items"]}
    assert not extras, sorted(extras)
    return groups
