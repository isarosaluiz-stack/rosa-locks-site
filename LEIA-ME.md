# Site Rosa Locks — site estático

Site novo da Rosa Locks, HTML estático (sem WordPress, sem formulário). Todo CTA
aponta direto pro WhatsApp da Vanessa.

## Páginas

| Arquivo | O que é |
|---|---|
| `index.html` | Home — hero full-bleed, Estúdio + croqui animado, portfólio, CTA |
| `projetos.html` | Grid de projetos com filtro (Todos / Residencial / Interiores) |
| `projeto-dd.html` | Casa D+D (4 fotos) — galeria com troca de imagem ao clicar nas miniaturas |
| `projeto-fd.html` | Casa F+D (3 fotos) |
| `projeto-ar.html` | Casa A+R (2 fotos) |
| `projeto-rg.html` | Projeto R+G — Interiores (2 fotos) |
| `estudio.html` | Estúdio — bio da Isadora (placeholder) + método + croqui |
| `assets/img/` | Todas as imagens já otimizadas pra web (6,2 MB no total) |

Os nomes dos projetos (D+D, F+D, A+R, R+G) vieram das iniciais dos arquivos que
você mandou. São placeholders elegantes — troque pelos nomes reais quando quiser.

## O que falta você me passar / editar (busque por `[EDITAR]`)

- **Número da Vanessa (WhatsApp):** hoje está `55XXXXXXXXXXX` em todos os botões.
  Troque em `build.py` (variável `WA`) e rode de novo, OU faça um find/replace por
  `wa.me/55XXXXXXXXXXX` em todos os `.html`.
- **Instagram:** confira o handle em `build.py` (variável `INSTA`).
- **Textos dos projetos:** local, metragem (m²), ano e o "porquê" de cada obra.
  Estão marcados `[EDITAR]` — me conta e eu escrevo o texto final.
- **Estúdio:** bio da Isadora (formação, prêmios/publicações) e, se tiver, uma
  foto dela pra substituir a imagem de projeto que está no lugar.

## Publicar no Coolify (VPS Vultr, ao lado do n8n)

1. No Coolify → **New Resource → Static Site** (ou "Dockerfile"/"Nixpacks" servindo
   a pasta). Aponte pro repositório/pasta que contém estes arquivos com o `index.html`
   na raiz.
2. Domínio: aponte `rosalocks.com.br` (raiz + `www`) pra este serviço. O n8n
   continua no subdomínio que já usa. Confirma o domínio pra eu fechar o roteamento.
3. Não precisa de build step — é HTML puro. Se o Coolify pedir, o "publish directory"
   é a raiz desta pasta.
4. HTTPS: deixe o Coolify emitir o Let's Encrypt automático pro domínio.

> Alternativa sem tocar no Coolify agora: dá pra publicar em Netlify/Cloudflare Pages
> arrastando esta pasta — mas a recomendação segue ser no seu VPS, custo zero e você
> mantém tudo no mesmo lugar.

## Trocar/regerar imagens

As imagens em `assets/img/` já estão otimizadas. Se quiser trocar alguma, mantenha o
mesmo nome de arquivo (ex.: `dd-01.jpg`) ou me mande as novas que eu regenero. Para
capa de projeto use ~1800px de largura; miniaturas ~1200px; JPG qualidade ~82.

## Notas técnicas

- Sem dependências, sem build, sem JS externo além do Google Fonts (CDN).
- Acessibilidade: respeita `prefers-reduced-motion` (desliga animações), foco visível.
- Imagens com `loading="lazy"`. Peso total do site: ~6,4 MB.
