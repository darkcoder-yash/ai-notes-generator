# 💎 AI Learning Engine - Production Design Specification

## 1. Design System & Tokens

### Color Palette (SaaS AI Aesthetic)
- **Primary (Indigo):** `#1E3A8A` (Deep, trustworthy, professional)
- **Accent (Cyan):** `#06B6D4` (Energetic, modern, AI-themed)
- **Success (Emerald):** `#10B981` (Positive reinforcement)
- **Warning (Amber):** `#F59E0B` (Cautionary/pending)
- **Danger (Rose):** `#EF4444` (Error/High difficulty)
- **Neutral (Gray):**
  - Surface (Light): `#F9FAFB`
  - Surface (Dark): `#0F172A`
  - Border: `#E2E8F0`
- **Text:**
  - Primary: `#111827`
  - Secondary: `#4B5563`
  - Inverted: `#F9FAFB`

### Typography
- **Headings:** `Plus Jakarta Sans` or `Inter` (Bold, 700-800 weight for hierarchy).
- **Body:** `Inter` (Regular, 400 weight for readability).
- **UI Elements:** `Inter` (Medium, 500 weight for labels and buttons).

### Spacing & Grid
- **Base Unit:** 8px (Tailwind-style spacing).
- **Gaps:** 16px (4 units) for cards, 32px (8 units) for sections.
- **Radius:** 12px (Standard for cards), 8px (Buttons).

---

## 2. Layout Architecture

### 3-Layer Implementation
1.  **Global Shell:** Full-height container with a fixed `Sidebar` (Left) and a `TopBar` (Header).
2.  **Navigation Layer:**
    - **Sidebar:** Collapsible menu with high-contrast icons (Lucide/Feather icons).
    - **Header:** Sticky top bar containing search, user stats (XP/Rank), and quick actions.
3.  **Workspace Layer:** Centered modular grid. Content is grouped into "SaaS Cards" with subtle shadows and border-accents.

---

## 3. UI Component Breakdown

### XP Progress Ring (Dashboard)
A SVG-based circular gauge that fills as the user earns XP. Centered inside is the current level percentage.

### Quiz Tile (Game Mode)
Large-format tiles (`width: 100%`) with a 2px border. 
- **Interaction:** On click, the border color transitions to `Primary`. On submission, it flashes `Success` or `Danger`.

### Analytics Grid
Line charts (using `Plotly` or `Recharts`) showing "XP Growth Over Time" and "Accuracy per Topic."

---

## 4. Interaction Logic

- **State Sync:** XP updates are globally synced via a central store (e.g., Redux or Streamlit Session State).
- **Animations:** 
  - **Framer Motion** style transitions (Slide-up-and-fade) for new content.
  - **Confetti/Celebration:** Triggered upon Rank Up or Boss Battle victory.
- **Adaptive Engine:** If accuracy < 60%, the "Next Mission" card automatically suggests a "Foundation" level topic.

---

## 5. Suggested Technical Stack

- **Frontend:** Next.js 14+ (App Router)
- **Styling:** Tailwind CSS + Headless UI / Shadcn UI
- **State Management:** TanStack Query (React Query) + Zustand
- **Animations:** Framer Motion
- **Charts:** Recharts or Chart.js
- **Backend:** FastAPI (Python) or Node.js (TypeScript)
- **AI Integration:** Gemini 2.5 Flash SDK

---

## 6. Layout Wireframe

```text
_________________________________________________________________
| [LOGO] | [SEARCH]            [XP: 450⚡] [RANK: 🥇] [Profile] | (TopBar)
|________|_______________________________________________________|
| Dashboard |                                                    |
| Notes     |   [ DASHBOARD WORKSPACE ]                          |
| Quiz      |                                                    |
| Boss      |   [ XP RING ]  [ ACCURACY CHART ] [ STREAK ]       |
| Speed     |                                                    |
| Analytics |   [ RECENT ACTIVITY ] [ RECOMMENDED MISSIONS ]     |
| Audit     |                                                    |
| Settings  |                                                    | (Sidebar)
|___________|____________________________________________________|
```
