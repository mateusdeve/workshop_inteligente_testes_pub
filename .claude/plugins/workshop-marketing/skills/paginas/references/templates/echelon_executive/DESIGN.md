# Design System: The Executive Authority

## 1. Overview & Creative North Star: "The Modern Boardroom"
This design system is engineered to command respect. It moves away from the "startup-friendly" soft UI and instead adopts a **High-End Editorial** approach. The Creative North Star is **"The Modern Boardroom"**—an environment defined by expansive space, architectural structuralism, and an uncompromising focus on clarity.

To break the "template" look, we bypass traditional grids in favor of **intentional asymmetry**. We use large, high-contrast typography scales (the "Manrope" display face) against deep, void-like backgrounds (`primary` #00152a) to create a sense of monumental scale. The UI is not just a tool; it is a digital manifestation of a corner office.

---

## 2. Colors: Tonal Depth over Borders
The palette is rooted in power. We use deep navies and muted golds to evoke tradition, while modern surface layering ensures the experience feels cutting-edge.

### The "No-Line" Rule
**Explicit Instruction:** You are prohibited from using 1px solid borders to define sections. Layout boundaries must be established solely through background color shifts. For example, a `surface-container-low` (#f3f4f5) section should sit directly against a `surface` (#f8f9fa) background. This creates a "seamless" high-end feel.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of premium materials.
*   **Base Level:** `surface` (#f8f9fa) for main page backgrounds.
*   **The Inset:** Use `surface-container` (#edeeef) for content blocks that need to feel "recessed."
*   **The Raised Layer:** Use `surface-container-lowest` (#ffffff) for floating cards or interactive modules to create a subtle, natural lift.

### The "Gold Standard" & Textures
*   **Secondary Tone:** `secondary` (#775a19) is our "Matte Gold." Use it sparingly for high-impact CTAs or accent icons.
*   **Signature Gradients:** To add "soul," use a subtle linear gradient on primary CTAs: from `primary` (#00152a) to `primary_container` (#102a43). This prevents the deep blue from looking "flat" or "dead" on high-brightness screens.

---

## 3. Typography: The Voice of Leadership
We utilize a dual-font strategy to balance architectural strength with executive readability.

*   **Display & Headlines (Manrope):** Chosen for its geometric precision and modern "strong" character. Use `display-lg` (3.5rem) for hero statements to create an immediate sense of authority.
*   **Body & Labels (Inter):** The industry standard for legibility. Inter provides a neutral, objective tone that allows the user to focus on the content without visual fatigue.
*   **Hierarchy as Brand:** Use extreme contrast between `display-lg` and `body-md`. Large headlines should feel like titles on a luxury magazine cover, while body text should feel like a well-drafted executive summary.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows and borders are too "retail." For this system, we use **Tonal Layering**.

### The Layering Principle
Depth is achieved by stacking `surface-container` tiers. 
*   **Example:** A white card (`surface-container-lowest`) placed on a light grey section (`surface-container-low`) creates a soft edge that the eye perceives as depth without the "noise" of a shadow.

### Ambient Shadows
If a floating effect (like a Modal or Menu) is required, use **Ambient Shadows**:
*   **Spec:** Blur: 32px to 64px | Opacity: 4%-6% | Color: `on_surface` (#191c1d).
*   Shadows must feel like "environmental light" rather than a dark glow.

### Glassmorphism
For floating navigation bars or overlays, use `surface` (#f8f9fa) at 80% opacity with a `20px backdrop-blur`. This allows the deep `primary` colors of the content to bleed through, softening the interface and making it feel integrated.

---

## 5. Components: Structural Integrity

### Buttons
*   **Primary:** Rectangular with `sm` (0.125rem) or `none` (0px) roundedness. Use the `primary` (#00152a) background with `on_primary` (#ffffff) text. No borders.
*   **Secondary (Gold):** Use `secondary` (#775a19). This is your "Action" color.
*   **Tertiary:** Text-only in `primary`, using a `2px` underline that only appears on hover.

### Inputs & Fields
*   **Style:** Minimalist. No four-sided boxes. Use a bottom-only border using `outline_variant` (#c3c6ce).
*   **Focus:** Transition the bottom border to `secondary` (#775a19) with a `2px` weight.

### Cards & Lists
*   **The "No-Divider" Rule:** Forbid the use of line dividers between list items. Use vertical white space (Scale `6` or `8`) or a `surface-variant` hover state to separate content. 
*   **Structure:** Content should be "left-aligned heavy" to emphasize the structured, serious nature of the brand.

### The "Executive Dashboard" Widget
A custom component for this system. A container using `primary` (#00152a) with `secondary` (#775a19) accents, used to highlight key metrics or "The Golden Rule" of a leadership lesson.

---

## 6. Do's and Don'ts

### Do:
*   **Do** use generous white space (Scale `16` and `20`) to create a "luxury" feel.
*   **Do** use `primary_fixed` (#d1e4ff) for subtle background highlights behind dark text.
*   **Do** ensure all icons are "Line Art" style with a consistent 1.5px or 2px stroke weight.

### Don't:
*   **Don't** use "Extra Large" rounded corners. Stick to `sm` (0.125rem) or `none` to maintain a "sharp," professional edge.
*   **Don't** use bright, saturated colors. If you need an error state, use `error` (#ba1a1a) but keep it contained within a small area.
*   **Don't** use standard "drop shadows." If it looks like a default "Material Design" card, it has failed.
*   **Don't** center-align long blocks of text. Leadership is direct; keep it left-aligned and structured.