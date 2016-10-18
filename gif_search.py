# Import Necessary Modules
from flask import Flask, render_template, request

import giphypop
import os

app = Flask(__name__)
g = giphypop.Giphy()

# Webpage references
@app.route('/')
def index():
    name = request.values.get('name', 'nobody')
    greeting = "Hello {}".format(name)
    return render_template('new_index.html', greeting=greeting)
    
@app.route('/about')
def about():
    name = request.values.get('name', 'nobody')
    greeting = "Hello {}".format(name)
    return render_template('about.html', greeting=greeting)



# def get_search_results():
#     g = giphypop.Giphy()
#     results = g.search(input()) 

@app.route('/results')
def results():
    keyword = request.values.get('keyword')
    header = "Gifs tagged with " + keyword
    results = g.search(keyword)
    #print(results)    
    return render_template('results.html', header=header, keyword=keyword, results=results)


    # for result in results:
    #     print(result.media_url)
    #     print(result.url)

app.run(debug=True)

####################################################################
###### Go to pages on canvas for necessary changes #################
###### Push to both GitHub and Heroku separately   #################
####################################################################




