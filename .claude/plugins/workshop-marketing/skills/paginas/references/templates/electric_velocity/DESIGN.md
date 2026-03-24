```markdown
# Design System Documentation: The Kinetic Nocturne

## 1. Overview & Creative North Star
This design system is engineered for high-performance SaaS environments that require a blend of technical precision and editorial elegance. We are moving away from the "standard SaaS template" to embrace a philosophy we call **The Kinetic Nocturne**.

**The Creative North Star: The Kinetic Nocturne**
The interface should feel like a high-end cockpit or a digital gallery at midnight. It leverages deep chromatic voids (`background: #0b082f`) contrasted against "electric" light sources. We break the grid through intentional asymmetry—overlapping glass layers and staggered typography—to create a sense of forward motion and sophisticated depth. We do not use lines to define space; we use light, blur, and tonal shifts.

---

## 2. Colors
Our palette is rooted in high-contrast "Nocturne" tones with vibrant "Electric" accents.

### The Color Roles
*   **Primary (`#a3a6ff`):** The "Electric Blue" signature. Used for high-priority actions and brand moments.
*   **Secondary (`#dd8bfb`):** The "Vibrant Purple" offset. Used to provide visual rhythm and secondary CTAs.
*   **Tertiary (`#96f8ff`):** The "Cyber Cyan" highlight. Used sparingly for data visualization or success accents.
*   **Surface Tones:** A progression from `surface_container_lowest` (#000000) to `surface_bright` (#28245f) allows for complex nesting.

### The "No-Line" Rule
**Explicit Instruction:** You are prohibited from using 1px solid borders to separate sections. Boundary definition must be achieved through:
1.  **Background Shifts:** Transitioning from `surface` to `surface_container_low` (#100c37).
2.  **Tonal Transitions:** Using subtle vertical gradients between surface tiers.
3.  **Negative Space:** Utilizing the Spacing Scale (e.g., `20` or `24`) to let the layout breathe.

### The "Glass & Gradient" Rule
To move beyond a flat UI, main CTAs and hero elements must use **Signature Textures**. 
*   **Gradients:** Use a linear gradient from `primary` (#a3a6ff) to `primary_container` (#9396ff) at a 135-degree angle.
*   **Glassmorphism:** For floating navigation or modal overlays, use `surface_variant` (#221e55) at 60% opacity with a `20px` backdrop-blur.

---

## 3. Typography
We utilize a dual-typeface system to balance technical clarity with high-end editorial flair.

*   **Display & Headlines (Manrope):** Chosen for its geometric modernism. Use `display-lg` (3.5rem) with tight letter-spacing (-0.02em) for hero sections. Use `headline-lg` (2rem) for section headers.
*   **Body & Labels (Inter):** The workhorse for legibility. Use `body-lg` (1rem) for primary copy.
*   **Hierarchy as Identity:** Create "typographic tension" by pairing a `display-lg` headline with a `label-md` all-caps subtitle in `secondary` (#dd8bfb). This creates an authoritative, custom feel.

---

## 4. Elevation & Depth
In this system, depth is a physical property of the "Nocturne" environment.

### The Layering Principle (Tonal Stacking)
Depth is achieved by stacking containers from dark to light. 
*   **Level 0:** `background` (#0b082f)
*   **Level 1:** `surface_container` (#161241) for large sections.
*   **Level 2:** `surface_container_high` (#1c184b) for cards or interactive modules.

### Ambient Shadows
Shadows must be felt, not seen.
*   **Shadow Spec:** Blur: 40px–80px. Opacity: 4%–8%. 
*   **Color:** Use a tinted version of `on_surface` (#e6e2ff) rather than black to maintain the "Kinetic" glow.

### The "Ghost Border" Fallback
If accessibility requires a container edge, use a **Ghost Border**: 
*   Token: `outline_variant` (#46436c)
*   Opacity: 15%–20%
*   Weight: 1px

---

## 5. Components

### Buttons
*   **Primary:** Background: Gradient (`primary` to `primary_container`). Text: `on_primary` (#1000a3). Shape: `DEFAULT` (8px).
*   **Secondary:** Background: `transparent`. Border: Ghost Border. Text: `primary`.
*   **Hover State:** Increase `surface_brightness` or add a `4px` outer glow using the `primary_dim` (#5c5eff) color.

### Cards & Modules
*   **Rule:** Forbid divider lines. Use `surface_container_highest` for card headers and `surface_container` for the body to create a natural "step down" in hierarchy.
*   **Rounding:** Apply `md` (12px) to external corners and `sm` (4px) to internal nested elements.

### Input Fields
*   **State:** Default state uses `surface_container_low`. On focus, transition the background to `surface_container_high` and apply a 1px `primary` ghost border.
*   **Typography:** Use `label-md` for floating labels to maintain a technical, clean look.

### Chips & Tags
*   Use `secondary_container` (#6e208c) with `on_secondary_container` (#f1bfff) for high-visibility status.
*   Shape: `full` (9999px) to contrast against the geometric cards.

---

## 6. Do's and Don'ts

### Do:
*   **Do** lean into asymmetry. Stagger images and text blocks using the `12` (3rem) and `16` (4rem) spacing tokens.
*   **Do** use glassmorphism on the Global Nav. It should feel like a translucent blade cutting across the content.
*   **Do** use `tertiary` (#96f8ff) for micro-interactions, like a 2px underline on a hovered link.

### Don't:
*   **Don't** use 100% white (#FFFFFF). Always use `on_surface` (#e6e2ff) to maintain the cinematic, low-eye-strain atmosphere.
*   **Don't** use standard drop shadows. If it looks like a "box shadow," it’s too heavy.
*   **Don't** use dividers. If two pieces of content feel merged, increase the spacing to `8` or `10` or shift the background tone.

### Accessibility Note:
While we use high-contrast accents, ensure that `on_background` text maintains a 4.5:1 ratio against `background`. Use `primary_dim` and `secondary_dim` tokens for interactive states to ensure visibility for all users.```