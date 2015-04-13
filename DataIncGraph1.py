import pandas as pd
import string
import numpy as np
import simplejson
import matplotlib.pyplot as plt
from matplotlib import cm


with open('yelp_academic_dataset_business.json') as f:
    df=pd.DataFrame(simplejson.loads(line) for line in f)
    
type_iter=(set(x) for x in df.categories)

types=sorted(set.union(*type_iter))

dummies=pd.DataFrame(np.zeros((len(df), len(types))),columns=types)

for i, gen in enumerate(df.categories):
    dummies.ix[i,gen]=1
    
bytype=df.join(dummies.add_prefix('Type_'))
restaurants=bytype[bytype.Type_Restaurants==1]


plt.scatter(restaurants.stars,restaurants.review_count)
plt.title("Review Count vs. Stars for Restaurants")

plt.ylim(0,5000)
plt.xlabel(r'Stars')
plt.ylabel(r'Reviews')
plt.show()
