"""
El Generator Klein v2.1 — ComfyUI Custom Nodes
FLUX.2 Klein 9B · Photographic realism · Amateur / Candid / Casual

v2.1 PROSE REWRITE — All generate/build functions rewritten to produce
flowing natural language that Qwen3 8B text encoder parses optimally.

Key principles applied:
  - Write like describing a photograph to someone who can't see it
  - Weave traits into sentences, never comma-list them
  - Each section = 1-2 complete sentences max
  - Subject first (highest priority), style annotations last
  - Lighting described as a photographer would say it out loud
  - No SDXL artifacts: no weight syntax, no quality tags, no booru tokens
"""

import random
from .klein_data import (
    ETHNICITIES, age_prose,
    HEIGHT, BUILD, BUST, BUST_SHAPE, HIPS, BUTT, BELLY, MUSCLE_M, PUBIC_HAIR,
    HAIR_COLORS, HAIR_LENGTHS, HAIR_TEXTURES, HAIR_STYLES, BANGS,
    EYE_COLORS, SKIN_DETAILS,
    EXPRESSIONS, MOUTH, GAZE, GESTURES,
    POSITIONS, LEFT_HAND, RIGHT_HAND, LEGS,
    TOPS, BOTTOMS, UNDERWEAR, BRA, SHOES, LEGWEAR, ACCESSORIES, COLORS, MATERIALS,
    LIGHTINGS, LOCATIONS, ATMOSPHERES,
    FRAMINGS, CAMERA_ANGLES, CAMERA_MODES, LENSES, FILM_STOCKS, QUALITY,
    COMPANIONS,
    NSFW_LEVELS, NSFW_CONTEXTS, SCENE_PRESETS,
    pick,
)

def _keys(d):
    return list(d.keys())

def _clean(text):
    """Clean up prose: fix double periods, orphan commas, trailing spaces."""
    while ".." in text: text = text.replace("..", ".")
    while ". ." in text: text = text.replace(". .", ".")
    while ",," in text: text = text.replace(",,", ",")
    while ", ," in text: text = text.replace(", ,", ",")
    text = text.replace(" ,", ",").replace("  ", " ")
    text = text.strip().strip(",").strip()
    return text


# ═══════════════════════════════════════════════════════════════
# 1. SUBJECT
# ═══════════════════════════════════════════════════════════════
class KleinSubject:
    """Physical body as natural prose."""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            "gender": (["female", "male"],),
            "age": ("INT", {"default": 25, "min": 18, "max": 70}),
            "ethnicity": (_keys(ETHNICITIES),),
            "height": (_keys(HEIGHT),),
            "build": (_keys(BUILD),),
            "bust_size": (_keys(BUST),),
            "bust_shape": (_keys(BUST_SHAPE),),
            "hips": (_keys(HIPS),),
            "butt": (_keys(BUTT),),
            "belly": (_keys(BELLY),),
            "muscle": (_keys(MUSCLE_M),),
            "hair_color": (HAIR_COLORS,),
            "hair_length": (_keys(HAIR_LENGTHS),),
            "hair_texture": (_keys(HAIR_TEXTURES),),
            "hair_style": (_keys(HAIR_STYLES),),
            "bangs": (_keys(BANGS),),
            "eye_color": (EYE_COLORS,),
            "skin_detail": (SKIN_DETAILS,),
            "dewy_skin": ("BOOLEAN", {"default": False, "tooltip": "Luminous dewy skin"}),
            "oily_skin": ("BOOLEAN", {"default": False}),
            "goosebumps": ("BOOLEAN", {"default": False}),
            "tan_lines": ("BOOLEAN", {"default": False}),
            "sweaty": ("BOOLEAN", {"default": False}),
            "body_hair_natural": ("BOOLEAN", {"default": False}),
            "tattoos": ("BOOLEAN", {"default": False}),
            "piercings": ("BOOLEAN", {"default": False}),
        }}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("subject",)
    FUNCTION = "generate"
    CATEGORY = "ElGenerator Klein"

    def generate(self, seed, gender, age, ethnicity, height, build,
                 bust_size, bust_shape, hips, butt, belly, muscle,
                 hair_color, hair_length, hair_texture, hair_style, bangs,
                 eye_color, skin_detail,
                 dewy_skin, oily_skin, goosebumps, tan_lines, sweaty,
                 body_hair_natural, tattoos, piercings):
        rng = random.Random(seed)
        g = "F" if gender == "female" else "M"
        pron = "She" if g == "F" else "He"
        poss = "her" if g == "F" else "his"

        eth = ETHNICITIES.get(ethnicity, ETHNICITIES["none"])

        # ── S1: who + body ──
        intro = age_prose(age, gender)
        feat = eth["features"]
        if feat:
            intro += f" with {feat}"

        body_frags = []
        h = HEIGHT.get(height, "")
        b = BUILD.get(build, "")
        if h and b:
            body_frags.append(f"{h} {b}")
        elif h:
            body_frags.append(h)
        elif b:
            body_frags.append(b)

        if g == "F":
            morph = []
            bust_s = BUST.get(bust_size, "")
            bust_sh = BUST_SHAPE.get(bust_shape, "")
            if bust_s and bust_sh:
                morph.append(f"{bust_sh} and {bust_s}")
            elif bust_s:
                morph.append(bust_s)
            elif bust_sh:
                morph.append(bust_sh)
            hip_v = HIPS.get(hips, "")
            butt_v = BUTT.get(butt, "")
            if hip_v and butt_v:
                morph.append(f"{hip_v} and {butt_v}")
            elif hip_v:
                morph.append(hip_v)
            elif butt_v:
                morph.append(butt_v)
            belly_v = BELLY.get(belly, "")
            if belly_v:
                morph.append(belly_v)
            if morph:
                body_frags.append(", ".join(morph))
        else:
            for val in [MUSCLE_M.get(muscle, ""), BELLY.get(belly, ""), BUTT.get(butt, "")]:
                if val: body_frags.append(val)

        s1 = f"{intro}, {', '.join(body_frags)}" if body_frags else intro

        # ── S2: hair ──
        hl = HAIR_LENGTHS.get(hair_length, "")
        hc = hair_color if hair_color != "none" else ""
        ht = HAIR_TEXTURES.get(hair_texture, "")
        hs = HAIR_STYLES.get(hair_style, "")
        bn = BANGS.get(bangs, "")

        if hl or hc:
            desc = f"{poss} "
            if hc and hl:
                desc += f"{hc} hair in {hl}"
            elif hc:
                desc += f"{hc} hair"
            else:
                desc += f"hair in {hl}"
            if ht: desc += f", {ht}"
            if hs: desc += f", {hs}"
            if bn: desc += f", {bn} framing {poss} face"
            s2 = f"{pron} has {desc}"
        else:
            s2 = ""

        # ── S3: eyes + skin ──
        ec = f"{eye_color} eyes" if eye_color != "none" else ""
        skin = rng.choice(eth["skin"]) if eth.get("skin") else ""
        sd = skin_detail if skin_detail != "none" else ""

        eye_skin = []
        if ec: eye_skin.append(ec)
        if skin: eye_skin.append(skin)

        if eye_skin:
            s3 = f"{pron} has {' and '.join(eye_skin)}"
            if sd: s3 += f", with {sd}"
        elif sd:
            s3 = f"{pron} has {sd}"
        else:
            s3 = ""

        # ── S4: skin switches ──
        switches = []
        if dewy_skin: switches.append("a luminous dewy glow")
        if oily_skin: switches.append("a natural oily sheen")
        if goosebumps: switches.append("visible goosebumps")
        if tan_lines: switches.append("visible tan lines")
        if sweaty: switches.append("a light sheen of sweat")
        if body_hair_natural: switches.append("natural visible body hair")
        if tattoos: switches.append("visible tattoos")
        if piercings: switches.append("piercings")

        if len(switches) == 1:
            s4 = f"{poss.capitalize()} skin shows {switches[0]}"
        elif len(switches) == 2:
            s4 = f"{poss.capitalize()} skin shows {switches[0]} and {switches[1]}"
        elif switches:
            s4 = f"{poss.capitalize()} skin shows {', '.join(switches[:-1])}, and {switches[-1]}"
        else:
            s4 = ""

        return (_clean(". ".join(filter(None, [s1, s2, s3, s4]))),)


# ═══════════════════════════════════════════════════════════════
# 2. FACE
# ═══════════════════════════════════════════════════════════════
class KleinFace:
    """Face as flowing prose."""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "expression": (_keys(EXPRESSIONS),),
            "mouth": (_keys(MOUTH),),
            "gaze": (_keys(GAZE),),
            "gesture": (_keys(GESTURES),),
        }}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("face",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator Klein"

    def build(self, expression, mouth, gaze, gesture):
        expr_v = EXPRESSIONS.get(expression, "")
        mouth_v = MOUTH.get(mouth, "")
        gaze_v = GAZE.get(gaze, "")
        gesture_v = GESTURES.get(gesture, "")

        bits = []
        if expr_v and mouth_v:
            bits.append(f"{expr_v} with {mouth_v}")
        elif expr_v:
            bits.append(expr_v)
        elif mouth_v:
            bits.append(mouth_v)

        if gaze_v:
            bits.append(gaze_v)

        if not bits:
            return (gesture_v if gesture_v else "",)

        face_str = "Her face shows " + bits[0]
        for b in bits[1:]:
            face_str += f", {b}"

        if gesture_v:
            face_str += f", while {gesture_v}"

        return (_clean(face_str),)


# ═══════════════════════════════════════════════════════════════
# 3. WARDROBE
# ═══════════════════════════════════════════════════════════════
class KleinWardrobe:
    """Clothing as natural prose."""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "top": (_keys(TOPS),),
            "bottom": (_keys(BOTTOMS),),
            "underwear": (_keys(UNDERWEAR),),
            "bra": (_keys(BRA),),
            "shoes": (_keys(SHOES),),
            "legwear": (_keys(LEGWEAR),),
            "main_color": (COLORS,),
            "material": (MATERIALS,),
            "accessory_1": (ACCESSORIES,),
            "accessory_2": (ACCESSORIES,),
        }, "optional": {
            "custom_outfit": ("STRING", {"default": "", "multiline": True,
                              "tooltip": "Free-text override (replaces all selections)"}),
        }}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("wardrobe",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator Klein"

    def build(self, top, bottom, underwear, bra, shoes, legwear,
              main_color, material, accessory_1, accessory_2,
              custom_outfit=""):
        if custom_outfit and custom_outfit.strip():
            return (custom_outfit.strip(),)

        color = main_color if main_color != "none" else ""
        mat = material if material != "none" else ""

        garments = []
        t = TOPS.get(top, "")
        if t:
            if color and t.startswith("a "):
                t = f"a {color} {t[2:]}"
            elif color and t.startswith("an "):
                t = f"a {color} {t[3:]}"
            elif color:
                t = f"{color} {t}"
            if mat:
                t += f" made of {mat}"
            garments.append(t)

        b = BOTTOMS.get(bottom, "")
        if b:
            if not garments and color:
                if b.startswith("a "): b = f"a {color} {b[2:]}"
                elif not b[0].isupper(): b = f"{color} {b}"
            garments.append(b)

        under_bits = []
        bra_v = BRA.get(bra, "")
        if bra_v: under_bits.append(bra_v)
        und_v = UNDERWEAR.get(underwear, "")
        if und_v: under_bits.append(und_v)

        lower_bits = []
        lw = LEGWEAR.get(legwear, "")
        if lw: lower_bits.append(lw)
        sh = SHOES.get(shoes, "")
        if sh: lower_bits.append(sh)

        accs = [a for a in [accessory_1, accessory_2] if a != "none"]

        if not garments and not under_bits and not lower_bits:
            return ("",)

        parts = []
        if garments:
            parts.append("dressed in " + " paired with ".join(garments))
        if under_bits:
            if garments:
                parts.append("with " + " and ".join(under_bits) + " visible underneath")
            else:
                parts.append("wearing only " + " and ".join(under_bits))
        if lower_bits:
            parts.append("wearing " + " and ".join(lower_bits))
        if accs:
            parts.append("accessorized with " + " and ".join(accs))

        result = "She is " + ", ".join(parts) if parts else ""
        return (_clean(result),)


# ═══════════════════════════════════════════════════════════════
# 4. POSE
# ═══════════════════════════════════════════════════════════════
class KleinPose:
    """Pose as flowing prose."""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "position": (_keys(POSITIONS),),
            "left_hand": (_keys(LEFT_HAND),),
            "right_hand": (_keys(RIGHT_HAND),),
            "legs": (_keys(LEGS),),
        }, "optional": {
            "custom_pose": ("STRING", {"default": "", "multiline": True}),
        }}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator Klein"

    def build(self, position, left_hand, right_hand, legs, custom_pose=""):
        if custom_pose and custom_pose.strip():
            return (custom_pose.strip(),)

        pos_v = POSITIONS.get(position, "")
        lh = LEFT_HAND.get(left_hand, "")
        rh = RIGHT_HAND.get(right_hand, "")
        lg = LEGS.get(legs, "")

        if not pos_v and not lh and not rh and not lg:
            return ("",)

        parts = []
        if pos_v:
            parts.append(f"She is {pos_v}")

        hand_bits = [x for x in [lh, rh] if x]
        if hand_bits and parts:
            parts.append("with " + " and ".join(hand_bits))
        elif hand_bits:
            parts.append("With " + " and ".join(hand_bits))

        if lg:
            parts.append(lg if parts else lg.capitalize())

        return (_clean(", ".join(parts)),)


# ═══════════════════════════════════════════════════════════════
# 5. SCENE
# ═══════════════════════════════════════════════════════════════
class KleinScene:
    """Scene as photographer's notes."""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "preset": (_keys(SCENE_PRESETS), {"default": "custom"}),
            "lighting": (_keys(LIGHTINGS),),
            "location": (_keys(LOCATIONS),),
            "atmosphere": (_keys(ATMOSPHERES),),
            "framing": (_keys(FRAMINGS),),
            "camera_angle": (_keys(CAMERA_ANGLES),),
            "camera_mode": (_keys(CAMERA_MODES),),
            "lens": (_keys(LENSES),),
            "film_stock": (_keys(FILM_STOCKS),),
            "quality": (_keys(QUALITY),),
            "film_grain": ("BOOLEAN", {"default": False}),
            "motion_blur": ("BOOLEAN", {"default": False}),
            "lens_flare": ("BOOLEAN", {"default": False}),
            "bokeh": ("BOOLEAN", {"default": False}),
            "vignette": ("BOOLEAN", {"default": False}),
            "chromatic_aberration": ("BOOLEAN", {"default": False}),
            "light_leaks": ("BOOLEAN", {"default": False}),
            "noise_grain": ("BOOLEAN", {"default": False}),
        }, "optional": {
            "custom_scene": ("STRING", {"default": "", "multiline": True}),
        }}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator Klein"

    def build(self, preset, lighting, location, atmosphere, framing,
              camera_angle, camera_mode, lens, film_stock, quality,
              film_grain, motion_blur, lens_flare, bokeh, vignette,
              chromatic_aberration, light_leaks, noise_grain,
              custom_scene=""):
        if custom_scene and custom_scene.strip():
            return (custom_scene.strip(),)

        if preset != "custom" and preset in SCENE_PRESETS and SCENE_PRESETS[preset]:
            p = SCENE_PRESETS[preset]
            lighting = p.get("lighting", lighting)
            location = p.get("location", location)
            atmosphere = p.get("atmosphere", atmosphere)
            framing = p.get("framing", framing)
            camera_angle = p.get("angle", camera_angle)

        # ── S1: camera + framing ──
        cam_parts = []
        cm = CAMERA_MODES.get(camera_mode, "")
        fr = FRAMINGS.get(framing, "")
        ca = CAMERA_ANGLES.get(camera_angle, "")
        if cm: cam_parts.append(cm)
        if fr: cam_parts.append(fr)
        if ca: cam_parts.append(ca)
        s_cam = ", ".join(cam_parts) if cam_parts else ""

        # ── S2: location + lighting ──
        loc = LOCATIONS.get(location, "")
        lt = LIGHTINGS.get(lighting, "")
        if loc and lt:
            s_env = f"The scene is set {loc}. {lt}"
        elif loc:
            s_env = f"The scene is set {loc}"
        elif lt:
            s_env = lt
        else:
            s_env = ""

        # ── S3: atmosphere + lens + stock + quality ──
        style_parts = []
        for key, data in [(atmosphere, ATMOSPHERES), (lens, LENSES),
                          (film_stock, FILM_STOCKS), (quality, QUALITY)]:
            v = data.get(key, "")
            if v: style_parts.append(v)
        s_style = ". ".join(style_parts) if style_parts else ""

        # ── S4: FX ──
        fx = []
        if film_grain: fx.append("visible film grain adding texture")
        if motion_blur: fx.append("subtle motion blur suggesting movement")
        if lens_flare: fx.append("natural lens flare catching the light")
        if bokeh: fx.append("soft creamy bokeh blurring the background")
        if vignette: fx.append("subtle vignetting darkening the edges")
        if chromatic_aberration: fx.append("slight chromatic aberration on the edges")
        if light_leaks: fx.append("warm light leaks bleeding into the frame")
        if noise_grain: fx.append("visible digital noise from high ISO")

        if len(fx) == 1:
            s_fx = f"The image has {fx[0]}"
        elif len(fx) == 2:
            s_fx = f"The image has {fx[0]} and {fx[1]}"
        elif fx:
            s_fx = f"The image has {', '.join(fx[:-1])}, and {fx[-1]}"
        else:
            s_fx = ""

        return (_clean(". ".join(filter(None, [s_cam, s_env, s_style, s_fx]))),)


# ═══════════════════════════════════════════════════════════════
# 6. PEOPLE
# ═══════════════════════════════════════════════════════════════
class KleinPeople:
    """Add companions, partner, or crowd."""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "companion": (_keys(COMPANIONS),),
        }, "optional": {
            "custom_people": ("STRING", {"default": "", "multiline": True}),
        }}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("people",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator Klein"

    def build(self, companion, custom_people=""):
        if custom_people and custom_people.strip():
            return (custom_people.strip(),)
        return (COMPANIONS.get(companion, ""),)


# ═══════════════════════════════════════════════════════════════
# 7. NSFW
# ═══════════════════════════════════════════════════════════════
class KleinNSFW:
    """NSFW as flowing prose."""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "level": (_keys(NSFW_LEVELS),),
            "context": (_keys(NSFW_CONTEXTS),),
            "pubic_hair": (_keys(PUBIC_HAIR),),
            "natural_skin": ("BOOLEAN", {"default": False}),
            "oiled_glossy": ("BOOLEAN", {"default": False}),
            "goosebumps": ("BOOLEAN", {"default": False}),
            "tan_lines": ("BOOLEAN", {"default": False}),
            "sweaty": ("BOOLEAN", {"default": False}),
            "wet_skin": ("BOOLEAN", {"default": False}),
            "body_hair": ("BOOLEAN", {"default": False}),
            "athletic_detail": ("BOOLEAN", {"default": False}),
            "soft_curves": ("BOOLEAN", {"default": False}),
            "nipples_erect": ("BOOLEAN", {"default": False}),
            "nipples_pierced": ("BOOLEAN", {"default": False}),
            "belly_button_piercing": ("BOOLEAN", {"default": False}),
        }, "optional": {
            "custom_nsfw": ("STRING", {"default": "", "multiline": True}),
        }}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("nsfw",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator Klein"

    def build(self, level, context, pubic_hair,
              natural_skin, oiled_glossy, goosebumps, tan_lines, sweaty,
              wet_skin, body_hair, athletic_detail, soft_curves,
              nipples_erect, nipples_pierced, belly_button_piercing,
              custom_nsfw=""):
        if custom_nsfw and custom_nsfw.strip():
            return (custom_nsfw.strip(),)

        lv = NSFW_LEVELS.get(level, "")
        ctx = NSFW_CONTEXTS.get(context, "")
        ph = PUBIC_HAIR.get(pubic_hair, "")

        if lv and ctx:
            s1 = f"She is {lv}, {ctx.lower()}"
        elif lv:
            s1 = f"She is {lv}"
        elif ctx:
            s1 = ctx
        else:
            s1 = ""

        if ph and s1:
            s1 += f", with {ph}"
        elif ph:
            s1 = f"With {ph}"

        details = []
        if natural_skin: details.append("natural and unretouched with real texture")
        if oiled_glossy: details.append("glistening with a light oil that traces every contour")
        if goosebumps: details.append("showing goosebumps from the cool air")
        if tan_lines: details.append("marked by visible tan lines")
        if sweaty: details.append("showing a light sheen of sweat")
        if wet_skin: details.append("wet with water droplets catching the light")
        if body_hair: details.append("with natural body hair visible")
        if athletic_detail: details.append("showing visible muscle definition")
        if soft_curves: details.append("with soft natural curves catching the light beautifully")
        if nipples_erect: details.append("with erect nipples")
        if nipples_pierced: details.append("with pierced nipples")
        if belly_button_piercing: details.append("with a belly button piercing catching the light")

        if len(details) == 1:
            s2 = f"Her skin is {details[0]}"
        elif len(details) == 2:
            s2 = f"Her skin is {details[0]} and {details[1]}"
        elif details:
            s2 = f"Her skin is {details[0]}, {', '.join(details[1:-1])}, and {details[-1]}"
        else:
            s2 = ""

        return (_clean(". ".join(filter(None, [s1, s2]))),)


# ═══════════════════════════════════════════════════════════════
# 8. COMBINE
# ═══════════════════════════════════════════════════════════════
class KleinCombine:
    """Assembles all sections into flowing prose for Klein 9B.
    Klein priority: Subject → NSFW/Wardrobe → Face → Pose → People → Scene → Extra."""
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}, "optional": {
            "subject": ("STRING", {"default": "", "forceInput": True}),
            "wardrobe": ("STRING", {"default": "", "forceInput": True}),
            "face": ("STRING", {"default": "", "forceInput": True}),
            "pose": ("STRING", {"default": "", "forceInput": True}),
            "people": ("STRING", {"default": "", "forceInput": True}),
            "scene": ("STRING", {"default": "", "forceInput": True}),
            "nsfw": ("STRING", {"default": "", "forceInput": True}),
            "extra": ("STRING", {"default": "", "multiline": True}),
        }}
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "combine"
    CATEGORY = "ElGenerator Klein"

    def combine(self, subject="", wardrobe="", face="", pose="",
                people="", scene="", nsfw="", extra=""):
        sections = []

        s = (subject or "").strip()
        if s: sections.append(s)

        n = (nsfw or "").strip()
        w = (wardrobe or "").strip()
        if n and w:
            sections.append(n)
            sections.append(w)
        elif n:
            sections.append(n)
        elif w:
            sections.append(w)

        f = (face or "").strip()
        if f: sections.append(f)

        p = (pose or "").strip()
        if p: sections.append(p)

        ppl = (people or "").strip()
        if ppl: sections.append(ppl)

        sc = (scene or "").strip()
        if sc: sections.append(sc)

        e = (extra or "").strip()
        if e: sections.append(e)

        prompt = ". ".join(sections)
        prompt = _clean(prompt)
        if prompt and not prompt.endswith("."):
            prompt += "."

        return (prompt,)


# ═══════════════════════════════════════════════════════════════
NODE_CLASS_MAPPINGS = {
    "Klein_Subject": KleinSubject,
    "Klein_Face": KleinFace,
    "Klein_Wardrobe": KleinWardrobe,
    "Klein_Pose": KleinPose,
    "Klein_Scene": KleinScene,
    "Klein_People": KleinPeople,
    "Klein_NSFW": KleinNSFW,
    "Klein_Combine": KleinCombine,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Klein_Subject": "Klein — Subject 📸",
    "Klein_Face": "Klein — Face 😶",
    "Klein_Wardrobe": "Klein — Wardrobe 👗",
    "Klein_Pose": "Klein — Pose 🧍",
    "Klein_Scene": "Klein — Scene 🎬",
    "Klein_People": "Klein — People 👥",
    "Klein_NSFW": "Klein — NSFW 🔞",
    "Klein_Combine": "Klein — Combine ✏️",
}
