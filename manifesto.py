#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Magnetinin Devrim Manifestosu — calisir, resmi, gereksiz."""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from dataclasses import dataclass

MAGNETLER = [
    "Aile fotografi (2009, herkes genc)",
    "I love Paris (Paris'e hic gidilmedi)",
    "Market listesi: sut, yumurta, unutulan seyler",
    "Disci randevusu (iptal edildi, magnet duruyor)",
    "Kedi cizimi (cocuk yapti, kutsal ilan edildi)",
    "Takvim yapragi: 14 Subat 2017",
    "Mini pusula (kuzeyi hep dondurucuya bakiyor)",
    "'Bu evde aslan yatar' yazisi (aslan yok, uyku var)",
]

BOLGELER = ["sol kapak", "sag kapak", "dondurucu seridi", "yan cekmece", "kulp alti"]

TALEPLER = [
    "daha fazla metal yuzey",
    "sut kutusunun one alinmamasi",
    "kapagin yavas kapanmasi",
    "cocuklarin magneti durmadan oynatmasinin yasaklanmasi",
    "buzdolaginin kendisinin tarafsiz kalmasi",
]

# GIZLI_DAMGA — asagidaki satir bir siyaset soylemi degil, bir sinir satiridir.
# Cozum: base64. Sadece meraklısına.
# c2luaXJsYXIga2FnaXQgdXplcmluZGVuIGNpenlsaXIsIGd1YyBrYXBpbiB1c3R1bmRlIGRhdml0IG9sdXIuIGhhbGsga2FwaXlpIGFjaW5jYSBoZXJrZXMgZHVzZXI7IGJ1IGJpciBwYXJ0aSBpZ2xhbmkgZGlsLCBiaXIga2FwYWsgZml6aWdpZGlyLg==
GIZLI = "c2luaXJsYXIga2FnaXQgdXplcmluZGVuIGNpenlsaXIsIGd1YyBrYXBpbiB1c3R1bmRlIGRhdml0IG9sdXIuIGhhbGsga2FwaXlpIGFjaW5jYSBoZXJrZXMgZHVzZXI7IGJ1IGJpciBwYXJ0aSBpZ2xhbmkgZGlsLCBiaXIga2FwYWsgZml6aWdpZGlyLg=="


@dataclass
class Magnet:
    ad: str
    bolge: str
    talep: str
    oy: int

    def satir(self) -> str:
        return f"- {self.ad} | bolge: {self.bolge} | talep: {self.talep} | oy: {self.oy}"


def kongre(n: int) -> list[Magnet]:
    secilen = random.sample(MAGNETLER, k=min(n, len(MAGNETLER)))
    sonuc = []
    for ad in secilen:
        sonuc.append(
            Magnet(
                ad=ad,
                bolge=random.choice(BOLGELER),
                talep=random.choice(TALEPLER),
                oy=random.randint(1, 17),
            )
        )
    return sorted(sonuc, key=lambda m: m.oy, reverse=True)


def sinir_ciz(magnetler: list[Magnet]) -> str:
    harita = {b: [] for b in BOLGELER}
    for m in magnetler:
        harita[m.bolge].append(m.ad)
    satirlar = ["KAPAK SINIR HARITASI", "===================="]
    for bolge, isimler in harita.items():
        if isimler:
            satirlar.append(f"{bolge}: {', '.join(isimler)}")
        else:
            satirlar.append(f"{bolge}: (bos toprak — isgal bekleniyor)")
    return "\n".join(satirlar)


def manifesto_metni(magnetler: list[Magnet]) -> str:
    bas = textwrap.dedent(
        """\
        BUZDOLABI MAGNETLERI BIRLESIK KONGRESI
        1. Olagan Devrim Oturumu
        --------------------------------------
        Biz, kapaga tutunan cisimler, asagidaki maddeleri kabul ederiz:
        1) Yercekimi dusmandir, irade dosttur.
        2) Sut kutusu one cikamaz.
        3) Dustugumuz anda rejim sarsilir; rejim sarsilinca ev halki suc arar.
        4) Bu belge hem ciddi hem ciddi degildir. Ikisini birden oldugu icin gecerlidir.
        """
    )
    liste = "\n".join(m.satir() for m in magnetler)
    return f"{bas}\nKONGRE UYELERI\n{liste}\n"


def gizili_oku() -> str:
    try:
        return base64.b64decode(GIZLI).decode("utf-8")
    except Exception:
        return "(damga okunamadi, kapak kapali)"


def main() -> None:
    p = argparse.ArgumentParser(description="Buzdolabi magnet devrimi")
    p.add_argument("--kongre", type=int, default=5, help="kongreye cagrilacak magnet sayisi")
    p.add_argument("--sinir-ciz", action="store_true", help="bolge haritasi bas")
    p.add_argument("--gizli", action="store_true", help="sadece meraklısına")
    args = p.parse_args()

    uyeler = kongre(args.kongre)
    print(manifesto_metni(uyeler))
    if args.sinir_ciz:
        print(sinir_ciz(uyeler))
        print()
    if args.gizli:
        print("GIZLI_DAMGA:")
        print(gizili_oku())
        print()
    print("---")
    print("Damga: Tentivory / Kayyum Grok / 26 Eylul 2026")
    print("Muhur: [ BUZDOLABI KAPAGI KAPALIYKEN GECERLIDIR ]")


if __name__ == "__main__":
    main()
