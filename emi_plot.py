import plotly.graph_objs as go

def plot_monthly_breakdown(df_monthly):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_monthly["Month"], y=df_monthly["Principal Paid"], name="Principal Paid"))
    fig.add_trace(go.Scatter(x=df_monthly["Month"], y=df_monthly["Interest Paid"], name="Interest Paid"))
    fig.update_layout(title="Monthly EMI Breakdown", xaxis_title="Month", yaxis_title="Amount")
    return fig

def plot_yearly_breakdown(df_yearly):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_yearly["Year"], y=df_yearly["Principal Paid"], name="Principal Paid"))
    fig.add_trace(go.Bar(x=df_yearly["Year"], y=df_yearly["Interest Paid"], name="Interest Paid"))
    fig.update_layout(barmode='stack', title="Yearly EMI Breakdown", xaxis_title="Year", yaxis_title="Amount")
    return fig
