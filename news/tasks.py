from celery.decorators import task
from celery.utils.log import get_task_logger
from .models import Feed

logger = get_task_logger(__name__)

@task(name="get_feed_articles")
def get_feed_articles_task(feed_id):
    """ imports articles for an RSS/Atom feed """
    feed = Feed.objects.get(pk=feed_id)
    
    logger.info("Retrieving Articles for " + feed.title)
    
    return feed.get_feed_articles()
    
@task(name="update_all_feed_articles")
def update_all_feed_articles_task():
    """ updates articles for all RSS/Atom feeds """
    feeds = Feed.objects.all()
    
    for feed in feeds:
        logger.info("Retrieving Articles for " + feed.title)
    
        feed.get_feed_articles()