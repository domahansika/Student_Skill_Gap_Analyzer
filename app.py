import streamlit as st
st.title("🎯Student Skill Gap Analyzer")
st.caption("Assess your current skills and identify what to learn for your target career.")
st.write("Build your career roadmap by comparing your current skills with the skills required for your target role.")
st.divider()
required_skills = {
    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Statistics",
        "Power BI"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Statistics",
        "Machine Learning",
        "Pandas"
    ],

    "Python Developer": [
        "Python",
        "OOP",
        "Git",
        "SQL",
        "APIs"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "Git",
        "APIs"
    ]
}
st.subheader("Choose your target role")
role = st.selectbox(
    "What job role are you preparing for?",
    list(required_skills.keys())
)

st.subheader("Select your current skills")
all_skills = [
    "Python",
    "SQL",
    "Excel",
    "Statistics",
    "Power BI",
    "Machine Learning",
    "Pandas",
    "OOP",
    "Git",
    "APIs",
    "HTML",
    "CSS",
    "JavaScript"
]
user_skills = st.multiselect(
    "Which skills do you currently have?",
    all_skills
)
role_skills = required_skills[role]
matched_skills = []
for skill in role_skills:
    if skill in user_skills:
        matched_skills.append(skill)
missing_skills = []
for skill in role_skills:
    if skill not in user_skills:
        missing_skills.append(skill)
match_percentage = (len(matched_skills) / len(role_skills)) * 100
st.subheader("💼 Role Skill Requirements")

st.write(f"Skills commonly considered for a **{role}** role:")

for skill in role_skills:
    st.write(f"🔹 {skill}")
st.divider()
st.subheader("📊 Your Skill Gap Analysis")
col1, col2 = st.columns(2)
with col1:
    st.metric(
        "📊 Skill Match",
        f"{match_percentage:.0f}%"
    )
with col2:
    st.metric(
        "🎯 Skills Matched",
        f"{len(matched_skills)} / {len(role_skills)}"
    )
st.progress(match_percentage / 100)
st.write("### ✅ Skills You Have")

if matched_skills:
    for skill in matched_skills:
        st.write(f"✅ {skill}")
else:
    st.write("No matching skills yet.")


st.write("### ❌ Skills You Need")

if missing_skills:
    for skill in missing_skills:
        st.write(f"❌ {skill}")
else:
    st.write("You have all the required skills!")
st.metric(
    "Skill Match",
    f"{match_percentage:.0f}%"
)
st.progress(match_percentage / 100)
if match_percentage < 40:
    st.warning("⚠️ You have a significant skill gap. Start with the missing skills.")
elif match_percentage < 80:
    st.info("📚 You have a good foundation. Focus on the remaining skills.")
else:
    st.success("🎉 Great! You have strong skill coverage for this role.")
if missing_skills:
    for skill in missing_skills:
        st.write(f"❌ {skill}")
else:
    st.write("You have all the required skills!")
st.write("### 📚 Learning Priority")
if missing_skills:
    for i, skill in enumerate(missing_skills, start=1):
        st.write(f"**Priority {i}:** Learn {skill}")
else:
    st.write("🎉 No new skills required!")
st.divider()
st.subheader("🗺️ Recommended Learning Path")
learning_topics = {
    "Python": "Learn Python basics, functions, lists, dictionaries and file handling.",
    "SQL": "Learn SELECT, WHERE, GROUP BY, JOIN and aggregate functions.",
    "Excel": "Learn formulas, lookup functions, pivot tables and data cleaning.",
    "Statistics": "Learn mean, median, probability, distributions and correlation.",
    "Power BI": "Learn data visualization, dashboards, Power Query and basic DAX.",
    "Machine Learning": "Learn regression, classification, model evaluation and preprocessing.",
    "Pandas": "Learn DataFrames, filtering, grouping, merging and data analysis.",
    "OOP": "Learn classes, objects, inheritance and encapsulation.",
    "Git": "Learn repositories, commits, branches, push, pull and GitHub.",
    "APIs": "Learn HTTP requests, JSON and how to consume REST APIs.",
    "HTML": "Learn page structure, forms, links and semantic HTML.",
    "CSS": "Learn selectors, layouts, Flexbox and responsive design.",
    "JavaScript": "Learn variables, functions, DOM manipulation and events."
}
if missing_skills:
    for skill in missing_skills:
        st.write(f"**{skill}**")
        st.write(learning_topics[skill])
else:
    st.write("🎉 You are ready to focus on advanced skills and projects!")
