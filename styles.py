"""Premium visual system and static UI content."""

HEADER_HTML = """
<div class="ambient ambient-one"></div>
<div class="ambient ambient-two"></div>

<nav class="topbar">
  <div class="brand-lockup">
    <div class="brand-mark"><span></span><span></span><span></span></div>
    <div><strong>KAUSHIK / RESEARCH</strong><small>INTELLIGENCE WORKSPACE</small></div>
  </div>
  <div class="topbar-actions">
    <span class="system-chip"><i></i> SYSTEM ONLINE</span>
    <span class="version-chip">V2.4</span>
  </div>
</nav>

<section class="hero">
  <div class="hero-copy">
    <div class="eyebrow"><span>✦</span> AGENTIC RESEARCH, GROUNDED IN EVIDENCE</div>
    <h1>Research that<br><em>shows its work.</em></h1>
    <p>One question becomes a planned, live-web investigation and a polished,
    source-backed report—without a paid AI subscription.</p>
    <div class="hero-tags">
      <span>Gemini 3.5 Flash-Lite</span>
      <span>Keyless live metasearch</span>
      <span>₹0 configuration</span>
    </div>
  </div>
  <div class="pipeline-visual">
    <div class="radar-ring ring-one"></div>
    <div class="radar-ring ring-two"></div>
    <div class="core-node"><b>AI</b><small>ORCHESTRATOR</small></div>
    <div class="satellite node-plan"><i>01</i><span>PLAN</span></div>
    <div class="satellite node-search"><i>02</i><span>SEARCH</span></div>
    <div class="satellite node-write"><i>03</i><span>WRITE</span></div>
  </div>
</section>

<section class="capability-strip">
  <article><strong>3</strong><span>Research modes</span></article>
  <article><strong>LIVE</strong><span>Source-backed web evidence</span></article>
  <article><strong>LOCAL</strong><span>Private cache & exports</span></article>
  <article><strong>0₹</strong><span>Paid services required</span></article>
</section>
"""

EXAMPLES = [
    ["How is generative AI changing entry-level software jobs in India?"],
    ["Compare PostgreSQL and MySQL for a student placement portal."],
    ["What skills should a data-science undergraduate build for 2027 hiring?"],
]

CSS = """
:root {
  --bg: #050711;
  --surface: rgba(13, 17, 32, 0.82);
  --surface-solid: #0d1120;
  --surface-2: #12182b;
  --line: rgba(143, 163, 203, 0.16);
  --line-bright: rgba(134, 114, 255, 0.38);
  --text: #edf1ff;
  --muted: #8f9bb8;
  --violet: #8875ff;
  --violet-2: #5b45e8;
  --cyan: #46e6d7;
  --blue: #6aa8ff;
  --glow: 0 0 70px rgba(102, 77, 255, 0.18);
}

* { box-sizing: border-box; }

html { background: var(--bg); }

body, .gradio-container {
  color: var(--text) !important;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}

body {
  background:
    linear-gradient(rgba(255,255,255,.018) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.018) 1px, transparent 1px),
    radial-gradient(circle at 50% -10%, #18134b 0, transparent 42%),
    var(--bg) !important;
  background-size: 54px 54px, 54px 54px, auto, auto !important;
}

.gradio-container {
  max-width: 1440px !important;
  margin: 0 auto !important;
  padding: 0 38px 34px !important;
  background: transparent !important;
}

.ambient {
  position: fixed;
  width: 360px;
  height: 360px;
  border-radius: 50%;
  filter: blur(110px);
  pointer-events: none;
  opacity: .17;
  z-index: 0;
}
.ambient-one { background: #704cff; top: 18%; left: -190px; }
.ambient-two { background: #13d8cc; right: -230px; top: 56%; }

.topbar {
  min-height: 78px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--line);
  position: relative;
  z-index: 2;
}

.brand-lockup { display: flex; gap: 12px; align-items: center; }
.brand-lockup strong { display: block; font-size: 12px; letter-spacing: .16em; }
.brand-lockup small { display: block; color: var(--muted); font-size: 8px; letter-spacing: .21em; margin-top: 3px; }
.brand-mark {
  width: 34px; height: 34px; border: 1px solid var(--line-bright); border-radius: 9px;
  display: grid; grid-template-columns: repeat(3, 4px); gap: 3px; place-content: center;
  background: linear-gradient(145deg, rgba(134,114,255,.22), rgba(70,230,215,.06));
  box-shadow: 0 0 25px rgba(113, 87, 255, .18);
}
.brand-mark span { height: 15px; border-radius: 5px; background: var(--violet); }
.brand-mark span:nth-child(2) { height: 22px; margin-top: -4px; background: var(--cyan); }
.brand-mark span:nth-child(3) { height: 10px; margin-top: 5px; }
.topbar-actions { display: flex; gap: 9px; align-items: center; }
.system-chip, .version-chip {
  border: 1px solid var(--line); border-radius: 999px; padding: 7px 11px;
  color: var(--muted); font-size: 9px; font-weight: 800; letter-spacing: .12em;
  background: rgba(10,14,27,.72);
}
.system-chip i {
  width: 6px; height: 6px; display: inline-block; border-radius: 50%;
  background: var(--cyan); box-shadow: 0 0 12px var(--cyan); margin-right: 6px;
}
.version-chip { color: var(--violet); }

.hero {
  min-height: 440px;
  display: grid;
  grid-template-columns: 1.15fr .85fr;
  align-items: center;
  gap: 48px;
  position: relative;
  z-index: 1;
  padding: 54px 32px 42px;
}
.hero-copy { max-width: 730px; }
.eyebrow {
  color: var(--cyan); font-size: 10px; font-weight: 900; letter-spacing: .19em;
  margin-bottom: 20px;
}
.eyebrow span { color: var(--violet); margin-right: 7px; }
.hero h1 {
  margin: 0; color: var(--text); font-size: clamp(52px, 6.5vw, 92px);
  line-height: .93; letter-spacing: -.068em; font-weight: 760;
}
.hero h1 em {
  font-style: normal;
  background: linear-gradient(110deg, #a99cff 5%, #6f8fff 48%, #4ce6d8 95%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hero p {
  color: #a9b3cc; max-width: 650px; font-size: 17px; line-height: 1.7;
  margin: 24px 0 21px;
}
.hero-tags { display: flex; flex-wrap: wrap; gap: 8px; }
.hero-tags span {
  color: #aeb9d5; font-size: 10px; font-weight: 700; letter-spacing: .05em;
  padding: 7px 10px; border: 1px solid var(--line); border-radius: 7px;
  background: rgba(14,18,34,.66);
}

.pipeline-visual {
  width: 330px; height: 330px; justify-self: center; position: relative;
  display: grid; place-items: center;
}
.radar-ring { position: absolute; border: 1px solid rgba(134,114,255,.22); border-radius: 50%; }
.ring-one { width: 210px; height: 210px; animation: spin 17s linear infinite; }
.ring-two { width: 315px; height: 315px; border-style: dashed; animation: spin 28s linear infinite reverse; }
.ring-one::before, .ring-two::after {
  content: ""; position: absolute; width: 7px; height: 7px; border-radius: 50%;
  background: var(--cyan); box-shadow: 0 0 16px var(--cyan);
}
.ring-one::before { left: 20px; top: 35px; }
.ring-two::after { right: 43px; bottom: 28px; background: var(--violet); box-shadow: 0 0 16px var(--violet); }
.core-node {
  width: 116px; height: 116px; border-radius: 31px; display: grid; place-content: center;
  text-align: center; background: linear-gradient(145deg, #1a2140, #0b0f1f);
  border: 1px solid var(--line-bright); box-shadow: 0 0 70px rgba(112,83,255,.27), inset 0 0 25px rgba(134,114,255,.08);
}
.core-node b { font-size: 34px; letter-spacing: -.06em; background: linear-gradient(120deg,#fff,#8c7aff); -webkit-background-clip:text; color:transparent; }
.core-node small { color: var(--muted); font-size: 7px; letter-spacing: .17em; margin-top: 4px; }
.satellite {
  position: absolute; min-width: 82px; padding: 9px 11px; display: flex; align-items: center; gap: 8px;
  background: rgba(12,16,31,.9); border: 1px solid var(--line); border-radius: 10px;
  box-shadow: 0 12px 30px rgba(0,0,0,.28); backdrop-filter: blur(12px);
}
.satellite i { font-style: normal; color: var(--cyan); font-size: 8px; }
.satellite span { font-size: 9px; font-weight: 800; letter-spacing: .12em; }
.node-plan { top: 31px; left: 8px; }
.node-search { right: -8px; top: 119px; }
.node-write { left: 21px; bottom: 28px; }
@keyframes spin { to { transform: rotate(360deg); } }

.capability-strip {
  display: grid; grid-template-columns: repeat(4, 1fr); border: 1px solid var(--line);
  background: rgba(9,13,25,.68); border-radius: 16px; margin-bottom: 26px;
  backdrop-filter: blur(16px); overflow: hidden;
}
.capability-strip article {
  padding: 17px 20px; display: flex; align-items: center; gap: 12px;
  border-right: 1px solid var(--line);
}
.capability-strip article:last-child { border-right: 0; }
.capability-strip strong { color: var(--text); font-size: 15px; }
.capability-strip span { color: var(--muted); font-size: 10px; letter-spacing: .05em; }

#research-workspace {
  position: relative; z-index: 2; gap: 18px; align-items: flex-start;
}
#control-panel, #report-panel {
  background: var(--surface) !important; border: 1px solid var(--line) !important;
  border-radius: 20px !important; backdrop-filter: blur(22px);
  box-shadow: 0 28px 80px rgba(0,0,0,.25), var(--glow);
}
#control-panel { padding: 25px !important; position: sticky; top: 16px; }
#report-panel { min-height: 720px; overflow: hidden; }
.panel-kicker { color: var(--cyan); font-size: 9px; font-weight: 900; letter-spacing: .18em; }
.panel-heading { margin: 8px 0 7px; font-size: 24px; letter-spacing: -.035em; }
.panel-copy { margin: 0 0 20px; color: var(--muted); font-size: 12px; line-height: 1.6; }

.gradio-container label, .gradio-container .label-wrap {
  color: #aeb8d1 !important; font-size: 10px !important; font-weight: 800 !important;
  letter-spacing: .06em !important;
}
.gradio-container input, .gradio-container textarea {
  color: var(--text) !important; background: #090d19 !important;
}
#research-query {
  border: 1px solid var(--line) !important; border-radius: 14px !important;
  background: #090d19 !important; overflow: hidden;
}
#research-query:focus-within { border-color: var(--violet) !important; box-shadow: 0 0 0 3px rgba(134,114,255,.1); }
#research-query textarea { min-height: 120px !important; font-size: 15px !important; line-height: 1.6 !important; }

#depth-selector { background: transparent !important; border: 0 !important; }
#depth-selector label {
  background: #0a0e1b !important; border: 1px solid var(--line) !important;
  border-radius: 9px !important; padding: 8px 10px !important;
}
#depth-selector label:has(input:checked) {
  border-color: var(--line-bright) !important;
  background: linear-gradient(145deg, rgba(134,114,255,.18), rgba(70,230,215,.05)) !important;
  color: #fff !important;
}

#mode-hint {
  color: #9da9c5 !important; background: rgba(105,82,255,.09) !important;
  border: 1px solid rgba(134,114,255,.17) !important; border-radius: 10px !important;
  padding: 9px 11px !important; font-size: 10px !important; line-height: 1.45 !important;
}

.gradio-container .wrap, .gradio-container .secondary-wrap {
  background: #090d19 !important; border-color: var(--line) !important;
}
#action-row { margin-top: 8px; }
#research-run {
  min-height: 48px !important; color: #fff !important; font-weight: 850 !important;
  background: linear-gradient(105deg, #674cff, #7d69ff 55%, #437ff5) !important;
  border: 0 !important; border-radius: 11px !important;
  box-shadow: 0 13px 28px rgba(96,72,255,.28) !important;
  transition: transform .2s ease, box-shadow .2s ease !important;
}
#research-run:hover { transform: translateY(-2px); box-shadow: 0 17px 36px rgba(96,72,255,.4) !important; }
#research-clear { border: 1px solid var(--line) !important; background: #0b0f1d !important; color: var(--muted) !important; border-radius: 11px !important; }
#examples-panel { border: 1px solid var(--line) !important; background: rgba(8,12,23,.5) !important; border-radius: 11px !important; }

.privacy-card {
  margin-top: 16px; display: flex; gap: 10px; align-items: flex-start; color: var(--muted);
  padding: 12px; border: 1px solid rgba(70,230,215,.12); border-radius: 11px;
  background: rgba(70,230,215,.035);
}
.privacy-icon { color: var(--cyan); font-size: 22px; line-height: 1; }
.privacy-card strong { color: #c8d1e8; font-size: 10px; letter-spacing: .07em; }
.privacy-card p { font-size: 9px; margin: 3px 0 0; }
.privacy-card code { color: var(--cyan); background: transparent; }

#report-toolbar {
  min-height: 61px; align-items: center; padding: 0 22px;
  border-bottom: 1px solid var(--line); background: rgba(7,10,20,.55);
}
.report-label { color: #cbd3e6; font-size: 9px; font-weight: 900; letter-spacing: .15em; white-space: nowrap; }
.live-dot {
  display: inline-block; width: 7px; height: 7px; border-radius: 50%;
  background: var(--cyan); box-shadow: 0 0 13px var(--cyan); margin-right: 7px;
  animation: pulse 1.8s ease-in-out infinite;
}
@keyframes pulse { 50% { opacity: .4; transform: scale(.75); } }
#research-status { color: var(--muted) !important; text-align: right; font-size: 10px !important; }
#research-status p { margin: 0 !important; }

#research-report {
  margin: 0 !important; padding: clamp(26px, 4vw, 52px) !important;
  min-height: 570px; background: transparent !important; border: 0 !important;
  color: #d9e0f2 !important;
}
#research-report h1 {
  font-size: clamp(34px, 4vw, 54px); line-height: 1.05; letter-spacing: -.05em;
  border-bottom: 1px solid var(--line); padding-bottom: 22px; margin-bottom: 28px;
}
#research-report h2 { color: #f0f3ff; font-size: 24px; letter-spacing: -.025em; margin-top: 35px; }
#research-report h3 { color: #cbd4eb; font-size: 17px; }
#research-report p, #research-report li { color: #b5bfd6; font-size: 14px; line-height: 1.82; }
#research-report a { color: #75dfd6; text-decoration-color: rgba(117,223,214,.34); }
#research-report blockquote {
  border-left: 3px solid var(--violet); color: #cbd4e8; background: rgba(134,114,255,.06);
  padding: 12px 16px; border-radius: 0 10px 10px 0;
}
#research-report code { color: #96efe7; background: #090d19; border: 1px solid var(--line); }

.empty-state { min-height: 450px; display: grid; place-content: center; text-align: center; }
.empty-orbit {
  width: 92px; height: 92px; border-radius: 50%; margin: 0 auto 20px; display: grid; place-items: center;
  border: 1px solid rgba(134,114,255,.28); box-shadow: inset 0 0 28px rgba(134,114,255,.09), 0 0 50px rgba(134,114,255,.12);
  position: relative;
}
.empty-orbit::after { content:""; position:absolute; inset:-13px; border:1px dashed rgba(70,230,215,.2); border-radius:50%; animation:spin 16s linear infinite; }
.empty-orbit span { color: var(--violet); font-size: 28px; text-shadow: 0 0 18px var(--violet); }
.empty-state h2 { margin: 0 !important; font-size: 25px !important; border: 0 !important; padding: 0 !important; }
.empty-state p { color: var(--muted) !important; margin: 8px auto 20px; max-width: 380px; }
.empty-steps { display: flex; justify-content: center; gap: 7px; flex-wrap: wrap; }
.empty-steps span { color: #77829e; font-size: 8px; letter-spacing: .13em; border: 1px solid var(--line); padding: 6px 8px; border-radius: 6px; }

#report-download {
  margin: 0 24px 24px !important; width: calc(100% - 48px) !important;
  background: rgba(70,230,215,.04) !important; border: 1px solid rgba(70,230,215,.14) !important;
  border-radius: 11px !important;
}

.app-footer {
  display: flex; justify-content: space-between; color: #68738e; font-size: 9px;
  letter-spacing: .06em; padding: 24px 4px 0;
}

@media (max-width: 1000px) {
  .hero { grid-template-columns: 1fr; min-height: auto; padding-top: 48px; }
  .pipeline-visual { display: none; }
  .capability-strip { grid-template-columns: repeat(2, 1fr); }
  .capability-strip article:nth-child(2) { border-right: 0; }
  .capability-strip article:nth-child(-n+2) { border-bottom: 1px solid var(--line); }
  #control-panel { position: static; }
}

@media (max-width: 720px) {
  .gradio-container { padding: 0 13px 28px !important; }
  .topbar { min-height: 66px; }
  .system-chip { display: none; }
  .hero { padding: 42px 5px 30px; }
  .hero h1 { font-size: 50px; }
  .hero p { font-size: 14px; }
  .capability-strip article { padding: 13px 11px; gap: 8px; }
  .capability-strip span { font-size: 8px; }
  #control-panel { padding: 18px !important; }
  #report-panel { min-width: 0 !important; }
  #report-toolbar { padding: 0 14px; }
  #research-status { display: none; }
  #research-report { padding: 25px 19px !important; }
  .app-footer { display: block; line-height: 1.8; }
  .app-footer span { display: block; }
}

/* v2.4 accessibility pass: brighter surfaces and enforced text contrast. */
:root {
  --bg: #0c1222;
  --surface: rgba(23, 32, 56, 0.96);
  --surface-solid: #172038;
  --surface-2: #1c2845;
  --line: rgba(190, 205, 240, 0.22);
  --line-bright: rgba(150, 132, 255, 0.58);
  --text: #f7f9ff;
  --muted: #b8c3da;
}

body {
  background:
    linear-gradient(rgba(255,255,255,.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.025) 1px, transparent 1px),
    radial-gradient(circle at 50% -10%, #302a6a 0, transparent 44%),
    #0c1222 !important;
}

.gradio-container {
  --body-background-fill: #0c1222;
  --block-background-fill: #172038;
  --input-background-fill: #10182a;
  --body-text-color: #f7f9ff;
  --block-label-text-color: #d9e1f2;
  --block-info-text-color: #aebbd4;
  color: var(--text) !important;
}

#control-panel,
#report-panel {
  background: linear-gradient(155deg, rgba(27, 38, 67, .98), rgba(18, 26, 47, .98)) !important;
  border-color: rgba(190, 205, 240, .24) !important;
}

#report-toolbar {
  background: #131c31 !important;
}

.panel-heading,
.panel-heading *,
#control-panel h1,
#control-panel h2,
#control-panel h3 {
  color: #ffffff !important;
}

.panel-copy,
.panel-copy *,
#control-panel p {
  color: #c2cce0 !important;
}

#control-panel .block:not(button),
#control-panel .form,
#control-panel .wrap,
#control-panel .secondary-wrap {
  background-color: #131d33 !important;
  color: #f4f7ff !important;
  border-color: rgba(190, 205, 240, .22) !important;
}

#control-panel label,
#control-panel label span,
#control-panel .label-wrap,
#control-panel .label-wrap span {
  color: #e5ebf8 !important;
}

#research-query,
#research-query textarea,
#control-panel input {
  background: #0f1729 !important;
  color: #ffffff !important;
}

#research-query textarea::placeholder,
#control-panel input::placeholder {
  color: #8f9db9 !important;
  opacity: 1 !important;
}

#depth-selector,
#depth-selector > div,
#depth-selector .wrap {
  background: #151f36 !important;
}

#depth-selector label,
#depth-selector label span {
  color: #eef3ff !important;
}

#mode-hint,
#mode-hint *,
#research-status,
#research-status * {
  color: #d7dff0 !important;
}

#mode-hint {
  background: rgba(128, 104, 255, .16) !important;
  border-color: rgba(157, 139, 255, .38) !important;
}

#research-report,
#research-report p,
#research-report li {
  color: #d4dced !important;
}

#research-report h1,
#research-report h2,
#research-report h3,
.empty-state h2 {
  color: #ffffff !important;
}

.report-label,
.capability-strip strong,
.capability-strip span,
.privacy-card strong,
.privacy-card p {
  color: #d6deef !important;
}

.empty-state p,
.empty-steps span,
.app-footer {
  color: #aebad2 !important;
}
"""

JS = """
() => {
  document.documentElement.style.scrollBehavior = 'smooth';
  const observer = new MutationObserver(() => {
    const report = document.querySelector('#research-report');
    if (report && report.innerText.includes('Complete')) {
      report.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
  observer.observe(document.body, { childList: true, subtree: true });
}
"""
