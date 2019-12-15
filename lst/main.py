import numpy as np
import pandas as pd
np.random.uniform(0.85,0.90,(6,1))
index=np.arange(0,238)
columns=[]
columns_name=['gender','Is a freshman','Whether to start the question on time','Undergraduate school level','Number of students supervised by instructor','Average grades for degree courses','Number of SCI articles published in three years of enrollment','Number of SCI articles published within 4 years of enrollment','Number of EI articles published three years after enrollment','Total articles published in admissions']
x=pd.DataFrame(index=index,columns=columns_name,data=np.nan)
rand=np.random.randint(0,2,(238,1))
h=np.array(x['Is a freshman'].map({1:'male',0:'female'}))
rand=np.random.randint(0,2,(238,1))
y=np.random.randint(0,2,(238,1))
x['Is a freshman']=y
z=np.random.randint(0,2,(238,1))
x['Whether to start the question on time']=z
q=np.random.randint(0,3,(238,1))
x['Undergraduate school level']=q
n=np.random.randint(0,15,(238,1))
x['Number of students supervised by instructor']=n
x['Is a freshman']=np.array(x['Is a freshman'].map({1:'yes',0:'no'}))
x['Whether to start the question on time']=np.array(x['Whether to start the question on time'].map({1:'yes',0:'no'}))
x['Undergraduate school level']=np.array(x['Undergraduate school level'].map({1:'211',2:'985',0:'general'}))

x['Number of SCI articles published in three years of enrollment']=np.random.randint(0,5,(238,1))
x['Number of EI articles published three years after enrollment']=np.random.randint(0,5,(238,1))
x['Total articles published in admissions']=x['Number of SCI articles published in three years of enrollment']+x['Number of EI articles published three years after enrollment']+np.random.randint(0,2)
del x['Number of SCI articles published within 4 years of enrollment']
x['Average grades for degree courses']=np.random.normal(76,5,(238,1))
x['gender']=np.random.randint(0,2,(238,1))
x['gender']=x['gender'].map({1:'male',0:'female'})
x.describe()
x['Delay time']=np.round(np.abs(np.random.normal(0,2,(238,1))),1)
x.columns
x.to_csv('dsadsa2.csv',index=True,header=True)
y=x.iloc[:,:-1]
y.head(30)
y.groupby(by=['gender','Undergraduate school level','Is a freshman','Whether to start the question on time']).median()
h=x.groupby(by=['gender','Undergraduate school level','Is a freshman','Whether to start the question on time']).median()

