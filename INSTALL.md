# Installation Guide - Prefect Body Elections Desktop Application

## Quick Installation

### Step 1: Install Python
1. Download Python 3.11 or higher from [python.org](https://python.org)
2. During installation, **check "Add Python to PATH"**
3. Verify installation by opening Command Prompt/Terminal and typing:
   ```
   python --version
   ```

### Step 2: Install Dependencies
1. Open Command Prompt/Terminal
2. Navigate to the application folder:
   ```
   cd path/to/PrefectElections_Desktop
   ```
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

### Step 3: Run the Application
1. In the same folder, run:
   ```
   python desktop_app_simple.py
   ```
2. Open your web browser and go to: `http://localhost:5003`

## Alternative Installation (Virtual Environment)

### For Advanced Users
1. Create a virtual environment:
   ```
   python -m venv voting_env
   ```
2. Activate it:
   - **Windows**: `voting_env\Scripts\activate`
   - **macOS/Linux**: `source voting_env/bin/activate`
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python desktop_app_simple.py
   ```

## Default Admin Access
- **URL**: `http://localhost:5003/admin.html`
- **Username**: `admin`
- **Password**: `admin123`

## Troubleshooting

### Python Not Found
- Reinstall Python and ensure "Add to PATH" is checked
- Try using `python3` instead of `python`

### Permission Errors
- Run Command Prompt/Terminal as Administrator
- Check folder permissions

### Port Already in Use
- Close other applications using port 5003
- Or modify the port in `desktop_app_simple.py`

## Support
For technical support, refer to `README_DESKTOP.md` for detailed documentation.

