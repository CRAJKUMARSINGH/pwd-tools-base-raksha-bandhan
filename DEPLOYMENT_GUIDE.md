# PWD Tools Deployment Guide

This guide provides step-by-step instructions for deploying PWD Tools on both Vercel and Streamlit Cloud platforms.

## 🚀 Streamlit Cloud Deployment (Recommended)

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at [streamlit.io/cloud](https://streamlit.io/cloud))

### Step-by-Step Deployment

1. **Push Code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit for PWD Tools"
   git push origin main
   ```

2. **Connect to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"

3. **Configure App Settings**
   - **Repository**: Select your `pwd-tools-base-raksha-bandhan` repository
   - **Branch**: `main`
   - **Main file path**: `Excel_se_EMD/streamlit_app.py`
   - **App URL**: Choose a custom subdomain (e.g., `pwd-tools-raksha-bandhan`)

4. **Advanced Settings**
   - **Python version**: 3.9 or higher
   - **Requirements file**: `Excel_se_EMD/requirements.txt`
   - **Command**: Leave empty (uses Procfile)

5. **Deploy**
   - Click "Deploy!"
   - Wait for build to complete
   - Your app will be available at `https://your-app-name.streamlit.app`

### Streamlit Cloud Features
- ✅ Automatic deployments on code changes
- ✅ Free hosting for public repositories
- ✅ Built-in analytics and monitoring
- ✅ Custom domains support
- ✅ Automatic dependency management

## 🌐 Vercel Deployment (Static Tools)

### Prerequisites
- GitHub account
- Vercel account (free at [vercel.com](https://vercel.com))

### Step-by-Step Deployment

1. **Push Code to GitHub** (same as above)

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign in with GitHub
   - Click "New Project"

3. **Import Repository**
   - Select your `pwd-tools-base-raksha-bandhan` repository
   - Vercel will auto-detect it's a static site

4. **Configure Build Settings**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave default)
   - **Build Command**: Leave empty
   - **Output Directory**: `public`

5. **Environment Variables** (if needed)
   - No environment variables required for static hosting

6. **Deploy**
   - Click "Deploy"
   - Wait for build to complete
   - Your static tools will be available at `https://your-project.vercel.app`

### Vercel Features
- ✅ Global CDN for fast loading
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ Automatic deployments
- ✅ Edge functions support (if needed later)

## 🔧 Configuration Files

### Procfile (Streamlit Cloud)
```
web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
```

### vercel.json (Vercel)
```json
{
  "version": 2,
  "cleanUrls": true,
  "trailingSlash": false,
  "public": true,
  "builds": [
    { "src": "public/**", "use": "@vercel/static" }
  ],
  "routes": [
    { "src": "/", "dest": "/public/index.html" },
    { "src": "/tools/(.*)", "dest": "/public/tools/$1" },
    { "src": "/assets/(.*)", "dest": "/src/assets/$1" }
  ]
}
```

### requirements.txt (Streamlit)
```
flask==3.0.0
pandas==2.1.4
jinja2==3.1.2
num2words==0.6.0
openpyxl==3.1.2
gunicorn==21.2.0
pdfkit==1.0.0
streamlit==1.29.0
reportlab==4.0.7
```

## 📱 Post-Deployment

### Streamlit App
- Test all functionality
- Verify PDF generation works
- Check mobile responsiveness
- Monitor performance metrics

### Static Tools (Vercel)
- Test all HTML tools
- Verify navigation works
- Check mobile compatibility
- Test file downloads

## 🚨 Troubleshooting

### Common Issues

#### Streamlit Deployment Fails
- Check Python version compatibility
- Verify requirements.txt syntax
- Ensure main file path is correct
- Check build logs for errors

#### Vercel Build Fails
- Verify vercel.json syntax
- Check if public folder exists
- Ensure all referenced files exist
- Review build logs

#### PDF Generation Issues
- Verify all dependencies are installed
- Check file permissions
- Test locally before deploying
- Review error logs

### Performance Optimization

#### Streamlit
- Use `@st.cache_data` for expensive operations
- Limit file upload sizes
- Implement pagination for large datasets
- Use efficient data structures

#### Vercel
- Optimize image sizes
- Minimize CSS/JS files
- Use CDN for static assets
- Implement lazy loading

## 🔄 Continuous Deployment

### Automatic Updates
Both platforms support automatic deployments:
- **Streamlit**: Updates on every push to main branch
- **Vercel**: Updates on every push to main branch

### Manual Updates
- Push changes to GitHub
- Wait for automatic deployment
- Verify changes are live
- Test functionality

## 📊 Monitoring

### Streamlit Cloud
- Built-in analytics
- Performance metrics
- Error tracking
- User engagement data

### Vercel
- Analytics dashboard
- Performance insights
- Error monitoring
- Real-time metrics

## 🎯 Best Practices

1. **Always test locally** before deploying
2. **Use version control** for all changes
3. **Monitor performance** after deployment
4. **Keep dependencies updated**
5. **Document configuration changes**
6. **Backup important data**
7. **Test on multiple devices**
8. **Monitor error logs regularly**

## 🆘 Support

### Streamlit Cloud
- [Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Community Forum](https://discuss.streamlit.io/)
- [GitHub Issues](https://github.com/streamlit/streamlit)

### Vercel
- [Documentation](https://vercel.com/docs)
- [Community](https://github.com/vercel/vercel/discussions)
- [Support](https://vercel.com/support)

---

**Note**: This deployment guide assumes you have basic knowledge of Git and GitHub. If you need help with Git operations, please refer to [GitHub's Git tutorial](https://docs.github.com/en/get-started/quickstart/git-and-github-learning-resources).
