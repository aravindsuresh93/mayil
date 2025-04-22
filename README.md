# Mayil

A Streamlit-like package for creating structured and formatted emails in Python.

## Installation

```bash
pip install mayil
```

## Usage

```python
from mayil import Mayil

# Create a new email builder instance
my = Mayil()

# Add components to your email
my.header("Welcome to Our Newsletter")
my.text("This is a sample text paragraph.")
my.text("This is another paragraph.")

# Get the complete HTML body
html_content = my.body
```

## Components

### Header
```python
my.header("Your Header Text")
```

### Text
```python
my.text("Your paragraph text")
```

## Features

- Streamlit-like interface for building emails
- HTML-based output
- Styled components
- Chainable methods 