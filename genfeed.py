# Generate an RSS feed. This should be done after creating a blog post.
import os
from joequery import before_first_request
from joequery.settings import app
from joequery.blog.helpers import (
    get_posts_by_category, BLOG_SYS_PATH, gen_rss_feed, _alter_rss, get_excerpt,
    BLOG_CATEGORIES, get_posts, get_post_by_url
)
from flask import render_template, current_app,g 
import copy
import time

currentDir = os.sep.join(os.path.realpath(__file__).split('/')[:-1])
    
# Write an rss feed to the appropriate file
def write_rss_feed(rss):
  feedPath = os.path.join(BLOG_SYS_PATH, "templates", "rssfeed.static")
  f = open(feedPath, 'w')
  f.write(rss)
  f.close()
  print("Generated static rss feed")

def write_index_pages(postsPerPage):
  for category in BLOG_CATEGORIES:
      i=1
      posts = get_posts_by_category(app, postsPerPage, category=category)
      while posts:
        for post in posts:
          post['pubDate'] = time.strftime("%B %d, %Y", post['pubDate'])

        pagePath = os.path.join(BLOG_SYS_PATH, "pages", category, "page%d.static" % i)
        with app.test_request_context():
          before_first_request()
          start = postsPerPage * i
          newposts = get_posts_by_category(app, postsPerPage, category, start)

          # Determine if we should display prev/next buttons
          prevPage = False
          nextPage = False
          if i>1:
            prevPage = i-1
          if len(newposts) > 0:
            nextPage = i+1

          # Determine the appropriate title tag to use.
          if i == 1:
            title = "Programming blog"
          else:
            title = "Programming blog | Page %d" % i
          html = render_template("templates/blog_index.html", 
              posts=posts, prevPage=prevPage, nextPage=nextPage, title=title,
              category=category)

          f = open(pagePath, 'w')
          f.write(html)
          f.close()
          i += 1
          posts = newposts
  print("Generated static blog pages")

def write_home_page_posts(app):
    '''
    Get a post from each category
    '''
    categories = BLOG_CATEGORIES[:]
    rssPath = os.path.join(BLOG_SYS_PATH, "rss.txt")
    posts = {}
    f = open(rssPath, 'r')
    line = f.next().strip()
    while categories:
        try:
            category = line.split('/')[0]
            if category in categories:
                categories.remove(category)
                post = get_post_by_url(line, app)
                post['pubDate'] = time.strftime("%B %d, %Y", post['pubDate'])
                posts[category] = post
            line = f.next().strip()
        except StopIteration:
            break
    f.close()

    # Render the blog samples template with our posts. Write the output
    # to be used as the home page
    with app.test_request_context():
        before_first_request()
        html = render_template("templates/home_blog_samples.html", posts=posts)

    homePagePath = os.path.join(currentDir, "joequery", "static_pages", "templates", "home.html")
    f = open(homePagePath, 'w')
    f.write(html)
    f.close()

    print("Generated sample posts for the home page")


posts = get_posts(app, 10)
rss = gen_rss_feed(app, posts)
write_rss_feed(rss)
write_index_pages(10)
write_home_page_posts(app)
