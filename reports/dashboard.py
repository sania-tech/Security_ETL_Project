import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
reports = os.path.join(base_dir, "reports")

# Load all CSV files
df_failed    = pd.read_csv(f"{reports}/failed_logins.csv")
df_ips       = pd.read_csv(f"{reports}/suspicious_ips.csv")
df_risk      = pd.read_csv(f"{reports}/risk_summary.csv")
df_activity  = pd.read_csv(f"{reports}/login_activity.csv")
df_kpi       = pd.read_csv(f"{reports}/kpi_summary.csv")

# KPI values
total_events  = int(df_kpi["total_events"].values[0])
total_failed  = int(df_kpi["total_failed"].values[0])
total_success = int(df_kpi["total_success"].values[0])
high_risk     = int(df_kpi["high_risk_events"].values[0])

# Colors
BG        = "#0D1117"
CARD_BG   = "#161B22"
ACCENT1   = "#00D4FF"
ACCENT2   = "#FF4B6E"
ACCENT3   = "#00FF88"
ACCENT4   = "#FFB800"
TEXT      = "#FFFFFF"
SUBTEXT   = "#8B949E"
GRID      = "#21262D"

fig = make_subplots(
    rows=4, cols=3,
    specs=[
        [{"type": "indicator"}, {"type": "indicator"}, {"type": "indicator"}],
        [{"type": "xy", "colspan": 2}, None, {"type": "domain"}],
        [{"type": "xy", "colspan": 3}, None, None],
        [{"type": "table", "colspan": 3}, None, None],
    ],
    row_heights=[0.15, 0.28, 0.28, 0.29],
    vertical_spacing=0.06,
    horizontal_spacing=0.05,
    subplot_titles=(
        "", "", "",
        "Failed Logins Per User", "", "Risk Distribution",
        "Login Activity Over Time",
        "Suspicious IP Addresses"
    )
)

# ── KPI Cards ──────────────────────────────────────────────
fig.add_trace(go.Indicator(
    mode="number+delta",
    value=total_events,
    title={"text": "TOTAL EVENTS", "font": {"size": 13, "color": SUBTEXT}},
    number={"font": {"size": 36, "color": ACCENT1}, "prefix": ""},
    delta={"reference": 450, "valueformat": ".0f", "increasing": {"color": ACCENT3}},
), row=1, col=1)

fig.add_trace(go.Indicator(
    mode="number+delta",
    value=total_failed,
    title={"text": "FAILED LOGINS", "font": {"size": 13, "color": SUBTEXT}},
    number={"font": {"size": 36, "color": ACCENT2}},
    delta={"reference": 120, "valueformat": ".0f", "increasing": {"color": ACCENT2}},
), row=1, col=2)

fig.add_trace(go.Indicator(
    mode="number+delta",
    value=high_risk,
    title={"text": "HIGH RISK EVENTS", "font": {"size": 13, "color": SUBTEXT}},
    number={"font": {"size": 36, "color": ACCENT4}},
    delta={"reference": 90, "valueformat": ".0f", "increasing": {"color": ACCENT2}},
), row=1, col=3)

# ── Bar Chart — Failed logins per user ────────────────────
colors = [ACCENT2 if i < 3 else ACCENT1 for i in range(len(df_failed))]
fig.add_trace(go.Bar(
    x=df_failed["user"],
    y=df_failed["failed_count"],
    marker=dict(
        color=colors,
        line=dict(width=0),
        opacity=0.9,
    ),
    text=df_failed["failed_count"],
    textposition="outside",
    textfont=dict(color=TEXT, size=11),
    hovertemplate="<b>%{x}</b><br>Failed logins: %{y}<extra></extra>",
    showlegend=False,
), row=2, col=1)

# ── Pie Chart — Risk distribution ─────────────────────────
risk_colors = {
    "high":   ACCENT2,
    "medium": ACCENT4,
    "none":   ACCENT3,
    "low":    ACCENT1,
}
pie_colors = [risk_colors.get(r, ACCENT1) for r in df_risk["risk_level"]]

fig.add_trace(go.Pie(
    labels=df_risk["risk_level"].str.upper(),
    values=df_risk["total"],
    marker=dict(colors=pie_colors, line=dict(color=BG, width=2)),
    textfont=dict(color=TEXT, size=12),
    hovertemplate="<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>",
    hole=0.5,
    pull=[0.05 if r == "high" else 0 for r in df_risk["risk_level"]],
), row=2, col=3)

# ── Line Chart — Login activity over time ─────────────────
fig.add_trace(go.Scatter(
    x=df_activity["date"],
    y=df_activity["total_logins"],
    name="Total",
    mode="lines+markers",
    line=dict(color=ACCENT1, width=2.5, shape="spline"),
    marker=dict(size=5, color=ACCENT1),
    fill="tozeroy",
    fillcolor="rgba(0,212,255,0.08)",
    hovertemplate="<b>%{x}</b><br>Total: %{y}<extra></extra>",
), row=3, col=1)

fig.add_trace(go.Scatter(
    x=df_activity["date"],
    y=df_activity["failed_logins"],
    name="Failed",
    mode="lines+markers",
    line=dict(color=ACCENT2, width=2.5, shape="spline"),
    marker=dict(size=5, color=ACCENT2),
    fill="tozeroy",
    fillcolor="rgba(255,75,110,0.08)",
    hovertemplate="<b>%{x}</b><br>Failed: %{y}<extra></extra>",
), row=3, col=1)

fig.add_trace(go.Scatter(
    x=df_activity["date"],
    y=df_activity["success_logins"],
    name="Success",
    mode="lines+markers",
    line=dict(color=ACCENT3, width=2.5, shape="spline"),
    marker=dict(size=5, color=ACCENT3),
    fill="tozeroy",
    fillcolor="rgba(0,255,136,0.08)",
    hovertemplate="<b>%{x}</b><br>Success: %{y}<extra></extra>",
), row=3, col=1)

# ── Table — Suspicious IPs ────────────────────────────────
top_ips = df_ips.head(10)
row_colors = [
    [ACCENT2 if i < 2 else CARD_BG for i in range(len(top_ips))],
    [ACCENT2 if i < 2 else CARD_BG for i in range(len(top_ips))],
]

fig.add_trace(go.Table(
    header=dict(
        values=["<b>IP ADDRESS</b>", "<b>FAILED LOGINS</b>"],
        fill_color=ACCENT1,
        font=dict(color=BG, size=13),
        align="center",
        height=35,
    ),
    cells=dict(
        values=[top_ips["ip_address"], top_ips["failed_count"]],
        fill_color=row_colors,
        font=dict(
            color=[
                [TEXT if i < 2 else SUBTEXT for i in range(len(top_ips))],
                [TEXT if i < 2 else SUBTEXT for i in range(len(top_ips))],
            ],
            size=12,
        ),
        align="center",
        height=30,
    ),
), row=4, col=1)

# ── Global layout ─────────────────────────────────────────
fig.update_layout(
    title=dict(
        text="🛡️  SECURITY LOG MONITORING DASHBOARD",
        font=dict(size=22, color=TEXT, family="Arial Black"),
        x=0.5,
        xanchor="center",
        y=0.98,
    ),
    paper_bgcolor=BG,
    plot_bgcolor=BG,
    font=dict(color=TEXT, family="Arial"),
    height=950,
    margin=dict(t=60, b=20, l=30, r=30),
    legend=dict(
        bgcolor=CARD_BG,
        bordercolor=GRID,
        borderwidth=1,
        font=dict(color=TEXT, size=11),
    ),
    annotations=[
        dict(
            text="Security_ETL_Project  |  sania-tech  |  2026",
            x=0.5, y=-0.01,
            xref="paper", yref="paper",
            showarrow=False,
            font=dict(size=10, color=SUBTEXT),
        )
    ],
)

# Style all XY axes
for row in [2, 3]:
    fig.update_xaxes(
        gridcolor=GRID, zeroline=False,
        tickfont=dict(color=SUBTEXT, size=10),
        linecolor=GRID, row=row, col=1,
    )
    fig.update_yaxes(
        gridcolor=GRID, zeroline=False,
        tickfont=dict(color=SUBTEXT, size=10),
        linecolor=GRID, row=row, col=1,
    )

# Style subplot titles
for ann in fig.layout.annotations:
    ann.font.color = SUBTEXT
    ann.font.size  = 12

# Save and open
output = os.path.join(reports, "dashboard.html")
fig.write_html(
    output,
    include_plotlyjs=True,
    config={"displayModeBar": True, "scrollZoom": True},
)
print("=" * 40)
print("DASHBOARD CREATED!")
print("=" * 40)
print(f"Saved to: reports/dashboard.html")
print("Opening in your browser now...")

import webbrowser
webbrowser.open(f"file://{output}")
