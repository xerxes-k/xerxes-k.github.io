document.addEventListener('DOMContentLoaded', function () {
    const currencySelect = document.querySelector('#currency');
    const resultDiv = document.querySelector('#result');

    // Fetch the list of available currencies and populate the dropdown
    fetch('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json')
        .then(response => response.json())
        .then(data => {
            // Clear the existing options
            currencySelect.innerHTML = '';

            // Populate the dropdown with currencies
            for (const [code, name] of Object.entries(data)) {
                const option = document.createElement('option');
                option.value = code;
                option.textContent = `${name} (${code.toUpperCase()})`;
                currencySelect.appendChild(option);
            }
        })
        .catch(error => {
            console.error('Error fetching currencies:', error);
            resultDiv.innerHTML = 'An error occurred while loading currencies. Please try again.';
        });

    // Handle form submission
    document.querySelector('#currency-form').onsubmit = function (event) {
        event.preventDefault(); // Prevent form from reloading the page

        const selectedCurrency = currencySelect.value;

        if (!selectedCurrency) {
            resultDiv.innerHTML = 'Please select a currency.';
            return;
        }

        // Fetch the exchange rate for the selected currency
        fetch(`https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json`)
            .then(response => response.json())
            .then(data => {
                const rate = data.usd[selectedCurrency];
                resultDiv.innerHTML = `1 USD is equal to ${rate.toFixed(2)} ${selectedCurrency.toUpperCase()}.`;
            })
            .catch(error => {
                console.error('Error fetching exchange rate:', error);
                resultDiv.innerHTML = 'An error occurred. Please try again.';
            });
    };
});
