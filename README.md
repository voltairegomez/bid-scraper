# Bid Scraper (Starter)

Compliant-first scraping scaffold for public bid portals.

## Quick Start (using GitHub Codespaces)

1. In this repo, click the green **Code** button → **Codespaces** tab → **Create codespace on main**.
2. Wait for the Codespace (cloud dev environment) to open.
3. In the built-in terminal, run these one at a time:
   ```bash
   pip install -U pip
   pip install -e .
   python -m playwright install chromium
   cp .env.example .env
   bid-scraper run opengov
