# Prefect Body Elections - Desktop Application

## Overview

This is a complete desktop voting application for **The Educators Professional's Campus** prefect body elections. The application has been redesigned to remove the unique code system and instead uses a session-based voting approach suitable for supervised voting in school computer labs.

## Key Features

### ✅ **Simplified Voting System**
- **No unique codes required** - Students can vote directly
- **Session-based voting** - Prevents multiple votes per session
- **Teacher supervision friendly** - Designed for use in computer labs
- **Clean, intuitive interface** - Easy for students to use

### 🔐 **Password-Protected Admin Panel**
- **Secure authentication** - Username and password protection
- **Election management** - Create and manage multiple elections
- **Candidate management** - Add candidates with symbols/images
- **Real-time results** - Live vote counting and statistics

### 🎯 **Election Management Features**
- **Multi-year support** - Create elections for different years
- **Voter count setting** - Set the expected number of voters
- **Candidate symbols** - Upload images for candidate identification
- **Election activation** - Only one election can be active at a time

### 📊 **Results & Analytics**
- **Live vote counting** - Real-time vote tallies
- **Turnout statistics** - Track voting participation
- **Visual results** - Clear presentation of election outcomes
- **Export capabilities** - Results can be viewed and recorded

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Quick Start

1. **Extract the application** to a folder on your computer
2. **Run the desktop application**:
   ```bash
   python desktop_app_simple.py
   ```
3. **Open your web browser** and go to: `http://localhost:5003`

### Default Admin Credentials
- **Username**: `admin`
- **Password**: `admin123`

⚠️ **Important**: Change the default password after first login!

## Usage Guide

### For Students (Voting)

1. **Open the voting page** at `http://localhost:5003`
2. **Click "Start Voting"** to begin a new voting session
3. **Select your preferred candidate** from the list
4. **Click "Cast Vote"** to submit your choice
5. **Confirmation** - You'll see a success message

**Note**: Each computer session allows only one vote. To vote again, the application must be restarted.

### For Administrators

#### Accessing the Admin Panel
1. Go to `http://localhost:5003/admin.html`
2. Login with admin credentials
3. Use the navigation tabs to manage elections

#### Creating a New Election
1. Go to the **Elections** tab
2. Click **"Create New Election"**
3. Fill in:
   - Election name (e.g., "Prefect Body Elections 2025")
   - Year
   - Total number of expected voters
4. Click **"Create Election"**

#### Adding Candidates
1. Go to the **Candidates** tab
2. Select the election from the dropdown
3. Click **"Add Candidate"**
4. Enter candidate name
5. Optionally upload a symbol/image
6. Click **"Add Candidate"**

#### Activating an Election
1. In the **Elections** tab
2. Find your election
3. Click **"Activate"** to make it available for voting

#### Viewing Results
1. Go to the **Results** tab
2. Select the election from the dropdown
3. View live statistics and vote counts

## Technical Specifications

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **RAM**: 512 MB minimum, 1 GB recommended
- **Storage**: 100 MB free space
- **Network**: Local network access (for multiple computers)

### Architecture
- **Backend**: Flask (Python web framework)
- **Database**: SQLite (embedded database)
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Session-based with password hashing

### Security Features
- **Password hashing** using Werkzeug security
- **Session management** to prevent vote manipulation
- **Input validation** on all forms
- **CSRF protection** on admin operations

## File Structure

```
voting-website/
├── desktop_app_simple.py      # Main desktop application
├── src/
│   ├── main.py                # Flask application
│   ├── models/                # Database models
│   │   ├── admin.py          # Admin user model
│   │   ├── election.py       # Election and candidate models
│   │   └── user.py           # Base database configuration
│   ├── routes/               # API endpoints
│   │   ├── admin.py          # Admin authentication
│   │   ├── election.py       # Election management
│   │   └── voting.py         # Voting functionality
│   ├── static/               # Web assets
│   │   ├── index.html        # Main voting page
│   │   ├── admin.html        # Admin panel
│   │   ├── styles.css        # Voting page styles
│   │   ├── admin-styles.css  # Admin panel styles
│   │   ├── script.js         # Voting functionality
│   │   ├── admin-script.js   # Admin panel functionality
│   │   ├── logo.png          # School logo
│   │   └── uploads/          # Candidate symbol storage
│   └── database/             # SQLite database files
└── README_DESKTOP.md         # This documentation
```

## Database Schema

### Tables
- **admin_users**: Admin authentication
- **elections**: Election information
- **candidates**: Candidate details and symbols
- **votes**: Vote records
- **voting_sessions**: Session tracking

## Troubleshooting

### Common Issues

**Q: The application won't start**
- Check that Python 3.11+ is installed
- Ensure no other application is using port 5003
- Try running: `python --version` to verify Python installation

**Q: Can't access the admin panel**
- Verify you're using the correct URL: `http://localhost:5003/admin.html`
- Check the default credentials: admin/admin123
- Clear your browser cache and cookies

**Q: Students can vote multiple times**
- This is expected behavior - each new session allows one vote
- For controlled voting, restart the application between voters
- Consider using separate computers for each voter

**Q: Candidate symbols don't appear**
- Check that image files are in supported formats (PNG, JPG, GIF)
- Ensure images are not too large (recommended: under 1MB)
- Verify the uploads folder has write permissions

### Getting Help

For technical support or questions:
1. Check this documentation first
2. Verify all system requirements are met
3. Try restarting the application
4. Contact your IT administrator if issues persist

## Deployment for School Use

### Single Computer Setup
1. Install the application on one computer
2. Students vote one at a time under teacher supervision
3. Restart application between voters if needed

### Multiple Computer Setup
1. Install on a server computer
2. Other computers access via network: `http://[server-ip]:5003`
3. Ensure all computers are on the same network
4. Configure firewall to allow port 5003

### Best Practices
- **Test before election day** with sample data
- **Backup the database** before starting voting
- **Have a backup plan** in case of technical issues
- **Train staff** on the admin panel before use
- **Monitor voting** throughout the election period

## License & Credits

Developed for **The Educators Professional's Campus**
- School motto: "Commitment, Quality, Dedication"
- Application designed for prefect body elections
- Built with modern web technologies for reliability and ease of use

---

**Version**: 2.0  
**Last Updated**: August 2025  
**Compatible with**: Windows, macOS, Linux

