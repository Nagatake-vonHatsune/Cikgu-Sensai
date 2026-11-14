"""Build the offline page bank. Run with Python and PyMuPDF."""
from pathlib import Path
import json, base64, html, fitz
root=Path(__file__).parent
lessons=[]
def lesson(title,lang,level,kind,notes,pages,key):
    pages=[(label,[body]) for label,body in zip(["日本語","Bahasa Melayu","English"],notes)]+pages+[("Teacher key",key)]
    lessons.append(dict(title=title,lang=lang,level=level,kind=kind,pages=[dict(label=l,lines=s) for l,s in pages]))
lesson("Di, ke and dari","Malay","A1","Grammar",["di は場所、ke は行き先、dari は出発点を表します。駅名の前に置きます。","Di: tempat sekarang. Ke: tempat kita pergi. Dari: tempat kita mula.","Use di for location, ke for destination and dari for starting point."],[("1 · Notice",["Saya di KL Sentral.","Saya nak pergi ke Pasar Seni.","Saya naik tren dari KL Sentral.","Cari nama tempat. Di mana saya sekarang?"]),("2 · Choose",["Pilih: di / ke / dari.","Saya sekarang ____ rumah.","Saya nak pergi ____ kelas.","Saya naik bas ____ rumah ke kampus."]),("3 · Make your own",["Anda di stesen. Pilih tempat yang anda nak pergi.","Beritahu kawan: anda di mana? Nak pergi ke mana? Dari mana?","________________________________","________________________________"])],["Stage 2: di / ke / dari.","Accept equivalent descriptions with different places. Check that direction and starting point are clear."])
lesson("Plans and arrangements","English","B1","Grammar",["その場の決定には will、前からの意図には going to、約束済みの予定には現在進行形が使えます。文脈によって複数の表現が可能です。","Guna will untuk keputusan spontan, going to untuk niat, dan present continuous untuk janji yang sudah diatur. Lihat konteks.","Use will for a decision made now, going to for an intention, and the present continuous for an arrangement. Context can allow more than one form."],[("1 · Notice",["The phone rings: “I’ll answer it.”","You have a plan: “I’m going to call the clinic.”","The clinic has confirmed: “I’m seeing the dentist on Friday.”","Which sentence suggests another person knows about the plan?"]),("2 · Choose",["The receptionist offers 3 pm. Decide now: “Thanks, I ____ take it.”","Tell your friend about the confirmed booking: “I ____ seeing the dentist at three.”","Explain how the situation changed."]),("3 · Improvise",["Tell a partner about an intention and a fixed appointment.","Your partner asks for help tomorrow. Decide what you can do. Say it aloud.","________________________________","________________________________"])],["Stage 1: the confirmed appointment.","Stage 2: will (or ’ll) / am.","Accept going to for an intended visit when the sentence is reformulated. Ask what the speaker wants to emphasise."])
lesson("A clear pickup message","Malay","A2","Writing",["迎えの依頼では、時刻と場所を伝えます。相手との関係によって頼み方を選びましょう。","Tulis masa dan tempat. Guna “boleh” untuk minta tolong.","Give a time and place. Use boleh to make a request."],[("1 · Compare",["A   Jumpa pukul tiga di pintu A, ya.","B   Boleh ambil saya di pintu A pukul tiga? Terima kasih.","C   Ambil saya dekat sana nanti.","Yang mana sesuai kalau kawan dah tahu rancangan anda? Yang mana jelas untuk minta tolong?"]),("2 · Repair",["Kawan anda tak tahu tempat atau masa. Baiki mesej C.","Tempat: pintu B. Masa: pukul empat petang.","________________________________","________________________________"]),("3 · Write",["Kelas tamat lewat. Minta kawan datang pukul lima. Pilih tempat baru.","Tulis mesej. Tukar dengan kawan. Boleh dia cari anda?","________________________________","________________________________"])],["A confirms an existing plan. B makes a request. C leaves the reader guessing.","Example: Boleh ambil saya di pintu B pukul empat petang?"])
lesson("Request figures by Thursday","English","B1","Writing",["期限、必要な資料、依頼の理由を明確にします。相手が次に何をすればよいか確認しましょう。","Nyatakan bahan yang anda perlu, sebab dan tarikh akhir. Semak sama ada pembaca tahu apa yang perlu dibuat.","Give the item, reason and deadline. Choose a tone that suits the reader."],[("1 · Compare",["A   Please send the sales figures by noon on Thursday for Friday’s report.","B   I’m putting Friday’s report together. Could you send the sales figures by noon on Thursday? Let me know if you need more time.","C   Just following up on those numbers. I need them soon.","Underline the deadline. Which message invites a reply about timing?"]),("2 · Repair",["Rewrite C for a colleague you know well.","Include the sales figures, Thursday at noon, and the purpose.","________________________________","________________________________"]),("3 · Write",["A supplier has the delivery figures you need for a Monday meeting. Choose a realistic deadline.","Write your request. Ask your partner to identify the next action and deadline.","________________________________","________________________________"])],["A and B give a deadline. B explicitly invites a reply. C leaves both the item and timing unclear.","Accept direct or warmer phrasing when the request, purpose and deadline are clear."])
from conversations import scenes, lunch, lunch_gap, train, train_gap, meeting, meeting_gap, jp, jp_gap
def extended(title,language,level,notes,model,guided,roles):
    first,_ = scenes(model)
    second,answers = scenes(guided,True)
    timer = {"Japanese":"3〜5分話しましょう。早く終わったら、条件を一つ変えて相談を続けましょう。","Malay":"Bual selama 3–5 minit. Kalau siap awal, tukar satu pilihan dan tanya lagi.","English":"Talk for 3–5 minutes. If you agree early, change one detail and work out a new plan."}[language]
    cards=[("3 · Role "+letter,[timer,*points,"________________________________","________________________________"]) for letter,points in zip("AB",roles)]
    lesson(title,language,level,"Conversation",notes,first+second+cards,["Guided answers in order: "+" / ".join(answers)+".","Allow equivalent natural answers. For each stage, play all three scenes as one conversation. Aim for 3–5 minutes per pair. If reading ends early, cover the script and negotiate a change before finishing.","Check that both partners ask a question, respond to a new detail and confirm the outcome."])
extended("Lunch at a Malaysian stall","Malay","A2",["「Nak …」で注文します。dah habis は売り切れ、bungkus は持ち帰り。予算を伝え、別の料理や飲み物を相談しましょう。","Nak untuk pesan makanan. Dah habis: tiada lagi. Baki: wang yang dapat balik. Tanya harga dan semak pesanan.","Use nak to order, dah habis for sold out and bungkus for takeaway. Ask about price, choose another dish and check your change."],lunch,lunch_gap,[["Ada RM10. Nak nasi lemak dan air. Tanya apa lagi yang ada dan bandingkan harga.","Kawan tak nak makanan pedas. Tanya pasal sambal. Pesan, semak harga dan cara bayar.","Tiba-tiba kawan nak bungkus. Apa perlu tukar?"],["Nasi lemak dah habis. Nasi ayam RM8, mi goreng RM6, air kosong RM2. Teh ais RM3.","Tanya pasal sambal, ais dan makan sini atau bungkus. Terima tunai atau QR.","Bila pelanggan semak pesanan, satu minuman belum siap. Cari jalan sama-sama."]])
extended("Finding the right platform","English","A1",["Where is …? で場所を聞き、On the left? のように方向を繰り返して確認します。lift はエレベーターです。","Tanya tempat dengan Where is …? Ulang arah untuk semak. Lift ialah lif.","Ask Where is …? Repeat the direction to check it. Ask What time …? for the next train."],train,train_gap,[["You need a ticket to Lake Street. You have two heavy bags. Ask for the platform, price and lift.","You want to arrive by ten. Ask when two trains leave and arrive. Choose one.","You lose sight of the lift. Call back and describe what you see."],["Lake Street: platform four, RM3. The lift is behind the shop. Ask what the traveller can see.","Trains leave at 9:35 and 9:50. The journey takes 15 minutes. Help your partner choose.","The shop is closed. Give a second landmark and check the traveller knows the way."]])
extended("Set a new meeting time","English","B1",["Would … work? で都合を尋ねます。代案とその理由を伝え、誰が何をするか最後に確認しましょう。","Guna Would … work? untuk tanya masa yang sesuai. Bincang pilihan, sebab dan tugas masing-masing.","Use Would … work? to check a suggestion. Compare two options and confirm who will follow up."],meeting,meeting_gap,[["A client needs you on Monday morning. Tuesday after three is possible. Explain why the team needs 45 minutes together.","Your branch manager can only attend online. Ask about the room and equipment. Agree who will send the figures.","A late message moves your client visit. Decide whether to change the plan again."],["Your Monday afternoon is full. Offer Tuesday morning first, then Tuesday at four. Find out why everyone needs to attend.","The small room has no video screen. Offer the training room. Ask for the figures before the meeting.","Confirm the time, who will send the link and who will brief anyone absent."]])
extended("Meeting at the station","Japanese","A2",["待ち合わせ（まちあわせ）：会う時間と場所を決めます。「近くに何がありますか」で目印を聞きます。改札（かいさつ）は駅の出入口にあります。","Gunakan 今、どこですか untuk tanya lokasi. 目印（めじるし） ialah tanda yang mudah dilihat. Semak pintu keluar dan tempat menunggu.","Ask 今、どこですか (Where are you now?) and 近くに何がありますか (What is nearby?). 改札（かいさつ） is a ticket gate. Suggest a landmark and confirm it."],jp,jp_gap,[["東口にいます。友達は別の出口にいます。今いる場所と近くの店を聞いてください。","大きな荷物があります。階段を使わずに会える場所を相談してください。","雨が降ってきました。待つ場所を変えて、服やかばんの色を伝えてください。"],["西口にいます。東口にはパン屋と花屋があります。相手に近くの店を聞いてください。","ベンチは外にあります。店の中でも待てます。相手の荷物について聞いてください。","同じ色のかばんが二つ見えます。別の目印を聞いて、会った後の予定を決めてください。"]])
lesson("Where things are · に and で","Japanese","A1","Grammar",["「に」は人や物がある場所、「で」は何かをする場所です。","Guna に untuk lokasi dengan あります. Guna で untuk tempat sesuatu aktiviti berlaku.","With あります, に marks where something is. With an action such as 読みます, で marks where you do it."],[("1 · Notice",["ロビーに本があります。","ロビーで本を読みます。","どちらの文で、人が何かをしますか。"]),("2 · Choose",["に・で を入れましょう。","駅の前＿＿店があります。","その店＿＿パンを買います。","部屋＿＿机があります。"]),("3 · Write and ask",["家や学校に何がありますか。そこで何をしますか。","二つの文を書いて、相手にも聞きましょう。","________________________________","________________________________"])],["Second model describes an action. Gaps: に / で / に.","Example: 学校に図書室があります。図書室で本を読みます。"])
lesson("Tell a colleague you will be late","Japanese","B1","Writing",["到着予定と次にしてほしいことを伝えます。相手との関係に合う言い方を選びましょう。","Nyatakan waktu tiba dan apa yang rakan boleh buat sementara menunggu.","State the expected arrival time and whether the recipient should wait or start."],[("1 · Compare",["A　ごめん、電車が遅れてる。10時10分ごろ着くよ。先に始めてて。","B　すみません。電車の遅れで、到着は10時10分ごろになります。先に始めていただけますか。","C　少し遅れます。すみません。","どれを親しい同僚に送りますか。Cを読んだ相手は何を聞きたいですか。"]),("2 · Repair",["Cを書き直しましょう。到着は9時15分です。会議は先に始めてください。","________________________________","________________________________"]),("3 · Write",["取引先との約束に遅れます。理由と到着予定を伝え、相手の都合を聞いてください。","________________________________","________________________________"])],["A is casual, B is appropriate for a more formal relationship. C leaves the recipient unsure whether to wait.","Example: 申し訳ありません。電車が遅れており、9時15分に到着予定です。先に始めていただけますか。"])

from curriculum import load_batch
load_batch(lesson)

from suite import Ledger, build_suite, paginate, authored_scope, component_words
ledger=Ledger()
suite_lessons,suite_units=build_suite(ledger)

from course import add_course
chapters=add_course(lessons,lesson,suite_units)
lessons.extend(suite_lessons)

from fontTools import subset
from fontTools.ttLib import TTFont, newTable
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
def cff_to_truetype(font):
    # Noto Sans CJK is a CID-keyed CFF font. After subsetting, its glyphs keep their old CIDs while MuPDF writes the new
    # glyph indices into the page text, so every PDF viewer drew the wrong glyphs (Sam, 14 Nov 2026: chapter 1 download
    # unreadable). TrueType outlines have no CIDs: the glyph index is the glyph, so the text renders as written.
    order=font.getGlyphOrder();glyphset=font.getGlyphSet()
    font["loca"]=newTable("loca");glyf=font["glyf"]=newTable("glyf");glyf.glyphOrder=order;glyf.glyphs={}
    for name in order:
        pen=TTGlyphPen(glyphset);glyphset[name].draw(Cu2QuPen(pen,1.0,reverse_direction=True));glyf[name]=pen.glyph()
    maxp=font["maxp"]=newTable("maxp");maxp.tableVersion=0x00010000
    for key in ("maxZones","maxTwilightPoints","maxStorage","maxFunctionDefs","maxInstructionDefs","maxStackElements","maxSizeOfInstructions","maxComponentElements"):
        setattr(maxp,key,1 if key=="maxZones" else 0)
    post=font["post"];post.formatType=2.0;post.extraNames=[];post.mapping={};post.glyphOrder=order
    for tag in ("CFF ","VORG"):
        if tag in font:del font[tag]
    font["head"].glyphDataFormat=0;font.sfntVersion="\x00\x01\x00\x00"
    return font
from tempfile import TemporaryDirectory
LEGACY_CSS="@font-face{font-family:Body;src:url(body.ttf)}*{font-family:Body;color:#151515}body{font-size:18pt;line-height:1.42}small{font-size:12pt}h1{font-size:27pt}h2{font-size:21pt;border-bottom:1pt solid black}p{margin:0 0 12pt}"
# Step 4 suites carry more text per sheet; a smaller face keeps tables on one page.
COMPACT_CSS="@font-face{font-family:Body;src:url(body.ttf)}*{font-family:Body;color:#151515}body{font-size:12.5pt;line-height:1.36}small{font-size:8pt}h1{font-size:19pt;margin:0 0 3pt}h2{font-size:14.5pt;border-bottom:1pt solid black;margin:4pt 0 7pt}p{margin:0 0 4.5pt}p.h{font-weight:bold;margin-top:7pt}.ms{color:#0b4a7a}.mn{font-style:italic}"
RECT=fitz.Rect(46,42,550,796)
import re
def marked_html(line):
    # Step 4 suites: Malay target text in blue, Kata-Kata root mentions in italics.
    text=html.escape(line)
    text=re.sub(r"«([^«»]*)»",r'<span class="ms">\1</span>',text)
    return re.sub(r"‹([^‹›]*)›",r'<span class="mn">\1</span>',text)
def markup(item,label,lines,raw=None):
    if item.get("style")=="compact":
        shown=raw if raw is not None else [html.escape(line) for line in lines]
        shown=[marked_html(x) for x in raw] if raw is not None else shown
        body="".join(('<p class="h">' if line.startswith("■ ") else "<p>")+text+"</p>" for line,text in zip(lines,shown))
        return f'<small>{html.escape(item["header"])}</small><h1>{html.escape(item["title"])}</h1><h2>{html.escape(label)}</h2>{body}',COMPACT_CSS
    body="".join("<p>"+html.escape(line)+"</p>" for line in lines)
    return f'<small>Cikgu, Sensai! / {item["lang"]} · {item["level"]}</small><h1>{item["title"]}</h1><h2>{label}</h2>{body}',LEGACY_CSS
with TemporaryDirectory() as tmp:
    font=TTFont("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",fontNumber=0)
    # Copying text out of the PDF (14 Nov 2026): the font's "liga" (fi, fl, ff, ffi) and "locl" (digits 0 to 9) features make the shaper
    # draw alternate glyphs that have no Unicode value of their own, so the PDF's ToUnicode map has no entry for them and a viewer copies
    # "A1" as "A=" and "file" as "6le". The glyphs look the same without those two features, so the subset keeps only ccmp, vert and vrt2.
    opts=subset.Options(); opts.layout_features=["ccmp","vert","vrt2"]
    sub=subset.Subsetter(opts); sub.populate(text=json.dumps(lessons,ensure_ascii=False)+"Cikgu, Sensai! · /()0123456789"); sub.subset(font); cff_to_truetype(font).save(tmp+"/body.ttf")
    archive=fitz.Archive(tmp)
    scratch=[fitz.open(),0]
    def fits(item,label,lines):
        # insert_htmlbox keeps memory until its document is closed, so the scratch document is replaced every 100 checks
        # (keeps the build under the session memory limit; the result is the same).
        if scratch[1]>=100:
            scratch[0].close();scratch[0]=fitz.open();scratch[1]=0
        scratch[1]+=1
        page=scratch[0].new_page(width=595.28,height=841.89)
        text,css=markup(item,label,lines)
        space,scale=page.insert_htmlbox(RECT,text,css=css,archive=archive,scale_low=1)
        scratch[0].delete_page(-1)
        return space>=0
    for item in suite_lessons:paginate(item,fits)
    scope=authored_scope(suite_lessons,ledger)
    for item in suite_lessons:component_words(item,ledger,suite_units)

    from catalogue import make_catalogue
    from language_checks import run_checks
    catalogue=make_catalogue(lessons,chapters)
    run_checks(lessons,catalogue,authored_scope=scope)
    # Developer copy of the generated scope, so tools/check_report.py can re-run the checks.
    (root/"docs/step4-authored-scope.json").write_text(json.dumps(scope,ensure_ascii=False,indent=1)+"\n")
    (root/"dist/catalogue.js").write_text("const catalogue="+json.dumps(catalogue,ensure_ascii=False)+";\n")

    doc=fitz.open()
    for item in lessons:
        for page_no,page in enumerate(item["pages"]):
            # insert_htmlbox keeps memory per page; reopening the document every 300 pages keeps the build under the
            # session memory limit (the saved PDF is the same).
            if len(doc) and len(doc)%300==0:
                data=doc.tobytes(garbage=1,deflate=True);doc.close();doc=fitz.open("pdf",data);del data
            page["index"]=len(doc)
            p=doc.new_page(width=595.28,height=841.89)
            raw=[x for x,k in item["_raw"][page_no]] if "_raw" in item else None
            text,css=markup(item,page["label"],page["lines"],raw)
            space,scale=p.insert_htmlbox(RECT,text,css=css,archive=archive,scale_low=1)
            assert space>=0,(item["title"],page)
    for item in suite_lessons:del item["_raw"]
    raw=doc.tobytes(garbage=4,deflate=True)
(root/"dist/bank.js").write_text("const lessons="+json.dumps(lessons,ensure_ascii=False)+";\nconst bankPDF='"+base64.b64encode(raw).decode()+"';")
(root/"dist/chapters.js").write_text("const chapters="+json.dumps(chapters,ensure_ascii=False)+";")
print(f"Built {len(lessons)} packs ({len(suite_lessons)} step 4 suite components), {len(doc)} pages, all fit-checked.")

# Keep the downloadable offline copy in sync with the deployed chapter guide.
# Preserve the existing archive layout (source files plus dist/index.html).
from zipfile import ZipFile, ZIP_DEFLATED
archive_path=root/"dist/Cikgu-Sensai-offline.zip"
with ZipFile(archive_path,"w",ZIP_DEFLATED) as offline:
    files=list(root.glob("*.py"))+[root/"README.md",root/"wrangler.json"]
    for folder in ("curriculum","dist","tools","suite"):
        files.extend((root/folder).rglob("*"))
    for path in sorted(set(files)):
        if path.is_file() and path!=archive_path and "__pycache__" not in path.parts:
            offline.write(path,path.relative_to(root))
