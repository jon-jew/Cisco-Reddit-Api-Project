Read Me
This is the python api that returns the top 20 articles of a subreddit that is specified by a user.
I used python, flask and html to complete this task.

How it works
I have an index.html in the template folder which is where flask will run all of the python code.
When the opens, flask renders the home page which is a simple html and bootstrap page.
Then, I use beautiful soup to sort through and find the data that I want which is the link
and the title of the top 20 reddit articles. In the html code of reddit, all of the content
is under the <div class="content" role="main">... </div> tag and all the posts are in <div id="siteTable">...</div>
which is inside that content div. I select this div with the "siteTable" id and the last thing in the post
would be div.thing. Then i get the information which is the link and title of each of the articles.
This is all appended to a list called ret which is then rendered in lisiting.html which also uses bootstrap.


Frameworks used:
-Python 2.7.14
-BeautifulSoup
-Flask

Installation
1. Install frameworks listed above.
2. Run reddit.py in command prompt.
3. The api should run on local port 5000 (http://127.0.0.1:5000/)

