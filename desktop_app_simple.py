#!/usr/bin/env python3
"""
Desktop Application for Prefect Body Elections
The Educators Professional's Campus

This application provides a desktop interface for the voting system,
including both the voting interface and admin panel.
"""

import os
import sys
import signal
import threading
import time

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from src.main import app

class VotingDesktopApp:
    """Desktop application wrapper for the voting system."""
    
    def __init__(self):
        self.app = app
        self.server_thread = None
        self.running = False
        
    def signal_handler(self, signum, frame):
        """Handle shutdown signals."""
        print("\nShutting down the application...")
        self.stop()
        sys.exit(0)
        
    def start_server(self):
        """Start the Flask server in a separate thread."""
        self.app.config['DEBUG'] = False
        self.app.config['TESTING'] = False
        
        try:
            self.app.run(host='0.0.0.0', port=5003, debug=False, use_reloader=False)
        except Exception as e:
            print(f"Error starting server: {e}")
            
    def start(self):
        """Start the desktop application."""
        print("=" * 60)
        print("PREFECT BODY ELECTIONS - DESKTOP APPLICATION")
        print("The Educators Professional's Campus")
        print("=" * 60)
        print()
        print("Starting the voting system...")
        print()
        print("Features:")
        print("• Simplified voting without unique codes")
        print("• Password-protected admin panel")
        print("• Election and candidate management")
        print("• Real-time results and statistics")
        print()
        print("Default Admin Credentials:")
        print("Username: admin")
        print("Password: admin123")
        print()
        print("Access the application at: http://localhost:5003")
        print("To access the admin panel, go to: http://localhost:5003/admin.html")
        print()
        print("Press Ctrl+C to stop the application.")
        print("=" * 60)
        
        # Set up signal handlers
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        
        # Start the server in a separate thread
        self.running = True
        self.server_thread = threading.Thread(target=self.start_server, daemon=True)
        self.server_thread.start()
        
        # Wait for the server to start
        time.sleep(2)
        
        print("✓ Application is running!")
        print("✓ Open your web browser and go to: http://localhost:5003")
        print()
        
        # Keep the main thread alive
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.signal_handler(signal.SIGINT, None)
            
    def stop(self):
        """Stop the application."""
        self.running = False
        if self.server_thread and self.server_thread.is_alive():
            print("Stopping server...")

def main():
    """Main function to run the desktop application."""
    app_instance = VotingDesktopApp()
    app_instance.start()

if __name__ == "__main__":
    main()

