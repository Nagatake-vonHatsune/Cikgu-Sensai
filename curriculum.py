"""Load scenario families. Each family supports three independent printable exercises."""
from pathlib import Path
import re
from conversations import scenes

ROOT = Path(__file__).with_name("curriculum")
LINE = "________________________________"
PROMPTS = {
    "English": ("Underline the different meanings. Explain your choice to a partner.", "Compare the three versions. Who is each for? Underline the action the reader can take.", "Stage 3 · Produce", "Close the model. Give your partner only your message. Ask them to say what they will do. Revise one detail if they hesitate.", "Role-play for 3–5 minutes. Ask follow-up questions and check your partner’s understanding."),
    "Malay": ("Gariskan perbezaan maksud. Terangkan pilihan anda kepada rakan.", "Bandingkan tiga versi. Untuk siapa? Gariskan tindakan yang boleh diambil oleh pembaca.", "3 · Guna sendiri", "Tutup contoh. Beri mesej anda kepada rakan. Tanya apa yang dia akan buat. Jika kurang jelas, ubah satu butiran.", "Bual selama 3–5 minit. Tanya soalan lanjut dan semak apa yang rakan faham."),
    "Japanese": ("意味の違いに線を引き、選んだ理由を相手に説明してください。", "三つを比べてください。誰に送りますか。相手が取れる行動に線を引いてください。", "3 · 自分で使う", "例を閉じて相手に伝えます。相手が次に何をするか聞き、分かりにくい点を一つ直してください。", "3〜5分話しましょう。相手の答えに合わせて質問し、最後に決まったことを確かめてください。"),
}
def blocks(name):
    return [s.strip().splitlines() for s in (ROOT/name).read_text().split("@ ") if s.strip()]

def page(label, lines):
    return (label, lines)

def load_batch(lesson):
    endings = {title:lines for title,*lines in blocks("guided.txt")}
    foundation_guides = {title: lines for title, *lines in blocks("foundation-guided.txt")}
    for advanced, filename in [(True,"advanced.txt"),(False,"foundation.txt")]:
        for data in blocks(filename):
            lang,level,title = data[0].split("|")
            notes = data[1].split("|")
            notice,compare,produce,transfer,timer = PROMPTS[lang]
            if advanced:
                start=next(i for i,s in enumerate(data) if s.startswith("Role A|"))
                a,b,change=[s.split("|",1)[1] for s in data[start:start+3]]
                model=[]; guided=[]; answers=[]
                for i in range(3):
                    block=data[2+i*9:11+i*9]
                    for is_gap,target in [(False,model),(True,guided)]:
                        src=endings[title] if i==2 and is_gap else block
                        text=re.sub(r"\{([^|}]+)\|([^}]+)\}",lambda m:m[2 if is_gap else 1],"\n".join(src))
                        if not is_gap:text=text.replace("[","").replace("]","")
                        pages,words=scenes(text,is_gap)
                        label,lines=pages[0]
                        target.append(page(f"{2 if is_gap else 1} · {i+1}. "+src[0],lines))
                        if is_gap:answers.extend(words)
                grammar,writing=[s.split("|")[1:] for s in data[-2:]]
            else:
                a,b,change=data[10].split("|")
                grammar,writing=[s.split("|") for s in data[-2:]]
                model=[];guided=[];answers=[]
                for part in range(2):
                    lines=[]
                    for pair in data[2+4*part:6+4*part]:
                        x,y=pair.split("|");lines.extend(["A   "+x,"B   "+y])
                    model.append(page(f"1 · Model {part+1}/2",lines))
                    variation=foundation_guides[title][part*4:part*4+4]
                    turns=[turn for pair in variation for turn in pair.split("|")]
                    scaffold, words=scenes("Practice "+str(part+1)+"/2"+"\n"+"\n".join(turns),True)
                    guided.append(page(f"2 · Practice {part+1}/2",scaffold[0][1]))
                    answers.extend(words)
            gt,examples,gaps,solutions,task=grammar
            wt,wa,wb,wc,repair,write=writing
            cards=[page("3 · Role "+role,[timer,brief,LINE,LINE]) for role,brief in zip("AB",[a,b])]
            twist=page("Transfer · Change of plan",[change,transfer,LINE,LINE])
            lesson(title,lang,level,"Conversation",notes,model+guided+cards+[twist],
                   ["Guided examples: "+" / ".join(answers),"Accept natural alternatives. Run the scenes as one exchange for 3–5 minutes. Then use the private roles and reveal the change after the first agreement.","Listen for both speakers asking a follow-up, adapting to the change and confirming the same outcome."])
            lesson(gt,lang,level,"Grammar",notes,[page("1 · Notice",examples.split(" / ")+[notice]),page("2 · Choose",gaps.split(" / ")+[LINE]),page(produce,[task,LINE,LINE]),twist],
                   ["Guided answers: "+solutions,"Use the model sentences to check meaning. Change the situation and ask for a second formulation. Accept an alternative if the learner can explain its effect."])
            lesson(wt,lang,level,"Writing",notes,[page("1 · Compare",["A   "+wa,"B   "+wb,"C   "+wc,compare]),page("2 · Repair",[repair,LINE,LINE]),page(produce,[write,LINE,LINE]),twist],
                   ["A: concise. B: supplies context, softens the request or adds a next step. C needs revision. Compare the facts each reader can recover.","One possible repair: "+wa,"Ask the recipient to restate the action. After the change, check that the revised message still works for its intended reader."])
