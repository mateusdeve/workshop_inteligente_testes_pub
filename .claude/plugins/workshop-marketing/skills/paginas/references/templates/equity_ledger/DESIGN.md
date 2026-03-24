# Design System Strategy: The Architectural Ledger

## 1. Overview & Creative North Star
**Creative North Star: "The Digital Private Bank"**

This design system moves away from the "fintech-startup" aesthetic of rounded bubbles and neon gradients. Instead, it adopts the posture of a high-end, editorialized investment firm. The goal is to blend the unwavering authority of a legacy bank with the precision of modern data science.

We break the "template" look by rejecting the standard 12-column rigid grid in favor of **Intentional Asymmetry**. Key data points should feel curated, not just displayed. We use a "Deep-Scale" typography approach where large, authoritative headlines (Manrope) contrast against hyper-legible, functional UI text (Inter). The interface should feel like a series of layered physical surfaces—think matte-finished paper and frosted glass—rather than a flat digital screen.

---

## 2. Colors & Surface Philosophy
The palette is rooted in `primary_container` (#0d1c32) and `secondary` (#006c47). We treat color as a functional tool for hierarchy and success, not just decoration.

### The "No-Line" Rule
**Strict Mandate:** Designers are prohibited from using 1px solid borders to section content. Boundaries must be defined solely through background color shifts.
*   **Example:** A `surface_container_low` section sitting directly on a `surface` background creates a natural, sophisticated edge. Use the Spacing Scale (e.g., `spacing.8`) to let the color transitions breathe.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack. Importance is signaled by "lifting" elements through the container tiers:
1.  **Base Layer:** `surface` (#f8f9ff)
2.  **Sectional Layer:** `surface_container_low` (#eff4ff)
3.  **Interactive Layer (Cards):** `surface_container_lowest` (#ffffff)
4.  **Information Callouts:** `surface_container_high` (#dce9ff)

### The "Glass & Gradient" Rule
To elevate the "Private Bank" feel, use **Glassmorphism** for floating elements (like navigation bars or hovering portfolios).
*   **Token:** Use `surface_variant` at 70% opacity with a `20px` backdrop-blur.
*   **Signature Textures:** For primary CTAs, use a subtle linear gradient from `primary` (#000000) to `primary_container` (#0d1c32) at a 135-degree angle. This adds a "weighted" feel that flat black cannot provide.

---

## 3. Typography: The Editorial Edge
We utilize a dual-font system to balance character with utility.

*   **Display & Headlines (Manrope):** This is our "Editorial" voice. It is geometric and bold. Use `display-lg` for portfolio totals and `headline-md` for section starts. The wide tracking of Manrope conveys stability.
*   **UI & Data (Inter):** This is our "Functional" voice. All labels, inputs, and body copy use Inter. It is optimized for the high-density data environments required for investment tracking.

**Hierarchy Tip:** Always pair a `headline-sm` (Manrope) with a `label-md` (Inter) in `on_surface_variant` (#44474d) to create a clear "Title/Caption" relationship that feels professional and intentional.

---

## 4. Elevation & Depth: Tonal Layering
Traditional drop shadows are too "software-heavy" for this system. We use light and tone to imply depth.

*   **The Layering Principle:** Place a `surface_container_lowest` card on a `surface_container_low` background. The slight shift from `#ffffff` to `#eff4ff` provides a clean, modern lift.
*   **Ambient Shadows:** If an element must float (e.g., a modal), use a shadow tinted with the surface color: `rgba(13, 28, 46, 0.08)` with a `40px` blur and `10px` Y-offset.
*   **The "Ghost Border" Fallback:** If accessibility requires a stroke (e.g., in high-glare environments), use `outline_variant` (#c5c6cd) at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons
*   **Primary:** Gradient of `primary` to `primary_container`. Text: `on_primary` (#ffffff). Radius: `md` (0.375rem).
*   **Secondary:** Solid `secondary` (#006c47). Use for "Success" actions like "Buy" or "Confirm."
*   **Tertiary:** No background. `label-md` in `primary_container` with a subtle `2px` underline on hover.

### Cards & Lists
*   **Rule:** Forbid the use of divider lines.
*   **Implementation:** Separate list items using `spacing.4` vertical padding. For complex data tables, use alternating row fills using `surface_container_low` and `surface_container_lowest`.

### Input Fields
*   **State:** Default background is `surface_container_highest`. 
*   **Focus:** Transition background to `surface_container_lowest` and add a `2px` "Ghost Border" using `surface_tint`.
*   **Error:** Use `error` (#ba1a1a) for the label text and a `surface_container_highest` background with a 10% `error` tint.

### Investment-Specific Components
*   **The "Ticker Tape" Header:** A thin `primary_container` bar at the very top using `label-sm` in `primary_fixed` to display live market indices.
*   **The "Trend Micro-Graph":** Sparklines should use `secondary` (#006c47) for growth and `error` (#ba1a1a) for loss, with a 0.5pt stroke weight for a sophisticated, technical look.

---

## 6. Do’s and Don’ts

### Do
*   **Do** use `spacing.20` and `spacing.24` for hero sections. Wealth management requires "breathing room" to feel premium.
*   **Do** use `surface_dim` for "empty state" backgrounds to maintain a moody, sophisticated atmosphere.
*   **Do** align data right in tables for professional financial legibility.

### Don't
*   **Don't** use `rounded-full` for anything other than status indicators or profile avatars. Professionalism is found in the `md` (0.375rem) and `lg` (0.5rem) corners.
*   **Don't** use pure gray (#808080). Use the "Slate Grays" provided in the `on_surface_variant` and `outline` tokens to keep the palette cool and oceanic.
*   **Don't** use animations that "bounce." Use linear or "ease-in-out" transitions with short durations (200ms) to maintain a serious tone.