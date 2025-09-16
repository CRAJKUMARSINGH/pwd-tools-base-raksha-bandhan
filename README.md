# PWD Tools - Raksha Bandhan

A comprehensive toolkit for PWD (Public Works Department) operations including receipt generation, financial calculations, and project management tools.

## 🚀 Quick Start (Windows Users)

**For users who are not familiar with command line:**

1. **Double-click** `PWD_Tools_Launcher.bat` in the main folder
2. Choose your preferred application:
   - **Option 1**: Streamlit App (Recommended - Modern Interface)
   - **Option 2**: Flask App (Traditional Web Interface)
   - **Option 3**: Open Tools Folder
3. The batch files will automatically install dependencies and start the application

## 🛠️ Manual Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation
1. Navigate to the `Excel_se_EMD` folder
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Applications

#### Streamlit App (Recommended)
```bash
cd Excel_se_EMD
streamlit run streamlit_app.py
```
- Opens in your default browser
- Modern, responsive interface
- Better for non-technical users

#### Flask App
```bash
cd Excel_se_EMD
python app.py
```
- Available at http://localhost:5000
- Traditional web interface
- Good for integration with other systems

## 🌐 Deployment

### Streamlit Cloud Deployment
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. The `Procfile` is already configured for deployment
4. Streamlit will automatically detect and deploy your app

### Vercel Deployment
1. Push your code to GitHub
2. Connect your repository to [Vercel](https://vercel.com)
3. The `vercel.json` is already configured for static file hosting
4. Vercel will automatically deploy your static tools

## 📁 Project Structure

```
pwd-tools-base-raksha-bandhan/
├── Excel_se_EMD/           # Main application folder
│   ├── app.py              # Flask application
│   ├── streamlit_app.py    # Streamlit application
│   ├── requirements.txt    # Python dependencies
│   └── Procfile           # Streamlit Cloud configuration
├── public/                 # Static web tools
│   ├── index.html         # Main hub page
│   └── tools/             # Individual tool pages
├── *.bat                  # Windows batch files for easy launching
└── vercel.json            # Vercel deployment configuration
```

## 🛠️ Available Tools

### Receipt Generator (RPWA 28)
- Upload Excel files with columns: Payee Name, Amount, Work
- Generate professional PDF receipts
- Supports both Flask and Streamlit interfaces

### Financial Tools
- **Bill Note Sheet**: Generate and view bill note sheets
- **Deductions Table**: Reference table for deductions
- **Delay Calculator**: Compute project delays and metrics
- **Financial Progress Tracker**: Monitor financial progress over time
- **Security Refund Calculator**: Calculate expected security refunds
- **Stamp Duty Calculator**: Compute applicable stamp duty

## 🔧 Technical Features

- **Dual Interface**: Both Flask and Streamlit versions available
- **PDF Generation**: Uses ReportLab for reliable PDF creation
- **Excel Processing**: Handles Excel files with pandas
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Robust error handling and validation
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🐛 Bug Fixes Applied

- Fixed formatting issues in DelayCalculator
- Removed redundant package-lock.json
- Added proper error handling in Python applications
- Optimized requirements.txt with specific versions
- Added user-friendly batch files for Windows users

## 🚀 Performance Optimizations

- Pinned dependency versions for consistent builds
- Added Procfile for Streamlit Cloud deployment
- Optimized Vercel configuration for static hosting
- Implemented proper error handling and validation
- Added caching strategies for Streamlit components

## 📝 Usage Instructions

### For Receipt Generation:
1. Prepare an Excel file with columns: "Payee Name", "Amount", "Work"
2. Upload the file through the web interface
3. Set the maximum number of rows to process
4. Download the generated PDF

### For Financial Calculations:
1. Navigate to the appropriate tool tab
2. Input the required data
3. View results and calculations
4. Use the results for your PWD operations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For technical support or questions:
- Check the documentation above
- Review the batch file instructions
- Ensure Python and dependencies are properly installed

---

**Note**: The batch files (`.bat`) are specifically designed for Windows users to make the application easy to use without command line knowledge. Simply double-click to run!


