# Design System Document: The Tactile Editorial

## 1. Overview & Creative North Star
The creative North Star for this design system is **"The Tactile Editorial."** 

This system moves away from the rigid, clinical grids of standard SaaS and instead draws inspiration from high-end lifestyle magazines and the physical sensation of premium linen paper. For 'Crochê Lucrativo,' we are not just selling a course; we are curated a transition from "hobbyist" to "professional artisan." 

The design breaks the "template" look through **intentional asymmetry**, where images may bleed off-canvas or overlap with typography, and **tonal depth**, where elements are separated by soft shifts in light rather than harsh lines. The goal is to make the user feel like they are leafing through a bespoke lookbook that is as inspiring as it is trustworthy.

---

## 2. Colors
Our palette is a sophisticated interplay of warmth (Terracotta), growth (Sage), and clarity (Cream).

*   **Primary (#94442e):** The heart of the brand. Use for primary CTAs and key headlines to convey passion and the "lucrative" aspect of the business.
*   **Secondary (#53624f):** Muted Sage. Represents the professional, calm, and organic nature of handmade work. Use for secondary actions or grounding elements.
*   **Surface Hierarchy:** Our "Cream" base (`surface` #fcf9f4) is the canvas. Use `surface-container-low` (#f6f3ee) for large section backgrounds and `surface-container-highest` (#e5e2dd) for interactive elements to create a sense of physical layering.

### The "No-Line" Rule
**Explicit Instruction:** You are prohibited from using 1px solid borders to define sections. Layout boundaries must be defined solely through background color shifts or ample white space (using the `20` or `24` spacing tokens). For example, a "Testimonials" section should sit on a `surface-container-low` background to distinguish it from the `surface` hero section, without a single line between them.

### Glass & Gradient Rule
To prevent a "flat" appearance, floating elements (like a sticky "Enroll Now" bar) should utilize **Glassmorphism**. Use a semi-transparent `surface` color with a `backdrop-filter: blur(12px)`. For primary buttons, apply a subtle linear gradient from `primary` (#94442e) to `primary_container` (#b35c44) at a 135-degree angle to add "soul" and dimension.

---

## 3. Typography
The typography strategy creates a dialogue between the *Artisan* (Serif) and the *Entrepreneur* (Sans-Serif).

*   **Display & Headlines (Noto Serif):** These are your "Editorial" voices. Use `display-lg` for the hero and `headline-md` for section starters. These should feel authoritative yet feminine. Encourage letter-spacing of `-0.02em` for large headers to feel more "custom."
*   **Body & Titles (Plus Jakarta Sans):** This is your "Professional" voice. It provides clarity and modern efficiency. Use `body-lg` for lead paragraphs and `label-md` for navigational elements.

**Editorial Tip:** Use "The Big Lead." Pair a `display-lg` headline with a `body-lg` paragraph that uses a wider tracking or a slightly different tonal color (`on_surface_variant`) to create a high-contrast, premium hierarchy.

---

## 4. Elevation & Depth
Depth in this system is achieved through **Tonal Layering**—stacking different values of the cream/beige palette to mimic sheets of fine paper.

*   **The Layering Principle:** Instead of shadows, place a `surface_container_lowest` card on a `surface_container` background. This creates a soft, natural lift.
*   **Ambient Shadows:** If a "floating" element is required (e.g., a modal), use a shadow with a `24px` blur, `0%` spread, and `6%` opacity. The shadow color must be a tinted version of our `on_surface` (#1c1c19), never pure black.
*   **The Ghost Border:** If a boundary is required for accessibility in input fields, use the `outline_variant` token (#dbc1ba) at **20% opacity**. It should be a whisper of a line, not a statement.

---

## 5. Components

### Buttons
*   **Primary:** Uses the Primary-to-Primary-Container gradient. Corner radius set to `full` to maintain the feminine, approachable vibe. 
*   **Secondary:** Muted Sage (`secondary`) with `on_secondary` text. No gradient. 
*   **Interaction:** On hover, scale the button by `1.02` and increase the shadow blur slightly. Avoid abrupt color flips.

### Course Module Cards
*   **Structure:** No borders. Use `surface_container_low` for the card body. 
*   **Nesting:** Inside the card, use `surface_container_lowest` for a small pill or badge (e.g., "6 Lessons") to create internal depth.
*   **Spacing:** Use `8` (2.75rem) internal padding to ensure the content feels "expensive" and has room to breathe.

### Input Fields
*   **Background:** Use `surface_container_highest` to create a "recessed" look. 
*   **Typography:** Labels should be `label-md` in `on_surface_variant`. 
*   **Focus State:** A 1px "Ghost Border" using the `primary` color at 40% opacity.

### Image Treatment
*   **Organic Shapes:** Apply the `xl` (1.5rem) roundedness to all course imagery. 
*   **Asymmetry:** For the Hero image, consider a "floating" look where the image overlaps two different surface colors to break the horizontal grid.

---

## 6. Do's and Don'ts

### Do:
*   **Use Asymmetric Margins:** Let text boxes sit slightly off-center to feel more like a custom-designed book.
*   **Embrace White Space:** If you think there is enough space, add one more level of the spacing scale (`20` or `24`).
*   **Mix Weights:** Use `Noto Serif` in a bold weight for headlines and `Plus Jakarta Sans` in a regular weight for body text for maximum contrast.

### Don't:
*   **Don't use 1px dividers.** Use a `surface` shift or a large gap of whitespace.
*   **Don't use pure black text.** Always use `on_surface` (#1c1c19) to maintain the warm, organic feel.
*   **Don't use standard "Material" shadows.** Stick to the Ambient Shadow rules to avoid a "software" look.
*   **Don't overcrowd.** This course is about the luxury of time and craft; the design must reflect that ease.