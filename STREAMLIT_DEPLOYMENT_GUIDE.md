# PWD Tools - Streamlit Deployment Guide

## 🚀 Deployment Options

This application can be deployed on various platforms that support Streamlit applications.

## 🌐 Supported Deployment Platforms

1. **Streamlit Cloud** (Recommended for easy deployment)
2. **Heroku**
3. **Render**
4. **Railway**
5. **AWS Elastic Beanstalk**
6. **Google Cloud Run**
7. **Azure App Service**

## 📋 Requirements for Deployment

The application requires the following dependencies:
- Python 3.8 or higher
- Streamlit 1.20.0 or higher
- Pandas 1.5.0 or higher
- NumPy 1.21.0 or higher
- OpenPyXL 3.0.0 or higher

These are specified in `streamlit_requirements.txt`.

## 🛠️ Local Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/CRAJKUMARSINGH/pwd-tools-base-raksha-bandhan.git
   cd pwd-tools-base-raksha-bandhan
   ```

2. Install dependencies:
   ```bash
   pip install -r streamlit_requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

## ☁️ Streamlit Cloud Deployment

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Enter the GitHub repository URL: `https://github.com/CRAJKUMARSINGH/pwd-tools-base-raksha-bandhan`
4. Set the main file path: `streamlit_app.py`
5. Click "Deploy"

## 🎨 Application Features

The Streamlit application provides a unified interface for all PWD tools:
- Bill Note Sheet Generator
- Deductions Table Calculator
- Delay Calculator
- Liquidity Damages Calculator
- Security Refund Calculator
- Stamp Duty Calculator

All tools are accessible through a clean, responsive sidebar navigation.

## 📁 Project Structure

```
pwd-tools-base-raksha-bandhan/
├── streamlit_app.py          # Main Streamlit application
├── streamlit_requirements.txt # Streamlit-specific dependencies
├── Procfile                 # Deployment configuration for Heroku/Render
├── public/                  # Static HTML tools
│   ├── index.html          # Main landing page
│   └── tools/              # Individual tool files
│       ├── BillNoteSheet.html
│       ├── DeductionsTable.html
│       ├── DelayCalculator.html
│       ├── LiquidityDamagesCalculator.html
│       ├── SecurityRefund.html
│       └── StampDuty.html
└── README.md               # Project documentation
```

## 🔧 Configuration

The application uses Streamlit's default configuration. For custom settings, you can create a `.streamlit/config.toml` file with your specific configurations.

## 🤝 Support

For technical support or questions:
1. Check the main README.md file
2. Review the documentation in each tool
3. Ensure all dependencies are properly installed
4. Check that HTML files are in the correct locations

## 📄 License

This software is an Initiative by Mrs. Premlata Jain, AAO, PWD, Udaipur, Rajasthan.
Based on prevailing PWF&AR.