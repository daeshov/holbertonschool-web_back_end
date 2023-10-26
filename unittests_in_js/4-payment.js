const Utils = require('./utils'); // Import the Utils module (assuming you have it)

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  // Calculate the sum using the Utils.calculateNumber function
  const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);

  // Display the result in the console
  console.log(`The total is: ${sum}`);

  return sum; // Return the sum (optional)
}

module.exports = sendPaymentRequestToApi; // Export the function
