import pickle
import numpy as np 
from scipy.sparse import hstack

with open('model.pkl','rb') as f:
    model = pickle.load(f)
    
with open('tfidf.pkl','rb') as f:
    tfidf = pickle.load(f)
    
ALL_COLUMNS = ['telecommuting', 'has_company_logo', 'has_questions', 
 'employment_type_Contract', 'employment_type_Full-time', 
 'employment_type_Other', 'employment_type_Part-time', 
 'employment_type_Temporary', 'employment_type_Unknown', 
 'required_experience_Associate', 'required_experience_Director', 
 'required_experience_Entry level', 'required_experience_Executive', 
 'required_experience_Internship', 'required_experience_Mid-Senior level', 
 'required_experience_Not Applicable', 'required_experience_Unknown', 
 'required_education_Associate Degree', "required_education_Bachelor's Degree", 
 'required_education_Certification', 'required_education_Doctorate', 
 'required_education_High School or equivalent', "required_education_Master's Degree", 
 'required_education_Professional', 'required_education_Some College Coursework Completed', 
 'required_education_Some High School Coursework', 'required_education_Unknown', 
 'required_education_Unspecified', 'required_education_Vocational', 
 'required_education_Vocational - Degree', 'required_education_Vocational - HS Diploma']
