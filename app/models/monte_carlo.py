import numpy as np

def monte_carlo_call(S, K, T, r, sigma, num_simulations=10000, num_steps=100):
    dt = T / num_steps
    call_payoffs = []

    for _ in range(num_simulations):
        price_path = [S]
        for _ in range(num_steps):
            Z = np.random.standard_normal()
            S_t = price_path[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
            price_path.append(S_t)
        call_payoffs.append(max(0, price_path[-1] - K))

    call_price = np.exp(-r * T) * np.mean(call_payoffs)
    return call_price
