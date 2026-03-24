# Design System Strategy: The Compassionate Concierge

This design system is engineered to transcend the typical "pet store" aesthetic. Instead of a generic retail interface, we are building a **high-end digital concierge**. The strategy centers on "The Compassionate Concierge" aesthetic: an editorial approach that treats pet care with the sophistication of a luxury wellness brand while maintaining the approachability of a local friend. 

By leveraging intentional asymmetry, tonal depth, and a complete rejection of rigid borders, we create a fluid, organic experience that feels as soft and welcoming as the animals the brand serves.

---

## 1. Creative North Star: Organic Editorial
We avoid the "grid-of-boxes" trap. The interface should feel like a premium lifestyle magazine.
- **Intentional Asymmetry:** Hero sections and image galleries should use offset layouts and overlapping elements (e.g., an image overlapping a `surface-container` card) to create movement.
- **Tonal Breadth:** We use the full spectrum of the blue (`primary`) and orange (`secondary`) palettes to create "vibe shifts" between different areas of the app—cool and clinical for pharmacy/health; warm and energetic for toys/play.
- **Breathing Room:** We treat white space as a functional element, not a void.

---

## 2. Color & Surface Architecture

### The Palette
The system uses a sophisticated Material 3 logic to ensure the "Amigo Fiel" brand feels professional yet vibrant.
- **Primary (`#00677d`)**: A deep, trustworthy teal-blue that anchors the professional side of the business.
- **Secondary (`#954a00`)**: A warm, vibrant orange used for energy and calls to action.
- **Tertiary (`#845400`)**: Used for "organic" accents, mimicking natural earth tones.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders for sectioning. 
Structure is defined by color shifts. A `surface-container-low` section should sit directly against a `surface` background. If you need a boundary, use a change in tonal value, never a line.

### Surface Hierarchy & Nesting
Treat the UI as a series of nested, physical layers. 
- **Base Layer:** `surface` (#f5fafd).
- **Secondary Layer:** `surface-container-low` (#eff4f7) for large background sections.
- **Action Layer:** `surface-container-lowest` (#ffffff) for interactive cards.
- **Nesting Logic:** Always place a "High" container inside a "Low" container to create a natural, soft lift.

### The Glass & Gradient Rule
To move beyond a flat UI, apply **Glassmorphism** to floating elements (like Navigation Bars or Quick-Action Modals):
- Use `surface` at 70% opacity with a `20px` backdrop-blur.
- **Signature Gradient:** Use a subtle linear gradient from `primary` (#00677d) to `primary_container` (#00b4d8) for Hero backgrounds to add "soul" and depth.

---

## 3. Typography: The Friendly Authority

We pair two distinct rounded faces to balance "Friendly" with "Professional."

| Level | Token | Font Family | Size | Character |
| :--- | :--- | :--- | :--- | :--- |
| **Display** | `display-lg` | Plus Jakarta Sans | 3.5rem | Bold, expressive, welcoming. |
| **Headline**| `headline-md` | Plus Jakarta Sans | 1.75rem | Clear, rounded, approachable. |
| **Title**   | `title-lg` | Be Vietnam Pro | 1.375rem | Clean, modern, efficient. |
| **Body**    | `body-lg` | Be Vietnam Pro | 1rem | Highly legible for long pet care tips. |
| **Label**   | `label-md` | Plus Jakarta Sans | 0.75rem | All-caps or bold for utility. |

**Editorial Note:** Use `display-lg` with tight letter-spacing and negative margins to overlap with images, creating a "custom-designed" feel for hero banners.

---

## 4. Elevation & Depth: Tonal Layering

### The Layering Principle
Forget shadows for standard cards. Use the **Surface Scale** to create hierarchy:
1. **Background:** `surface`
2. **Main Content Area:** `surface-container-low`
3. **Interactive Cards:** `surface-container-lowest`

### Ambient Shadows
When an element must float (e.g., a "Book Grooming" FAB), use an **Ambient Shadow**:
- **Color:** A tinted version of `on-surface` (e.g., `#171c1f` at 6% opacity).
- **Blur:** Large and diffused (e.g., `box-shadow: 0 20px 40px rgba(23, 28, 31, 0.06)`).

### The Ghost Border Fallback
If accessibility requires a container boundary, use a **Ghost Border**:
- Token: `outline-variant` at 15% opacity. It should be felt, not seen.

---

## 5. Components & Signature Patterns

### Buttons (The "Pill" Shape)
- **Primary:** Background `primary`, text `on-primary`. Use `rounded-full` (9999px).
- **Secondary:** Background `secondary_container`, text `on-secondary_container`. No border.
- **Interaction:** On hover, shift background to the `_fixed_dim` variant for a soft glow effect.

### Cards & Lists (The "Anti-Divider" Rule)
- **Rule:** Never use horizontal lines to separate list items.
- **Solution:** Use vertical spacing (`spacing-4`) and alternating background subtle shifts (e.g., odd items on `surface`, even items on `surface-container-low`).
- **Corner Radius:** All cards must use `rounded-lg` (2rem) to maintain the "friendly" aesthetic.

### Input Fields
- Avoid the "boxed" look. Use a `surface-container-highest` background with a `rounded-md` (1.5rem) corner.
- **Focus State:** Instead of a heavy border, use a 2px outer glow of `primary_fixed_dim`.

### Pet-Specific Components
- **The "Vitality Chip":** Small `rounded-full` badges using `tertiary_container` to highlight pet health stats or personality traits (e.g., "Active," "Vaccinated").
- **Booking Carousel:** Use `spacing-10` between cards and allow them to bleed off the edge of the screen to encourage horizontal exploration.

---

## 6. Do’s and Don’ts

### Do
- **Do** overlap images of pets over the edges of container cards to break the "web box" feel.
- **Do** use the `secondary` (orange) sparingly for high-conversion moments—like "Adopt Now" or "Emergency Vet."
- **Do** use `rounded-xl` (3rem) for image masks to mirror the "friendly" typography.

### Don't
- **Don't** use pure black (#000000). Always use `on-surface` (#171c1f) for a softer, premium look.
- **Don't** use sharp corners. Anything less than `rounded-sm` (0.5rem) is prohibited.
- **Don't** use 100% opaque borders. They create visual "noise" that contradicts the "friendly" goal.

---

## 7. Spacing Philosophy
The spacing scale is built on a 0.35rem base. 
- Use **Large Gaps** (`spacing-12` to `spacing-20`) between major editorial sections to let the brand "breathe."
- Use **Tight Gaps** (`spacing-2` to `spacing-4`) within component groups (e.g., Title vs. Subtitle) to maintain a strong proximity relationship.

---
**Director's Closing Note:** 
Remember, the user is trusting us with their best friend. The UI must feel as safe, soft, and professional as the care they expect for their pet. Avoid the default; choose the intentional.