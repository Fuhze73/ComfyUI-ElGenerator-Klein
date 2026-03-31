# ComfyUI-ElGenerator-Klein v2

**El Generator Klein v2** — Éditeur de personnage et scène pour **FLUX.2 Klein 9B**  
8 nodes · Prose naturelle · Réalisme photographique · Focus amateur / candid / casual

---

## ⚡ Quoi de neuf en v2

- **8 nodes** au lieu de 6 — Face et People sont des nodes séparés
- **"none" partout par défaut** — rien n'est forcé, tu composes ce que tu veux
- **Booleans empilables** — goosebumps, tan lines, film grain etc. sont des switches ON/OFF qu'on empile
- **Beaucoup plus de choix** sur tout : morphologie, visage, mains, gestuelle, vêtements, sous-vêtements, chaussures
- **Focus amateur / candid** — selfie, phone camera, disposable, party snapshot, webcam, smartphone casual
- **Node People** — ajout de compagnon (homme, femme, foule)
- **Wardrobe détaillée** — pièce par pièce (top, bottom, underwear, bra, shoes, legwear)
- **Node NSFW repensé** — booleans pour chaque détail corporel, plus de contextes casual

---

## 📦 Installation

```bash
cd ComfyUI/custom_nodes/
# Copiez le dossier ou :
git clone https://github.com/Fuhze73/ComfyUI-ElGenerator-Klein.git
```

---

## 🧩 Les 8 nodes

### 📸 Klein — Subject
Apparence physique complète :
- Genre, Âge, Ethnicité (8 + none)
- Taille (5 niveaux), Corpulence (9 options)
- **Femme** : poitrine taille + forme (perky, natural sag, heavy sag...), hanches, fesses, ventre
- **Homme** : musculature (lean → bodybuilder, dad bod), ventre, fesses
- Cheveux : 19 couleurs, 9 longueurs, 9 textures, 13 coiffures, 6 franges
- Yeux : 12 couleurs
- Peau : 11 détails
- **Switches** : peau dewy, oily, goosebumps, tan lines, sueur, body hair, tattoos, piercings

### 😶 Klein — Face
Visage et gestuelle :
- **22 expressions** : neutre → euphoric, shy, drunk, bored, crying, seductive...
- **19 bouches** : tongue out, licking lips, blowing kiss, smoking, drinking, chewing gum, biting lip...
- **19 regards** : camera direct, flirty, shy, defiant, winking, rolling eyes, looking at phone, at partner...
- **17 gestes** : peace sign, middle finger, heart hands, selfie arm, finger guns, flexing, prayer hands...

### 👗 Klein — Wardrobe
Vêtements pièce par pièce :
- **Haut** (28) : t-shirt → corset, bralette, sheer top, bodysuit, flannel...
- **Bas** (26) : skinny jeans → sarong, towel, bodycon dress, sundress...
- **Sous-vêtements** (13) : full brief, thong, g-string, boy shorts, lace, cotton, cheeky, no underwear...
- **Soutien-gorge** (7) : push-up, bralette, sports bra, sheer, strapless, no bra...
- **Chaussures** (17) : barefoot → thigh boots, flip-flops, slippers, Converse...
- **Legwear** (8) : ankle socks → garter stockings
- **Accessoires** (2 slots, 23 choix) : sunglasses, AirPods, phone in hand...
- Couleur principale (24), Matière (16)

### 🧍 Klein — Pose
Position du corps détaillée :
- **29 positions** : debout, assis (chaise, sol, bord), couché (côté, dos, ventre), accroupi, à genoux, dans baignoire, au lit, sur canapé, dans voiture, dans piscine...
- **Main gauche** (20 choix séparés)
- **Main droite** (20 choix séparés)
- **Jambes** (15 choix)
- Champ libre pour override

### 🎬 Klein — Scene
Éclairage + lieu + atmosphère + caméra + qualité :
- **22 éclairages** : + phone flash, bathroom light, screen glow, string lights, club lights, car headlights, sunset through blinds...
- **34 lieux** : + bathroom mirror, shower, bathtub, kitchen, bar/club, dressing room, elevator, gym, festival, concert, train...
- **21 ambiances** : + amateur_candid, smartphone_casual, polaroid, social_media, paparazzi, home_video, webcam, party_snapshot
- **11 modes caméra** : selfie front, mirror selfie, group selfie, DSLR, film, phone, disposable, webcam, security cam, polaroid, GoPro
- **10 objectifs** : + phone_wide
- **11 rendus film** : + VSCO filter, lo-fi
- **7 qualités** : ultra detailed → award winning, 4K, 8K, raw unedited, magazine quality
- **8 switches FX** : film grain, motion blur, lens flare, bokeh, vignette, chromatic aberration, light leaks, noise/grain
- **12 presets** : + candid_street, selfie_bathroom, party_vibes, pool_day, morning_light, home_casual

### 👥 Klein — People
Ajout de personnes :
- **14 options** : homme (casual, intime, derrière, mains seulement), femme (casual, intime, amie), couple (kissing, hugging), groupe d'amis, foule, passants, seul en public

### 🔞 Klein — NSFW
Node adulte séparé (opt-in) :
- **10 niveaux** : suggestive, cleavage, underboob, sideboob, topless, bottomless, nude, partial nude, implied nude
- **18 contextes** : + morning after, getting dressed, changing room, skinny dipping, sunbathing, bedroom casual, mirror selfie, body paint...
- Poils pubiens (6 options)
- **12 switches corporels** : natural skin, oiled, goosebumps, tan lines, sweaty, wet skin, body hair, athletic detail, soft curves, nipples erect, nipples pierced, belly piercing

### ✏️ Klein — Combine
Assemblage final → STRING :
- Ordre optimisé Klein : Subject → NSFW/Wardrobe → Face → Pose → People → Scene
- Champ `extra` pour texte libre

---

## 🔌 Workflow typique

```
[Subject] ──→ [Combine] ──prompt──→ [CLIPTextEncode]
[Face]    ──→    ↗
[Wardrobe]──→   ↗
[Pose]    ──→  ↗
[People]  ──→ ↗
[Scene]   ──→↗
```

Pour le NSFW, branchez [NSFW] sur l'entrée `nsfw` du Combine (remplace/complète Wardrobe).

---

## 📊 Compteur d'options

| Node | Options totales |
|------|----------------|
| Subject | ~170+ combinaisons (sliders + switches) |
| Face | 77 choix (expression + bouche + regard + geste) |
| Wardrobe | ~160 choix (pièces + couleurs + matières) |
| Pose | 84 choix (position + mains + jambes) |
| Scene | ~150 choix + 8 switches + 12 presets |
| People | 14 options |
| NSFW | ~56 choix + 12 switches |
| **Total** | **~700+ options individuelles** |

---

*El Generator Klein v2 — par El Randolo*
