const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '123-456-7890',
  message: 'This is a test notification',
};

// Create a job in the "push_notification_code" queue
const job = queue.create('push_notification_code', jobData);

// When the job is created without error
job
  .on('complete', () => {
    console.log(`Notification job completed`);
  })
  .on('failed', () => {
    console.log(`Notification job failed`);
  })
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Error creating job:', err);
    }
  });
