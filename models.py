from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    User model that represents a platform user.
    - Stores username and password.
    - Provides a relation to the RSS feed and comment models.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique user ID
    username = db.Column(db.String(150), unique=True, nullable=False)  # Username field
    password = db.Column(db.String(150), nullable=False)  # Password field (hashed)

class RSSFeed(db.Model):
    """
    RSSFeed model representing an RSS feed submitted by a user.
    - Stores feed title, description, and URL.
    - Relates to the User who submitted the feed.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique feed ID
    title = db.Column(db.String(150), nullable=False)  # Feed title
    url = db.Column(db.String(250), unique=True, nullable=False)  # Unique feed URL
    description = db.Column(db.String(500), nullable=True)  # Optional description
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # The user who submitted this feed

class Comment(db.Model):
    """
    Comment model representing user comments on RSS feeds.
    - Each comment is linked to a user and a specific RSS feed.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique comment ID
    content = db.Column(db.String(500), nullable=False)  # Content of the comment
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # The user who made the comment
    feed_id = db.Column(db.Integer, db.ForeignKey('rss_feed.id'), nullable=False)  # The feed being commented on

class Vote(db.Model):
    """
    Vote model to track upvotes and downvotes on RSS feeds.
    - Relates votes to specific users and feeds.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique vote ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # The user who voted
    feed_id = db.Column(db.Integer, db.ForeignKey('rss_feed.id'), nullable=False)  # The feed being voted on
    vote_type = db.Column(db.String(50), nullable=False)  # 'upvote' or 'downvote'
