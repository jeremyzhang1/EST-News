from flask import Flask, render_template, request
from newsapi import NewsApiClient
import os

app = Flask(__name__)
first_boot = True

@app.route('/', methods=["GET","POST"])
def Index():
    global first_boot
    #Setup the API Key
    api = NewsApiClient(api_key=os.environ['NEWS_API_KEY'])

    #Get the search query from the HTML form
    query = request.form.get("search_query")

    #Display top headlines if the page was first loaded or if the query is invalid 
    if first_boot is True or query == None:
        first_boot = False
        #Use News API to get the news for the three categories
        entertainment = api.get_top_headlines(category="entertainment", country="us")
        sports = api.get_top_headlines(category="sports", country="us")
        technology = api.get_top_headlines(category="technology", country="us")
    else:
        #Search in the three categories with the user's search query
        entertainment = api.get_top_headlines(q=query, category="entertainment", country="us")
        sports = api.get_top_headlines(q=query, category="sports", country="us")
        technology = api.get_top_headlines(q=query, category="technology", country="us")

    #Store the articles
    entertainment = entertainment['articles']
    sports = sports['articles']
    technology = technology['articles']

    #Sanitize inputs
    for i in range(len(entertainment)):
        #Only keep the date, not the time
        entertainment[i]['publishedAt'] = entertainment[i]['publishedAt'][0:entertainment[i]['publishedAt'].find('T')]
        #Give a default thumbnail if there is no thumbnail image provided
        if entertainment[i]['urlToImage'] == None:
            entertainment[i]['urlToImage'] = "https://motionarray.imgix.net/preview-247810-wmhtcGFuxa-high_0004.jpg"
        #Give default description when none is provided
        if entertainment[i]['description'] == None:
            entertainment[i]['description'] = "No description found."

    for i in range(len(sports)):
        sports[i]['publishedAt'] = sports[i]['publishedAt'][0:sports[i]['publishedAt'].find('T')]
        if sports[i]['urlToImage'] == None:
            sports[i]['urlToImage'] = "https://motionarray.imgix.net/preview-247810-wmhtcGFuxa-high_0004.jpg"
        if sports[i]['description'] == None:
            sports[i]['description'] = "No description found"

    for i in range(len(technology)):
        technology[i]['publishedAt'] = technology[i]['publishedAt'][0:technology[i]['publishedAt'].find('T')]
        if technology[i]['urlToImage'] == None:
            technology[i]['urlToImage'] = "https://motionarray.imgix.net/preview-247810-wmhtcGFuxa-high_0004.jpg"
        if technology[i]['description'] == None:
            technology[i]['description'] = "No description found"
            
    #Pass the articles into the webpage template
    return render_template('index.html', entertainment=entertainment, sports=sports, technology=technology)

if __name__ == "__main__":
    app.run()
