# Professional 3D Designer Portfolio - Flask

A stunning, professional portfolio website built with Flask, featuring 3D animations, modern design, and responsive layout. Perfect for college students and creative professionals.

## ✨ Features

- **3D Background Animation** - Interactive Three.js powered 3D geometric shapes
- **Modern Design** - Glass morphism effects with gradient accents
- **Responsive Layout** - Works perfectly on all devices
- **Smooth Animations** - CSS and JavaScript powered animations
- **Interactive Elements** - Project filtering, skill bars, contact form
- **Professional Sections** - Hero, About, Skills, Projects, Experience, Contact
- **Loading Screen** - Elegant loading animation with 3D sphere
- **Mobile Navigation** - Hamburger menu for mobile devices
- **Scroll Effects** - Parallax and scroll-triggered animations

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Flask

### Installation

1. **Clone or download the project**
   ```bash
   # If you have git installed
   git clone <repository-url>
   cd portfolio
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
portfolio/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # All styles and animations
│   ├── js/
│   │   └── main.js       # JavaScript functionality
│   └── images/           # Your portfolio images
└── README.md
```

## 🎨 Customization Guide

### 1. Personal Information
Edit the `portfolio_data` dictionary in `app.py`:

```python
portfolio_data = {
    'name': 'Your Name',
    'title': 'Your Title',
    'email': 'your.email@example.com',
    'phone': '+1 (555) 123-4567',
    'location': 'Your City, State',
    # ... other data
}
```

### 2. About Section
Update the about description and stats:

```python
'about': {
    'description': 'Your personal description here...',
    'stats': [
        {'number': '25+', 'label': 'Projects Completed'},
        {'number': '3+', 'label': 'Years Experience'},
        {'number': '100%', 'label': 'Client Satisfaction'}
    ]
}
```

### 3. Skills
Modify your skills and proficiency levels:

```python
'skills': {
    'categories': [
        {
            'title': 'Your Skill Category',
            'skills': [
                {'name': 'Skill Name', 'proficiency': 90},
                # ... more skills
            ]
        }
    ],
    'software': ['Software 1', 'Software 2', ...]
}
```

### 4. Projects
Add your projects:

```python
'projects': [
    {
        'id': 1,
        'title': 'Project Title',
        'category': 'category_name',
        'description': 'Project description...',
        'image': '/static/images/project1.jpg',
        'technologies': ['Tech 1', 'Tech 2']
    }
]
```

### 5. Experience
Update your work experience:

```python
'experience': [
    {
        'title': 'Job Title',
        'company': 'Company Name',
        'period': '2022 - Present',
        'location': 'City, State',
        'description': 'Job description...',
        'achievements': ['Achievement 1', 'Achievement 2'],
        'technologies': ['Tech 1', 'Tech 2']
    }
]
```

### 6. Social Links
Update your social media links:

```python
'social_links': [
    {'name': 'LinkedIn', 'url': 'https://linkedin.com/in/yourprofile', 'icon': 'linkedin'},
    {'name': 'GitHub', 'url': 'https://github.com/yourusername', 'icon': 'github'},
    # ... more social links
]
```

### 7. Colors and Styling
Customize colors in `static/css/style.css`:

```css
:root {
    --primary-color: #6366f1;      /* Main brand color */
    --secondary-color: #8b5cf6;    /* Secondary color */
    --accent-color: #06b6d4;       /* Accent color */
    --background-dark: #0a0a0a;    /* Dark background */
    /* ... other colors */
}
```

### 8. Adding Images
1. Place your images in `static/images/`
2. Update image paths in the portfolio data
3. Replace placeholder images in the HTML

## 🎯 Sections Overview

### Hero Section
- 3D animated background with floating geometric shapes
- Your name and title with typing effect
- Call-to-action buttons
- Key statistics

### About Section
- Personal photo placeholder
- Detailed description
- Key features/strengths
- Professional highlights

### Skills Section
- Categorized skills with progress bars
- Software and tools proficiency
- Animated skill bars on scroll

### Projects Section
- Filterable project gallery
- Project categories
- Technology tags
- Hover effects and overlays

### Experience Section
- Timeline-based work history
- Company information
- Achievements and technologies used
- Professional timeline design

### Contact Section
- Functional contact form
- Contact information
- Social media links
- Professional layout

## 🔧 Technical Features

### 3D Animation
- Three.js powered 3D background
- Floating geometric shapes
- Smooth camera movement
- Performance optimized

### Responsive Design
- Mobile-first approach
- Tablet and desktop optimized
- Flexible grid layouts
- Touch-friendly interactions

### Performance
- Optimized CSS and JavaScript
- Lazy loading for images
- Smooth scrolling
- Efficient animations

### Accessibility
- Semantic HTML structure
- Keyboard navigation support
- Screen reader friendly
- High contrast ratios

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment

1. **Using PythonAnywhere:**
   - Upload files to your account
   - Set up a new web app
   - Configure WSGI file

2. **Using Heroku:**
   - Create `requirements.txt`: `echo "flask" > requirements.txt`
   - Create `Procfile`: `echo "web: python app.py" > Procfile`
   - Deploy using Heroku CLI

3. **Using Vercel:**
   - Install Vercel CLI
   - Run `vercel` in project directory

4. **Using Netlify:**
   - Build static version
   - Upload to Netlify

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 🎨 Design Features

- **Glass Morphism** - Modern glass effect styling
- **Gradient Accents** - Beautiful color gradients
- **Smooth Animations** - CSS transitions and keyframes
- **3D Elements** - Three.js powered 3D graphics
- **Typography** - Inter font family
- **Icons** - Font Awesome icons
- **Dark Theme** - Professional dark color scheme

## 🔒 Security

- Form validation
- CSRF protection (can be added)
- Input sanitization
- Secure headers

## 📈 SEO Optimization

- Semantic HTML structure
- Meta tags
- Open Graph tags
- Structured data
- Fast loading times

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you need help or have questions:
1. Check the documentation
2. Look at the code comments
3. Create an issue on GitHub

## 🎉 Getting Started Checklist

- [ ] Install Python and Flask
- [ ] Run the application locally
- [ ] Customize personal information
- [ ] Add your projects and experience
- [ ] Update skills and software
- [ ] Add your images
- [ ] Customize colors if needed
- [ ] Test on different devices
- [ ] Deploy to your preferred platform

---

**Made with ❤️ and Flask**

Your professional portfolio is ready to showcase your skills and creativity! 

## 🚀 Deployment on Render

1. Create a new Web Service from your GitHub repo or upload.
2. Environment: Python
3. Build Command:
```
pip install -r requirements.txt
```
4. Start Command:
```
gunicorn app:app --preload --workers 2 --threads 8 --timeout 120 --bind 0.0.0.0:$PORT
```
5. Add environment variables:
- MONGODB_URI: your MongoDB connection string

Alternative: use `render.yaml` as an Infrastructure as Code blueprint. "# protfolio" 
