# Portfolio Optimisation with Python

A small learning exercise for Financial Notes #020 — Portfolio Theory & Optimisation. It uses assumed annual returns, volatilities and correlations for three assets; no market API or dataset is required.

## What it does

- Builds the covariance matrix from volatilities and correlations.
- Calculates the initial portfolio's expected return, variance and volatility.
- Uses SciPy SLSQP to find a minimum variance portfolio, with weights summing to one and no short selling.
- Allocates £10,000 using the optimised weights.
- Finds the minimum risk portfolio for a 12% expected return.
- Solves for 30 target returns and plots the efficient frontier with the minimum variance portfolio marked.

## Inputs

| Asset | Expected annual return | Annual volatility | Initial weight |
|---|---:|---:|---:|
| Tech | 15% | 25% | 40% |
| Consumer | 9% | 15% | 30% |
| Energy | 12% | 20% | 30% |

Correlation matrix, in the same asset order:

```text
[[1.0, 0.3, 0.2],
 [0.3, 1.0, 0.4],
 [0.2, 0.4, 1.0]]
```

## Run locally

From the project folder containing `note20_practice.py` and `requirements.txt`, on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python note20_practice.py
```

The script prints the calculations and opens a Matplotlib plot. Close the plot window to finish. Both chart axes use decimal rates: 0.15 means 15%.

The exercise was verified locally with Python 3.9.6 and the package versions recorded in `requirements.txt`.

## Approximate results

| Portfolio | Expected annual return | Annual volatility |
|---|---:|---:|
| Initial weights | 12.30% | 15.13% |
| Minimum variance | 10.58% | 13.55% |
| Target return of 12% | 12.00% | 14.58% |

The minimum variance allocation is approximately £1,445.65 in Tech, £6,174.41 in Consumer and £2,379.94 in Energy.

The frontier starts at the minimum variance portfolio's expected return and ends at 15%. Each point minimises variance subject to its target expected return. Results describe the assumed inputs, not realised investment performance; transaction costs and estimation uncertainty are outside this exercise.
