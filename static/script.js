document.getElementById('donate-button').addEventListener('click', function() {
  const donationAmount = parseFloat(document.getElementById('donation-amount').value);
  
  // Check if the donation amount is valid and does not exceed the maximum limit
  if (donationAmount > 0 && donationAmount <= 500) {
      fetch('/api/donation', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ amount: donationAmount }),
      })
      .then(response => response.json())
      .then(data => {
          document.getElementById('total-raised').textContent = data.totalAmount;
          document.getElementById('donation-amount').value = ''; // Clear the input
      })
      .catch(error => {
          console.error('Error:', error);
      });
  } else {
      // Alert the user if the donation is invalid or exceeds the limit
      alert("Please enter a valid donation amount (between 1 and 500).");
  }
});

// Function to fetch and display the current total raised amount on page load
function fetchTotalRaised() {
  fetch('/api/donation')
      .then(response => response.json())
      .then(data => {
          document.getElementById('total-raised').textContent = data.totalAmount;
      })
      .catch(error => {
          console.error('Error:', error);
      });
}

// Call the function when the page loads
window.onload = fetchTotalRaised;

