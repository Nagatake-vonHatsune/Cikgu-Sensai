"""Chapter order, component selection and printable lesson plans."""
from pathlib import Path

def add_course(lessons, lesson):
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
    links={2:["Beli buah di pasar"],4:["Jumlah buah","Pesanan buah"],7:["Di, ke and dari"],9:["Di, ke and dari"],10:["Lunch at a Malaysian stall"]}
    prior="Ask what Malay greetings the learner already recognises."
    for i in range(0,len(rows),6):
        title,genre,goal=rows[i].split("|"); notes=rows[i+2].split("|")
        guided=rows[i+4].split("|");task,check=rows[i+5].split("|")
        chapter(title,genre,"Malay","A1" if i//6<9 else "A2",goal,notes,rows[i+1].split("|"),
                [("A   " if k%2==0 else "B   ")+s for k,s in enumerate(rows[i+3].split("|"))],guided[:2],task,check,guided[2],links.get(i//6,[]),prior)
        prior="From the previous chapter: "+goal
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
    titles={l["title"] for l in lessons}
    assert all(t in titles for group in groups for t in group["items"])
    assert titles=={t for group in groups for t in group["items"]}
    return groups
