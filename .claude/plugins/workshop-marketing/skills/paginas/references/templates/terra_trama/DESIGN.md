# Design System Document: The Artisanal Executive

## 1. Overview & Creative North Star: "The Tactile Studio"
This design system moves away from the sterile, "software-as-a-service" aesthetic to embrace the warmth of a physical atelier. Our Creative North Star is **The Tactile Studio**. We aim to create a digital environment that feels like high-end stationery or a curated physical workshop—organic and handmade, yet sharp, professional, and profitable.

To break the "template" look, we reject rigid grids in favor of **Intentional Asymmetry**. We use overlapping elements (e.g., an image bleeding off the edge of a container) and high-contrast typography scales (pairing massive serif displays with tiny, wide-tracked labels) to create an editorial, high-fashion feel for the crochet entrepreneur.

---

## 2. Colors & Surface Architecture
Our palette transitions from the warmth of raw clay (`primary`) to the calming influence of dried herbs (`secondary`).

### The Hierarchy of Tone
*   **Primary (#86432b):** Used for "The Hook"—call-to-actions and brand moments.
*   **Secondary (#5a614f):** Used for "The Craft"—stabilizing elements and secondary information.
*   **Tertiary (#615344):** Used for "The Business"—sophisticated accents that lend an entrepreneurial edge.

### The "No-Line" Rule
**Strict Prohibition:** Do not use 1px solid borders to define sections.
Boundaries are created through background shifts. A section using `surface-container-low` (#f8f2f0) should sit directly against the `surface` (#fef8f5). This creates a "soft-edge" transition that mimics natural light hitting different planes of fabric or paper.

### The Glass & Gradient Rule
To add "soul," use subtle linear gradients for Hero sections and Primary Buttons:
*   **CTA Gradient:** Transition from `primary` (#86432b) to `primary_container` (#a45a41) at a 135-degree angle.
*   **Glassmorphism:** For floating navigation or modal overlays, use `surface_container_lowest` (#ffffff) at 80% opacity with a `20px` backdrop-blur. This keeps the "handmade" textures of the background visible while providing functional legibility.

---

## 3. Typography: Editorial Authority
The typography is a dialogue between the "Artisan" (Serif) and the "Professional" (Sans-Serif).

*   **Display & Headline (Noto Serif):** These are our "Artisan" voices. They should be used with generous leading. `display-lg` (3.5rem) is reserved for high-impact brand statements.
*   **Title, Body & Label (Manrope):** This is our "Business" voice. Manrope provides a modern, clean contrast that ensures the infoproduct feels like a serious educational tool.
*   **The Signature Pairing:** Always pair a `headline-md` in Noto Serif with a `label-md` in Manrope (all caps, letter-spacing: 0.1rem) to achieve a high-end magazine layout effect.

---

## 4. Elevation & Depth: Tonal Layering
We do not "lift" objects with dark shadows; we "layer" them with light.

*   **The Layering Principle:** Use the `surface-container` tiers to nest content.
    *   *Level 0 (Base):* `surface`
    *   *Level 1 (Section):* `surface-container-low`
    *   *Level 2 (Card):* `surface-container-lowest`
*   **Ambient Shadows:** If a shadow is required (e.g., for a floating action button), use `on-surface` (#1d1b1a) at 5% opacity with a `32px` blur and `8px` Y-offset. This mimics soft, overhead studio lighting.
*   **The Ghost Border:** For input fields or essential containers, use `outline-variant` (#d9c1ba) at **20% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons
*   **Primary:** Uses the Primary Gradient with `rounded-md` (0.75rem). Text is `label-md` in `on-primary` (#ffffff).
*   **Secondary:** A "Ghost" style using `surface-container-high` (#ede7e4) as a base with no border.
*   **Tertiary:** Text-only in `primary`, underlined with a 2px `primary-fixed` (#ffdbd0) stroke for an "analogue" feel.

### Cards & Lists
*   **The Card Rule:** No dividers. Use `spacing-6` (2rem) of vertical white space to separate list items.
*   **Structure:** Cards use `surface-container-lowest` (#ffffff) with a `rounded-lg` (1rem) corner. If multiple cards are grouped, use an asymmetrical "masonry" layout rather than a perfect grid.

### Input Fields
*   **Style:** Minimalist. Use `surface-container-low` (#f8f2f0) as the fill. 
*   **Interaction:** On focus, the background transitions to `surface-container-highest` (#e7e1df) with a subtle `primary` underline (2px). No outer glow.

### Signature Component: The "Pattern Preview" Chip
*   **Design:** A small, circular avatar of a crochet texture paired with `label-sm` text. Use `secondary-container` (#dce2cc) for the background to denote "Eco-friendly/Handmade" status.

---

## 6. Do's and Don'ts

### Do
*   **DO** use whitespace as a functional element. "Breathe" the layout using `spacing-16` (5.5rem) between major sections.
*   **DO** overlap images with text blocks. Place a `title-lg` partially over a high-quality photo of yarn to create depth.
*   **DO** use `tertiary` (#615344) for fine print and captions to maintain the "professional" edge.

### Don't
*   **DON'T** use pure black (#000000) for text. Always use `on-surface` (#1d1b1a) to maintain the organic warmth.
*   **DON'T** use `rounded-full` for buttons unless they are icon-only. The `md` (0.75rem) or `lg` (1rem) radii feel more like "cut fabric" and less like "software."
*   **DON'T** use 1px dividers. If you must separate content, use a background color shift or a `spacing-4` gap.