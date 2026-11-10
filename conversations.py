"""Each block is one A4 scene. Brackets mark guided-practice gaps."""
def scenes(text, guided=False):
    import re
    result, answers = [], []
    for number, block in enumerate(text.strip().split("\n\n"), 1):
        title, *lines = block.splitlines()
        assert len(lines) % 2 == 0
        turns = []
        for i, line in enumerate(lines):
            answers.extend(re.findall(r"\[([^\]]+)\]", line))
            turns.append(("A   " if i % 2 == 0 else "B   ") + re.sub(r"\[[^\]]+\]", "____", line))
        result.append((f"{2 if guided else 1} · {number}. {title}", turns))
    return result, answers

lunch = """Pesan makan
Nak nasi ayam satu. Ada lagi?
Ada. Nak makan sini ke bungkus?
Makan sini. Kawan saya pun nak makan.
Dia nak nasi ayam juga?
Dia tak makan ayam. Ada mi goreng?
Ada. Nak satu pinggan?
Ya. Mi tu pedas tak?
Tak pedas. Sambal ada di tepi.

Pilih minuman
Air apa yang ada hari ni?
Ada teh ais, kopi dan air kosong.
Teh ais satu. Boleh kurang manis?
Boleh. Kawan nak minum apa?
Dia nak air kosong. Berapa harga teh ais?
Tiga ringgit. Air kosong satu ringgit.
Kalau dua air kosong saja?
Dua ringgit. Nak tukar?
Ya, dua air kosong saja.
Baik. Nak ais?
Satu dengan ais, satu lagi tak nak ais.
Baik, saya ambil sekarang.

Semak dan bayar
Maaf, mi goreng belum sampai. Dah siap?
Sekejap ya. Ini mi goreng. Cukup semua?
Ya. Nasi ayam, mi goreng dan dua air kosong.
Betul. Nasi lapan, mi enam, air dua. Semua enam belas.
Boleh bayar dengan kad?
Maaf, tunai atau QR saja.
Kalau saya bagi dua puluh ringgit, ada baki?
Ada. Ini baki empat ringgit.
Terima kasih. Sambal boleh ambil di mana?
Di hujung meja, dekat sudu."""
lunch_gap = """Tanya pilihan
Nak nasi lemak satu. Ada lagi?
Maaf, nasi lemak dah [habis].
Kalau macam tu, ada apa [lagi]?
Ada nasi ayam dan mi goreng.
Mi goreng [pedas] tak?
Pedas sikit. Nak cuba nasi ayam?
Ya. Kalau nak sambal asing, boleh?
[Boleh]. Nak makan sini atau bungkus?

Semak bajet
Saya nak [bungkus]. Nasi ayam berapa?
Lapan ringgit. Nak air juga?
Saya ada sepuluh ringgit. Air apa yang boleh saya beli?
Air kosong dua ringgit. Teh ais tiga ringgit.
Kalau ambil air kosong, cukup tak?
[Cukup]. Semua sepuluh ringgit.
Baik. Air kosong satu, tak nak ais.
Baik. Nak sudu sekali?

Ambil pesanan
Ya, satu sudu. Saya tunggu di [mana]?
Di tepi kaunter. Saya panggil nanti.
Maaf, yang ini nasi saya ke?
Ya. Cuba tengok, cukup semua?
Air belum ada. Boleh saya ambil sekarang?
Boleh. Ini air kosong. Nak bayar macam mana?
Boleh bayar dengan [kad]?
Boleh. Terima kasih, jumpa lagi."""
train = """Find the platform
Excuse me. Where is platform two?
It’s on the left. Where are you going?
To Park Road. Is this the right train?
Yes. Do you have a ticket?
Yes. Is this ticket for one person?
Let me see. Yes, one adult.
Do I go through this gate?
Yes. Put your ticket here.

Choose a route
I have a big bag. Are there stairs?
Yes. There’s a lift too. Do you want the lift?
Yes, please. Is it near the gate?
It’s next to the shop. Can you see the sign?
The blue sign on the right?
That’s the toilet. Look on the left.
Oh, next to the coffee shop?
Yes. Take the lift down one floor.

Check the time
What time is the next train?
At ten past two. What time is it now?
Five past two. Do I have time?
Yes. It’s two minutes to the platform.
And if I miss it?
There’s another train at two twenty.
So I take the lift down and go to platform two?
Yes. Check the screen for Park Road.
Thank you. Is there a lift at Park Road too?
Yes. It’s near the exit."""
train_gap = """Find the gate
Excuse me. [Where] is platform three?
It’s over there. Where do you want to go?
To Lake Street. Is this the right gate?
Yes. Have you got a ticket?
No. Where can I buy one?
At the machine on the [right].
Can I pay by card?
Yes. Tap your card here.

Find a lift
Thanks. Are there stairs to the platform?
Yes. Do you need the [lift]?
Yes. I have two bags. Is it near here?
It’s next to the ticket office.
Is that the office on the left?
Yes. Take the lift up one floor.
Up [one] floor, then platform three?
That’s right. Follow the signs.

Check the train
What [time] is the next train?
At nine fifteen. It’s nine ten now.
Five minutes. Is the platform far?
No. You have time. Look at the screen upstairs.
What name do I look for?
Lake Street. Where are you getting off?
At Lake Street. Which exit is near the bus stop?
Exit B. The buses are outside."""
meeting = """Explain the change
Can we move Monday’s meeting? A client wants a site visit.
What time do you need to leave?
By nine. I should be back by noon, traffic permitting.
Could we meet at twelve thirty, then?
I’d rather allow for a delay. Is your afternoon free?
I’m interviewing someone at two. How long do we need?
About forty minutes if we read the figures first.
That sounds reasonable. Let me check Tuesday as well.

Compare options
Would Tuesday at ten work better for you?
I’m at the branch until three. Could you do four?
Possibly. What do we need to decide before Wednesday?
The supplier needs our numbers by lunchtime.
Then four gives us enough time. Where shall we meet?
The small meeting room is quiet. Is it available?
I’ll check. It’s booked, but the training room is free.
Let’s take that. Can the branch team join online?

Agree on next steps
Yes. Shall I add a video link to the invitation?
Please do. Could you send the figures beforehand too?
I have last month’s totals. Do you need the forecast?
Yes, the supplier will ask about next month.
I can send both by Tuesday morning. Who will brief Mei?
I’ll call her today. So we’re meeting on Tuesday at four?
Yes, in the training room, with the branch team online.
Great. I’ll look out for your updated invitation."""
meeting_gap = """Explain a clash
Could we [move] our Thursday workshop? My train was cancelled.
Of course. Would the afternoon [work] for you?
I can get there by three, but I leave again at four.
How long do we need for the workshop?
An hour and a half. Could we try Friday instead?
Perhaps. Do all the trainees need to attend in person?
They need to practise with the equipment.
Then let’s find a time when everyone can come.

Compare alternatives
How [about] Friday morning at nine?
Two people have training until ten. What about eleven?
The room is free then. Shall I reserve it until half past twelve?
Yes, please. Is there time to set everything up?
I can get there early if you send me the checklist.
Would tonight be early enough?
Yes. Who can bring the spare equipment?
I’ll ask the technician before I go home.

Confirm responsibilities
Shall I [send] the revised invitation?
Yes. Could you explain why we moved it?
I’ll mention the travel delay. Anything else to include?
Ask everyone to bring their practice notes.
So that’s Friday at [eleven], in the original room?
Correct. You’ll send the invitation and I’ll bring the checklist.
I thought you were sending me the checklist tonight.
You’re right. I’ll send it tonight and bring a copy on Friday."""
jp = """待ち合わせの場所
もしもし。今、どこですか。
駅に着きました。今、改札の前です。
改札は二つあります。近くに何がありますか。
パン屋があります。右に小さな花屋もあります。
あ、それは東口ですね。私は西口にいます。
西口ですか。ここから遠いですか。
歩いて五分くらいです。荷物は多いですか。
はい、大きいかばんが二つあります。

行き方を相談する
そちらに行きましょうか。
お願いします。階段はちょっと大変です。
では東口で会いましょう。座る場所はありますか。
はい、パン屋の前にベンチがあります。
そこは人が多いですか。
ええ。花屋の横にもベンチがありますよ。
じゃあ、花屋の横にしませんか。
いいですね。そこで待っています。

目印を確認する
花屋の近くに着きました。何色のかばんですか。
大きい青いかばんです。今、どこにいますか。
赤い看板の前です。ベンチが見えません。
あ、看板の後ろですよ。私は白い帽子をかぶっています。
見えました。手を上げてもらえますか。
はい。分かりますか。
分かりました。お待たせしました。お昼はもう食べましたか。
まだです。荷物を預けてから、一緒に食べませんか。"""
jp_gap = """場所を聞く
もしもし。今、[どこ]ですか。
バス停の前です。駅はどちらですか。
近くに何が[あります]か。
コンビニがあります。向かいに銀行があります。
それなら南口ですね。北口まで来られますか。
歩いて何分くらいですか。
十分くらいです。道は分かりますか。
いいえ。行き方を教えてください。

別の場所を提案する
まず銀行の前を通ってください。
すみません、雨が強くなりました。
じゃあ、コンビニで[待って]いてください。
ありがとうございます。入口でいいですか。
入口は寒いでしょう。店の中に座る場所はありますか。
はい、窓のそばにテーブルがあります。
では、そこにしましょう。何か飲みますか。
温かいお茶をお願いします。

相手を見つける
コンビニに着きました。窓の[そば]にいますか。
はい。黒いコートを着ています。
テーブルが二つありますね。どちらですか。
奥のテーブルです。手を上げますね。
あ、分かりました。お茶をどうぞ。
ありがとうございます。雨はまだ強いですか。
少し弱くなりました。駅まで一緒に歩きませんか。
そうですね。お茶を飲んでから行きましょう。"""
