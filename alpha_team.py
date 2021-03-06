


from google.colab import drive
drive.mount('/content/drive')

import pandas as  pd 
df = pd.read_csv("survey_results_public.csv")
'''df = df[df['ConvertedComp'] < 250000]'''

'''df = df.reset_index(drop=True)
df["MainBranch"].index'''

list(df["OpenSource"].unique())

df.head()

df.shape

from tqdm import tqdm
first_15_col_excl_yearcode = [ 'MainBranch'	,'Hobbyist',	'OpenSourcer',	'OpenSource',	'Employment',	'Country' ,
                'Student'	,'EdLevel',	'UndergradMajor',	'OrgSize',		'CareerSat']
df[first_15_col_excl_yearcode].fillna(value =-1, inplace= True)
for i in tqdm(first_15_col_excl_yearcode):
  print('Converting '+ i +'\n')
  df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
  print(df[i].unique())

from tqdm import tqdm
first_15_col_excl_yearcode = ['WorkPlan',	'WorkRemote',	'WorkLoc',	'ImpSyn' ,
                'CodeRev'	,'UnitTests',	'PurchaseHow',	'PurchaseWhat']
df[first_15_col_excl_yearcode].fillna(value =-1, inplace= True)
for i in tqdm(first_15_col_excl_yearcode):
  print('Converting '+i +'\n')
  
  df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
  print(df[i].unique())

from tqdm import tqdm
first_15_col_excl_yearcode = ['OpSys'	,'BlockchainOrg',	'BlockchainIs',	'ITperson']
df[first_15_col_excl_yearcode].fillna(value =-1, inplace= True)
for i in tqdm(first_15_col_excl_yearcode):
  print('Converting '+i +'\n')
  
  df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
  print(df[i].unique())

from tqdm import tqdm
last_15_col_excl_yearcode = ['OffOn','SocialMedia',	'SOFindAnswer',	'SOVisitFreq','SOTimeSaved' ,
                'SOHowMuchTime'	,'SOAccount',	'SOPartFreq',	'SOJobs',	'WelcomeChange',	'SONewContent',	'Gender','Trans','Sexuality','Dependents']
df[last_15_col_excl_yearcode].fillna(value = -1, inplace= True)
for i in tqdm(last_15_col_excl_yearcode):
  print('Converting '+i)
  
  df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
  print(df[i].unique())

from tqdm import tqdm
last_15_col_excl_yearcode = ['JobSat','MgrIdiot','MgrMoney','MgrWant','JobSeek','LastHireDate','CurrencySymbol']
df[last_15_col_excl_yearcode].fillna(value = -1, inplace= True)
for i in tqdm(last_15_col_excl_yearcode):
  print( 'Converting '+ i )
  
  df[i].replace(to_replace = list(df[i].unique()), value = range(1,len(list(df[i].unique()))+1) , inplace = True)
  print(df[i].unique())

df = df.drop(axis=1,columns=["Respondent", "Age1stCode", "FizzBuzz", "ResumeUpdate", "BetterLife", "ScreenName", "SOVisit1st",
                             "EntTeams","SOComm","Extraversion","SurveyLength","SurveyEase","LastInt",'CurrencyDesc',
                             "Ethnicity", "DevEnviron", "LanguageDesireNextYear","DatabaseDesireNextYear","PlatformDesireNextYear",
                             "WebFrameDesireNextYear","MiscTechDesireNextYear","SOVisitTo", "WelcomeChange",
                             "CurrencySymbol","CompTotal","CompFreq" ,'EduOther',	'WorkChallenge','JobFactors'])

'''Dropped non - useful columns '''

df.shape

def Convert_YearsCodePro_and_YearsCode ( df ):
    df["YearsCode"].replace(to_replace = ['Less than 1 year', 'More than 50 years'],
                            value = [1,50] , inplace = True) 
    df["YearsCode"].fillna(value= '-1', inplace = True )
    df["YearsCode"] = df["YearsCode"].apply(pd.to_numeric) 
    df["YearsCodePro"].replace(to_replace = ['Less than 1 year', 'More than 50 years'],
                            value = [1,50] , inplace = True) 
    df["YearsCodePro"].fillna(value= '-1', inplace = True )
    df["YearsCodePro"] = df["YearsCodePro"].apply(pd.to_numeric) 
    return df
Convert_YearsCodePro_and_YearsCode(df)

import numpy as np
from sklearn.impute import SimpleImputer
yrcode =df["YearsCode"]
imp = SimpleImputer(missing_values= -1, strategy='mean')
yrcodepro =df["YearsCodePro"]
imp = SimpleImputer(missing_values= -1, strategy='mean')

DevType = df["DevType"]
DevType.fillna(value= '-1', inplace = True )
ls = []
for i in DevType:    
    if i != '-1':
        cat = i.split(';')
        for j in cat:
            if j not in ls:
                ls.append(j)
d = dict(zip(set(ls), [1]*len(ls)))
rep_devtype = []
for i in DevType:
    if i == '-1':
        rep_devtype.append(-1)
    if i != '-1':
        sum = 0
        cat = i.split(';')
        for j in cat:
            sum = d[ j ] + sum
        rep_devtype.append(sum) 
        
DevType = pd.DataFrame(rep_devtype)

df["DevType"] = DevType

LanguageWorkedWith = df["LanguageWorkedWith"]
LanguageWorkedWith.fillna(value= '-1', inplace = True )
ls = []
for i in LanguageWorkedWith  :    
    if i != '-1':
        cat = i.split(';')
        for j in cat:
            if j not in ls:
                ls.append(j)
d = dict(zip(set(ls),[1]*len(ls)))
rep_LanguageWorkedWith   = []
for i in LanguageWorkedWith  :
    if i == '-1':
        rep_LanguageWorkedWith.append(-1)
    if i != '-1':
        sum = 0
        cat = i.split(';')
        for j in cat:
            sum = d[ j ] + sum
        rep_LanguageWorkedWith.append(sum) 
LanguageWorkedWith = pd.DataFrame(rep_LanguageWorkedWith)

df["LanguageWorkedWith"] = LanguageWorkedWith

DatabaseWorkedWith = df["DatabaseWorkedWith"]
DatabaseWorkedWith.fillna(value= '-1', inplace = True )
ls = []
for i in DatabaseWorkedWith  :    
    if i != '-1':
        cat = i.split(';')
        for j in cat:
            if j not in ls:
                ls.append(j)
d = dict(zip(set(ls), [1]*len(ls)))
rep_DatabaseWorkedWith   = []
for i in DatabaseWorkedWith  :
    if i == '-1':
        rep_DatabaseWorkedWith.append(-1)
    if i != '-1':
        sum = 0
        cat = i.split(';')
        for j in cat:
            sum = d[ j ] + sum
        rep_DatabaseWorkedWith.append(sum) 
DatabaseWorkedWith = pd.DataFrame(rep_DatabaseWorkedWith)

df["DatabaseWorkedWith"] = DatabaseWorkedWith

PlatformWorkedWith = df["PlatformWorkedWith"]
PlatformWorkedWith.fillna(value= '-1', inplace = True )
ls = []
for i in PlatformWorkedWith  :    
    if i != '-1':
        cat = i.split(';')
        for j in cat:
            if j not in ls:
                ls.append(j)
d = dict(zip(set(ls),[1]*len(ls)))
rep_PlatformWorkedWith   = []
for i in PlatformWorkedWith  :
    if i == '-1':
        rep_PlatformWorkedWith.append(-1)
    if i != '-1':
        sum = 0
        cat = i.split(';')
        for j in cat:
            sum = d[ j ] + sum
        rep_PlatformWorkedWith.append(sum) 
PlatformWorkedWith = pd.DataFrame(rep_PlatformWorkedWith)

df["PlatformWorkedWith"] = PlatformWorkedWith

WebFrameWorkedWith = df["WebFrameWorkedWith"]
WebFrameWorkedWith.fillna(value= '-1', inplace = True )
ls = []
for i in WebFrameWorkedWith  :    
    if i != '-1':
        cat = i.split(';')
        for j in cat:
            if j not in ls:
                ls.append(j)
d = dict(zip(set(ls),[1]*len(ls)))
rep_WebFrameWorkedWith   = []
for i in WebFrameWorkedWith  :
    if i == '-1':
        rep_WebFrameWorkedWith.append(-1)
    if i != '-1':
        sum = 0
        cat = i.split(';')
        for j in cat:
            sum = d[ j ] + sum
        rep_WebFrameWorkedWith.append(sum) 
WebFrameWorkedWith = pd.DataFrame(rep_WebFrameWorkedWith)

df["WebFrameWorkedWith"] = WebFrameWorkedWith

MiscTechWorkedWith = df["MiscTechWorkedWith"]
MiscTechWorkedWith.fillna(value= '-1', inplace = True)
ls = []
for i in MiscTechWorkedWith  :    
    if i != '-1':
        cat = i.split(';')
        for j in cat:
            if j not in ls:
                ls.append(j)
d = dict(zip(set(ls), [1]*len(ls)))
rep_MiscTechWorkedWith   = []
for i in MiscTechWorkedWith  :
    if i == '-1':
        rep_MiscTechWorkedWith.append(-1)
    if i != '-1':
        sum = 0
        cat = i.split(';')
        for j in cat:
            sum = d[ j ] + sum
        rep_MiscTechWorkedWith.append(sum) 
MiscTechWorkedWith = pd.DataFrame(rep_MiscTechWorkedWith)

df["MiscTechWorkedWith"] = MiscTechWorkedWith

Containers = df["Containers"]
Containers.fillna(value= '-1', inplace = True )
ls = []
for i in Containers  :    
    if i != '-1':
        cat = i.split(';')
        for j in cat:
            if j not in ls:
                ls.append(j)
d = dict(zip(set(ls),[1]*len(ls)))
rep_Containers   = []
for i in Containers  :
    if i == '-1':
        rep_Containers.append(-1)
    if i != '-1':
        sum = 0
        cat = i.split(';')
        for j in cat:
            sum = d[ j ] + sum
        rep_Containers.append(sum) 
Containers = pd.DataFrame(rep_Containers)

df["Containers"] = Containers

import numpy as np
np.std(df['ConvertedComp'])

np.std(df['Hobbyist'])

df['WorkWeekHrs'] = df['WorkWeekHrs'].fillna((df['WorkWeekHrs'].mean()))

df['CodeRevHrs'] = df['CodeRevHrs'].fillna((df['CodeRevHrs'].mean()))

df['Age'] = df['Age'].fillna((df['Age'].median()))

df.isna().sum()

np.std(df['Age'])

df['Student'].unique()

cols = ['Hobbyist', 'OpenSourcer', 'Employment',
       'Country', 'Student', 'EdLevel', 'DevType',
       'YearsCode', 'YearsCodePro','ConvertedComp',
       'WorkWeekHrs', 'WorkPlan', 'WorkRemote', 'WorkLoc', 'ImpSyn',
       'LanguageWorkedWith', 'DatabaseWorkedWith', 'PlatformWorkedWith',
       'WebFrameWorkedWith', 'MiscTechWorkedWith', 'OpSys', 'Containers',
       'ITperson', 'OffOn', 'SocialMedia',
       'Age', 'Gender',
       'Trans', 'Sexuality', 'Dependents']
len(cols)

df.index

ls = []
for i in range(len(df["MainBranch"])):
  if df["MainBranch"][i] == 1:
    ls.append(i)
len(ls)
for i in range(len(df["ConvertedComp"])):
  if i in ls:
    df["ConvertedComp"][i] = 0

df["ConvertedComp"] = df["ConvertedComp"].fillna(value = df["ConvertedComp"].mean())
df["ConvertedComp"].isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

k = 20 
corrmat = df.corr()
cols = corrmat.nlargest(k, 'ConvertedComp')['ConvertedComp'].index 
  
cm = np.corrcoef(df[cols].values.T) 
f, ax = plt.subplots(figsize =(12, 10)) 
  
sns.heatmap(cm, ax = ax, cmap ="YlGnBu", 
            linewidths = 0.1, yticklabels = cols.values,  
                              xticklabels = cols.values)

'''newConvComp=[]
for i in df["ConvertedComp"]:
  newConvComp.append(i//200000)
df["ConvertedComp"]=newConvComp'''

from sklearn import preprocessing

cols = ['Hobbyist', 
        'OpenSourcer', 
        'Employment',
        'Country', 
        'Student', 
        'EdLevel', 
        'DevType',
       'YearsCode', 
        'YearsCodePro',
        'ConvertedComp',
       'WorkWeekHrs', 
        'WorkPlan', 
        #'WorkRemote', 
        'WorkLoc', 
        #'ImpSyn',
       'LanguageWorkedWith', 
        'DatabaseWorkedWith', 
        #'PlatformWorkedWith',
       'WebFrameWorkedWith', 
        #'MiscTechWorkedWith', 'OpSys', 'Containers',
       'Age', 'Gender', 'Trans', 'Sexuality', 'Dependents']

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler( feature_range= (0,1))

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(df[cols].drop(axis = 1, columns= "ConvertedComp"))
# Run the normalizer on the dataframe
df_normalized = pd.DataFrame(x_scaled)

import keras
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense,Dropout
from tensorflow.keras import regularizers

#cols = corrmat.nlargest(20, 'ConvertedComp')['ConvertedComp'].index 

cols = ['Hobbyist', 
        'OpenSourcer', 
        'Employment',
        'Country', 
        'Student', 
        'EdLevel', 
        'DevType',
       'YearsCode', 
        'YearsCodePro',
        'ConvertedComp',
       'WorkWeekHrs', 
        'WorkPlan', 
        #'WorkRemote', 
        'WorkLoc', 
        #'ImpSyn',
       'LanguageWorkedWith', 
        'DatabaseWorkedWith', 
        #'PlatformWorkedWith',
       'WebFrameWorkedWith', 
        #'MiscTechWorkedWith', 'OpSys', 'Containers',
       'Age', 'Gender', 'Trans', 'Sexuality', 'Dependents']

#X = df[cols].drop(axis =1, columns= 'ConvertedComp')
X = df[cols].drop(axis = 1, columns= "ConvertedComp")
y = df["ConvertedComp"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

my_callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=2),
    tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5'),
    tf.keras.callbacks.TensorBoard(log_dir='./logs'),
]

NN_model = Sequential()

# The Input Layer :
NN_model.add(Dense(32, kernel_initializer='normal',input_dim = X.shape[1], activation='relu'))

# The Hidden Layers :
NN_model.add(Dense(64, kernel_initializer='normal',activation='relu'))
NN_model.add(Dense(64, kernel_initializer='normal',activation='relu'))
NN_model.add(Dense(64, kernel_initializer='normal',activation='relu'))

# The Output Layer :
NN_model.add(Dense(1, kernel_initializer='normal',activation='linear'))

# Compile the network :
NN_model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])
NN_model.summary()

NN_model.fit(X_train, y_train, validation_data = (X_test,y_test), epochs=10, batch_size=32, callbacks = my_callbacks)

pred = NN_model.predict(X_test)
pred

d = X_test.iloc[11]
d = dict(d)
d = pd.DataFrame(d,index=[0])
pred = NN_model.predict(d)
pred

l = {'Age': 20.0,
 'Country': 8.0,
 'DatabaseWorkedWith': 52.0,
 'Dependents': 1.0,
 'DevType': 10.0,
 'EdLevel': 8.0,
 'Employment': 3.0,
 'Gender': 1.0,
 'Hobbyist': 1.0,
 'LanguageWorkedWith': 5.0,
 'OpenSourcer': 1.0,
 'Sexuality': 1.0,
 'Student': 1.0,
 'Trans': 1.0,
 'WebFrameWorkedWith': 5.0,
 'WorkLoc': 2.0,
 'WorkPlan': 4.0,
 'WorkWeekHrs': 100.0 ,
 'YearsCode': 9.0,
 'YearsCodePro': 2.0 }

l = pd.DataFrame(l,index=[0])
pred = NN_model.predict(l)
pred

'''NN_model.save('/content/drive/My Drive/developer_survey_2019/final_NN_model1.h5')
NN_model.save_weights('/content/drive/My Drive/developer_survey_2019/final_weights1.h5')
loaded_NN_model = tf.keras.models.load_model('/content/drive/My Drive/developer_survey_2019/final_NN_model1.h5')'''

'''d = X_test.iloc[25001]
d = dict(d)
d = pd.DataFrame(d,index=[0])
pred = loaded_NN_model.predict(d)
pred'''

'''import keras
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense,Dropout
from tensorflow.keras import regularizers

cols = corrmat.nlargest(20, 'ConvertedComp')['ConvertedComp'].index 

X = df.drop(axis =1, columns= 'ConvertedComp')
y = df["ConvertedComp"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

my_callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=2),
    tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5'),
    tf.keras.callbacks.TensorBoard(log_dir='./logs'),
]

model = Sequential()

model.add(Dense(units= 5, kernel_initializer = 'uniform', activation = 'relu', input_dim = X.shape[1]))
model.add(Dropout(0.5))

model.add(Dense(units= 5, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dropout(0.5))

model.add(Dense(units = 1 , kernel_initializer = 'uniform', activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])


model.fit(X_train, y_train, validation_data= (X_test,y_test) , batch_size = 10, epochs = 20, validation_split = 0.33, callbacks = my_callbacks)
'''

'''print("Generate predictions for samples")
predictions = model.predict(X_test)
print("predictions shape:", predictions.shape)
print("predictions :", pd.DataFrame(predictions).head(20))'''

'''import matplotlib.pyplot as plt
plt.hist(df['ConvertedComp'],bins = 10 ,range=(df['ConvertedComp'].unique().min(), df['ConvertedComp'].unique().max()) )'''


'''from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_classification

#cols = corrmat.nlargest(20, 'ConvertedComp')['ConvertedComp'].index 
X = df[cols].drop(axis =1 , columns = 'ConvertedComp')
y = df["ConvertedComp"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = RandomForestRegressor(max_depth=1 , random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
from sklearn.metrics import classification_report
print(clf.score(y_test,y_pred))
'''

'''
X = df.drop( axis =1  , columns = 'ConvertedComp' )
y = df["ConvertedComp"]

from keras.models import load_model
model = load_model('  developer_survey_2019/model1.h5')
model.load_weights("/content/drive/My Drive/developer_survey_2019/model_weights1.h5")
model.summary()'''

'''from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

pred = model.predict(X_test,verbose = 0)
results = model.evaluate(X_test, y_test, batch_size=10)

results'''

'''import tensorflow as tf

my_callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=2),
    tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5'),
    tf.keras.callbacks.TensorBoard(log_dir='./logs')]
loss = model.fit(X, y, batch_size = 10, epochs = 20, validation_split = 0.33, callbacks = my_callbacks)'''

'''import matplotlib.pyplot as plt

plt.plot(pd.DataFrame(loss.history) )'''

'''print("Generate predictions for samples")
predictions = model.predict(X_test)
print("predictions shape:", predictions.shape)
print("predictions :", pd.DataFrame(predictions))'''

