# WellTrack Cloud ☁️

### Serverless Wellness Tracking Application Built with AWS

WellTrack Cloud is a serverless web application designed to collect and store daily wellness check-ins.

I developed this project to gain hands-on experience building and deploying applications using Amazon Web Services (AWS).

## Technologies Used

- **Amazon S3:** Static website file storage
- **Amazon CloudFront:** HTTPS content delivery
- **Amazon API Gateway:** REST-style API endpoint using an HTTP API
- **AWS Lambda (Python):** Serverless backend processing
- **Amazon DynamoDB:** NoSQL database storage
- **AWS IAM:** Access management
- **HTML, CSS, JavaScript:** Frontend development

## Application Architecture

User → CloudFront → S3-hosted frontend → API Gateway → AWS Lambda → DynamoDB

## Features

- Wellness check-in form
- Mood, water intake, steps, and sleep tracking
- Serverless API integration
- DynamoDB record storage
- CloudFront HTTPS website delivery

## Live Application

https://d13cayer7xsx98.cloudfront.net

**Note:** This is a demonstration project. Please use fictional information only.

## What I Learned

Through this project, I gained practical experience with:

- Connecting multiple AWS services
- Configuring IAM permissions
- Deploying a serverless application
- Troubleshooting API connectivity and CORS
- Hosting a website using S3 and CloudFront
- Working with Python and JavaScript

## Future Improvements

- Add user authentication using Amazon Cognito
- Build a dashboard to visualize wellness trends
- Automate infrastructure deployment using Terraform
- Add monitoring through Amazon CloudWatch

## Project Status

Initial version deployed. End-to-end form submission and database verification are being finalized.
