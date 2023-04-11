import pickle
import streamlit as st
from win32com.client import Dispatch

def speak(text):
     speak=Dispatch(("SAPI.SpVoice"))
     speak.Speak(text)

model=pickle.load(open("spam.pkl", "rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))


def main():
    st.title("Email / SMS Spam Detector")
    st.subheader("Build with Streamlit & Python")
    msg=st.text_area("Enter your Message : ")
    col1, col2, col3 , col4, col5 = st.beta_columns(5)
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        if st.button("Predict"):
            data=[msg]
            vect = cv.transform(data).toarray()
            prediction = model.predict(vect)
            result = prediction[0]
        if result==1:
            st.error("This is a spam mail")
            speak("This is a spam mail")
        else:
              st.success("This is not a spam mail")
              speak("This is not a spam mail")


main()