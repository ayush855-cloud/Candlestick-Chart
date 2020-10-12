
# # Akhbaar padhke sunaao
# import requests
# import json

# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)

# if __name__ == '__main__':
#     speak("News for today.. Lets begin")
#     url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"
#     news = requests.get(url).text
#     news_dict = json.loads(news)
#     arts = news_dict['articles']
#     for article in arts:
#         speak(article['title'])
#         print(article['title'])
#         speak("Moving on to the next news..Listen Carefully")

#     speak("Thanks for listening...")

import datetime , requests
from bs4 import BeautifulSoup
from pandas_datareader import data
from bokeh.plotting import show, figure, output_file
start = datetime.datetime(2015, 11, 1)
end = datetime.datetime(2016 , 3 , 10)
 
df = data.DataReader(name='GOOG' , data_source="yahoo" , start= start , end = end)
def inc_dec(c,o):
    if c>o:
        value= "Increase"
    else:
        value = "Decrease"
    return value
df["Status"] = [inc_dec(c,o) for c,o in zip(df.Close , df.Open)]
df["Middle"] = (df.Open+df.Close)/2
df["Height"] = abs(df.Close-df.Open)
p = figure(x_axis_type  ='datetime' ,width=1000 , height= 300,sizing_mode="scale_width")
p.grid.grid_line_alpha=0.3
hours_12 = 12*60*60*1000

p.segment(df.index, df.High ,df.index, df.Low, color="Black")
p.rect(df.index[df.Status == "Increase"] ,df.Middle[df.Status=="Increase"] , hours_12 ,df.Height[df.Status=="Increase"] , fill_color ="green" , line_color="black")
p.rect(df.index[df.Status == "Decrease"] , df.Middle[df.Status=="Decrease"] , hours_12 ,df.Height[df.Status=="Decrease"] , fill_color ="red")
 
# p.title = "Graph"
output_file("CS.html")
show(p)
print(df)
