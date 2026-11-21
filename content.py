# Shared content for the LEGO case study: used by app.py (Streamlit) and build_preview.py (static preview)
RED, YEL, BLUE, GREEN, DARK, PALE = "#D01012", "#FFCF00", "#006CB7", "#00AF4D", "#1A1A1A", "#FFF6D6"
TABCOL = [RED, YEL, BLUE, GREEN]

CSS = f"""
.cs {{ font-family: 'Helvetica Neue', Arial, sans-serif; color:#1F1F24; max-width:1150px; margin:0 auto; }}
.cs p, .cs li {{ line-height:1.6; color:#1F1F24; }}
.cs .banner {{ background:{RED}; border-radius:14px 14px 0 0; padding:1.8rem 2.2rem 1.5rem; position:relative; overflow:hidden; }}
.cs .stripe {{ height:8px; background:{YEL}; border-radius:0 0 14px 14px; margin-bottom:1.2rem; }}
.cs .tag {{ display:inline-block; background:{YEL}; color:#3A2A00 !important; font-weight:700; font-size:0.78rem; letter-spacing:0.05em; text-transform:uppercase; padding:0.25rem 0.75rem; border-radius:999px; }}
.cs .btitle {{ color:#FFFFFF !important; font-size:2.1rem; font-weight:800; margin:0.7rem 0 0.4rem; line-height:1.2; max-width:640px; }}
.cs .bsub {{ color:#FFE3E3 !important; font-size:1.05rem; max-width:640px; }}
.cs .by {{ color:#FFFFFF !important; margin-top:1rem; font-size:0.95rem; }}
.cs .by a {{ color:{YEL} !important; text-decoration:none; font-weight:700; }}
.cs .bricks {{ position:absolute; right:26px; top:22px; width:300px; height:150px; }}
.cs .brick {{ position:absolute; border-radius:5px; }}
.cs .stud {{ position:absolute; top:-9px; width:17px; height:9px; border-radius:4px 4px 0 0; }}
.cs .kpis {{ display:grid; grid-template-columns:repeat(4,1fr); gap:0.9rem; margin:0 0 1.2rem; }}
.cs .kpi {{ background:{PALE}; border-top:6px solid {RED}; border-radius:8px; padding:0.9rem 1rem; }}
.cs .kpi .v {{ font-size:1.7rem; font-weight:800; color:#5A1010 !important; }}
.cs .kpi .l {{ font-size:0.85rem; color:#6B4A12 !important; }}
.cs .nav {{ display:flex; flex-wrap:wrap; gap:0.45rem; margin:0 0 1.4rem; }}
.cs .nav a {{ text-decoration:none; font-weight:700; font-size:0.86rem; padding:0.5rem 0.85rem; border-radius:8px; }}
.cs .block {{ border:1px solid #F0D5D5; border-radius:12px; overflow:hidden; margin:0 0 1.6rem; background:#FFFFFF; scroll-margin-top:70px; }}
.cs .bh {{ padding:0.7rem 1.1rem; font-weight:800; font-size:1.05rem; }}
.cs .bh small {{ display:block; font-weight:700; font-size:0.72rem; letter-spacing:0.12em; opacity:0.85; }}
.cs .bb {{ padding:1rem 1.2rem 1.1rem; }}
.cs .cards {{ display:grid; grid-template-columns:repeat(3,1fr); gap:0.8rem; margin:0.4rem 0 0.9rem; }}
.cs .cards.two {{ grid-template-columns:repeat(2,1fr); }}
.cs .cards.four {{ grid-template-columns:repeat(4,1fr); }}
.cs .card {{ background:#FFFFFF; border:1px solid #ECECEC; border-top:5px solid {BLUE}; border-radius:8px; padding:0.8rem 0.9rem; }}
.cs .card h4 {{ margin:0 0 0.35rem; font-size:0.98rem; color:#14213D !important; }}
.cs .card div, .cs .card li {{ font-size:0.9rem; color:#3A4250 !important; }}
.cs .card ul {{ margin:0; padding-left:1.1rem; }}
.cs table.t {{ width:100%; border-collapse:collapse; margin:0.3rem 0 0.9rem; font-size:0.92rem; }}
.cs table.t th {{ background:{DARK}; color:#FFFFFF !important; text-align:left; padding:0.55rem 0.7rem; }}
.cs table.t td {{ border-bottom:1px solid #EEE; padding:0.55rem 0.7rem; vertical-align:top; color:#1F1F24 !important; }}
.cs table.t tr:nth-child(even) td {{ background:{PALE}; }}
.cs .note {{ background:{PALE}; border-left:5px solid {YEL}; padding:0.75rem 1rem; border-radius:6px; margin:0.5rem 0 0; color:#3A2A00 !important; }}
.cs .code {{ background:#F6F6F6; border:1px solid #E5E5E5; border-radius:6px; padding:0.6rem 0.8rem; font-family:Menlo,Consolas,monospace; font-size:0.82rem; color:#1A1A1A !important; margin:0.3rem 0 0.7rem; white-space:pre-wrap; }}
.cs .footer {{ background:{DARK}; color:#D9D9D9 !important; text-align:center; font-size:0.85rem; padding:0.8rem; border-radius:10px; margin-top:0.6rem; }}
@media (max-width:800px) {{ .cs .kpis, .cs .cards, .cs .cards.four {{ grid-template-columns:repeat(2,1fr); }} .cs .bricks {{ display:none; }} .cs .btitle {{ font-size:1.6rem; }} }}
"""

def brick(x, y, w, h, col, studs):
    s = "".join(f'<div class="stud" style="left:{8 + i*((w-16-17)/max(studs-1,1)):.0f}px;background:{col};"></div>' for i in range(studs))
    return f'<div class="brick" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{col};">{s}</div>'

BRICKS = '<div class="bricks">' + "".join([
    brick(0, 92, 96, 40, YEL, 4), brick(104, 100, 64, 32, "#FFFFFF", 2),
    brick(176, 92, 120, 40, BLUE, 4), brick(40, 38, 84, 38, GREEN, 3),
    brick(150, 38, 96, 38, YEL, 4), brick(250, 10, 50, 28, "#FFFFFF", 2),
]) + '</div>'

def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{v}</td>" for v in row) + "</tr>" for row in rows)
    return f'<table class="t"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'

def cards(items, cls=""):
    out = []
    for i, (t, b) in enumerate(items):
        col = TABCOL[(i + 2) % 4]
        out.append(f'<div class="card" style="border-top-color:{col};"><h4>{t}</h4><div>{b}</div></div>')
    return f'<div class="cards {cls}">' + "".join(out) + "</div>"

def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def note(t):
    return f'<div class="note">{t}</div>'

def p(t):
    return f"<p>{t}</p>"

BANNER = (
    '<div class="banner">' + BRICKS +
    '<span class="tag">Prepared for the LEGO Group · Global Executive Recruitment &amp; Sourcing</span>'
    '<div class="btitle">Hiring a VP of Digital Play: an executive search plan</div>'
    '<div class="bsub">A worked search from intake and market mapping through assessment, offer and appointment</div>'
    '<div class="by"><b>Adam Baig</b> · Executive Recruitment · London · '
    '<a href="https://www.linkedin.com/in/adambaiguk">LinkedIn</a> · '
    '<a href="https://github.com/SkynetAI-Labs">GitHub</a></div>'
    '</div><div class="stripe"></div>'
)

KPIS = '<div class="kpis">' + "".join(
    f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in [
        ("VP+", "Search level, global scope"), ("12 wks", "Target intake to accepted offer"),
        ("5–7", "Calibrated shortlist"), ("70%+", "Slate from passive sourcing")]
) + "</div>"

S = []  # (title, html)

S.append(("Intake & search strategy", p(
    "<b>The scenario.</b> The LEGO Group is investing in digital play: experiences that connect physical bricks with apps, "
    "games and online platforms. This worked example takes a confidential VP of Digital Play search from the first intake "
    "meeting to an accepted offer, run with rigour and pace. It is a hypothetical plan built on public information. No real candidates or executives are named.")
 + cards([
    ("Intake with the hiring leader", ul(["What the business must achieve in 24 months", "Must-haves vs trade-offs", "Hub location: Billund, London or Boston", "Fit across the multi-brand portfolio: consumer, education, digital and retail", "Confidentiality level and internal successors"])),
    ("Success profile", ul(["Has scaled a digital product or platform to millions of users", "Has led product, engineering and design together", "Brings child safety and privacy by design", "Works well in a values-led, family-owned culture"])),
    ("Search plan sign-off", ul(["Target company map and no-go list", "Assessment scorecard agreed up front", "Interview panel and decision owner", "Weekly update rhythm and timeline"])),
 ]) + table(["Scorecard area", "What good looks like", "Weight"], [
    ["Digital product leadership", "Built and scaled consumer digital experiences with measurable engagement", "30%"],
    ["Play and child-first judgement", "Designs for kids and families with safety, privacy and wellbeing built in", "20%"],
    ["Commercial impact", "Clear link between digital investment and revenue, retention or brand reach", "20%"],
    ["Leading through a matrix", "Influences across product, marketing, licensing and markets without direct control", "15%"],
    ["Culture and values", "Curiosity, humility and care, matched to the LEGO Group's values", "15%"],
 ]) + table(["Stakeholder", "Role in the search"], [
    ["Senior hiring leader and executive sponsor", "Owns the brief, the scorecard and the final decision"],
    ["HR business partner", "Organisation design, internal successors, values and culture interview"],
    ["Talent Acquisition community", "Shares market knowledge, internal referrals and regional sourcing support; avoids duplicate approaches"],
    ["Total Rewards", "Pay range, bonus and long-term incentive benchmarking"],
    ["Global Mobility", "Visa, relocation and family support across hubs"],
 ]) + note("Agreeing the scorecard before sourcing starts keeps the shortlist objective and speeds up decisions later.")))

S.append(("Global talent map", p(
    "The map covers company types and geographies, not individual names. It shows where proven digital play leaders sit "
    "today and how likely they are to move.")
 + cards([
    ("Gaming and interactive", "Console, mobile and online game studios; platform and live-ops leaders"),
    ("Kids and family digital", "Children's apps, edtech and family entertainment platforms"),
    ("Consumer tech and devices", "Connected devices, smart toys and consumer app businesses"),
    ("Entertainment and media", "Studios and streaming companies with franchise and IP experience"),
    ("Toys and games", "Global toy and games makers building hybrid physical-digital play"),
    ("Adjacent wildcards", "Sports, music and creator platforms with strong engagement models"),
 ]) + table(["Segment", "Typical title", "Fit", "Likely to move", "Priority"], [
    ["Step-up leaders", "Senior Director / Head of Digital Product", "High", "High", "Core"],
    ["Sitting VPs, large platforms", "VP Product / VP Digital Experiences", "High", "Medium", "Core"],
    ["Kids and family specialists", "GM / Head of Kids Digital", "High", "Medium", "Core"],
    ["Toy and games makers", "VP Digital / Digital Play Lead", "High", "Low–Medium", "Selective"],
    ["Wildcards", "Product or GM leaders from adjacent sectors", "Medium", "High", "Stretch"],
 ]) + table(["Region", "Talent depth", "Notes"], [
    ["UK and Europe", "Deep", "London, Nordics and Berlin game and kids-tech hubs; close to Billund"],
    ["North America", "Deepest", "West Coast gaming and platform leaders; Boston hub option"],
    ["Asia Pacific", "Growing", "Shanghai and Singapore hubs; mobile-first gaming experience"],
 ]) + table(["Hub", "Time zone", "How I would run it"], [
    ["Billund (HQ)", "CET", "Morning calls with London; decision meetings with HQ leaders"],
    ["London", "GMT", "Search base; overlaps with Europe all day and the US in the afternoon"],
    ["Boston", "ET", "Afternoon UK slots for candidates and stakeholders"],
    ["Shanghai and Singapore", "CST / SGT", "Early UK morning slots; local TA partners for cultural and language context"],
 ]) + note("Across regions and cultures: shared interview slots across time zones, local market context from regional TA partners, and one weekly update so every stakeholder sees the same picture.") + note("<b>Step-up leaders</b> who are ready for VP scope say yes more often and tend to outperform. I would weight the map towards them.")))

S.append(("Passive sourcing", p("Most leaders at this level are not looking. Sourcing combines research, network referrals and personal, discreet outreach.")
 + '<div class="code">("VP" OR "Vice President" OR "Head of" OR "General Manager") AND ("digital play" OR "kids digital" OR "family games" OR "digital experiences") AND (product OR platform OR "live ops") -recruiter</div>'
 + '<div class="code">site:linkedin.com/in ("Head of Digital Product" OR "VP Product") (kids OR family OR games) (London OR Copenhagen OR Boston)</div>'
 + cards([
    ("Channels", ul(["LinkedIn Recruiter and Boolean search", "Google X-ray and industry press", "Conference speaker lists and awards", "Referrals from trusted senior networks"])),
    ("Outreach sequence", ul(["Personal note tied to their work", "Follow-up with role context, no name until NDA", "Phone call to qualify interest", "Discreet first meeting"])),
    ("Active, upcoming and confidential", ul(["Active: live outreach to the target map", "Upcoming: warm pipelines built before roles open, from succession and workforce plans", "Confidential: codename, NDA and need-to-know updates"])),
    ("Pipeline targets", ul(["120–150 mapped profiles", "40–50 approached", "15–20 qualified calls", "5–7 on the shortlist"])),
 ], "two") + note("Confidential searches use a role codename until the candidate signs an NDA.")))

S.append(("Market intelligence", cards([
    ("Talent availability", "Digital product leaders with kids and family experience are scarce. Most sit in gaming, platforms or edtech."),
    ("Competitor landscape", "Toy makers, game studios and online platforms are all competing for children's time and for the same leaders."),
    ("Industry trends", "Hybrid physical-digital play, safer online spaces, AI-enabled creativity and screen-time scrutiny."),
], "") + table(["Insight for the hiring leader", "So what"], [
    ["Pay at large tech platforms is often higher, with heavy equity", "Lead with mission, scope and long-term bonus; agree a pay range early with Total Rewards"],
    ["Many strong leaders are US-based", "Agree early whether relocation, hybrid or a Boston base is acceptable"],
    ["Child safety and privacy experience is rare at VP level", "Treat it as essential, or plan to strengthen it in the leadership team"],
 ]) + note("I would share a short market snapshot after week 2 so the hiring leader can calibrate before the shortlist.")))

S.append(("Assessment & calibration", table(["Stage", "Who", "What we assess"], [
    ["Screening call", "Executive Recruitment", "Motivation, scope, pay expectations, mobility"],
    ["Competency interview", "Hiring leader + Executive Recruitment", "Scorecard areas, with evidence from past results"],
    ["Case conversation", "Digital and product leaders", "Approach to a real digital play challenge"],
    ["Values and culture", "HR business partner + peer VP", "Values fit, leading through a matrix"],
    ["Final meeting", "Executive sponsor", "Vision, judgement and alignment"],
    ["Referencing", "Executive Recruitment", "Discreet 360 references after the offer is agreed in principle"],
 ]) + cards([
    ("Calibration", "Review 2–3 profiles with the hiring leader in week 3 before the full slate goes out"),
    ("Objective scoring", "Every interviewer scores against the same scorecard, before any group discussion"),
    ("Trade-off advice", "Clear options when no one candidate has everything: what to hire for, what to build"),
 ]) + note("<b>Coaching leaders:</b> I would coach hiring leaders on market realities, candidate calibration, talent trade-offs and hiring decisions, and challenge thinking when the brief and the market do not match.")))

S.append(("Diverse, quality slate", cards([
    ("Segmentation", "Map women, international and under-represented leaders across every segment, not just one"),
    ("Wider pools", "Include adjacent sectors and step-up leaders so the slate isn't limited to one profile"),
    ("Fair process", "Same questions and scorecard for all; inclusive job content; varied interview panels"),
]) + table(["Slate goal", "Target"], [
    ["Gender balance on the shortlist", "At least 40% women"],
    ["International mix", "Candidates from at least 2 regions"],
    ["Sector mix", "At least 3 company types represented"],
 ])))

S.append(("Offer, mobility & onboarding", cards([
    ("Total Rewards", "Benchmark early, test pay expectations at every stage, no surprises at offer"),
    ("Global Mobility", "Visa, relocation, family and schooling support for Billund, London or Boston"),
    ("Candidate experience", "One point of contact, fast feedback within 48 hours, help with resignation and counter-offers"),
    ("Child safeguarding", "Explain the LEGO Group's Child Safeguarding Background Screening early, so it is expected and does not delay the offer"),
    ("Onboarding", "90-day plan agreed with the hiring leader; check-ins through the notice period and first months"),
    ("Mobility decisions", "Talk through relocation, schooling and family needs early, before the offer stage"),
]) + table(["Step", "Owner", "Timing"], [
    ["Verbal offer and pay check", "Executive Recruitment + Total Rewards", "Week 10"],
    ["Written offer and mobility package", "HR + Global Mobility", "Week 11"],
    ["Child Safeguarding Background Screening (role works closely on children's play experiences)", "HR + Executive Recruitment", "Week 11, condition of offer"],
    ["Acceptance and resignation support", "Executive Recruitment", "Week 12"],
    ["Pre-start check-ins and onboarding plan", "Hiring leader + HR", "Notice period"],
 ]) + note("Senior candidates often face counter-offers. Keeping in close contact during the notice period protects the hire.")))

S.append(("Candidate briefs & updates", cards([
    ("Candidate brief: Candidate A (example)", ul([
        "Current: Head of Digital Product at a global family entertainment platform",
        "Scaled a kids app to millions of monthly users across 30 markets",
        "Scorecard: strong on digital and play, developing on matrix leadership",
        "Motivation: wants a mission-led brand and wider scope",
        "Mobility: open to London, considering Billund"])),
    ("Weekly pipeline update", table(["Stage", "Count"], [
        ["Mapped", "140"], ["Approached", "46"], ["Qualified", "18"], ["Shortlisted", "6"], ["Final stage", "2"]])),
], "two") + note("Each update is one page: pipeline numbers, market insight, risks and the decisions needed this week.")))

S.append(("12-week timeline", table(["Weeks", "Milestone", "Output"], [
    ["1", "Intake and search strategy", "Success profile, scorecard, target map"],
    ["2–4", "Mapping and passive outreach", "Market snapshot, calibration profiles"],
    ["5–6", "Shortlist", "5–7 candidate briefs"],
    ["7–9", "Interviews and assessment", "Scored feedback, references"],
    ["10–12", "Offer and appointment", "Accepted offer, mobility plan"],
 ]) + cards([
    ("Time to shortlist", "Under 6 weeks"),
    ("Hiring leader satisfaction", "4.5 / 5 or higher"),
    ("Offer acceptance", "90%+"),
    ("Candidate experience", "Every candidate given feedback"),
], "four")))

S.append(("How I would work", cards([
    ("Executive search experience", "15 years of headhunting and executive search, including directors and C-suite, across the UK, Europe, the US, the Middle East and Africa"),
    ("Global, multi-business clients", "Led international director and C-suite placements for global groups with several businesses and brands, working across regions, cultures and time zones"),
    ("Mostly passive talent", "Around 70% of my hires came from outbound headhunting; offer acceptance of around 90–95%"),
    ("Data and AI tools", "I build my own sourcing and talent dashboards to map markets faster and report clearly"),
], "two") + note("Sound judgement, discretion and a personal approach to every search: anticipating challenges early and keeping global hiring decisions moving.")))

def nav():
    out = []
    for i, (t, _) in enumerate(S):
        col = TABCOL[i % 4]
        fg = "#3A2A00" if col == YEL else "#FFFFFF"
        out.append(f'<a href="#s{i+1}" style="background:{col};color:{fg} !important;">{i+1:02d} {t}</a>')
    return '<div class="nav">' + "".join(out) + "</div>"

def block(i):
    t, body = S[i]
    col = TABCOL[i % 4]
    fg = "#3A2A00" if col == YEL else "#FFFFFF"
    return (f'<div class="block" id="s{i+1}"><div class="bh" style="background:{col};color:{fg} !important;">'
            f'<small>SECTION {i+1:02d}</small>{t}</div><div class="bb">{body}</div></div>')

FOOTER = '<div class="footer">Prepared by Adam Baig · London, UK · A hypothetical case study built on public information. No real candidates or executives named.</div>'

def full_html():
    return BANNER + KPIS + nav() + "".join(block(i) for i in range(len(S))) + FOOTER
