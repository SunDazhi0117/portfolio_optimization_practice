import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

assets = ["Tech","Consumer","Energy"]
mu = np.array([0.15,0.09,0.12])
volatility = np.array([0.25,0.15,0.2])

correlation = np.array([
    [1,0.3,0.2],
    [0.3,1,0.4],
    [0.2,0.4,1]
])

covariance = np.outer(volatility, volatility) * correlation
print(covariance)

covariance_table = pd.DataFrame(covariance, index=assets, columns=assets)
print(covariance_table)
weights = np.array([0.4, 0.3, 0.3])
portfolio_return = weights @ mu
portfolio_variance = weights @ covariance @ weights
portfolio_volatility = np.sqrt(portfolio_variance)
print(portfolio_return, portfolio_variance, portfolio_volatility)

def objective(w):
    return w @ covariance @ w

bounds = [(0, 1), (0, 1), (0, 1)]

def weight_constraint(w):
    return np.sum(w) - 1

constraints = {"type": "eq", "fun": weight_constraint}

result = minimize(
    objective,
    x0=weights,
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)
print(result.success)
print(result.message)
print(result.x)

optimal_weights = result.x

optimal_return = optimal_weights @ mu
optimal_volatility = np.sqrt(optimal_weights @ covariance @ optimal_weights)

allocation = optimal_weights * 10000

print("Optimal return:", optimal_return)
print("Optimal volatility:", optimal_volatility)
print(pd.Series(allocation, index=assets))

target_return = 0.12

def return_constraint(w):
    return w @ mu - target_return

target_constraints = [
    {"type": "eq", "fun": weight_constraint},
    {"type": "eq", "fun": return_constraint}
]

target_result = minimize(
    objective,
    x0=weights,
    method="SLSQP",
    bounds=bounds,
    constraints=target_constraints
)

print(target_result.success)
print(target_result.message)

if target_result.success:
    target_weights = target_result.x
    print(pd.Series(target_weights, index=assets))
    print("Expected return:", target_weights @ mu)
    print("Volatility:", np.sqrt(objective(target_weights)))

target_returns = np.linspace(optimal_return, mu.max(), 30)
print(target_returns)

frontier_volatilities = []

for target_return in target_returns:
    frontier_result = minimize(
        objective,
        x0=optimal_weights,
        method="SLSQP",
        bounds=bounds,
        constraints=target_constraints,
        options={"ftol": 1e-10}
    )

    if not frontier_result.success:
        raise RuntimeError(frontier_result.message)

    risk = np.sqrt(objective(frontier_result.x))
    frontier_volatilities.append(risk)

print(frontier_volatilities)

plt.plot(frontier_volatilities, target_returns, label="Efficient Frontier")

plt.scatter(
    optimal_volatility,
    optimal_return,
    color="red",
    label="Minimum Variance Portfolio"
)

plt.xlabel("Annual Volatility")
plt.ylabel("Expected Annual Return")
plt.title("Portfolio Efficient Frontier")
plt.legend()
plt.grid(True)
plt.show()
