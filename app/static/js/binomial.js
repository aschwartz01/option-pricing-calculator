document.getElementById('options-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from submitting the default way

    const S = parseFloat(document.getElementById('S').value);
    const K = parseFloat(document.getElementById('K').value);
    const T = parseFloat(document.getElementById('T').value);
    const r = parseFloat(document.getElementById('r').value);
    const method = document.querySelector('input[name="method"]:checked').value;

    let params;
    let endpoint;

    if (method === 'volatility') {
        const sigma = parseFloat(document.getElementById('sigma').value);
        params = { S, K, T, r, sigma };
        endpoint = '/api/binomial_tree_volatility';
    } else {
        const u = parseFloat(document.getElementById('u').value);
        const d = parseFloat(document.getElementById('d').value);
        params = { S, K, T, r, u, d };
        endpoint = '/api/binomial_tree_uptick_downtick';
    }

    fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Call Price: ${data.call_price}, Put Price: ${data.put_price}, Risk-Neutral Probability: ${data.p}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


