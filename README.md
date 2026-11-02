# WellTrack Cloud

A serverless wellness check-in web application built using Amazon Web Services (AWS).

## Project Overview

WellTrack Cloud allows users to submit wellness check-ins, including mood, water intake, daily steps, sleep, and personal notes.

The project demonstrates how a static website can communicate with a serverless backend and store information in a cloud database.

## AWS Architecture

**Frontend:** HTML, CSS, JavaScript  
**Website Hosting:** Amazon S3 and Amazon CloudFront  
**API:** Amazon API Gateway  
**Backend:** AWS Lambda (Python)  
**Database:** Amazon DynamoDB

### Data Flow

User → CloudFront → S3-hosted frontend → API Gateway → AWS Lambda → DynamoDB

## Features

- Responsive wellness check-in form
- Serverless backend architecture
- REST API integration
- NoSQL database storage
- HTTPS website delivery through CloudFront

## Technical Skills Demonstrated

- AWS cloud architecture
- Serverless application development
- API integration and troubleshooting
- Python backend development
- DynamoDB data storage
- Static website hosting and content delivery
- AWS IAM permissions and access control

## Live Demo

https://d13cayer7xsx98.cloudfront.net

*Demo application. Use fictional information only.*

## Future Improvements

- User authentication with Amazon Cognito
- Wellness trends dashboard
- Infrastructure as Code using Terraform
- Automated deployments with GitHub Actions
- Monitoring and alerting with Amazon CloudWatch

## Project Status

Initial working version completed. Future enhancements planned.
