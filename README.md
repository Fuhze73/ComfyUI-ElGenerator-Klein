# ComfyUI-ElGenerator-Klein


![Alt text](https://github.com/Fuhze73/ComfyUI-ElGenerator-Klein/blob/main/image.webp)

**El Generator Klein** — Character and scene editor for **FLUX.2 Klein 9B**  
8 nodes · Natural prose · Photographic realism · Amateur / candid / casual focus

---

## ⚡ What's in ElGenerator-Klein

- **8 nodes** instead of 6 — Face and People are now separate nodes
- **"none" everywhere by default** — nothing is forced, you compose what you want
- **Stackable booleans** — goosebumps, tan lines, film grain etc. are ON/OFF switches you can stack
- **Many more choices** across the board: body type, face, hands, gestures, clothing, underwear, shoes
- **Amateur / candid focus** — selfie, phone camera, disposable, party snapshot, webcam, smartphone casual
- **People node** — add a companion (man, woman, crowd)
- **Detailed wardrobe** — piece by piece (top, bottom, underwear, bra, shoes, legwear)
- **Redesigned NSFW node** — booleans for each body detail, more casual contexts

---

## 📦 Installation

```bash
cd ComfyUI/custom_nodes/
# Copy the folder or:
git clone https://github.com/Fuhze73/ComfyUI-ElGenerator-Klein.git
```

---

## 🧩 The 8 Nodes

### 📸 Klein — Subject
Full physical appearance:
- Gender, Age, Ethnicity (8 + none)
- Height (5 levels), Build (9 options)
- **Female**: bust size + shape (perky, natural sag, heavy sag...), hips, buttocks, belly
- **Male**: musculature (lean → bodybuilder, dad bod), belly, buttocks
- Hair: 19 colors, 9 lengths, 9 textures, 13 styles, 6 bangs
- Eyes: 12 colors
- Skin: 11 details
- **Switches**: dewy skin, oily, goosebumps, tan lines, sweat, body hair, tattoos, piercings

### 😶 Klein — Face
Face and gestures:
- **22 expressions**: neutral → euphoric, shy, drunk, bored, crying, seductive...
- **19 mouths**: tongue out, licking lips, blowing kiss, smoking, drinking, chewing gum, biting lip...
- **19 gazes**: direct at camera, flirty, shy, defiant, winking, rolling eyes, looking at phone, at partner...
- **17 gestures**: peace sign, middle finger, heart hands, selfie arm, finger guns, flexing, prayer hands...

### 👗 Klein — Wardrobe
Clothing piece by piece:
- **Top** (28): t-shirt → corset, bralette, sheer top, bodysuit, flannel...
- **Bottom** (26): skinny jeans → sarong, towel, bodycon dress, sundress...
- **Underwear** (13): full brief, thong, g-string, boy shorts, lace, cotton, cheeky, no underwear...
- **Bra** (7): push-up, bralette, sports bra, sheer, strapless, no bra...
- **Shoes** (17): barefoot → thigh boots, flip-flops, slippers, Converse...
- **Legwear** (8): ankle socks → garter stockings
- **Accessories** (2 slots, 23 choices): sunglasses, AirPods, phone in hand...
- Main color (24), Material (16)

### 🧍 Klein — Pose
Detailed body position:
- **29 positions**: standing, sitting (chair, floor, edge), lying (side, back, stomach), crouching, kneeling, in bathtub, in bed, on couch, in car, in pool...
- **Left hand** (20 separate choices)
- **Right hand** (20 separate choices)
- **Legs** (15 choices)
- Free text field for override

### 🎬 Klein — Scene
Lighting + location + atmosphere + camera + quality:
- **22 lightings**: + phone flash, bathroom light, screen glow, string lights, club lights, car headlights, sunset through blinds...
- **34 locations**: + bathroom mirror, shower, bathtub, kitchen, bar/club, dressing room, elevator, gym, festival, concert, train...
- **21 moods**: + amateur_candid, smartphone_casual, polaroid, social_media, paparazzi, home_video, webcam, party_snapshot
- **11 camera modes**: selfie front, mirror selfie, group selfie, DSLR, film, phone, disposable, webcam, security cam, polaroid, GoPro
- **10 lenses**: + phone_wide
- **11 film renders**: + VSCO filter, lo-fi
- **7 quality levels**: ultra detailed → award winning, 4K, 8K, raw unedited, magazine quality
- **8 FX switches**: film grain, motion blur, lens flare, bokeh, vignette, chromatic aberration, light leaks, noise/grain
- **12 presets**: + candid_street, selfie_bathroom, party_vibes, pool_day, morning_light, home_casual

### 👥 Klein — People
Add people:
- **14 options**: man (casual, intimate, behind, hands only), woman (casual, intimate, friend), couple (kissing, hugging), friend group, crowd, passersby, alone in public

### 🔞 Klein — NSFW
Separate adult node (opt-in):
- **10 levels**: suggestive, cleavage, underboob, sideboob, topless, bottomless, nude, partial nude, implied nude
- **18 contexts**: + morning after, getting dressed, changing room, skinny dipping, sunbathing, bedroom casual, mirror selfie, body paint...
- Pubic hair (6 options)
- **12 body switches**: natural skin, oiled, goosebumps, tan lines, sweaty, wet skin, body hair, athletic detail, soft curves, nipples erect, nipples pierced, belly piercing

### ✏️ Klein — Combine
Final assembly → STRING:
- Optimized Klein order: Subject → NSFW/Wardrobe → Face → Pose → People → Scene
- `extra` field for free text

---

## 🔌 Typical Workflow

```
[Subject] ──→ [Combine] ──prompt──→ [CLIPTextEncode]
[Face]    ──→    ↗
[Wardrobe]──→   ↗
[Pose]    ──→  ↗
[People]  ──→ ↗
[Scene]   ──→↗
```

For NSFW, connect [NSFW] to the `nsfw` input of Combine (replaces/completes Wardrobe).

---

## 📊 Option Counter

| Node | Total Options |
|------|----------------|
| Subject | ~170+ combinations (sliders + switches) |
| Face | 77 choices (expression + mouth + gaze + gesture) |
| Wardrobe | ~160 choices (pieces + colors + materials) |
| Pose | 84 choices (position + hands + legs) |
| Scene | ~150 choices + 8 switches + 12 presets |
| People | 14 options |
| NSFW | ~56 choices + 12 switches |
| **Total** | **~700+ individual options** |

---

*El Generator Klein v2 — by El Randolo*
