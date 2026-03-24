# Aurea Craft Design System

## 1. Overview & Creative North Star
**Creative North Star: "The Digital Atelier"**

Aurea Craft is a design system that elevates traditional craftsmanship to the level of high-fashion editorial. It rejects the "standard app" aesthetic in favor of a curated, gallery-like experience. The system is built on the philosophy that digital interfaces should feel as tactile and intentional as a hand-woven textile. 

It breaks traditional grid rigidity through:
- **Intentional Asymmetry:** Off-center imagery and staggered content blocks.
- **Tonal Depth:** Relying on subtle shifts in greys and off-whites rather than borders.
- **Typographic Authority:** Massive display scales contrasted against ultra-small, wide-tracked labels.

## 2. Colors
The palette is rooted in sophisticated neutrals (Off-whites, Charcoals) with a signature Gold (`primary`) that acts as a thread of luxury through the interface.

- **The "No-Line" Rule:** 1px solid borders are strictly prohibited for sectioning. Structural boundaries must be defined through background color shifts (e.g., moving from `surface` #f9f9f9 to `surface_container_low` #f3f3f3) or high-contrast shifts to `on_surface` (#1a1c1c).
- **Surface Hierarchy:** Use `surface_container_lowest` (#ffffff) for card elements to make them "lift" off the `surface` background without using shadows.
- **Signature Textures:** Main CTAs should utilize a gradient from `primary` (#735C00) to `primary_container` (#D4AF37) to mimic the shimmer of metallic thread.

## 3. Typography
The system uses a high-contrast pairing of **Noto Serif** and **Inter**.

- **Display & Headline:** Noto Serif. Used for high-impact emotional messaging. It conveys heritage and prestige. 
- **Body & Labels:** Inter. A clean, functional sans-serif that provides a modern counter-balance.
- **Scale Ground Truth:**
  - **Display (Huge):** 4.5rem (72px) to 5.5rem (88px) for hero titles.
  - **Headline:** 3.75rem (60px) and 3rem (48px) for section starts.
  - **Subhead/Large Body:** 1.125rem (18px) to 1.5rem (24px) for editorial intro paragraphs.
  - **The Micro-Label:** 10px (0.625rem) with 0.4em letter spacing. This is the hallmark of the system—using tiny, uppercase, wide-tracked text for navigation and metadata to create a "Vogue" editorial feel.

## 4. Elevation & Depth
Aurea Craft eschews traditional Material elevation in favor of layering and transparency.

- **The Layering Principle:** Depth is achieved by stacking `surface-container` tiers. A navigation bar uses `surface/80` with a `backdrop-blur-xl` to feel like glass resting on the content.
- **Ambient Shadows:** Only use the `shadow-2xl` value for featured product imagery to give it a "physical object" presence. UI components (cards, buttons) should remain flat.
- **Glassmorphism:** Navigation and floating overlays must use 80% opacity backgrounds with high-blur (20px+) to maintain a sense of environmental light.

## 5. Components
- **Buttons:** Sharp 0px corners. High-ticket CTAs use the primary gradient. Secondary buttons use ghost styling with wide-tracked 10px text.
- **Cards:** No borders. Backgrounds set to `surface_container_lowest`. Hover states should involve subtle scaling (1.02x) rather than shadow changes.
- **Inputs:** Minimalist bottom-border only or purely tonal backgrounds.
- **The "Editorial Image":** Images should be treated as components. Use grayscale filters by default, transitioning to full color on hover to emphasize "focus and discovery."

## 6. Do's and Don'ts
- **Do:** Use whitespace aggressively. If a section feels crowded, double the padding.
- **Do:** Use italics for emphasis in headlines to create a "designer's note" feel.
- **Don't:** Use rounded corners on anything except "full" pill-shaped elements (like specific status tags).
- **Don't:** Use standard blue for links. Use `primary` or `on_surface` with a bottom-border offset.
- **Do:** Ensure a minimum contrast ratio of 4.5:1, especially when using the Gold `primary` on light backgrounds.