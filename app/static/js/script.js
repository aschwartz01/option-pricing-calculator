document.getElementById('options-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const model = document.getElementById('model').value;
    const params = {
        S: parseFloat(document.getElementById('S').value),
        K: parseFloat(document.getElementById('K').value),
        T: parseFloat(document.getElementById('T').value),
        r: parseFloat(document.getElementById('r').value),
        sigma: parseFloat(document.getElementById('sigma').value)
    };
    fetch(`/${model}_call`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Call Price: ${data.call_price}`;
    });
});
