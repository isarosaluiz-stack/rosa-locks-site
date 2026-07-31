# -*- coding: utf-8 -*-
"""Gera o site estático da Rosa Locks a partir de um template comum."""
import os

OUT = "."
os.makedirs(OUT, exist_ok=True)

# ---- Configurações que o José troca depois ----
WA = "https://wa.me/5548988761429?text=Ol%C3%A1%21%20Vim%20pelo%20site%20e%20quero%20falar%20sobre%20um%20projeto."
INSTA = "https://www.instagram.com/rosalocks.arquitetura/"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
'<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300,0,0;0,9..144,400,0,0;0,9..144,500,0,0;1,9..144,400,0,0;1,9..144,500,0,0&family=Work+Sans:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

CSS = """
  :root{
    --bg:#1c1c1c; --paper:#f2efea; --ironwood:#141414;
    --brass:#b67e57; --brass-soft:#c99671; --taupe:#8c8171;
    --bordo:#5a2e35;
    --paper-ink:#1c1c1c; --dark-ink:#f2efea;
    --line-dark: rgba(242,239,234,0.14); --line-paper: rgba(28,28,28,0.14);
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{ scroll-behavior:smooth; overflow-x:hidden; overflow-x:clip; }
  body{ background:var(--bg); color:var(--dark-ink); font-family:'Work Sans',sans-serif; font-weight:300; -webkit-font-smoothing:antialiased; overflow-x:hidden; overflow-x:clip; }
  a{color:inherit; text-decoration:none;}
  img{max-width:100%; display:block;}
  .eyebrow{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.18em; text-transform:uppercase; color:var(--brass); }
  h1,h2,h3{ font-family:'Fraunces',serif; font-weight:400; font-variation-settings:'SOFT' 0, 'WONK' 0, 'opsz' 144; }
  .wrap{ max-width:1180px; margin:0 auto; padding:0 32px; }

  /* header */
  header{ position:fixed; top:0; left:0; right:0; z-index:50; padding:22px 0; transition:background .3s ease, padding .3s ease; }
  header.solid{ background:rgba(20,19,15,0.92); backdrop-filter:blur(8px); border-bottom:1px solid var(--line-dark); padding:16px 0; }
  header.static{ position:sticky; background:rgba(20,19,15,0.92); backdrop-filter:blur(8px); border-bottom:1px solid var(--line-dark); }
  header .wrap{ display:flex; align-items:center; justify-content:space-between; }
  .logo{ font-family:'Fraunces',serif; font-size:16px; letter-spacing:0.14em; text-transform:uppercase; color:var(--dark-ink); display:inline-flex; align-items:center; }
  .logo span{ color:var(--brass-soft); }
  .logo-img{ height:44px; width:auto; display:block; }
  header.solid .logo-img{ height:36px; transition:height .3s ease; }
  footer .logo-img{ height:40px; opacity:0.9; }
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
  .intro.flip .wrap{ grid-template-columns:0.9fr 1.1fr; }
  .intro .eyebrow{ margin-bottom:20px; }
  .intro h2{ font-size:clamp(26px,3vw,36px); line-height:1.3; max-width:16ch; }
  .intro-body p{ font-size:16px; line-height:1.85; color:#4a463d; max-width:56ch; }
  .intro-body p + p{ margin-top:18px; }
  .intro-signature{ margin-top:34px; font-family:'Fraunces',serif; font-style:italic; font-size:17px; }
  .intro-signature span{ display:block; font-family:'IBM Plex Mono',monospace; font-style:normal; font-size:11px; letter-spacing:0.1em; text-transform:uppercase; color:var(--brass); margin-top:6px; }
  .intro-photo{ border-radius:2px; overflow:hidden; aspect-ratio:4/5; }
  .intro-photo img{ width:100%; height:100%; object-fit:cover; display:block; }

  /* sócios (Estúdio) */
  .partner-feature{ display:grid; grid-template-columns:1fr 1fr; gap:56px; align-items:center; padding:70px 0 40px; }
  .partner-portrait{ aspect-ratio:4/5; overflow:hidden; border-radius:2px; width:100%; max-width:440px; }
  .partner-portrait img{ width:100%; height:100%; object-fit:cover; display:block; }
  .partner-text .pubs{ margin-top:26px; padding-top:18px; border-top:1px solid var(--line-dark); font-family:'IBM Plex Mono',monospace; font-size:10.5px; letter-spacing:0.12em; text-transform:uppercase; color:var(--taupe); }
  .partner-bio h2{ font-size:clamp(24px,2.8vw,34px); color:var(--dark-ink); max-width:16ch; }
  .partner-text p{ font-size:16px; line-height:1.85; color:#d8d2c6; max-width:56ch; }
  .partner-text p + p{ margin-top:16px; }
  .partner-secondary{ display:grid; grid-template-columns:0.4fr 1.6fr; gap:44px; align-items:center; padding:30px 0 70px; border-top:1px solid var(--line-dark); margin-top:20px; }
  .partner-portrait.sm{ aspect-ratio:4/5; max-width:280px; }
  .partner-feature.reverse{ border-top:1px solid var(--line-dark); padding-top:56px; }
  .partner-feature.reverse .partner-bio{ order:1; }
  .partner-feature.reverse .partner-portrait{ order:2; margin-left:auto; }

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
  .band .band-text h2 em{ color:var(--brass-soft); font-style:italic; }

  /* services */
  .services{ background:var(--paper); color:var(--paper-ink); padding:120px 0; }
  .services .eyebrow{ margin-bottom:44px; }
  .service-row{ display:grid; grid-template-columns:1fr 2fr; gap:32px; padding:34px 0; border-top:1px solid var(--line-paper); align-items:baseline; }
  .service-row:last-child{ border-bottom:1px solid var(--line-paper); }
  .service-row h3{ font-size:24px; font-style:italic; }
  .service-row p{ font-size:15px; line-height:1.8; color:#4a463d; max-width:52ch; }


  /* servicos - grade de icones */
  .svc-grid{ display:grid; grid-template-columns:repeat(6,1fr); border-top:1px solid var(--line-paper); border-left:1px solid var(--line-paper); }
  .svc-card{ grid-column:span 2; padding:52px 34px; border-right:1px solid var(--line-paper); border-bottom:1px solid var(--line-paper); text-align:center; transition:background .3s ease; }
  .svc-card:hover{ background:rgba(182,126,87,0.05); }
  .svc-card .ico{ width:34px; height:34px; margin:0 auto 22px; display:block; }
  .svc-card .ico path, .svc-card .ico line, .svc-card .ico rect, .svc-card .ico circle, .svc-card .ico polyline{ fill:none; stroke:var(--brass); stroke-width:1.1; stroke-linecap:round; stroke-linejoin:round; }
  .svc-card h3{ font-family:'IBM Plex Mono',monospace; font-size:11px; font-weight:500; letter-spacing:0.16em; text-transform:uppercase; color:var(--paper-ink); }
  .svc-card p{ margin-top:14px; font-size:13.5px; line-height:1.75; color:#4a463d; max-width:32ch; margin-left:auto; margin-right:auto; }
  .svc-wide{ grid-column:span 3; }
  .svc-half{ grid-column:span 3; }

  /* processo */
  .proc{ background:var(--bg); padding:110px 0; }
  .proc .eyebrow{ margin-bottom:14px; }
  .proc h2{ font-size:clamp(26px,3.4vw,38px); color:var(--dark-ink); max-width:18ch; }
  .proc-steps{ margin-top:56px; border-top:1px solid var(--line-dark); }
  .proc-step{ display:grid; grid-template-columns:90px 1fr; gap:28px; padding:34px 0; border-bottom:1px solid var(--line-dark); align-items:baseline; }
  .proc-step .n{ font-family:'IBM Plex Mono',monospace; font-size:13px; letter-spacing:0.14em; color:var(--brass); }
  .proc-step h3{ font-size:21px; font-style:italic; color:var(--dark-ink); }
  .proc-step p{ margin-top:10px; font-size:14.5px; line-height:1.8; color:var(--taupe); max-width:62ch; }
  .proc-360{ margin-top:56px; border:1px solid var(--brass); border-radius:2px; padding:40px 36px; display:grid; grid-template-columns:auto 1fr; gap:28px; align-items:center; }
  .proc-360 svg{ width:44px; height:44px; }
  .proc-360 svg path, .proc-360 svg circle, .proc-360 svg ellipse{ fill:none; stroke:var(--brass-soft); stroke-width:1.2; stroke-linecap:round; }
  .proc-360 h3{ font-size:20px; font-style:italic; color:var(--dark-ink); }
  .proc-360 p{ margin-top:8px; font-size:14.5px; line-height:1.75; color:#d8d2c6; max-width:60ch; }

  /* contato */
  .contact-grid{ display:grid; grid-template-columns:1fr 1fr; gap:64px; align-items:start; padding:70px 0 20px; }
  .contact-info h1{ font-size:clamp(30px,4vw,46px); line-height:1.15; }
  .contact-info h1 em{ font-style:italic; color:var(--brass-soft); }
  .contact-info .lede{ margin-top:20px; font-size:15.5px; line-height:1.8; color:#d8d2c6; max-width:42ch; }
  .contact-list{ margin-top:40px; display:grid; gap:20px; }
  .contact-item{ display:flex; align-items:flex-start; gap:16px; }
  .contact-item .ico{ width:19px; height:19px; flex:0 0 19px; margin-top:2px; }
  .contact-item .ico path, .contact-item .ico circle, .contact-item .ico rect{ fill:none; stroke:var(--brass-soft); stroke-width:1.2; stroke-linecap:round; stroke-linejoin:round; }
  .contact-item .k{ font-family:'IBM Plex Mono',monospace; font-size:9.5px; letter-spacing:0.16em; text-transform:uppercase; color:var(--taupe); }
  .contact-item .v{ margin-top:4px; font-size:15px; color:var(--dark-ink); line-height:1.55; }
  .contact-item a.v:hover{ color:var(--brass-soft); }
  .contact-cta{ margin-top:42px; }
  .contact-photo{ aspect-ratio:4/5; overflow:hidden; border-radius:2px; }
  .contact-photo img{ width:100%; height:100%; object-fit:cover; }
  .map-wrap{ height:380px; background:#e9e5dd; position:relative; overflow:hidden; border-top:1px solid var(--line-dark); }
  .map-wrap iframe{ width:100%; height:100%; border:0; filter:grayscale(0.35) contrast(1.02); }
  .map-note{ position:absolute; inset:0; display:flex; align-items:center; justify-content:center; text-align:center; padding:24px; }
  .map-note span{ font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:0.14em; text-transform:uppercase; color:var(--taupe); border:1px dashed var(--line-dark); padding:14px 22px; }
  .hours{ border-top:1px solid var(--line-dark); padding:44px 0 0; margin-top:56px; display:grid; grid-template-columns:repeat(3,1fr); gap:30px; }
  .hours .k{ font-family:'IBM Plex Mono',monospace; font-size:9.5px; letter-spacing:0.16em; text-transform:uppercase; color:var(--taupe); }
  .hours .v{ margin-top:8px; font-size:14.5px; color:#d8d2c6; line-height:1.6; }

  /* closing */
  .closing{ background:var(--bg); padding:150px 0; text-align:center; }
  .closing.has-bg{ position:relative; overflow:hidden; }
  .closing.has-bg > img{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; }
  .closing.has-bg::after{ content:""; position:absolute; inset:0; background:linear-gradient(to bottom, rgba(15,14,10,0.78), rgba(15,14,10,0.88)); z-index:1; }
  .closing.has-bg .wrap{ position:relative; z-index:2; }
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
  .gallery-hero{ margin-top:46px; height:66vh; min-height:400px; overflow:hidden; position:relative; }
  .gallery-hero img{ width:100%; height:100%; object-fit:cover; }
  .gallery-hero::after{ content:""; position:absolute; left:0; right:0; bottom:0; height:32%; background:linear-gradient(to top, rgba(15,14,10,0.5) 0%, rgba(15,14,10,0) 100%); z-index:1; pointer-events:none; }
  .hero-sign{ position:absolute; z-index:2; left:0; right:0; bottom:20px; display:flex; align-items:center; justify-content:center; gap:13px; pointer-events:none; }
  .hero-sign .mark{ font-family:'Fraunces',serif; font-size:13px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(242,239,234,0.9); }
  .hero-sign .mark span{ color:var(--brass-soft); }
  .hero-sign .sep{ width:1px; height:12px; background:rgba(242,239,234,0.32); }
  .hero-sign .at{ font-family:'IBM Plex Mono',monospace; font-size:10.5px; letter-spacing:0.06em; color:rgba(242,239,234,0.68); }
  .thumbs{ display:grid; gap:2px; margin-top:2px; }
  .thumbs{ grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); }
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


  /* menu mobile */
  .nav-toggle{ display:none; background:none; border:0; padding:10px; cursor:pointer; z-index:120; position:relative; }
  .nav-toggle span{ display:block; width:24px; height:1.5px; background:var(--dark-ink); margin:5px 0; transition:transform .3s ease, opacity .2s ease; }
  .nav-toggle.open span:nth-child(1){ transform:translateY(6.5px) rotate(45deg); }
  .nav-toggle.open span:nth-child(2){ opacity:0; }
  .nav-toggle.open span:nth-child(3){ transform:translateY(-6.5px) rotate(-45deg); }
  body.nav-open{ overflow:hidden; }
  body.nav-open header{ -webkit-backdrop-filter:none !important; backdrop-filter:none !important; }

  @media (max-width:860px){
    .nav-toggle{ display:block; }
    /* hero em tela pequena: eyebrow legivel, titulo maior, respiro certo */
    .hero{ min-height:92svh; }
    .hero-inner{ padding-top:108px; padding-bottom:7vh; }
    .hero-inner .eyebrow{ font-size:9.5px; letter-spacing:0.12em; line-height:1.6; margin-bottom:16px; max-width:26ch; }
    .hero h1{ font-size:clamp(30px,8.4vw,44px); line-height:1.14; max-width:13ch; }
    .hero .lede{ font-size:14.5px; line-height:1.65; margin-top:18px; max-width:38ch; }
    .hero-actions{ margin-top:26px; gap:14px; }
    .hero-actions .hint{ font-size:10px; }
    .hero-media::after{ background:linear-gradient(to top, rgba(15,14,10,0.94) 0%, rgba(15,14,10,0.62) 45%, rgba(15,14,10,0.34) 100%); }
    .hero-sign{ bottom:14px; gap:9px; }
    .hero-sign .mark{ font-size:11px; letter-spacing:0.13em; }
    .hero-sign .at{ font-size:9px; }
    .hero-sign .sep{ height:10px; }
    .logo-img{ height:36px; }
    header.solid .logo-img{ height:30px; }
    .eyebrow{ letter-spacing:0.13em; }
    nav.primary-nav{
      position:fixed; inset:0; background:rgba(20,19,15,0.985);
      flex-direction:column; justify-content:center; align-items:center; gap:30px;
      transform:translateX(100%); transition:transform .35s cubic-bezier(.4,0,.2,1);
      z-index:110; padding:80px 24px;
    }
    nav.primary-nav.open{ transform:translateX(0); }
    nav.primary-nav a{ font-size:15px; letter-spacing:0.16em; opacity:1; }
    nav.primary-nav .btn-whats{ font-size:12px; padding:14px 26px; margin-top:10px; }
    header.solid{ background:rgba(20,19,15,0.96); }
    .intro .wrap{ grid-template-columns:1fr; gap:40px; }
    .intro.flip .wrap{ grid-template-columns:1fr; }
    .grid2,.grid3{ grid-template-columns:1fr; }
    .band{ height:50vh; }
    .service-row{ grid-template-columns:1fr; gap:10px; }
    .svc-grid{ grid-template-columns:1fr; }
    .svc-wide, .svc-half, .svc-card{ grid-column:span 1; }
    .svc-card{ padding:40px 24px; }
    .contact-grid{ grid-template-columns:1fr; gap:36px; padding-top:40px; }
    .proc-step{ grid-template-columns:1fr; gap:6px; }
    .proc-360{ grid-template-columns:1fr; gap:18px; padding:30px 24px; }
    .contact-photo{ aspect-ratio:4/3; }
    .hours{ grid-template-columns:1fr; gap:22px; }
    .map-wrap{ height:300px; }
    .portfolio-head{ flex-direction:column; align-items:flex-start; }
    .proj-head{ grid-template-columns:1fr; }
    .narrative .wrap{ grid-template-columns:1fr; }
    .thumbs.n3{ grid-template-columns:repeat(2,1fr); }
    .related-card{ grid-template-columns:1fr; }
    .studio-grid{ grid-template-columns:1fr; gap:32px; }
    .partner-feature{ grid-template-columns:1fr; gap:28px; padding:40px 0 30px; }
    .partner-feature.reverse .partner-portrait{ order:1; }
    .partner-feature.reverse .partner-bio{ order:2; }
    .partner-secondary{ grid-template-columns:1fr; gap:24px; }
    .partner-portrait.sm{ max-width:220px; }
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
    <a href="index.html" class="logo"><img src="assets/img/logo.png" alt="Rosa Locks Arquitetura" class="logo-img"></a>
    <button class="nav-toggle" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu-principal"><span></span><span></span><span></span></button>
    <nav class="primary-nav" id="menu-principal">
      {nav('Projetos','projetos.html')}
      {nav('Serviços','servicos.html')}
      {nav('Estúdio','estudio.html')}
      {nav('Contato','contato.html')}
      <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp</a>
    </nav>
  </div>
</header>"""

FOOTER = f"""<footer>
  <div class="wrap">
    <a href="index.html" class="logo"><img src="assets/img/logo.png" alt="Rosa Locks Arquitetura" class="logo-img" loading="lazy"></a>
    <div class="foot-links">
      <a href="projetos.html">Projetos</a>
      <a href="servicos.html">Serviços</a>
      <a href="estudio.html">Estúdio</a>
      <a href="contato.html">Contato</a>
      <a href="{INSTA}" target="_blank" rel="noopener">Instagram</a>
      <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
    </div>
  </div>
</footer>"""

SCROLL_JS = """<script>
  // menu mobile
  (function(){
    var t=document.querySelector('.nav-toggle'), n=document.querySelector('.primary-nav');
    if(!t||!n) return;
    function toggle(force){
      var open = (typeof force==='boolean') ? force : !n.classList.contains('open');
      n.classList.toggle('open', open);
      t.classList.toggle('open', open);
      document.body.classList.toggle('nav-open', open);
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
      t.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    }
    t.addEventListener('click', function(){ toggle(); });
    n.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){ toggle(false); }); });
    document.addEventListener('keydown', function(e){ if(e.key==='Escape') toggle(false); });
    window.addEventListener('resize', function(){ if(window.innerWidth>860) toggle(false); });
  })();
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

SITE = "https://rosalocks.com.br"

PIXEL = """<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '425335903506425');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=425335903506425&ev=PageView&noscript=1"/></noscript>
<!-- End Meta Pixel Code -->"""

SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["ProfessionalService", "LocalBusiness"],
  "@id": "https://rosalocks.com.br/#organizacao",
  "name": "Rosa Locks Arquitetura e Engenharia",
  "alternateName": "Rosa Locks Arquitetura",
  "description": "Escritorio de arquitetura e interiores em Criciuma e no litoral de Santa Catarina. Projetos residenciais autorais, interiores sob medida e regularizacao de imoveis, com projeto em BIM desde o primeiro esboco.",
  "url": "https://rosalocks.com.br",
  "logo": "https://rosalocks.com.br/assets/img/hero.jpg",
  "image": "https://rosalocks.com.br/assets/img/hero.jpg",
  "telephone": "+5548988761429",
  "founder": { "@type": "Person", "name": "Isadora Rosa Luiz" },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua Sao Jose 392, Sala 68, Edificio Mario da Cunha Carneiro, Centro",
    "addressLocality": "Criciuma",
    "addressRegion": "SC",
    "postalCode": "88801-520",
    "addressCountry": "BR"
  },
  "areaServed": [
    { "@type": "City", "name": "Criciuma" },
    { "@type": "City", "name": "Balneario Camboriu" },
    { "@type": "City", "name": "Itapema" },
    { "@type": "AdministrativeArea", "name": "Litoral de Santa Catarina" }
  ],
  "knowsAbout": ["Arquitetura residencial", "Design de interiores", "Regularizacao de imoveis", "Projeto autoral", "BIM"],
  "sameAs": ["https://www.instagram.com/rosalocks.arquitetura"],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Servicos",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Projeto residencial autoral" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Projeto de interiores sob medida" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Regularizacao de imoveis" } }
    ]
  }
}
</script>"""

def page(title, body, current, static=False, extra_js="", desc=None, og_img="hero.jpg", url=""):
    desc = desc or "Rosa Locks Arquitetura e Engenharia. Projetos residenciais e de interiores de alto padrao em Criciuma e no litoral de Santa Catarina."
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{PIXEL}
{SCHEMA}
<title>{title}</title>
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/favicon.png">
<meta name="theme-color" content="#1c1c1c">
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rosa Locks Arquitetura">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{url}">
<meta property="og:image" content="{SITE}/assets/img/{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
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
import glob as _glob

def _imgs(slug):
    """Descobre as imagens do projeto na pasta assets/img (slug-01.jpg, slug-02.jpg, ...)."""
    achadas = sorted(_glob.glob(f"{OUT}/assets/img/{slug}-[0-9][0-9].jpg"))
    return [os.path.basename(a) for a in achadas] or [f"{slug}-01.jpg"]

def _plantas(slug):
    achadas = sorted(_glob.glob(f"{OUT}/assets/img/{slug}-planta-[0-9][0-9].jpg"))
    return [os.path.basename(a) for a in achadas]

_NARR_PADRAO = [
  "[EDITAR] O partido do projeto: o que o terreno e o programa pediram.",
  "[EDITAR] Materialidade, iluminação e como os ambientes se conectam.",
  "Projeto modelado em BIM, compatibilizando estrutura e instalações antes da obra."]

PROJETOS = [
  dict(slug='ar', nome='Residência A+R', tipo='interiores', tipo_label='Interiores', capa='ar-09.jpg', escopo='Projeto de interiores', related='dd', local='Criciúma, SC', area='140 m²', ano='2024', h2='Interiores pensados para serem vividos.', narr=['Cada ambiente foi desenhado para refletir a rotina da família, unindo conforto, funcionalidade e uma linguagem visual única.', 'A marcenaria sob medida organiza os espaços, enquanto materiais naturais, tons neutros e iluminação integrada criam uma atmosfera acolhedora e atemporal.']),
  dict(slug='dd', nome='Residência D+D', tipo='residencial', tipo_label='Residencial', escopo='Projeto completo', related='rg', local='Balneário Camboriú, SC', area='517,26 m²', ano='2026', h2='Arquitetura em níveis, moldada pela topografia.', narr=['Em vez de adaptar o terreno ao projeto, a arquitetura se adapta ao terreno. A implantação acompanha o desnível natural, revelando diferentes perspectivas da paisagem e uma integração contínua entre os ambientes.', 'Grandes aberturas, materiais naturais e espaços generosos criam uma residência contemporânea, onde arquitetura e natureza fazem parte da mesma experiência.']),
  dict(slug='rg', nome='Residência R+G', tipo='residencial', tipo_label='Residencial', escopo='Projeto completo', related='luxi', local='Palhoça, SC', area='450 m²', ano='2025', h2='Arquitetura pensada para viver e receber.', narr=['O projeto valoriza a integração entre os ambientes sociais, criando espaços amplos, iluminados e preparados para reunir a família sem abrir mão da privacidade dos ambientes íntimos.', 'Materiais naturais, iluminação indireta e grandes aberturas reforçam a sensação de aconchego, enquanto a arquitetura contemporânea cria uma casa elegante e acolhedora.']),
  dict(slug='luxi', nome='Residência L+D', tipo='residencial', tipo_label='Residencial', escopo='Projeto completo', related='laguna', local='Jaguaruna, SC', area='520 m²', ano='2024', h2='Arquitetura integrada à paisagem.', narr=['A implantação privilegia a integração entre arquitetura e paisagem, criando ambientes amplos, iluminados e conectados às áreas externas.', 'Concreto aparente, madeira e pedra definem uma linguagem contemporânea e atemporal, reforçada pela vegetação tropical.']),
  dict(slug='laguna', nome='Residência L+G', tipo='residencial', tipo_label='Residencial', escopo='Projeto completo', related='edificio-jl', local='Laguna, SC', area='420 m²', ano='2024', h2='Integração, privacidade e luz natural.', narr=['A residência organiza os ambientes sociais no térreo e preserva a privacidade da área íntima no pavimento superior, favorecendo uma rotina fluida e funcional.', 'Volumes horizontais, madeira, pedra e grandes aberturas aproximam os ambientes internos da área externa e valorizam a iluminação natural.']),
  dict(slug='edificio-jl', nome='Edifício JL', tipo='residencial', tipo_label='Residencial', escopo='Projeto completo', related='kitnet-natal', local='Forquilhinha, SC', area='1.103,37 m²', ano='2023', h2='Verticalidade marcada por ritmo, sombra e vegetação.', narr=['O edifício organiza seus pavimentos de forma a valorizar a fachada urbana, criando uma presença marcante na rua e espaços comerciais bem iluminados.', 'Brises, jardineiras e grandes planos envidraçados controlam a incidência solar, conferem profundidade à fachada e reforçam a identidade contemporânea do conjunto.']),
  dict(slug='kitnet-natal', nome='Kitnet Natal', tipo='interiores', tipo_label='Interiores', capa='kitnet-natal-06.jpg', escopo='Projeto de interiores', related='varanda', local='Criciúma, SC', area='35,56 m²', ano='2022', h2='Cada centímetro pensado para ampliar as possibilidades de uso.', narr=['O layout compacto reúne estar, trabalho e descanso com soluções multifuncionais e aproveitamento vertical.', 'A marcenaria multifuncional, o mezanino metálico e a iluminação pontual transformam um espaço compacto em um ambiente versátil e acolhedor.']),
  dict(slug='varanda', nome='Residencial Varanda', tipo='interiores', tipo_label='Interiores', escopo='Interiores + marcenaria', related='ar', local='Florianópolis, SC', area='224 m²', ano='2025', h2='Interiores desenhados sob medida, do piso à marcenaria.', narr=['A integração entre estar, jantar e varanda orienta o projeto, criando continuidade visual e espaços amplos para o convívio.', 'A continuidade dos revestimentos, a marcenaria sob medida e a iluminação indireta reforçam a sensação de amplitude e valorizam a vista para o exterior.']),
  dict(slug='ezos', nome='Grupo Ezos', tipo='comercial', tipo_label='Comercial', escopo='Arquitetura corporativa', related='saint-bier', local='Criciúma, SC', area='88,23 m²', ano='2023', h2='Identidade corporativa traduzida em espaço.', narr=['A recepção, as áreas de trabalho e os espaços de reunião foram organizados para favorecer produtividade, atendimento e conforto no dia a dia da equipe.', 'Materiais naturais, iluminação linear e a identidade visual da empresa aparecem de forma integrada em todo o ambiente.']),
  dict(slug='saint-bier', nome='Saint Bier', tipo='comercial', tipo_label='Comercial', escopo='Arquitetura comercial', related='tigre', local='Forquilhinha, SC', area='66,55 m²', ano='2022', h2='Arquitetura que convida a permanecer.', narr=['O projeto foi pensado para estimular encontros, tornando a circulação intuitiva e criando diferentes experiências entre o bar, o salão e os espaços de convivência.', 'Madeira, tijolos aparentes, vegetação e iluminação quente criam uma atmosfera acolhedora que reforça a identidade da marca.']),
  dict(slug='tigre', nome='Tigre Sports Bar', tipo='comercial', tipo_label='Comercial', capa='tigre-02.jpg', escopo='Arquitetura comercial', related='ciee', local='Estádio, Criciúma, SC', area='a confirmar', ano='2022', h2='Arquitetura que transforma torcida em experiência.', narr=['O projeto organiza bar, mesas, área de jogos e grandes telas para criar uma experiência dinâmica, onde cada lugar acompanha a emoção da partida.', 'Madeira, iluminação quente e os elementos visuais inspirados no Criciúma E.C. reforçam a identidade do espaço, criando um ambiente acolhedor, vibrante e feito para reunir pessoas.']),
  dict(slug='ciee', nome='CIEE', tipo='comercial', tipo_label='Comercial', escopo='Arquitetura corporativa', related='ezos', local='Criciúma, SC', area='1.172,52 m²', ano='2026', h2='Uma sede preparada para receber pessoas.', narr=['Projetado para o CIEE Santa Catarina, este edifício reúne arquitetura e interiores em uma proposta que valoriza acolhimento, organização e eficiência.', 'Cada ambiente foi pensado para facilitar o dia a dia da instituição, oferecer conforto aos usuários e fortalecer sua presença na cidade por meio de uma arquitetura contemporânea e atemporal.']),
]
for _p in PROJETOS:
    _p["imgs"] = _imgs(_p["slug"])
    _p["plantas"] = _plantas(_p["slug"])
    _capa = _p.get("capa")
    if _capa:
        if _capa in _p["imgs"]:
            _p["imgs"].remove(_capa)
            _p["imgs"].insert(0, _capa)
        else:
            print(f"AVISO: capa '{_capa}' nao existe em assets/img para o projeto '{_p['slug']}'. Fotos encontradas: {_p['imgs']}")

BY = {p["slug"]: p for p in PROJETOS}

def card(p, tall=False):
    cls = "pcard tall" if tall else "pcard"
    return f"""<a class="{cls}" href="projeto-{p['slug']}.html" data-tipo="{p['tipo']}">
      <div class="ph"><img src="assets/img/{p['imgs'][0]}" alt="{p['nome']}" loading="lazy"></div>
      <div class="cap"><h3>{p['nome']}</h3><div class="meta">{p['local']} · {p['tipo_label']}</div></div>
    </a>"""

# =================== HOME ===================
home_cards = "\n".join(card(BY[s]) for s in ["ar","dd","varanda","tigre"])
home_body = f"""
<section class="hero">
  <div class="hero-media"><img src="assets/img/hero.jpg" alt="Residência projetada pela Rosa Locks ao anoitecer"></div>
  <div class="hero-inner">
    <div class="wrap">
      <p class="eyebrow">Rosa Locks Arquitetura · Criciúma &amp; Litoral de SC</p>
      <h1>Cada projeto nasce do <em>terreno</em>, não do catálogo.</h1>
      <p class="lede">Projetamos residências e interiores para quem acredita que uma casa deve ser tão única quanto as pessoas que vivem nela.</p>
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
      <h2>Projeto pensado do zero. Construído com confiança.</h2>
      <div class="intro-body" style="margin-top:22px;">
        <p>Cada família vive de uma forma. Por isso, acreditamos que nenhuma casa deve nascer de uma planta pronta.</p>
        <p>Antes de desenhar espaços, entendemos pessoas. Conhecemos sua rotina, seus desejos e a forma como você quer viver para criar uma arquitetura única, feita para durar.</p>
        <p>Cada decisão é tomada com cuidado para que a obra aconteça com clareza, organização e tranquilidade.</p>
        <p>Não repetimos projetos. Cada terreno, cada família e cada história dão origem a uma arquitetura verdadeiramente autoral.</p>
      </div>
      <div class="intro-signature">Arquiteta Isadora Rosa Luiz<span>Direção criativa e acompanhamento pessoal em todas as etapas do projeto</span></div>
    </div>
    <div class="intro-photo">
      <img src="assets/img/isadora-perfil.jpg" alt="Arquiteta Isadora Rosa, Diretora de Projetos da Rosa Locks" loading="lazy">
    </div>
  </div>
</section>

<section class="portfolio" id="projetos">
  <div class="wrap">
    <div class="portfolio-head">
      <div><p class="eyebrow">Projetos selecionados</p><h2>Um recorte do que já saiu do papel.</h2></div>
      <p>Mais do que projetos concluídos, estes são espaços criados para melhorar a forma como cada cliente vive.</p>
    </div>
    <div class="grid2">
      {home_cards}
    </div>
    <div class="see-all"><a class="btn-whats" style="background:transparent;color:var(--brass-soft);" href="projetos.html">Ver todos os projetos</a></div>
  </div>
</section>

<section class="band">
  <img src="assets/img/atmo-01.jpg" alt="Arquitetura residencial Rosa Locks">
  <div class="band-text"><h2>A boa arquitetura se dissolve no conforto do <em>dia a dia</em>.</h2></div>
</section>

<section class="closing">
  <div class="wrap">
    <h2>O primeiro passo é <em>uma conversa</em>.</h2>
    <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp</a>
  </div>
</section>
"""
open(f"{OUT}/index.html","w",encoding="utf-8").write(page("Rosa Locks Arquitetura | Criciúma &amp; Litoral de SC", home_body, "início", static=False, url="", desc="Escritório de arquitetura autoral em Criciúma e litoral de Santa Catarina. Projetos residenciais, interiores e comerciais assinados pela arquiteta Isadora Rosa."))

# =================== PROJETOS (grid) ===================
grid_cards = "\n".join(card(p) for p in PROJETOS)
projetos_body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Portfólio</p>
    <h1>Projetos</h1>
    <p>Cada projeto nasce de uma história diferente. Nenhum poderia existir em outro lugar.</p>
    <div class="filters">
      <button class="filter-btn active" data-filter="todos">Todos</button>
      <button class="filter-btn" data-filter="residencial">Residencial</button>
      <button class="filter-btn" data-filter="interiores">Interiores</button>
      <button class="filter-btn" data-filter="comercial">Comercial</button>
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
open(f"{OUT}/projetos.html","w",encoding="utf-8").write(page("Projetos | Rosa Locks Arquitetura", projetos_body, "projetos", static=True, extra_js=filter_js, url="projetos.html", desc="Portfólio da Rosa Locks Arquitetura: residências e projetos de interiores de alto padrão em Criciúma e no litoral catarinense."))

# =================== PROJETO (detalhe) x4 ===================
def detail(p):
    rest = p["imgs"][1:]
    ncls = f"n{min(len(rest),3)}" if rest else "n1"
    thumbs = "".join(
        f'<div class="thumb"><img src="assets/img/{im}" alt="{p["nome"]}, imagem {i+2}" loading="lazy" data-full="assets/img/{im}"></div>'
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
<div class="gallery-hero"><img id="mainimg" src="assets/img/{p['imgs'][0]}" alt="{p['nome']}, imagem principal"><div class="hero-sign"><span class="mark">Rosa <span>Locks</span></span><span class="sep"></span><span class="at">@rosalocks.arquitetura</span></div></div>
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
    <h2>Gostou do que viu? <em>Fale conosco</em> e conte o seu projeto.</h2>
    <a class="btn-whats" style="padding:15px 30px;font-size:12px;" href="{WA}" target="_blank" rel="noopener">Iniciar uma conversa</a>
  </div>
</section>
"""
    html = page(f"{p['nome']} | Rosa Locks Arquitetura", body, "projetos", static=True, extra_js=(swap_js if rest else ""), url=f"projeto-{p['slug']}.html", og_img=p['imgs'][0], desc=f"{p['nome']}, projeto {p['tipo_label'].lower()} da Rosa Locks Arquitetura em {p['local']}. {p['h2']}")
    open(f"{OUT}/projeto-{p['slug']}.html","w",encoding="utf-8").write(html)

for p in PROJETOS: detail(p)

# =================== ESTÚDIO ===================
estudio_body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">Quem assina</p>
    <h1>O Estúdio</h1>
    <p>Dois profissionais, uma assinatura: criação autoral e responsabilidade técnica integradas do primeiro estudo à entrega do projeto.</p>
  </div>
</section>

<div class="wrap">
  <div class="partner-feature">
    <div class="partner-portrait">
      <img src="assets/img/isadora.jpg" alt="Arquiteta Isadora Rosa, Diretora de Projetos da Rosa Locks" loading="lazy">
    </div>
    <div class="partner-bio reveal">
      <p class="eyebrow" style="margin-bottom:16px;">Arquiteta Isadora Rosa · Diretora de Projetos · CAU/SC A169029-9</p>
      <h2>A criação nasce, e permanece, dentro do estúdio.</h2>
      <div class="partner-text" style="margin-top:22px;">
        <p>Arquiteta e urbanista formada pela UNESC, com registro CAU/SC A169029-9. Atua no mercado desde 2014 e, em 2021, fundou a Rosa Locks Arquitetura.</p>
        <p>Seu processo de criação parte das pessoas, do terreno e da forma de viver, transformando essas informações em projetos autorais, contemporâneos e atemporais.</p>
        <p>Cada projeto é desenvolvido do primeiro esboço ao executivo, buscando conforto, funcionalidade e soluções que valorizam luz natural, materiais duráveis e uma arquitetura pensada para durar.</p>
        <p>À frente da direção criativa do estúdio, Isadora conduz cada projeto do conceito à definição de acabamentos, acompanhando todas as decisões que dão identidade e personalidade a cada obra.</p>
        <p class="pubs">Publicações · Revista Tribuna de Interiores · 2022 e 2023</p>
      </div>
    </div>
  </div>
</div>

<div class="wrap">
  <div class="partner-feature reverse reveal">
    <div class="partner-bio">
      <p class="eyebrow" style="margin-bottom:16px;">Engenheiro Civil José Locks · Direção Técnica · CREA-SC 168536-8</p>
      <h2>A engenharia que sustenta cada projeto.</h2>
      <div class="partner-text" style="margin-top:22px;">
        <p>Engenheiro civil formado pela UNESC, com registro CREA-SC 168536-8.</p>
        <p>Sua atuação começa antes do primeiro desenho, avaliando a viabilidade técnica do terreno, os parâmetros urbanísticos e as exigências legais que orientam o desenvolvimento do projeto.</p>
        <p>Ao longo de todo o processo, coordena a compatibilização entre arquitetura, estrutura e instalações no modelo BIM, além de conduzir a documentação técnica e as aprovações junto aos órgãos competentes.</p>
        <p>Seu papel é garantir que cada decisão arquitetônica seja executável, reduzindo imprevistos na obra e assegurando que o projeto seja construído exatamente como foi concebido.</p>
      </div>
    </div>
    <div class="partner-portrait">
      <img src="assets/img/jose.jpg" alt="José Locks, Engenheiro Civil da Rosa Locks" loading="lazy">
    </div>
  </div>
</div>

<section class="intro flip" style="margin-top:40px;">
  <div class="wrap">
    <div class="intro-photo">
      <img src="assets/img/isadora-atelier.jpg" alt="Seleção de materiais no atelier Rosa Locks" loading="lazy">
    </div>
    <div>
      <p class="eyebrow">Método</p>
      <h2>Do terreno ao projeto. Do projeto à obra.</h2>
      <div class="intro-body" style="margin-top:22px;">
        <p>Todo projeto começa no terreno: orientação solar, ventos, topografia e o jeito da família viver. A partir daí, o desenho é modelado em BIM, compatibilizando arquitetura, estrutura e instalações antes de qualquer tijolo.</p>
        <p>O resultado é uma obra mais previsível, com menos surpresas no canteiro e uma casa que corresponde exatamente ao que foi projetado.</p>
      </div>
    </div>
  </div>
</section>
<section class="closing has-bg">
  <img src="assets/img/ar-01.jpg" alt="Projeto residencial Rosa Locks" loading="lazy">
  <div class="wrap">
    <h2>Pronto para começar <em>o seu projeto</em>?</h2>
    <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp</a>
  </div>
</section>
"""
open(f"{OUT}/estudio.html","w",encoding="utf-8").write(page("O Estúdio | Rosa Locks Arquitetura", estudio_body, "estúdio", static=True, url="estudio.html", og_img="isadora.jpg", desc="Quem assina a Rosa Locks: a arquiteta Isadora Rosa e o engenheiro civil José Locks. Projeto autoral e responsabilidade técnica no mesmo escritório."))


# =================== SERVIÇOS ===================
SERVICOS = [
  ("Arquitetura residencial",
   "Projetos autorais pensados no terreno, na orientação solar e no jeito da família viver.",
   '<path d="M4 14 L17 4 L30 14"/><path d="M7 12.5 V29 H27 V12.5"/><path d="M14 29 V20 H20 V29"/>'),
  ("Arquitetura comercial",
   "Espaços que fortalecem marcas, melhoram a operação e transformam a experiência de clientes e equipes.",
   '<rect x="5" y="7" width="11" height="22"/><rect x="18" y="13" width="10" height="16"/><path d="M8 12h5M8 17h5M8 22h5M21 18h4M21 23h4"/>'),
  ("Interiores",
   "Ambientes personalizados, com marcenaria, iluminação e especificações pensadas em cada detalhe.",
   '<path d="M4 25v-6a3 3 0 013-3h18a3 3 0 013 3v6"/><path d="M7 16v-4a2 2 0 012-2h12a2 2 0 012 2v4"/><path d="M4 25h24M8 25v3M24 25v3"/>'),
  ("Aprovações e regularização",
   "Documentação técnica conduzida pela nossa equipe, do protocolo ao imóvel regularizado.",
   '<path d="M8 4h12l6 6v22H8z"/><path d="M20 4v6h6"/><path d="M12 18h10M12 23h10M12 28h6"/>'),
  ("Projetos complementares",
   "Estrutural, elétrico e hidrossanitário coordenados junto ao projeto arquitetônico para uma obra sem incompatibilidades.",
   '<path d="M16 4v24"/><path d="M6 28h20"/><path d="M16 8L7 28M16 8l9 20"/><circle cx="16" cy="5" r="2"/>'),

]

def svc_card(nome, desc, ico, wide=False):
    cls = "svc-card svc-wide" if wide else "svc-card"
    return f'''<div class="{cls}">
      <svg class="ico" viewBox="0 0 32 32" aria-hidden="true">{ico}</svg>
      <h3>{nome}</h3>
      <p>{desc}</p>
    </div>'''

svc_cards = "\n".join(svc_card(n,d,i) for n,d,i in SERVICOS[:3])
svc_cards += "\n" + "\n".join(svc_card(n,d,i).replace('class="svc-card"','class="svc-card svc-half"') for n,d,i in SERVICOS[3:])

servicos_body = f"""
<section class="services" style="padding-top:150px;">
  <div class="wrap">
    <div style="text-align:center; max-width:620px; margin:0 auto 56px;">
      <p class="eyebrow">Serviços</p>
      <h1 style="font-size:clamp(30px,4vw,46px); margin-top:14px;">Do estudo do terreno ao <em style="font-style:italic;color:var(--brass);">projeto executivo</em>.</h1>
      <p style="margin-top:18px; font-size:15px; line-height:1.8; color:#4a463d;">Arquitetura e engenharia na mesma equipe, para que o projeto chegue à obra sem lacunas. A execução fica com a construtora de sua confiança.</p>
    </div>
    <div class="svc-grid">
      {svc_cards}
    </div>
  </div>
</section>

<section class="proc">
  <div class="wrap">
    <p class="eyebrow">Como funciona</p>
    <h2>Um caminho claro, do primeiro encontro ao projeto pronto.</h2>
    <p style="margin-top:16px; max-width:56ch; font-size:15px; line-height:1.75; color:#c9c3b8;">Todos os projetos são desenvolvidos em BIM, compatibilizados com engenharia e apresentados de forma imersiva antes da obra começar.</p>
    <div class="proc-steps">
      <div class="proc-step">
        <span class="n">01</span>
        <div>
          <h3>Essência</h3>
          <p>Briefing aprofundado, referências e moodboard, medições no local e estudo do terreno. Antes de desenhar, entendemos como vocês vivem.</p>
        </div>
      </div>
      <div class="proc-step">
        <span class="n">02</span>
        <div>
          <h3>Concepção</h3>
          <p>Definição de escopo e conceito arquitetônico, apresentados de forma imersiva até a aprovação do anteprojeto.</p>
        </div>
      </div>
      <div class="proc-step">
        <span class="n">03</span>
        <div>
          <h3>Projeto legal</h3>
          <p>Nossa equipe conduz toda a documentação e o relacionamento com os órgãos competentes.</p>
        </div>
      </div>
      <div class="proc-step">
        <span class="n">04</span>
        <div>
          <h3>Executivo</h3>
          <p>O conjunto de documentos que orienta cada etapa da execução da obra.</p>
        </div>
      </div>
    </div>
    <div class="proc-360">
      <svg viewBox="0 0 48 48" aria-hidden="true"><ellipse cx="24" cy="24" rx="19" ry="8"/><circle cx="24" cy="24" r="6"/><path d="M40 30c2 1.6 2.4 3 1 4.4M8 30c-2 1.6-2.4 3-1 4.4"/></svg>
      <div>
        <h3>Tour 360 antes de aprovar</h3>
        <p>Uma das etapas mais valorizadas pelos clientes, porque permite viver o projeto antes da obra começar.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <img src="assets/img/fd-02.jpg" alt="Projeto residencial Rosa Locks">
  <div class="band-text" style="max-width:30ch;">
    <h2>Tecnologia <em>BIM</em> do início ao projeto executivo.</h2>
    <p style="margin-top:18px; font-size:15px; line-height:1.75; color:#d8d2c6;">Estrutura e instalações compatibilizadas ainda no projeto, reduzindo imprevistos, retrabalhos e custos durante a execução.</p>
  </div>
</section>

<section class="closing">
  <div class="wrap">
    <h2>Qual desses o <em>seu projeto</em> precisa?</h2>
    <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp</a>
  </div>
</section>
"""
open(f"{OUT}/servicos.html","w",encoding="utf-8").write(page("Serviços | Rosa Locks Arquitetura", servicos_body, "serviços", static=True, url="servicos.html", desc="Arquitetura residencial e comercial, interiores, aprovações e regularização, e coordenação de projetos complementares em Criciúma e litoral de SC."))

# =================== CONTATO ===================
ICO_PIN = '<path d="M10 8.5c0 4.5-6 10-6 10s-6-5.5-6-10a6 6 0 1112 0z" transform="translate(6 0)"/><circle cx="10" cy="8.5" r="2.2"/>'
ICO_WHATS = '<path d="M3 17l1.2-4A7 7 0 1110 17z"/><path d="M7 9.5c.6 1.8 1.7 2.9 3.5 3.5"/>'
ICO_MAIL = '<rect x="2" y="4" width="16" height="12" rx="1.5"/><path d="M2.5 5l7.5 6 7.5-6"/>'
ICO_IG = '<rect x="3" y="3" width="14" height="14" rx="4"/><circle cx="10" cy="10" r="3.4"/><circle cx="14.2" cy="5.8" r="0.9"/>'

contato_body = f"""
<section style="padding-top:120px;">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-info">
        <p class="eyebrow" style="margin-bottom:18px;">Contato</p>
        <h1>Vamos conversar sobre <em>o seu projeto</em>.</h1>
        <p class="lede">Será um prazer entender sua ideia e transformá-la em um projeto único. O caminho mais rápido é o WhatsApp: respondemos em poucos minutos no horário comercial.</p>

        <div class="contact-list">
          <div class="contact-item">
            <svg class="ico" viewBox="0 0 20 20" aria-hidden="true">{ICO_WHATS}</svg>
            <div><div class="k">WhatsApp</div><a class="v" href="{WA}" target="_blank" rel="noopener">(48) 9 8876-1429</a></div>
          </div>
          <div class="contact-item">
            <svg class="ico" viewBox="0 0 20 20" aria-hidden="true">{ICO_MAIL}</svg>
            <div><div class="k">E-mail</div><a class="v" href="mailto:contato@rosalocks.com.br">contato@rosalocks.com.br</a></div>
          </div>
          <div class="contact-item">
            <svg class="ico" viewBox="0 0 20 20" aria-hidden="true">{ICO_PIN}</svg>
            <div><div class="k">Escritório</div><a class="v" href="https://maps.google.com/?cid=10516080442723537507" target="_blank" rel="noopener">Rua São José, 392 · Sala 68<br>Centro · Criciúma / SC · 88801-520</a></div>
          </div>
          <div class="contact-item">
            <svg class="ico" viewBox="0 0 20 20" aria-hidden="true">{ICO_IG}</svg>
            <div><div class="k">Instagram</div><a class="v" href="{INSTA}" target="_blank" rel="noopener">@rosalocks.arquitetura</a></div>
          </div>
        </div>

        <div class="contact-cta">
          <a class="btn-whats" style="padding:15px 30px;font-size:12px;" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp agora</a>
        </div>

        <div class="hours">
          <div><div class="k">Atendimento</div><div class="v">Segunda a sexta-feira<br>09h às 12h · 13h30 às 18h</div></div>
          <div><div class="k">Reuniões</div><div class="v">Presenciais ou<br>por videoconferência</div></div>
          <div><div class="k">Atuação</div><div class="v">Criciúma, região<br>e litoral de SC</div></div>
        </div>
      </div>

      <div class="contact-photo">
        <img src="assets/img/varanda-03.jpg" alt="Interiores projetados pela Rosa Locks">
      </div>
    </div>
  </div>
</section>

<div class="map-wrap">
  <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5788.561159907763!2d-49.3713042!3d-28.675158200000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x952183cb99c3abc9%3A0x91f0275624181263!2sRosa%20Locks%20-%20Arquitetura%20autoral%20de%20alto%20padr%C3%A3o!5e1!3m2!1spt-BR!2sbr!4v1785327661408!5m2!1spt-BR!2sbr" title="Localização do escritório Rosa Locks Arquitetura" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
</div>

<section class="closing wood">
  <div class="wrap">
    <h2>O primeiro passo é <em>uma conversa</em>.</h2>
    <a class="btn-whats" href="{WA}" target="_blank" rel="noopener">Iniciar no WhatsApp</a>
  </div>
</section>
"""
open(f"{OUT}/contato.html","w",encoding="utf-8").write(page("Contato | Rosa Locks Arquitetura", contato_body, "contato", static=True, url="contato.html", og_img="rg-01.jpg", desc="Fale com a Rosa Locks Arquitetura. Atendimento por WhatsApp e escritório na Rua São José, 392, Centro, Criciúma, SC."))

print("OK, páginas geradas:")
for f in sorted(os.listdir(OUT)):
    if f.endswith(".html"): print("  ", f)
