# -*- coding: utf-8 -*-
"""
Created on Sun June 05 15:01:17 2020

"""

import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle as pkl
#import matplotlib
#matplotlib.use('TkAgg')
#import matplotlib.image as mp


st.title('Hello user')

#img = mp.imread("heart2.png")
#st.image(img)


st.sidebar.header('User, please give your inputs for the following questions : ')

svm_model = pkl.load(open('final_model_svm.p','rb'))


def user_input_features(Company,Experience,Job_Post_History,Location,Salary,Skills):


    if Company== "Accenture":
        Company = 0
    elif Company == "Air Products":
        Company = 1
    elif Company == "Aspire Systems":
        Company = 2
    elif Company == "Associated Auto Solutions International Pvt. Ltd.":
        Company = 3
    elif Company == "BNY Mellon":
        Company = 4
    elif Company== "Citibank, N.A":
        Company = 5
    elif Company == "CoinDCX":
        Company = 6
    elif Company == "Company3 Method India Private Limited":
        Company = 7
    elif Company == "CompuCom":
        Company = 8
    elif Company == "Credit Suisse":
        Company = 9
    elif Company == "Duff & Phelps":
        Company = 10
    elif Company == "Eversendai":
        Company = 11
    elif Company == "HealthSpring":
        Company = 12
    elif Company == "Icon Clinical Research":
        Company = 13
    elif Company == "Icon Pharmaceutical s":
        Company = 14
    elif Company == "Kraftmaid Services India":
        Company = 15
    elif Company == "Method Studios":
        Company = 16
    elif Company == "NatWest Group":
        Company = 17
    elif Company == "Oracle":
        Company = 18
    elif Company == "Prodair Air Products":
        Company = 19
    elif Company == "RRD":
        Company = 20
    elif Company == "Rave Technologies":
        Company = 21
    elif Company == "Shell":
        Company = 22
    elif Company == "Siemens":
        Company = 23
    elif Company == "Snaphunt":
        Company = 24
    elif Company == "Sona Comstar":
        Company = 25
    elif Company == "Thinksynq Solutions":
        Company = 26
    else:
        Company = 27



    if Experience == "0-2 Yrs":
        Experience = 0
    elif Experience == "0-3 Yrs":
        Experience = 1
    elif Experience == "0-4 Yrs":
        Experience = 2
    elif Experience == "0-5 Yrs":
        Experience = 3
    elif Experience == "1-3 Yrs":
        Experience = 4
    elif Experience == "1-4 Yrs":
        Experience = 5
    elif Experience == "12-15 Yrs":
        Experience = 6
    elif Experience == "2-3 Yrs":
        Experience = 7
    elif Experience == "2-4 Yrs":
        Experience = 8
    elif Experience == "2-6 Yrs":
        Experience = 9
    elif Experience == "2-7 Yrs":
        Experience = 10
    elif Experience == "3-5 Yrs":
        Experience = 11
    elif Experience == "3-6 Yrs":
        Experience = 12
    elif Experience == "3-7 Yrs":
        Experience = 13
    elif Experience == "3-8 Yrs":
        Experience = 14
    elif Experience == "4-6 Yrs":
        Experience = 15
    elif Experience == "4-8 Yrs":
        Experience = 16
    elif Experience == "4-9 Yr":
        Experience = 17
    elif Experience == "5-10 Yrs":
        Experience = 18
    else:
        Experience = 19



    if Job_Post_History == "1 Day Ago":
        Job_Post_History = 0
    elif Job_Post_History == "10 Days Ago":
        Job_Post_History = 1
    elif Job_Post_History == "12 Days Ago":
        Job_Post_History = 2
    elif Job_Post_History == "14 Days Ago":
        Job_Post_History = 3
    elif Job_Post_History == "2 Days Ago":
        Job_Post_History = 4
    elif Job_Post_History == "3 Days Ago":
        Job_Post_History = 5
    elif Job_Post_History == "4 Days Ago":
        Job_Post_History = 6
    elif Job_Post_History == "5 Days Ago":
        Job_Post_History = 7
    elif Job_Post_History == "8 Days Ago":
        Job_Post_History = 8
    else:
        Job_Post_History = 9


    if Location == "Chennai":
        Location = 0
    elif Location == "Chennai(Ekkaduthangal)":
        Location = 1
    elif Location == "Chennai(Kodambakkam), Kodambakkam":
        Location = 2
    elif Location == "Chennai(Teynampet)":
        Location = 3
    elif Location == "Chennai, Hyderabad/Secunderabad, Pune, Delhi / NCR, Bangalore/Bengaluru, Mumbai (All Areas)":
        Location = 4
    elif Location == "Mumbai":
        Location = 5
    elif Location == "Mumbai (All Areas)":
        Location = 6
    elif Location == "Mumbai (All Areas), Hyderabad/Secunderabad, Pune, Chennai, Delhi / NCR, Bangalore/Bengaluru":
        Location = 7
    elif Location == "Mumbai, Gurgaon/Gurugram, Aurangabad, Vadodara":
        Location = 8
    elif Location == "Pune":
        Location = 9
    else:
        Location = 10


    if Salary == "11,00,000 - 20,00,000 PA.":
        Salary = 0
    elif Salary == "4,00,000 - 6,00,000 PA.":
        Salary = 1
    elif Salary == "4,00,000 - 9,00,000 PA.":
        Salary = 2
    elif Salary == "4,50,000 - 7,00,000 PA.":
        Salary = 3
    elif Salary == "5,00,000 - 12,00,000 PA.":
        Salary = 4
    elif Salary == "5,00,000 - 14,00,000 PA.":
        Salary = 5
    elif Salary == "7,00,000 - 15,00,000 PA.":
        Salary = 6
    elif Salary == "8,00,000 - 13,00,000 PA.":
        Salary = 7
    else:
        Salary = 10


    if Skills == "Analysis":
        Skills = 0
    elif Skills == "Analyst":
        Skills = 1
    elif Skills == "Analytical skills":
        Skills = 2
    elif Skills == "Associate Financial Analyst":
        Skills = 3
    elif Skills == "Assurance":
        Skills = 4
    elif Skills == "Automation":
        Skills = 5
    elif Skills == "Due diligence":
        Skills = 6
    elif Skills == "Dynamics 365":
        Skills = 7
    elif Skills == "ERP":
        Skills = 8
    elif Skills == "Finance":
        Skills = 9
    elif Skills == "Financial Analysis":
        Skills = 10
    elif Skills == "Financial Analyst":
        Skills = 11
    elif Skills == "Financial analysis":
        Skills = 12
    elif Skills == "Financial planning":
        Skills = 13
    elif Skills == "Financial reporting":
        Skills = 14
    elif Skills == "Financial statements":
        Skills = 15
    elif Skills == "KYC":
        Skills = 16
    elif Skills == "Microstrategy":
        Skills = 17
    elif Skills == "Oracle Fusion Finance":
        Skills = 18
    elif Skills == "Post production":
        Skills = 19
    elif Skills == "Power Bi Reports":
        Skills = 20
    elif Skills == "R12":
        Skills = 21
    elif Skills == "Structured Finance":
        Skills = 22
    elif Skills == "Team management":
        Skills = 23
    elif Skills == "business analysis":
        Skills = 24
    elif Skills == "data analyses":
        Skills = 25
    elif Skills == "equity research":
        Skills = 26
    elif Skills == "finance":
        Skills = 27
    elif Skills == "financial analysis":
        Skills = 28
    elif Skills == "financial data analysis":
        Skills = 29
    elif Skills == "financial forecasting":
        Skills = 30
    elif Skills == "financial reporting":
        Skills = 31
    elif Skills == "general ledger":
        Skills = 32
    else:
        Skills = 33


    user_input=[Company,Experience,Job_Post_History,Location,Salary,Skills]
    user_input=np.array(user_input)
    #st.subheader('User inserted values')
    #st.write(user_input)
    user_input=user_input.reshape(1,-1)
    prediction = svm_model.predict(user_input)

    return prediction


Company = st.sidebar.selectbox('Select the Company : ',['Accenture', 'CoinDCX', 'Oracle', 'Siemens',
                                                      'Rave Technologies', 'HealthSpring', 'Citibank, N.A', 'Snaphunt', 'Duff & Phelps',
                                                       'BNY Mellon', 'Credit Suisse', 'Prodair Air Products',
                                                       'Air Products', 'Ubisoft', 'CompuCom', 'Kraftmaid Services India',
                                                       'Method Studios', 'Company3 Method India Private Limited ', 'RRD',
                                                         'Thinksynq Solutions', 'Shell', 'Icon Clinical Research',
                                                           'Aspire Systems', 'Icon Pharmaceutical s',
                                                           'Associated Auto Solutions International Pvt. Ltd.',
                                                           'Sona Comstar', 'NatWest Group', 'Eversendai'])
Experience = st.sidebar.selectbox('How much experience do you have?',['5-8 Yrs', '1-3 Yrs', '5-10 Yrs', '0-5 Yrs', '4-6 Yrs', '3-5 Yrs',
                                                                      '4-9 Yrs', '12-15 Yrs', '0-3 Yrs', '0-2 Yrs', '2-7 Yrs', '3-6 Yrs',
                                                                        '2-3 Yrs', '3-7 Yrs', '1-4 Yrs', '2-6 Yrs', '0-4 Yrs', '3-8 Yrs',
                                                                        '4-8 Yrs', '2-4 Yrs'])
Job_Post_History = st.sidebar.selectbox('Date on which the Job was posted?',['1 Day Ago', '5 Days Ago', '4 Days Ago', '8 Days Ago', '9 Days Ago', '2 Days Ago', '10 Days Ago', '3 Days Ago', '12 Days Ago', '14 Days Ago'])
Location = st.sidebar.selectbox("Location of the Job?",['Mumbai',
                                                       'Mumbai (All Areas), Hyderabad/Secunderabad, Pune, Chennai, Delhi / NCR, Bangalore/Bengaluru', 'Mumbai, Gurgaon/Gurugram, Aurangabad, Vadodara',
                                                           'Mumbai (All Areas)', 'Pune, Hyderabad/Secunderabad, Chennai, Delhi / NCR, Bangalore/Bengaluru, Mumbai (All Areas)', 'Pune',  'Chennai, Hyderabad/Secunderabad, Pune, Delhi / NCR, Bangalore/Bengaluru, Mumbai (All Areas)', 'Chennai', 'Chennai(Teynampet)', 'Chennai(Ekkaduthangal)', 'Chennai(Kodambakkam), Kodambakkam'])
Salary = st.sidebar.selectbox("Select your salary expectations from below : ",['Not disclosed', '4,00,000 - 9,00,000 PA.', '11,00,000 - 20,00,000 PA.', '5,00,000 - 12,00,000 PA.', '4,00,000 - 6,00,000 PA.', '8,00,000 - 13,00,000 PA.', '4,50,000 - 7,00,000 PA.', '5,00,000 - 14,00,000 PA.', '7,00,000 - 15,00,000 PA.'])
Skills = st.sidebar.selectbox('Which of the following Skillset do you have?',['Due diligence', 'Analyst', 'Oracle Fusion Finance', 'Analytical skills', 'Associate Financial Analyst', 'Financial analysis', 'financial forecasting', 'financial reporting', 'Team management', 'finance', 'financial data analysis', 'Structured Finance', 'Automation',
                                                'general ledger', 'Financial Analysis', 'Financial statements', 'Microstrategy', 'financial analysis', 'R12', 'Post production', 'Dynamics 365', 'Financial reporting', 'Finance',       'investment banking', 'ERP', 'Analysis', 'Financial planning', 'equity research', 'Assurance', 'data analyses', 'Power Bi Reports', 'Financial Analyst', 'KYC', 'business analysis'])

prediction = user_input_features(Company,Experience,Job_Post_History,Location,Salary,Skills)


st.subheader('Following is the best suitatable Job for you : ')

def result():
    if prediction == 0:
        results = "Analyst I, Global Financial Data Operations"
    elif prediction == 1:
        results = "Analyst-Finance Processes"
    elif prediction == 2:
         results = "Analyst-Finance Processes and Operations"
    elif prediction == 3:
        results = "Business Analyst - Finance"
    elif prediction == 4:
        results = "Business Analyst /Peoplesoft / finance modules / General ledger"
    elif prediction == 5:
        results = "Consultant / Analyst - Finance"
    elif prediction == 6:
        results = "Finance Analyst"
    elif prediction == 7:
        results = "Finance Analyst\n"
    elif prediction == 8:
        results = "Finance Reporting Analyst"
    elif prediction == 9:
        results = "Financial / Research Analyst - Corporate Development"
    elif prediction == 10:
        results = "Financial Analyst"
    elif prediction == 11:
        results = "Financial Analyst "
    elif prediction == 12:
        results = "Financial Analyst II @ ICON | Spot Offer"
    elif prediction == 13:
        results = "Financial Crime Operations Analyst"
    elif prediction == 14:
        results = "Financial Planning Analyst"
    elif prediction == 15:
        results = "Immediate Hiring For Financial Analyst"
    elif prediction == 16:
        results = "Lead Analyst, Financial Planning & Analysis"
    elif prediction == 17:
        results = "Lead/Senior Analyst Structured finance - 2 To 10 years BNY Mellon Pune"
    elif prediction == 18:
        results = "Manager/ Analyst- Business Finance & M&A"
    elif prediction == 19:
        results = "Oracle Financial Analyst"
    elif prediction == 20:
        results = "Oracle Fusion Finance Analyst"
    elif prediction == 21:
        results = "R&A Int. Lubes Finance Analyst - IT"
    elif prediction == 22:
        results = "R&A Int. Lubes Finance Analyst - OM/EG"
    elif prediction == 23:
        results = "RA Marine Finance Analyst"
    elif prediction == 24:
        results = "SAP FI CO Finance Business Analyst"
    elif prediction == 25:
        results = "Senior Analyst-Finance Processes and Operations"
    elif prediction == 26:
        results = "equity research"
    elif prediction == 27:
        results = "Senior Financial Analyst"
    elif prediction == 28:
        results = "Senior Financial Associate/Financial Analyst/Senior Financial Analyst"
    else:
        results = "Sr. Associate - Financial Analyst"
    return results


results = result()
st.write(results)


#Inserting graphs and diagrams


df=pd.read_csv("final_data.csv",index_col=0, encoding = "utf-8")



#Ttitlewise

st.title('Based on Title')

most_jobs = df.Title.value_counts().head(25)*100/df.Title.count()
most_jobs

sns.set_style("whitegrid")
fig1=plt.figure(figsize = (8,12))
pal = sns.color_palette("pastel", len(most_jobs.index))
rank = most_jobs.argsort().argsort()
sns.barplot(x = most_jobs, y = most_jobs.index, palette=np.array(pal[::])[rank]);
st.pyplot(fig1)


#Based on Company

st.title('Based on Company')

most_company = df.Company.value_counts().head(15)*100/df.Company.count()
most_company

sns.set_style("whitegrid")
fig2=plt.figure(figsize = (8,12))
pal = sns.color_palette("pastel", len(most_company.index))
rank = most_company.argsort().argsort()
sns.barplot(x = most_company, y = most_company.index, palette=np.array(pal[::])[rank]);
st.pyplot(fig2)


#Based on Experience

st.title('Based on Experience')

most_exp = df.Experience.value_counts().head(25)*100/df.Experience.count()
most_exp

sns.set_style("whitegrid")
fig3=plt.figure(figsize = (8,12))
pal = sns.color_palette("pastel", len(most_exp.index))
rank = most_exp.argsort().argsort()
sns.barplot(x = most_exp, y = most_exp.index, palette=np.array(pal[::])[rank]);
st.pyplot(fig3)


#Job posted on

st.title('Date on which Job was posted')

job_posted_on = df['Job_Post_History'].value_counts()
job_posted_on

sns.set_style("whitegrid")
fig, ax = plt.subplots()
plt.figure(figsize=(15, 5))
plt.title("Job Distribution based on date it was posted on", fontsize = 20)
plt.xlabel("Date", fontsize = 18)
plt.ylabel("No. of Jobs", fontsize = 18)
bar2 = plt.bar(job_posted_on.index, job_posted_on.values, color='Green')
plt.xticks(rotation = 90);
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}', ha='center', va='bottom')
plt.tight_layout()
fig4=plt.show();
st.pyplot(fig4)
st.set_option('deprecation.showPyplotGlobalUse', False)


#Locationwise

st.title('Based on Location')

job_citywise = df['Location'].value_counts()
job_citywise

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
fig, ax = plt.subplots()
plt.figure(figsize=(15, 5))
plt.title("Citywise Job Distribution", fontsize = 20)
plt.xlabel("City", fontsize = 18)
plt.ylabel("No. of Jobs", fontsize = 18)
bar1 = plt.bar(job_citywise.index, job_citywise.values, color='Blue')
plt.xticks(rotation = 90);
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}', ha='center', va='bottom')
plt.tight_layout()
#plt.bar1.savefig('loc.png')
fig5=plt.show();
st.pyplot(fig5)
#st.pyplot(bar1)
st.set_option('deprecation.showPyplotGlobalUse', False)


#Based on Salary

st.title('Based on Salary')

salary = df['Salary'].value_counts()
salary

sns.set_style("whitegrid")
plt.figure(figsize=(15, 10))
plt.title("Job Distribution based Salary", fontsize = 20)
plt.xlabel("Salary", fontsize = 18)
plt.ylabel("No. of Jobs", fontsize = 18)
bar2 = plt.bar(salary.index, salary.values, color='Magenta')
plt.xticks(rotation = 90);
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}', ha='center', va='bottom')
plt.tight_layout()
fig6=plt.show();
st.pyplot(fig6)
st.set_option('deprecation.showPyplotGlobalUse', False)


#Based on Skills

st.title('Based on Skills')

most_skills = df.Skills.value_counts().head(25)*100/df.Skills.count()
most_skills

sns.set_style("whitegrid")
fig7=plt.figure(figsize = (8,12))
pal = sns.color_palette("pastel", len(most_skills.index))
rank = most_skills.argsort().argsort()
sns.barplot(x = most_skills, y = most_skills.index, palette=np.array(pal[::])[rank]);
st.pyplot(fig7)




#prediction = loaded_model1.predict(df)
#prediction_proba = loaded_modl.predict_proba(df)

#st.subheader('Prediction Probability')
#st.write(prediction_proba)

#st.subheader('Predicted Result')
#if btn is True:
#    st.write('Heart disease detected' if prediction_proba[0][1] > 0.5 else 'You do not have a heart disease')
