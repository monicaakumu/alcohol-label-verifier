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
* Swagger/OpenAPI

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
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

Returns PASS or REVIEW.

---

## POST /verify-label

Complete workflow.

1. Upload image
2. Extract OCR text
3. Verify label fields
4. Return PASS or REVIEW

---

# Design Decisions

* AWS Textract was selected for managed OCR capabilities.
* FastAPI was chosen for rapid API development and automatic OpenAPI documentation.
* Verification is implemented using case-insensitive string comparison to reduce false mismatches caused by capitalization differences.

---

# Assumptions

* AWS credentials are already configured.
* Uploaded images are readable.
* OCR quality depends on image quality.

---

# Current Limitations

* Verification is based on text matching.
* Government Warning verification checks the presence of the supplied warning text but does not validate formatting such as font size or bold text.
* Batch processing is not implemented.
* The application currently stores uploaded files locally.

---

# Future Enhancements

* Batch label processing
* Automatic detection of all required TTB fields
* Improved fuzzy matching for OCR errors
* Frontend web interface
* Cloud deployment with persistent object storage
* Integration with enterprise compliance workflows

