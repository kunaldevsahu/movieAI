import requests
import random
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-rec-466x.onrender.com" or "http://127.0.0.1:8000"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    page_title="MovieAI — Cinematic Discovery",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =============================
# PREMIUM CSS
# =============================
st.markdown(
    """
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── CSS Tokens ── */
:root {
  --bg:         #080812;
  --bg2:        #0d0d1f;
  --card:       rgba(255,255,255,0.04);
  --border:     rgba(255,255,255,0.07);
  --border-hov: rgba(108,92,231,0.5);
  --purple:     #6C5CE7;
  --purple-dim: #4a3eb0;
  --cyan:       #00CEC9;
  --white:      #f0eeff;
  --muted:      rgba(240,238,255,0.45);
  --gold:       #ffd700;
  --red:        #ff4d6d;
  --ff-head:    'Bebas Neue', sans-serif;
  --ff-ui:      'Syne', sans-serif;
  --ff-body:    'DM Sans', sans-serif;
  --ease:       cubic-bezier(.22,.68,0,1.2);
}

/* ── Global Reset ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
  background: var(--bg) !important;
  color: var(--white) !important;
  font-family: var(--ff-body) !important;
}

/* Grain overlay */
.stApp::before {
  content: '';
  position: fixed; inset: 0; pointer-events: none; z-index: 9999;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
  opacity: 0.022;
}

/* ── Wipe out Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden !important; }
.stDeployButton { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
.block-container {
  padding: 0 !important;
  max-width: 100% !important;
}
section.main > div { padding: 0 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--purple-dim); border-radius: 99px; }

/* ══════════════════════════════════
   NAVBAR
══════════════════════════════════ */
.mai-navbar {
  position: sticky; top: 0; z-index: 200;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 5%;
  height: 68px;
  background: rgba(8,8,18,0.92);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  box-shadow: 0 4px 30px rgba(0,0,0,0.4);
}
.mai-logo {
  font-family: var(--ff-head);
  font-size: 1.9rem;
  letter-spacing: 3px;
  background: linear-gradient(135deg, var(--purple) 0%, var(--cyan) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  user-select: none;
}
.mai-nav-links {
  display: flex; gap: 2.5rem;
  font-family: var(--ff-ui); font-size: 0.75rem; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
}
.mai-nav-links a {
  color: var(--muted);
  text-decoration: none;
  transition: color 0.2s;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}
.mai-nav-links a:hover { color: var(--white); border-bottom-color: var(--cyan); }
.mai-nav-links a.active { color: var(--white); border-bottom-color: var(--purple); }

/* ══════════════════════════════════
   PAGE WRAPPER
══════════════════════════════════ */
.mai-page { padding: 0 5% 4rem; max-width: 1400px; margin: 0 auto; }

/* ══════════════════════════════════
   HERO SECTION
══════════════════════════════════ */
.mai-hero {
  position: relative;
  min-height: 520px;
  border-radius: 0 0 32px 32px;
  overflow: hidden;
  margin-bottom: 3rem;
  display: flex; align-items: flex-end;
}
.mai-hero-bg {
  position: absolute; inset: 0;
  background: linear-gradient(120deg, #0d001a 0%, #0a0a2e 40%, #001a2e 100%);
}
.mai-hero-orb {
  position: absolute; border-radius: 50%;
  filter: blur(80px); pointer-events: none;
}
.mai-hero-orb-1 {
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(108,92,231,0.35) 0%, transparent 70%);
  top: -80px; right: 8%;
  animation: orbFloat 8s ease-in-out infinite alternate;
}
.mai-hero-orb-2 {
  width: 350px; height: 350px;
  background: radial-gradient(circle, rgba(0,206,201,0.2) 0%, transparent 70%);
  bottom: 5%; left: 20%;
  animation: orbFloat 10s ease-in-out infinite alternate-reverse;
}
@keyframes orbFloat {
  from { transform: translate(0,0) scale(1); }
  to   { transform: translate(15px,-25px) scale(1.08); }
}
.mai-hero-poster {
  position: absolute; right: 0; top: 0; bottom: 0; width: 50%;
  opacity: 0;
  transition: opacity 0.8s ease;
}
.mai-hero-poster img {
  width: 100%; height: 100%;
  object-fit: cover;
}
.mai-hero-poster.loaded { opacity: 0.35; }
.mai-hero-overlay {
  position: absolute; inset: 0;
  background:
    linear-gradient(90deg, rgba(8,8,18,1) 0%, rgba(8,8,18,0.85) 35%, rgba(8,8,18,0.2) 70%, rgba(8,8,18,0.05) 100%),
    linear-gradient(0deg, rgba(8,8,18,0.7) 0%, transparent 45%);
}
.mai-hero-content {
  position: relative; z-index: 2;
  padding: 3.5rem 5% 3rem;
  animation: heroUp 0.8s var(--ease) both;
}
@keyframes heroUp {
  from { opacity:0; transform: translateY(30px); }
  to   { opacity:1; transform: translateY(0); }
}
.mai-hero-badge {
  display: inline-flex; align-items: center; gap: 0.4rem;
  background: rgba(108,92,231,0.18);
  border: 1px solid rgba(108,92,231,0.4);
  border-radius: 99px;
  padding: 0.3rem 0.9rem;
  font-family: var(--ff-ui); font-size: 0.68rem; font-weight: 700;
  letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--purple);
  margin-bottom: 1.1rem;
}
.mai-hero-title {
  font-family: var(--ff-head);
  font-size: clamp(2.8rem, 6vw, 5.5rem);
  line-height: 0.95; letter-spacing: 2px;
  margin-bottom: 1rem;
  text-shadow: 0 4px 24px rgba(108,92,231,0.3);
}
.mai-hero-title .grad {
  background: linear-gradient(90deg, var(--purple), var(--cyan));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.mai-hero-meta {
  display: flex; align-items: center; gap: 0.85rem;
  font-family: var(--ff-ui); font-size: 0.78rem; font-weight: 600;
  color: var(--muted); margin-bottom: 0.9rem; flex-wrap: wrap;
}
.mai-hero-meta .gold { color: var(--gold); }
.mai-hero-meta .dot { opacity: 0.3; }
.mai-genre-pill {
  background: rgba(0,206,201,0.1);
  border: 1px solid rgba(0,206,201,0.25);
  border-radius: 99px;
  padding: 0.15rem 0.65rem;
  font-size: 0.67rem; color: var(--cyan);
}
.mai-hero-desc {
  font-size: 0.92rem; line-height: 1.7;
  color: rgba(240,238,255,0.65);
  max-width: 480px; margin-bottom: 1.8rem;
  display: -webkit-box; -webkit-line-clamp: 3;
  -webkit-box-orient: vertical; overflow: hidden;
}
.mai-hero-actions { display: flex; gap: 0.9rem; flex-wrap: wrap; }

/* ══════════════════════════════════
   BUTTONS
══════════════════════════════════ */
.mai-btn {
  display: inline-flex; align-items: center; gap: 0.5rem;
  font-family: var(--ff-ui); font-size: 0.82rem; font-weight: 700;
  letter-spacing: 0.06em;
  padding: 0.75rem 1.8rem;
  border-radius: 99px; border: none; cursor: pointer;
  transition: all 0.25s var(--ease);
  text-decoration: none;
}
.mai-btn-primary {
  background: linear-gradient(135deg, var(--purple) 0%, #8b5cf6 100%);
  color: var(--white);
  box-shadow: 0 4px 20px rgba(108,92,231,0.4);
}
.mai-btn-primary:hover {
  transform: translateY(-2px) scale(1.03);
  box-shadow: 0 8px 28px rgba(108,92,231,0.6);
}
.mai-btn-ghost {
  background: rgba(255,255,255,0.07);
  color: var(--white);
  border: 1px solid rgba(255,255,255,0.14);
  backdrop-filter: blur(8px);
}
.mai-btn-ghost:hover {
  background: rgba(255,255,255,0.13);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

/* ══════════════════════════════════
   SEARCH BAR
══════════════════════════════════ */
.mai-search-wrap {
  padding: 1.5rem 5% 0;
  max-width: 1400px; margin: 0 auto;
}
.mai-search-label {
  font-family: var(--ff-ui); font-size: 0.68rem; font-weight: 700;
  letter-spacing: 0.15em; text-transform: uppercase;
  color: var(--cyan); margin-bottom: 0.5rem;
}
.mai-search-heading {
  font-family: var(--ff-head);
  font-size: clamp(1.5rem, 3vw, 2.2rem);
  letter-spacing: 1px; margin-bottom: 1.2rem;
}

/* Override Streamlit text_input */
.mai-search-wrap .stTextInput > div > div {
  background: rgba(255,255,255,0.05) !important;
  border: 1px solid var(--border) !important;
  border-radius: 50px !important;
  padding: 0.3rem 1.4rem !important;
  transition: all 0.3s var(--ease) !important;
}
.mai-search-wrap .stTextInput > div > div:focus-within {
  border-color: var(--purple) !important;
  background: rgba(108,92,231,0.07) !important;
  box-shadow: 0 0 0 3px rgba(108,92,231,0.12), 0 0 30px rgba(108,92,231,0.15) !important;
}
.mai-search-wrap .stTextInput input {
  font-family: var(--ff-body) !important;
  font-size: 0.95rem !important;
  color: var(--white) !important;
  background: transparent !important;
}
.mai-search-wrap .stTextInput input::placeholder { color: var(--muted) !important; }
.mai-search-wrap .stTextInput label {
  font-family: var(--ff-ui) !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.1em !important;
  color: var(--muted) !important;
  text-transform: uppercase !important;
}

/* Streamlit selectbox override */
.mai-search-wrap .stSelectbox > div > div {
  background: rgba(13,13,31,0.97) !important;
  border: 1px solid var(--border-hov) !important;
  border-radius: 16px !important;
  color: var(--white) !important;
  font-family: var(--ff-body) !important;
}

/* ══════════════════════════════════
   SECTION HEADINGS
══════════════════════════════════ */
.mai-section {
  padding: 0 5%;
  max-width: 1400px;
  margin: 0 auto 2.5rem;
}
.mai-section-header {
  display: flex; align-items: baseline; justify-content: space-between;
  margin-bottom: 1.2rem;
}
.mai-section-title {
  font-family: var(--ff-head);
  font-size: clamp(1.3rem, 2.5vw, 1.8rem);
  letter-spacing: 1px;
}
.mai-section-title .acc { color: var(--cyan); }
.mai-see-all {
  font-family: var(--ff-ui); font-size: 0.7rem; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--purple); cursor: pointer;
}

/* ══════════════════════════════════
   MOVIE CARD
══════════════════════════════════ */
.mai-card-outer {
  position: relative;
  border-radius: 18px;
  overflow: hidden;
  cursor: pointer;
  border: 1px solid var(--border);
  background: var(--card);
  transition: transform 0.3s var(--ease), box-shadow 0.3s var(--ease), border-color 0.3s;
  aspect-ratio: 2/3;
}
.mai-card-outer:hover {
  transform: translateY(-8px) scale(1.04);
  box-shadow: 0 16px 40px rgba(0,0,0,0.55), 0 0 0 1px var(--border-hov), 0 0 28px rgba(108,92,231,0.15);
  border-color: var(--border-hov);
  z-index: 10;
}

/* Poster */
.mai-card-poster {
  width: 100%; height: 100%;
  position: absolute; inset: 0;
  background-size: cover; background-position: center;
  transition: transform 0.4s var(--ease);
}
.mai-card-outer:hover .mai-card-poster { transform: scale(1.07); }

/* Gradient from bottom */
.mai-card-gradient {
  position: absolute; inset: 0;
  background: linear-gradient(0deg, rgba(8,8,18,0.97) 0%, rgba(8,8,18,0.3) 55%, transparent 80%);
  pointer-events: none;
}

/* Rating badge */
.mai-card-rating {
  position: absolute; top: 10px; left: 10px;
  background: rgba(0,0,0,0.75);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(255,215,0,0.25);
  border-radius: 99px;
  padding: 0.18rem 0.55rem;
  font-family: var(--ff-ui); font-size: 0.65rem; font-weight: 700;
  color: var(--gold);
  z-index: 3;
}

/* Card content */
.mai-card-body {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 0.7rem 0.8rem 0.85rem;
  z-index: 3;
}
.mai-card-title {
  font-family: var(--ff-ui); font-size: 0.8rem; font-weight: 700;
  color: var(--white);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  margin-bottom: 0.25rem;
}
.mai-card-meta {
  font-size: 0.67rem; color: var(--muted);
  display: flex; align-items: center; gap: 0.4rem;
}
.mai-card-dot {
  width: 4px; height: 4px; border-radius: 50%;
  background: var(--cyan); flex-shrink: 0;
}

/* Hover overlay */
.mai-card-hover {
  position: absolute; inset: 0;
  background: linear-gradient(0deg, rgba(8,8,18,0.97) 0%, rgba(108,92,231,0.08) 100%);
  opacity: 0;
  transition: opacity 0.3s;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 0.6rem; z-index: 5;
  padding: 1rem;
}
.mai-card-outer:hover .mai-card-hover { opacity: 1; }

/* ══════════════════════════════════
   SKELETON SHIMMER
══════════════════════════════════ */
.mai-skeleton {
  background: linear-gradient(90deg,
    rgba(255,255,255,0.04) 25%,
    rgba(255,255,255,0.09) 50%,
    rgba(255,255,255,0.04) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.4s infinite;
  border-radius: 18px;
  aspect-ratio: 2/3;
  width: 100%;
}
@keyframes shimmer {
  0%   { background-position: -200% 0; }
  100% { background-position:  200% 0; }
}

/* ══════════════════════════════════
   DETAILS PAGE
══════════════════════════════════ */
.mai-backdrop {
  width: 100%;
  max-height: 360px;
  object-fit: cover;
  border-radius: 0 0 32px 32px;
  display: block;
  margin-bottom: 2rem;
  opacity: 0.7;
  mask-image: linear-gradient(0deg, transparent 0%, rgba(0,0,0,0.9) 30%, black 100%);
  -webkit-mask-image: linear-gradient(0deg, transparent 0%, rgba(0,0,0,0.9) 30%, black 100%);
}
.mai-backdrop-wrap {
  position: relative;
}
.mai-backdrop-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(0deg, var(--bg) 0%, transparent 50%);
  border-radius: 0 0 32px 32px;
}
.mai-details-poster {
  width: 100%;
  border-radius: 18px;
  box-shadow: 0 20px 50px rgba(0,0,0,0.6), 0 0 0 1px var(--border);
  display: block;
}
.mai-details-title {
  font-family: var(--ff-head);
  font-size: clamp(2rem, 5vw, 3.5rem);
  letter-spacing: 2px; line-height: 0.95;
  margin-bottom: 0.9rem;
}
.mai-badge-genre {
  display: inline-flex; align-items: center;
  background: rgba(0,206,201,0.1);
  border: 1px solid rgba(0,206,201,0.3);
  border-radius: 99px;
  padding: 0.2rem 0.75rem;
  font-family: var(--ff-ui); font-size: 0.68rem; font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--cyan);
  margin-right: 0.4rem; margin-bottom: 0.4rem;
}
.mai-rating-badge {
  display: inline-flex; align-items: center; gap: 0.3rem;
  background: rgba(255,215,0,0.1);
  border: 1px solid rgba(255,215,0,0.3);
  border-radius: 99px;
  padding: 0.25rem 0.85rem;
  font-family: var(--ff-ui); font-size: 0.75rem; font-weight: 700;
  color: var(--gold);
  margin-bottom: 1rem;
}
.mai-overview-label {
  font-family: var(--ff-ui); font-size: 0.68rem; font-weight: 700;
  letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--purple); margin-bottom: 0.5rem;
}
.mai-overview-text {
  font-size: 0.9rem; line-height: 1.75;
  color: rgba(240,238,255,0.7);
}
.mai-meta-pill {
  display: inline-flex; align-items: center; gap: 0.3rem;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.3rem 0.75rem;
  font-family: var(--ff-ui); font-size: 0.72rem;
  color: var(--muted);
  margin-right: 0.5rem; margin-bottom: 0.5rem;
}

/* ══════════════════════════════════
   GLASS CARD (info panels)
══════════════════════════════════ */
.mai-glass {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 1.5rem;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

/* ══════════════════════════════════
   BACK BUTTON
══════════════════════════════════ */
.mai-back-wrap { padding: 1rem 5% 0.5rem; max-width: 1400px; margin: 0 auto; }
.mai-back-btn {
  display: inline-flex; align-items: center; gap: 0.5rem;
  background: rgba(255,255,255,0.06);
  border: 1px solid var(--border);
  border-radius: 99px;
  padding: 0.5rem 1.1rem;
  font-family: var(--ff-ui); font-size: 0.72rem; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--muted); cursor: pointer;
  transition: all 0.2s;
}
.mai-back-btn:hover {
  background: rgba(108,92,231,0.15);
  border-color: var(--purple); color: var(--white);
}

/* ══════════════════════════════════
   STREAMLIT COMPONENT OVERRIDES
══════════════════════════════════ */
/* All Streamlit buttons → gradient pill */
.stButton > button {
  background: linear-gradient(135deg, var(--purple) 0%, #8b5cf6 100%) !important;
  color: var(--white) !important;
  border: none !important;
  border-radius: 99px !important;
  font-family: var(--ff-ui) !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.07em !important;
  padding: 0.5rem 1.4rem !important;
  transition: all 0.25s var(--ease) !important;
  box-shadow: 0 4px 16px rgba(108,92,231,0.35) !important;
  text-transform: uppercase !important;
}
.stButton > button:hover {
  transform: translateY(-2px) scale(1.03) !important;
  box-shadow: 0 8px 24px rgba(108,92,231,0.55) !important;
}
.stButton > button:active { transform: scale(0.97) !important; }

/* Dividers */
hr {
  border: none !important;
  border-top: 1px solid var(--border) !important;
  margin: 1.5rem 0 !important;
}

/* Spinner */
.stSpinner > div { border-top-color: var(--purple) !important; }

/* Info/warning boxes */
.stAlert {
  background: rgba(108,92,231,0.1) !important;
  border: 1px solid rgba(108,92,231,0.3) !important;
  border-radius: 14px !important;
  color: var(--white) !important;
}

/* Images */
.stImage img {
  border-radius: 14px !important;
}

/* Selectbox */
.stSelectbox [data-baseweb="select"] > div {
  background: rgba(13,13,31,0.97) !important;
  border-color: var(--border) !important;
  border-radius: 14px !important;
  color: var(--white) !important;
  font-family: var(--ff-body) !important;
}
.stSelectbox [data-baseweb="select"] > div:focus-within {
  border-color: var(--purple) !important;
  box-shadow: 0 0 0 3px rgba(108,92,231,0.15) !important;
}

/* Text inputs globally */
.stTextInput > div > div {
  background: rgba(255,255,255,0.05) !important;
  border-color: var(--border) !important;
  border-radius: 50px !important;
  color: var(--white) !important;
  font-family: var(--ff-body) !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--purple) !important;
  box-shadow: 0 0 0 3px rgba(108,92,231,0.12) !important;
}
.stTextInput input { color: var(--white) !important; }
.stTextInput input::placeholder { color: var(--muted) !important; }
.stTextInput label {
  color: var(--muted) !important;
  font-family: var(--ff-ui) !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
}

/* Markdown text */
.stMarkdown p, .stMarkdown li {
  color: rgba(240,238,255,0.75) !important;
  font-family: var(--ff-body) !important;
}
h1, h2, h3, h4 {
  font-family: var(--ff-ui) !important;
  color: var(--white) !important;
}

/* Caption */
.stCaption {
  color: var(--muted) !important;
  font-family: var(--ff-body) !important;
}

/* ══════════════════════════════════
.mai-footer-copyright {
  text-align: center;
  padding: 1.5rem 0;
  font-size: 0.75rem;
  color: var(--muted);
  border-top: 1px solid rgba(255,255,255,0.05);
  margin-top: 2rem;
}

.mai-social-icons {
  display: flex; gap: 0.6rem;
}
.mai-social-icon {
  width: 32px; height: 32px; border-radius: 50%;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--border);
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 0.8rem; color: var(--muted);
  cursor: pointer; transition: all 0.2s;
}
.mai-social-icon:hover {
  background: rgba(108,92,231,0.2);
  border-color: var(--purple); color: var(--white);
}

/* ══════════════════════════════════
   MISC HELPERS
══════════════════════════════════ */
.mai-label {
  font-family: var(--ff-ui); font-size: 0.68rem; font-weight: 700;
  letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--purple); margin-bottom: 0.4rem;
}
.mai-divider {
  height: 1px; background: var(--border);
  margin: 1.2rem 0;
}
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# STATE + ROUTING
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except Exception:
        pass


def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


# =============================
# API HELPERS (unchanged)
# =============================
@st.cache_data(ttl=30)
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}: {r.text[:300]}"
        return r.json(), None
    except Exception as e:
        return None, f"Request failed: {e}"


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append(
                {
                    "tmdb_id": tmdb["tmdb_id"],
                    "title": tmdb.get("title") or x.get("title") or "Untitled",
                    "poster_url": tmdb.get("poster_url"),
                }
            )
    return cards


def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()
    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        raw_items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                }
            )
    elif isinstance(data, list):
        raw_items = []
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": poster_url,
                    "release_date": m.get("release_date", ""),
                }
            )
    else:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
        for x in final_list[:limit]
    ]
    return suggestions, cards


# =============================
# PREMIUM POSTER GRID
# =============================
def poster_grid(cards, cols=6, key_prefix="grid"):
    """Upgraded poster grid with cinematic cards."""
    if not cards:
        st.markdown(
            "<div style='color:var(--muted);font-family:var(--ff-body);padding:2rem 0;text-align:center;'>No movies found.</div>",
            unsafe_allow_html=True,
        )
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols, gap="small")
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1
            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")

            with colset[c]:
                # Skeleton while no poster
                if not poster:
                    st.markdown(
                        f"""
                        <div class="mai-card-outer">
                          <div class="mai-card-gradient"></div>
                          <div style="position:absolute;inset:0;display:flex;align-items:center;
                               justify-content:center;font-size:2rem;background:linear-gradient(135deg,rgba(108,92,231,0.2),rgba(0,206,201,0.1));">🎬</div>
                          <div class="mai-card-body">
                            <div class="mai-card-title">{title}</div>
                          </div>
                          <div class="mai-card-hover">
                            <span style="font-size:0.7rem;color:var(--muted);text-align:center;">{title}</span>
                          </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"""
                        <div class="mai-card-outer">
                          <div class="mai-card-poster" style="background-image:url('{poster}');"></div>
                          <div class="mai-card-gradient"></div>
                          <div class="mai-card-body">
                            <div class="mai-card-title">{title}</div>
                          </div>
                          <div class="mai-card-hover">
                          </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                # Actual clickable Streamlit button (hidden visual, functional)
                if tmdb_id:
                    if st.button("Open", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}",
                                 help=f"Open {title}", use_container_width=True):
                        goto_details(tmdb_id)


# =============================
# SKELETON LOADER
# =============================
def skeleton_grid(cols=6, count=12):
    rows = (count + cols - 1) // cols
    idx = 0
    for _ in range(rows):
        colset = st.columns(cols, gap="small")
        for c in range(cols):
            if idx >= count:
                break
            idx += 1
            with colset[c]:
                st.markdown('<div class="mai-skeleton"></div>', unsafe_allow_html=True)


# =============================
# NAVBAR
# =============================
def render_navbar(active="home"):
    home_cls = "active" if active == "home" else ""
    st.markdown(
        f"""
        <div class="mai-navbar">
          <div class="mai-logo">🎬 MovieAI</div>
          <div class="mai-nav-links">
            <a href="#" class="{home_cls}">Home</a>
            <a href="#">Explore</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =============================
# HERO SECTION
# =============================
def render_hero(featured: dict | None):
    if not featured:
        # Fallback gradient hero
        st.markdown(
            """
            <div class="mai-hero">
              <div class="mai-hero-bg"></div>
              <div class="mai-hero-orb mai-hero-orb-1"></div>
              <div class="mai-hero-orb mai-hero-orb-2"></div>
              <div class="mai-hero-overlay"></div>
              <div class="mai-hero-content" style="padding:3.5rem 5% 3rem;">
                <div class="mai-hero-badge">✦ AI-Powered Discovery</div>
                <div class="mai-hero-title">DISCOVER YOUR<br><span class="grad">NEXT FILM</span></div>
                <div class="mai-hero-desc">Powered by AI recommendations. Search, explore, and find your perfect movie.</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    title = featured.get("title", "Featured Film")
    overview = featured.get("overview", "")
    poster_url = featured.get("poster_url") or ""
    backdrop_url = featured.get("backdrop_url") or poster_url

    # Truncate overview
    short_desc = (overview[:160] + "...") if len(overview) > 160 else overview

    # Split title for two-line display
    words = title.split()
    half = max(1, len(words) // 2)
    line1 = " ".join(words[:half]).upper()
    line2 = " ".join(words[half:]).upper() if words[half:] else ""

    poster_style = f"background-image:url('{backdrop_url}'); background-size:cover; background-position:center top;" if backdrop_url else ""
    loaded_cls = "loaded" if backdrop_url else ""

    st.markdown(
        f"""
        <div class="mai-hero">
          <div class="mai-hero-bg"></div>
          <div class="mai-hero-orb mai-hero-orb-1"></div>
          <div class="mai-hero-orb mai-hero-orb-2"></div>
          <div class="mai-hero-poster {loaded_cls}" style="{poster_style}"></div>
          <div class="mai-hero-overlay"></div>
          <div class="mai-hero-content">
            <div class="mai-hero-badge">✦ <span style="color:var(--cyan)">AI Pick</span> — Featured Today</div>
            <div class="mai-hero-title">
              {line1}<br><span class="grad">{line2}</span>
            </div>
            <div class="mai-hero-meta">
              <span class="gold">⭐ Top Pick</span>
              <span class="dot">•</span>
              <span>Featured</span>
              <span class="dot">•</span>
              <span class="mai-genre-pill">MovieAI</span>
            </div>
            <div class="mai-hero-desc">{short_desc}</div>
            <div class="mai-hero-actions">
              <button class="mai-btn mai-btn-primary">▶ Play Now</button>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =============================
# SECTION HEADER
# =============================
def section_header(title: str, accent: str, see_all: bool = True):
    see_all_html = '<span class="mai-see-all">See All →</span>' if see_all else ""
    st.markdown(
        f"""
        <div class="mai-section-header">
          <div class="mai-section-title">{title} <span class="acc">{accent}</span></div>
          {see_all_html}
        </div>
        """,
        unsafe_allow_html=True,
    )





# ════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════
def render_footer():
    st.markdown(
        '<div class="mai-footer-copyright">© 2026 MovieAI. All rights reserved.</div>',
        unsafe_allow_html=True,
    )


# ════════════════════════════════════════
# SIDEBAR (hidden visually, kept for logic)
# ════════════════════════════════════════
with st.sidebar:
    st.markdown("## 🎬 MovieAI")
    if st.button("🏠 Home"):
        goto_home()
    st.markdown("---")
    home_category = st.selectbox(
        "Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        index=0,
    )
    grid_cols = st.slider("Grid columns", 4, 8, 6)


# ════════════════════════════════════════
# VIEW: HOME
# ════════════════════════════════════════
if st.session_state.view == "home":
    render_navbar(active="home")

    # ── Disclaimer Banner ──────────────────────
    st.warning(" **Trained on limited data** — This recommendation system is trained on limited  sample data. Results may not be accurate. Please use for demonstration purposes only.", icon="⚠️")

    # ── System Description ──────────────────────
    st.markdown(
        """
        <div style='margin: 2.5rem 0 2rem 0;'>
          <div style='font-family: var(--ff-ui); font-size: 0.72rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: var(--cyan); margin-bottom: 0.8rem;'>
            🤖 INTELLIGENT MOVIE DISCOVERY
          </div>
          <h1 style='font-family: var(--ff-head); font-size: 3rem; letter-spacing: 2px; line-height: 1.1; margin-bottom: 0.8rem;'>
            Your Personal<br><span style='background: linear-gradient(90deg, var(--purple) 0%, var(--cyan) 60%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;'>Movie Guide</span>
          </h1>
          <p style='font-size: 1rem; color: rgba(240,238,255,0.65); max-width: 650px; line-height: 1.7; margin-bottom: 0;'>
            Discover movies tailored to your taste using AI-powered recommendations. Search any title, explore by genre, and find your next favorite film with precision matching and personalized suggestions.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Search Bar ──────────────────────
    st.markdown(
        """
        <div class="mai-search-wrap">
          <div class="mai-search-label">🔍 Start Your Journey</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        col_search, _ = st.columns([2, 1])
        with col_search:
            typed = st.text_input(
                "Search movies",
                placeholder="🔍  Type a title, genre, or actor...",
                label_visibility="collapsed",
            )

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    # ── SEARCH MODE ──────────────────────
    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Type at least 2 characters for suggestions.")
        else:
            with st.spinner("🔍 Searching..."):
                data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search failed: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(
                    data, typed.strip(), limit=24
                )

                if suggestions:
                    labels = ["— Select a movie —"] + [s[0] for s in suggestions]
                    col_dd, _ = st.columns([2, 1])
                    with col_dd:
                        selected = st.selectbox(
                            "Suggestions",
                            labels,
                            index=0,
                            label_visibility="collapsed",
                        )
                    if selected != "— Select a movie —":
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])
                else:
                    st.info("No suggestions found. Try another keyword.")

                st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
                section_header("Search", f'"{typed}"', see_all=False)
                poster_grid(cards, cols=grid_cols, key_prefix="search_results")

        render_footer()
        st.stop()

    # ── HOME FEED MODE ───────────────────
    with st.spinner("Loading featured content..."):
        home_cards, err = api_get_json(
            "/home", params={"category": home_category, "limit": 24}
        )

    # Hero (featured = first card that has backdrop/poster)
    featured = None
    if home_cards:
        for card in home_cards:
            if card.get("poster_url") or card.get("backdrop_url"):
                # Try to get full details for the hero card
                details, _ = api_get_json(f"/movie/id/{card.get('tmdb_id')}")
                featured = details if details else card
                break
        if not featured:
            featured = home_cards[0] if home_cards else None

    render_hero(featured)

    if err or not home_cards:
        st.error(f"Home feed failed: {err or 'Unknown error'}")
        render_footer()
        st.stop()

    # Section header
    category_display = home_category.replace("_", " ").title()
    section_header("🏠 Home", f"— {category_display}", see_all=False)

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")

    render_footer()


# ════════════════════════════════════════
# VIEW: DETAILS
# ════════════════════════════════════════
elif st.session_state.view == "details":
    render_navbar(active="")

    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    # Back button
    st.markdown('<div class="mai-back-wrap">', unsafe_allow_html=True)
    if st.button("← Back to Home"):
        goto_home()
    st.markdown("</div>", unsafe_allow_html=True)

    # Load details
    with st.spinner("Loading movie details..."):
        data, err = api_get_json(f"/movie/id/{tmdb_id}")
    if err or not data:
        st.error(f"Could not load details: {err or 'Unknown error'}")
        st.stop()

    # ── Backdrop Banner ──────────────────
    if data.get("backdrop_url"):
        st.markdown(
            f"""
            <div class="mai-backdrop-wrap">
              <img class="mai-backdrop" src="{data['backdrop_url']}" alt="backdrop"/>
              <div class="mai-backdrop-overlay"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── 2-Column Details Layout ──────────
    st.markdown('<div class="mai-page">', unsafe_allow_html=True)

    left, right = st.columns([1, 2.4], gap="large")

    with left:
        if data.get("poster_url"):
            st.markdown(
                f'<img class="mai-details-poster" src="{data["poster_url"]}" alt="{data.get("title","")}"/>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div style="aspect-ratio:2/3; background:linear-gradient(135deg,rgba(108,92,231,0.2),rgba(0,206,201,0.1));
                     border-radius:18px; display:flex; align-items:center; justify-content:center; font-size:3rem;">🎬</div>
                """,
                unsafe_allow_html=True,
            )

    with right:
        st.markdown('<div class="mai-glass">', unsafe_allow_html=True)

        # Title
        title_text = data.get("title", "Unknown Title")
        st.markdown(
            f'<div class="mai-details-title">{title_text}</div>',
            unsafe_allow_html=True,
        )

        # Rating
        vote = data.get("vote_average")
        if vote:
            st.markdown(
                f'<div class="mai-rating-badge">⭐ {round(float(vote), 1)} / 10</div>',
                unsafe_allow_html=True,
            )

        # Genres as pills
        genres = data.get("genres", [])
        if genres:
            pills_html = "".join(
                [f'<span class="mai-badge-genre">{g["name"]}</span>' for g in genres]
            )
            st.markdown(
                f'<div style="margin-bottom:0.8rem;">{pills_html}</div>',
                unsafe_allow_html=True,
            )

        # Meta pills
        release = data.get("release_date") or ""
        runtime = data.get("runtime")
        meta_pills = ""
        if release:
            meta_pills += f'<span class="mai-meta-pill">📅 {release[:4]}</span>'
        if runtime:
            hrs, mins = divmod(int(runtime), 60)
            meta_pills += f'<span class="mai-meta-pill">⏱ {hrs}h {mins}m</span>'
        if meta_pills:
            st.markdown(
                f'<div style="margin-bottom:1rem;">{meta_pills}</div>',
                unsafe_allow_html=True,
            )

        st.markdown('<div class="mai-divider"></div>', unsafe_allow_html=True)

        # Overview
        st.markdown('<div class="mai-overview-label">Overview</div>', unsafe_allow_html=True)
        overview = data.get("overview") or "No overview available."
        st.markdown(
            f'<div class="mai-overview-text">{overview}</div>',
            unsafe_allow_html=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── Recommendations ──────────────────
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    section_header("✦ Recommendations", "For You")

    title = (data.get("title") or "").strip()
    if title:
        with st.spinner("Fetching AI recommendations..."):
            bundle, err2 = api_get_json(
                "/movie/search",
                params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
            )

        if not err2 and bundle:
            # TF-IDF section
            tfidf_cards = to_cards_from_tfidf_items(bundle.get("tfidf_recommendations"))
            if tfidf_cards:
                st.markdown(
                    """
                    <div class="mai-label">🔎 Similar Movies (AI / TF-IDF)</div>
                    """,
                    unsafe_allow_html=True,
                )
                poster_grid(tfidf_cards, cols=grid_cols, key_prefix="details_tfidf")

            st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

            # Genre section
            genre_cards = bundle.get("genre_recommendations", [])
            if genre_cards:
                st.markdown(
                    """
                    <div class="mai-label">🎭 More Like This (Genre)</div>
                    """,
                    unsafe_allow_html=True,
                )
                poster_grid(genre_cards, cols=grid_cols, key_prefix="details_genre")

        else:
            st.info("Showing Genre recommendations (fallback).")
            with st.spinner("Loading recommendations..."):
                genre_only, err3 = api_get_json(
                    "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
                )
            if not err3 and genre_only:
                st.markdown(
                    '<div class="mai-label">🎭 Genre Recommendations</div>',
                    unsafe_allow_html=True,
                )
                poster_grid(genre_only, cols=grid_cols, key_prefix="details_genre_fallback")
            else:
                st.warning("No recommendations available right now.")
    else:
        st.warning("No title available to compute recommendations.")

    render_footer()