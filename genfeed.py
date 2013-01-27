# Generate an RSS feed. This should be done after creating a blog post.
import os
from joequery import before_request
from joequery.settings import app
from joequery.blog.helpers import (
    get_posts_by_category, BLOG_SYS_PATH, gen_rss_feed, _alter_rss, get_excerpt,
    BLOG_CATEGORIES, get_posts, get_post_by_url, BLOG_VIEW_MORE_NAMES
)
from flask import render_template, current_app,g 
import copy
import time
import ConfigParser

currentDir = os.sep.join(os.path.realpath(__file__).split('/')[:-1])
    
# Write an rss feed to the appropriate file
def write_rss_feed(rss):
  feedPath = os.path.join(BLOG_SYS_PATH, "templates", "rssfeed.static")
  f = open(feedPath, 'w')
  rss = rss.encode("ascii", "xmlcharrefreplace")
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
          before_request()
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

    # Only display recent articles
    postURLs = postURLs[0:10]

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

def write_xml_sitemap():
    rssPath = os.path.join(BLOG_SYS_PATH, "rss.txt")
    with open(rssPath, 'r') as f:
        posts = [x.strip() for x in f.readlines()]

    with app.test_request_context():
        html = render_template("sitemap.html", posts=posts, categories=BLOG_CATEGORIES)
        sitemapPath = os.path.join(currentDir, "joequery", "static_pages",
                      "templates", "sitemap.static")
        f = open(sitemapPath, 'w')
        f.write(html)
        f.close()
        print("Generated xml sitemap")

def write_tags_index():
    tagsPath = os.path.join(BLOG_SYS_PATH, "posts", "tags")
    tagDirs = []
    for f in os.listdir(tagsPath):
        if os.path.isdir(os.path.join(tagsPath, f)):
            tagDirs.append(f)

    for d in tagDirs:
        tag = os.path.basename(d)
        entryPath = os.path.join(tagsPath, d, "posts.txt")
        f = open(entryPath, 'r')
        postList = [x.strip() for x in f.readlines()]
        posts = []
        f.close()

        for p in postList:
            parser = ConfigParser.ConfigParser()
            parser.read(os.path.join(BLOG_SYS_PATH, "posts", p, "meta.txt"))
            metaData = dict(parser.items("post"))
            postTime = time.strptime(metaData['time'], "%Y-%m-%d %a %H:%M %p")

            posts.append({"url":"/"+p, "title":metaData["title"], 
                "pubDate": time.strftime("%B %d, %Y", postTime)})
          

        with app.test_request_context():
            title = "Posts tagged as %s" % tag
            tagGenHTML = render_template("templates/tag_index_bodygen.html",
                    posts=posts, kind="tag", title=title)


        # Each meta file should begin with a [post] section
        metaData = dict(parser.items("post"))

        tagIndexTemplate = os.path.join(BLOG_SYS_PATH, "templates", "tag_index.html")
        f = open(tagIndexTemplate, 'r')
        template = f.read()
        f.close()
        html = template.replace("REPLACEME", tagGenHTML)
        
        pagePath = os.path.join(tagsPath, d, "index.static")
        f = open(pagePath, 'w')
        f.write(html)
        f.close()

    print("Generated tag index pages")

def write_series_index():
    seriesPath = os.path.join(BLOG_SYS_PATH, "posts", "series")
    seriesDirs = []
    for f in os.listdir(seriesPath):
        if os.path.isdir(os.path.join(seriesPath, f)):
            seriesDirs.append(f)

    for d in seriesDirs:
        series = os.path.basename(d)
        entryPath = os.path.join(seriesPath, d, "posts.txt")
        f = open(entryPath, 'r')
        postList = [x.strip() for x in f.readlines()]
        posts = []
        f.close()

        for p in postList:
            parser = ConfigParser.ConfigParser()
            parser.read(os.path.join(BLOG_SYS_PATH, "posts", p, "meta.txt"))
            metaData = dict(parser.items("post"))
            postTime = time.strptime(metaData['time'], "%Y-%m-%d %a %H:%M %p")

            posts.append({"url":"/"+p, "title":metaData["title"], 
                "pubDate": time.strftime("%B %d, %Y", postTime)})
          

        with app.test_request_context():
            title = "Posts in the %s series" % series
            seriesGenHTML = render_template("templates/tag_index_bodygen.html",
                    posts=posts, kind="series", title=title)

        seriesIndexTemplate = os.path.join(BLOG_SYS_PATH, "templates", "tag_index.html")
        f = open(seriesIndexTemplate, 'r')
        template = f.read()
        f.close()
        html = template.replace("REPLACEME", seriesGenHTML)
        
        pagePath = os.path.join(seriesPath, d, "index.static")
        f = open(pagePath, 'w')
        f.write(html)
        f.close()

    print("Generated series index pages")

def get_posts_in_order(reverse=True):
    # Merge the posts from all the categries
    postsPath = os.path.join(BLOG_SYS_PATH, "posts")
    categoryPaths = {}
    for c in BLOG_CATEGORIES:
        categoryPaths[c] = os.path.join(postsPath, c) 

    posts = []
    for x,c in categoryPaths.iteritems():
        for p in os.listdir(c):
            path = os.path.join(c,p)
            parser = ConfigParser.ConfigParser()
            parser.read(os.path.join(path, "meta.txt"))
            meta = dict(parser.items("post"))
            postTime = time.strptime(meta['time'], "%Y-%m-%d %a %H:%M %p")
            del meta['time']
            
            category = path.split("/")[-2]
            slug = path.split("/")[-1]
            posts.append({"path":path, "category":category, "slug":slug, 
                          "postTime":postTime, "meta":meta})


    # sort the posts based on their date
    posts = sorted(posts, key=lambda k: k['postTime'], reverse=reverse)
    return posts

def write_related_txts():
    postsPath = os.path.join(BLOG_SYS_PATH, "posts")
    seriesPath = os.path.join(postsPath, "series")
    tagsPath = os.path.join(postsPath, "tags")

    # Create empty tags/series post files
    for p in os.listdir(seriesPath):
        with file(os.path.join(seriesPath, p, "posts.txt"), 'w') as f:
            f.write("")

    for p in os.listdir(tagsPath):
        with file(os.path.join(tagsPath, p, "posts.txt"), 'w') as f:
            f.write("")

    # Now sort the posts based on their date, with newest first.
    posts = get_posts_in_order(reverse=True)

    # Write the posts.txt files
    for post in posts:
        tags = post['meta'].get('tags')
        if tags:
            for tag in [x.strip() for x in tags.split(",")]:
                tagFilePath = os.path.join(tagsPath, tag, "posts.txt")
                with open(tagFilePath, 'a') as f:
                    f.write(os.path.join(post['category'], post['slug']) + "\n")

    # We want series to go in chronological order
    posts.reverse()
    for post in posts:
        series = post['meta'].get('series')
        if series:
            seriesFilePath = os.path.join(seriesPath, series, "posts.txt")
            with open(seriesFilePath, 'a') as f:
                f.write(os.path.join(post['category'], post['slug']) + "\n")

    print("Generated related posts.txt files")

def write_rss_txt():
    posts = get_posts_in_order(reverse=True)
    rssPath = os.path.join(BLOG_SYS_PATH, "rss.txt")
    with open(rssPath, 'w') as f:
        for post in posts:
            f.write(os.path.join(post['category'], post['slug']) + "\n")

    print("Generated rss.txt")


write_rss_txt()
posts = get_posts(app, 10)
rss = gen_rss_feed(app, posts)
write_rss_feed(rss)
write_index_pages(10)
write_home_page_posts(app, 10)
write_xml_sitemap()
write_related_txts()
write_tags_index()
write_series_index()
