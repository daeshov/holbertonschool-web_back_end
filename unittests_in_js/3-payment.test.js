const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;

// Import the sendPaymentRequestToApi function
const sendPaymentRequestToApi = require('./3-payment');

// Import the Utils module (assuming you have it)
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  // Create a spy for Utils.calculateNumber
  let calculateNumberSpy;

  beforeEach(() => {
    // Create a spy and replace the original calculateNumber function
    calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(() => {
    // Restore the original calculateNumber function
    calculateNumberSpy.restore();
  });

  it('should call Utils.calculateNumber with SUM, totalAmount, and totalShipping', () => {
    // Call the sendPaymentRequestToApi function
    const totalAmount = 100;
    const totalShipping = 20;
    sendPaymentRequestToApi(totalAmount, totalShipping);

    // Verify that Utils.calculateNumber was called with the correct arguments
    expect(calculateNumberSpy.calledWith('SUM', totalAmount, totalShipping)).to.be.true;
  });

  it('should return the correct sum', () => {
    // Call the sendPaymentRequestToApi function
    const totalAmount = 100;
    const totalShipping = 20;
    const result = sendPaymentRequestToApi(totalAmount, totalShipping);

    // Verify that the function returns the correct sum
    expect(result).to.equal(120); // Expected sum: 100 + 20 = 120
  });
});
git add .Utils