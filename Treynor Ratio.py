#Imports_and_set_up

from openbb_terminal.sdk import openbb
data = openbb.stocks.load(
    "JPM, SPY",
    start_date="2014-01-01",
    end_date="2022-12-31"
)
#Compute_the_Treynor_ratio
asset = data["Adj Close"].JPM
benchmark = data["Adj Close"].SPY

asset_returns = asset.pct_change().dropna()
benchmark_returns = benchmark.pct_change().dropna()

bm_cov = benchmark_returns.rolling(
    window=30
).cov(asset_returns)

bm_var = benchmark_returns.rolling(
    window=30
).var()

beta = bm_cov / bm_var
treynor = (
    asset_returns - benchmark_returns
) / beta

treynor.plot()