import streamlit as st
import streamlit.components.v1 as components
import base64, os

# ─────────────────────────────────────────────
#  PAGE CONFIG  (must be the very first st call)
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Abhishek Rawat | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  KILL EVERY PIXEL OF STREAMLIT'S DEFAULT UI
#  This removes the top gap, toolbar, footer,
#  deploy button and all padding.
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* remove ALL default streamlit padding / margins */
html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"], [data-testid="block-container"],
.main, .block-container, section.main {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
    background: #080c14 !important;
}
/* hide header toolbar (causes the top gap) */
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu, footer, header {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
}
/* remove iframe border if any */
iframe { border: none !important; display: block; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  IMAGE HELPER
# ─────────────────────────────────────────────
def img_to_b64(path: str) -> str:
    """Convert a local image file to a base64 data-URI."""
    if os.path.exists(path):
        ext  = path.rsplit(".", 1)[-1].lower()
        mime = "image/jpeg" if ext in ("jpg", "jpeg") else "image/png"
        with open(path, "rb") as fh:
            return f"data:{mime};base64,{base64.b64encode(fh.read()).decode()}"
    return ""

profile_src = img_to_b64("assets/profile.png")
cert_src    = img_to_b64("assets/certificate.jpg")

# Build the img tags (fallback if images not present)
profile_tag = (
    f'<img src="{profile_src}" alt="Abhishek Rawat" '
    f'style="width:100%;height:100%;object-fit:cover;border-radius:50%;">'
    if profile_src else
    '<div style="width:100%;height:100%;display:flex;align-items:center;'
    'justify-content:center;font-size:72px;border-radius:50%;'
    'background:linear-gradient(135deg,rgba(0,212,255,.15),rgba(99,102,241,.15));">A</div>'
)

cert_tag = (
    f'<img src="{cert_src}" alt="IIT Roorkee Certificate" '
    f'style="width:100%;display:block;border-radius:12px;">'
    if cert_src else ""
)


# ─────────────────────────────────────────────
#  FULL HTML PAGE  (rendered via components.html
#  so Streamlit's markdown parser never touches it)
# ─────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
/* ── Reset ── */
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{
  background:#080c14;
  font-family:'Sora',sans-serif;
  color:#e8eaf0;
  overflow-x:hidden;
}}
::-webkit-scrollbar{{width:4px}}
::-webkit-scrollbar-track{{background:#080c14}}
::-webkit-scrollbar-thumb{{background:#00d4ff;border-radius:2px}}

/* ── NAV ── */
.nav{{
  position:sticky;top:0;z-index:999;
  background:rgba(8,12,20,.92);
  backdrop-filter:blur(20px);
  border-bottom:1px solid rgba(0,212,255,.1);
  display:flex;align-items:center;justify-content:space-between;
  padding:0 64px;height:62px;
}}
.nav-brand{{
  font-family:'JetBrains Mono',monospace;
  font-size:14px;font-weight:500;
  color:#00d4ff;letter-spacing:.09em;text-decoration:none;
}}
.nav-links{{display:flex;gap:36px}}
.nav-links a{{
  font-size:13px;color:#8892a4;
  text-decoration:none;letter-spacing:.04em;
  transition:color .2s;
}}
.nav-links a:hover{{color:#00d4ff}}

/* ── HERO ── */
.hero{{
  min-height:calc(100vh - 62px);
  display:flex;align-items:center;
  padding:60px 64px;gap:60px;
  position:relative;overflow:hidden;
}}
.hero::before{{
  content:'';position:absolute;
  top:-180px;right:-180px;
  width:650px;height:650px;
  background:radial-gradient(circle,rgba(0,212,255,.07) 0%,transparent 70%);
  pointer-events:none;
}}
.hero::after{{
  content:'';position:absolute;
  bottom:-100px;left:100px;
  width:500px;height:500px;
  background:radial-gradient(circle,rgba(99,102,241,.05) 0%,transparent 70%);
  pointer-events:none;
}}
.hero-left{{flex:1;max-width:620px;position:relative;z-index:1}}
.hero-right{{flex:0 0 280px;display:flex;justify-content:center;align-items:center;position:relative;z-index:1}}

.badge{{
  display:inline-flex;align-items:center;gap:8px;
  font-family:'JetBrains Mono',monospace;font-size:11px;
  color:#00d4ff;background:rgba(0,212,255,.06);
  border:1px solid rgba(0,212,255,.2);
  padding:5px 14px;border-radius:20px;
  margin-bottom:28px;letter-spacing:.06em;
}}
.dot{{font-size:7px;animation:blink 2s infinite}}
@keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}

h1.name{{
  font-size:clamp(38px,5vw,64px);
  font-weight:800;line-height:1.05;
  letter-spacing:-.025em;color:#f0f2f8;
  margin-bottom:6px;
}}
h1.name span{{color:#00d4ff}}
.title{{
  font-family:'JetBrains Mono',monospace;
  font-size:14px;font-weight:300;
  color:#6366f1;letter-spacing:.12em;
  margin-bottom:22px;
}}
.desc{{
  font-size:15px;line-height:1.8;
  color:#8892a4;margin-bottom:38px;
}}
.desc strong{{color:#e8eaf0}}
.cta{{display:flex;gap:14px;flex-wrap:wrap}}

.btn-p{{
  display:inline-flex;align-items:center;gap:7px;
  background:#00d4ff;color:#080c14;
  font-family:'Sora',sans-serif;font-size:13px;font-weight:700;
  padding:13px 26px;border-radius:8px;
  text-decoration:none;transition:all .2s;
}}
.btn-p:hover{{background:#26dcff;transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,212,255,.3)}}
.btn-o{{
  display:inline-flex;align-items:center;gap:7px;
  border:1px solid rgba(0,212,255,.3);color:#00d4ff;
  font-family:'Sora',sans-serif;font-size:13px;font-weight:500;
  padding:12px 26px;border-radius:8px;
  text-decoration:none;transition:all .2s;
}}
.btn-o:hover{{border-color:#00d4ff;background:rgba(0,212,255,.05);transform:translateY(-2px)}}

/* Profile ring */
.ring{{
  width:256px;height:256px;border-radius:50%;
  background:conic-gradient(#00d4ff 0%,#6366f1 50%,#00d4ff 100%);
  padding:3px;
  animation:spin 9s linear infinite;
  display:flex;align-items:center;justify-content:center;
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.ring-inner{{
  width:250px;height:250px;
  border-radius:50%;overflow:hidden;
  background:#080c14;
  display:flex;align-items:center;justify-content:center;
}}

/* ── STATS ── */
.stats{{
  display:flex;
  margin:0 64px;
  background:rgba(255,255,255,.02);
  border:1px solid rgba(255,255,255,.06);
  border-radius:14px;overflow:hidden;
}}
.stat{{
  flex:1;padding:26px 16px;text-align:center;
  border-right:1px solid rgba(255,255,255,.06);
}}
.stat:last-child{{border-right:none}}
.snum{{font-size:28px;font-weight:800;color:#00d4ff;line-height:1;margin-bottom:7px}}
.slbl{{font-size:11px;color:#6b7280;letter-spacing:.04em}}

/* ── DIVIDER ── */
.hr{{height:1px;background:rgba(255,255,255,.05);margin:56px 64px}}

/* ── SECTIONS ── */
.sec{{padding:56px 64px}}
.sec-tag{{
  font-family:'JetBrains Mono',monospace;
  font-size:11px;color:#6366f1;
  letter-spacing:.12em;text-transform:uppercase;
  margin-bottom:10px;
}}
.sec-title{{
  font-size:clamp(26px,3vw,38px);
  font-weight:800;color:#f0f2f8;
  letter-spacing:-.02em;line-height:1.1;
  margin-bottom:44px;
}}
.sec-title span{{color:#00d4ff}}

/* ── SKILLS ── */
.skills-grid{{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(255px,1fr));
  gap:18px;
}}
.sk{{
  background:rgba(255,255,255,.02);
  border:1px solid rgba(255,255,255,.06);
  border-radius:14px;padding:26px;
  transition:all .3s;position:relative;overflow:hidden;
}}
.sk::after{{
  content:'';position:absolute;
  top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,#00d4ff,#6366f1);
  transform:scaleX(0);transform-origin:left;
  transition:transform .3s;
}}
.sk:hover{{border-color:rgba(0,212,255,.2);transform:translateY(-4px)}}
.sk:hover::after{{transform:scaleX(1)}}
.sk-icon{{font-size:24px;margin-bottom:12px}}
.sk-cat{{
  font-size:11px;font-weight:700;color:#00d4ff;
  letter-spacing:.07em;text-transform:uppercase;margin-bottom:12px;
}}
.tags{{display:flex;flex-wrap:wrap;gap:7px}}
.tag{{
  font-family:'JetBrains Mono',monospace;
  font-size:10px;color:#8892a4;
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.08);
  padding:3px 9px;border-radius:4px;
}}

/* ── PROJECTS ── */
.proj-grid{{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(310px,1fr));
  gap:22px;
}}
.proj{{
  background:rgba(255,255,255,.02);
  border:1px solid rgba(255,255,255,.06);
  border-radius:18px;padding:30px;
  transition:all .3s;
}}
.proj:hover{{
  border-color:rgba(0,212,255,.22);
  transform:translateY(-5px);
  box-shadow:0 20px 50px rgba(0,0,0,.4),0 0 30px rgba(0,212,255,.05);
}}
.proj-num{{
  font-family:'JetBrains Mono',monospace;
  font-size:10px;color:rgba(0,212,255,.35);
  letter-spacing:.1em;margin-bottom:16px;
}}
.proj-title{{font-size:17px;font-weight:700;color:#f0f2f8;line-height:1.3;margin-bottom:10px}}
.proj-desc{{font-size:13px;color:#6b7280;line-height:1.75;margin-bottom:18px}}
.badges{{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:20px}}
.tb{{
  font-family:'JetBrains Mono',monospace;font-size:10px;
  color:#6366f1;background:rgba(99,102,241,.08);
  border:1px solid rgba(99,102,241,.2);
  padding:3px 11px;border-radius:20px;
}}
.links{{display:flex;gap:14px}}
.lnk{{
  font-size:12px;font-weight:600;color:#00d4ff;
  text-decoration:none;transition:opacity .2s;
}}
.lnk:hover{{opacity:.7}}

/* ── TIMELINE ── */
.tl{{position:relative;padding-left:34px}}
.tl::before{{
  content:'';position:absolute;
  left:0;top:10px;bottom:10px;
  width:1px;background:rgba(0,212,255,.14);
}}
.tl-item{{
  position:relative;margin-bottom:36px;
  padding:26px 28px;
  background:rgba(255,255,255,.02);
  border:1px solid rgba(255,255,255,.06);
  border-radius:14px;transition:border-color .3s;
}}
.tl-item:hover{{border-color:rgba(0,212,255,.14)}}
.tl-item::before{{
  content:'';position:absolute;
  left:-41px;top:30px;
  width:13px;height:13px;border-radius:50%;
  background:#00d4ff;
  box-shadow:0 0 0 3px rgba(0,212,255,.12);
}}
.tl-period{{
  font-family:'JetBrains Mono',monospace;
  font-size:10px;color:#6366f1;
  letter-spacing:.08em;margin-bottom:7px;
}}
.tl-role{{font-size:17px;font-weight:700;color:#f0f2f8;margin-bottom:3px}}
.tl-co{{font-size:13px;color:#00d4ff;margin-bottom:12px}}
.tl-pts{{list-style:none}}
.tl-pts li{{
  font-size:13px;color:#6b7280;
  line-height:1.75;padding:3px 0 3px 16px;
  position:relative;
}}
.tl-pts li::before{{
  content:'&#9658;';color:#00d4ff;
  position:absolute;left:0;
  font-size:9px;top:7px;
}}

/* ── CERT ── */
.cert-card{{
  background:rgba(255,255,255,.02);
  border:1px solid rgba(255,255,255,.06);
  border-radius:18px;padding:32px;
  display:flex;gap:28px;align-items:flex-start;
  transition:border-color .3s;margin-bottom:28px;
}}
.cert-card:hover{{border-color:rgba(0,212,255,.18)}}
.cert-ico{{
  flex:0 0 66px;height:66px;
  background:linear-gradient(135deg,rgba(0,212,255,.14),rgba(99,102,241,.14));
  border:1px solid rgba(0,212,255,.18);border-radius:14px;
  display:flex;align-items:center;justify-content:center;font-size:28px;
}}
.cert-body{{flex:1}}
.cert-title{{font-size:16px;font-weight:700;color:#f0f2f8;margin-bottom:5px}}
.cert-issuer{{font-size:13px;color:#00d4ff;margin-bottom:7px}}
.cert-meta{{font-family:'JetBrains Mono',monospace;font-size:10px;color:#4b5563}}
.cert-img{{
  border-radius:12px;overflow:hidden;
  border:1px solid rgba(255,255,255,.07);
  max-width:480px;
}}

/* ── CONTACT ── */
.contact-lead{{
  font-size:15px;color:#6b7280;line-height:1.8;
  margin-bottom:32px;max-width:460px;
}}
.c-links{{display:flex;flex-direction:column;gap:14px;max-width:480px}}
.c-link{{
  display:flex;align-items:center;gap:14px;
  font-size:14px;color:#8892a4;
  text-decoration:none;transition:color .2s;
}}
.c-link:hover{{color:#00d4ff}}
.c-ico{{
  width:38px;height:38px;flex-shrink:0;
  background:rgba(255,255,255,.03);
  border:1px solid rgba(255,255,255,.07);
  border-radius:9px;
  display:flex;align-items:center;justify-content:center;font-size:15px;
}}

/* ── FOOTER ── */
.footer{{
  padding:24px 64px;
  border-top:1px solid rgba(255,255,255,.05);
  display:flex;justify-content:space-between;align-items:center;
  margin-top:16px;
}}
.footer span{{
  font-family:'JetBrains Mono',monospace;
  font-size:11px;color:#374151;
}}
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
  <a class="nav-brand" href="#about">abhishek.rawat</a>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#contact">Contact</a>
  </div>
</nav>

<!-- HERO -->
<section id="about" class="hero">
  <div class="hero-left">
    <div class="badge"><span class="dot">&#9679;</span>&nbsp;Available for opportunities</div>
    <h1 class="name">Abhishek<br><span>Rawat</span></h1>
    <p class="title">DATA ANALYST &nbsp;&middot;&nbsp; BUSINESS ANALYST</p>
    <p class="desc">
      I build <strong>production-grade analytics tools</strong> &mdash; not just notebooks.
      From fraud detection on 50K+ transactions to live AI-powered dashboards,
      I turn raw data into decisions that actually ship.
    </p>
    <div class="cta">
      <a href="https://github.com/rawatabhishek2909-blip" target="_blank" class="btn-p">&#128279; GitHub</a>
      <a href="https://www.linkedin.com/in/rawatabhishek106" target="_blank" class="btn-o">in&nbsp;LinkedIn</a>
      <a href="mailto:rawatabhishek106@gmail.com" class="btn-o">&#9993;&nbsp;Email Me</a>
    </div>
  </div>
  <div class="hero-right">
    <div class="ring">
      <div class="ring-inner">{profile_tag}</div>
    </div>
  </div>
</section>

<!-- STATS -->
<div class="stats">
  <div class="stat"><div class="snum">50K+</div><div class="slbl">Records Analysed</div></div>
  <div class="stat"><div class="snum">3</div><div class="slbl">Live Projects</div></div>
  <div class="stat"><div class="snum">80%</div><div class="slbl">Analysis Time Saved</div></div>
  <div class="stat"><div class="snum">IIT</div><div class="slbl">Roorkee Certified</div></div>
  <div class="stat"><div class="snum">4 yrs</div><div class="slbl">Client Experience</div></div>
</div>

<div class="hr"></div>

<!-- SKILLS -->
<section id="skills" class="sec">
  <div class="sec-tag">// 01 &mdash; SKILLS</div>
  <h2 class="sec-title">What I Work<br><span>With</span></h2>
  <div class="skills-grid">

    <div class="sk">
      <div class="sk-icon">&#128013;</div>
      <div class="sk-cat">Languages</div>
      <div class="tags">
        <span class="tag">Python</span><span class="tag">Pandas</span>
        <span class="tag">NumPy</span><span class="tag">SQL</span><span class="tag">MySQL</span>
      </div>
    </div>

    <div class="sk">
      <div class="sk-icon">&#128202;</div>
      <div class="sk-cat">Data Analysis</div>
      <div class="tags">
        <span class="tag">EDA</span><span class="tag">Data Cleaning</span>
        <span class="tag">Statistical Analysis</span><span class="tag">Fraud Detection</span>
        <span class="tag">Root Cause Analysis</span>
      </div>
    </div>

    <div class="sk">
      <div class="sk-icon">&#128200;</div>
      <div class="sk-cat">Visualisation &amp; BI</div>
      <div class="tags">
        <span class="tag">Power BI</span><span class="tag">Matplotlib</span>
        <span class="tag">Seaborn</span><span class="tag">Streamlit</span>
        <span class="tag">Dashboard Design</span>
      </div>
    </div>

    <div class="sk">
      <div class="sk-icon">&#127970;</div>
      <div class="sk-cat">Business Analysis</div>
      <div class="tags">
        <span class="tag">Requirements Gathering</span><span class="tag">Gap Analysis</span>
        <span class="tag">Stakeholder Reporting</span><span class="tag">BI</span>
      </div>
    </div>

    <div class="sk">
      <div class="sk-icon">&#9881;&#65039;</div>
      <div class="sk-cat">Tools &amp; Platforms</div>
      <div class="tags">
        <span class="tag">Excel</span><span class="tag">Jupyter</span>
        <span class="tag">GitHub</span><span class="tag">Streamlit Cloud</span>
        <span class="tag">ETL Pipelines</span>
      </div>
    </div>

    <div class="sk">
      <div class="sk-icon">&#129504;</div>
      <div class="sk-cat">Concepts</div>
      <div class="tags">
        <span class="tag">Data Modeling</span><span class="tag">Forecasting</span>
        <span class="tag">Data Governance</span><span class="tag">Data Quality</span>
        <span class="tag">ETL</span>
      </div>
    </div>

  </div>
</section>

<div class="hr"></div>

<!-- PROJECTS -->
<section id="projects" class="sec">
  <div class="sec-tag">// 02 &mdash; PROJECTS</div>
  <h2 class="sec-title">Things I&rsquo;ve<br><span>Built</span></h2>
  <div class="proj-grid">

    <div class="proj">
      <div class="proj-num">PROJECT 01 &middot; LIVE ON STREAMLIT CLOUD</div>
      <div class="proj-title">AI-Powered Data Analyst Assistant</div>
      <div class="proj-desc">
        Production-deployed web app automating EDA, insight generation &amp; visualisation for datasets up to 500 MB.
        Reduced analysis setup time by ~80%. AI layer makes analytics accessible to non-technical users with zero code.
      </div>
      <div class="badges">
        <span class="tb">Python</span><span class="tb">Pandas</span>
        <span class="tb">Streamlit</span><span class="tb">Power BI</span><span class="tb">ETL</span>
      </div>
      <div class="links">
        <a href="https://ai-data-analyst-intern.streamlit.app" target="_blank" class="lnk">&#128279; Live Demo</a>
        <a href="https://github.com/rawatabhishek2909-blip/AI-Data-Analyst-Intern" target="_blank" class="lnk">&#128279; GitHub</a>
      </div>
    </div>

    <div class="proj">
      <div class="proj-num">PROJECT 02 &middot; FRAUD DETECTION</div>
      <div class="proj-title">Online Payment Fraud Detection Analysis</div>
      <div class="proj-desc">
        EDA on 50,000+ financial transaction records. Identified TRANSFER &amp; CASH_OUT as dominant fraud vectors.
        Delivered an operationalisable risk monitoring framework with publication-ready dashboards.
      </div>
      <div class="badges">
        <span class="tb">Python</span><span class="tb">Pandas</span>
        <span class="tb">Matplotlib</span><span class="tb">Seaborn</span><span class="tb">Stats</span>
      </div>
      <div class="links">
        <a href="https://github.com/rawatabhishek2909-blip/Online-Payment-Fraud-detectionAnalysis" target="_blank" class="lnk">&#128279; GitHub</a>
      </div>
    </div>

    <div class="proj">
      <div class="proj-num">PROJECT 03 &middot; BUSINESS INTELLIGENCE</div>
      <div class="proj-title">Retail Sales Profit Analysis</div>
      <div class="proj-desc">
        Queried 4,200+ retail transactions using advanced SQL (window functions, joins, aggregations).
        Surfaced profit margin drivers &amp; regional gaps. Produced a board-ready BI brief with investment recommendations.
      </div>
      <div class="badges">
        <span class="tb">SQL</span><span class="tb">Window Functions</span>
        <span class="tb">BI</span><span class="tb">Data Analysis</span>
      </div>
      <div class="links">
        <a href="https://github.com/rawatabhishek2909-blip/Retail-Sales-Profit-Analysis-using-SQL" target="_blank" class="lnk">&#128279; GitHub</a>
      </div>
    </div>

  </div>
</section>

<div class="hr"></div>

<!-- EXPERIENCE -->
<section id="experience" class="sec">
  <div class="sec-tag">// 03 &mdash; EXPERIENCE</div>
  <h2 class="sec-title">My<br><span>Journey</span></h2>
  <div class="tl">

    <div class="tl-item">
      <div class="tl-period">2025 &ndash; 2026</div>
      <div class="tl-role">Executive PG Certificate &mdash; Data Science &amp; AI</div>
      <div class="tl-co">IIT Roorkee &times; iHUB DivyaSampark &times; Intellipaat</div>
      <ul class="tl-pts">
        <li>Completed advanced curriculum in Data Science, Machine Learning &amp; Artificial Intelligence</li>
        <li>Built and deployed production-grade analytics projects applying course learnings</li>
        <li>Certified by Dept. of Science &amp; Technology, Govt. of India in association with IIT Roorkee</li>
      </ul>
    </div>

    <div class="tl-item">
      <div class="tl-period">2017 &ndash; 2024</div>
      <div class="tl-role">Freelance Content Writer &amp; Poet</div>
      <div class="tl-co">Self-Employed &middot; Remote</div>
      <ul class="tl-pts">
        <li>Analysed audience engagement metrics and iterated content strategy based on measurable data</li>
        <li>Named Top 10 Poet of India by S7 Poetry Organization</li>
        <li>Built structured communication skills now applied to analyst stakeholder reporting</li>
      </ul>
    </div>

    <div class="tl-item">
      <div class="tl-period">2014 &ndash; 2017</div>
      <div class="tl-role">Tax Advisor</div>
      <div class="tl-co">Reliance Nippon Life Insurance &middot; Prayagraj</div>
      <ul class="tl-pts">
        <li>Managed client portfolios, translating complex financial data into clear risk-ranked recommendations</li>
        <li>Identified new client segments through market analysis and opportunity mapping</li>
        <li>Developed stakeholder communication skills directly transferable to BA roles</li>
      </ul>
    </div>

  </div>
</section>

<div class="hr"></div>

<!-- CERTIFICATION -->
<section class="sec">
  <div class="sec-tag">// 04 &mdash; CERTIFICATION</div>
  <h2 class="sec-title">IIT Roorkee<br><span>Certified</span></h2>
  <div class="cert-card">
    <div class="cert-ico">&#127891;</div>
    <div class="cert-body">
      <div class="cert-title">Executive PG Certification in Data Science &amp; Artificial Intelligence</div>
      <div class="cert-issuer">iHUB DivyaSampark &middot; IIT Roorkee &times; Intellipaat</div>
      <div class="cert-meta">
        Issued: 31-Mar-2026 &nbsp;&middot;&nbsp; ID: IPTIH26030014 &nbsp;&middot;&nbsp; Verify: tih.iitr.ac.in
      </div>
    </div>
  </div>
  <div class="cert-img">{cert_tag}</div>
</section>

<div class="hr"></div>

<!-- CONTACT -->
<section id="contact" class="sec">
  <div class="sec-tag">// 05 &mdash; CONTACT</div>
  <h2 class="sec-title">Let&rsquo;s<br><span>Connect</span></h2>
  <p class="contact-lead">
    Actively looking for Data Analyst and Business Analyst roles.
    If you have an opportunity, a project, or just want to talk data &mdash; my inbox is always open.
  </p>
  <div class="c-links">
    <a href="mailto:rawatabhishek106@gmail.com" class="c-link">
      <span class="c-ico">&#9993;</span>rawatabhishek106@gmail.com
    </a>
    <a href="tel:+919580293410" class="c-link">
      <span class="c-ico">&#128222;</span>+91 95802 93410
    </a>
    <a href="https://www.linkedin.com/in/rawatabhishek106" target="_blank" class="c-link">
      <span class="c-ico">in</span>linkedin.com/in/rawatabhishek106
    </a>
    <a href="https://github.com/rawatabhishek2909-blip" target="_blank" class="c-link">
      <span class="c-ico">&#128279;</span>github.com/rawatabhishek2909-blip
    </a>
    <span class="c-link" style="cursor:default;">
      <span class="c-ico">&#128205;</span>Prayagraj, Uttar Pradesh, India
    </span>
  </div>
</section>

<!-- FOOTER -->
<div class="footer">
  <span>&#169; 2026 Abhishek Rawat</span>
  <span>Built with Python + Streamlit &#128013;</span>
</div>

</body>
</html>"""

# Render the entire page as a self-contained HTML component.
# height is set large enough so no internal scrollbar appears.
components.html(HTML, height=5800, scrolling=False)
