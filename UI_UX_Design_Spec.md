# 🎨 AI Learning Engine - UI/UX Design Specification

## 1. Complete Layout Structure

**Theme:** Professional AI Platform, Minimalist SaaS
**Mode:** Dual Mode (Light & Soft Dark)

### Top Navigation Bar (Header)
- **Left:** Logo & App Name ("AI Learning Engine" in bold sans-serif)
- **Center:** Global Search / Topic Quick-jump
- **Right:** 
  - Theme Toggle (☀️/🌙)
  - Rank Badge (e.g., "Rookie Explorer 🥉")
  - XP Counter (e.g., "⚡ 120 XP")
  - User Profile Avatar

### Left Sidebar (Collapsible)
- **Menu Items:**
  - 📝 Generate Notes
  - 🎮 Start Quiz
  - ⚔️ Boss Battle
  - ⏳ Speed Round
  - 📊 Progress Dashboard
  - 🏆 Leaderboard
  - 🔓 Unlock Topics
  - ⚙️ Settings
- **Footer:** Logout / Help

### Main Content Area (Dynamic)
- Fluid container, max-width bounded for readability.
- Content changes based on the sidebar selection.

---

## 2. UI Component Breakdown

### Dashboard Cards
- **Stat Cards:** Clean white/dark-gray boxes with subtle shadow, displaying XP, Rank, Streak.
- **Progress Bar:** Horizontal smooth bar showing XP needed for the next rank.

### Quiz Interface
- **Question Card:** Centered, large legible font.
- **Option Buttons:** Block-style buttons that highlight on hover and indicate correct/incorrect states upon selection.
- **Timer:** Circular progress ring or sleek linear top-bar timer.

### Leaderboard Table
- **Data Grid:** Clean lines, alternate row shading.
- **Top 3 Highlight:** Gold, Silver, and Bronze subtle background tints or border highlights for the top 3 users.

### Feedback Panel
- **Summary:** Animated circular chart showing accuracy.
- **Action Buttons:** "Retry Level", "Next Topic", "Review Notes".

---

## 3. Suggested CSS Styling Rules

```css
:root {
  /* Colors */
  --primary-blue: #1E3A8A; /* Deep Indigo */
  --secondary-teal: #0D9488; /* Soft Teal Accent */
  --bg-light: #F9FAFB;
  --bg-dark: #111827;
  --surface-light: #FFFFFF;
  --surface-dark: #1F2937;
  --text-main-light: #111827;
  --text-main-dark: #F3F4F6;
  --text-muted: #6B7280;
  
  /* Spacing */
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  
  /* Borders */
  --border-radius-md: 8px;
  --border-radius-lg: 12px;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
}

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background-color: var(--bg-light);
  color: var(--text-main-light);
  transition: background-color 0.3s ease;
}

/* Card Styling */
.card {
  background: var(--surface-light);
  border-radius: var(--border-radius-lg);
  padding: var(--spacing-lg);
  box-shadow: var(--shadow-sm);
  border: 1px solid #E5E7EB;
}

/* Buttons */
.btn-primary {
  background-color: var(--primary-blue);
  color: white;
  border-radius: var(--border-radius-md);
  padding: var(--spacing-md) var(--spacing-lg);
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: transform 0.1s, box-shadow 0.2s;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}
```

---

## 4. Color Palette with Hex Codes

| Role | Color Name | Hex Code | Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Deep Indigo | `#1E3A8A` | Main buttons, Header text, Active states |
| **Secondary** | Soft Teal | `#0D9488` | Accents, Progress bars, Success states |
| **Background (Light)** | Light Gray | `#F9FAFB` | App background |
| **Surface (Light)** | Pure White | `#FFFFFF` | Cards, Modals, Dropdowns |
| **Text (Dark)** | Dark Gray | `#111827` | Primary typography |
| **Text (Muted)** | Cool Gray | `#6B7280` | Subtitles, placeholders |
| **Error/Alert** | Soft Red | `#EF4444` | Incorrect answers, warnings |

---

## 5. Button Style Guidelines

1. **Primary Action (Start Quiz, Generate Notes):** Solid fill (`--primary-blue`), white text, medium border radius.
2. **Secondary Action (Settings, Cancel):** Outline or ghost button with `--primary-blue` text.
3. **Quiz Options:** Large block buttons taking up 100% width of their container. Gray outline by default, turns `--primary-blue` on hover, `--secondary-teal` on correct, `--error-red` on incorrect.
4. **Navigation Links:** Ghost buttons with no background until hovered. Active state gets a light `--secondary-teal` background.

---

## 6. Font Recommendations

- **Primary Typeface:** `Inter` or `Roboto`. (Clean, highly legible sans-serif for UI elements and data).
- **Secondary/Heading Typeface:** `Plus Jakarta Sans` or `Poppins`. (Gives a slightly more structural, modern tech feel to headers).
- **Monospace (for code/notes):** `Fira Code` or `JetBrains Mono`.

---

## 7. Layout Wireframe Explanation

**Desktop View:**
The screen is divided into a permanent Top Bar (60px height) and a two-column body. 
The left column (Sidebar) is fixed at 250px width, containing the main vertical navigation menu. 
The right column (Main Content) takes up the remaining viewport width, centered with a maximum width of around 1200px to ensure text doesn't span too far and become hard to read.

**Mobile View:**
The sidebar becomes a hamburger menu accessible from the Top Bar. Dashboard stats stack vertically instead of horizontally. Quiz option buttons take up the full width of the screen.

**Interactions:**
Transitions between views (Dashboard -> Quiz) should feature a subtle fade-in. Hovering over a quiz option slightly lifts the button. Progress bars animate smoothly from 0 to their current value on load.
