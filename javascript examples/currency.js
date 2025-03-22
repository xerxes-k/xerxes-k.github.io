document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {
        fetch('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json')
        .then(response => response.json())
        .then(data => {
            // console.log(data.usd.krw);
            // Get rate from data
            const currency = document.querySelector('#currency').value
            const rate = data.usd[currency];
            if (rate !== undefined) {
                document.querySelector('#result').innerHTML = `1 USD is equal to ${rate.toFixed(2)} KRW.`;
            }
            else {
                document.querySelector('#result').innerHTML = 'invalid currency';
            }
        }).catch(error => {
            console.log('Error:', error);
        });
        return false;
    }
});