import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import time

vectorizer = joblib.load('vectorizer.pkl')
resp_vecs = joblib.load('resp_vecs.pkl')
df = pd.read_csv('df_match.csv')

#A placeholder for the user input skill list which initializes as the session starts
if 'skills_list' not in st.session_state: st.session_state.skills_list = []

st.set_page_config(page_title="Crafted Path", layout = "centered")
#st.title("Welcome to Crafted Path: A Skill-Based Job Matcher")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style.css")

st.markdown("<div class='custom-title'>Welcome to Crafted Path:<br> A Skill-Based Job Matcher 🔎 </div>", unsafe_allow_html=True)

st.sidebar.success("Select a page.")

if st.session_state.skills_list:
    st.markdown("<div class='sub-text1'>🧰 Your Skills:</div>", unsafe_allow_html=True)
    st.markdown(
        " ".join(
            [f"<span class='skill-bubble'>{skill}</span>" for skill in st.session_state.skills_list]
        ),
        unsafe_allow_html=True
    )

st.markdown("<div class='sub-text2'> 📝 Insert a Skill: </div>", unsafe_allow_html=True)
skill_input = st.text_input(" ", placeholder="e.g. Python", key = 'skill_input')

col1, col2 = st.columns([1,0.145])

with col1:
    if st.button("Add Skill"):
        skill = skill_input.strip()
        #st.session_state.skill_input=" "
        if not skill:
            st.warning("Please insert a skill before pressing 'Add Skill'.")
        elif len(st.session_state.skills_list) >= 5:
            st.warning("You've reached the 5 skills limit.")
        elif skill.lower() in [s.lower() for s in st.session_state.skills_list]: 
            st.info(f"'{skill}' already added.")
        else: 
            st.session_state.skills_list.append(skill)
            st.success(f"Skill Added ✅")
            time.sleep(1.5)
            st.experimental_rerun()

with col2:
    if st.button("Clear All"):
        st.session_state.skills_list=[]
        st.experimental_rerun()

if st.button("Find Jobs"):
    #st.session_state.skill_input=" "
    if not st.session_state.skills_list: st.warning("Please insert at least one skill.")
    else: 
        user_input = ' '.join(st.session_state.skills_list)
        user_input_vec = vectorizer.transform([user_input])
        similarity_scores = cosine_similarity(user_input_vec,resp_vecs).flatten()
        top_indices = similarity_scores.argsort()[::-1]
        top_matches = []
        seen = set()
        for idx in top_indices:
            job = df.loc[idx, 'job_position_name']
            if job not in seen:
                top_matches.append(job)
                seen.add(job)
            if len(top_matches)==3:
                break
        st.markdown("<div class='custom-success'>Top Job Matches 🎯</div>", unsafe_allow_html=True)
        for i, job in enumerate(top_matches,1):
            st.markdown(f"**{i}. {job}**")