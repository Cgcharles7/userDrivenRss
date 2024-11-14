from sqlalchemy.orm import joinedload
from models import db, User, RSSFeed, Vote

def get_recommendations(user_id):
    """
    Generates RSS feed recommendations for a user.
    - Recommends feeds based on feeds that users with similar preferences have voted on.
    - Could implement simple collaborative filtering or content-based filtering.
    """
    # Fetch all feeds voted on by similar users (simple example: same category)
    similar_users = db.session.query(User).join(Vote).filter(Vote.user_id != user_id).all()

    recommended_feeds = []
    for user in similar_users:
        # Find feeds voted by similar users
        feeds = db.session.query(RSSFeed).join(Vote).filter(Vote.user_id == user.id).all()
        for feed in feeds:
            if feed not in recommended_feeds:
                recommended_feeds.append(feed)

    return recommended_feeds  # Return a list of recommended RSS feeds
