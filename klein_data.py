"""
El Generator Klein v2 — Data tables
Natural language prose for FLUX.2 Klein 9B
Photographic realism · Amateur / Candid / Casual focus

Design rules:
  - "none" = default for ALL optional fields (never forces a choice)
  - Prose descriptions, not keyword lists
  - Booleans for stackable body/skin details
  - Lighting = highest impact element
"""

import random

def pick(arr):
    return random.choice(arr) if arr else ""

# ═══════════════════════════════════════════════════════════════
# ETHNICITIES
# ═══════════════════════════════════════════════════════════════
ETHNICITIES = {
    "none": {"skin": [], "features": ""},
    "european": {
        "skin": ["porcelain-pale skin", "fair ivory complexion", "light beige skin with a subtle warmth", "rosy fair skin"],
        "features": "European features with a defined bone structure"
    },
    "east_asian": {
        "skin": ["luminous porcelain skin", "smooth ivory complexion", "warm light skin with a healthy glow"],
        "features": "East Asian features with elegant almond-shaped eyes"
    },
    "southeast_asian": {
        "skin": ["warm golden-toned skin", "light sun-kissed tan", "radiant golden complexion"],
        "features": "Southeast Asian features with soft expressive eyes"
    },
    "south_asian": {
        "skin": ["warm olive complexion", "rich golden-brown skin", "deep honey-toned skin"],
        "features": "South Asian features with dark expressive eyes"
    },
    "middle_eastern": {
        "skin": ["warm olive complexion", "golden olive skin", "sun-warmed tan"],
        "features": "Middle Eastern features with defined dark eyes and strong brows"
    },
    "african": {
        "skin": ["rich deep brown skin", "warm medium brown complexion", "deep ebony skin that catches the light beautifully"],
        "features": "African features with a strong defined bone structure"
    },
    "latin": {
        "skin": ["warm caramel complexion", "golden-tan skin", "sun-kissed olive tone"],
        "features": "Latin features with warm expressive eyes"
    },
    "mixed": {
        "skin": ["warm honey complexion", "light caramel skin", "golden beige with an even tone"],
        "features": "striking mixed heritage features"
    },
}

# ═══════════════════════════════════════════════════════════════
# AGE
# ═══════════════════════════════════════════════════════════════
def age_prose(age, gender):
    g = "woman" if gender == "female" else "man"
    pron = "her" if gender == "female" else "his"
    if age <= 20: return f"a young {g} in {pron} late teens"
    elif age <= 25: return f"a young {g} in {pron} early twenties"
    elif age <= 30: return f"a {g} in {pron} late twenties"
    elif age <= 35: return f"a {g} in {pron} early thirties"
    elif age <= 45: return f"a {g} in {pron} forties"
    elif age <= 55: return f"a mature {g} in {pron} fifties"
    else: return f"an older {g} with graceful features"

# ═══════════════════════════════════════════════════════════════
# PHYSIQUE
# ═══════════════════════════════════════════════════════════════
HEIGHT = {
    "none": "",
    "very_short": "very petite and compact",
    "short": "on the shorter side with delicate proportions",
    "average": "",
    "tall": "tall with long proportions",
    "very_tall": "statuesque and towering"
}

BUILD = {
    "none": "",
    "very_slim": "with a very slender, almost ethereal frame",
    "slim": "with a slim, lean figure",
    "average": "",
    "curvy": "with soft, natural curves",
    "full_figured": "with a voluptuous, full-figured body",
    "athletic": "with a toned, athletic build",
    "muscular": "with a powerfully muscled physique",
    "chubby": "with a soft, chubby body and round features",
}

BUST = {
    "none": "",
    "flat": "flat-chested",
    "small": "with a small, modest bust",
    "medium": "",
    "large": "with a full, large bust",
    "very_large": "with a very large, heavy bust",
}

BUST_SHAPE = {
    "none": "",
    "perky": "perky and firm breasts",
    "round": "round, full breasts",
    "natural_sag": "natural breasts with a slight sag",
    "heavy_sag": "heavy breasts hanging naturally with gravity",
    "teardrop": "teardrop-shaped breasts",
    "wide_set": "wide-set breasts",
}

HIPS = {
    "none": "",
    "narrow": "narrow hips",
    "average": "",
    "wide": "wide hips and a curvy silhouette",
    "very_wide": "very wide hips with a dramatic hourglass figure",
}

BUTT = {
    "none": "",
    "flat": "a flat backside",
    "small_round": "a small, round butt",
    "average": "",
    "full_round": "a full, round butt",
    "large": "a large, prominent butt",
    "bubble": "a perky bubble butt",
}

BELLY = {
    "none": "",
    "flat_toned": "a flat, toned stomach",
    "soft": "a soft, slightly rounded belly",
    "chubby": "a chubby, rounded belly",
    "muscular_abs": "visible abdominal muscles",
}

MUSCLE_M = {
    "none": "",
    "lean": "with a lean, wiry frame",
    "athletic": "with an athletic, toned physique",
    "muscular": "with well-defined musculature",
    "bodybuilder": "with a heavily muscled bodybuilder physique",
    "dad_bod": "with a soft dad-bod build",
}

PUBIC_HAIR = {
    "none": "",
    "shaved": "completely shaved smooth",
    "trimmed": "neatly trimmed pubic hair",
    "landing_strip": "a thin landing strip",
    "natural": "natural, ungroomed pubic hair",
    "full_bush": "a full natural bush",
}

# ═══════════════════════════════════════════════════════════════
# HAIR
# ═══════════════════════════════════════════════════════════════
HAIR_COLORS = [
    "none", "jet black", "dark brown", "warm chestnut", "rich auburn",
    "fiery red", "ginger", "dark blonde", "golden blonde",
    "platinum blonde", "strawberry blonde", "silver-grey",
    "pure white", "pink-tinted", "purple-tinted",
    "blue-tinted", "teal-tinted", "ombre dark-to-light",
    "highlighted with lighter streaks",
]

HAIR_LENGTHS = {
    "none": "",
    "shaved": "a shaved head",
    "buzz": "a buzz cut",
    "pixie": "a short pixie cut",
    "bob": "a bob cut grazing the jawline",
    "shoulder": "shoulder-length hair",
    "chest": "long hair falling past the chest",
    "waist": "very long hair reaching the waist",
    "ultra_long": "extremely long flowing hair cascading past the hips",
}

HAIR_TEXTURES = {
    "none": "",
    "straight": "pin-straight and sleek",
    "wavy": "falling in loose natural waves",
    "curly": "in bouncy defined curls",
    "coily": "in tight natural coils",
    "messy": "messy and tousled",
    "voluminous": "thick and voluminous",
    "wet_look": "slicked back with a wet look",
    "frizzy": "with natural frizz and volume",
}

HAIR_STYLES = {
    "none": "",
    "loose": "worn loose and free",
    "ponytail_high": "pulled up in a high ponytail",
    "ponytail_low": "in a low ponytail",
    "messy_bun": "in a messy bun",
    "neat_bun": "in a sleek, neat bun",
    "braided": "woven into a braid",
    "twin_tails": "in twin pigtails",
    "half_up": "styled half-up half-down",
    "side_swept": "swept dramatically to one side",
    "space_buns": "in playful space buns",
    "french_braid": "in a French braid",
    "bed_head": "in a natural bed-head style, sleep-tousled",
}

BANGS = {
    "none": "",
    "blunt": "with straight-cut blunt bangs",
    "curtain": "with soft curtain bangs",
    "side_swept": "with side-swept bangs",
    "micro": "with short micro bangs",
    "wispy": "with delicate wispy bangs",
}

# ═══════════════════════════════════════════════════════════════
# EYES
# ═══════════════════════════════════════════════════════════════
EYE_COLORS = [
    "none", "ice-blue", "deep blue", "grey", "vivid green",
    "forest-green", "hazel", "golden amber", "honey-brown",
    "deep dark brown", "nearly black", "violet",
]

# ═══════════════════════════════════════════════════════════════
# SKIN DETAILS
# ═══════════════════════════════════════════════════════════════
SKIN_DETAILS = [
    "none",
    "a light dusting of freckles across the nose and cheeks",
    "heavy freckles covering the face and shoulders",
    "a small beauty mark near the lip",
    "flushed rosy cheeks",
    "a light sun-kissed tan",
    "a deep, even tan",
    "visible tan lines",
    "a faint scar along one cheek",
    "acne scars",
    "dimples when smiling",
]

# ═══════════════════════════════════════════════════════════════
# FACE — expression, mouth, gaze, gestures
# ═══════════════════════════════════════════════════════════════
EXPRESSIONS = {
    "none": "",
    "neutral": "a calm, composed expression",
    "confident": "a confident, self-assured expression",
    "contemplative": "a thoughtful, introspective expression",
    "intense": "an intense, piercing expression",
    "soft_smile": "a gentle, warm smile",
    "big_smile": "a wide, beaming smile showing teeth",
    "laughing": "caught mid-laugh, genuine joy on the face",
    "mysterious": "an enigmatic half-smile",
    "serious": "a serious, focused expression",
    "playful": "a playful, teasing expression",
    "seductive": "a seductive, inviting expression with heavy-lidded eyes",
    "shy": "a shy, bashful expression",
    "surprised": "a surprised expression with wide eyes",
    "annoyed": "a slightly annoyed, unimpressed expression",
    "sleepy": "a sleepy, drowsy expression with heavy eyelids",
    "drunk": "a tipsy, slightly unfocused expression",
    "bored": "a bored, disinterested expression",
    "vulnerable": "a raw, unguarded vulnerable expression",
    "cold": "a cold, distant expression betraying nothing",
    "euphoric": "an expression of pure bliss and euphoria",
    "crying": "tears streaming down the face, raw emotion",
}

MOUTH = {
    "none": "",
    "closed": "lips closed",
    "slightly_parted": "lips slightly parted",
    "open": "mouth open",
    "biting_lip": "biting the lower lip",
    "tongue_out": "tongue sticking out playfully",
    "tongue_side": "tongue poking out to the side",
    "tongue_teeth": "tongue pressed against the upper teeth",
    "licking_lips": "licking the lips",
    "blowing_kiss": "blowing a kiss toward the camera",
    "pout": "pouty lips, duck-face",
    "smirk": "a sly smirk, one corner raised",
    "teeth_showing": "showing teeth in a grin",
    "grimace": "a grimace, teeth clenched",
    "o_shape": "mouth in a surprised O shape",
    "eating_something": "eating or biting into something",
    "chewing_gum": "chewing gum with a casual attitude",
    "smoking": "with a cigarette between the lips",
    "drinking": "drinking from a glass or bottle",
}

GAZE = {
    "none": "",
    "camera_direct": "looking directly into the camera",
    "camera_flirty": "giving a flirty look to the camera",
    "camera_defiant": "staring defiantly into the camera",
    "camera_shy": "glancing shyly at the camera",
    "away_left": "looking away to the left",
    "away_right": "looking away to the right",
    "down": "eyes cast downward",
    "up": "looking upward",
    "over_shoulder": "looking back over the shoulder at the camera",
    "closed": "eyes gently closed",
    "half_lidded": "eyes half-lidded, heavy gaze",
    "winking": "winking at the camera",
    "squinting": "squinting slightly",
    "rolling_eyes": "rolling the eyes",
    "looking_at_phone": "looking down at a phone screen",
    "looking_at_mirror": "looking at own reflection",
    "staring_distance": "staring off into the distance",
    "looking_at_partner": "looking at the other person",
}

GESTURES = {
    "none": "",
    "peace_sign": "holding up a peace sign",
    "middle_finger": "flipping off the camera with the middle finger",
    "heart_hands": "making a heart shape with both hands",
    "thumbs_up": "giving a thumbs up",
    "rock_horns": "throwing up rock horns",
    "wave": "waving at the camera",
    "finger_on_lips": "pressing a finger to the lips in a shush gesture",
    "pointing_camera": "pointing directly at the camera",
    "finger_guns": "making finger guns at the camera",
    "ok_sign": "making an OK sign with thumb and index finger",
    "blowing_kiss_hand": "hand in front of lips blowing a kiss",
    "flexing": "flexing one or both arms",
    "prayer_hands": "hands pressed together in a prayer gesture",
    "covering_mouth": "hand covering the mouth, laughing or surprised",
    "chin_rest": "resting chin on hand thoughtfully",
    "selfie_arm": "one arm extended holding the phone for a selfie",
}

# ═══════════════════════════════════════════════════════════════
# POSE — position, hands, legs
# ═══════════════════════════════════════════════════════════════
POSITIONS = {
    "none": "",
    "standing_relaxed": "standing in a relaxed, natural pose",
    "standing_confident": "standing tall with squared shoulders",
    "standing_contrapposto": "standing with weight on one hip, contrapposto",
    "leaning_wall": "leaning casually against a wall",
    "leaning_forward": "leaning forward slightly",
    "leaning_back": "leaning back",
    "sitting_chair": "sitting on a chair",
    "sitting_floor": "sitting on the floor",
    "sitting_edge": "sitting on the edge of a surface, legs hanging",
    "sitting_cross_legged": "sitting cross-legged on the ground",
    "sitting_knees_up": "sitting with knees pulled up to the chest",
    "squatting": "squatting down low",
    "kneeling": "kneeling on the ground",
    "lying_side": "lying on one side, propped on an elbow",
    "lying_back": "lying on the back",
    "lying_stomach": "lying face-down on the stomach",
    "walking": "captured mid-stride, walking naturally",
    "running": "caught mid-run, dynamic motion",
    "dancing": "captured mid-dance, fluid movement",
    "stretching": "stretching the body, arms overhead",
    "climbing_stairs": "going up or down stairs",
    "getting_out_of_car": "getting out of a car, one leg out",
    "in_bathtub": "sitting or lying in a bathtub",
    "in_bed": "in bed, among rumpled sheets and pillows",
    "on_couch": "lounging on a couch or sofa",
    "at_table": "sitting at a table or counter",
    "against_railing": "leaning against a railing or balustrade",
    "in_pool": "in a swimming pool, water at various levels",
}

LEFT_HAND = {
    "none": "",
    "relaxed_side": "left hand relaxed at the side",
    "in_pocket": "left hand in pocket",
    "on_hip": "left hand on hip",
    "in_hair": "left hand running through hair",
    "on_face": "left hand touching the face",
    "on_neck": "left hand on the neck",
    "on_chest": "left hand on the chest",
    "on_thigh": "left hand resting on the thigh",
    "on_waist": "left hand on the waist",
    "raised": "left hand raised up",
    "behind_head": "left hand behind the head",
    "behind_back": "left hand behind the back",
    "holding_phone": "left hand holding a phone",
    "holding_drink": "left hand holding a drink",
    "gripping_clothing": "left hand gripping or pulling at clothing",
    "on_partner": "left hand on the other person",
    "covering_chest": "left hand covering the chest",
    "adjusting_hair": "left hand adjusting hair behind the ear",
    "on_knee": "left hand resting on the knee",
}

RIGHT_HAND = {
    "none": "",
    "relaxed_side": "right hand relaxed at the side",
    "in_pocket": "right hand in pocket",
    "on_hip": "right hand on hip",
    "in_hair": "right hand in hair",
    "on_face": "right hand touching the face or jaw",
    "on_neck": "right hand on the neck",
    "on_chest": "right hand on the chest",
    "on_thigh": "right hand resting on the thigh",
    "on_waist": "right hand on the waist",
    "raised": "right hand raised up",
    "behind_head": "right hand behind the head",
    "behind_back": "right hand behind the back",
    "holding_phone": "right hand holding a phone",
    "holding_drink": "right hand holding a drink",
    "gripping_clothing": "right hand pulling at clothing",
    "on_partner": "right hand on the other person",
    "covering_face": "right hand partially covering the face",
    "reaching_camera": "right hand reaching toward the camera",
    "on_knee": "right hand resting on the knee",
}

LEGS = {
    "none": "",
    "together": "legs together",
    "slightly_apart": "legs slightly apart",
    "wide_stance": "legs in a wide, grounded stance",
    "crossed_standing": "legs crossed while standing",
    "crossed_sitting": "legs crossed while sitting",
    "one_knee_up": "one knee raised",
    "bent": "legs bent at the knee",
    "spread": "legs spread apart",
    "tucked": "legs tucked underneath",
    "dangling": "legs dangling off an edge",
    "one_leg_forward": "one leg extended forward",
    "on_tiptoes": "up on tiptoes",
    "wrapped_around": "legs wrapped around something or someone",
    "in_water": "legs partially submerged in water",
}

# ═══════════════════════════════════════════════════════════════
# WARDROBE — detailed pieces
# ═══════════════════════════════════════════════════════════════
TOPS = {
    "none": "",
    "tshirt": "a casual t-shirt", "tank_top": "a simple tank top",
    "crop_top": "a cropped top showing the midriff",
    "blouse": "a light blouse", "silk_shirt": "a silk button-up shirt",
    "hoodie": "a cozy hoodie", "sweater": "a knit sweater",
    "cardigan": "an open cardigan", "blazer": "a tailored blazer",
    "leather_jacket": "a leather jacket", "denim_jacket": "a denim jacket",
    "bomber_jacket": "a bomber jacket",
    "corset": "a laced corset", "bustier": "a structured bustier",
    "tube_top": "a strapless tube top", "halter": "a halter-neck top",
    "off_shoulder": "an off-the-shoulder top", "cami": "a delicate camisole",
    "oversized_shirt": "an oversized button-up shirt barely covering",
    "sports_bra": "a sports bra", "bikini_top": "a bikini top",
    "bralette": "a lacy bralette", "sheer_top": "a sheer see-through top",
    "mesh_top": "a mesh top", "bodysuit": "a fitted bodysuit",
    "turtleneck": "a fitted turtleneck",
    "flannel": "an unbuttoned flannel shirt",
}

BOTTOMS = {
    "none": "",
    "jeans_skinny": "skinny jeans", "jeans_relaxed": "relaxed-fit jeans",
    "jeans_shorts": "denim cutoff shorts", "mini_skirt": "a mini skirt",
    "midi_skirt": "a midi skirt", "long_skirt": "a flowing long skirt",
    "pleated_skirt": "a pleated skirt",
    "leggings": "leggings", "yoga_pants": "yoga pants",
    "sweatpants": "loose sweatpants", "shorts": "casual shorts",
    "hot_pants": "very short hot pants", "bike_shorts": "bike shorts",
    "leather_pants": "leather pants", "cargo_pants": "cargo pants",
    "trousers": "tailored trousers",
    "mini_dress": "a mini dress", "midi_dress": "a midi dress",
    "maxi_dress": "a long flowing maxi dress",
    "bodycon_dress": "a tight bodycon dress",
    "sundress": "a light sundress", "slip_dress": "a silk slip dress",
    "bikini_bottom": "a bikini bottom",
    "sarong": "a wrap sarong around the hips",
    "towel": "wrapped in a towel",
}

UNDERWEAR = {
    "none": "",
    "full_brief": "plain full-coverage panties",
    "bikini_cut": "bikini-cut underwear",
    "hipster": "hipster-style panties",
    "thong": "a thong",
    "g_string": "a g-string",
    "boy_shorts": "boyshort panties",
    "lace_panties": "delicate lace panties",
    "cotton_panties": "simple cotton panties",
    "high_waisted": "high-waisted retro panties",
    "string_bikini": "string bikini underwear",
    "cheeky": "cheeky-cut panties",
    "no_underwear": "no underwear",
}

BRA = {
    "none": "",
    "push_up": "a push-up bra",
    "bralette_lace": "a delicate lace bralette",
    "sports_bra_u": "a sports bra",
    "strapless": "a strapless bra",
    "sheer_bra": "a sheer, see-through bra",
    "no_bra": "no bra, braless",
}

SHOES = {
    "none": "",
    "barefoot": "barefoot",
    "sneakers": "casual sneakers",
    "heels_stiletto": "stiletto heels",
    "heels_block": "block heels",
    "heels_platform": "platform heels",
    "boots_ankle": "ankle boots",
    "boots_knee": "knee-high boots",
    "boots_thigh": "thigh-high boots",
    "sandals": "strappy sandals",
    "flip_flops": "flip-flops",
    "slippers": "cozy slippers",
    "flats": "ballet flats",
    "loafers": "loafers",
    "combat_boots": "combat boots",
    "converse": "classic Converse sneakers",
    "running_shoes": "running shoes",
}

LEGWEAR = {
    "none": "",
    "ankle_socks": "ankle socks",
    "knee_socks": "knee-high socks",
    "thigh_highs": "thigh-high stockings",
    "fishnet": "fishnet stockings",
    "sheer_pantyhose": "sheer pantyhose",
    "opaque_tights": "opaque black tights",
    "leg_warmers": "leg warmers",
    "garter_stockings": "stockings held up by a garter belt",
}

ACCESSORIES = [
    "none", "delicate necklace", "choker", "layered chains",
    "hoop earrings", "stud earrings", "sunglasses",
    "baseball cap", "beanie", "watch", "bracelets",
    "rings", "belt", "scarf", "hair clip", "scrunchie",
    "headband", "small handbag", "backpack",
    "phone in hand", "headphones around neck", "AirPods",
]

COLORS = [
    "none", "black", "white", "grey", "deep red", "bright red",
    "navy blue", "light blue", "beige", "burgundy", "emerald green",
    "olive", "pink", "pastel pink", "lavender", "gold",
    "camel brown", "leopard print", "plaid", "striped",
    "neon pink", "neon green", "tie-dye", "floral print",
]

MATERIALS = [
    "none", "cotton", "denim", "silk", "satin", "velvet",
    "leather", "lace", "mesh", "sheer fabric", "latex",
    "knit wool", "faux fur", "linen", "chiffon", "jersey",
]

# ═══════════════════════════════════════════════════════════════
# PEOPLE / COMPANIONS
# ═══════════════════════════════════════════════════════════════
COMPANIONS = {
    "none": "",
    "man_casual": "with a man standing beside her in a casual, relaxed manner",
    "man_intimate": "with a man close to her in an intimate, affectionate pose",
    "man_behind": "with a man standing behind her, partially visible",
    "man_hands_only": "with only a man's hands visible on her body",
    "woman_casual": "with another woman beside her, side by side",
    "woman_intimate": "with another woman in a close, intimate embrace",
    "woman_friend": "with a female friend, both smiling and casual",
    "couple_kissing": "locked in a kiss with another person",
    "couple_hugging": "in a tight embrace with another person",
    "group_friends": "surrounded by a group of friends in a social setting",
    "crowd_background": "with a crowd of people visible in the background",
    "passersby": "with strangers walking past in the background",
    "alone_public": "alone but in a public place with people at a distance",
}

# ═══════════════════════════════════════════════════════════════
# LIGHTING
# ═══════════════════════════════════════════════════════════════
LIGHTINGS = {
    "none": "",
    "soft_window": "Soft diffused natural light from a nearby window creating gentle shadows",
    "golden_hour": "Warm golden-hour sunlight backlighting the subject with a radiant halo and soft lens flare",
    "studio_beauty": "Clean studio beauty lighting with a softbox creating even illumination",
    "rembrandt": "Dramatic Rembrandt lighting from one side, half the face in deep shadow",
    "neon_night": "Colorful neon lights reflected off wet surfaces, pink and blue tones on the skin",
    "candlelight": "Warm flickering candlelight casting golden highlights and deep shadows",
    "overcast": "Soft overcast daylight, even shadow-free illumination with muted tones",
    "chiaroscuro": "Extreme chiaroscuro — harsh spotlight carving the subject from deep blackness",
    "backlit": "Strong backlight creating a luminous rim around the subject",
    "ring_light": "Ring light creating even frontal illumination with circular catchlights",
    "harsh_sun": "Harsh direct sunlight creating strong shadows — raw and unfiltered",
    "blue_hour": "Cool blue-hour twilight bathing the scene in melancholic blue tones",
    "foggy": "Diffused light through fog, dreamy atmosphere wrapping every surface",
    "fluorescent": "Cold fluorescent overhead lighting — unflattering, raw, documentary feel",
    "phone_flash": "Harsh phone camera flash illuminating the face directly — amateur snapshot feel",
    "bathroom_light": "Flat bathroom mirror lighting from above — casual, everyday feel",
    "screen_glow": "The cool glow of a phone or computer screen illuminating the face in darkness",
    "string_lights": "Warm string lights or fairy lights creating a soft bokeh glow",
    "club_lights": "Pulsing colorful club lights creating dynamic, fragmented illumination",
    "car_headlights": "Car headlights cutting through darkness, dramatic and uncontrolled",
    "sunset_through_blinds": "Sunset light filtering through venetian blinds, casting striped shadows",
}

# ═══════════════════════════════════════════════════════════════
# LOCATION
# ═══════════════════════════════════════════════════════════════
LOCATIONS = {
    "none": "",
    "studio_black": "against a seamless pure black background",
    "studio_white": "against a clean white background",
    "studio_grey": "against a neutral grey gradient backdrop",
    "bedroom": "in a lived-in bedroom with rumpled sheets and personal clutter",
    "bedroom_luxury": "in a luxurious bedroom with crisp white linens",
    "bathroom_mirror": "in a bathroom, reflected in the mirror",
    "bathroom_shower": "in a steamy shower or just stepping out",
    "bathtub": "in a filled bathtub, water at chest level",
    "living_room": "in a cozy living room on the couch",
    "kitchen": "in a kitchen, casual domestic setting",
    "balcony": "on a balcony overlooking the city",
    "rooftop": "on a rooftop terrace at dusk",
    "apartment_modern": "in a modern minimalist apartment with large windows",
    "hotel_room": "in a hotel room with crisp linens and warm lighting",
    "urban_street_night": "on a city street at night, neon signs and wet pavement",
    "urban_street_day": "on a sunny city sidewalk",
    "cafe": "at an outdoor café",
    "bar_club": "inside a dimly lit bar or club",
    "restaurant": "at a restaurant table",
    "beach": "on a sandy beach",
    "pool": "by a pool with turquoise water",
    "park": "in a park with trees and natural light",
    "forest": "in a forest with dappled light through the canopy",
    "car_interior": "inside a car",
    "parking_garage": "in a parking garage with harsh fluorescent light",
    "gym_locker": "in a gym or locker room",
    "dressing_room": "in a fitting or dressing room",
    "staircase": "on a staircase",
    "elevator": "inside an elevator",
    "office": "in an office or workspace",
    "garden": "in a lush garden",
    "festival": "at an outdoor music festival, crowd in background",
    "concert": "at a concert venue, stage lights in background",
    "train": "on a train, scenery passing through windows",
}

# ═══════════════════════════════════════════════════════════════
# ATMOSPHERE
# ═══════════════════════════════════════════════════════════════
ATMOSPHERES = {
    "none": "",
    "cinematic": "Cinematic quality with anamorphic lens characteristics and film grain",
    "editorial": "High-end fashion editorial photography",
    "intimate": "Intimate, warm atmosphere suggesting closeness",
    "dramatic": "Dramatic high-contrast mood with deep shadows",
    "dreamy": "Dreamy, ethereal quality with soft pastel tones",
    "raw_documentary": "Raw documentary photography, honest and unflinching",
    "noir": "Film-noir atmosphere with hard shadows and moody tension",
    "romantic": "Soft romantic mood with warm golden tones and bokeh",
    "edgy": "Edgy, provocative atmosphere with high contrast",
    "serene": "Calm, meditative atmosphere with muted colors",
    "glamour": "Classic glamour photography with flattering light",
    "gritty": "Gritty urban realism with grain and muted palette",
    "amateur_candid": "Candid amateur snapshot, natural and unposed",
    "smartphone_casual": "Casual smartphone photo, imperfect and authentic",
    "polaroid": "Polaroid instant-photo aesthetic with washed-out colors and white border",
    "social_media": "Social media selfie aesthetic, slightly filtered and flattering",
    "paparazzi": "Paparazzi-style stolen shot, telephoto compression, caught unaware",
    "home_video": "Home video still frame, warm and low-fi",
    "webcam": "Webcam-quality capture, slightly compressed, computer-screen ambient light",
    "party_snapshot": "Party snapshot, slightly blurry, flash visible, chaotic energy",
}

# ═══════════════════════════════════════════════════════════════
# CAMERA
# ═══════════════════════════════════════════════════════════════
FRAMINGS = {
    "none": "",
    "extreme_closeup": "Extreme close-up on the face, every detail visible",
    "headshot": "Tight headshot framing face and neck",
    "portrait": "Portrait from the chest up",
    "medium": "Medium shot from the waist up",
    "three_quarter": "Three-quarter shot from mid-thigh up",
    "full_body": "Full-body shot from head to toe",
    "wide": "Wide shot placing the subject within the environment",
    "from_behind": "Shot from behind, looking at the subject's back",
    "overhead": "Shot from directly above, looking down",
    "floor_level": "Shot from floor level looking up",
}

CAMERA_ANGLES = {
    "none": "",
    "eye_level": "shot at eye level, direct and intimate",
    "slightly_above": "shot from slightly above, flattering angle",
    "low_angle": "shot from below looking up, powerful perspective",
    "high_angle": "shot from above looking down",
    "dutch": "shot at a tilted dutch angle",
    "over_shoulder": "shot from over the shoulder",
    "profile": "shot in profile, clean silhouette",
    "three_quarter": "shot at a three-quarter angle",
}

CAMERA_MODES = {
    "none": "",
    "selfie_front": "Shot as a front-facing phone selfie, arm-length distance, slight wide-angle distortion",
    "selfie_mirror": "Mirror selfie, phone visible in hand, reflected in a mirror",
    "selfie_group": "Group selfie, one person holding the phone with arm extended",
    "dslr": "Shot with a professional DSLR camera",
    "film_camera": "Shot on a film camera with analog characteristics",
    "phone_camera": "Shot with a smartphone camera, natural phone-photo quality",
    "disposable_camera": "Shot on a disposable camera with flash, grainy and imperfect",
    "webcam": "Captured from a webcam, slightly compressed and grainy",
    "security_cam": "Security camera perspective, slightly overhead, low resolution feel",
    "polaroid": "Captured as a Polaroid instant photo",
    "gopro": "Shot on a GoPro with wide-angle fisheye distortion",
}

LENSES = {
    "none": "",
    "24mm": "Shot on a 24mm wide-angle lens with environmental context",
    "35mm": "Shot on a 35mm lens with natural perspective",
    "50mm": "Shot on a classic 50mm lens with beautiful bokeh",
    "85mm": "Shot on an 85mm portrait lens with creamy bokeh",
    "135mm": "Shot on a 135mm telephoto with extreme background blur",
    "macro": "Shot with a macro lens revealing extraordinary detail",
    "vintage_lens": "Shot through a vintage lens with softness and flare",
    "anamorphic": "Shot with an anamorphic lens, oval bokeh and flares",
    "phone_wide": "Phone camera wide-angle lens, slight barrel distortion",
}

FILM_STOCKS = {
    "none": "",
    "portra_400": "Style: Kodak Portra 400 — warm skin tones, soft contrast, fine grain",
    "ektar_100": "Style: Kodak Ektar 100 — vivid saturated colors, punchy contrast",
    "tri_x": "Style: Kodak Tri-X — classic black and white with rich grain",
    "velvia_50": "Style: Fuji Velvia 50 — extremely saturated colors, deep blacks",
    "cinestill_800": "Style: CineStill 800T — cinematic tungsten film with halation",
    "hp5": "Style: Ilford HP5 — beautiful black and white, fine grain",
    "superia": "Style: Fuji Superia — nostalgic consumer film, green shadows",
    "digital_clean": "Clean digital photography with precise white balance",
    "digital_moody": "Moody digital processing, lifted blacks, teal-and-orange grade",
    "vsco_filter": "VSCO-filtered aesthetic, slightly faded, modern Instagram look",
    "lo_fi": "Low-fidelity, slightly out of focus, imperfect exposure",
}

# ═══════════════════════════════════════════════════════════════
# QUALITY / RENDER TAGS (Klein prose-adapted)
# ═══════════════════════════════════════════════════════════════
QUALITY = {
    "none": "",
    "ultra_detailed": "Captured in extraordinary detail, every texture and pore visible",
    "high_resolution": "High-resolution photograph with crisp sharpness throughout",
    "4k_sharp": "Sharp 4K photograph with pixel-perfect detail",
    "8k_ultra": "Ultra-high-resolution 8K photograph with stunning clarity",
    "raw_unedited": "Raw, unedited photograph straight from the camera sensor",
    "magazine_quality": "Magazine-quality photograph with professional retouching",
    "award_winning": "Award-winning photograph with masterful composition and technical perfection",
}

# ═══════════════════════════════════════════════════════════════
# NSFW levels & contexts (more casual / amateur options)
# ═══════════════════════════════════════════════════════════════
NSFW_LEVELS = {
    "none": "",
    "suggestive": "in revealing clothing that hints and suggests, leaving plenty to the imagination",
    "cleavage": "showing generous cleavage, top pulled low",
    "underboob": "with underboob visible beneath a cropped top",
    "sideboob": "with sideboob exposed from the side of a loose top",
    "topless": "topless, bare chest exposed",
    "bottomless": "bottomless, bare from the waist down",
    "nude": "completely nude, the natural unclothed body",
    "partial_nude": "partially nude, selectively bare with fabric providing minimal coverage",
    "implied_nude": "apparently nude but with hands, fabric, or shadows strategically concealing",
}

NSFW_CONTEXTS = {
    "none": "",
    "fine_art": "Presented as fine-art photography, the body treated as sculpture",
    "boudoir": "Boudoir photography, intimate and sensual in soft bedroom light",
    "editorial": "Fashion editorial context, nude as high-fashion artistry",
    "classical": "Classical figure study, referencing Renaissance composition",
    "candid_private": "A candid private moment, unselfconscious, as if caught naturally",
    "morning_after": "Morning-after atmosphere, relaxed in bed, natural and unposed",
    "getting_dressed": "In the middle of getting dressed or undressed, casual transition",
    "shower_bath": "In or just out of the shower or bath, skin glistening with water",
    "changing_room": "In a changing room, mid-change, casual and unposed",
    "skinny_dipping": "Skinny-dipping, body partially visible through water",
    "sunbathing": "Sunbathing, body relaxed and sun-warmed",
    "bedroom_casual": "Casually nude or near-nude in the bedroom, everyday comfort",
    "mirror_selfie": "Taking a mirror selfie, phone visible, casual nude or lingerie",
    "silhouette": "Body presented as a silhouette, form defined by rim light",
    "fabric_drape": "Draped in a single piece of fabric that partially reveals the form",
    "wet_skin": "Skin glistening wet, droplets catching the light",
    "body_paint": "Body partially covered in artistic body paint or markings",
}

# Scene presets
SCENE_PRESETS = {
    "custom": {},
    "studio_noir": {"lighting": "chiaroscuro", "location": "studio_black", "atmosphere": "noir", "framing": "portrait", "angle": "three_quarter"},
    "golden_portrait": {"lighting": "golden_hour", "location": "rooftop", "atmosphere": "romantic", "framing": "portrait", "angle": "slightly_above"},
    "fashion_editorial": {"lighting": "studio_beauty", "location": "studio_grey", "atmosphere": "editorial", "framing": "full_body", "angle": "eye_level"},
    "urban_night": {"lighting": "neon_night", "location": "urban_street_night", "atmosphere": "cinematic", "framing": "three_quarter", "angle": "three_quarter"},
    "intimate_bedroom": {"lighting": "candlelight", "location": "bedroom", "atmosphere": "intimate", "framing": "medium", "angle": "slightly_above"},
    "candid_street": {"lighting": "harsh_sun", "location": "urban_street_day", "atmosphere": "amateur_candid", "framing": "three_quarter", "angle": "eye_level"},
    "selfie_bathroom": {"lighting": "bathroom_light", "location": "bathroom_mirror", "atmosphere": "smartphone_casual", "framing": "medium", "angle": "slightly_above"},
    "party_vibes": {"lighting": "club_lights", "location": "bar_club", "atmosphere": "party_snapshot", "framing": "portrait", "angle": "eye_level"},
    "boudoir": {"lighting": "candlelight", "location": "hotel_room", "atmosphere": "intimate", "framing": "medium", "angle": "slightly_above"},
    "pool_day": {"lighting": "harsh_sun", "location": "pool", "atmosphere": "amateur_candid", "framing": "full_body", "angle": "low_angle"},
    "morning_light": {"lighting": "soft_window", "location": "bedroom_luxury", "atmosphere": "serene", "framing": "portrait", "angle": "slightly_above"},
    "home_casual": {"lighting": "soft_window", "location": "living_room", "atmosphere": "smartphone_casual", "framing": "medium", "angle": "eye_level"},
}
