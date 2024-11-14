# Import necessary libraries for Flask, database handling, password security, etc.
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user

# Set up the Flask app and database connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.secret_key = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Initialize LoginManager to handle user authentication
login_manager = LoginManager()
login_manager.init_app(app)

# Define the User model, representing users in the system
class User(UserMixin, db.Model):
    """
    User model for the platform.
    - Stores information about each user (username, password)
    - Passwords are hashed for security.
    """
    id = db.Column(db.Integer, primary_key=True)  # User ID
    username = db.Column(db.String(150), unique=True, nullable=False)  # Unique username
    password = db.Column(db.String(150), nullable=False)  # Password field, needs to be hashed

# Load user for Flask-Login to identify users during sessions
@login_manager.user_loader
def load_user(user_id):
    """
    Load a user based on their unique user_id.
    """
    return User.query.get(int(user_id))

# Define route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login.
    - Checks user credentials and logs them in if valid.
    - Redirects to the dashboard on successful login.
    """
    if request.method == 'POST':
        username = request.form['username']  # Get username from form
        password = request.form['password']  # Get password from form
        user = User.query.filter_by(username=username).first()  # Check if user exists
        if user and check_password_hash(user.password, password):  # Verify password hash
            login_user(user)  # Log the user in
            return redirect(url_for('dashboard'))  # Redirect to dashboard
    return render_template('login.html')  # Render login page if GET request

# Define route for logging out
@app.route('/logout')
def logout():
    """
    Logs the user out and redirects them to the login page.
    """
    logout_user()  # Logout the current user
    return redirect(url_for('login'))  # Redirect to login page

# Define the Feed model to store RSS feed information submitted by users
class RSSFeed(db.Model):
    """
    Model to represent an RSS feed.
    - Stores URL, title, description, and associated user.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique feed ID
    title = db.Column(db.String(150), nullable=False)  # Title of the feed
    url = db.Column(db.String(250), unique=True, nullable=False)  # Feed URL (should be unique)
    description = db.Column(db.String(500), nullable=True)  # Description of the feed
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # User who submitted the feed

def parse_rss(url):
    """
    Parses the RSS feed from a given URL and returns the feed's title and description.
    Uses the feedparser library to parse the feed.
    """
    feed = feedparser.parse(url)  # Parse the RSS URL
    feed_title = feed.feed.get("title", "No Title")  # Get the feed's title
    feed_description = feed.feed.get("description", "No Description")  # Get the feed's description
    return feed_title, feed_description  # Return the parsed data

# Define the route for submitting RSS feeds
@app.route('/submit_feed', methods=['GET', 'POST'])
@login_required  # Only authenticated users can submit feeds
def submit_feed():
    """
    Handles the submission of an RSS feed.
    - Parses the provided URL and saves the feed to the database.
    """
    if request.method == 'POST':
        url = request.form['url']  # Get the RSS URL from the form
        title, description = parse_rss(url)  # Parse the RSS feed
        new_feed = RSSFeed(title=title, url=url, description=description, user_id=current_user.id)  # Create new feed
        db.session.add(new_feed)  # Add to database session
        db.session.commit()  # Commit the changes to the database
        return redirect(url_for('dashboard'))  # Redirect to dashboard after submission
    return render_template('submit_feed.html')  # Render feed submission form
