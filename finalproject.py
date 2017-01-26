#import modules
import requests
import pandas as pd
#get endpoint of api
endpoint = 'http://pokeapi.co/api/v2/pokemon/'
#make empty lists
sattack = []
attack = []
#get data for every pokemon in 1st generation
for x in range(1,152):
    num = str(x)
    url = endpoint + num + '/'
    
    r = requests.get(url)
        
    pokemon = r.json()
    sa = pokemon['stats'][2]['base_stat']
    a = pokemon['stats'][4]['base_stat']
    #get data inside list
    sattack.append(sa)
    attack.append(a)
#make dataframe
df = pd.DataFrame({
    'sattack': sattack,
    'attack': attack
})
#import functions from bokeh
from bokeh.charts import Scatter, output_file, save
#make and save chart
p = Scatter(df, 'sattack', 'attack', title = 'Special Attack vs. Attack')
output_file = 'Graph.html'
save(p)