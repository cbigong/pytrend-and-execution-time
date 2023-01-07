from flask import Flask,render_template
import pandas as pd
from pytrends.request import TrendReq
import pandas as pd
import time
import matplotlib.pyplot as plt
import os
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__)

#save img
#Pytrend = TrendReq() 
#Pytrend.build_payload(kw_list=['vlog','blog'], timeframe='2022-09-25 2022-12-25' , geo ='ID')
#df = Pytrend.interest_over_time()
#fig=plt.figure()
#plt.plot(df)
#fig.savefig('static/IMG/comparison3.jpg')
#IMG_FOLDER = os.path.join('static', 'IMG')
#app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/', methods=["GET"])
def plot_trend():
    #Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'flask-logo.png')
    #load trends with google api
    Pytrend = TrendReq() 
    Pytrend.build_payload(kw_list=['vlog','blog'], timeframe='2022-09-25 2022-12-25' , geo ='ID')
    df = Pytrend.interest_over_time()
    #generate plot
    x=df["blog"]
    y=df["vlog"]
    fig=plt.figure(figsize=(8,5))
    plt.plot(df.index,x,label="blog")
    plt.plot(df.index,y,label="vlog")
    plt.xlabel("time")
    plt.ylabel("interest")
    plt.title("comparison between vlog and blog over time")
    plt.legend()
    #convert plot to png image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
     # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template("image.html", image=pngImageB64String)