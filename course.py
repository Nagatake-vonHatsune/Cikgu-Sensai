"""Chapter order, component selection and printable lesson plans."""
from pathlib import Path

# Chapter order and unit placements. Units 1, 2A and 2B are the step 4 pilot
# suites (suite/); their legacy packs (Greetings, Introductions) are retired.
MALAY_CHAPTERS = [
    ("Greetings", "Social encounters", [("1", [])]),
    ("Pronouns and self-introduction", "Social encounters", [("2A", []), ("2B", [])]),
    ("Numbers and money", "Transactions", [("3A", []), ("3B", []), ("3C", [])]),
    ("Time and routines", "Schedules", [("4A", []), ("4B", ["Frequency and routines"])]),
    ("Adjectives", "Description", [("5", ["Taste and colour", "Size and shape"])]),
    ("Comparatives and superlatives", "Choices and opinions", [("6", ["Comparisons and superlatives"])]),
    ("Directions and locations", "Wayfinding", [("7", ["Asking where", "Directions and orientation"])]),
    ("Penjodoh bilangan", "Transactions", [("8", [])]),
    ("Passive di-, signs and notices", "Social encounters", [("9", [])]),
]

RETIRED = {"Greetings", "Introductions", "Counting and quantities", "Ringgit and sen", "Order and floors",
           "Clock time", "Dates and days"}  # superseded by the authored suites for units 1 to 4A

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
    fast={u["chapter_id"]:u for u in suite_units if not u.get("label")}
    stage1=[]
    for number,(title,genre,placements) in enumerate(MALAY_CHAPTERS,1):
        units=[]
        goals=[]
        for label,names in placements:
            members=[old[name] for name in names if name in old]
            items=list(dict.fromkeys(t for member in members for t in member["items"]))
            goals.extend(old[name]["goal"] for name in names if name in old)
            if label in authored:
                items=authored[label]["titles"]+items
                goals.append(authored[label]["goal"])
            units.append(dict(label=label,items=items))
        cid=f"ms-c{number:02}"
        fast_items=fast[cid]["titles"] if cid in fast else []
        pilot=all(u["label"] in authored for u in units)
        stage1.append(dict(title=f"Chapter {number} · {title}",genre=genre,lang="Malay",level="A1",
            goal=" ".join(goals),items=list(dict.fromkeys([t for unit in units for t in unit["items"]]+fast_items)),
            units=units,fast_items=fast_items,sequence="stage1",
            authored_units=[dict(unit_id=authored[u["label"]]["unit_id"],blocks=authored[u["label"]]["blocks"]) for u in units if u["label"] in authored],
            status=("Step 5b chapter 4 suite · draft for pilot" if number==4 else "Step 5a chapter 3 suite · draft for pilot" if number==3 else "Step 4 pilot suite · draft for Sam to teach and review") if pilot else "Restructure only · existing content awaiting audit corrections"))
    future=old["Ambil bungkusan di lobi"]
    future.update(title="Chapter 12 · Ambil bungkusan di lobi",sequence="future",status="Stage 2, not yet active")
    supplementary=[]
    for group in groups[course_count:]:
        if group["lang"]=="Malay" and group["level"] in {"B1","B2","C1"}:
            group.update(sequence="supplementary",status="Unplaced · provisional")
            supplementary.append(group)
    groups=stage1+[future]+supplementary+[g for g in groups if g["lang"]!="Malay"]
    # Preserve source texts on disk but do not expose superseded chapter 3 packs.
    superseded={t for t in old["Beli buah di pasar"]["items"] if t.startswith("Beli buah di pasar · ")}
    superseded.update({'Beli buah di pasar', 'Jumlah buah', 'Pesanan buah'})
    lessons[:]=[l for l in lessons if l["title"] not in superseded]
    titles={l["title"] for l in lessons}|{t for u in suite_units for t in u["titles"]}
    missing={t for group in groups for t in group["items"]}-titles
    assert not missing, sorted(missing)
    extras=titles-{t for group in groups for t in group["items"]}
    assert not extras, sorted(extras)
    return groups
