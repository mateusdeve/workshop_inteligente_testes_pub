# Design System: Zen Moderno Editorial

This design system is a comprehensive framework for creating high-end, digital experiences tailored for Personal Development and Mindfulness. It moves away from the rigid, "boxed-in" nature of standard web templates, favoring an editorial approach that breathes with intentionality, peace, and clarity.

---

## 1. Overview & Creative North Star
**Creative North Star: "The Tactile Sanctuary"**

The design must feel less like a "software interface" and more like a high-end, physical wellness journal or a serene architectural space. We achieve this through **Organic Asymmetry** and **Tonal Depth**. 

Instead of centering everything perfectly in a grid, we use generous, uneven white space to guide the eye. We break the "template" look by overlapping typography over soft-edged images and utilizing a "paper-on-paper" layering effect rather than traditional borders.

---

## 2. Colors & Surface Philosophy

The palette is rooted in nature—earthy "Sand" neutrals and "Sage" greens—to evoke a sense of groundedness.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders (`#787c75` or otherwise) to define sections. Boundaries are created through:
- **Background Color Shifts:** Transitioning from `surface` (#fafaf5) to `surface-container-low` (#f3f4ee).
- **Negative Space:** Using the `24` (8.5rem) or `20` (7rem) spacing tokens to create mental "chapters" between content.

### Surface Hierarchy & Nesting
Treat the UI as a series of stacked, fine-paper sheets. 
- **Base Layer:** `surface` (#fafaf5).
- **Secondary Content Areas:** `surface-container` (#edefe8).
- **Interactive Cards:** Place a `surface-container-lowest` (#ffffff) card on top of a `surface-container-low` (#f3f4ee) section. This creates a soft, natural lift without a single line of CSS border.

### The "Glass & Soul" Rule
For floating navigation or modal overlays, use **Glassmorphism**. Use `surface` at 80% opacity with a `backdrop-blur` of 20px. This allows the sage and sand tones of the background to bleed through, maintaining a "breathable" atmosphere.
- **Signature Texture:** Use a subtle linear gradient for Hero CTAs, moving from `primary` (#526447) to `primary-container` (#d4e9c4) at a 45-degree angle. This adds a "soulful" shimmer that flat colors lack.

---

## 3. Typography: The Editorial Voice

We pair a timeless, high-contrast Serif with a modern, breathable Sans-Serif to balance authority with accessibility.

*   **Display & Headlines (Noto Serif):** These are your "vibe setters." Use `display-lg` (3.5rem) for hero statements with tight letter-spacing (-0.02em). This serif conveys the wisdom and prestige of the infoproduct.
*   **Body & Labels (Manrope):** A geometric sans-serif that ensures clarity. Manrope’s open counters allow for high legibility in long-form mindfulness exercises.
*   **The Hierarchy Strategy:** Always pair a `headline-lg` Serif with a `body-md` Sans-Serif. The contrast between the ornate serif and the functional sans-serif creates the "High-End Magazine" feel.

---

## 4. Elevation & Depth

We eschew "Material Design" shadows for **Ambient Tonal Layering**.

*   **The Layering Principle:** Depth is achieved by "stacking." A `surface-container-highest` element placed on a `surface` background provides enough contrast to signify importance without visual noise.
*   **Ambient Shadows:** If a floating element (like a "Start Meditation" FAB) requires a shadow, use:
    *   `box-shadow: 0 20px 40px rgba(47, 52, 46, 0.06);` (Using a tinted version of `on-surface`). Never use pure black or grey.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility (e.g., input fields), use `outline-variant` (#afb3ac) at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons: The Weighted Interaction
*   **Primary:** Background `primary` (#526447), text `on-primary` (#ecffdd). Shape: `full` (pill). Use `spacing-5` (1.7rem) for horizontal padding.
*   **Secondary:** Background `surface-container-high` (#e7e9e2). No border.
*   **Tertiary:** Text `primary`. Underline is a 2px `primary-container` (#d4e9c4) offset by 4px.

### Cards & Lists: The No-Divider Rule
*   **Rule:** Forbid the use of horizontal rules (`<hr>`). 
*   **Execution:** Separate list items using `spacing-4` (1.4rem). To separate cards, use a shift from `surface-container-low` to `surface-container-highest`.
*   **Content:** Cards should use the `xl` (0.75rem) roundedness for a soft, approachable feel.

### Input Fields: The Minimalist Entry
*   **Style:** Background `surface-container-low`, no border, `md` (0.375rem) corner radius. Focus state shifts background to `surface-container-high` with a 1px `primary` ghost border (20% opacity).

### Specialized Component: The "Progress Bloom"
*   For mindfulness tracking, replace standard progress bars with a circular "bloom" using `primary-fixed-dim` (#c6dbb7) that expands in scale rather than a linear fill.

---

## 6. Do's and Don'ts

### Do:
*   **DO** use "Negative Space" as a functional element. A screen should feel 40% "empty."
*   **DO** overlap images with text. Place a `display-md` title so it slightly covers the corner of an image to create depth.
*   **DO** use the `24` (8.5rem) spacing token for top/bottom margins of major sections to promote a sense of calm.

### Don't:
*   **DON'T** use 100% opaque black (#000000). Use `on-background` (#2f342e) for maximum softness.
*   **DON'T** use sharp corners (`none`). Even the most subtle `sm` (0.125rem) radius is required to maintain the "Zen" aesthetic.
*   **DON'T** crowd the edges. No element should ever be within `spacing-4` of the screen edge.