document.getElementById('options-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from submitting the default way

    const params = {
        S: parseFloat(document.getElementById('S').value),
        K: parseFloat(document.getElementById('K').value),
        T: parseFloat(document.getElementById('T').value),
        r: parseFloat(document.getElementById('r').value),
        sigma: parseFloat(document.getElementById('sigma').value),
    };

    fetch(`/api/black_scholes`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('call-price').innerText = `Price: ${data.call_price}`;
        document.getElementById('put-price').innerText = `Price: ${data.put_price}`;
        
        document.getElementById('call-delta').innerText = `Delta: ${data.call_greeks.delta}`;
        document.getElementById('put-delta').innerText = `Delta: ${data.put_greeks.delta}`;
        
        document.getElementById('call-gamma').innerText = `Gamma: ${data.call_greeks.gamma}`;
        document.getElementById('put-gamma').innerText = `Gamma: ${data.put_greeks.gamma}`;
        
        document.getElementById('call-theta').innerText = `Theta: ${data.call_greeks.theta}`;
        document.getElementById('put-theta').innerText = `Theta: ${data.put_greeks.theta}`;
        
        document.getElementById('call-vega').innerText = `Vega: ${data.call_greeks.vega}`;
        document.getElementById('put-vega').innerText = `Vega: ${data.put_greeks.vega}`;
        
        document.getElementById('call-rho').innerText = `Rho: ${data.call_greeks.rho}`;
        document.getElementById('put-rho').innerText = `Rho: ${data.put_greeks.rho}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
