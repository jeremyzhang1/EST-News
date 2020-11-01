# EST News
EST News is a web app that searches for and displays entertainment, sports, and technology news that is built with Flask and the News API, and deployed using Heroku.  
https://est-news.herokuapp.com/  
Link to the GitHub repository:  
https://github.com/jeremyzhang1/EST-News

### Design
EST-News was designed using Flask to handle API calls and user requests.  
A user interface was built using HTML, Bootstrap, and CSS.  
Favicon generation was done using favicon.io.  

Upon loading of the webpage, articles would already be populated if the user just wanted to browse.  
If the user's query was invalid (empty query), then the top entertainment, sports, and tech articles would be displayed.  
Each API call returns lots of information, however, I will only retained the 'articles' portion of the information, which contains article metadata as well as links to the articles. Articles from all languages and all regions of the world are included in the displayed results, since I wanted to make this app usable by as many people around the world as possible.

NewsAPI will sometimes return duplicate articles, so those duplicates must be removed.  
The algorithm to do so is outlined in this article:  
https://www.geeksforgeeks.org/python-removing-duplicate-dicts-in-list/

Then, error handling and some data processing must happen next.  
For each of the three categories, the 'publishedAt' field is converted into a readable YYYY-MM-DD date.  
If a 'urlToImage' (thumbnail image) is not provided, then a generic picture with the word "news" is used instead.  
If there is no description, "No description found." will be displayed in place of the description.  
Time complexity for this part is O(n), since all the articles must be proccessed.

The articles with proper error handling are then passed into the HTML webpage.  
Using Jinja2, each article is rendered as a card on the webpage.  
If there were no articles returned passed in because no articles were returned by the API, then a message explaining
that no articles are found is displayed instead.

### Deployment Process
EST-News was deployed to Heroku using the process outlined in their documentation here:  
https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true

### Additional Resources Consulted
https://newsapi.org/docs (NewsAPI documentation)  
https://getbootstrap.com/docs/4.5/getting-started/introduction/ (Bootstrap Documentation)  
https://flask.palletsprojects.com/en/1.1.x/ (Flask Documentation)  
https://jinja.palletsprojects.com/en/2.11.x/ (Jinja2 Documentation)  
https://www.mindsumo.com/contests/newsapi (Contest Page)