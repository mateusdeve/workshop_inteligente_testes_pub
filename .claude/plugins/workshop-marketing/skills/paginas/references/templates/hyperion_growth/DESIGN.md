```markdown
# Design System Strategy: Growth Tech Editorial

## 1. Overview & Creative North Star
**Creative North Star: "The Kinetic Architect"**
In the world of Digital Marketing and Paid Traffic, data is often viewed as static. This design system rejects that notion. "The Kinetic Architect" is about movement, precision, and high-velocity growth. We are moving away from the "standard SaaS dashboard" look toward a **High-End Editorial Tech** aesthetic. 

The experience must feel like a premium command center. We break the "template" look by using **Intentional Asymmetry**: hero sections should feature overlapping elements (e.g., a mockup bleeding into a headline) and high-contrast typography scales that demand attention. This isn't just a landing page; it’s an engine for conversion.

---

## 2. Colors & Surface Philosophy
The palette is built on a deep, obsidian foundation (`surface: #0b1326`) punctuated by high-energy neon pulses.

*   **Primary (`#ddb7ff` / `#b76dff`):** Use for high-conversion actions. This "Electric Lavender" signifies premium authority.
*   **Secondary & Tertiary (`#4cd7f6` / `#3cddc7`):** Use for data visualization and "Growth" indicators (ROAS, Scaling, Success metrics).
*   **The "No-Line" Rule:** 1px solid borders are strictly prohibited for sectioning. To separate the Hero from the "Social Proof" section, shift the background from `surface` to `surface-container-low`. Let the eye perceive boundaries through tonal shifts, not "boxes."
*   **The Glass & Gradient Rule:** For floating cards or navigation bars, use Glassmorphism. 
    *   *Implementation:* `surface-container` at 60% opacity with a `20px` backdrop-blur. 
    *   Apply a linear gradient from `primary` to `primary-container` at a 135° angle for main CTAs to give them a "liquid light" feel.

---

## 3. Typography: The Power of Scale
We utilize two distinct Sans-Serif personalities to create an editorial hierarchy.

*   **Display & Headlines (Space Grotesk):** This is our "Tech" voice. It’s wide, aggressive, and modern. 
    *   *Usage:* Use `display-lg` (3.5rem) for bold claims like "SCALING TO 7-FIGURES." Use tight letter-spacing (-0.02em) to create a compact, high-impact look.
*   **Body & Titles (Manrope):** This is our "Human" voice. It’s highly legible and professional.
    *   *Usage:* Use `body-lg` (1rem) for persuasive copy. Ensure a line height of 1.6 for maximum readability against the dark background.
*   **Labels:** Use `label-md` in all-caps with 0.05em tracking for overlines (e.g., "STRATEGY PHASE 01") to evoke a sophisticated "dossier" feel.

---

## 4. Elevation & Depth
In this system, depth is not "shadows"—it is **Luminance**.

*   **The Layering Principle:** 
    *   Level 0 (Floor): `surface-container-lowest` (#060e20)
    *   Level 1 (Section): `surface` (#0b1326)
    *   Level 2 (Card): `surface-container` (#171f33)
    *   Level 3 (Interactive): `surface-container-high` (#222a3d)
*   **Ambient Shadows:** If a "Lead Magnet" modal must float, use a shadow with a 40px blur, 0% spread, and 8% opacity using the `secondary` color. This creates a "neon glow" rather than a muddy black shadow.
*   **The "Ghost Border" Fallback:** If accessibility requires a border (e.g., input fields), use `outline-variant` at 15% opacity. It should feel like a suggestion of a shape, not a hard cage.

---

## 5. Components & Interaction

### Buttons (The Conversion Engines)
*   **Primary:** Background: `primary_container` gradient; Shape: `xl` (0.75rem); Text: `on_primary_container` (Bold). On hover, increase the `surface_tint` glow.
*   **Secondary:** Ghost style. No background, `outline-variant` (20% opacity) border. On hover, fill with `secondary` at 10% opacity.

### Performance Chips
*   Use `secondary_container` for positive metrics (e.g., "+450% ROI"). 
*   Shape: `full` (9999px) for a soft, pill-like "tech" aesthetic.

### Data Cards & Lists
*   **Forbid dividers.** Use `spacing-8` (2rem) of vertical whitespace to separate list items. 
*   Use a `surface-container-low` background for even-numbered rows in data tables to maintain the "No-Line" rule.

### Input Fields
*   Background: `surface-container-lowest`. 
*   Focus state: The bottom border glows with a 2px `tertiary` (Ciano) line. This directs "energy" into the user's input.

### Growth Progress Bars (Signature Component)
*   Track: `surface-container-highest`.
*   Indicator: Linear gradient from `secondary` to `tertiary`. This visualizes the transition from "Traffic" to "Conversion."

---

## 6. Do’s and Don’ts

### Do:
*   **Do** use asymmetrical layouts. Place a large `display-lg` headline on the left and a floating "Stat Card" slightly overlapping the bottom right of the text.
*   **Do** use the `24` (6rem) spacing token for major vertical sections to let the "Growth Tech" aesthetic breathe.
*   **Do** use `secondary` (Ciano) for numbers and data points to differentiate "Information" from "Action" (`primary` Purple).

### Don't:
*   **Don't** use pure black (#000000). It kills the depth of the neon accents. Always use `surface`.
*   **Don't** use standard 1px borders. If you feel you need a line, use a background color shift instead.
*   **Don't** use "Light Mode" components. This system is natively dark to reduce eye strain during long "Traffic Management" sessions and to maximize the "Neon" energy.

---

## 7. Spacing Rhythm
Standardize the "Growth Pulse" using the 4px base scale:
*   **Layout Gaps:** `spacing-12` (3rem) or `spacing-16` (4rem).
*   **Component Internal Padding:** `spacing-4` (1rem) for horizontal, `spacing-3` (0.75rem) for vertical.
*   **Rounding:** Use `xl` (0.75rem) for large cards to soften the "Aggressive Tech" edge, making the product feel premium and accessible.```