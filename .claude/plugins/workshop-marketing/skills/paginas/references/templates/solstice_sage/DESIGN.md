# Design System Strategy: The Editorial Sanctuary

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Curated Breath."** 

In an industry often cluttered with aggressive "growth hacks" and loud calls to action, this system acts as a digital sanctuary. We are moving away from the rigid, boxed-in nature of traditional apps and toward a high-end editorial experience. We achieve this through **Intentional Asymmetry**—where images and text blocks are purposefully offset to create a sense of organic movement—and **Atmospheric Depth**, utilizing tonal shifts rather than structural lines. The goal is to make the user feel as though they are turning the pages of a premium, heavy-stock wellness magazine.

---

## 2. Colors: Tonal Architecture
The palette is rooted in the earth, using `primary` (Sage), `secondary` (Warm Beige), and `tertiary` (Terracotta) to guide the eye.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders to define sections. Layout boundaries must be established solely through background color shifts. For instance, a main content area in `surface` may transition into a footer or a sidebar using `surface-container-low`. This creates a seamless, "liquid" interface that feels expensive and custom.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of fine paper. 
- **Base Level:** `surface` (#fbf9f4).
- **Secondary Content:** `surface-container-low` (#f5f3ee).
- **Elevated Interactive Elements:** `surface-container-highest` (#e4e2dd).
By nesting a `surface-container-lowest` (#ffffff) card inside a `surface-container` (#f0eee9) section, you create a soft, natural focal point without a single drop shadow.

### The Glass & Gradient Rule
To prevent a "flat" or "template" appearance, use Glassmorphism for floating navigation bars or overlay modals. 
- **Glass Specs:** Use `surface` at 70% opacity with a `24px` backdrop-blur. 
- **Signature Textures:** Apply a subtle linear gradient (Top-Left to Bottom-Right) from `primary` (#526442) to `primary-container` (#9caf88) on high-impact CTAs. This adds "soul" and a tactile, silk-like quality to the interface.

---

## 3. Typography: The Editorial Voice
The tension between the serif and sans-serif defines the premium nature of the system.

- **Display & Headlines (`notoSerif`):** These are your "Art Director" moments. Use `display-lg` (3.5rem) with generous `16` (5.5rem) spacing above to let the words breathe. Serifs convey heritage, wisdom, and calm.
- **Body & Labels (`manrope`):** A clean, highly legible sans-serif. By using `body-lg` (1rem) for general content, we maintain a modern edge that balances the traditional serif headers.
- **Hierarchy Hint:** Always pair a `headline-sm` in Serif with a `label-md` in Sans-Serif (all-caps, 0.05em tracking) for a sophisticated, magazine-style "category" look.

---

## 4. Elevation & Depth: Tonal Layering
We reject the heavy, muddy shadows of the early 2010s. We define space through light and atmospheric perspective.

- **The Layering Principle:** Depth is achieved by "stacking" surface tokens. Use the `Roundedness Scale` of `lg` (2rem) or `xl` (3rem) to soften these transitions, making them feel like smooth river stones.
- **Ambient Shadows:** If an element must float (e.g., a FAB or a modal), use a shadow tinted with `on-surface` (#1b1c19) at 4% opacity. The blur should be at least `40px` to mimic natural, diffuse light.
- **The "Ghost Border" Fallback:** If accessibility requires a container boundary, use the `outline-variant` token (#c5c8bc) at 15% opacity. Never use a 100% opaque border.
- **Micro-Depth:** Use a 1px "inner glow" on cards using `surface-container-lowest` at 50% opacity to give the appearance of a beveled edge on fine stationary.

---

## 5. Components: The Tactile Kit

### Buttons
- **Primary:** Gradient fill (`primary` to `primary-container`), `md` (1.5rem) roundedness. No border. White text (`on-primary`).
- **Secondary:** `surface-container-highest` fill with `primary` text. This feels more integrated and less "loud" than an outlined button.
- **Tertiary:** Text-only in `primary` with a `label-md` style.

### Cards & Content Blocks
- **Forbid Dividers:** Do not use horizontal rules (`<hr>`). Separate list items using `3` (1rem) or `4` (1.4rem) spacing from the `Spacing Scale`.
- **Image Treatment:** All imagery must use `lg` (2rem) corner radius. For a "signature" look, use a subtle `surface-variant` (#e4e2dd) background color behind images while they load to maintain the tonal palette.

### Input Fields
- **Styling:** Use `surface-container-low` for the field fill. No bottom line or border. Upon focus, shift the background to `surface-container-highest`.
- **Labels:** Use `label-md` floating above the field, never inside.

### Signature Component: The "Reflection Map"
A custom component for wellness tracking. It uses a soft, organic SVG blob shape (utilizing `tertiary-container`) behind a text layer to highlight daily intentions, breaking the square-grid layout.

---

## 6. Do’s and Don’ts

### Do
- **Embrace Whitespace:** Use the `20` (7rem) and `24` (8.5rem) spacing tokens for top and bottom margins of sections.
- **Asymmetric Grids:** Offset images by `8` (2.75rem) from the text alignment to create an editorial flow.
- **Tone-on-Tone:** Use `secondary-container` text on a `secondary_fixed` background for low-priority "whisper" text.

### Don’t
- **Don’t use pure black:** Always use `on-surface` (#1b1c19) for text to maintain a soft, organic feel.
- **Don’t use `none` roundedness:** Everything in this system has a minimum of `sm` (0.5rem) radius; sharp corners represent tension, which we are actively avoiding.
- **Don’t use "Default" Shadows:** Avoid any shadow that looks like a "drop shadow." If it doesn't look like ambient light, it doesn't belong.
- **Don't crowd the edges:** High-end design requires "wasteful" space. If a screen feels "efficient," it's likely too crowded.