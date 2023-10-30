const kue = require('kue');
const queue = kue.createQueue();

// Function to send a notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Set up the queue process to listen to new jobs on "push_notification_code"
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done(); // Acknowledge the job is completed
});
