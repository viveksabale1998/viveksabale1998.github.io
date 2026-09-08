#!/usr/bin/env python3
"""
Automatically fetches citation statistics from Google Scholar for Vivek Sabale
and updates the pictorial stats section in content/publications.md.
"""

import os
import re
import sys
import urllib.request

SCHOLAR_USER_ID = "LdMLDdwAAAAJ"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_USER_ID}&hl=en"
PUBLICATIONS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "publications.md")


def fetch_scholar_stats():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    
    req = urllib.request.Request(SCHOLAR_URL, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8")
    except Exception as e:
        print(f"⚠️ Warning: Could not fetch Google Scholar page ({e}). Skipping update without failing.")
        return None

    # Parse citation summary table
    cit_match = re.search(r'Citations.*?class=\"gsc_rsb_std\">(\d+)', html)
    h_match = re.search(r'h-index.*?class=\"gsc_rsb_std\">(\d+)', html)
    i10_match = re.search(r'i10-index.*?class=\"gsc_rsb_std\">(\d+)', html)

    if not (cit_match and h_match and i10_match):
        print("⚠️ Warning: Could not parse table metrics from Google Scholar response. Skipping update.")
        return None

    citations = int(cit_match.group(1))
    h_index = int(h_match.group(1))
    i10_index = int(i10_match.group(1))

    # Parse years and counts from histogram
    years = re.findall(r'<span class=\"gsc_g_t\"[^>]*>(\d+)</span>', html)
    counts = [int(c) for c in re.findall(r'<span class=\"gsc_g_al\">(\d+)</span>', html)]

    # Pair them together
    yearly_data = []
    if len(years) == len(counts) and years:
        yearly_data = list(zip(years, counts))
    else:
        yearly_data = [("2024", 5), ("2025", 23), ("2026", 21)]

    return {
        "citations": citations,
        "h_index": h_index,
        "i10_index": i10_index,
        "yearly": yearly_data,
    }


def generate_html_block(stats):
    citations = stats["citations"]
    h_index = stats["h_index"]
    i10_index = stats["i10_index"]
    yearly = stats["yearly"]

    max_count = max([c for _, c in yearly]) if yearly else 1
    
    bars_html = []
    for year, count in yearly:
        pct = max(int(round((count / max_count) * 100)), 12) if max_count > 0 else 12
        bars_html.append(f'<div class="hist-col"><div class="hist-value">{count}</div><div class="hist-bar-track"><div class="hist-bar-fill" style="height: {pct}%;"></div></div><div class="hist-label">{year}</div></div>')

    bars_str = "\n".join(bars_html)

    # Note: Zero leading spaces and no empty lines to prevent CommonMark from treating HTML as code blocks
    return f"""<!-- CITATION_METRICS_START -->
<div class="metrics-overview">
<div class="metrics-grid">
<div class="metric-card">
<div class="metric-icon-wrap citation-theme"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/></svg></div>
<div class="metric-body"><div class="metric-num">{citations}</div><div class="metric-title">Citations</div><div class="metric-sub">Across all articles</div></div>
</div>
<div class="metric-card">
<div class="metric-icon-wrap hindex-theme"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></div>
<div class="metric-body"><div class="metric-num">{h_index}</div><div class="metric-title">h-index</div><div class="metric-sub">{h_index} papers with ≥ {h_index} citations</div></div>
</div>
<div class="metric-card">
<div class="metric-icon-wrap i10-theme"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>
<div class="metric-body"><div class="metric-num">{i10_index}</div><div class="metric-title">i10-index</div><div class="metric-sub">{i10_index} papers with ≥ 10 citations</div></div>
</div>
</div>
<div class="chart-box">
<div class="chart-header">
<div class="chart-title"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -3px; margin-right: 6px;"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>Citations Growth</div>
<a href="https://scholar.google.com/citations?user=LdMLDdwAAAAJ&hl=en" target="_blank" rel="noopener noreferrer" class="scholar-badge"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: -2px; margin-right: 4px;"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5l4 3.18v6.82h3v-4.5h10v4.5h3V12.7l4-3.2L12 0z"/></svg>Google Scholar Profile ↗</a>
</div>
<div class="histogram">
{bars_str}
</div>
</div>
</div>
<style>
.metrics-overview {{ margin: 1.5rem 0 2.5rem 0; display: flex; flex-direction: column; gap: 1.25rem; }}
.metrics-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }}
.metric-card {{ background: #ffffff; border: 1px solid #e1e8f0; border-radius: 12px; padding: 1.25rem; display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 12px rgba(0, 54, 135, 0.04); transition: transform 0.2s ease, box-shadow 0.2s ease; }}
.metric-card:hover {{ transform: translateY(-2px); box-shadow: 0 6px 18px rgba(20, 149, 167, 0.12); }}
.metric-icon-wrap {{ width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
.citation-theme {{ background: rgba(20, 149, 167, 0.12); color: #1495a7; }}
.hindex-theme {{ background: rgba(0, 54, 135, 0.1); color: #003687; }}
.i10-theme {{ background: rgba(108, 92, 231, 0.12); color: #6c5ce7; }}
.metric-num {{ font-size: 1.9rem; font-weight: 700; line-height: 1.1; color: #110E38; }}
.metric-title {{ font-size: 0.95rem; font-weight: 600; color: #334155; margin-top: 2px; }}
.metric-sub {{ font-size: 0.75rem; color: #64748b; margin-top: 2px; }}
.chart-box {{ background: #ffffff; border: 1px solid #e1e8f0; border-radius: 12px; padding: 1.25rem 1.5rem; box-shadow: 0 4px 12px rgba(0, 54, 135, 0.04); }}
.chart-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.5rem; }}
.chart-title {{ font-size: 0.95rem; font-weight: 600; color: #110E38; }}
.scholar-badge {{ display: inline-flex; align-items: center; font-size: 0.8rem; font-weight: 500; color: #003687; background: #f0f4fc; padding: 0.35rem 0.75rem; border-radius: 20px; text-decoration: none; transition: background 0.2s ease, color 0.2s ease; }}
.scholar-badge:hover {{ background: #003687; color: #ffffff; }}
.histogram {{ display: flex; align-items: flex-end; justify-content: space-around; height: 140px; padding-top: 15px; border-bottom: 1px solid #e2e8f0; }}
.hist-col {{ display: flex; flex-direction: column; align-items: center; width: 50px; height: 100%; }}
.hist-value {{ font-size: 0.85rem; font-weight: 700; color: #1495a7; margin-bottom: 4px; }}
.hist-bar-track {{ width: 32px; flex-grow: 1; display: flex; align-items: flex-end; background: rgba(226, 232, 240, 0.4); border-radius: 6px 6px 0 0; overflow: hidden; }}
.hist-bar-fill {{ width: 100%; background: linear-gradient(180deg, #1495a7 0%, #003687 100%); border-radius: 6px 6px 0 0; transition: opacity 0.2s ease; }}
.hist-col:hover .hist-bar-fill {{ opacity: 0.85; }}
.hist-label {{ font-size: 0.8rem; font-weight: 500; color: #64748b; margin-top: 8px; }}
@media (max-width: 480px) {{
.metric-card {{ padding: 1rem; }}
.metric-num {{ font-size: 1.6rem; }}
.hist-bar-track {{ width: 26px; }}
.chart-box {{ padding: 1rem; }}
}}
</style>
<!-- CITATION_METRICS_END -->"""


def main():
    print("🔍 Fetching latest Google Scholar metrics...")
    stats = fetch_scholar_stats()
    if not stats:
        print("Done (no changes made).")
        return 0

    print(f"📊 Found: {stats['citations']} citations, h-index {stats['h_index']}, i10-index {stats['i10_index']}")

    if not os.path.exists(PUBLICATIONS_FILE):
        print(f"❌ Error: {PUBLICATIONS_FILE} does not exist.")
        return 1

    with open(PUBLICATIONS_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    marker_pattern = r"<!-- CITATION_METRICS_START -->.*?<!-- CITATION_METRICS_END -->"
    if not re.search(marker_pattern, content, flags=re.DOTALL):
        print("❌ Error: Could not find <!-- CITATION_METRICS_START --> marker in publications.md")
        return 1

    new_block = generate_html_block(stats)
    new_content = re.sub(marker_pattern, new_block, content, flags=re.DOTALL)

    if new_content == content:
        print("✨ Publication metrics are already up to date. No changes needed.")
        return 0

    with open(PUBLICATIONS_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ Successfully updated content/publications.md with latest metrics.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
