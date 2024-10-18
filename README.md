# Karbon Hackathon Financial Analysis Project

## Overview

This project was developed as part of the Karbon Hackathon Internship. It is a financial analysis tool that processes company financial data from a JSON file, applies specific financial rules, and outputs the results. The project includes a web interface built with Flask, allowing users to upload a financial data file and view the analysis results.

## Features

- Upload financial data in JSON format (`data.json`).
- Perform analysis based on rules defined in `rules.py`.
- Display financial flags such as:
  - Total Revenue Flag
  - Borrowing to Revenue Ratio Flag
  - Interest Service Coverage Ratio (ISCR) Flag

## Technologies

- Python
- Flask
- HTML (Templates for file upload and result display)

## Setup and Usage

### Prerequisites

- Python 3.x
- Flask (`pip install Flask`)

### Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/justinzivpatil/Karbon_Hackathon_Internship.git
   cd Karbon_Hackathon_Internship
