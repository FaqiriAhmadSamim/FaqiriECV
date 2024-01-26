from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | FAQIRI"
PAGE_ICON = "ℹ️"
NAME = "AHMAD SAMIM FAQIRI"
DESCRIPTION = """
Competent IT specialist with 12 years of working experience.
"""
EMAIL = "a.samim.faqiri@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/samim.faqirii",
    "LinkedIn": "https://www.linkedin.com/in/ahmad-samim-faqiri-6838156a/",
    "GitHub": "https://github.com/FaqiriAhmadSamim",
    "Twitter": "https://twitter.com/Samimkhan11",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Educations")
st.write(
    """
- ✔️ Master of Computer Science and Technology from H.I.T (Harbin Institute of Technology), Harbin- China/ Sep- 2022 to July 2024
- ✔️ Bachelor of Computer Science From Bakhtar University, Kabul- Afghanistan/ Nov- 2009 to April- 2013
- ✔️ 12th grade- Baccalaureate Degree from Habibia High School, Kabul- Afghanistan/ April- 2003 to December- 2006
- ✔️ IT Diploma (DIT) from Logix Institute of IT , Kabul- Afghanistan/ Aug-2006 to Aug- 2007
- ✔️ Certificate of Proficiency in Web Designing from Aptech, New Delhi- India/ Oct 2013 to Jan 2014
- ✔️ Website Designing and Developing Specialist Aptech, Kabul- Afghanistan/ May 2014 to Oct 2014
"""
)
st.write('\n')
st.subheader("Experience")
st.write(
    """
- ✔️ 4 Years ICT Director at MUDL- Afghanistan Government
- ✔️ 4 Years Web and MIS Manager at MUDH- Afghanistan Government
- ✔️ Around 1 Year Web and MIS Manager at MUDH- Afghanistan Government
- ✔️ 2 Years ICT Officer and MIS team member at MUDH- Afghanistan Government 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Excellent leadership, and interpersonal skills.
- 📊 Advanced decision making and problem solving skills.
- 📚 Strong team leading skills.
- 🗄️ Ability to effectively priorities and execute tasks in a high- pressure environment.
- 📚 Knowledge- sharing and open communicator.
- 🤝 Ability to contribute to senior team performance.
- 📶 Help Desk Support and Computer Networking: installing, configuring, testing,
     and updating network hardware and software such as routers, switches, firewalls,
     servers and wireless access points; solving software and hardware problems on computers.
- 🧑‍💻 Programming, Databases and Modeling: Python (Streamlit), PHP (CodeIgniter);
     MySQL, Firebase; Logistic regression, SVM.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🧑🏼‍💼", "**IT Director | MUDL**")
st.write("Nov/ 2017 to Aug/ 2021")
st.write(
    """
- ► Improve networking backbone and connecting MUDL Provincial directorates.
- ► Technical advising to the top level management in implementing of E- governance.
- ► Technical instructing of MUDL- MIS team to improve MIS and implement E-governance.
- ► Monitor and advising MUDL ICT technical team.
- ► Install, configure and implement open sources operating systems.
- ► Technical instructing of MUDL- MIS team to improve MIS and implement E-governance.
"""
)

# --- JOB 2
st.write('\n')
st.write("🧑🏼‍💼", "**Web and MIS Manager | MUDH**")
st.write("Nov/ 2012 to Nov/ 2017")
st.write(
    """
- ► Analyzing clients' existing systems.
- ►	Writing user manuals.
- ►	Providing training to users.
- ►	Plan a system flow from the ground up.
- ►	Perform system testing.
- ►	Deploy the completed system.
- ►	Responsible to implement new system.
"""
)

# --- JOB 3
st.write('\n')
st.write("🧑🏼‍💼", "**IT Officer  | MUDH**")
st.write("Jan/ 2010 to Oct/2012")
st.write(
    """
- ► Performed Troubleshoot and repair of all hardware and network operating system
- ►	Provided solutions to the problems of hardware/software and internet related services
- ►	Maintained and configured LAN/WLAN Performed hardware installation and removal
- ► Repaired scanners, copy machines, printers and other equipment
- ►	Maintained a system of safety backups and the disaster recovery process
- ► Monitored security of all technology
- ►	Installed, configured, and optimized operating systems
- ► Provided technical support to systems administrators, database administrators and network engineers
"""
)