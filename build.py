# -*- coding: utf-8 -*-
import os, io

OUT = "/mnt/user-data/outputs"
os.makedirs(OUT, exist_ok=True)

WA = "https://wa.me/554888761429?text=Ol%C3%A1!%20Vim%20pelo%20site%20da%20Rosa%20Locks%20e%20quero%20falar%20sobre%20um%20projeto."

CSS = """
:root{
  --cream:#F6F3EE;
  --cream-2:#EFEAE2;
  --ink:#1C1B19;
  --ink-2:#3A3733;
  --muted:#8A837A;
  --line:rgba(28,27,25,.14);
  --line-soft:rgba(28,27,25,.08);
  --bronze:#9A7B4F;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--cream);color:var(--ink);font-family:'Jost',sans-serif;font-weight:300;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.wrap{max-width:1240px;margin:0 auto;padding:0 40px}
h1,h2,h3,.serif{font-family:'Cormorant Garamond',serif;font-weight:300}
.label{font-family:'Jost',sans-serif;font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);font-weight:400}

/* header */
header{position:sticky;top:0;z-index:60;background:rgba(246,243,238,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line-soft)}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:78px}
.brand{display:flex;align-items:center;gap:12px}
.brand .mono{width:34px;height:34px;border:1px solid var(--ink);display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:19px;letter-spacing:.02em}
.brand .name{line-height:1.15}
.brand .name b{display:block;font-family:'Jost',sans-serif;font-weight:500;font-size:12.5px;letter-spacing:.28em;text-transform:uppercase}
.brand .name i{display:block;font-style:normal;font-size:8.5px;letter-spacing:.36em;text-transform:uppercase;color:var(--muted);margin-top:2px}
nav{display:flex;align-items:center;gap:30px}
nav a{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-2);padding-bottom:3px;border-bottom:1px solid transparent;transition:.25s}
nav a:hover{border-color:var(--ink)}
nav a.on{border-color:var(--ink)}
.btn{display:inline-block;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;padding:13px 24px;border:1px solid var(--ink);color:var(--ink);background:transparent;transition:.28s;cursor:pointer}
.btn:hover{background:var(--ink);color:var(--cream)}
.btn-fill{background:var(--ink);color:var(--cream)}
.btn-fill:hover{background:transparent;color:var(--ink)}
.btn-light{border-color:var(--cream);color:var(--cream)}
.btn-light:hover{background:var(--cream);color:var(--ink)}
a:focus-visible,button:focus-visible{outline:2px solid var(--bronze);outline-offset:3px}

/* photo placeholders */
.ph{position:relative;background:linear-gradient(135deg,#dcd6cc,#c9c2b6 55%,#b9b1a4);overflow:hidden}
.ph.dark{background:linear-gradient(135deg,#3b3833,#2a2825 60%,#201e1b)}
.ph:after{content:attr(data-l);position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:9.5px;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.72);border:1px dashed rgba(255,255,255,.4);padding:8px 14px;white-space:nowrap}
.ph.light:after{color:rgba(28,27,25,.5);border-color:rgba(28,27,25,.25)}

/* hero */
.hero{position:relative;height:88vh;min-height:560px;display:flex;align-items:center}
.hero .bg{position:absolute;inset:0}
.hero .bg:before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(20,19,17,.82) 0%,rgba(20,19,17,.45) 48%,rgba(20,19,17,.15) 100%);z-index:2}
.hero .wrap{position:relative;z-index:3;color:#F6F3EE}
.hero h1{font-size:clamp(38px,5.2vw,74px);line-height:1.06;letter-spacing:.01em;text-transform:uppercase;max-width:13ch}
.hero p{margin-top:22px;max-width:34ch;font-size:15px;line-height:1.75;color:rgba(246,243,238,.82)}
.hero .btn{margin-top:36px}
.hero .scroll{position:absolute;left:40px;bottom:38px;z-index:3;display:flex;align-items:center;gap:14px;color:rgba(246,243,238,.75);font-size:10px;letter-spacing:.24em;text-transform:uppercase}
.hero .scroll span.line{width:64px;height:1px;background:rgba(246,243,238,.5);display:block}

/* stats */
.stats{border-bottom:1px solid var(--line-soft);background:var(--cream)}
.stats .wrap{display:grid;grid-template-columns:repeat(4,1fr)}
.stat{padding:38px 28px;border-right:1px solid var(--line-soft)}
.stat:last-child{border-right:0}
.stat .n{font-family:'Cormorant Garamond',serif;font-size:38px;line-height:1}
.stat .k{margin-top:8px;font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);line-height:1.7}

/* section heads */
section{padding:104px 0}
.sec-head{text-align:center;max-width:640px;margin:0 auto 56px}
.sec-head h2{font-size:clamp(28px,3.6vw,44px);letter-spacing:.08em;text-transform:uppercase}
.sec-head p{margin-top:16px;font-size:14.5px;line-height:1.8;color:var(--muted)}

/* project cards */
.pgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:26px}
.pgrid.three{grid-template-columns:repeat(3,1fr);gap:30px}
.pcard .ph{aspect-ratio:4/5;transition:.5s}
.pcard:hover .ph{filter:brightness(1.06)}
.pcard h3{margin-top:16px;font-family:'Jost',sans-serif;font-weight:400;font-size:12px;letter-spacing:.16em;text-transform:uppercase}
.pcard .t{margin-top:5px;font-size:11px;letter-spacing:.1em;color:var(--muted);text-transform:uppercase}
.center{text-align:center}
.mt48{margin-top:48px}

/* quote band */
.quote{background:var(--ink);color:var(--cream);padding:96px 0}
.quote .wrap{max-width:900px;text-align:center}
.quote .mark{font-family:'Cormorant Garamond',serif;font-size:56px;line-height:0;color:var(--bronze);display:block;margin-bottom:26px}
.quote p{font-family:'Cormorant Garamond',serif;font-size:clamp(22px,2.7vw,32px);line-height:1.5;font-style:italic}
.quote .who{margin-top:26px;font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:rgba(246,243,238,.6)}

/* cta band */
.cta{position:relative;padding:0}
.cta .ph{height:300px}
.cta .inner{position:absolute;inset:0;display:flex;align-items:center;justify-content:space-between;gap:30px;z-index:3}
.cta .inner .wrap{display:flex;align-items:center;justify-content:space-between;gap:30px;width:100%}
.cta:before{content:'';position:absolute;inset:0;background:rgba(20,19,17,.62);z-index:2}
.cta h2{color:var(--cream);font-size:clamp(24px,3.2vw,38px);letter-spacing:.06em;text-transform:uppercase;line-height:1.25;max-width:16ch}

/* footer */
footer{background:var(--cream-2);border-top:1px solid var(--line-soft);padding:34px 0}
footer .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}
footer .links{display:flex;gap:26px}
footer .links a,footer .copy{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
footer .links a:hover{color:var(--ink)}

/* generic page head */
.phead{padding:78px 0 10px;text-align:center}
.phead h1{font-size:clamp(32px,4.4vw,54px);letter-spacing:.09em;text-transform:uppercase}
.phead p{margin:16px auto 0;max-width:52ch;font-size:14.5px;line-height:1.8;color:var(--muted)}

/* filters */
.filters{display:flex;justify-content:center;gap:6px;flex-wrap:wrap;margin:38px 0 46px}
.fbtn{font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;padding:10px 18px;border:1px solid transparent;color:var(--muted);background:none;cursor:pointer;transition:.2s}
.fbtn:hover{color:var(--ink)}
.fbtn.on{color:var(--ink);border-color:var(--line)}

/* project detail */
.detail-hero{height:62vh;min-height:420px;position:relative}
.detail-hero:before{content:'';position:absolute;inset:0;background:linear-gradient(0deg,rgba(20,19,17,.72),rgba(20,19,17,.15));z-index:2}
.detail-hero .cap{position:absolute;left:0;right:0;bottom:44px;z-index:3;color:var(--cream)}
.detail-hero h1{font-size:clamp(30px,4.4vw,52px);letter-spacing:.06em;text-transform:uppercase}
.detail-hero .t{margin-top:8px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:rgba(246,243,238,.75)}
.back{display:inline-block;padding:26px 0;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.back:hover{color:var(--ink)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start}
.blk h3{font-size:12px;font-family:'Jost',sans-serif;font-weight:500;letter-spacing:.22em;text-transform:uppercase;margin-bottom:14px}
.blk p{font-size:15px;line-height:1.85;color:var(--ink-2);max-width:46ch}
.blk + .blk{margin-top:40px}
.specs{display:grid;grid-template-columns:repeat(4,1fr);gap:26px;border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);padding:26px 0;margin:56px 0}
.specs .k{font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.specs .v{margin-top:6px;font-size:15px}
.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.gal .ph{aspect-ratio:4/3}
.gal .ph.wide{grid-column:span 2;aspect-ratio:8/3}

/* about */
.split{display:grid;grid-template-columns:1fr 1fr;align-items:center}
.split .ph{height:100%;min-height:480px}
.split .txt{padding:0 8% }
.split h2{font-size:clamp(28px,3.4vw,42px);letter-spacing:.08em;text-transform:uppercase}
.split p{margin-top:20px;font-size:15px;line-height:1.85;color:var(--ink-2);max-width:44ch}
.people{display:grid;grid-template-columns:1fr 1fr;gap:0;background:var(--ink);color:var(--cream)}
.person{display:grid;grid-template-columns:1fr 1.2fr;align-items:center;gap:0}
.person .ph{aspect-ratio:3/4}
.person .txt{padding:40px 34px}
.person h3{font-family:'Jost',sans-serif;font-weight:400;font-size:12px;letter-spacing:.2em;text-transform:uppercase}
.person .role{margin-top:6px;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--bronze)}
.person p{margin-top:14px;font-size:13.5px;line-height:1.75;color:rgba(246,243,238,.72)}
.values{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line-soft)}
.value{padding:44px 26px;border-right:1px solid var(--line-soft);text-align:center}
.value:last-child{border-right:0}
.value svg{width:26px;height:26px;margin:0 auto 16px;display:block;stroke:var(--ink);fill:none;stroke-width:1.1}
.value h4{font-family:'Jost',sans-serif;font-weight:400;font-size:11px;letter-spacing:.2em;text-transform:uppercase}
.value p{margin-top:10px;font-size:12.5px;line-height:1.7;color:var(--muted)}

/* services */
.sgrid{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line-soft);border-left:1px solid var(--line-soft)}
.scard{padding:46px 34px;border-right:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);text-align:center}
.scard svg{width:30px;height:30px;margin:0 auto 20px;display:block;stroke:var(--ink);fill:none;stroke-width:1}
.scard h3{font-family:'Jost',sans-serif;font-weight:400;font-size:11.5px;letter-spacing:.2em;text-transform:uppercase}
.scard p{margin-top:12px;font-size:13px;line-height:1.75;color:var(--muted);max-width:30ch;margin-left:auto;margin-right:auto}

/* process */
.steps{border-top:1px solid var(--line-soft)}
.step{display:grid;grid-template-columns:70px 1fr 300px;gap:30px;align-items:center;padding:26px 0;border-bottom:1px solid var(--line-soft)}
.step .n{font-family:'Cormorant Garamond',serif;font-size:32px;color:var(--muted)}
.step h3{font-family:'Jost',sans-serif;font-weight:400;font-size:12px;letter-spacing:.2em;text-transform:uppercase}
.step p{margin-top:8px;font-size:13.5px;line-height:1.75;color:var(--muted);max-width:52ch}
.step .ph{aspect-ratio:16/9}

@media (max-width:1000px){
  .pgrid{grid-template-columns:repeat(2,1fr)}
  .pgrid.three{grid-template-columns:repeat(2,1fr)}
  .stats .wrap{grid-template-columns:repeat(2,1fr)}
  .stat{border-bottom:1px solid var(--line-soft)}
  .two{grid-template-columns:1fr;gap:36px}
  .gal{grid-template-columns:repeat(2,1fr)}
  .gal .ph.wide{grid-column:span 2}
  .split{grid-template-columns:1fr}
  .split .txt{padding:56px 40px}
  .split .ph{min-height:340px}
  .people{grid-template-columns:1fr}
  .values{grid-template-columns:repeat(2,1fr)}
  .value{border-bottom:1px solid var(--line-soft)}
  .sgrid{grid-template-columns:repeat(2,1fr)}
  .step{grid-template-columns:52px 1fr;}
  .step .ph{display:none}
  .specs{grid-template-columns:repeat(2,1fr)}
}
@media (max-width:760px){
  .wrap{padding:0 22px}
  nav a:not(.btn){display:none}
  .pgrid,.pgrid.three{grid-template-columns:1fr}
  .sgrid{grid-template-columns:1fr}
  .cta .inner .wrap{flex-direction:column;text-align:center}
  .hero .scroll{display:none}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
"""

HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
"""

def header(active=""):
    def a(href, name, key):
        on = " on" if key == active else ""
        return f'<a class="{on.strip()}" href="{href}">{name}</a>'
    return f"""
<header>
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="mono">R</span>
      <span class="name"><b>Rosa Locks</b><i>Arquitetura</i></span>
    </a>
    <nav>
      {a("projetos.html","Projetos","projetos")}
      {a("servicos.html","Serviços","servicos")}
      {a("processo.html","Processo","processo")}
      {a("sobre.html","Sobre","sobre")}
      {a("contato.html","Contato","contato")}
      <a class="btn" href="{WA}" target="_blank" rel="noopener">Agendar reunião</a>
    </nav>
  </div>
</header>
"""

FOOTER = f"""
<footer>
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="mono">R</span>
      <span class="name"><b>Rosa Locks</b><i>Arquitetura</i></span>
    </a>
    <div class="links">
      <a href="projetos.html">Projetos</a>
      <a href="servicos.html">Serviços</a>
      <a href="sobre.html">Sobre</a>
      <a href="contato.html">Contato</a>
      <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
    </div>
    <span class="copy">© 2026 Rosa Locks Arquitetura</span>
  </div>
</footer>
</body>
</html>
"""

def cta_band(title="Vamos criar algo extraordinário juntos."):
    return f"""
<section class="cta">
  <div class="ph dark" data-l="Foto ambiente — 1920×600"></div>
  <div class="inner">
    <div class="wrap">
      <h2>{title}</h2>
      <a class="btn btn-light" href="{WA}" target="_blank" rel="noopener">Agendar uma reunião</a>
    </div>
  </div>
</section>
"""

PROJETOS = [
    ("Casa Horizonte", "Residencial", "residencial"),
    ("Chalés Encontros do Mundo", "Hospitalidade", "hospitalidade"),
    ("Tigre Sports Bar", "Comercial", "comercial"),
    ("CEO Room", "Comercial", "comercial"),
    ("Residência Itália", "Residencial", "residencial"),
    ("Saint Bier", "Comercial", "comercial"),
    ("Casa Dunas", "Residencial", "residencial"),
    ("Residência AT", "Interiores", "interiores"),
]

def pcard(nome, tipo, ratio_label="Foto — 900×1120"):
    return f"""
      <a class="pcard" href="projeto.html">
        <div class="ph" data-l="{ratio_label}"></div>
        <h3>{nome}</h3>
        <div class="t">{tipo}</div>
      </a>"""

# ---------------- HOME ----------------
home = HEAD.format(title="Rosa Locks Arquitetura", css=CSS) + header("") + f"""
<section class="hero" style="padding:0">
  <div class="bg ph dark" data-l="Foto principal — 1920×1080"></div>
  <div class="wrap">
    <h1>Arquitetura que traduz quem você é.</h1>
    <p>Projetos autorais que conectam forma, função e essência, do primeiro esboço à entrega das chaves.</p>
    <div><a class="btn btn-light" href="{WA}" target="_blank" rel="noopener">Agendar uma reunião</a></div>
  </div>
  <div class="scroll"><span>Saiba mais</span><span class="line"></span></div>
</section>

<div class="stats">
  <div class="wrap">
    <div class="stat"><div class="n">+10</div><div class="k">Anos de<br>experiência</div></div>
    <div class="stat"><div class="n">+200</div><div class="k">Projetos<br>entregues</div></div>
    <div class="stat"><div class="n serif" style="font-size:16px;letter-spacing:.14em;text-transform:uppercase">Arquitetura e engenharia</div><div class="k">Integradas na<br>mesma equipe</div></div>
    <div class="stat"><div class="n serif" style="font-size:16px;letter-spacing:.14em;text-transform:uppercase">Tecnologia BIM</div><div class="k">Menos imprevistos<br>na obra</div></div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="sec-head">
      <h2>Projetos em destaque</h2>
      <p>Conheça alguns dos espaços que já transformamos.</p>
    </div>
    <div class="pgrid">
      {''.join(pcard(n,t) for n,t,_ in PROJETOS[:4])}
    </div>
    <div class="center mt48"><a class="btn" href="projetos.html">Ver todos os projetos</a></div>
  </div>
</section>

<div class="quote">
  <div class="wrap">
    <span class="mark">“</span>
    <p>O verdadeiro luxo não está nos materiais mais caros, mas em viver num espaço pensado exclusivamente para você.</p>
    <div class="who">Rosa Locks Arquitetura</div>
  </div>
</div>

{cta_band()}
""" + FOOTER

# ---------------- PROJETOS ----------------
projetos = HEAD.format(title="Projetos — Rosa Locks", css=CSS) + header("projetos") + f"""
<div class="phead">
  <div class="wrap">
    <h1>Projetos</h1>
    <p>Cada projeto é único. Conheça alguns dos espaços que ajudamos a transformar.</p>
    <div class="filters">
      <button class="fbtn on" data-f="todos">Todos</button>
      <button class="fbtn" data-f="residencial">Residencial</button>
      <button class="fbtn" data-f="comercial">Comercial</button>
      <button class="fbtn" data-f="hospitalidade">Hospitalidade</button>
      <button class="fbtn" data-f="interiores">Interiores</button>
    </div>
  </div>
</div>

<section style="padding-top:0">
  <div class="wrap">
    <div class="pgrid three" id="grid">
      {''.join(f'<a class="pcard" href="projeto.html" data-t="{k}"><div class="ph" data-l="Foto — 900×1120"></div><h3>{n}</h3><div class="t">{t}</div></a>' for n,t,k in PROJETOS)}
    </div>
    <div class="center mt48"><button class="btn" type="button">Carregar mais</button></div>
  </div>
</section>

{cta_band("Vamos criar um projeto com a sua essência.")}

<script>
document.querySelectorAll('.fbtn').forEach(function(b){{
  b.addEventListener('click',function(){{
    document.querySelectorAll('.fbtn').forEach(function(x){{x.classList.remove('on')}});
    b.classList.add('on');
    var f=b.dataset.f;
    document.querySelectorAll('#grid .pcard').forEach(function(c){{
      c.style.display=(f==='todos'||c.dataset.t===f)?'':'none';
    }});
  }});
}});
</script>
""" + FOOTER

# ---------------- PROJETO INDIVIDUAL ----------------
projeto = HEAD.format(title="Casa Horizonte — Rosa Locks", css=CSS) + header("projetos") + f"""
<div class="wrap"><a class="back" href="projetos.html">← Voltar para projetos</a></div>

<div class="detail-hero ph dark" data-l="Foto de capa — 1920×1080">
  <div class="cap"><div class="wrap"><h1>Casa Horizonte</h1><div class="t">Residencial · Criciúma, SC</div></div></div>
</div>

<section>
  <div class="wrap two">
    <div>
      <div class="blk">
        <h3>O desafio</h3>
        <p>Criar uma residência que integrasse conforto, sofisticação e conexão com a natureza, num terreno de frente estreita e fundo profundo.</p>
      </div>
      <div class="blk">
        <h3>A solução</h3>
        <p>Desenvolvemos um projeto atemporal, com espaços amplos e integrados, materiais nobres e iluminação pensada para valorizar cada detalhe ao longo do dia.</p>
      </div>
    </div>
    <div class="gal" style="grid-template-columns:1fr 1fr">
      <div class="ph" data-l="Interior — 800×600"></div>
      <div class="ph" data-l="Detalhe — 800×600"></div>
    </div>
  </div>

  <div class="wrap">
    <div class="specs">
      <div><div class="k">Local</div><div class="v">Criciúma, SC</div></div>
      <div><div class="k">Área</div><div class="v">310 m²</div></div>
      <div><div class="k">Ano</div><div class="v">2025</div></div>
      <div><div class="k">Escopo</div><div class="v">Projeto completo</div></div>
    </div>
  </div>

  <div class="wrap">
    <div class="label" style="margin-bottom:18px">Galeria</div>
    <div class="gal">
      <div class="ph" data-l="Foto 01"></div>
      <div class="ph" data-l="Foto 02"></div>
      <div class="ph" data-l="Foto 03"></div>
      <div class="ph wide" data-l="Foto panorâmica — 1600×600"></div>
      <div class="ph" data-l="Foto 04"></div>
    </div>
  </div>

  <div class="wrap" style="margin-top:64px">
    <div class="label" style="margin-bottom:18px">Plantas</div>
    <div class="ph light" data-l="Planta baixa — desenho técnico" style="aspect-ratio:16/6;background:linear-gradient(135deg,#F1EDE6,#E6E0D6)"></div>
  </div>
</section>

<div class="quote">
  <div class="wrap">
    <span class="mark">“</span>
    <p>Desde o primeiro contato nos sentimos seguros. O projeto ficou exatamente como sonhávamos, e a obra seguiu com muita perfeição.</p>
    <div class="who">Família — cliente Rosa Locks</div>
  </div>
</div>

{cta_band("Vamos criar um projeto com a sua essência.")}
""" + FOOTER

# ---------------- SOBRE ----------------
def icon(paths):
    return f'<svg viewBox="0 0 24 24">{paths}</svg>'

sobre = HEAD.format(title="Sobre — Rosa Locks", css=CSS) + header("sobre") + f"""
<div class="split">
  <div class="txt">
    <div class="label" style="margin-bottom:16px">O escritório</div>
    <h2>Sobre nós</h2>
    <p>A Rosa Locks nasceu da união entre sensibilidade estética e rigor técnico. Somos um escritório de arquitetura e engenharia em Criciúma, atendendo também o litoral de Santa Catarina.</p>
    <p>Criamos espaços exclusivos, que refletem a essência de quem vive neles, com projetos modelados em BIM do primeiro esboço à entrega.</p>
    <div style="margin-top:32px"><a class="btn" href="processo.html">Conheça nosso processo</a></div>
  </div>
  <div class="ph" data-l="Retrato — 900×1100"></div>
</div>

<div class="people">
  <div class="person">
    <div class="ph dark" data-l="Foto Isadora"></div>
    <div class="txt">
      <h3>Isadora Rosa Luiz</h3>
      <div class="role">Arquiteta e fundadora</div>
      <p>Responsável pela direção criativa dos projetos, com olhar atento aos detalhes e à experiência de cada cliente.</p>
    </div>
  </div>
  <div class="person">
    <div class="ph dark" data-l="Foto José"></div>
    <div class="txt">
      <h3>José Locks</h3>
      <div class="role">Co-fundador</div>
      <p>Responsável pela coordenação técnica e comercial, garantindo previsibilidade e excelência na execução.</p>
    </div>
  </div>
</div>

<div class="values">
  <div class="value">{icon('<path d="M12 3l7 4v6c0 4-3 7-7 8-4-1-7-4-7-8V7z"/>')}<h4>Propósito</h4><p>Projetar com significado, não por repetição.</p></div>
  <div class="value">{icon('<path d="M12 3l2.6 5.6L21 9.6l-4.5 4.3 1.1 6.1L12 17.1 6.4 20l1.1-6.1L3 9.6l6.4-1z"/>')}<h4>Excelência</h4><p>Compromisso com a qualidade em cada detalhe.</p></div>
  <div class="value">{icon('<circle cx="12" cy="12" r="8"/><path d="M12 8v8M8 12h8"/>')}<h4>Inovação</h4><p>Tecnologia BIM e criatividade caminhando juntas.</p></div>
  <div class="value">{icon('<path d="M4 20v-2a4 4 0 014-4h2M16 6a3 3 0 11-6 0 3 3 0 016 0zM14 20v-2a4 4 0 014-4h2"/>')}<h4>Relacionamento</h4><p>Parcerias que atravessam todas as etapas.</p></div>
</div>

{cta_band()}
""" + FOOTER

# ---------------- SERVIÇOS ----------------
servicos = HEAD.format(title="Serviços — Rosa Locks", css=CSS) + header("servicos") + f"""
<div class="phead">
  <div class="wrap">
    <h1>Serviços</h1>
    <p>Soluções completas para todas as etapas do seu projeto.</p>
  </div>
</div>

<section style="padding-top:56px">
  <div class="wrap">
    <div class="sgrid">
      <div class="scard">{icon('<path d="M3 11l9-7 9 7v9a1 1 0 01-1 1h-5v-6H9v6H4a1 1 0 01-1-1z"/>')}<h3>Arquitetura residencial</h3><p>Projetos autorais pensados em cada detalhe para o estilo de vida da família.</p></div>
      <div class="scard">{icon('<path d="M4 21V6l7-3v18M11 21V9l9 3v9M15 14v3M8 9v3"/>')}<h3>Arquitetura comercial</h3><p>Soluções arquitetônicas que fortalecem marcas e negócios.</p></div>
      <div class="scard">{icon('<path d="M3 20h18M6 20V9l6-4 6 4v11M10 20v-5h4v5"/>')}<h3>Interiores</h3><p>Projetos de interiores que unem estética e funcionalidade.</p></div>
      <div class="scard">{icon('<path d="M6 3h9l5 5v13H6zM15 3v5h5M9 13h7M9 17h7"/>')}<h3>Regularização</h3><p>Cuidamos da documentação e da adequação do seu imóvel.</p></div>
      <div class="scard">{icon('<path d="M4 19h16M6 19V8l6-4 6 4v11M9 19v-6h6v6"/>')}<h3>Engenharia</h3><p>Soluções estruturais e complementares com segurança e eficiência.</p></div>
      <div class="scard">{icon('<path d="M4 5h16v14H4zM4 10h16M9 5v14"/>')}<h3>Compatibilização BIM</h3><p>Mais precisão, menos imprevistos e maior controle da obra.</p></div>
    </div>
  </div>
</section>

<div class="split" style="background:var(--cream-2)">
  <div class="ph" data-l="Foto processo — 900×700"></div>
  <div class="txt">
    <div class="label" style="margin-bottom:16px">Diferencial</div>
    <h2>Tecnologia e processos BIM</h2>
    <p>Mais precisão, menos imprevistos e economia em todas as etapas da obra. O projeto é compatibilizado antes de a primeira parede subir.</p>
    <div style="margin-top:30px"><a class="btn" href="processo.html">Ver o processo completo</a></div>
  </div>
</div>

{cta_band()}
""" + FOOTER

# ---------------- PROCESSO ----------------
STEPS = [
 ("01","Conhecimento","Entendemos suas necessidades, seus sonhos e seu estilo de vida."),
 ("02","Estudo preliminar","Analisamos o terreno e exploramos as melhores possibilidades."),
 ("03","Projeto","Desenvolvemos o projeto a uma estética, funcionalidade e técnica."),
 ("04","Detalhamento","Detalhamento completo para uma execução precisa."),
 ("05","Execução","Acompanhamento e gestão para garantir a qualidade na obra."),
 ("06","Acompanhamento","Estamos ao seu lado até a entrega final do projeto."),
]
processo = HEAD.format(title="Processo — Rosa Locks", css=CSS) + header("processo") + f"""
<div class="phead">
  <div class="wrap">
    <h1>Nosso processo</h1>
    <p>Um caminho claro e transparente para garantir sua tranquilidade.</p>
  </div>
</div>

<section style="padding-top:48px">
  <div class="wrap">
    <div class="steps">
      {''.join(f'<div class="step"><div class="n">{n}</div><div><h3>{t}</h3><p>{d}</p></div><div class="ph" data-l="Foto etapa {n}"></div></div>' for n,t,d in STEPS)}
    </div>
  </div>
</section>

{cta_band()}
""" + FOOTER

# ---------------- CONTATO ----------------
contato = HEAD.format(title="Contato — Rosa Locks", css=CSS) + header("contato") + f"""
<section>
  <div class="wrap two" style="gap:56px">
    <div>
      <div class="label" style="margin-bottom:18px">Contato</div>
      <h2 style="font-size:clamp(28px,3.4vw,42px);letter-spacing:.07em;text-transform:uppercase;line-height:1.2">Vamos conversar sobre o seu projeto</h2>
      <p style="margin-top:20px;font-size:15px;line-height:1.85;color:var(--ink-2);max-width:40ch">Será um prazer entender suas ideias e transformá-las em um projeto único.</p>

      <div style="margin-top:40px;display:grid;gap:16px;font-size:14px;color:var(--ink-2)">
        <div>WhatsApp · (48) 8876-1429</div>
        <div>contato@rosalocks.com.br</div>
        <div>@rosalocks.arquitetura</div>
        <div>Criciúma · SC</div>
      </div>

      <div style="margin-top:40px">
        <a class="btn btn-fill" href="{WA}" target="_blank" rel="noopener">Falar agora no WhatsApp</a>
      </div>
      <p style="margin-top:16px;font-size:12px;color:var(--muted);max-width:38ch;line-height:1.7">Atendimento imediato pelo WhatsApp. Respondemos em poucos minutos durante o horário comercial.</p>
    </div>
    <div class="ph" data-l="Foto do escritório — 900×700" style="aspect-ratio:4/3"></div>
  </div>
</section>

<div class="ph light" data-l="Mapa — localização do escritório" style="height:320px;background:linear-gradient(135deg,#EDE8E0,#E2DCD2)"></div>

{cta_band()}
""" + FOOTER

files = {
 "index.html": home,
 "projetos.html": projetos,
 "projeto.html": projeto,
 "sobre.html": sobre,
 "servicos.html": servicos,
 "processo.html": processo,
 "contato.html": contato,
}
for name, content in files.items():
    with io.open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
print("gerados:", ", ".join(files.keys()))
