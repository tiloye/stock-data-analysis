import plotly.express as px
import numpy as np
import pandas as pd
import empyrical as ep

def prep_returns(data, log=False):
    if log:
        return data.pct_change().fillna(0).apply(np.log1p)
    else:
        return data.pct_change().fillna(0)

def plot_stats(data, option="price"):
    if option == "price":
        fig = px.line(data, title="<b>Asset Price</b>")
        fig.update_layout(yaxis_title="Price", legend_title_text="Ticker")
        return fig
    elif option == "cum_ret":
        returns = prep_returns(data)
        cum_ret = ep.stats.cum_returns(returns)*100
        fig = px.line(cum_ret, title="<b>Cummulative Returns</b>")
        fig.update_layout(yaxis_title="Cummulative Return (%)", legend_title_text="Ticker")
        return fig
    elif option == "drawdown":
        returns = prep_returns(data)
        dds = ep.stats.drawdown_series(returns)*100
        fig = px.area(dds, title="<b>Daily Drawdown</b>")
        fig.update_layout(yaxis_title="Drawdown (%)", legend_title="Ticker")
        return fig
    elif option == "corr_mat":
        ret_corr = data.corr()
        fig = px.imshow(ret_corr, title="<b>Return Correlation Matrix</b>", text_auto=".2f")
        return fig

def plot_rolling_stats(stats, type="cum_ret"):
    if type == "cum_ret":
        fig = px.line(stats, title="<b>Rolling Cumulative Return</b>")
        fig.update_layout(yaxis_title="Cumulative Return (%)", legend_title_text="Ticker")
        return fig
    elif type == "vol":
        fig = px.line(stats, title="<b>Volatility</b>")
        fig.update_layout(yaxis_title="Volatility (%)", legend_title_text="Ticker")
        return fig
    elif type == "cvar":
        fig = px.line(stats, title="<b>Rolling Conditional Value at Risk (5%)</b>")
        fig.update_layout(yaxis_title="CVAR (%)", legend_title_text="Ticker")
        return fig
    elif type == "sr":
        fig = px.line(stats, title="<b>Rolling Sharpe Ratio</b>")
        fig.update_layout(yaxis_title="Sharpe Ratio", legend_title_text="Ticker")
        return fig

def get_ann_return(returns):
    if isinstance(returns, pd.Series):
        return ep.annual_return(returns)*100
    else:
        return returns.apply(ep.annual_return)*100
    
def get_ann_vol(returns):
    return returns.apply(ep.annual_volatility)*100
    
def get_sharpe_ratio(returns):
    return returns.apply(ep.sharpe_ratio)
    
def get_max_drawdown(returns):
    return -returns.apply(ep.max_drawdown)*100

def get_cvar(returns): # historical cVaR
    return -returns.apply(ep.conditional_value_at_risk)*100
    
def get_summary_df(returns):
    ann_rets = get_ann_return(returns)
    ann_vol = get_ann_vol(returns)
    sr = ep.sharpe_ratio(returns)
    mdd = get_max_drawdown(returns)
    cvar = get_cvar(returns)
    
    
    df = pd.DataFrame(index=returns.columns)
    df["Annual Return"] = ann_rets
    df["Annual Volatility"] = ann_vol
    df["Sharpe Ratio"] = sr
    df["Max Drawdown"] = mdd
    df["Conditional VaR (5%)"] = cvar
    
    return df.round(2)

def get_rolling_stats(returns, window, stat="cum_ret"):
    if stat == "cum_ret":
        return returns.rolling(window).apply(ep.stats.cum_returns_final).dropna() * 100
    elif stat == "vol":
        return returns.rolling(window).std().dropna() * 100
    elif stat == "cvar":
        return -100*returns.rolling(window).apply(ep.conditional_value_at_risk).dropna()
    elif stat == "sr":
        return returns.apply(ep.roll_sharpe_ratio, window=window)
    