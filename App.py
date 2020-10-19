from flask import Flask, render_template
from newsapi import NewsApiClient
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def Index():
    api = NewsApiClient(api_key='4cc7e5c83c7a4b778f048e6796c0ef0c')
    entertainment = api.get_top_headlines(category="entertainment", country="us")
    sports = api.get_top_headlines(category="sports", country="us")
    technology = api.get_top_headlines(category="technology", country="us")

    entertainment = entertainment['articles']
    sports = sports['articles']
    technology = technology['articles']

    for i in range(len(entertainment)):
        entertainment[i]['publishedAt'] = entertainment[i]['publishedAt'][0:entertainment[i]['publishedAt'].find('T')]
        if entertainment[i]['urlToImage'] == None:
            entertainment[i]['urlToImage'] = "https://motionarray.imgix.net/preview-247810-wmhtcGFuxa-high_0004.jpg"
        if entertainment[i]['description'] == None:
            entertainment[i]['description'] = ""

    for i in range(len(sports)):
        sports[i]['publishedAt'] = sports[i]['publishedAt'][0:sports[i]['publishedAt'].find('T')]
        if sports[i]['urlToImage'] == None:
            sports[i]['urlToImage'] = "https://motionarray.imgix.net/preview-247810-wmhtcGFuxa-high_0004.jpg"
        if sports[i]['description'] == None:
            sports[i]['description'] = ""

    for i in range(len(technology)):
        technology[i]['publishedAt'] = technology[i]['publishedAt'][0:technology[i]['publishedAt'].find('T')]
        if technology[i]['urlToImage'] == None:
            technology[i]['urlToImage'] = "https://motionarray.imgix.net/preview-247810-wmhtcGFuxa-high_0004.jpg"
        if technology[i]['description'] == None:
            technology[i]['description'] = ""

    return render_template('index.html', entertainment=entertainment, sports=sports, technology=technology)

if __name__ == "__main__":
    app.run()