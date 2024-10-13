# SuperDashboard

**SuperDashboard** is an advanced dashboarding application designed for flexibility and interactivity. 

You are an expert in TypeScript, Next.js App Router, React, and Tailwind. Follow @Next.js docs for Data Fetching, Rendering, and Routing.

Use the existing Firebase configuration and utility functions from the codebase. Create any necessary components for the user interface. Replace any existing code in the codebase to transform it into a Dashboard application.

Your job is to create a Super Dashboard following these features:

## Features

1. User authentication using Firebase Auth
- **Softly-Raised Rounded Tiles**
  - Each dashboard item is contained within a softly-raised tile with rounded corners.
  - Each tile is a standalone visualization, allowing for easy editing and updates.
  
- **Variable Tile Sizes**
  - Customize the size of each tile to fit your specific dashboard elements.

- **Interactive Charts**
  - Every tile runs a single query and displays the results as an interactive chart.

- **Drag & Rearrange**
  - Easily drag and rearrange tiles to organize your dashboard layout.

- **Add New Tiles**
  - Use the **Plus** button to create and add new tiles seamlessly.

- **Data Download**
  - Hover over a tile to reveal a three-dot hamburger menu for downloading chart data.

- **Individual Visualization Files**
  - Each tile is a standalone visualization, allowing for easy editing and updates.

- **Secure Backend**
  - Visualization code is managed on the backend, ensuring users cannot modify it directly.

  Data for these visualizations is fetched from Amazon Redshift via SQL queries over a Tailscale connected network.

**Current tech stack**
React with Next.js 14 App Router
TailwindCSS
Firebase Auth, Storage, and Database

**Need to add**
Data Visualization: Python + Bokeh
Database connection: Amazon Redshift connection
Network: Tailscale VPN


