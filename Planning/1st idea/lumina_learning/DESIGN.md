---
name: Lumina Learning
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#464555'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#831ada'
  on-secondary: '#ffffff'
  secondary-container: '#9e41f5'
  on-secondary-container: '#fffbff'
  tertiary: '#00505f'
  on-tertiary: '#ffffff'
  tertiary-container: '#006a7c'
  on-tertiary-container: '#93e8ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#f0dbff'
  secondary-fixed-dim: '#ddb8ff'
  on-secondary-fixed: '#2c0051'
  on-secondary-fixed-variant: '#6800b4'
  tertiary-fixed: '#acedff'
  tertiary-fixed-dim: '#4cd7f6'
  on-tertiary-fixed: '#001f26'
  on-tertiary-fixed-variant: '#004e5c'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  container-max: 1280px
---

## Brand & Style

The design system is built for an educational environment that balances the rigor of computer science with the approachability of a personal mentor. The aesthetic combines the structural logic of a developer tool with the vibrant, celebratory feedback loops of a modern consumer app.

**Design Style: Modern Technical Minimalist**
The system blends three distinct influences:
- **Structural Integrity:** Borrowing from Linear’s precision, using crisp lines and subtle borders to organize complex information.
- **Vibrant Professionalism:** Utilizing Stripe-inspired gradients and high-saturation accents to highlight key actions and milestones.
- **Tactile Accessibility:** Incorporating Duolingo-style roundedness and large, clear touch targets to reduce the cognitive load of learning AI.

The interface should evoke a sense of "approachable power"—making cutting-edge technology feel like a tool anyone can master.

## Colors

The palette is designed to transition seamlessly between deep focus and celebratory achievement.

- **Primary (Indigo):** Used for core navigation, primary actions, and "Stable AI" concepts.
- **Secondary (Purple):** Reserved for "Generative" or "Creative" features, achievement states, and premium callouts.
- **Neutral:** A deep slate-to-white scale provides the backbone of the UI, ensuring high legibility.
- **Success/Warning/Error:** Follow standard semantic patterns but with increased saturation to match the vibrant primary accents.

**Dark Mode Implementation:**
In dark mode, background surfaces should use a deep #0F172A (Slate 950) rather than pure black. Primary accents should maintain their hex values but gain a subtle outer glow (0 0 12px) to maintain contrast against dark backgrounds.

## Typography

This design system utilizes **Inter** for all UI and prose elements to ensure maximum legibility and a modern, neutral tone. **JetBrains Mono** is introduced as a secondary functional font for technical labels, code snippets, and progress indicators, reinforcing the "AI Academy" context.

- **Headings:** Should always use tighter letter-spacing and bold weights to create a strong visual anchor.
- **Body Text:** Uses generous leading (1.5x - 1.6x) to make long-form educational content easy to digest.
- **Case Usage:** Headlines use sentence case. Labels and small badges may use all-caps with 0.05em tracking for a more "systematized" look.

## Layout & Spacing

The system uses a **Fluid Grid** model with a base unit of 4px. All spacing between elements should be a multiple of 8px (8, 16, 24, 32, 48, 64).

- **Desktop (1280px+):** 12-column grid, 24px gutters, 40px side margins. Content is centered in a max-width container for dashboard views.
- **Tablet (768px - 1279px):** 8-column grid, 20px gutters, 24px side margins.
- **Mobile (<767px):** 4-column grid, 16px gutters, 16px side margins.

**Vertical Rhythm:**
Use large vertical gaps (64px+) between major sections in the learning path to provide "breathing room," preventing the user from feeling overwhelmed by technical information.

## Elevation & Depth

Hierarchy is established through a combination of **Tonal Layers** and **Ambient Shadows**.

- **Level 0 (Base):** White (#FFFFFF) or Slate-950.
- **Level 1 (Cards):** Subtly raised with a soft shadow: `0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)`.
- **Level 2 (Active Elements):** For hover states and modals, use a multi-layered shadow with a subtle primary color tint to simulate a glow.
- **Glassmorphism:** Use `backdrop-filter: blur(12px)` with a 60% opaque white background for navigation bars and floating progress widgets. This keeps the UI feeling light and layered.

## Shapes

The shape language is purposefully friendly. While the layout is structured, the corners are soft to encourage exploration.

- **Standard Elements:** 8px (rounded-md) for input fields and small buttons.
- **Containers:** 16px (rounded-lg) for course cards, module containers, and dashboard widgets.
- **Feature Elements:** 24px (rounded-xl) for hero sections or prominent "Next Lesson" callouts.
- **Interactive:** Use pill-shapes for status chips (e.g., "In Progress", "Completed") to differentiate them from square-ish buttons.

## Components

### Buttons
- **Primary:** Solid #4F46E5 background with white text. High contrast, 8px border radius. On hover, apply a slight upward lift (-1px) and a subtle shadow increase.
- **Secondary:** Subtle #F3F4F6 background (light mode) or #1E293B (dark mode).
- **Learning Action:** Large, centered buttons for "Continue Lesson" should use the Secondary Purple (#9333EA) to differentiate from standard UI navigation.

### Input Fields
- Use a 1px border (#E2E8F0) that transitions to Primary Indigo on focus. Add a 4px soft outer glow in the primary color when focused to enhance the "modern SaaS" feel.

### Cards & Progress
- **Course Cards:** 16px rounded corners, subtle border, and a progress bar at the very bottom edge.
- **Progress Circles:** Use thick strokes (8px+) with rounded caps. The track should be a very faint neutral, and the progress should be a gradient from Primary Indigo to Secondary Purple.

### Chips & Badges
- Small, uppercase labels using JetBrains Mono. Use glassmorphism (blurred backgrounds) for badges that sit on top of images or colorful backgrounds to maintain legibility.

### List Items
- Lesson lists should feature a "Connection Line" (2px dashed neutral) between items to visualize the learning path, inspired by Notion’s clean hierarchy.