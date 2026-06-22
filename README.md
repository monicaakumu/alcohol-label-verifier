# AI-Powered Alcohol Label Verification App

## Overview

This project is a prototype AI-powered alcohol label verification application developed as a take-home engineering project. The application demonstrates how Optical Character Recognition (OCR) and automated verification can reduce the manual effort required during alcohol label compliance reviews.

The application allows a user to upload an alcohol label image, extracts text using AWS Textract, and compares the extracted text against expected application values.

The system returns either:

* **PASS** – All required fields match.
* **REVIEW** – One or more required fields do not match.

---

# Business Problem

Alcohol label reviewers spend a significant amount of time manually comparing information submitted in an application with information printed on a label.

This prototype automates repetitive verification tasks so reviewers can focus on more complex compliance decisions.

---

# Features

* Upload alcohol label images
* OCR text extraction using AWS Textract
* Brand Name verification
* Class/Type verification
* Alcohol Content verification
* Net Contents verification
* Government Warning verification
* End-to-end verification workflow
* Swagger API documentation

---

# Architecture

```
Label Image
      │
      ▼
FastAPI Upload Endpoint
      │
      ▼
AWS Textract OCR
      │
      ▼
Extracted Text
      │
      ▼
Verification Engine
      │
      ▼
PASS / REVIEW
```

---

# Technologies Used

* Python 3.12
* FastAPI
* AWS Textract
* boto3
* Uvicorn
* Pydantic
* Git
* Terraform
* Ansible
* Swagger/OpenAPI

---

# Installation

Clone the repository.

```bash
git clone https://github.com/monicaakumu/alcohol-label-verifier.git
cd alcohol-label-verifier/backend
```

Create a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Configure AWS credentials.

```bash
aws configure
```

---

# Running the Application

```bash
uvicorn app.main:app --reload --port 8001
```

Swagger UI:

```
http://127.0.0.1:8001/docs
```

---

# Deployment

This application can be deployed to AWS EC2 using the Terraform and Ansible files included in this repository.

## Terraform

From the project root:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Terraform provisions:

* EC2 Instance
* Security Group
* IAM Role for AWS Textract
* IAM Instance Profile
* EC2 Key Pair

## Ansible

Before running the Ansible playbook, update `ansible/inventory.ini` with the public IP address of your EC2 instance.

Example:

```ini
[app]
<EC2_PUBLIC_IP> ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/KUBERNETES-KEY.pem
```

Deploy the application:

```bash
cd ansible
ansible-playbook -i inventory.ini playbook.yml
```

---

# API Endpoints

## GET /

Returns application status.

---

## POST /upload-label

Uploads and stores an image.

---

## POST /extract-text

Extracts OCR text from an uploaded image using AWS Textract.

---

## POST /verify

Verifies OCR text against expected values.

Checks:

* Brand Name
* Class/Type
* Alcohol Content
* Net Contents
* Government Warning

Returns **PASS** or **REVIEW**.

---

## POST /verify-label

Complete end-to-end workflow.

1. Upload image
2. Extract OCR text using AWS Textract
3. Verify required label fields
4. Return PASS or REVIEW

---

# Design Decisions

* AWS Textract was selected for managed OCR capabilities.
* FastAPI was chosen for rapid API development and automatic OpenAPI documentation.
* Terraform was used to provision AWS infrastructure.
* Ansible was used to automate application deployment.
* Verification uses case-insensitive string matching to reduce false mismatches caused by capitalization differences.

---

# Assumptions

* AWS credentials are configured.
* Uploaded label images are readable.
* OCR accuracy depends on image quality.

---

# Current Limitations

* Verification uses text matching and does not perform semantic validation.
* Government Warning verification checks for the presence of the expected warning text but does not validate formatting such as bold text or font size.
* Batch processing is not yet implemented.
* Uploaded files are stored locally on the application server.

---

# Future Enhancements

* Batch label processing
* Fuzzy matching for OCR inaccuracies
* Automatic extraction of all required TTB fields
* Frontend web interface
* Docker containerization
* CI/CD pipeline with GitHub Actions
* Integration with enterprise compliance workflows
