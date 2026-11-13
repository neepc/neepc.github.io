# Regenerates past.html and one page per past year (2025.html, 2026.html, ...)
# from _build/programs.py, reusing the header and footer from index.html.
# Usage (from the repo root): python3 _build/build_past.py
import os
import re
import sys
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from programs import PROGRAMS  # noqa: E402


def template():
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    head = src.split("<main>")[0].replace(' aria-current="page"', "")
    head = head.replace('<a href="past.html">Past Conferences</a>',
                        '<a href="past.html" aria-current="page">Past Conferences</a>')
    foot = src.split("</main>")[1]
    return head, foot


def page(head, foot, title, description, main):
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head)
    h = re.sub(r'<meta name="description" content=".*?">',
               f'<meta name="description" content="{escape(description)}">', h)
    return h + main + foot


def school(aff):
    return aff.replace(" (visiting)", "")


def stats(p):
    talks = [t for s in p["sessions"] for r in s["rooms"] for t in r["talks"]]
    pres = sum(len(r["talks"]) for s in p["sessions"] if s["kind"] == "Presentation" for r in s["rooms"])
    pitches = sum(len(r["talks"]) for s in p["sessions"] if s["kind"] == "Pitch" for r in s["rooms"])
    schools = sorted({school(t[1]) for t in talks})
    return pres, pitches, schools


def room_html(r):
    has_titles = any(t[2] for t in r["talks"])
    topic = f'<span class="room-topic">{escape(r["topic"])}</span>' if r.get("topic") else ""
    rows = []
    for name, aff, title in r["talks"]:
        cells = f'<td class="who">{escape(name)}</td><td class="aff">{escape(aff)}</td>'
        if has_titles:
            cells += f'<td class="paper">{escape(title)}</td>'
        rows.append(f"<tr>{cells}</tr>")
    head = "<th>Presenter</th><th>Affiliation</th>" + ("<th>Paper</th>" if has_titles else "")
    return f'''
        <div class="room">
          <div class="room-head"><h4>{escape(r["room"])}</h4>{topic}<span class="room-host">Host: {escape(r["host"])}</span></div>
          <table class="talks{'' if has_titles else ' no-titles'}">
            <thead><tr>{head}</tr></thead>
            <tbody>
              {"".join(rows)}
            </tbody>
          </table>
        </div>'''


def year_page(year, p):
    pres, pitches, schools = stats(p)
    glance = []
    for time, label, sid in p["timeline"]:
        lab = f'<a href="#{sid}">{escape(label)}</a>' if sid else escape(label)
        cls = ' class="is-session"' if sid else ""
        glance.append(f'<li{cls}><span class="t">{time}</span><span class="l">{lab}</span></li>')
    sessions = []
    for s in p["sessions"]:
        sessions.append(f'''
      <section class="session" id="{s["id"]}">
        <div class="session-head">
          <h3>{escape(s["name"])}</h3>
          <span class="session-time">{s["time"]}</span>
        </div>
        {"".join(room_html(r) for r in s["rooms"])}
      </section>''')
    photo = ""
    if p.get("photo"):
        photo = f'<figure class="year-photo"><img src="{p["photo"]}" alt="A presentation at NEEPC {year}"></figure>'
    formats = "".join(f"<li>{escape(f)}</li>" for f in p["formats"])
    main = f'''<main>
  <section class="page-head">
    <div class="wrap year-head{' has-photo' if photo else ''}">
      <div>
        <p class="eyebrow"><a href="past.html">Past Conferences</a></p>
        <h1>NEEPC {year}</h1>
        <hr class="rule">
        <p class="year-meta">{p["date"]} · {p["venue"]}</p>
        <ul class="year-stats">
          <li><strong>{pres}</strong> presentations</li>
          <li><strong>{pitches}</strong> pitches</li>
          <li><strong>{len(schools)}</strong> universities</li>
        </ul>
      </div>
      {photo}
    </div>
  </section>

  <section class="block">
    <div class="wrap two-col">
      <div>
        <p class="eyebrow">Program</p>
        <h2>Schedule at a glance</h2>
        <ul class="formats">{formats}</ul>
      </div>
      <ol class="glance">
        {"".join(glance)}
      </ol>
    </div>
  </section>

  <section class="block alt">
    <div class="wrap">
      <p class="eyebrow">Sessions</p>
      <h2>Presenters and papers</h2>
      {"".join(sessions)}
    </div>
  </section>
</main>'''
    return main, pres, pitches, schools


def main():
    head, foot = template()
    cards = []
    for year in sorted(PROGRAMS, reverse=True):
        p = PROGRAMS[year]
        body, pres, pitches, schools = year_page(year, p)
        html = page(head, foot, f"NEEPC {year} | Past Conferences",
                    f"Program of NEEPC {year}, held {p['date']} at {p['venue']}.", body)
        open(os.path.join(ROOT, f"{year}.html"), "w", encoding="utf-8").write(html)
        cards.append(f'''
        <a class="card year-card" href="{year}.html">
          <p class="eyebrow">{p["date"]}</p>
          <h3>NEEPC {year}</h3>
          <p class="meta">{p["venue"]}</p>
          <p>{pres} presentations · {pitches} pitches · {len(schools)} universities</p>
          <p class="more">View program →</p>
        </a>''')
    past = f'''<main>
  <section class="page-head"><div class="wrap"><p class="eyebrow">NEEPC</p><h1>Past Conferences</h1><hr class="rule" style="margin-bottom:0"></div></section>
  <section class="block">
    <div class="wrap">
      <p class="lead">Programs from previous years, with every presenter, their university and their paper.</p>
      <div class="cards">{"".join(cards)}
      </div>
    </div>
  </section>
</main>'''
    open(os.path.join(ROOT, "past.html"), "w", encoding="utf-8").write(
        page(head, foot, "Past Conferences | NEEPC", "Programs from past NEEPC conferences.", past))
    print("built past.html and", ", ".join(f"{y}.html" for y in sorted(PROGRAMS)))


if __name__ == "__main__":
    main()
