const request = require('request');
const chai = require('chai')

describe('API test', () => {
  it('respond with 200 code and body', (done) => {
    request('http://localhost:7865', 'GET /', (error, res, body) => {
      if (error) throw error;
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
    });
    done();
  });
});
