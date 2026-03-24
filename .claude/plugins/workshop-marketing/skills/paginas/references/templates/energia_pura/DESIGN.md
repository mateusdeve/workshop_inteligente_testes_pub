# Design System Strategy: High-Performance Kineticism

## 1. Overview & Creative North Star: "The Kinetic Pulse"
This design system is built to mirror the physiological state of high-performance training: adrenaline, precision, and raw power. Our Creative North Star is **"The Kinetic Pulse."** 

We are moving away from the static, "boxed-in" layout of traditional fitness apps. Instead, we embrace **Organic Brutalism**. This means high-contrast typography, intentional asymmetry, and a sense of motion. Layouts should feel like they are "mid-movement," using overlapping elements and extreme type scales to create an editorial, premium feel that motivates the user through visual energy.

## 2. Color Theory: High-Voltage Contrast
The palette is rooted in a deep, monochromatic foundation (Black and Gunmetal) to allow the "Electric Yellow" to act as a functional signal of energy and action.

### The "No-Line" Rule
To maintain a high-end, seamless feel, **1px solid borders are strictly prohibited for sectioning.** Boundaries must be defined through:
*   **Background Shifts:** Transitioning from `surface` (#0e0e0e) to `surface-container-low` (#131313).
*   **Negative Space:** Using the Spacing Scale (specifically `spacing-16` or `spacing-20`) to create "breathing rooms" that define content blocks.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. 
*   **Base:** `background` (#0e0e0e).
*   **Intermediate:** `surface-container` (#1a1a1a) for secondary content.
*   **Elevated:** `surface-container-highest` (#262626) for interactive cards.
By nesting a `surface-container-highest` element inside a `surface-container-low` section, we achieve depth through tonal shifts rather than artificial outlines.

### Glass & Gradient (The "Soul" Rule)
Flat colors can feel "dead." For primary CTAs or Hero backgrounds, use a subtle linear gradient:
*   **Active Gradient:** `primary` (#f3ffca) → `primary-container` (#cafd00) at a 135° angle.
*   **Glassmorphism:** For floating navigation or modal overlays, use `surface` at 70% opacity with a `20px` backdrop-blur. This allows the high-performance imagery underneath to bleed through, softening the interface.

## 3. Typography: The Power of the Grid
Typography is our primary visual tool. We pair the industrial precision of **Space Grotesk** with the clean readability of **Manrope**.

*   **Display (Space Grotesk):** Used for PRs (Personal Records), weights, and motivational headlines. Large, bold, and unapologetic.
*   **Headline (Space Grotesk):** Used to anchor sections. Use `headline-lg` with a -2% letter-spacing to increase the "technical" feel.
*   **Body (Manrope):** The workhorse. `body-lg` provides a sophisticated editorial feel for workout descriptions.
*   **Label (Lexend):** Its geometric nature makes it perfect for technical data (Heart Rate, RPM, Time).

**Editorial Tip:** Don't be afraid of the "Display" scale. A single `display-lg` number (e.g., "120kg") can be the centerpiece of a screen, replacing the need for complex iconography.

## 4. Elevation & Depth: Tonal Layering
We reject the "drop shadow" of 2010. Hierarchy is achieved through light and layer physics.

*   **The Layering Principle:** Stack `surface-container` tiers. A `surface-container-lowest` (#000000) card on a `surface-container-low` (#131313) background creates a "recessed" look, perfect for data input fields.
*   **Ambient Shadows:** If a card must float, use a shadow with a blur of `40px`, spread of `0`, and a color of `on-surface` at 6% opacity. It should feel like an ambient occlusion, not a "glow."
*   **The "Ghost Border" Fallback:** If accessibility requires a stroke (e.g., in high-glare environments), use `outline-variant` (#484847) at **15% opacity**.

## 5. Components: Precision Tools

### Buttons
*   **Primary:** Background: `primary` (#f3ffca); Text: `on-primary` (#516700). Shape: `rounded-sm` (0.125rem) for a sharp, technical edge.
*   **Secondary:** Background: `surface-container-highest`; Text: `primary`. 
*   **Kinetic State:** On hover/active, the button should slightly expand (scale 1.02) using a `cubic-bezier(0.4, 0, 0.2, 1)` transition.

### Workout Cards
*   **Rule:** No dividers. Use `surface-container-high` as the card background.
*   **Layout:** Use asymmetrical padding. `padding-top: spacing-8`, `padding-left: spacing-4`. Overlap the workout category label (using `label-md`) across the top-left edge of the card.

### Chips (Metric Tags)
*   **Style:** `surface-variant` background with `on-surface-variant` text.
*   **Selection:** When active, the chip flips to `primary-container` with `on-primary-container` text.

### Performance Inputs (Text Fields)
*   **Style:** Minimalist. Only a bottom stroke using `outline` (#767575) at 30% opacity. 
*   **Focus:** The stroke becomes `primary` (#f3ffca) at 100% opacity with a subtle `primary` outer glow.

### Additional High-Performance Components
*   **The Pulse Meter:** A custom component using a `primary` to `error_dim` gradient to visualize heart rate zones.
*   **The Progress Blade:** Instead of a rounded progress bar, use a sharp-edged bar with a `rounded-none` setting to emphasize the "technical" and "hard" nature of the training.

## 6. Do’s and Don’ts

### Do:
*   **Embrace Asymmetry:** Place headlines off-center to create a sense of movement.
*   **Use High-Contrast:** Keep the `background` dark to let the `primary` (Electric Yellow) scream.
*   **Large Spacing:** Use `spacing-12` or `spacing-16` between major sections to prevent the UI from feeling "cluttered."

### Don't:
*   **Don't use Rounded-Full:** Avoid pill-shaped buttons unless they are small utility tags. Stick to `rounded-sm` or `rounded-md` to maintain a "tough" aesthetic.
*   **Don't use Dividers:** If you feel the need for a line, use a background color shift instead.
*   **Don't use Generic Icons:** Use ultra-thin (1.5pt) or heavy-bold icons; avoid "medium" weights which feel like system defaults.