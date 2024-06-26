import numpy as np

def binomial_tree_call(S, K, T, r, u, d, N=100):
    dt = T / N
    p = (np.exp(r * dt) - d) / (u - d)
    discount_factor = np.exp(-r * dt)

    print(f"dt: {dt}, p: {p}, discount_factor: {discount_factor}")

    # Initialize asset prices at maturity
    asset_prices = np.zeros(N + 1)
    option_values = np.zeros(N + 1)
    for j in range(N + 1):
        asset_prices[j] = S * (u ** (N - j)) * (d ** j)
    print(f"Asset prices at maturity: {asset_prices}")

    # Calculate option values at maturity
    for j in range(N + 1):
        option_values[j] = max(0, asset_prices[j] - K)
    print(f"Option values at maturity: {option_values}")

    # Step back through the tree
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            option_values[j] = discount_factor * (p * option_values[j] + (1 - p) * option_values[j + 1])
        print(f"Option values at step {i}: {option_values[:i+1]}")

    price = option_values[0]
    return price, p

def binomial_tree_put(S, K, T, r, u, d, N=100):
    dt = T / N
    p = (np.exp(r * dt) - d) / (u - d)
    discount_factor = np.exp(-r * dt)

    print(f"dt: {dt}, p: {p}, discount_factor: {discount_factor}")

    # Initialize asset prices at maturity
    asset_prices = np.zeros(N + 1)
    option_values = np.zeros(N + 1)
    for j in range(N + 1):
        asset_prices[j] = S * (u ** (N - j)) * (d ** j)
    print(f"Asset prices at maturity: {asset_prices}")

    # Calculate option values at maturity
    for j in range(N + 1):
        option_values[j] = max(0, K - asset_prices[j])
    print(f"Option values at maturity: {option_values}")

    # Step back through the tree
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            option_values[j] = discount_factor * (p * option_values[j] + (1 - p) * option_values[j + 1])
        print(f"Option values at step {i}: {option_values[:i+1]}")

    price = option_values[0]
    return price, p