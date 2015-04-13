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

bytype.rename(columns={'Type_American (New)':'Type_American_New'}, inplace=True)
bytype.rename(columns={'Type_American (Traditional)':'Type_American_Traditional'}, inplace=True)

chineseRests=bytype[bytype.Type_Chinese==1]
fivestarchinese=chineseRests[chineseRests.stars==5]
japaneseRests=bytype[bytype.Type_Japanese==1]
fivestarjapanese=japaneseRests[japaneseRests.stars==5]
americanRests=bytype[bytype.Type_American_Traditional==1]
fivestaramerican=americanRests[americanRests.stars==5]
americanNewRests=bytype[bytype.Type_American_New==1]
fivestaramericannew=americanNewRests[americanNewRests.stars==5]
frenchRests=bytype[bytype.Type_French==1]
fivestarfrench=frenchRests[frenchRests.stars==5]


labels=["Chinese", "Japanese", "American","French"]
stars=["1 Star", "1.5 Star", "2 Star", "2.5 Star", "3 Star", "3.5 Star","4 Star", "4.5 Star", "5 Star"]
chinesevals=[float(len(chineseRests[chineseRests.stars==1]))/len(chineseRests), 
             float(len(chineseRests[chineseRests.stars==1.5]))/len(chineseRests), 
             float(len(chineseRests[chineseRests.stars==2]))/len(chineseRests), 
             float(len(chineseRests[chineseRests.stars==2.5]))/len(chineseRests), 
             float(len(chineseRests[chineseRests.stars==3]))/len(chineseRests), 
             float(len(chineseRests[chineseRests.stars==3.5]))/len(chineseRests), 
             float(len(chineseRests[chineseRests.stars==4]))/len(chineseRests),
             float(len(chineseRests[chineseRests.stars==4.5]))/len(chineseRests), 
             float(len(chineseRests[chineseRests.stars==5]))/len(chineseRests)]
japanesevals=[float(len(japaneseRests[japaneseRests.stars==1]))/len(japaneseRests), 
             float(len(japaneseRests[japaneseRests.stars==1.5]))/len(japaneseRests), 
             float(len(japaneseRests[japaneseRests.stars==2]))/len(japaneseRests), 
             float(len(japaneseRests[japaneseRests.stars==2.5]))/len(japaneseRests), 
             float(len(japaneseRests[japaneseRests.stars==3]))/len(japaneseRests), 
             float(len(japaneseRests[japaneseRests.stars==3.5]))/len(japaneseRests), 
             float(len(japaneseRests[japaneseRests.stars==4]))/len(japaneseRests),
             float(len(japaneseRests[japaneseRests.stars==4.5]))/len(japaneseRests), 
             float(len(japaneseRests[japaneseRests.stars==5]))/len(japaneseRests)]
americanvals=[float((len(americanRests[americanRests.stars==1])+len(americanNewRests[americanNewRests.stars==1])))/(len(americanRests)+len(americanNewRests)), 
             float((len(americanRests[americanRests.stars==1.5])+len(americanNewRests[americanNewRests.stars==1.5])))/(len(americanRests)+len(americanNewRests)),
              float((len(americanRests[americanRests.stars==2])+len(americanNewRests[americanNewRests.stars==2])))/(len(americanRests)+len(americanNewRests)),
              float((len(americanRests[americanRests.stars==2.5])+len(americanNewRests[americanNewRests.stars==2.5])))/(len(americanRests)+len(americanNewRests)),
              float((len(americanRests[americanRests.stars==3])+len(americanNewRests[americanNewRests.stars==3])))/(len(americanRests)+len(americanNewRests)),
              float((len(americanRests[americanRests.stars==3.5])+len(americanNewRests[americanNewRests.stars==3.5])))/(len(americanRests)+len(americanNewRests)),
              float((len(americanRests[americanRests.stars==4])+len(americanNewRests[americanNewRests.stars==4])))/(len(americanRests)+len(americanNewRests)),
              float((len(americanRests[americanRests.stars==4.5])+len(americanNewRests[americanNewRests.stars==4.5])))/(len(americanRests)+len(americanNewRests)),
              float((len(americanRests[americanRests.stars==5])+len(americanNewRests[americanNewRests.stars==5])))/(len(americanRests)+len(americanNewRests))]
frenchvals=[float(len(frenchRests[frenchRests.stars==1]))/len(frenchRests), 
             float(len(frenchRests[frenchRests.stars==1.5]))/len(frenchRests), 
             float(len(frenchRests[frenchRests.stars==2]))/len(frenchRests), 
             float(len(frenchRests[frenchRests.stars==2.5]))/len(frenchRests), 
             float(len(frenchRests[frenchRests.stars==3]))/len(frenchRests), 
             float(len(frenchRests[frenchRests.stars==3.5]))/len(frenchRests), 
             float(len(frenchRests[frenchRests.stars==4]))/len(frenchRests),
             float(len(frenchRests[frenchRests.stars==4.5]))/len(frenchRests), 
             float(len(frenchRests[frenchRests.stars==5]))/len(frenchRests)]

cmap = cm.Accent

cs = cmap(np.linspace(0., 1., len(chinesevals)))

plt.axis("equal")
plt.pie(
        chinesevals,
        labels=stars,
        autopct="%1.1f%%",
        colors=cs
        )
plt.title("Chinese Restaurant Breakdown")
plt.show()

plt.axis("equal")
plt.pie(
        japanesevals,
        labels=stars,
        autopct="%1.1f%%",
        colors=cs
        )
plt.title("Japanese Restaurant Breakdown")
plt.show()


plt.axis("equal")
plt.pie(
        americanvals,
        labels=stars,
        autopct="%1.1f%%",
        colors=cs
        )
plt.title("American Restaurant Breakdown")
plt.show()

plt.axis("equal")
plt.pie(
        frenchvals,
        labels=stars,
        autopct="%1.1f%%",
        colors=cs
        )
plt.title("French Restaurant Breakdown")
plt.show()






