import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report


df = pd.read_csv(r"C:\Users\lenovo\Downloads\archive (5)\IRIS.csv")

le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])

x = df.drop('species' , axis=1)
y = df['species']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=42)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

model = RandomForestClassifier(n_estimators=100 , random_state=42)
model.fit(x_train,y_train)


y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)

st.title ('🌸 Iris Flower Classification')
st.write (f"**Model Accuracy :** {acc:.2f}")

st.header('Enter the flower measurements:')

sl = st.number_input('Sepal Length (cm)' , min_value = 4.3,max_value = 7.9)
sw = st.number_input('Sepal Width (cm)' , min_value = 2.0,max_value = 4.4)
pl = st.number_input('Petal Length (cm)' , min_value = 1.0,max_value = 6.9)
pw = st.number_input('Petal Width (cm)' , min_value = 0.1,max_value = 2.5)

if st.button('Classify'):
    try:
        input_data =[[sl,sw,pl,pw]]
        input_scaled  = sc.transform(input_data)
        predict = model.predict(input_scaled)
        flower_species = le.inverse_transform(predict)
        st.success(f'The Iris flower species is : **{flower_species[0]}** ')
    except Exception as e:
        st.error(f'Error : {e}')
