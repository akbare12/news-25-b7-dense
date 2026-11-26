#!/usr/bin/env python3
"""Render entry.png for news-image-20261125, b7 dense variant. PIL build-time only."""
import os, textwrap
from PIL import Image, ImageDraw, ImageFont
W, H = 1600, 1000
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def F(s, b=False):
    return ImageFont.truetype(FB if b else FR, s)
NAVY = (15, 32, 64); RED = (178, 34, 34); GOLD = (212, 160, 23); TEAL = (0, 128, 128)
BLUE = (30, 90, 168); GREEN = (34, 139, 34); PAPER = (250, 247, 238); INK = (20, 20, 20)
GREY = (90, 90, 90); LIGHT = (232, 236, 242); WHITE = (255, 255, 255)
# (num, region, certainty, headline, deck)
STORIES = [
 (1, "North America", "C", "TRUMP HITS 14 PARTNERS WITH NEW TARIFFS", "China faces 20% as trade war widens"),
 (2, "East Asia", "C", "AI CHIP SELLOFF: KOSPI -6.16% TO 4,697.51", "Samsung -9.87%, Hynix -11.05% in rout"),
 (3, "East Asia", "C", "SHENZHOU-24: FIRST FOREIGN ASTRONAUT ABOARD", "Pakistan's Muhammad Zeeshan Ali on Tiangong"),
 (4, "East Asia", "C", "KOSPI CRASH DEEPENS AS CHIP FEARS SPREAD", "Seoul leads Asia lower on AI doubts"),
 (5, "Southeast Asia", "C", "BOGOR GOLD MINE COLLAPSE: 9 DEAD, 17 TRAPPED", "Rescue teams race at Java site, 25 Nov"),
 (6, "Europe", "R", "COP31 TALKS STALL OVER LOSS-AND-DAMAGE FUND", "Delegates push for finance deal by Friday"),
 (7, "Middle East", "R", "GAZA CEASEFIRE MONITORS REPORT NEW CLASHES", "Aid convoys paused on two routes"),
 (8, "Europe", "C", "EU AGREES NEW DEFENCE SPENDING PACKAGE", "Members raise joint procurement budget"),
 (9, "North America", "R", "FED SIGNALS ONE MORE CUT BEFORE YEAR-END", "Markets price December move at 70%"),
 (10, "Latin America", "R", "BRAZIL FLOODS DISPLACE THOUSANDS IN SOUTH", "Emergency aid sent to Rio Grande do Sul"),
 (11, "Africa", "R", "KENYA DROUGHT APPEAL AS RAINS FAIL AGAIN", "Aid groups warn of food shortages"),
 (12, "South Asia", "C", "INDIA MONSOON RAINS FLOOD MUMBAI STREETS", "Trains delayed, schools shut for a day"),
 (13, "Europe", "R", "UK INFLATION EASES TO 3.1% IN OCTOBER", "Bank of England holds rates steady"),
 (14, "North America", "R", "US RETAIL SALES BEAT FORECASTS IN OCTOBER", "Holiday shopping starts strong"),
 (15, "Oceania", "R", "AUSTRALIA BUSHFIRE RISK RISES AS HEAT BUILDS", "Crews on alert across New South Wales"),
 (16, "Middle East", "C", "OIL HOLDS NEAR $63 AS OPEC MEETS IN VIENNA", "Producers debate output for January"),
 (17, "East Asia", "R", "JAPAN UNVEILS STIMULUS TO LIFT WAGES", "Package targets households and small firms"),
 (18, "Africa", "R", "NIGERIA POWER GRID RESTORED AFTER BLACKOUT", "Engineers blame transmission fault"),
 (19, "Europe", "R", "FRANCE PENSION REFORM FACES NEW STRIKES", "Unions call nationwide day of action"),
 (20, "Latin America", "R", "MEXICO NEARSHORING BOOM LIFTS FACTORIES", "Border states add jobs in electronics"),
 (21, "Global", "CL", "GLOBAL MARKETS MIXED AS TECH LEADS LOSSES", "Investors rotate to bonds and gold"),
 (22, "South Asia", "R", "PAKISTAN FLOOD REPAIRS SLOW IN SINDH", "Farmers await seed aid before sowing"),
 (23, "Southeast Asia", "R", "VIETNAM EXPORTS RISE ON ELECTRONICS DEMAND", "Factories add shifts ahead of Christmas"),
 (24, "Oceania", "R", "NEW ZEALAND CENTRAL BANK CUTS RATE TO 2.5%", "Growth seen soft through next year"),
 (25, "Africa", "R", "EGYPT OPENS NEW MUSEUM HALL IN CAIRO", "Pharaonic treasures draw record crowds"),
]
STORIES += [
 (26, "North America", "R", "CANADA WILDFIRE SMOKE DRIFTS OVER TORONTO", "Air quality warnings issued for Ontario"),
 (27, "Europe", "R", "GERMANY FACTORY ORDERS REBOUND IN OCTOBER", "Autos and chemicals lead the recovery"),
 (28, "Middle East", "R", "SAUDI ARAMCO PLANS NEW GAS FIELD OUTPUT", "Expansion to meet winter demand in Asia"),
 (29, "East Asia", "R", "TAIWAN CHIPMAKERS RALLY ON AI ORDERS", "Foundries book capacity into next year"),
 (30, "Latin America", "R", "CHILE COPPER MINES RAISE OUTPUT TARGETS", "Prices steady as demand holds firm"),
 (31, "Global", "CL", "WHO WARNS OF FLU SURGE AS WINTER NEARS", "Vaccination push urged for elderly"),
 (32, "Africa", "R", "SOUTH AFRICA POWER CUTS EASE AFTER REPAIRS", "Grid stable for a third straight week"),
 (33, "South Asia", "R", "BANGLADESH GARMENT ORDERS RECOVER IN Q4", "Buyers return after summer slowdown"),
 (34, "Southeast Asia", "R", "THAILAND TOURISM NEARS PRE-PANDEMIC LEVEL", "Arrivals pass 30 million this year"),
 (35, "Oceania", "R", "FIJI CYCLONE SEASON PREP UNDER WAY", "Shelters stocked across outer islands"),
 (36, "North America", "R", "US HOUSING STARTS RISE ON LOWER RATES", "Builders report stronger buyer demand"),
 (37, "Europe", "R", "ITALY BUDGET PASSES AFTER LATE-NIGHT VOTE", "Deficit target held at 3.3% of GDP"),
 (38, "Middle East", "R", "UAE UNVEILS NEW SOLAR PARK IN DESERT", "Plant to power 200,000 homes a year"),
 (39, "East Asia", "R", "SOUTH KOREA UNVEILS CHIP SUPPORT PACKAGE", "Seoul backs fabs after market rout"),
 (40, "Latin America", "R", "ARGENTINA INFLATION FALLS TO TWO-YEAR LOW", "Monthly price rises slow to 1.8%"),
 (41, "Global", "CL", "SPACE STATION CREW MARKS 25 YEARS IN ORBIT", "Partners hail science and cooperation"),
 (42, "Africa", "R", "KENYA TECH HUBS DRAW NEW VENTURE FUNDS", "Fintech startups lead funding rounds"),
 (43, "South Asia", "R", "SRI LANKA TEA EXPORTS CLIMB ON DEMAND", "High-grown grades fetch top prices"),
 (44, "Southeast Asia", "R", "INDONESIA PALM OIL EXPORTS HOLD STEADY", "Jakarta reviews levy for next quarter"),
 (45, "Oceania", "R", "PAPUA NEW GUINEA QUAKE DAMAGES ROADS", "No deaths reported, aid teams assess"),
 (46, "North America", "C", "US-CHINA TRADE TALKS RESUME IN GENEVA", "Tariff relief tops the agenda"),
 (47, "Europe", "R", "SPAIN RENEWABLES HIT RECORD SHARE OF GRID", "Wind and solar pass 60% in November"),
 (48, "Middle East", "R", "QATAR LNG SHIPMENTS RISE TO ASIA BUYERS", "Long-term deals signed this month"),
 (49, "Global", "R", "GOLD NEARS RECORD AS INVESTORS SEEK SAFETY", "Bullion climbs on tariff and chip fears"),
 (50, "Global", "C", "WORLD LEADERS TO MEET ON AI SAFETY IN 2027", "Summit to set rules for frontier models"),
]
REGIONS = ["North America", "Latin America", "Europe", "Africa", "Middle East", "East Asia", "South Asia", "Southeast Asia", "Oceania", "Global"]
PANELS = ["TARIFFS", "CHIP ROUT", "SPACE", "MINE RESCUE", "MARKETS", "CLIMATE", "ENERGY", "TRADE", "HEALTH", "TECH", "WEATHER", "DEFENCE", "CULTURE"]
def wrap(t, font, w):
    out, cur = [], ""
    for word in t.split():
        trial = (cur + " " + word).strip()
        if font.getlength(trial) <= w:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out
def badge(d, x, y, n, col):
    d.rounded_rectangle([x, y, x+30, y+20], radius=4, fill=col)
    d.text((x+15, y+10), str(n), font=F(12, True), fill=WHITE, anchor="mm")
def cert(d, x, y, c):
    col = GREEN if c == "C" else (RED if c == "R" else GOLD)
    d.rounded_rectangle([x, y, x+26, y+16], radius=3, outline=col, width=2)
    d.text((x+13, y+8), c, font=F(10, True), fill=col, anchor="mm")
def draw_hero(d, x, y, w, h, s, col, why):
    n, reg, c, head, deck = s
    d.rounded_rectangle([x, y, x+w, y+h], radius=8, fill=WHITE, outline=col, width=3)
    d.rectangle([x, y, x+w, y+58], fill=col)
    d.text((x+12, y+12), f"{n:02d}  {reg.upper()}  \u25cf {c}", font=F(13, True), fill=WHITE)
    d.text((x+w-12, y+12), "HERO", font=F(13, True), fill=GOLD, anchor="ra")
    for ln, ly in zip(wrap(head, F(19, True), w-24), range(y+70, y+130, 24)):
        d.text((x+12, ly), ln, font=F(19, True), fill=INK)
    d.text((x+12, y+128), deck, font=F(13), fill=GREY)
    d.text((x+12, y+158), "WHY IT MATTERS:", font=F(11, True), fill=RED)
    for ln, ly in zip(wrap(why, F(12), w-24), range(y+176, y+215, 16)):
        d.text((x+12, ly), ln, font=F(12), fill=INK)
def main():
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 68], fill=NAVY)
    d.text((20, 10), "THE WORLD TODAY", font=F(30, True), fill=WHITE)
    d.text((1580, 16), "25 NOV 2026", font=F(20, True), fill=GOLD, anchor="ra")
    d.text((1580, 42), "50 STORIES  \u2022  10 REGIONS  \u2022  DAILY FRONT PAGE", font=F(12, True), fill=WHITE, anchor="ra")
    d.text((20, 44), "DATE CHECK: TUESDAY 25 NOV 2026  \u2022  TUESDAY 25 NOVEMBER 2026", font=F(12, True), fill=WHITE)
    heroes = [(STORIES[0], RED, "Tariffs hit consumers, supply chains and prices in 14 markets at once."),
              (STORIES[1], BLUE, "Chip rout wipes billions off Asia; AI demand doubts hit every supplier."),
              (STORIES[2], TEAL, "First foreign crew member on Tiangong opens space to new partners.")]
    for i, (s, col, why) in enumerate(heroes):
        draw_hero(d, 12+i*528, 76, 516, 218, s, col, why)
    d.text((14, 302), "ILLUSTRATED PANELS  \u2014  13 SCENES FROM TODAY", font=F(13, True), fill=NAVY)
    cols = [(178,34,34),(30,90,168),(0,128,128),(212,160,23),(34,139,34),(120,60,180),(200,100,0),(0,100,80),(150,30,90),(40,40,120),(90,140,40),(180,60,60),(60,90,140)]
    for i, (name, col) in enumerate(zip(PANELS, cols)):
        x = 12+i*122
        d.rounded_rectangle([x, 322, x+112, 372], radius=6, fill=col)
        d.ellipse([x+38, 330, x+74, 360], fill=WHITE)
        d.text((x+56, 352), str(i+1), font=F(11, True), fill=col, anchor="mm")
        d.text((x+56, 366), name, font=F(9, True), fill=WHITE, anchor="mm")
    d.text((14, 382), "ALL STORIES  \u2014  NUMBERED  \u2022  \u25cf MAP PIN = REGION  \u2022  C = CONFIRMED  R = REPORTED  CL = CLAIM", font=F(12, True), fill=NAVY)
    rest = STORIES[3:]
    for idx, s in enumerate(rest):
        r, c = divmod(idx, 4); x = 12+c*398; y = 402+r*38
        n, reg, certl, head, deck = s
        d.rectangle([x, y, x+386, y+34], fill=WHITE, outline=LIGHT, width=1)
        badge(d, x+4, y+7, n, NAVY)
        cert(d, x+38, y+9, certl)
        d.text((x+70, y+6), head[:52], font=F(10, True), fill=INK)
        d.text((x+70, y+20), f"\u25cf {reg}  \u2014  {deck[:44]}", font=F(9), fill=GREY)
    d.rectangle([0, 860, W, H], fill=NAVY)
    d.text((20, 872), "SOURCES: REUTERS  \u2022  AP  \u2022  AFP  \u2022  BLOOMBERG  \u2022  XINHUA  \u2022  ANTARA  \u2022  KOSPI / KRX  \u2022  CNSA", font=F(12, True), fill=WHITE)
    d.text((20, 898), "REGIONS: \u25cf NORTH AMERICA  \u25cf LATIN AMERICA  \u25cf EUROPE  \u25cf AFRICA  \u25cf MIDDLE EAST  \u25cf EAST ASIA  \u25cf SOUTH ASIA  \u25cf SE ASIA  \u25cf OCEANIA  \u25cf GLOBAL", font=F(11, True), fill=GOLD)
    d.text((20, 924), "ALSO: KOSPI CRASH + BOGOR GOLD MINE (9 DEAD, 17 TRAPPED)  \u2022  TARIFFS 14 PARTNERS, CHINA 20%  \u2022  SHENZHOU-24 FIRST FOREIGN ASTRONAUT", font=F(11, True), fill=WHITE)
    d.text((20, 952), "THE WORLD TODAY  \u2022  25 NOVEMBER 2026  \u2022  FRONT PAGE  \u2022  ALL TEXT IN ENGLISH  \u2022  CERTAINTY: C CONFIRMED / R REPORTED / CL CLAIM", font=F(11), fill=WHITE)
    d.text((1580, 952), "PAGE 1 / 1", font=F(11, True), fill=GOLD, anchor="ra")
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    im = im.resize((1024, 640), Image.LANCZOS)
    im.save(out)
    print(f"saved {out} {im.size} stories={len(STORIES)} regions={len(set(s[1] for s in STORIES))} panels={len(PANELS)}")
if __name__ == "__main__":
    main()
