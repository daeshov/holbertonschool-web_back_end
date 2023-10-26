const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('./your-express-app'); // Replace with the actual path to your Express app
const expect = chai.expect;

chai.use(chaiHttp);

describe('API Index Page', () => {
  it('should return the correct status code', (done) => {
    chai
      .request(app)
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200); // You can adjust the status code as needed
        done();
      });
  });

  it('should return the correct result', (done) => {
    chai
      .request(app)
      .get('/')
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system'); // You can adjust the expected result
        done();
      });
  });

  // You can add additional tests as needed
  // For example, you might test the response headers, content type, or other aspects of the API.
});
