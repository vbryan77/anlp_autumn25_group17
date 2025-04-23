import streamlit as st

st.title("About Us")
st.markdown("""**Welcome to Crafted Path: A Skill-Based Job Matcher**
            
🛤️ **Crafted Path** is a web application that helps you find career options based on your skills and proficiencies. 
Whether you are trying to explore new opportunities or career pathways, this tool is built to guide your path 

✅ **What Crafted Path Does:**
1. Insert up to five skills
2. Get real-time job recommendations using skill similarity
3. Discover new roles and career paths

The app utilises **TF-IDF** to help vectorise your list of skills. **Cosine Similarity** is computed in the background between the skills you have against the job descriptions in different roles. The top three matches are then shown instantly
    
Skills-based hiring is on the rise, as well as a more competitive job market landscape. Crafted Path helps you to:
1. Focus on what you can do and is already good at, not just focusing on your previous job titles
2. Explore transferable career paths (in regards to skill) with confidence

**The app is build with:**
- Pandas
- Cosine Similarity
- TfidVectorizer
- Streamlit
- Data ('Resume Dataset' by Saugata Roy Arghya on Kaggle)
            
🤝 **Developed By**: Pranav Sathyababu, Musaib Alam, Stark Fu, Bryan
           
            """)