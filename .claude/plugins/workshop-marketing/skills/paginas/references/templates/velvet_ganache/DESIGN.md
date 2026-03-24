# Design System Document: High-End Editorial Culinary Experience

## 1. Overview & Creative North Star: "The Artisanal Atelier"
This design system is engineered to elevate a digital learning platform into a luxury culinary experience. Our Creative North Star is **"The Artisanal Atelier."** Unlike standard educational portals that feel like rigid grids of data, this system mimics the tactile, curated feel of a high-end pastry lookbook or a Michelin-starred dessert menu.

We break the "template" look by prioritizing **intentional asymmetry** and **tonal depth**. By utilizing oversized serif typography (Editorial Scale) and overlapping elements that break container boundaries, we create a sense of movement and "appetizing" flow. The interface should feel as layered and sophisticated as a multi-tiered chocolate ganache.

---

### 2. Colors & Surface Philosophy
The palette is a rich, sensory journey through textures of cream, gold, and deep cacao. 

*   **Primary (#271310):** The "Deep Chocolate." Used for the most critical brand moments and high-contrast typography.
*   **Secondary (#735c00):** The "Burnished Gold." Reserved for accents, interactive highlights, and "Elite" status indicators.
*   **Surface Hierarchy (Cream Layers):** Use the `surface-container` tiers to create a physical sense of depth.
    *   **The "No-Line" Rule:** 1px solid borders are strictly prohibited for sectioning. Boundaries must be defined solely through background shifts. For example, a "Featured Module" card in `surface_container_highest` should sit directly on a `surface` background without an outline.
    *   **The "Glass & Gradient" Rule:** To provide visual "soul," use subtle gradients for Hero backgrounds transitioning from `primary` to `primary_container`. For floating overlays (like recipe navigation), use Glassmorphism: `surface_bright` at 70% opacity with a `20px` backdrop-blur.

---

### 3. Typography: Editorial Authority
Our typography pairs the timeless authority of a serif with the effortless modernism of a clean sans-serif.

*   **The Hero (notoSerif):** Use `display-lg` and `display-md` for headlines. These are your "flavor notes"—large, confident, and elegant. Don't be afraid to let a display-lg headline overlap a product image slightly to create an editorial layout.
*   **The Detail (manrope):** Use `body-lg` for instructional content. Its geometric clarity ensures that complex confectionery steps remain legible even on small mobile screens.
*   **The Labels (manrope):** Use `label-md` in all-caps with `0.05em` letter spacing for "Prep Time" or "Difficulty" tags to maintain a professional, technical look.

---

### 4. Elevation & Tonal Layering
In this system, elevation is an environmental effect, not a structural one.

*   **The Layering Principle:** Depth is achieved by "stacking." Place a `surface_container_lowest` card on a `surface_container_low` section to create a soft, natural lift. This mimics the way fine parchment sits on a marble countertop.
*   **Ambient Shadows:** When a floating effect is required (e.g., a modal), use an extra-diffused shadow.
    *   *Spec:* `0px 20px 40px`, 6% opacity, using the color `on_surface` (#1e1b13). Never use pure black shadows.
*   **The "Ghost Border" Fallback:** If a container requires definition against an identical background color, use a "Ghost Border": the `outline_variant` token at 15% opacity. It should be felt, not seen.

---

### 5. Components & Interaction Patterns

#### Buttons (The "Confection" CTAs)
*   **Primary:** Background: `primary` (#271310). Text: `on_primary` (#ffffff). Shape: `md` (0.375rem). Use a subtle inner-glow gradient on hover to simulate the sheen of tempered chocolate.
*   **Secondary:** Background: `secondary_container` (#fed65b). Text: `on_secondary_container` (#745c00).
*   **Tertiary:** No background. `notoSerif` text with a `2px` underline in `secondary`.

#### Cards & Modules
*   **Strict Rule:** No divider lines. Separate content using the Spacing Scale (e.g., `8` or `10` units of vertical white space).
*   **Composition:** Use asymmetric padding. For instance, a `16` unit padding on the left and a `12` unit padding on the right to create a "Signature" off-center look.

#### Input Fields
*   **Style:** Minimalist. Only a bottom border using `outline` (#827472). On focus, the border transitions to `secondary` (Gold) and the label animates upward using `label-sm`.

#### Special Component: "The Recipe Progress" (Chips)
*   **Action Chips:** Use `secondary_fixed` for completed steps. They should feel like "golden seals" of approval.

---

### 6. Do’s and Don’ts

#### Do:
*   **Embrace Whitespace:** Use `20` and `24` spacing tokens between major sections to let the design "breathe" like a high-end boutique.
*   **Use High-End Imagery:** Only use photography with warm lighting and macro focus on textures (crumbs, melting chocolate, dusting of sugar).
*   **Layering:** Allow images to break out of their `surface-container` boxes for an organic feel.

#### Don’t:
*   **No Grid-Lock:** Avoid perfectly symmetrical 3-column grids. Try a 2/3 and 1/3 split to maintain an editorial rhythm.
*   **No Opaque Borders:** Never use 100% opaque borders to separate content. It kills the "luxury" vibe and makes it look like a standard dashboard.
*   **No System Blues:** Avoid standard "information" blues. Use `tertiary` (deep amber/gold) for informational states.

---

### 7. Implementation Note for Juniors
When building a new screen, always start with the `surface` background. Before placing a box, ask: "Can I define this space just by changing the background tone to `surface_container_low`?" If the answer is yes, you are following the system. If you reach for a border tool, you are straying from the "Atelier" path.