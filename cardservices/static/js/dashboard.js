
document.addEventListener('DOMContentLoaded', (event) => {
    const userName = localStorage.getItem('userName');
    if (userName) {
        document.getElementById('userNameDisplay').innerText = userName;
    }
});

async function fetchVisaStockPrice(apiKey) {
    const apiUrl = `https://api.polygon.io/v1/last/stocks/V?apiKey=${apiKey}`;
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        // Ensure this path matches the structure of your API response
        return data.results[0].price; 
    } catch (error) {
        console.error('Error fetching Visa stock price:', error);
        return 'Unavailable';
    }
}

// Usage
fetchVisaStockPrice('aesCHZ44Ti9JRVsT52LpthpqtMKtJ8q2').then(price => {
    document.getElementById('visaPrice').textContent = price;
});