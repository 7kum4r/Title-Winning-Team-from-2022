from mplsoccer import Pitch,VerticalPitch
import matplotlib.pyplot as plt
from PIL import Image 
import numpy as np
import urllib.request
import mysql.connector
import pandas as pd


con = mysql.connector.connect(host="localhost", user="root", password="----")
cursorObject = con.cursor()
cursorObject.execute("USE fifa")

with open('sql_query.txt','r')as f:
    query_2=f.read()
with open('pre_requisite_query.txt','r')as f:
    query_1=f.read()

cursorObject.execute(query_1)
cursorObject.execute(query_2)
data=pd.DataFrame(cursorObject.fetchall())

pos=[[33,48,2,17],
     [3,18,25,40],[24,39,25,40],[43,58,25,40],[62,77,25,40],
     [15,30,52,67],[50,65,52,67],
     [10,25,78,93],[33,48,78,93],[56,71,78,93],
     [33,48,100,115]]

for t in range(6):
    urls=[]
    names=[]
    ids=data.iloc[t,1:12].values
    ids=[str(x) for x in ids]
    for j in ids:
        cursorObject.execute(f"select short_name from fifa_2022 where sofifa_id= {j}")
        name=cursorObject.fetchall()[0][0]
        names.append(name)
        if len(j)== 5:
            j='0'+j
        url="https://cdn.sofifa.net/players/" + j[:3] +"/" + j[3:] +'/22_120.png'
        urls.append(url)

    pitch = VerticalPitch(pitch_color='grass',line_color='white',line_alpha=0.25, goal_alpha=0.25, stripe=True)
    fig, ax = pitch.draw(figsize=(30, 15))
    for i in range(11):

        r_site = urllib.request.Request(urls[i], headers={"User-Agent": "Mozilla/5.0"})
        im = Image.open(urllib.request.urlopen(r_site))
        ax.imshow(im, extent=pos[i])
        plt.text(pos[i][0]+7,pos[i][2] -3.5, names[i], fontsize = 20,
                 ha='center',color='black',bbox=dict(boxstyle="square"))   
    plt.show()

