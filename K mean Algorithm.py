import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame({
    "x":[12,20,28,18,29,33,24,45,45,52,51,52,55,53,55,61,64,69,72],
    "y":[39,36,30,52,54,46,55,59,63,70,66,63,58,23,14,8,19,7,24]
 })
print("step 1:Initialization- K initial means (centroids) are generated at random");
print(" ..........................................")
print("Dataset for training");
print("............................................")
print(df);
print("..............................................")
np.random.seed(200)
k=3
#centroid[i]=[x,y]
centroid={
    i+1:[np.random.randint(0,80),np.random.randint(0,80)]
    for i in range(k)
}
print("................................................")
print("Random centroid generated");
print(centroid);
print(".............................................")
fig=plt.figure(figsize=(5,5))
plt.scatter(df['x'],df["y"],color='k')
colmap={1:'r',2:'g',3:'b'}
for i in centroid.keys():
    plt.scatter(*centroid[i],color=colmap[i])
plt.title("Marvellous:Dataset with random centroid");
plt.xlim(0,80)
plt.ylim(0,80)
plt.show()
#______________________________________________________________________-
#Assignment-K clusters are created by associating each Observation with the nearest centroid

def assignment(df,centroid):
    for i in centroid.keys():
        #sqrt((x1-x2)^2-(y1-y2)^2)
        df['distance_from_{}'.format(i)]=(np.sqrt((df['x']-centroid[i][0])**2+(df['y']-centroid[i][1])**2))

        centroid_distance_cols=['distance_from_{}'.format(i)for i in centroid.keys()]
    df['closest']=df.loc[:,centroid_distance_cols].idxmin(axis=1)
    df['closest']=df['closest'].map(lambda x:int(x.lstrip('distance_from)_')))
    df['color']=df['closest'].map(lambda x:colmap[x])
    return df

print("step 2:Assignment-K clusters are created by associating each observation with the nearest centroid");
print("Before assignment dataset");
print(df)
df=assignment(df,centroid)

print("First centroid:Red");
print("Second centroid:Green");
print("Third centroid:Blue");
print("After Assignment Dataset");
print(df)

fig=plt.figure(figsize=(5,5))
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolor='k')
for i in centroid.keys():
    plt.scatter(*centroid[i],color=colmap[i])
plt.xlim(0,80)
plt.ylim(0,80)
plt.title("Marvellous:Dataset with clustering and random centroid");
plt.show()
#__________________________________
old_centroid=copy.deepcopy(centroid)
print("Step 3:Update-The centroid of the cluster become the new mean Assignment and update are repeated iteratively until convergence ")

def update(k):
    print("old value of centroid");
    print(k);

    for i in centroid.keys():
        centroid[i][0]=np.mean(df[df['closest']==i]['x'])
        centroid[i][1]=np.mean(df[df['closest'] == i]['y'])
    print("New value of centroids");
    print(k);
    return k
centroids=update(centroid)
fig=plt.figure(figsize=(5,5))
ax=plt.axes()
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i],color=colmap[i])
    plt.xlim(0,80)
    plt.ylim(0,80)

    for i in old_centroid.keys():
        old_x=old_centroid[i][0]
        old_y=old_centroid[i][1]
        dx=(centroid[i][0]-old_centroid[i][0])*0.75
        dy=(centroid[i][1]-old_centroid[i][1])*0.75
        ax.arrow(old_x,old_y,dx,dy,head_width=2,head_length=3,fc=colmap[i],ec=colmap[i])
    plt.title("Marvellous:Dataset with clustering and update centroids");
    plt.show()
    # ....................................................
    ##Repeat Assignment Stage
    print("Before assignment dataset");
    print(df)
    df=assignment(df,centroids)
    print("After Assignment Dataset");
    print(df)

    #plot result
    fig=plt.figure(figsize=(5,5))
    plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolor='k')
    for i in centroid.keys():
        plt.scatter(*centroid[i],color=colmap[i])
        plt.xlim(0,80)
        plt.ylim(0,80)
        plt.title("Marvellous:Dataset with clustering and updated centroids");
        plt.show()
        #continue until all assigned categories dont change any more
        while True:
            closest_centroid=df['closest'].copy(deep=True)
            centroids=update(centroid)
            print("Before assignment Dataset");
            print(df)
            df=assignment(df,centroid)
            print("After assignment dataset");
            print(df)
            if closest_centroid.equals(df['closest']):
                break
        print("final value of centroids");
        print(centroids);

        fig=plt.figure(figsize=(5,5))
        plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolor='k')
        for i in centroid.keys():
            plt.scatter(*centroid[i],color=colmap[i])
            plt.xlim(0,80)
            plt.ylim(0,80)
            plt.title("Marvellous:final dataset with set centroids");
            plt.show()























