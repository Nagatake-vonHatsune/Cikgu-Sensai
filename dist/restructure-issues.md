# Step 1 restructure: issues log by unit

Date: 11 November 2026. Status: provisional audit; no content corrections made.

## Scope and method

Existing Malay lesson wording is preserved by Sam’s instruction. This is an issues inventory, not language validation and not the step 3 build checks. All Japanese remains an AI draft awaiting native-speaker review.

Compared with 982 ledger rows and 427 chapter cards. Source revisions and SHA-256 file hashes are in `docs/restructure-sources.json`. The raw occurrence evidence is in `restructure-issues.csv`.

The audit covers every legacy Malay unit, each Malay scenario family, the linked Di/ke/dari sheet and the A2 lunch extension. It reads Malay vocabulary entries, Malay explainers, models, guided examples, tasks and role cards. Generated lesson plans repeat these sources; English scheduling boilerplate and English/Japanese translations are excluded. Generic Malay instruction text is included and may itself exceed beginner vocabulary.

Ledger matching is case-insensitive, longest phrase first, with slash alternatives and parenthetical annotations normalised. A missing exact match is a review candidate, not proof that a root is absent. Known proper names, role letters and English am/pm cues are excluded. A word that occurs only inside an intact ledger phrase is not treated as an independently taught word: isolated pagi/petang/malam are therefore flagged against their later standalone cards even though the greeting phrases occur in Ch1. Scene “primes Ch…” labels are reported but do not silently confer chapter permission. Chapter availability comes from existing ms-cXX card IDs; it is not inferred from a CEFR label.

Register inventory includes nak/tak/dah and other observed short forms. These resources do not explicitly teach the standard/spoken pair in sequence. In particular nak already appears in the greetings Malay explainer before any standard mahu teaching; tak enters the fruit-market material before a standard-first contrast; dah occurs in the linked A2 lunch pack. The ledger has tidak/tak in Ch1, sudah/dah in Ch4 and mahu/nak in Ch5, but ledger presence is not proof that the existing Cikgu Sensai sheets taught the standard form first. Other pairs in the inventory are provisional usage mappings.

The affix inventory reproduces Kata-Kata’s shape detection and records allow-list roots and chapter chunk exemptions separately. It lists all ber-/me-shaped forms encountered, including exemptions, rather than asserting that every match is an error. Future chapter 12 and unplaced advanced packs have no validated earlier-course sequence; their later-chapter compliance is not asserted.

## Unit inventory

### Unit 1

**Existing resources:** Greetings

- **No exact ledger match:** bila, pun
- **Ledger present, chapter unassigned:** guna
- **Later chapter:** awak → Earliest chapter card: Ch2. L-0038; balik → Earliest chapter card: Ch4. L-0202; malam → Earliest chapter card: Ch4. L-0165; nak → Earliest chapter card: Ch5. L-0213; pada → Earliest chapter card: Ch9. L-0378; pagi → Earliest chapter card: Ch4. L-0162; petang → Earliest chapter card: Ch4. L-0164; saya → Earliest chapter card: Ch2. L-0036; waktu → Earliest chapter card: Ch4. L-0156
- **Register:** nak → mahu
- **Affix inventory:** None detected in the scoped text.

### Unit 2A

**Existing resources:** Introductions

The unchanged Introductions pack mentions home (tinggal di PJ), which the expanded plan places in 2B. No new split or duplicate lesson has been authored; 2B is empty.

- **No exact ledger match:** oh, pun, tempat, untuk
- **Ledger present, chapter unassigned:** None detected in the scoped text.
- **Later chapter:** dari mana → Earliest chapter card: Ch7. L-0298; sekarang → Earliest chapter card: Ch4. L-0161
- **Register:** None detected in the scoped text.
- **Affix inventory:** None detected in the scoped text.

### Unit 2B

**Existing resources:** None. Placeholder only; no lesson text to audit.

- **No exact ledger match:** Not applicable: no content.
- **Ledger present, chapter unassigned:** Not applicable: no content.
- **Later chapter:** Not applicable: no content.
- **Register:** Not applicable: no content.
- **Affix inventory:** Not applicable: no content.

### Unit 3A

**Existing resources:** Counting and quantities

- **No exact ledger match:** belas, ialah, jumlah, puluh, saja, sebut, semak, semula, untuk
- **Ledger present, chapter unassigned:** tiket
- **Later chapter:** nak → Earliest chapter card: Ch5. L-0213
- **Register:** nak → mahu, saja → sahaja
- **Affix inventory:** belas [allow-list root]; berapa [chapter chunk/lex exemption]

### Unit 3B

**Existing resources:** Ringgit and sen, Beli buah di pasar, Jumlah buah, Pesanan buah, Beli buah di pasar · Learner pack

Beli buah di pasar / Jumlah buah / Pesanan buah teach biji and sebiji before chapter 8 (L-0344, L-0361). This was already early in the old course and remains unresolved.

The fruit-market practice uses manis/masam/besar/kecil (chapter 5), sameness with sama (chapter 6), and esok/pukul (chapter 4). These are preserved forward references.

The existing Lunch at a Malaysian stall link is retained at A2 as an optional extension, not relabelled A1 or treated as core 3B content. Its separate issues inventory follows below.

- **No exact ledger match:** baiki, bajet, bandingkan, beri, betul, bual, buat, butiran, campur, cara, contoh, cukup, datang, epal, gariskan, ini, itu, jika, jumlah, kepada, lanjut, maksud, mangga, mesej, ni, pembaca, perbezaan, pesan, pilihan, pisang, puluh, pun, rakan, saja, sebut, selama, selepas, semak, setandan, supaya, terangkan, ubah, untuk, versi
- **Ledger present, chapter unassigned:** ambil, beg, buka, faham, jelas, pasar, pesanan, tahu, tanya, tindakan, tulis, tutup
- **Later chapter:** air → Earliest chapter card: Ch5. L-0259; akan → Earliest chapter card: Ch4. L-0192; besar → Earliest chapter card: Ch5. L-0237; biji → Earliest chapter card: Ch8. L-0344; buah → Earliest chapter card: Ch8. L-0514; dalam → Earliest chapter card: Ch7. L-0308; diambil → Earliest chapter card: Ch9. L-0391; hari ini → Earliest chapter card: Ch4. L-0169; hijau → Earliest chapter card: Ch5. L-0229; kalau → Earliest chapter card: Ch7. L-0341; kecil → Earliest chapter card: Ch5. L-0238; kurang → Earliest chapter card: Ch6. L-0266; lain → Earliest chapter card: Ch6. L-0281; macam mana → Earliest chapter card: Ch5. L-0211; manis → Earliest chapter card: Ch5. L-0218; masam → Earliest chapter card: Ch5. L-0220; merah → Earliest chapter card: Ch5. L-0226; minit → Earliest chapter card: Ch4. L-0159; nak → Earliest chapter card: Ch5. L-0213; oleh → Earliest chapter card: Ch9. L-0377; pilih → Earliest chapter card: Ch6. L-0280; pukul → Earliest chapter card: Ch4. L-0157; sama → Earliest chapter card: Ch6. L-0268; sebiji → Earliest chapter card: Ch8. L-0361; sekali → Earliest chapter card: Ch4. L-0188; semua → Earliest chapter card: Ch8. L-0374; sikit → Earliest chapter card: Ch5. L-0216; yang → Earliest chapter card: Ch5. L-0212
- **Register:** macam mana → bagaimana, nak → mahu, ni → ini, saja → sahaja, sikit → sedikit, tak → tidak
- **Affix inventory:** beli [allow-list root]; berapa [chapter chunk/lex exemption]; beri [review]; merah [allow-list root]; mesej [review]

### Unit 3C

**Existing resources:** Order and floors

Order and floors uses tingkat and location-related vocabulary ahead of chapter 7. Existing gap, preserved.

- **No exact ledger match:** ialah, ini, itu, jumlah, keempat, nombor, selepas, turutan, untuk
- **Ledger present, chapter unassigned:** guna, pintu
- **Later chapter:** tingkat → Earliest chapter card: Ch7. L-0331; yang → Earliest chapter card: Ch5. L-0212
- **Register:** None detected in the scoped text.
- **Affix inventory:** berapa [chapter chunk/lex exemption]

### Unit 4A

**Existing resources:** Clock time, Dates and days

- **No exact ledger match:** belas, ialah, kelas, selepas, supaya, tambah, tarikh, untuk
- **Ledger present, chapter unassigned:** jelas
- **Later chapter:** atau → Earliest chapter card: Ch5. L-0214
- **Register:** None detected in the scoped text.
- **Affix inventory:** belas [allow-list root]; berapa [chapter chunk/lex exemption]

### Unit 4B

**Existing resources:** Frequency and routines

- **No exact ledger match:** beri, saja, seminggu
- **Ledger present, chapter unassigned:** angka, pasar, tepat
- **Later chapter:** None detected in the scoped text.
- **Register:** saja → sahaja, tak → tidak
- **Affix inventory:** beri [review]

### Unit 5

**Existing resources:** Taste and colour, Size and shape

REORDER-CREATED dependency: Size and shape now precedes Asking where and Directions and orientation. Its model uses di atas / di bawah before those location lessons in chapter 7. Previously the direction/orientation unit was before Size and shape.

The existing Lunch at a Malaysian stall A2 extension remains linked, with a separate audit below.

- **No exact ledger match:** begitu, ini, itu, perisa, rak, sos, tali, tanpa, untuk
- **Ledger present, chapter unassigned:** gula
- **Later chapter:** atas → Earliest chapter card: Ch7. L-0306; bawah → Earliest chapter card: Ch7. L-0307; buku → Earliest chapter card: Ch8. L-0487; kalau → Earliest chapter card: Ch7. L-0341; yang mana → Earliest chapter card: Ch6. L-0279
- **Register:** nak → mahu, sikit → sedikit, tak → tidak
- **Affix inventory:** merah [allow-list root]

### Unit 6

**Existing resources:** Comparisons and superlatives

REORDER-CREATED dependency: Comparisons and superlatives now precedes chapter 7. Its model uses Antara tiga buku ini and its Malay explainer uses dalam kumpulan, before the ledger introduces antara/dalam in chapter 7. Previously the location/direction lessons preceded this resource. Buku remains a ledger-to-course sequencing discrepancy (chapter 8 card, already used in unit 5).

- **No exact ledger match:** banding, benda, ceritanya, ini, kelakar, kumpulan, lucu, memang
- **Ledger present, chapter unassigned:** bagi
- **Later chapter:** antara → Earliest chapter card: Ch7. L-0311; buku → Earliest chapter card: Ch8. L-0487; dalam → Earliest chapter card: Ch7. L-0308
- **Register:** tapi → tetapi
- **Affix inventory:** memang [review]

### Unit 7

**Existing resources:** Asking where, Directions and orientation, Di, ke and dari

Di, ke and dari remains linked to both existing location/direction resources; it is inventoried once here.

- **No exact ledger match:** barat, beritahu, itu, kampus, kelas, lintasan, pun, selatan, tempat, timur, tren, untuk, utara
- **Ledger present, chapter unassigned:** cari, guna, lintas, pejalan kaki
- **Later chapter:** None detected in the scoped text.
- **Register:** nak → mahu, tak → tidak
- **Affix inventory:** belakang [allow-list root]; belok [allow-list root]; beritahu [review]

### Unit 8

**Existing resources:** None. Placeholder only; no lesson text to audit.

- **No exact ledger match:** Not applicable: no content.
- **Ledger present, chapter unassigned:** Not applicable: no content.
- **Later chapter:** Not applicable: no content.
- **Register:** Not applicable: no content.
- **Affix inventory:** Not applicable: no content.

### Unit 9

**Existing resources:** None. Placeholder only; no lesson text to audit.

- **No exact ledger match:** Not applicable: no content.
- **Ledger present, chapter unassigned:** Not applicable: no content.
- **Later chapter:** Not applicable: no content.
- **Register:** Not applicable: no content.
- **Affix inventory:** Not applicable: no content.

### Future chapter 12 · Stage 2, not yet active

**Existing resources:** Ambil bungkusan di lobi, Dah atau belum, Mesej untuk pengawal, Ambil bungkusan di lobi · Learner pack, A clear pickup message

- **No exact ledger match:** baiki, bandingkan, beri, betul, bila, bual, buat, butiran, cara, contoh, datang, elok, gariskan, ini, itu, jadi, jika, kelas, kenal, kepada, kotaknya, koyak, label, lanjut, lewat, lobi, maksud, mesej, mesejnya, mungkin, ni, nombor, nombornya, oh, pembaca, perbezaan, perlu, pilihan, pun, rakan, selama, semak, sesuai, tamat, tempat, terangkan, tu, tunjuk, ubah, untuk, van, versi
- **Ledger present, chapter unassigned:** Not assessed: no approved chapter sequence for this pack.
- **Later chapter:** Not assessed: no approved chapter sequence for this pack.
- **Register:** dah → sudah, macam tu → seperti itu, nak → mahu, ni → ini, tak → tidak, tu → itu
- **Affix inventory:** belum [allow-list root]; beri [review]; mesej [review]; mesejnya [review]

### Supplementary · Susun giliran di kaunter · unplaced / provisional

**Existing resources:** Susun giliran di kaunter, Sebab dan akibat, Mesej tukar giliran, Susun giliran di kaunter · Learner pack

- **No exact ledger match:** akibat, alasan, baiki, bandingkan, bantu, bentuk, beri, beritahu, betul, biasa, bual, buat, butiran, contoh, cukup, dapat, datang, dokumen, gariskan, giliran, hasil, hingga, ikut, ini, itu, jadi, jadual, jaga, jelaskan, jika, kampus, kedua-dua, kelas, kena, kenapa, kepada, keputusan, kunci, langkah, lanjut, lewat, maksud, memberi, menggunakan, menunjukkan, mesej, mesti, papan, pelan, pembaca, pengesahan, penyelia, perbezaan, perlu, perlukan, perubahan, pilihan, rakan, sahkan, saja, sebelum, selama, selepas, semak, sempat, sistem, supaya, susun, tamat, tarikh, terangkan, tunjuk, ubah, untuk, versi
- **Ledger present, chapter unassigned:** Not assessed: no approved chapter sequence for this pack.
- **Later chapter:** Not assessed: no approved chapter sequence for this pack.
- **Register:** dah → sudah, nak → mahu, saja → sahaja, tak → tidak, tapi → tetapi
- **Affix inventory:** belas [allow-list root]; belum [allow-list root]; berapa [chapter chunk/lex exemption]; beri [review]; beritahu [review]; memberi [review]; menggunakan [review]; menunjukkan [review]; mesej [review]; mesti [review]

### Supplementary · Runding masa kerja pembaikan · unplaced / provisional

**Existing resources:** Runding masa kerja pembaikan, Syarat dan konsesi, Notis air untuk penduduk, Runding masa kerja pembaikan · Learner pack

- **No exact ledger match:** agihan, alat, anggaran, anggarannya, baharu, baiki, bandingkan, bantuan, begitu, bekalan, beri, beritahu, berlaku, bermula, betul, bila, bocor, bual, buat, butiran, cara, catat, contoh, cukup, dapat, diberi, dihubungi, diisi, dikosongkan, gariskan, hanya, hubungi, ini, itu, jangan, jika, kenapa, kepada, keputusan, kerosakan, kesihatan, kini, konsesi, kumpul, langkah, lanjut, lobi, lokasi, maklumat, maksud, masalah, memberi, mengakui, mengambil, mengubah, mesej, mungkin, nombor, nyatakan, pasti, pembaca, pembaikan, pendirian, penduduk, penghantaran, penghuni, penyelia, perbezaan, perkara, perkembangan, perlu, perlukan, perubahan, petugas, pilihan, pulih, rakan, ruang, runding, sahkan, saja, sampaikan, sebelum, sediakan, sejam, sekejap, selama, selepas, selesai, semak, sementara, semula, senarai, seorang, seterusnya, setuju, syarat, tambah, tangki, tanpa, tempoh, tentang, tentu, terangkan, tiada, tiba, ubah, untuk, utama, versi, wakil, walaupun
- **Ledger present, chapter unassigned:** Not assessed: no approved chapter sequence for this pack.
- **Later chapter:** Not assessed: no approved chapter sequence for this pack.
- **Register:** dah → sudah, nak → mahu, saja → sahaja, tak → tidak, tapi → tetapi
- **Affix inventory:** bekalan [review]; belum [allow-list root]; berapa [chapter chunk/lex exemption]; beri [review]; beritahu [review]; berlaku [review]; bermula [review]; memberi [review]; mengakui [review]; mengambil [review]; mengubah [review]; mereka [allow-list root]; mesej [review]

### Supplementary · Menimbang dapatan tinjauan kampus · unplaced / provisional

**Existing resources:** Menimbang dapatan tinjauan kampus, Membezakan andaian dan bukti, Catatan keputusan dan kenyataan awam, Menimbang dapatan tinjauan kampus · Learner pack

- **No exact ledger match:** adakah, aduan, ahli, alasan, andaian, asasnya, awam, ayat, bahawa, balas, bandingkan, batas, begitu, bekas, berbeza, berbunyi, bergantung, berhenti, beri, beroperasi, berpuas, bersetuju, bersuara, bertangguh, betul, betulkan, bezakan, bila, bimbang, bual, buat, bukti, butiran, cadangan, cadangkan, catat, catatan, contoh, dahulu, dakwaan, dapatan, dasar, datang, dibincangkan, dicadangkan, diedarkan, dihentikan, dikekalkan, diketepikan, dilaksanakan, diluluskan, dinilai, dinyatakan, direkodkan, disahkan, ditanya, diumumkan, diwakili, gagal, gambaran, gantikan, gariskan, hadkan, hanya, hati, hujah, ini, itu, jadi, jadual, jawatankuasa, jelaskan, jika, kampus, kata, kedengaran, kekalkan, kelas, keluasannya, kelulusan, kenyataan, kepada, keperluan, keputusan, kerana, kesannya, kesimpulan, ketersediaan, ketiadaan, kos, kosnya, langsung, lanjut, lewat, maklum, maksud, masalah, melaporkan, membantah, memberi, membezakan, memenuhi, memerlukannya, memilih, meminta, menafikan, mencuba, mencukupi, mendahului, mengalami, menganggarkan, mengapa, menggunakan, menghilangkan, mengurangkan, menilai, menimbang, menjawab, menjelang, menolak, menulis, menunjukkan, menyangka, menyebut, menyediakan, menyeluruh, mesej, mesti, mewakili, mungkin, namun, nyatakan, operasi, pasti, pembaca, pembetulan, pendirian, pengalaman, pengangkutan, pengerusi, pengguna, penyelia, perbelanjaan, perbezaan, percubaan, perkataan, perkhidmatan, persatuan, persetujuan, persetujui, peruntukan, pihak, pilihan, proses, pun, rakan, rekodkan, responden, ringkas, ringkasan, saluran, sanggup, sebelum, sebut, sedia, sekadar, sekiranya, selama, selepas, semak, semakan, seperti, sertakan, setuju, supaya, syarat, syaratnya, syor, tajuk, tambah, tambahan, tanpa, tarikh, telah, tempoh, tentang, tentu, tepatkah, terangkan, tertakluk, tiada, tolak, turut, ubah, umum, umumkan, untuk, versi, wakil, wakili, wartawan, wujud
- **Ledger present, chapter unassigned:** Not assessed: no approved chapter sequence for this pack.
- **Later chapter:** Not assessed: no approved chapter sequence for this pack.
- **Register:** tak → tidak
- **Affix inventory:** bekas [review]; belanja [allow-list root]; beliau [allow-list root]; belum [allow-list root]; berapa [chapter chunk/lex exemption]; berbeza [review]; berbunyi [review]; bergantung [review]; berhenti [review]; beri [review]; bermakna [review]; beroperasi [review]; berpuas [review]; bersetuju [review]; bersuara [review]; bertangguh [review]; bertanggungjawab [review]; melaporkan [review]; memadai [review]; membantah [review]; memberi [review]; membezakan [review]; memenuhi [review]; memerlukannya [review]; memilih [review]; meminta [review]; menafikan [review]; menanggung [review]; mencuba [review]; mencukupi [review]; mendahului [review]; mengalami [review]; menganggarkan [review]; mengapa [review]; mengesahkan [review]; menggunakan [review]; menghilangkan [review]; mengurangkan [review]; menilai [review]; menimbang [review]; menjawab [review]; menjelang [review]; menolak [review]; menulis [review]; menunjukkan [review]; menyangka [review]; menyebut [review]; menyediakan [review]; menyeluruh [review]; mereka [allow-list root]; mesej [review]; mesti [review]; mewakili [review]

### Linked A2 extension · Lunch at a Malaysian stall

**Existing resources:** Lunch at a Malaysian stall

- **No exact ledger match:** bandingkan, belas, betul, bila, bual, cara, cukup, dapat, hujung, ini, lemak, ni, panggil, pasal, pelanggan, perlu, pesan, pilihan, pun, saja, sambal, sekejap, selama, semak, tepi, terima, tiada, tiba-tiba, tu, untuk
- **Ledger present, chapter unassigned:** Not assessed: no approved chapter sequence for this pack.
- **Later chapter:** Not assessed: no approved chapter sequence for this pack.
- **Register:** dah → sudah, macam mana → bagaimana, macam tu → seperti itu, nak → mahu, ni → ini, saja → sahaja, sikit → sedikit, tak → tidak, tu → itu
- **Affix inventory:** belas [allow-list root]; beli [allow-list root]; belum [allow-list root]; berapa [chapter chunk/lex exemption]; meja [allow-list root]

## Decisions and limitations

- No new ledger words or patterns are proposed automatically. Candidate matches must be reconciled with roots, phrases and chapter placement before Sam approves any addition.
- Units 2B, 8 and 9 have no existing dedicated material. The placeholders do not claim that the agreed chapter scope is covered.
- Existing units still lack much of the charter’s expanded grammar/vocabulary coverage; that content work remains outside step 1.
- The old 13 resources remain intact inside the 13 planned unit slots; several slots contain two resources and three slots are empty. This is not a claim that 13 complete charter units now exist.
- B1/B2/C1 families retain their existing levels as unplaced, provisional supplementary packs. Chapter 12 is Stage 2, not yet active.
- Step 2 chapter records/component tags, step 3 enforcement and new teaching content have not been implemented.
