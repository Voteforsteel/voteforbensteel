document.getElementById('donation-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const amount = document.getElementById('amount').value; // Get the amount

    fetch('/donate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ amount: amount }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.total_donations) {
            alert(`Thank you for your donation! Total donations: ${data.total_donations}`);
        } else {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
