const { expect } = require('chai');

const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('promise response from API should resolve', (done) => {
    getPaymentTokenFromAPI(true)
      .then((result) => {
        expect(result).to.eql({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => {
        done(error);
      });
  });
});
