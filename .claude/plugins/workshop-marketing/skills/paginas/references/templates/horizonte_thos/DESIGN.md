# Design System: Horizonte Imóveis
**Project:** High-End Real Estate Digital Experience  
**Status:** Director's Editorial Guidelines  

---

### 1. Overview & Creative North Star: "The Curated Horizon"
The objective of this design system is to move beyond the "real estate portal" archetype. We are not building a database; we are crafting a digital gallery. The Creative North Star is **"The Curated Horizon"**—a concept where the UI acts as a silent, sophisticated frame for world-class architecture. 

To achieve this, we reject the rigid, "boxed-in" layout of traditional web design. We embrace **intentional asymmetry**, allowing high-contrast serif typography to overlap imagery, and utilizing vast amounts of white space (The "Breathing Room" principle) to signal luxury and exclusivity. The interface should feel as tactile and premium as a physical architectural monograph.

---

### 2. Colors: Tonal Depth & The "No-Line" Rule
The palette is rooted in organic, earthy sophistication. We avoid the "digital blue" of tech and instead use a deep, oceanic navy to anchor the brand's reliability.

*   **Primary (`#000c1e`):** Our Navy. Use this for high-authority moments and primary calls to action.
*   **Secondary (`#625d5a`):** Taupe. This is our bridge between the cold navy and the warm off-white. Use it for supporting text and subtle UI elements.
*   **Surface Hierarchy (`#faf9f7` to `#e3e2e0`):** We use the `surface` tokens to create a "Nested Depth" model.
*   **The "No-Line" Rule:** Explicitly prohibit the use of 1px solid borders to define sections. Boundaries must be established solely through background shifts. For example, a `surface-container-low` section should sit directly against a `background` section to create a soft, architectural transition.
*   **The "Glass & Gradient" Rule:** For floating navigation or modal overlays, use a Glassmorphism effect. Combine `surface-container-lowest` at 80% opacity with a `backdrop-filter: blur(20px)`.
*   **Signature Texture:** In the Hero section, use a subtle linear gradient from `primary` (`#000c1e`) to `primary-container` (`#002344`) to provide a "midnight sky" depth that flat color cannot replicate.

---

### 3. Typography: The Editorial Scale
Typography is our primary tool for conveying "High-End." We pair a timeless Serif for authority with a clean, modern Sans for precision.

*   **Display & Headlines (Noto Serif):** Use `display-lg` (3.5rem) and `headline-lg` (2.0rem) for property names and brand statements. Use a slightly tighter letter-spacing (-0.02em) for a more bespoke, "ink-on-paper" look.
*   **Body & Labels (Manrope):** Use `body-lg` (1.0rem) for property descriptions. Manrope’s geometric clarity balances the Serif’s tradition.
*   **Hierarchy Note:** Do not center-align long blocks of text. Stick to editorial left-alignment or use asymmetrical placement (e.g., a headline offset to the left of a right-aligned image) to break the "template" feel.

---

### 4. Elevation & Depth: Tonal Layering
In "The Curated Horizon," shadows are rare and borders are forbidden. Depth is achieved through **Tonal Layering**.

*   **The Layering Principle:** Place a `surface-container-lowest` card (the lightest "paper") on top of a `surface-container-low` section. The contrast in tone creates a natural, soft lift.
*   **Ambient Shadows:** If an element *must* float (like a floating action button or a modal), use a shadow with a blur radius of at least `32px` at `4%` opacity, tinted with the Navy (`#000c1e`) rather than black.
*   **The "Ghost Border":** If accessibility requires a border, use `outline-variant` at 15% opacity. It should be felt, not seen.

---

### 5. Components: Precision & Minimalist Luxury

*   **Buttons:** 
    *   *Primary:* `primary` background with `on-primary` text. Use `rounded-sm` (0.125rem) for a sharp, architectural edge. Avoid fully rounded "pill" buttons; they feel too "startup."
    *   *Secondary:* `surface-container-highest` background with `primary` text.
*   **Input Fields:** 
    *   Eliminate the 4-sided box. Use a 1px `outline-variant` bottom border only. When focused, transition the color to `primary`. Labels should use `label-sm` in `secondary` taupe.
*   **Cards (Property Cards):** 
    *   No borders. Use a `surface-container-lowest` background. 
    *   **The "Edge-to-Edge" Imagery:** Images in cards must be full-bleed to the top and sides. 
    *   **Spacing:** Use `spacing-6` (2rem) for internal card padding to ensure the content feels "exhibited," not "packed."
*   **Chips (Property Tags):**
    *   Use `secondary-container` with `on-secondary-container` text. Keep them `rounded-none` or `rounded-sm` to maintain the architectural aesthetic.
*   **Lists:** 
    *   Forbid dividers. Separate property features using vertical white space `spacing-4` (1.4rem) or subtle background shifts.

---

### 6. Do's and Don'ts

#### **Do:**
*   **Do** use asymmetrical layouts where a headline overlaps an image by `spacing-10`.
*   **Do** use the full range of `surface-container` tokens to create a sense of physical stacks of paper.
*   **Do** prioritize high-quality, architectural photography with desaturated tones to match the Taupe palette.

#### **Don't:**
*   **Don't** use standard drop shadows (e.g., `0px 4px 10px rgba(0,0,0,0.1)`). They look cheap and dated.
*   **Don't** use "Safety Blue" or "Success Green" in their pure forms. Soften them into the brand palette (e.g., use the Navy for "success" moments).
*   **Don't** use icons with heavy strokes. Use ultra-thin (1pt or 1.5pt) line icons to match the sophistication of the Manrope typeface.
*   **Don't** use 100% opaque black for text. Use `on-surface` (`#1a1c1b`) to maintain a softer, more organic contrast against the off-white background.