import plotly.graph_objs as go

def plot_monthly_breakdown(df_monthly):
    fig = go.Figure()

    # Remaining Balance
    fig.add_trace(go.Scatter(
        x=df_monthly["Month"],
        y=df_monthly["Remaining Balance"],
        name="Remaining Balance",
        mode="lines",
        line=dict(color="blue", width=3)
    ))

    fig.update_layout(
        title="📊 Monthly Balance Trend",
        xaxis_title="Month",
        yaxis_title="Remaining Balance (₹)",
        legend=dict(title="Component", orientation="h", x=0.5, xanchor="center", y=-0.2),
        hovermode="x unified",
        template="plotly_white",
        margin=dict(t=60, b=60)
    )

    return fig
