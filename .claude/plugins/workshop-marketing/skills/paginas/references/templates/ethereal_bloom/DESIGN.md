```markdown
# Design System Strategy: The Radiant Editorial

## 1. Overview & Creative North Star
**The Creative North Star: "The Ethereal Atelier"**

This design system is not a utility; it is a digital sanctuary. We are moving away from the "e-commerce template" look toward a "High-End Editorial" experience. The goal is to mimic the tactile sensation of a luxury fashion magazine—heavy paper stocks, airy margins, and a deliberate rejection of "boxy" digital constraints.

To achieve this, we break the traditional grid through **Intentional Asymmetry**. Large-scale typography should overlap high-resolution imagery, and "Surface-Container" layers should be nested to create a sense of physical depth. The layout should breathe, using white space not as a gap, but as a premium "material" itself.

---

## 2. Colors & Surface Philosophy
The palette is a sophisticated blend of organic warmth and metallic precision. We rely on tonal transitions rather than structural lines to define the user journey.

### The "No-Line" Rule
**Strict Mandate:** Designers are prohibited from using 1px solid borders to define sections or cards. 
*   **How to separate content:** Use background color shifts. A `surface-container-low` (#f6f3f1) section should sit directly against a `background` (#fcf9f7) section.
*   **The Depth Hierarchy:** Use the surface tiers to create "stacked paper" effects.
    *   **Level 0 (Base):** `surface` (#fcf9f7)
    *   **Level 1 (Nesting):** `surface-container-low` (#f6f3f1) for secondary content blocks.
    *   **Level 2 (Interaction):** `surface-container-high` (#eae8e6) for hovered states or elevated UI elements.

### The "Glass & Gold" Signature
To elevate the experience beyond flat color, utilize the **Muted Gold Accents** (`secondary`: #775a19) sparingly. 
*   **Glassmorphism:** For floating navigation or modal overlays, use `surface` at 80% opacity with a `20px` backdrop-blur. This allows the soft blush tones of the photography to bleed through the UI, softening the overall aesthetic.
*   **Signature Gradients:** For primary CTAs, apply a subtle linear gradient from `primary` (#785652) to `primary_container` (#ffd4cf) at a 135-degree angle. This mimics the sheen of silk or fine cream.

---

## 3. Typography
Typography is our primary tool for authority. The contrast between the serif and sans-serif conveys the "Science vs. Beauty" duality of the brand.

*   **The Display Scale (notoSerif):** Use `display-lg` and `display-md` for product names and editorial hooks. Kern these tightly (-2%) to create a high-fashion, "locked-in" look.
*   **The Body Scale (manrope):** Use `body-md` (#4f4443) for descriptions. Increase letter spacing (tracking) to `0.02em` to enhance the "airy" feel.
*   **The Label Scale:** Use `label-md` in All-Caps with `0.1em` tracking for utility text, such as "SKIN TYPE" or "APPLICATION." This provides a functional, clinical contrast to the romantic headings.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are too "tech." We achieve depth through **Ambient Light** and **Tonal Stacking**.

*   **The Layering Principle:** Place a `surface-container-lowest` (#ffffff) card on top of a `surface-container` (#f0edeb) background. This creates a soft, natural "lift" that feels expensive and intentional.
*   **Ambient Shadows:** When a float is required (e.g., a luxury product quick-view), use a shadow with a blur of `40px`, a spread of `-10px`, and an opacity of 6% using the `on_surface` (#1b1c1b) color. It should look like a soft glow, not a drop shadow.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility in forms, use `outline-variant` (#d2c3c1) at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons & Interaction
*   **Primary Button:** `surface-tint` (#785652) background with `on_primary` (#ffffff) text. Use `DEFAULT` (0.25rem) roundedness—sharp enough to feel architectural, soft enough to feel premium.
*   **Tertiary Button:** Use `label-md` styling with a 1px underline using the `secondary` (Gold) token, offset by `4px`. No background.

### Input Fields
*   **Form Style:** Forbid "boxed" inputs. Use a "Bottom-Line Only" approach or a very subtle `surface-container-low` fill.
*   **States:** On focus, the bottom line transitions from `outline-variant` to `primary`.

### Cards & Lists
*   **The No-Divider Rule:** Explicitly forbid horizontal rules (`<hr>`). Separate list items using `spacing-5` (1.7rem) or by alternating background tones between `surface` and `surface-container-lowest`.
*   **Image Treatment:** All product imagery should use a "Soft-Focus" shadow or be clipped into asymmetrical containers (e.g., a 0.75rem radius on the top-left corner only) to break the "square" digital feel.

### Selection (Chips & Radios)
*   **Selection Chips:** Use `secondary_container` (#fed488) for the selected state to bring in the muted gold warmth. Text should be `on_secondary_container` (#785a1a).

---

## 6. Do's and Don'ts

### Do:
*   **Do** use asymmetrical spacing (e.g., `spacing-16` on the left, `spacing-24` on the right) to create a sense of movement.
*   **Do** allow typography to overlap image boundaries slightly to create a layered, "collage" editorial feel.
*   **Do** use `surface-dim` (#dcd9d8) for footer backgrounds to ground the experience.

### Don't:
*   **Don't** use pure black (#000000). Always use `on_surface` (#1b1c1b) to maintain the "Soft Blush" warmth.
*   **Don't** use high-contrast borders or dividers. They shatter the premium, seamless illusion.
*   **Don't** cram content. If you think there is enough white space, add `spacing-4` more. Premium is synonymous with "room to breathe."
*   **Don't** use "vibrant" colors for errors. Use the muted `error` (#ba1a1a) tone to ensure the brand's calm composure isn't broken even when something goes wrong.```