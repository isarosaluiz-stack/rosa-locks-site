# -*- coding: utf-8 -*-
"""Gera o site estático da Rosa Locks a partir de um template comum."""
import os

OUT = "site"
os.makedirs(OUT, exist_ok=True)

# ---- Configurações que o José troca depois ----
WA = "https://wa.me/55XXXXXXXXXXX?text=Ol%C3%A1%21%20Vim%20pelo%20site%20e%20quero%20falar%20sobre%20um%20projeto."  # TROCAR pelo número da Vanessa
INSTA = "https://instagram.com/rosalocks.arq"  # conferir handle

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
'<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,400;1,9..144,500&family=Work+Sans:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

CSS = """
  :root{
    --bg:#14130f; --paper:#e7e2d8; --ironwood:#221b13;
    --brass:#9c7a3c; --brass-soft:#c9ad74; --taupe:#8c8171;
    --paper-ink:#1c1a15; --dark-ink:#efeae0;
    --line-dark: rgba(239,234,224,0.14); --line-paper: rgba(28,26,21,0.14);
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{scroll-behavior:smooth;}
  body{ background:var(--bg); color:var(--dark-ink); font-family:'Work Sans',sans-serif; font-weight:300; -webkit-font-smoothing:antialiased; overflow-x:hidden; }
  a{color:inherit; text-decoration:none;}
  img{max-width:100%; display:block;}
  .eyebrow{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.18em; text-transform:uppercase; color:var(--brass); }
  h1,h2,h3{ font-family:'Fraunces',serif; font-weight:400; }
  .wrap{ max-width:1180px; margin:0 auto; padding:0 32px; }

  /* header */
  header{ position:fixed; top:0; left:0; right:0; z-index:50; padding:22px 0; transition:background .3s ease, padding .3s ease; }
  header.solid{ background:rgba(20,19,15,0.92); backdrop-filter:blur(8px); border-bottom:1px solid var(--line-dark); padding:16px 0; }
  header.static{ position:sticky; background:rgba(20,19,15,0.92); backdrop-filter:blur(8px); border-bottom:1px solid var(--line-dark); }
  header .wrap{ display:flex; align-items:center; justify-content:space-between; }
  .logo{ font-family:'Fraunces',serif; font-size:16px; letter-spacing:0.14em; text-transform:uppercase; color:var(--dark-ink); }
  .logo span{ color:var(--brass-soft); }
  nav.primary-nav{ display:flex; align-items:center; gap:34px; }
  nav.primary-nav a{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.1em; text-transform:uppercase; color:var(--dark-ink); opacity:0.78; transition:opacity .25s,color .25s; }
  nav.primary-nav a:hover{ opacity:1; color:var(--brass-soft); }
  nav.primary-nav a.current{ opacity:1; color:var(--brass-soft); }
  .btn-whats{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.08em; text-transform:uppercase; color:var(--bg); background:var(--brass-soft); padding:11px 20px; border-radius:2px; border:1px solid var(--brass-soft); transition:background .25s,color .25s,transform .2s; white-space:nowrap; }
  .btn-whats:hover{ background:transparent; color:var(--brass-soft); }
  a:focus-visible, button:focus-visible{ outline:2px solid var(--brass-soft); outline-offset:3px; }

  /* hero full-bleed */
  .hero{ position:relative; min-height:100vh; display:flex; align-items:flex-end; }
  .hero-media{ position:absolute; inset:0; z-index:0; }
  .hero-media img{ width:100%; height:100%; object-fit:cover; }
  .hero-media::after{ content:""; position:absolute; inset:0; background:linear-gradient(to top, rgba(15,14,10,0.92) 0%, rgba(15,14,10,0.45) 40%, rgba(15,14,10,0.25) 100%); }
  .hero-inner{ position:relative; z-index:2; width:100%; padding-bottom:9vh; padding-top:140px; }
  .hero-inner .eyebrow{ margin-bottom:22px; }
  .hero h1{ font-size:clamp(36px,5.2vw,68px); line-height:1.08; color:var(--dark-ink); max-width:15ch; }
  .hero h1 em{ font-style:italic; color:var(--brass-soft); }
  .hero .lede{ margin-top:24px; font-size:16px; line-height:1.7; color:#d8d2c6; max-width:46ch; }
  .hero-actions{ margin-top:36px; display:flex; align-items:center; gap:22px; flex-wrap:wrap; }
  .hero-actions .hint{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.05em; color:#b9b1a1; }
  .scroll-cue{ position:absolute; left:50%; bottom:26px; transform:translateX(-50%); z-index:2; font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:var(--taupe); }

  /* intro / estudio signature */
  .intro{ background:var(--paper); color:var(--paper-ink); padding:120px 0; }
  .intro .wrap{ display:grid; grid-template-columns:0.9fr 1.1fr; gap:64px; align-items:center; }
  .intro .eyebrow{ margin-bottom:20px; }
  .intro h2{ font-size:clamp(26px,3vw,36px); line-height:1.3; max-width:16ch; }
  .intro-body p{ font-size:16px; line-height:1.85; color:#4a463d; max-width:56ch; }
  .intro-body p + p{ margin-top:18px; }
  .intro-signature{ margin-top:34px; font-family:'Fraunces',serif; font-style:italic; font-size:17px; }
  .intro-signature span{ display:block; font-family:'IBM Plex Mono',monospace; font-style:normal; font-size:11px; letter-spacing:0.1em; text-transform:uppercase; color:var(--brass); margin-top:6px; }
  .croqui-frame{ border:1px solid var(--line-paper); padding:26px; border-radius:2px; background:linear-gradient(160deg, rgba(156,122,60,0.05), transparent 70%); }
  .draw path,.draw line,.draw rect,.draw polyline{ fill:none; stroke:var(--brass); stroke-width:1.1; stroke-linecap:round; stroke-linejoin:round; }
  .draw .fillfaint{ fill:var(--brass); fill-opacity:0.06; stroke:none; }
  .croqui-cap{ margin-top:14px; font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:0.1em; text-transform:uppercase; color:var(--taupe); }

  /* portfolio */
  .portfolio{ background:var(--bg); padding:120px 0; }
  .portfolio-head{ display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:48px; gap:24px; flex-wrap:wrap; }
  .portfolio-head h2{ font-size:clamp(26px,3vw,34px); color:var(--dark-ink); max-width:14ch; margin-top:14px; }
  .portfolio-head p{ color:var(--taupe); font-size:14px; max-width:34ch; line-height:1.7; }
  .grid2{ display:grid; grid-template-columns:repeat(2,1fr); gap:20px; }
  .grid3{ display:grid; grid-template-columns:repeat(3,1fr); gap:18px; }
  .pcard{ display:block; position:relative; overflow:hidden; border-radius:2px; background:var(--ironwood); }
  .pcard .ph{ aspect-ratio:4/3; overflow:hidden; }
  .pcard.tall .ph{ aspect-ratio:4/5; }
  .pcard img{ width:100%; height:100%; object-fit:cover; transition:transform .7s cubic-bezier(.2,.6,.2,1); }
  .pcard:hover img{ transform:scale(1.045); }
  .pcard .cap{ position:absolute; left:0; right:0; bottom:0; padding:22px 22px 20px; background:linear-gradient(to top, rgba(15,14,10,0.85), transparent); }
  .pcard h3{ font-size:20px; font-style:italic; color:var(--dark-ink); }
  .pcard .meta{ font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:0.08em; text-transform:uppercase; color:var(--brass-soft); margin-top:6px; }
  .see-all{ margin-top:44px; text-align:center; }

  /* atmosphere band */
  .band{ position:relative; height:70vh; min-height:420px; display:flex; align-items:center; justify-content:center; overflow:hidden; }
  .band img{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; }
  .band::after{ content:""; position:absolute; inset:0; background:rgba(15,14,10,0.5); z-index:1; }
  .band .band-text{ position:relative; z-index:2; text-align:center; max-width:22ch; }
  .band .band-text h2{ font-size:clamp(26px,3.4vw,40px); font-style:italic; color:var(--dark-ink); line-height:1.25; }

  /* services */
  .services{ background:var(--paper); color:var(--paper-ink); padding:120px 0; }
  .services .eyebrow{ margin-bottom:44px; }
  .service-row{ display:grid; grid-template-columns:1fr 2fr; gap:32px; padding:34px 0; border-top:1px solid var(--line-paper); align-items:baseline; }
  .service-row:last-child{ border-bottom:1px solid var(--line-paper); }
  .service-row h3{ font-size:24px; font-style:italic; }
  .service-row p{ font-size:15px; line-height:1.8; color:#4a463d; max-width:52ch; }

  /* closing */
  .closing{ background:var(--bg); padding:150px 0; text-align:center; }
  .closing.wood{ background:var(--ironwood); padding:100px 0; }
  .closing h2{ font-size:clamp(28px,4.4vw,50px); color:var(--dark-ink); max-width:18ch; margin:0 auto 32px; }
  .closing h2 em{ color:var(--brass-soft); font-style:italic; }
  .closing .btn-whats{ padding:16px 34px; font-size:12px; }

  /* footer */
  footer{ background:var(--ironwood); padding:46px 0; border-top:1px solid var(--line-dark); }
  footer .wrap{ display:flex; justify-content:space-between; align-items:center; gap:20px; flex-wrap:wrap; }
  footer .logo{ font-size:13px; }
  .foot-links{ display:flex; gap:26px; align-items:center; }
  .foot-links a,.foot-links span{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.08em; text-transform:uppercase; color:var(--taupe); }
  .foot-links a:hover{ color:var(--brass-soft); }

  /* ------- páginas internas ------- */
  .page-head{ padding:150px 0 52px; border-bottom:1px solid var(--line-dark); }
  .page-head .eyebrow{ margin-bottom:16px; }
  .page-head h1{ font-size:clamp(30px,4vw,48px); max-width:16ch; }
  .page-head p{ margin-top:18px; color:var(--taupe); max-width:52ch; line-height:1.7; font-size:15px; }
  .filters{ display:flex; gap:8px; margin-top:38px; flex-wrap:wrap; }
  .filter-btn{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.06em; text-transform:uppercase; padding:10px 18px; border:1px solid var(--line-dark); border-radius:2px; color:var(--taupe); background:transparent; cursor:pointer; transition:all .2s; }
  .filter-btn:hover{ color:var(--dark-ink); border-color:var(--brass-soft); }
  .filter-btn.active{ color:var(--bg); background:var(--brass-soft); border-color:var(--brass-soft); }

  /* project detail */
  .back-link{ display:inline-block; margin:150px 0 0; font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.08em; text-transform:uppercase; color:var(--taupe); }
  .back-link:hover{ color:var(--brass-soft); }
  .proj-head{ padding:22px 0 48px; display:grid; grid-template-columns:1.3fr 0.7fr; gap:48px; align-items:end; border-bottom:1px solid var(--line-dark); }
  .proj-head .eyebrow{ margin-bottom:16px; }
  .proj-head h1{ font-size:clamp(32px,5vw,54px); font-style:italic; }
  .specs{ display:grid; grid-template-columns:1fr 1fr; gap:18px 24px; }
  .spec-item .k{ font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:0.1em; text-transform:uppercase; color:var(--taupe); margin-bottom:4px; }
  .spec-item .v{ font-size:15px; color:var(--dark-ink); }
  .gallery-hero{ margin-top:46px; height:66vh; min-height:400px; overflow:hidden; }
  .gallery-hero img{ width:100%; height:100%; object-fit:cover; }
  .thumbs{ display:grid; gap:2px; margin-top:2px; }
  .thumbs.n1{ grid-template-columns:1fr; }
  .thumbs.n2{ grid-template-columns:repeat(2,1fr); }
  .thumbs.n3{ grid-template-columns:repeat(3,1fr); }
  .thumb{ aspect-ratio:4/3; overflow:hidden; cursor:pointer; position:relative; }
  .thumb img{ width:100%; height:100%; object-fit:cover; transition:transform .5s, opacity .3s; }
  .thumb:hover img{ transform:scale(1.05); }
  .narrative{ background:var(--paper); color:var(--paper-ink); padding:110px 0; }
  .narrative .wrap{ display:grid; grid-template-columns:0.8fr 1.2fr; gap:64px; }
  .narrative .eyebrow{ margin-bottom:18px; }
  .narrative h2{ font-size:clamp(24px,3vw,32px); max-width:15ch; }
  .narrative-body p{ font-size:16px; line-height:1.85; color:#4a463d; max-width:58ch; }
  .narrative-body p + p{ margin-top:18px; }
  .related{ background:var(--bg); padding:96px 0 120px; }
  .related .eyebrow{ margin-bottom:8px; }
  .related h2{ font-size:22px; font-style:italic; margin-bottom:30px; }
  .related-card{ display:grid; grid-template-columns:200px 1fr; gap:26px; align-items:center; padding:0; border:1px solid var(--line-dark); border-radius:2px; overflow:hidden; transition:border-color .2s; }
  .related-card:hover{ border-color:var(--brass-soft); }
  .related-card .rc-img{ aspect-ratio:4/3; overflow:hidden; }
  .related-card .rc-img img{ width:100%; height:100%; object-fit:cover; }
  .related-card .rc-body{ padding:20px 24px 20px 0; }
  .related-card h3{ font-size:18px; font-style:italic; margin-bottom:6px; }
  .related-card .meta{ font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:.08em; text-transform:uppercase; color:var(--taupe); }

  /* estudio */
  .studio-lead{ padding:60px 0 0; }
  .studio-grid{ display:grid; grid-template-columns:1fr 1fr; gap:56px; align-items:center; padding:80px 0 20px; }
  .studio-portrait{ aspect-ratio:4/5; overflow:hidden; border-radius:2px; }
  .studio-portrait img{ width:100%; height:100%; object-fit:cover; }
  .studio-bio p{ font-size:16px; line-height:1.85; color:#d8d2c6; max-width:56ch; }
  .studio-bio p + p{ margin-top:16px; }

  @media (max-width:860px){
    nav.primary-nav a:not(.btn-whats){ display:none; }
    .intro .wrap{ grid-template-columns:1fr; gap:40px; }
    .croqui-frame{ order:-1; }
    .grid2,.grid3{ grid-template-columns:1fr; }
    .band{ height:50vh; }
    .service-row{ grid-template-columns:1fr; gap:10px; }
    .portfolio-head{ flex-direction:column; align-items:flex-start; }
    .proj-head{ grid-template-columns:1fr; }
    .narrative .wrap{ grid-template-columns:1fr; }
    .thumbs.n3{ grid-template-columns:repeat(2,1fr); }
    .related-card{ grid-template-columns:1fr; }
    .studio-grid{ grid-template-columns:1fr; gap:32px; }
  }
  @media (prefers-reduced-motion: reduce){ *{ animation:none !important; transition:none !important; scroll-behavior:auto !important; } }
"""

CROQUI_SVG = """<svg id="houseSvg" class="draw" viewBox="0 0 560 420" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="360" x2="540" y2="360"></line>
  <line x1="90" y1="300" x2="90" y2="360"></line><line x1="140" y1="300" x2="140" y2="360"></line>
  <line x1="330" y1="300" x2="330" y2="360"></line><line x1="380" y1="300" x2="380" y2="360"></line>
  <rect class="fillfaint" x="70" y="190" width="360" height="112" rx="1"></rect>
  <path d="M70 302 L70 190 L430 190 L430 302"></path>
  <line x1="55" y1="190" x2="445" y2="190"></line><line x1="55" y1="182" x2="445" y2="182"></line>
  <line x1="130" y1="190" x2="130" y2="302"></line><line x1="190" y1="190" x2="190" y2="302"></line>
  <line x1="250" y1="190" x2="250" y2="302"></line><line x1="310" y1="190" x2="310" y2="302"></line>
  <line x1="370" y1="190" x2="370" y2="302"></line>
  <path d="M430 250 L500 250 L500 302 L430 302"></path><line x1="465" y1="250" x2="465" y2="302"></line>
  <rect x="90" y="372" width="180" height="26"></rect>
  <line x1="90" y1="385" x2="270" y2="385" stroke-dasharray="3 6"></line>
  <path d="M480 360 C476 330 500 320 498 296"></path><path d="M488 340 C500 336 506 322 502 310"></path>
  <line x1="20" y1="150" x2="445" y2="150" stroke-dasharray="1 6" opacity="0.4"></line>
</svg>"""

def header(current, static=False):
    cls = "static" if static else ""
    def nav(name, href):
        c = ' class="current"' if name.lower()==current else ''
        return f'<a href="{href}"{c}>{name}</a>'
    return f"""<header class="{cls}">
  <div class="wrap">
    <a href="index.html" class="logo">ROSA LOCKS <span>ARQUITETURA</span></a>
    <nav class="primary-nav">
      {nav('Projetos','projetos.html')}
      {nav('Estúdio','estudio.html')}
      {nav('Como trabalhamos','index.html#como-trabalhamos')}
      <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp</a>
    </nav>
  </div>
</header>"""

FOOTER = f"""<footer>
  <div class="wrap">
    <a href="index.html" class="logo">ROSA LOCKS <span>ARQUITETURA</span></a>
    <div class="foot-links">
      <span>Criciúma · SC</span>
      <a href="{INSTA}" target="_blank" rel="noopener">Instagram</a>
      <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
    </div>
  </div>
</footer>"""

SCROLL_JS = """<script>
  // header ganha fundo ao rolar (só na home, onde é fixo transparente)
  (function(){ var h=document.querySelector('header'); if(!h||h.classList.contains('static'))return;
    function on(){ if(window.scrollY>40) h.classList.add('solid'); else h.classList.remove('solid'); }
    window.addEventListener('scroll',on,{passive:true}); on(); })();
  // croqui se desenhando
  (function(){ var r=matchMedia('(prefers-reduced-motion: reduce)').matches; var s=document.getElementById('houseSvg'); if(!s||r)return;
    var els=s.querySelectorAll('path,line,rect,polyline'), d=0;
    els.forEach(function(el){ var len=200; try{ if(el.getTotalLength) len=el.getTotalLength(); }catch(e){}
      el.style.strokeDasharray=len; el.style.strokeDashoffset=len;
      el.style.transition='stroke-dashoffset 1.1s cubic-bezier(.4,0,.2,1) '+d+'s';
      requestAnimationFrame(function(){ requestAnimationFrame(function(){ el.style.strokeDashoffset='0'; }); }); d+=0.045; }); })();
  // reveal on scroll
  (function(){ var r=matchMedia('(prefers-reduced-motion: reduce)').matches; if(r)return;
    var els=document.querySelectorAll('.pcard,.service-row,.reveal');
    els.forEach(function(c){ c.style.opacity=0; c.style.transform='translateY(14px)'; c.style.transition='opacity .6s ease, transform .6s ease'; });
    var io=new IntersectionObserver(function(en){ en.forEach(function(e){ if(e.isIntersecting){ e.target.style.opacity=1; e.target.style.transform='none'; io.unobserve(e.target);} }); },{threshold:0.12});
    els.forEach(function(c){ io.observe(c); }); })();
</script>"""

def page(title, body, current, static=False, extra_js=""):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="Rosa Locks Arquitetura e Engenharia — projetos residenciais e de interiores de alto padrão em Criciúma e no litoral de Santa Catarina.">
{FONTS}
<style>{CSS}</style>
</head>
<body>
{header(current, static)}
{body}
{FOOTER}
{SCROLL_JS}
{extra_js}
</body>
</html>"""

# =================== PROJETOS (dados) ===================
# Cada projeto usa SOMENTE imagens do próprio grupo (sem risco de trocar obra).
# Textos marcados [EDITAR] são placeholders plausíveis pro José ajustar.
PROJETOS = [
  dict(slug="dd", nome="Casa D+D", tipo="residencial", tipo_label="Residencial",
       local="Santa Catarina", area="[EDITAR] m²", ano="[EDITAR]", escopo="Projeto completo",
       imgs=["dd-01.jpg","dd-02.jpg","dd-03.jpg","dd-04.jpg"],
       h2="Volumes de pedra e madeira em diálogo com o terreno.",
       narr=[
         "[EDITAR] Um resumo do partido: o que o terreno pediu, a implantação, a orientação solar e o programa da família. A Rosa Locks escreve a partir do que o José contar.",
         "[EDITAR] O uso de pedra natural e madeira define a materialidade da fachada; a piscina e a área externa foram pensadas como extensão das áreas de convívio.",
         "Projeto modelado inteiramente em BIM, compatibilizando estrutura, elétrica e hidráulica antes do início da obra."],
       related="fd"),
  dict(slug="fd", nome="Casa F+D", tipo="residencial", tipo_label="Residencial",
       local="Santa Catarina", area="[EDITAR] m²", ano="[EDITAR]", escopo="Projeto completo",
       imgs=["fd-01.jpg","fd-02.jpg","fd-03.jpg"],
       h2="Uma casa de linhas escuras e presença noturna.",
       narr=[
         "[EDITAR] O porquê da solução: como a paleta escura, a iluminação e os grandes vãos de vidro definiram o caráter do projeto.",
         "[EDITAR] A relação entre a piscina, o deck e os ambientes internos, e como a família vive esses espaços.",
         "Projeto desenvolvido em BIM, garantindo que o desenhado seja exatamente o construído."],
       related="dd"),
  dict(slug="ar", nome="Casa A+R", tipo="residencial", tipo_label="Residencial",
       local="Litoral de SC", area="[EDITAR] m²", ano="[EDITAR]", escopo="Projeto completo",
       imgs=["ar-01.jpg","ar-02.jpg"],
       h2="Contemporânea, aberta e voltada para o convívio ao ar livre.",
       narr=[
         "[EDITAR] Contexto litorâneo: teto plano, madeira quente e integração total entre interior e área de piscina.",
         "[EDITAR] Como o programa foi organizado para receber e para o dia a dia da família.",
         "Compatibilização completa em BIM antes da obra."],
       related="dd"),
  dict(slug="rg", nome="Projeto R+G", tipo="interiores", tipo_label="Interiores",
       local="Santa Catarina", area="[EDITAR] m²", ano="[EDITAR]", escopo="Interiores + marcenaria",
       imgs=["rg-01.jpg","rg-02.jpg"],
       h2="Interiores desenhados sob medida, do piso à marcenaria.",
       narr=[
         "[EDITAR] Projeto de interiores: como a iluminação quente, os materiais e a marcenaria sob medida foram especificados para os ambientes.",
         "[EDITAR] O modo de morar que orientou cada decisão de layout e acabamento.",
         "Especificação técnica completa, pronta para execução e compras."],
       related="ar"),
]
BY = {p["slug"]: p for p in PROJETOS}

def card(p, tall=False):
    cls = "pcard tall" if tall else "pcard"
    return f"""<a class="{cls}" href="projeto-{p['slug']}.html" data-tipo="{p['tipo']}">
      <div class="ph"><img src="assets/img/{p['imgs'][0]}" alt="{p['nome']}" loading="lazy"></div>
      <div class="cap"><h3>{p['nome']}</h3><div class="meta">{p['local']} · {p['tipo_label']}</div></div>
    </a>"""

# =================== HOME ===================
home_cards = "\n".join(card(BY[s]) for s in ["dd","fd","ar","rg"])
home_body = f"""
<section class="hero">
  <div class="hero-media"><img src="assets/img/hero.jpg" alt="Residência projetada pela Rosa Locks ao anoitecer"></div>
  <div class="hero-inner">
    <div class="wrap">
      <p class="eyebrow">Rosa Locks Arquitetura · Criciúma &amp; Litoral de SC</p>
      <h1>Cada projeto nasce do <em>terreno</em>, não do catálogo.</h1>
      <p class="lede">Arquitetura residencial e de interiores assinada pessoalmente pela arquiteta Isadora Rosa Luiz, do primeiro esboço à entrega das chaves.</p>
      <div class="hero-actions">
        <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Iniciar uma conversa</a>
        <span class="hint">resposta em minutos, direto no WhatsApp</span>
      </div>
    </div>
  </div>
  <div class="scroll-cue">role para ver ↓</div>
</section>

<section class="intro" id="estudio">
  <div class="wrap">
    <div>
      <p class="eyebrow">O Estúdio</p>
      <h2>Projeto pensado do zero, executado sem imprevistos.</h2>
      <div class="intro-body" style="margin-top:22px;">
        <p>A Rosa Locks projeta casas e interiores em Criciúma e no litoral de Santa Catarina, incluindo Itapema. Cada projeto é modelado em BIM desde o primeiro esboço, o que compatibiliza estrutura, elétrica e hidráulica antes da obra começar — e garante que o que foi desenhado seja exatamente o que se constrói.</p>
        <p>Não trabalhamos com plantas padronizadas. Cada terreno, orientação solar e forma de morar da família definem um projeto que não se repete em nenhum outro endereço.</p>
      </div>
      <div class="intro-signature">Isadora Rosa Luiz<span>Arquiteta responsável · acompanha pessoalmente cada projeto</span></div>
    </div>
    <div class="croqui-frame">
      {CROQUI_SVG}
      <div class="croqui-cap">— do esboço ao BIM, cada casa se desenha a partir do lugar</div>
    </div>
  </div>
</section>

<section class="portfolio" id="projetos">
  <div class="wrap">
    <div class="portfolio-head">
      <div><p class="eyebrow">Projetos selecionados</p><h2>Um recorte do que já saiu do papel.</h2></div>
      <p>Cada obra responde a um terreno, uma família e um jeito de morar específicos.</p>
    </div>
    <div class="grid2">
      {home_cards}
    </div>
    <div class="see-all"><a class="btn-whats" style="background:transparent;color:var(--brass-soft);" href="projetos.html">Ver todos os projetos</a></div>
  </div>
</section>

<section class="band">
  <img src="assets/img/atmo-01.jpg" alt="Arquitetura residencial Rosa Locks">
  <div class="band-text"><h2>A arquitetura certa desaparece no modo como a casa é vivida.</h2></div>
</section>

<section class="services" id="como-trabalhamos">
  <div class="wrap">
    <p class="eyebrow">Como trabalhamos</p>
    <div class="service-row"><h3>Residencial</h3><p>Projeto completo de arquitetura, do estudo de viabilidade no terreno às visitas técnicas em pontos-chave da obra.</p></div>
    <div class="service-row"><h3>Interiores</h3><p>Ambientes desenhados sob medida para quem já mora ou está prestes a se mudar, com marcenaria e especificação técnica.</p></div>
    <div class="service-row"><h3>Regularização</h3><p>Documentação e adequação de imóveis já construídos junto aos órgãos competentes, com laudo técnico responsável.</p></div>
  </div>
</section>

<section class="closing">
  <div class="wrap">
    <h2>O primeiro passo é <em>uma conversa</em>.</h2>
    <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Falar com a Vanessa no WhatsApp</a>
  </div>
</section>
"""
open(f"{OUT}/index.html","w").write(page("Rosa Locks Arquitetura — Criciúma &amp; Litoral de SC", home_body, "início", static=False))

# =================== PROJETOS (grid) ===================
grid_cards = "\n".join(card(p) for p in PROJETOS)
projetos_body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Portfólio</p>
    <h1>Projetos</h1>
    <p>Cada projeto responde a um terreno, uma família e um jeito de morar específicos. Nenhum se repete.</p>
    <div class="filters">
      <button class="filter-btn active" data-filter="todos">Todos</button>
      <button class="filter-btn" data-filter="residencial">Residencial</button>
      <button class="filter-btn" data-filter="interiores">Interiores</button>
    </div>
  </div>
</section>
<section class="wrap">
  <div class="grid3" id="grid" style="padding:56px 0 120px;">
    {grid_cards}
  </div>
</section>
"""
filter_js = """<script>
  var buttons=document.querySelectorAll('.filter-btn'); var cards=document.querySelectorAll('#grid .pcard');
  buttons.forEach(function(btn){ btn.addEventListener('click',function(){
    buttons.forEach(function(b){b.classList.remove('active');}); btn.classList.add('active');
    var f=btn.getAttribute('data-filter');
    cards.forEach(function(c){ c.style.display=(f==='todos'||c.getAttribute('data-tipo')===f)?'':'none'; });
  }); });
</script>"""
open(f"{OUT}/projetos.html","w").write(page("Projetos — Rosa Locks Arquitetura", projetos_body, "projetos", static=True, extra_js=filter_js))

# =================== PROJETO (detalhe) x4 ===================
def detail(p):
    rest = p["imgs"][1:]
    ncls = f"n{min(len(rest),3)}" if rest else "n1"
    thumbs = "".join(
        f'<div class="thumb"><img src="assets/img/{im}" alt="{p["nome"]} — imagem {i+2}" loading="lazy" data-full="assets/img/{im}"></div>'
        for i,im in enumerate(rest))
    thumbs_block = f'<div class="thumbs {ncls}">{thumbs}</div>' if rest else ""
    narr = "\n      ".join(f"<p>{t}</p>" for t in p["narr"])
    r = BY[p["related"]]
    swap_js = """<script>
  var hero=document.getElementById('mainimg');
  document.querySelectorAll('.thumb img').forEach(function(t){
    t.addEventListener('click',function(){ var f=t.getAttribute('data-full'); var old=hero.getAttribute('src');
      hero.style.opacity=0; setTimeout(function(){ hero.setAttribute('src',f); t.setAttribute('data-full',old); t.setAttribute('src',old); hero.style.opacity=1; },180); });
  }); hero.style.transition='opacity .25s ease';
</script>"""
    body = f"""
<div class="wrap"><a class="back-link" href="projetos.html">← Todos os projetos</a></div>
<div class="wrap">
  <div class="proj-head">
    <div><p class="eyebrow">{p['tipo_label']} · {p['local']}</p><h1>{p['nome']}</h1></div>
    <div class="specs">
      <div class="spec-item"><div class="k">Local</div><div class="v">{p['local']}</div></div>
      <div class="spec-item"><div class="k">Área</div><div class="v">{p['area']}</div></div>
      <div class="spec-item"><div class="k">Ano</div><div class="v">{p['ano']}</div></div>
      <div class="spec-item"><div class="k">Escopo</div><div class="v">{p['escopo']}</div></div>
    </div>
  </div>
</div>
<div class="gallery-hero"><img id="mainimg" src="assets/img/{p['imgs'][0]}" alt="{p['nome']} — imagem principal"></div>
{thumbs_block}
<section class="narrative">
  <div class="wrap">
    <div><p class="eyebrow">Sobre o projeto</p><h2>{p['h2']}</h2></div>
    <div class="narrative-body">
      {narr}
    </div>
  </div>
</section>
<section class="related">
  <div class="wrap">
    <p class="eyebrow">Continue navegando</p><h2>Outro projeto que pode interessar</h2>
    <a class="related-card" href="projeto-{r['slug']}.html">
      <div class="rc-img"><img src="assets/img/{r['imgs'][0]}" alt="{r['nome']}" loading="lazy"></div>
      <div class="rc-body"><h3>{r['nome']}</h3><p class="meta">{r['local']} · {r['tipo_label']}</p></div>
    </a>
  </div>
</section>
<section class="closing wood">
  <div class="wrap">
    <h2>Gostou do que viu? <em>Fale com a Vanessa</em> e conte o seu projeto.</h2>
    <a class="btn-whats" style="padding:15px 30px;font-size:12px;" href="{WA}" target="_blank" rel="noopener">Iniciar uma conversa</a>
  </div>
</section>
"""
    html = page(f"{p['nome']} — Rosa Locks Arquitetura", body, "projetos", static=True, extra_js=(swap_js if rest else ""))
    open(f"{OUT}/projeto-{p['slug']}.html","w").write(html)

for p in PROJETOS: detail(p)

# =================== ESTÚDIO ===================
estudio_body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Quem assina</p>
    <h1>O Estúdio</h1>
    <p>Um escritório de arquitetura e engenharia focado em residências de alto padrão em Criciúma e no litoral catarinense.</p>
  </div>
</section>
<div class="wrap studio-lead">
  <div class="studio-grid">
    <div class="studio-portrait"><img src="assets/img/intro.jpg" alt="Projeto Rosa Locks"></div>
    <div class="studio-bio reveal">
      <p class="eyebrow" style="margin-bottom:18px;">Isadora Rosa Luiz</p>
      <p>[EDITAR] Bio da Isadora: formação, ano de formatura e instituição, e a abordagem que ela quer transmitir. A Rosa Locks escreve o texto final a partir do que ela quiser destacar.</p>
      <p>[EDITAR] Prêmios, publicações ou reconhecimentos, se houver. Se não houver, este parágrafo pode falar da filosofia de projeto — atenção ao terreno, ao modo de morar e ao detalhe construtivo.</p>
      <p>Cada projeto do estúdio é acompanhado pessoalmente pela arquiteta, do primeiro esboço à entrega — sem terceirização da criação.</p>
      <div class="intro-signature" style="color:var(--brass-soft);margin-top:28px;">Isadora Rosa Luiz<span>Arquiteta responsável</span></div>
    </div>
  </div>
</div>
<section class="intro" style="margin-top:80px;">
  <div class="wrap">
    <div>
      <p class="eyebrow">Método</p>
      <h2>Do lugar ao desenho, e do desenho à obra.</h2>
      <div class="intro-body" style="margin-top:22px;">
        <p>Todo projeto começa no terreno: orientação solar, ventos, topografia e o jeito da família viver. A partir daí, o desenho é modelado em BIM, compatibilizando arquitetura, estrutura e instalações antes de qualquer tijolo.</p>
        <p>O resultado é uma obra mais previsível — menos surpresas no canteiro, e uma casa que corresponde exatamente ao que foi projetado.</p>
      </div>
    </div>
    <div class="croqui-frame">
      {CROQUI_SVG}
      <div class="croqui-cap">— cada casa se desenha a partir do lugar</div>
    </div>
  </div>
</section>
<section class="closing">
  <div class="wrap">
    <h2>Quer conversar sobre <em>o seu projeto</em>?</h2>
    <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp</a>
  </div>
</section>
"""
open(f"{OUT}/estudio.html","w").write(page("O Estúdio — Rosa Locks Arquitetura", estudio_body, "estúdio", static=True))

print("OK — páginas geradas:")
for f in sorted(os.listdir(OUT)):
    if f.endswith(".html"): print("  ", f)
