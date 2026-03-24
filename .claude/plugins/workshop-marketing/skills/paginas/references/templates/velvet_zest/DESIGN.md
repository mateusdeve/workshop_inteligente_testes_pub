```markdown
# Design System Document: High-End Gastronomy & Confectionery

## 1. Overview & Creative North Star: "The Artisanal Gallery"

This design system is built to evoke the sensory experience of a high-end patisserie or a Michelin-starred kitchen. Our Creative North Star is **"The Artisanal Gallery"**—a digital space where the interface recedes to let the craftsmanship of the food take center stage. 

To achieve a "signature" look, we move away from the rigid, boxy layouts of standard e-commerce. Instead, we utilize **intentional asymmetry**, **layered tonal surfaces**, and **generous white space (3.5rem+)** to create a sense of luxury. We treat the screen like a high-end editorial spread, where elements overlap and "breathe," breaking the traditional grid to suggest the organic, hand-finished nature of confectionery.

---

## 2. Colors & Surface Philosophy

The palette is rooted in the "Golden Hour" of gastronomy—warm, buttery vanillas and deep, rich cocoas.

### The "No-Line" Rule
Traditional 1px borders are strictly prohibited for sectioning. They feel clinical and "default." Instead, define boundaries through **Background Color Shifts**. 
- A hero section using `surface` (#fff9ec) should transition into a product story section using `surface-container-low` (#faf3e0). 
- To separate content within a section, use the `surface-container` tiers to create subtle, sophisticated shifts in "heat" and "depth."

### Surface Hierarchy & Nesting
Treat the UI as a series of fine paper sheets. 
- **Base Layer:** `surface` (#fff9ec)
- **Nested Content (Cards/Modules):** `surface-container-low` (#faf3e0) for soft emphasis, or `surface-container-highest` (#e9e2d0) for high-impact callouts.
- **Floating Elements:** Use `surface-container-lowest` (#ffffff) to create a "bright" lift that mimics light hitting a glazed pastry.

### The "Glass & Gradient" Rule
To add "soul" to the interface:
- **CTAs:** Use a subtle linear gradient from `primary` (#a23f00) to `primary-container` (#fa7025) at a 135-degree angle. This mimics the shimmer of caramel.
- **Navigation:** Utilize **Glassmorphism**. Apply `surface` at 80% opacity with a `backdrop-filter: blur(20px)`. This allows the warm tones of food photography to bleed through the interface, keeping the brand feel "appetizing" at all times.

---

## 3. Typography: Editorial Authority

We pair the precision of **Manrope** with the character of **Epilogue** to create a high-contrast, premium hierarchy.

- **Display & Headlines (Epilogue):** These are our "Statement" pieces. Use `display-lg` for hero messaging. The tight kerning and bold weights of Epilogue convey the weight of a luxury brand.
- **Body & Titles (Manrope):** Chosen for its modern, clean legibility. Even at `body-sm`, the open apertures of Manrope ensure readability against the creamy vanilla backgrounds.
- **The Accents (Script):** (Implementation Note: Use a high-end, custom script for "Chef's Notes" or signature elements). Accents should always be set in `primary` (#a23f00) and placed with intentional asymmetry—overlapping images or cutting across "Ghost Borders."

---

## 4. Elevation & Depth: Tonal Layering

We avoid "Drop Shadows" in favor of **Ambient Light**.

- **The Layering Principle:** Depth is achieved by placing a `surface-container-lowest` (#ffffff) element atop a `surface-container` (#f4eedb) background. The 4-unit color shift provides all the "lift" needed for a premium feel.
- **Ambient Shadows:** If a floating element (like a shopping bag) requires a shadow, use a 40px blur with only 6% opacity. The shadow color must be `on-surface` (#1e1c10) mixed with a hint of `primary`, ensuring the shadow feels "warm" rather than grey.
- **The "Ghost Border" Fallback:** If a border is required for a form field, use `outline-variant` (#dcc1b1) at 20% opacity. It should be felt, not seen.

---

## 5. Components

### Buttons: The "Glazed" Interaction
- **Primary:** Gradient from `primary` to `primary-container`. `border-radius: xl` (0.75rem). No shadow. On hover, increase the `surface-tint` overlay by 8%.
- **Secondary:** Transparent background with a `Ghost Border`. Text in `primary`.
- **Tertiary:** Text only in `on-surface-variant` with a 1.5rem bottom-border "accent" that appears only on hover.

### Cards: The "Borderless" Container
Forbid all divider lines.
- **Layout:** Use `surface-container-low` with `xl` rounding.
- **Spacing:** Use `spacing-6` (2rem) internal padding. 
- **Separation:** Use vertical white space (`spacing-12` or `spacing-16`) to separate card groups rather than horizontal rules.

### Input Fields: Soft Forms
- **Background:** `surface-container-highest` (#e9e2d0).
- **Shape:** `md` (0.375rem) rounding.
- **State:** When focused, the `Ghost Border` transitions to 100% opacity `primary`.

### Navigation: The Floating Menu
- Use a floating "Island" style navigation at the bottom or top, utilizing the Glassmorphism rule. This breaks the "top-bar" template and feels more like a modern, artisanal app experience.

---

## 6. Do's and Don'ts

### Do:
- **Use "Scale" as a tool:** Don't be afraid to use `display-lg` typography next to `body-sm` text. The contrast is where the luxury lives.
- **Embrace Asymmetry:** Offset images from their containers by `spacing-4` (1.4rem) to create a custom, scrapbooked feel.
- **Prioritize the "Cream":** Use `surface` (#fff9ec) as your primary canvas. Avoid pure white (#ffffff) unless it's for a high-light "lifted" card.

### Don't:
- **Never use 1px solid dividers:** They "cut" the appetite. Use a change in background tone instead.
- **Avoid high-contrast shadows:** Pure black shadows look "dirty" on vanilla backgrounds. Always tint shadows with the brand's chocolate brown (`on-secondary-fixed-variant`).
- **Don't over-round:** While food is organic, the brand is "High-End." Stick to `xl` (0.75rem) for main containers; `full` rounding is reserved only for Chips and specific utility buttons.

---

*Director's Final Note: This system is a recipe. The tokens provide the ingredients, but the "flavor" comes from your use of negative space. If the layout feels crowded, add another 2rem of padding. Let the brand breathe.*```