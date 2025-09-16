# 🏢 HR Hand Receipt Generator (RPWA 28)

A modern, user-friendly web application built with Streamlit that generates professional Hand Receipts (RPWA 28) from Excel data for PWD Electric Division, Udaipur.

## ✨ Features

- **📤 Excel File Upload**: Upload Excel files (.xlsx, .xls) with contractor data
- **🔍 Data Validation**: Automatic validation of required columns and data integrity
- **📄 PDF Generation**: Generate professional PDF receipts using ReportLab
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **⚙️ Customizable Settings**: Adjust maximum receipt count and other parameters
- **📋 Sample Template**: Download sample Excel template for reference
- **🎨 Modern UI**: Clean, intuitive interface with emojis and clear instructions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install -r streamlit_requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

### Windows Users
Simply double-click `run_streamlit.bat` to install dependencies and start the app.

## 📋 Required Excel Format

Your Excel file must contain these columns:

| Column Name | Description | Example |
|-------------|-------------|---------|
| **Payee Name** | Name of the contractor | "John Doe" |
| **Amount** | Payment amount (numeric) | 50000 |
| **Work** | Description of the work | "Electrical Installation" |

## 🎯 How It Works

1. **Upload Excel File**: Drag and drop or browse for your Excel file
2. **Data Validation**: The app checks for required columns and data integrity
3. **Data Preview**: Review your data before processing
4. **Generate PDF**: Click the button to create professional hand receipts
5. **Download**: Get your PDF file ready for printing or distribution

## 🏗️ Architecture

- **Frontend**: Streamlit (Python-based web framework)
- **PDF Generation**: ReportLab (professional PDF library)
- **Data Processing**: Pandas (data manipulation and analysis)
- **Number to Words**: num2words (converts numbers to text)
- **File Handling**: openpyxl (Excel file processing)

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended)
- Free hosting for public repositories
- Automatic deployment from GitHub
- Built-in analytics and monitoring

### 2. Heroku
- Cloud platform with free tier
- Easy deployment with Git integration
- Scalable infrastructure

### 3. Docker
- Containerized deployment
- Consistent environment across platforms
- Easy scaling and management

### 4. Render.com
- Modern cloud platform
- Automatic deployments
- Free tier available

See [STREAMLIT_DEPLOYMENT_GUIDE.md](STREAMLIT_DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

## 🔧 Configuration

### Custom Settings
- **Maximum Receipts**: Limit the number of receipts generated (1-20)
- **File Size Limits**: Configure maximum upload file size
- **PDF Styling**: Customize receipt appearance and layout

### Environment Variables
```bash
# Optional: Set custom port
export STREAMLIT_SERVER_PORT=8502

# Optional: Set custom address
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## 📊 Sample Data

Here's an example of the expected Excel format:

| Payee Name | Amount | Work |
|------------|--------|------|
| John Doe | 50000 | Electrical Installation |
| Jane Smith | 75000 | Transformer Maintenance |
| Bob Johnson | 25000 | Cable Laying |

## 🎨 Customization

### Receipt Template
Modify the `build_pdf_with_reportlab()` function in `streamlit_app.py` to:
- Change layout and styling
- Add new fields
- Modify signature areas
- Update company information

### UI Customization
- Update colors and themes
- Modify sidebar content
- Add new features and widgets
- Customize error messages

## 🔒 Security Features

- **File Validation**: Checks file type and size
- **Data Sanitization**: Cleans input data
- **Temporary Storage**: Files are not permanently stored
- **Error Handling**: Comprehensive error messages and logging

## 📱 Mobile Optimization

- **Responsive Design**: Automatically adapts to screen size
- **Touch-Friendly**: Optimized for mobile devices
- **Fast Loading**: Minimal data transfer
- **Offline Capability**: Works without internet after initial load

## 🚀 Performance Features

- **Efficient Processing**: Optimized data handling
- **Memory Management**: Cleans up temporary files
- **Progress Indicators**: Shows processing status
- **Batch Processing**: Handles multiple receipts efficiently

## 🔍 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Use different port
   streamlit run streamlit_app.py --server.port=8502
   ```

2. **Dependencies Installation Issues**
   ```bash
   # Upgrade pip
   python -m pip install --upgrade pip
   
   # Install with specific Python version
   python3.9 -m pip install -r streamlit_requirements.txt
   ```

3. **PDF Generation Errors**
   - Ensure Excel file has required columns
   - Check that amounts are numeric
   - Verify file permissions

### Getting Help

- Check the [deployment guide](STREAMLIT_DEPLOYMENT_GUIDE.md)
- Review error messages in the application
- Check Python and package versions
- Ensure sufficient disk space for temporary files

## 📈 Future Enhancements

- [ ] User authentication and user management
- [ ] Receipt template customization
- [ ] Batch processing for large files
- [ ] Receipt history and storage
- [ ] Multiple receipt formats
- [ ] API endpoints for integration
- [ ] Advanced reporting features
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **PWD Electric Division, Udaipur** for the receipt format
- **Streamlit** for the amazing web framework
- **ReportLab** for professional PDF generation
- **Pandas** for data processing capabilities

## 📞 Support

For support and questions:
- Check the troubleshooting section above
- Review the deployment guide
- Open an issue on GitHub
- Contact the development team

---

**Made with ❤️ for PWD Electric Division, Udaipur**

*Generate professional hand receipts with ease! 🎉*
