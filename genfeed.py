# Generate an RSS feed. This should be done after creating a blog post.
import os
from joequery import before_first_request
from joequery.settings import app
from joequery.blog.helpers import (
    get_posts_by_category, BLOG_SYS_PATH, gen_rss_feed, _alter_rss, get_excerpt,
    BLOG_CATEGORIES, get_posts, get_post_by_url, BLOG_VIEW_MORE_NAMES
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
          # needed for blog index pages to avoid broken links
          post['url']  = os.path.join("/", post['url']) 

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
          blogIndexHTML = render_template("templates/blog_index_bodygen.html", 
              posts=posts, prevPage=prevPage, nextPage=nextPage, title=title,
              category=category)

          # This keeps things "relatively" static while allowing for dynamic messages
          # in the header for things like ScreenX TV
          blogIndexTemplate = os.path.join(currentDir, "joequery", "blog", "templates", "blog_index.html")
          f = open(blogIndexTemplate, 'r')
          template = f.read()
          f.close()
          html = template.replace("REPLACEME", blogIndexHTML)

          f = open(pagePath, 'w')
          f.write(html)
          f.close()
          i += 1
          posts = newposts
  print("Generated static blog pages")

def write_home_page_posts(app, numPosts):
    '''
    Get a post from each category
    '''
    categories = BLOG_CATEGORIES[:]
    rssPath = os.path.join(BLOG_SYS_PATH, "rss.txt")
    with open(rssPath, 'r') as f:
        postURLs = f.readlines(numPosts)

    posts = []
    for url in postURLs:
        # Remove trailing newline caused by readlines
        url = url.strip()
        category = url.split('/')[0]
        post = get_post_by_url(url, app)
        post['pubDate'] = time.strftime("%B %d, %Y", post['pubDate'])
        post['category'] = category
        post['viewMore'] = BLOG_VIEW_MORE_NAMES[category]
        posts.append(post)

    # Render the blog samples template with our posts. Write the output
    # to be used as the home page
    with app.test_request_context():
        blogSampleHTML = render_template("templates/home_blog_samples_bodygen.html", posts=posts)

    # This keeps things "relatively" static while allowing for dynamic messages
    # in the header for things like ScreenX TV
    homeTemplatePath = os.path.join(currentDir, "joequery", "blog", "templates", "home_blog_samples.html")
    f = open(homeTemplatePath, 'r')
    template = f.read()
    f.close()
    html = template.replace("REPLACEME", blogSampleHTML)
    homePagePath = os.path.join(currentDir, "joequery", "static_pages", "templates", "home.static")
    f = open(homePagePath, 'w')
    f.write(html)
    f.close()

    print("Generated sample posts for the home page")


posts = get_posts(app, 10)
rss = gen_rss_feed(app, posts)
write_rss_feed(rss)
write_index_pages(10)
write_home_page_posts(app, 10)
