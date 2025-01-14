import streamlit as st
from PIL import Image

import sys
sys.path.append(r'C:\Users\alimu\Desktop\webpage\PIL')

# -- page configuration
st.set_page_config(page_title="Hello from Ali!", page_icon=":tada:", layout="wide")


about_me_image = Image.open("images/about_me_picture.png")
work_exp_image = Image.open("images/work_exp_new_pic.png")
projects_image = Image.open("images/projects_picture.png")
leadership_and_volunteer_image = Image.open("images/lead_and_vol_pic.png")
sports_image = Image.open("images/sports_pic.png")
free_resources_image = Image.open("images/free_learning.png")


# -- Using our own local CSS file for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")



# -- Header section
with st.container(): # adding container is optional. Makes the code look clean.
    st.title("Hi, I am Ali! :wave:")
    st.subheader("A rising junior majoring in CS and Data science, passionate about Software Engineering with interest in AI/ML :desktop_computer: ")


# -- About me section
with st.container():
    st.write("---")
    left_column, right_column = st.columns((1, 2)) # code changed from st.column(2) to this.
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """
            🚀 Welcome to my Tech corner! As an aspiring Software Engineer and Product Manager, I am:\n
            💡 Proficient in Python and ML algorithms like regression and neural networks, engineering solutions that make use of Cloud and product development methodologies like Agile and Lean to tackle real-world challenges with precision.\n
            🌐 Utilize tools like Figma and excel in user research, navigating the complexities of product development.\n
            💼 Armed with a versatile and diverse skill set, I am ready to add value and grow your business with AI and data-driven approach!\n

            If this sounds interesting to you, lets [Connect!](https://www.linkedin.com/in/ali-muhammadnathani/)
            """
        )

    with right_column:
        st.image(about_me_image, width=450)



#right column code will go here with lottie file or just a jpeg

# -- Work Experience

with st.container():
    st.write("---")
    st.header("Work Experience ‍💼")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(work_exp_image)
    with text_column:
        st.subheader("Data Science Intern - Oeson Global Training and Internship Program")
        st.write(
            """
            Position starts in May 2024
            """
        )

with st.container():
    with text_column:
        st.subheader("Branding Strategy and Business Analytics Externship - Beats by Dre")
        st.write(
            """
            Position starts in July 2024
            """
        )

with st.container():
    #image_column, text_column = st.columns((1, 2))
    #with image_column:
        #st.image(img_contact_form)
    with text_column:
        st.subheader("Engineering Intern - UL Solutions")
        st.write(
            """
            Used SPEAG DASY8 to measure Specific Absorption Rate values for different electronic devices and analyzed all the data to find what devices were to be considered flawed.
            """
        )

with st.container():
    #image_column, text_column = st.columns((1, 2))
    #with image_column:
        #st.image(img_contact_form)
    with text_column:
        st.subheader("Manager - Student Center SMSU")
        st.write(
            """
            Managed a crew of 20 students for organizing campus wide events in coordination with over 15 student body committees. 
            """
        )

with st.container():
    #image_column, text_column = st.columns((1, 2))
    #with image_column:
        #st.image(img_contact_form)
    with text_column:
        st.subheader("Resident Assistant - Reslife SMSU")
        st.write(
            """
            Supervised and mentored a diverse community of over 30 residents, facilitating programming and demonstrating effective leadership.
            """
        )


# -- Projects

with st.container():
    st.write("---")
    st.header("Projects 🎨")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(projects_image)
    with text_column:
        st.subheader("Stock Price Predictor")
        st.write(
            """
            Utilizes ML (Random Forest) to predict stock price movements based on historical data of the S&P 500 index.\n
            [Source Code](https://github.com/AliNathanii/Stock-Price-Predictor)
            """
        )

with st.container():

    with text_column:
        st.subheader("CAD-Eng")
        st.write(
            """
            A web application that takes input in natural language and returns a 3D printing CAD File. \n
            [Source Code](https://github.com/AliNathanii/CAD-Eng)
            """
        )

with st.container():

    with text_column:
        st.subheader("Blogify")
        st.write(
            """
            A full-stack web application built using React, Node.js and MySQL where users can write and categorize blogs, upload media and form communities. \n
            [Source Code](https://github.com/AliNathanii/Blogify)
            """
        )


with st.container():
    #image_column, text_column = st.columns((1, 2))
    #with image_column:
        #st.image(img_contact_form)
    with text_column:
        st.subheader("Text Generator")
        st.write(
            """
            Using an LSTM-based neural network to generate text based on an input seed text, providing predictions for the next word and generating new text sequences.\n
            [Source Code](https://github.com/AliNathanii/Text-Generator)
            """
        )


# -- Leadership and Volunteer section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Leadership and Volunteer 🤝")
        st.write("##")
        st.subheader("Leadership Council Member - American Pakistan Foundation")
        st.write(
            "Areas of focus: Networking, Professional Development, Mentoring and Guidance.\n"
            "\nContributed to flagship programs APF Fellowships and UN Initiatives:"
            "\n- The APF Fellowship places U.S. based students and professionals with organizations focused on Pakistan-centric initiatives, helping them gain global awareness, analytical skills, career development, and mentorship opportunities."
            "\n- The UN Initiative connects Pakistan civil society organizations with the UN, offering U.S. students and organizations opportunities to engage in UN dialogues on Pakistan. Our six-month fellowship provides exposure to the UN ECOSOC, attendance at UN meetings, and research on Sustainable Development Goals (SDGs)."
        )
        st.write("[American Pakistan Foundation](https://www.americanpakistan.org/)")

    with right_column:
        st.image(leadership_and_volunteer_image, width=650)




with st.container():
    #image_column, text_column = st.columns((1, 2))
    #with image_column:
        #st.image(img_contact_form)
    with left_column:
        st.subheader("Vice President - CS Club SMSU")
        st.write(
            """
            Provided strong leadership support to the president, including organizing and executed multiple webinars and speaker events.\n
            Represented the school at numerous competitive programming competitions like Digi-key DKC, ICPC and Data Derby.\n
            [Computer Science Club SMSU](https://southwestmsu.campuslabs.com/engage/organization/computer-science)
            """
        )


# --  Outside classroom section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("🏏 Outside the classroom")
        st.write("##")

        st.write(
            """
            🏈 San Francisco 49ers\n
            🏓 Felix Lebrun\n
            ⚾ Minnesota Twins\n
            🏏 Australia\n
            🏎️ Mercedes-AMG PETRONAS F1 Team\n
            🎮 Fortnite\n
            📺 F.R.I.E.N.D.S\n
            🎬 Interstellar\n
            """
        )
    with right_column:
        st.image(sports_image, width=650)

# -- Free resources section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("📚 Free Resources for students")
        st.subheader("Looking for some extra help with classes? Here are my notes from CS/MATH classes I have taken so far!")
        st.write("##")
        st.write(
            """
             [Precalculus](https://drive.google.com/drive/folders/1-2bLhWbvtnWQ7bHJC1plBNJrS_evb9eV?usp=drive_link)\n
             [Calculus 1](https://drive.google.com/drive/folders/1-4W2LOmjj885Tde8WldtKhivBu6sy4u_?usp=drive_link)\n
             [Calculus 2](https://drive.google.com/drive/folders/1-7D9We-LyqCwhXTMa_F7GJmKloXeO7pp?usp=drive_link)\n
             [Foundations of/Discrete Mathematics](https://drive.google.com/drive/folders/1-5J2QPnsjuWvpI440LUaPpXsb-iDM10x?usp=drive_link) \n
             [Combinatorics and Graph Theory](https://drive.google.com/drive/u/0/folders/1-NtVW_hWD6-zjw9CTj6p5Qa7N7Abo0QJ)\n
             [Linear Algebra](https://drive.google.com/drive/u/0/folders/1-Jc8573qS5SeTpkxlBK3Txykrrc4SuJj)\n
            """
        )
        st.write("Feel free to share this with your friends and reach out if you have any questions. Happy to help!")
    with right_column:
        st.image(free_resources_image, width=650)

# -- Contact form
with st.container():
    st.write("---")
    st.header("Still here? Let's talk!")
    st.write("##")

    # Documentation for the form submit tool/website
    contact_form = """
    <form action="https://formsubmit.co/ali.nathani201@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name..." required>
     <input type="email" name="email" placeholder="Your email address..." required>
     <textarea name="message" placeholder="Type your message here..." required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.subheader("[LinkedIn](https://www.linkedin.com/in/ali-muhammadnathani/) | [GitHub](https://github.com/AliNathanii) | [X](https://twitter.com/AliNathanii)")
        st.write("💡 Fun fact: All pictures on this site, except my own, were generated by the DALL-E 3 model. Gotta love technology!")


# -- Bottom Footer All rights Reserved

# Reserve space for the footer
footer_placeholder = st.empty()

# Define the footer with improved styling
footer = """
    <style>
    .footer {
        position: relative;
        bottom: 0;
        width: 100%;
        color: white;
        text-align: center;
        padding: 10px 0;
        margin-top: 20px;
    }
    </style>
    <div class="footer">
        <p>&copy; 2025 Ali-Muhammad Nathani. All rights reserved.</p>
    </div>
    """

# Display the footer in the reserved space
footer_placeholder.markdown(footer, unsafe_allow_html=True)



# -- Last edited 12/01/2025
# Changes made: Added LA and Combinatorics notes hyperklinks and all rights reserved changed!

# To run this app on your device to see the changes etc: (assuming streamlit is downloaded and venv is not being used or activated)
# 1. run the command: streamlit run app.py in address
# or the command: streamlit run /Users/alimuhammad/Desktop/Personal Projects Master/Personal Projects/webpage/app.py

# if venv is being used ie activated:
# 1. --download or setup and activate a virtual env, download streamlit on that and then run!
# * but streamlit globally downloaded so we are good to go with the above one at this point!
# * without the virt env, use python3 -m pip install <package name> to download something in your mac terminal

# Instructions on deploying this webapp:
# 1. git add "name of the file".py ie app.py
# 2. git commit -m "message for this commit, the changes that you made"
# 3. git push heroku master
# *4. heroku ps:scale web=1 to make sure you stay on the free tier V.IMP
