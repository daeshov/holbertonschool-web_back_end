const kue = require('kue');
const queue = kue.createQueue();

// Create an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send a notification
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    job.failed(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Set up the queue for "push_notification_code_2" with concurrent processing of 2 jobs
queue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(
        job.data.phoneNumber,
        job.data.message,
        job,
        done
      );
});
