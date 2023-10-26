const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;

// Import the sendPaymentRequestToApi function
const sendPaymentRequestToApi = require('./4-payment'); // Update the import

// Import the Utils module (assuming you have it)
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  // Create a stub for Utils.calculateNumber
  let calculateNumberStub;
  // Create a spy for console.log
  let consoleLogSpy;

  beforeEach(() => {
    // Create a stub for Utils.calculateNumber to always return 10
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Create a spy for console.log
    consoleLogSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the stub and the spy
    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });

  it('should call Utils.calculateNumber with type SUM, a = 100, and b = 20', () => {
    const totalAmount = 100;
    const totalShipping = 20;
    sendPaymentRequestToApi(totalAmount, totalShipping);

    // Verify that Utils.calculateNumber was called with the correct arguments
    expect(calculateNumberStub.calledWith('SUM', totalAmount, totalShipping)).to.be.true;
  });

  it('should log the correct message', () => {
    const totalAmount = 100;
    const totalShipping = 20;
    sendPaymentRequestToApi(totalAmount, totalShipping);

    // Verify that console.log was called with the correct message
    expect(consoleLogSpy.calledWith('The total is: 10')).to.be.true;
  });

  // Additional test 1
  it('should log "The total is: 120" and be called once with 100 and 20', () => {
    const totalAmount = 100;
    const totalShipping = 20;
    sendPaymentRequestToApi(totalAmount, totalShipping);

    // Verify that console.log was called with the correct message
    expect(consoleLogSpy.calledWith('The total is: 120')).to.be.true;
    // Verify that console.log was called only once
    expect(consoleLogSpy.calledOnce).to.be.true;
  });

  // Additional test 2
  it('should log "The total is: 20" and be called once with 10 and 10', () => {
    const totalAmount = 10;
    const totalShipping = 10;
    sendPaymentRequestToApi(totalAmount, totalShipping);

    // Verify that console.log was called with the correct message
    expect(consoleLogSpy.calledWith('The total is: 20')).to.be.true;
    // Verify that console.log was called only once
    expect(consoleLogSpy.calledOnce).to.be.true;
  });
});
