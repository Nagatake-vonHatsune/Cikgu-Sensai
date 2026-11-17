# Check of 17 Nov 2026: five rule changes run over Cikgu Sensai, Kata-Kata and Hanashishou

Rules commit: see HANDOFF.md. The scripts were scratch tooling and are not committed. Kata-Kata (`main` at d9d9f48) and Hanashishou (`main` at 4be57ac) were cloned read only and not edited.

## Cikgu Sensai

All content (28,460 Malay segments, as the build reads it). Before and after: **20 current violations, 20 legacy exceptions, 140 ledger gaps**; the keys are identical. No hit appears or disappears.

## Kata-Kata (read only)

All 57 packs in `content/ms` (Kelas, Dunia, Jambatan, stretch), with Kata-Kata's own ledger and its own checker. The checker was patched in a scratch copy only (the patch is `docs/handoff/stage-rules-mjs-17nov2026.patch`) and the 174 shared fixtures agree with the Python. Before and after: **10 violations and 6 gaps, the same entries**. No new hit, no gap disappears. The lower-case «pasar malam» in `content/ms/kelas/c03.json` (lines 1382 and 1418) is at chapter 3, where «pasar» is placed.

## Hanashishou (read only)

Malay learner text from every `content/packs/*/targets/ms`: story `.ink` lines (speaker labels, tags and ink logic removed), `ladders.json`, `vocab.json` examples and gap sentences, `minigames.json` targets; 5,037 segments, 2,992 of them with a chapter tag from `course.json`. Checked with the Cikgu Sensai checker and ledger snapshot, one segment at a time, two ways: with no chapter (as the Kata-Kata guard reads Jambatan) and at the scene's chapter tag (the JSON items have no tag, so they are unplaced in both views). A segment is checked alone, so a register hit may also sit in a scene that teaches the standard form first; that is the same before and after. Hanashishou has no guard of its own, so nothing blocks.

### No chapter: 6268 entries before, 6316 after

New hits: **48** (all register: the seven new chapter 17 pairs). Gaps or violations that disappear: **0**.

| Hit | File | Line | Chapter tag | Text |
| --- | --- | ---: | --- | --- |
| bisnes | daily-life/story/missed_bus.ink | 46 | 16 | Anda bayar RM10. Lelaki di sebelah anda dalam barisan sedang baca majalah bisnes |
| je | office/ladders.json | 1336 | - | Mana ada, biasa je! Tapi terima kasih. |
| je | office/ladders.json | 1363 | - | Tak ada date! Kerja je. Awak pula? Hujung minggu okey? |
| je | office/ladders.json | 1370 | - | Haha, mana ada date, mesyuarat dengan Encik Lim je! Awak pula? Hujung minggu bes |
| je | office/minigames.json | 327 | - | Jangan ambil hati, saya gurau je. |
| je | office/story/pantry_banter.ink | 11 | 17 | Mana ada, biasa je! Tapi terima kasih. |
| je | office/story/pantry_banter.ink | 14 | 17 | Tak, baju ni buruk. Murah je. |
| je | office/story/pantry_banter.ink | 23 | 17 | Hmm, diam je... mencurigakan ni. 😏 |
| je | office/story/pantry_banter.ink | 30 | 17 | Wah, seriusnya! Relaks, saya gurau je. |
| je | office/story/pantry_banter.ink | 34 | 17 | Oh... maaf, maaf. Gurau je. |
| je | office/story/pantry_banter.ink | 36 | 17 | Tak ada date! Kerja je. Awak pula? Hujung minggu okey? |
| je | office/story/pantry_banter.ink | 38 | 17 | Haha, mana ada date, mesyuarat dengan Encik Lim je! Awak pula? Hujung minggu bes |
| je | office/story/pantry_banter.ink | 62 | 17 | Hahaha, tengok muka awak! Saya gurau je. Jangan ambil hati, makan tengah hari te |
| je | social/story/mamak_lepak.ink | 31 | 17 | Biasa je. |
| je | social/story/mamak_lepak.ink | 32 | 17 | "Biasa je" saja? 🙄 |
| je | social/story/mamak_lepak.ink | 36 | 17 | Wah, maaf, tanya je. |
| je | social/story/mamak_lepak.ink | 72 | 17 | Er... "okey" je? Terima kasih pun jadilah. 😅 |
| kejap | daily-life/story/grab_pickup.ink | 23 | 17 | Oh, Pintu A? Tak apa, tunggu kejap. |
| kejap | daily-life/story/grab_pickup.ink | 26 | 17 | Oh, sebelah bank. Okey, saya tahu. Tunggu kejap. |
| kejap | daily-life/story/grab_pickup.ink | 29 | 17 | Ahh, lain pintu. Okey, okey, saya tahu bank tu. Tunggu kejap. |
| komplen | office/story/meeting_disagree.ink | 9 | 17 | Diam, kemudian komplen nanti. |
| motor | social/ladders.json | 1758 | - | Boleh encik bagi satu hari? Kami perlu motor itu untuk demo. |
| motor | social/ladders.json | 1765 | - | Boleh encik beri tarikh yang tepat? Kami perlukan motor itu sebelum demo pada 20 |
| motor | social/ladders.json | 1786 | - | Motor sampai hari Selasa, 17hb. Sebelum tengah hari. |
| motor | social/ladders.json | 1793 | - | Berita baik: motor sampai hari Selasa 17hb, sebelum tengah hari. Dia akan hantar |
| motor | social/ladders.json | 1801 | - | Versi pendek: barang dari kilang lambat, tapi motor akan tiba hari Selasa 17hb,  |
| motor | social/story/jinx_late_parts.ink | 8 | 17 | Bengkel Jinx. Dua ratus motor kecil untuk dron dia sepatutnya sampai hari Isnin. |
| motor | social/story/jinx_late_parts.ink | 35 | 17 | Boleh encik bagi satu hari? Kami perlu motor itu untuk demo. |
| motor | social/story/jinx_late_parts.ink | 37 | 17 | Boleh encik beri tarikh yang tepat? Kami perlukan motor itu sebelum demo pada 20 |
| motor | social/story/jinx_late_parts.ink | 53 | 17 | Bila motor itu akan sampai? |
| motor | social/story/jinx_late_parts.ink | 65 | 17 | Motor sampai hari Selasa, 17hb. Sebelum tengah hari. |
| motor | social/story/jinx_late_parts.ink | 66 | 17 | Berita baik: motor sampai hari Selasa 17hb, sebelum tengah hari. Dia akan hantar |
| motor | social/story/jinx_late_parts.ink | 67 | 17 | Versi pendek: barang dari kilang lambat, tapi motor akan tiba hari Selasa 17hb,  |
| motor | social/vocab.json | 1693 | - | Tolong call   tentang motor itu. |
| motor | social/vocab.json | 1732 | - | Ringkasnya, motor sampai Selasa. |
| motor | social/vocab.json | 1736 | - | , motor itu sampai hari Selasa. |
| takkan | home-condo/ladders.json | 681 | - | Encik memang betul, dan saya minta maaf kerana buat encik lewat. Ia takkan berul |
| takkan | home-condo/story/blocked_car.ink | 34 | 16 | Encik memang betul, dan saya minta maaf kerana buat encik lewat. Ia takkan berul |
| takkan | social/ladders.json | 1527 | - | Saya takkan lepaskan peluang ini! Cuma, saya ada latihan sampai pukul 5, jadi sa |
| takkan | social/ladders.json | 1536 | - | Saya takkan lepaskan peluang ini! Malangnya, saya terikat dengan latihan sehingg |
| takkan | social/ladders.json | 1943 | - | Takkan saya nak lepaskan peluang! Selepas penat dikejar kamu berdua satu padang, |
| takkan | social/story/mamak_lepak.ink | 15 | 17 | Takkan saya nak lepaskan peluang! Selepas penat dikejar kamu berdua satu padang, |
| takkan | social/story/wedding_invite.ink | 11 | 17 | Saya takkan lepaskan peluang ini! Cuma, saya ada latihan sampai pukul 5, jadi sa |
| takkan | social/story/wedding_invite.ink | 12 | 17 | Saya takkan lepaskan peluang ini! Malangnya, saya terikat dengan latihan sehingg |
| takkan | social/vocab.json | 1580 | - | Saya takkan lepaskan peluang ini! |
| takkan | social/vocab.json | 1584 | - | Saya takkan lepaskan   ini! |
| tau | daily-life/story/phone_plan.ink | 21 | 14 | Fon telinga percuma, tau! Kualiti sangat bagus! |
| tau | social/story/weekend_plans.ink | 29 | 17 | Bila-bila? Nanti panas sangat, tau. |

### At the chapter tag: 9982 entries before, 9994 after

New hits: **45** (all register: the seven new chapter 17 pairs). Gaps or violations that disappear: **33**.

| Hit | File | Line | Chapter tag | Text |
| --- | --- | ---: | --- | --- |
| je | office/ladders.json | 1336 | - | Mana ada, biasa je! Tapi terima kasih. |
| je | office/ladders.json | 1363 | - | Tak ada date! Kerja je. Awak pula? Hujung minggu okey? |
| je | office/ladders.json | 1370 | - | Haha, mana ada date, mesyuarat dengan Encik Lim je! Awak pula? Hujung minggu bes |
| je | office/minigames.json | 327 | - | Jangan ambil hati, saya gurau je. |
| je | office/story/pantry_banter.ink | 11 | 17 | Mana ada, biasa je! Tapi terima kasih. |
| je | office/story/pantry_banter.ink | 14 | 17 | Tak, baju ni buruk. Murah je. |
| je | office/story/pantry_banter.ink | 23 | 17 | Hmm, diam je... mencurigakan ni. 😏 |
| je | office/story/pantry_banter.ink | 30 | 17 | Wah, seriusnya! Relaks, saya gurau je. |
| je | office/story/pantry_banter.ink | 34 | 17 | Oh... maaf, maaf. Gurau je. |
| je | office/story/pantry_banter.ink | 36 | 17 | Tak ada date! Kerja je. Awak pula? Hujung minggu okey? |
| je | office/story/pantry_banter.ink | 38 | 17 | Haha, mana ada date, mesyuarat dengan Encik Lim je! Awak pula? Hujung minggu bes |
| je | office/story/pantry_banter.ink | 62 | 17 | Hahaha, tengok muka awak! Saya gurau je. Jangan ambil hati, makan tengah hari te |
| je | social/story/mamak_lepak.ink | 31 | 17 | Biasa je. |
| je | social/story/mamak_lepak.ink | 32 | 17 | "Biasa je" saja? 🙄 |
| je | social/story/mamak_lepak.ink | 36 | 17 | Wah, maaf, tanya je. |
| je | social/story/mamak_lepak.ink | 72 | 17 | Er... "okey" je? Terima kasih pun jadilah. 😅 |
| kejap | daily-life/story/grab_pickup.ink | 23 | 17 | Oh, Pintu A? Tak apa, tunggu kejap. |
| kejap | daily-life/story/grab_pickup.ink | 26 | 17 | Oh, sebelah bank. Okey, saya tahu. Tunggu kejap. |
| kejap | daily-life/story/grab_pickup.ink | 29 | 17 | Ahh, lain pintu. Okey, okey, saya tahu bank tu. Tunggu kejap. |
| komplen | office/story/meeting_disagree.ink | 9 | 17 | Diam, kemudian komplen nanti. |
| motor | social/ladders.json | 1758 | - | Boleh encik bagi satu hari? Kami perlu motor itu untuk demo. |
| motor | social/ladders.json | 1765 | - | Boleh encik beri tarikh yang tepat? Kami perlukan motor itu sebelum demo pada 20 |
| motor | social/ladders.json | 1786 | - | Motor sampai hari Selasa, 17hb. Sebelum tengah hari. |
| motor | social/ladders.json | 1793 | - | Berita baik: motor sampai hari Selasa 17hb, sebelum tengah hari. Dia akan hantar |
| motor | social/ladders.json | 1801 | - | Versi pendek: barang dari kilang lambat, tapi motor akan tiba hari Selasa 17hb,  |
| motor | social/story/jinx_late_parts.ink | 8 | 17 | Bengkel Jinx. Dua ratus motor kecil untuk dron dia sepatutnya sampai hari Isnin. |
| motor | social/story/jinx_late_parts.ink | 35 | 17 | Boleh encik bagi satu hari? Kami perlu motor itu untuk demo. |
| motor | social/story/jinx_late_parts.ink | 37 | 17 | Boleh encik beri tarikh yang tepat? Kami perlukan motor itu sebelum demo pada 20 |
| motor | social/story/jinx_late_parts.ink | 53 | 17 | Bila motor itu akan sampai? |
| motor | social/story/jinx_late_parts.ink | 65 | 17 | Motor sampai hari Selasa, 17hb. Sebelum tengah hari. |
| motor | social/story/jinx_late_parts.ink | 66 | 17 | Berita baik: motor sampai hari Selasa 17hb, sebelum tengah hari. Dia akan hantar |
| motor | social/story/jinx_late_parts.ink | 67 | 17 | Versi pendek: barang dari kilang lambat, tapi motor akan tiba hari Selasa 17hb,  |
| motor | social/vocab.json | 1693 | - | Tolong call   tentang motor itu. |
| motor | social/vocab.json | 1732 | - | Ringkasnya, motor sampai Selasa. |
| motor | social/vocab.json | 1736 | - | , motor itu sampai hari Selasa. |
| takkan | home-condo/ladders.json | 681 | - | Encik memang betul, dan saya minta maaf kerana buat encik lewat. Ia takkan berul |
| takkan | social/ladders.json | 1527 | - | Saya takkan lepaskan peluang ini! Cuma, saya ada latihan sampai pukul 5, jadi sa |
| takkan | social/ladders.json | 1536 | - | Saya takkan lepaskan peluang ini! Malangnya, saya terikat dengan latihan sehingg |
| takkan | social/ladders.json | 1943 | - | Takkan saya nak lepaskan peluang! Selepas penat dikejar kamu berdua satu padang, |
| takkan | social/story/mamak_lepak.ink | 15 | 17 | Takkan saya nak lepaskan peluang! Selepas penat dikejar kamu berdua satu padang, |
| takkan | social/story/wedding_invite.ink | 11 | 17 | Saya takkan lepaskan peluang ini! Cuma, saya ada latihan sampai pukul 5, jadi sa |
| takkan | social/story/wedding_invite.ink | 12 | 17 | Saya takkan lepaskan peluang ini! Malangnya, saya terikat dengan latihan sehingg |
| takkan | social/vocab.json | 1580 | - | Saya takkan lepaskan peluang ini! |
| takkan | social/vocab.json | 1584 | - | Saya takkan lepaskan   ini! |
| tau | social/story/weekend_plans.ink | 29 | 17 | Bila-bila? Nanti panas sangat, tau. |

| Gone | Kind | File | Line | Chapter tag | Text |
| --- | --- | --- | ---: | --- | --- |
| banyak-banyak | gap ledger gap | office/story/report_deadline.ink | 98 | 17 | Terima kasih banyak-banyak kerana menghantar angka itu tepat pada masanya. Sanga |
| belon | violation affix | social/story/trio_surprise_party.ink | 24 | 17 | Jess, tolong buat belon dan konfeti. Puan Tan, tolong cakap masanya kepada tetam |
| belon | violation affix | social/story/trio_surprise_party.ink | 26 | 17 | Jess, boleh buat belon dan konfeti, tapi tak ada bunga api dalam bilik? Puan Tan |
| belon | violation affix | social/story/trio_surprise_party.ink | 28 | 17 | Jess, boleh uruskan hiasan, belon dan konfeti, tetapi tiada apa-apa yang meletup |
| belon | violation affix | social/story/trio_surprise_party.ink | 30 | 17 | Jess, awak bertanggungjawab atas hiasan: belon dan konfeti sebanyak mana pun, cu |
| cepat-cepat | gap ledger gap | daily-life/story/hotel_checkin.ink | 71 | 16 | Ada lima belas minit lagi. Anda cepat-cepat turun. |
| gula-gula | gap ledger gap | social/story/miku_sore_throat.ink | 49 | 14 | Gula-gula ubat ini berkesan. Oh, sekejap: dia alah pada apa-apa? |
| hari-hari | gap ledger gap | daily-life/story/grab_pickup.ink | 102 | 17 | Alah, tak apa. Hari-hari jadi macam ni kat sini. |
| hari-hari | gap ledger gap | daily-life/story/grab_pickup.ink | 105 | 17 | Alah, tak payah berterima kasih. Hari-hari jadi macam ni kat sini. |
| kawan-kawan | gap ledger gap | daily-life/story/price_haggle.ink | 63 | 17 | Bolehkah kita ambil jalan tengah pada RM60? Tunai, sekarang juga, dan saya akan  |
| kira-kira | gap ledger gap | daily-life/story/card_blocked.ink | 22 | 16 | Hai, kad debit saya ditolak dua kali di sebuah pasar raya kira-kira sepuluh mini |
| kira-kira | gap ledger gap | daily-life/story/grab_ride_chat.ink | 13 | 17 | Asalnya dari Jepun. Saya berpindah ke sini kira-kira setahun lalu, jadi KL sudah |
| kira-kira | gap ledger gap | daily-life/story/post_parcel.ink | 25 | 17 | Pos udara atau pos laut? Pos udara kira-kira seminggu, RM98. Pos laut kira-kira  |
| kira-kira | gap ledger gap | home-condo/story/new_neighbour.ink | 29 | 17 | Asalnya dari Osaka. Syarikat menghantar saya ke sini kira-kira sebulan lalu. Enc |
| kira-kira | gap ledger gap | office/story/team_dinner.ink | 75 | 17 | Maaf sangat, mesyuarat saya terlajak masa. Saya sampai dalam kira-kira 20 minit. |
| kira-kira | gap ledger gap | office/story/team_dinner.ink | 77 | 17 | Maaf sangat-sangat, mesyuarat saya berlarutan. Saya bertolak sekarang dan sepatu |
| kira-kira | gap ledger gap | social/story/trio_surprise_party.ink | 46 | 17 | Hai, saya berhasrat untuk menempah sebiji kek hari jadi untuk Sabtu ini, mencuku |
| kira-kira | gap ledger gap | social/story/weekend_plans.ink | 62 | 17 | 7.30 pagi. Anda akan lambat kira-kira sepuluh minit. |
| kira-kira | gap ledger gap | social/story/weekend_plans.ink | 69 | 17 | Maaf sangat, saya tersangkut dalam kesesakan. Saya sampai dalam kira-kira 10 min |
| lagu-lagu | gap ledger gap | social/story/miku_karaoke.ink | 42 | 17 | Maaf, satu soalan lagi: adakah minuman percuma itu termasuk minuman panas? Rakan |
| lagu-lagu | gap ledger gap | social/story/trio_road_trip.ink | 39 | 17 | Yeay! Lagu-lagu hebat Miku sepanjang jalan! 🎶 |
| main-main | gap ledger gap | daily-life/story/grab_ride_chat.ink | 75 | 17 | Terima kasih, saya seronok berbual. Semoga perjalanan encik menyeronokkan, dan b |
| malam-malam | gap ledger gap | home-condo/story/new_neighbour.ink | 49 | 17 | Maaf sangat ganggu malam-malam! Maaf sangat! |
| meriah | violation affix | social/story/jinx_fireworks.ink | 47 | 17 | Parti itu meriah. Pukul 8.55 malam, tetamu mula tanya tentang bunga api. |
| nombor-nombor | gap ledger gap | office/story/feedback_junior.ink | 17 | 14 | Dengan senang hati. Analisisnya memang mantap; cuma ringkaskan teks supaya nombo |
| pagi-pagi | gap ledger gap | office/story/pantry_banter.ink | 50 | 17 | Jangan layan dia sangat. Pagi-pagi pun dah mulut murai. |
| sangat-sangat | gap ledger gap | daily-life/story/grab_pickup.ink | 106 | 17 | Maaf sangat-sangat. Saya betul-betul minta maaf. Maaf, saya buat susah. |
| sangat-sangat | gap ledger gap | office/story/team_dinner.ink | 77 | 17 | Maaf sangat-sangat, mesyuarat saya berlarutan. Saya bertolak sekarang dan sepatu |
| satu-satu | gap ledger gap | home-condo/story/visitor_parking.ink | 22 | 14 | Perlahan sikit, bos. Satu-satu huruf. |
| sebelah-sebelah | gap ledger gap | social/story/trio_movie_night.ink | 46 | 14 | Empat tiket muzikal. Tempat duduk sebelah-sebelah. |
| sebelah-sebelah | gap ledger gap | social/story/trio_movie_night.ink | 47 | 14 | Empat tiket muzikal pukul 8 malam. Boleh kami duduk sebelah-sebelah? |
| sedap-sedap | gap ledger gap | social/story/miku_drinks_run.ink | 26 | 17 | Buat sedap-sedap. |
| seronok-seronok | gap ledger gap | office/story/annual_leave.ink | 69 | 16 | Tak ada masalah. Seronok-seronok di Melbourne! |

