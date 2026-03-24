# Design System Document: The Editorial Executive

## 1. Overview & Creative North Star
**Creative North Star: "The Modern Dean"**
This design system moves away from the "e-learning template" aesthetic to embrace a high-end, editorial experience. It is designed to feel like a premium business journal or an Ivy League digital archive. We achieve this through **Organic Authority**: a balance of rigid, professional typography and fluid, asymmetrical layouts. 

The goal is to move the user through "The Global Dean" not as a student, but as a rising executive. We break the grid using intentional white space (`spacing.24`) and overlapping elements to create a sense of momentum and "high-growth" energy.

---

## 2. Colors: Tonal Depth & The "No-Line" Rule
The palette is rooted in a deep, authoritative Navy (`primary`) and energized by Amber (`secondary`).

### The "No-Line" Rule
**Strict Mandate:** Designers are prohibited from using 1px solid borders to define sections. Layout boundaries must be established through:
1.  **Background Shifts:** Transitioning from `surface` (#f7f9fe) to `surface_container_low` (#f1f4f9).
2.  **Tonal Nesting:** Placing a `surface_container_lowest` (#ffffff) card atop a `surface_container` (#ebeef3) background.

### Surface Hierarchy & Nesting
Treat the UI as physical layers of fine stationery.
*   **Base:** `surface` for general page backgrounds.
*   **Depth Level 1:** Use `surface_container` for sidebars or secondary content zones.
*   **High-Impact Content:** Use `surface_container_lowest` (Pure White) for the most critical information cards to make them "pop" against the light grey background without needing a stroke.

### The "Glass & Gradient" Rule
To add "soul" to the academic aesthetic:
*   **CTAs:** Use a subtle linear gradient from `primary` (#00113a) to `primary_container` (#002366) at a 135-degree angle.
*   **Overlays:** Use Glassmorphism for floating navigation or modal backdrops. Apply `surface` at 80% opacity with a `20px` backdrop-blur to allow the content beneath to bleed through softly.

---

## 3. Typography: The Authoritative Voice
We utilize a dual-sans-serif approach to maintain modern clarity while feeling established.

*   **Display & Headlines (Manrope):** This is our "Editorial" voice. `display-lg` (3.5rem) should be used for hero statements with tight letter-spacing (-0.02em) to feel impactful and "Growth-Oriented."
*   **Titles & Body (Public Sans):** This is our "Functional" voice. Public Sans provides a neutral, highly readable foundation for complex career-English curriculum.
*   **The Hierarchy Strategy:** Use `label-md` in ALL CAPS with `0.1em` letter-spacing for category tags (e.g., "MODULE 01") to create a sophisticated, archival feel.

---

## 4. Elevation & Depth: Tonal Layering
Traditional drop shadows are too "software-like." We use **Ambient Shadows** and **Tonal Stacking**.

*   **The Layering Principle:** Rather than an elevation scale of 1-5, use the `surface_container` tiers. A "raised" element is simply a lighter color than its parent container.
*   **Ambient Shadows:** If a card must float (e.g., a "Join Now" popover), use a shadow tinted with `on_surface` (#181c20). 
    *   *Spec:* `0px 20px 40px rgba(24, 28, 32, 0.06)`. It should feel like a soft glow, not a hard edge.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility, use `outline_variant` (#c5c6d2) at **15% opacity**. Anything more is too heavy for this system.

---

## 5. Components

### Buttons (The "Call to Growth")
*   **Primary:** Gradient of `primary` to `primary_container`. Text: `on_primary`. Radius: `md` (0.375rem).
*   **Secondary:** Ghost style. Transparent background with a `Ghost Border` and `secondary` (#795900) text.
*   **Tertiary:** Text-only in `primary` with a `2px` underline that expands on hover.

### Progress Cards & Lists
*   **Constraint:** Forbid the use of divider lines between list items. 
*   **Execution:** Use `spacing.4` (1rem) of vertical white space between items. Use a subtle background hover state of `surface_container_high` to indicate interactivity.

### Career-Path Chips
*   **Selection Chips:** Use `secondary_fixed` (#ffdfa0) for the background with `on_secondary_fixed` (#261a00) for text to signal "Amber" energy and high value.

### Input Fields
*   **Style:** Minimalist. No background color (transparent). Only a bottom border using `outline` at 30% opacity. On focus, the border transitions to `primary` with a `2px` weight.

### Bespoke "Global Dean" Components
*   **The "Dean's Note" Callout:** A `surface_container_high` box with a thick `6px` left-accent-bar of `secondary`. This mimics a high-end textbook annotation.
*   **Achievement Badges:** Circular elements using `tertiary_container` (#501300) with `on_tertiary_fixed` (#390b00) icons to denote legacy and prestige.

---

## 6. Do’s and Don'ts

### Do
*   **Do** use asymmetrical margins. If the left margin is `spacing.12`, the right can be `spacing.20` for a modern, editorial feel.
*   **Do** use `headline-lg` for short, punchy career advice.
*   **Do** embrace "The Void." Use ample white space (`spacing.24`) to denote a premium, unhurried experience.

### Don’t
*   **Don't** use 100% black. Use `on_surface` (#181c20) for all text to maintain a softer, high-end look.
*   **Don't** use `full` (pill) roundedness for buttons. It looks too "social media." Stick to `md` (0.375rem) for a professional, architectural feel.
*   **Don't** use standard "Success Green." Use the Amber `secondary` for all positive reinforcements—it’s our signature color for "Growth."

---
*Document Version 1.0 | Authored by Senior Design Direction*