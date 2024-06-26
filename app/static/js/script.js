document.getElementById('options-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from submitting the default way

    const model = document.getElementById('model').value;
    const type = document.getElementById('type').value;
    const params = {
        S: parseFloat(document.getElementById('S').value),
        K: parseFloat(document.getElementById('K').value),
        T: parseFloat(document.getElementById('T').value),
        r: parseFloat(document.getElementById('r').value),
        sigma: parseFloat(document.getElementById('sigma').value),
        type: type
    };

    fetch(`/api/${model}_${type}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Price: ${data.price}`;
        if (data.uptick && data.downtick) {
            document.getElementById('uptick').innerText = `Uptick: ${(data.uptick * 100).toFixed(2)}%`;
            document.getElementById('downtick').innerText = `Downtick: ${(data.downtick * 100).toFixed(2)}%`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
