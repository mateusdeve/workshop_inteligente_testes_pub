```markdown
# Design System Documentation: The Editorial Authority

## 1. Overview & Creative North Star
**The Creative North Star: "The Modern Dean"**

This design system moves away from the "startup-blue" aesthetic and into the realm of high-end academic prestige and executive mentoring. It is designed to feel like a bespoke digital broadsheet—authoritative, dense with value, yet breathable. 

We break the "template" look through **Intentional Asymmetry** and **Tonal Depth**. Instead of standard centered grids, we utilize heavy left-aligned typography contrasted against expansive, layered surfaces. The system prioritizes "the silent space" between elements, using structural weight and the interplay of deep Navy (`primary`) and Gold (`tertiary_fixed_dim`) to signal expertise without shouting.

---

## 2. Colors & Surface Philosophy

The palette is rooted in a deep, scholarly foundation. The interaction between the dark primary tones and the warm gold accents creates a "Privileged Information" feel.

### The "No-Line" Rule
Explicitly prohibited: 1px solid `#000` or high-contrast borders for sectioning. Structural boundaries must be defined through:
1.  **Background Color Shifts:** Use `surface_container_low` for the page foundation and `surface_container_lowest` for primary content areas.
2.  **Tonal Transitions:** A section change should be a shift from `surface` to `surface_container`, not a divider line.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. 
- **Base Layer:** `surface` (#f6fafe)
- **Content Blocks:** `surface_container_low` (#f0f4f8)
- **Interactive Cards:** `surface_container_lowest` (#ffffff) sitting atop a `surface_container` section.
This "nesting" creates natural depth and directs the eye toward the most interactive (lightest) elements.

### The "Glass & Gold" Rule
For floating navigation or high-impact mentoring callouts, use **Glassmorphism**. Apply `surface_container_lowest` at 80% opacity with a `20px` backdrop-blur. Use `tertiary_fixed_dim` (#ecc157) sparingly as a signature accent for progress bars or "Verified" status badges to provide a professional polish.

---

## 3. Typography

The typography system is a dialogue between the structured **Work Sans** (Display/Headline) and the highly legible **Inter** (Title/Body).

*   **Display & Headlines (Work Sans):** Used for authoritative statements. High-contrast sizing (e.g., `display-lg` at 3.5rem) should be used to anchor pages. Bold weights in `primary` (#00152a) convey stability.
*   **Body & Labels (Inter):** Optimized for long-form educational content. Use `body-lg` (1rem) for course descriptions to ensure a premium, readable experience.
*   **The Hierarchy of Trust:** Use `label-md` in `on_surface_variant` (#43474d) for metadata (e.g., "5 mins read" or "Mentor Level") to keep the UI clean and focused on the primary narrative.

---

## 4. Elevation & Depth

We eschew "material" shadows in favor of **Tonal Layering** and **Ambient Light**.

*   **The Layering Principle:** Depth is achieved by stacking. A `surface_container_highest` (#dfe3e7) element should only exist to highlight a tertiary piece of information, like a sidebar or a "Notes" panel.
*   **Ambient Shadows:** For "floating" elements like Modals or Dropdowns, use a shadow with a 32px blur, 0% spread, and 6% opacity of `on_secondary_fixed` (#001d33). This mimics natural light in a professional study.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility, use the `outline_variant` (#c3c6ce) at **15% opacity**. It should be a suggestion of a boundary, not a hard stop.

---

## 5. Components

### Buttons
*   **Primary:** Background: `primary` (#00152a); Text: `on_primary` (#ffffff). Use `md` (0.375rem) roundedness. These represent "The Final Action."
*   **Secondary:** Background: `secondary_container` (#c4e0ff); Text: `on_secondary_container` (#48637e). No border.
*   **Tertiary (The "Gold" Action):** Background: `transparent`; Text: `on_tertiary_fixed_variant` (#5a4300); Border: `ghost` style. Use for "Scholarship" or "Premium" paths.

### Input Fields
*   **Surface:** `surface_container_lowest` (#ffffff).
*   **Border:** Use `outline_variant` at 20% opacity. On focus, transition to a 2px `primary` bottom-border only to maintain an editorial feel.
*   **Text:** `on_surface` (#171c1f) for input, `on_surface_variant` for placeholders.

### Cards & Lists (The "Anti-Divider" Rule)
*   **Forbid Divider Lines:** Use `Spacing Scale 8` (2rem) of vertical white space to separate list items.
*   **Mentoring Cards:** Use `surface_container_low` with a `tertiary_fixed_dim` (Gold) left-edge accent (4px width) to denote "Featured" or "Expert" status.

### Progress Indicators (Education Context)
*   Use `primary_container` (#102a43) for the track and `tertiary_fixed_dim` (#ecc157) for the progress fill. This "Gold on Navy" pairing signals achievement and value.

---

## 6. Do's and Don'ts

### Do:
*   **Do** use `20` (5rem) or `24` (6rem) spacing for top-level section margins to create an "Executive" feel.
*   **Do** use `Work Sans` for all numerical data to give it an architectural, precise look.
*   **Do** layer `surface_container_lowest` cards on `surface_container_low` backgrounds for a soft "lift."

### Don't:
*   **Don't** use 100% opaque `outline` tokens for borders; it creates a "cheap" or "boxed-in" feeling.
*   **Don't** use standard "Success Green" for mentoring wins. Use `tertiary` (Gold) or `primary` (Navy) to maintain the sophisticated palette.
*   **Don't** use `full` (9999px) roundedness on primary buttons; stay within `md` (0.375rem) or `lg` (0.5rem) to keep the look "Sharp and Structured."