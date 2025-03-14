# Salary-Prediction-for-Data-Science-Jobs-in-India
Built an ML Model to predict salaries for Data Science roles in India. Scraped job data from naukri, performed feature engineering, applied stacking regressor(R^2 = 0.85), and deployed using solara on Hugging Face.


🔗[Live App](https://shama7-Salary-Prediction-App.hf.space)

---

# Salary Prediction for Data Science Jobs in India    

## Project Overview   

This is a full end-to-end machine learning project focused on predicting salaries for data science-related job roles in India. The project covers web scraping, data preprocessing, feature engineering, model building, evaluation, and deployment. The final model is deployed using **Solara on Hugging Face Spaces.**   

## Problem Statement    

Many job postings do not disclose salary information, making it difficult for job seekers to estimate expected pay. This project predicts salaries based on job role, experience, location, company type, and other factors.


---


## Data Collection    

**Scraped 7,293** job postings from Naukri.com for **18 data-related roles:**    

Data Scientist, Data Analyst, ML Engineer, AI Engineer, Data Engineer, etc.      


Extracted 7 key columns: Role, Company Name, Experience, Salary, Location, etc.    

---


## Data Preprocessing & Feature Engineering     

#### 1. Feature Creation & Transformation

1. **Company Type**: Classified into 5 categories – MNC, Startup, Product-based, Service-based, Mid-size.   


2. **Experience Handling**: Converted experience ranges into average years of experience.   


3. **Location Cleaning**: Mapped duplicate and similar city names (e.g., Bengaluru → Bangalore).   


4. **Job Mode**: Classified jobs as Remote, Onsite, Hybrid.   


#### 2.Salary Prediction for Missing Values:  

Many job postings did not disclose salary, making salary prediction a major challenge.   

Manually scraped salary estimates from AmbitionBox for key roles.   

Used interpolation to estimate missing salaries based on experience.   

Applied city multipliers to adjust salaries based on location.   



#### 3. Final Dataset Size:

Initially scraped: 7,293 rows    

After salary estimation: 1,730 rows (used for model building).   

⚡ Expanding the dataset is part of future improvements.   



#### 4. Additional Features Created:

Salary Category, City Type, Region, Experience Level, Job Level.   

**Encoding**: Manually mapped categorical variables into numerical values.   

---



## Model Building & Evaluation

Train-Test Split: 80-20    

Applied multiple regression models:   

Best Individual Models:   

Random Forest, LightGBM, CatBoost, Gradient Boosting, XGBoost (R² > 0.80)    


## Final Model:

Stacking Regressor (Combining top 5 models)   

Performance:  

R² Score: 0.85    
  
MAE: 3.74   

RMSE: 5.43   

---



## Model Deployment   

Saved model using pickle.   

Deployed using Solara, a modern Python-based UI framework.    

Hosted on Hugging Face Spaces using Docker.   

🔗[Live App](https://shama7-Salary-Prediction-App.hf.space)

---


## Future Improvements

🚀 Expand dataset by manually estimating more salaries.   
🚀 Automate salary estimation using web scraping & NLP techniques.   
🚀 Improve model accuracy by experimenting with deep learning models.    

---


## Technologies Used

**Scraping: BeautifulSoup**    

**Data Processing: Pandas, NumPy**

**Visualization: Matplotlib, Seaborn**

**Machine Learning: Scikit-learn, XGBoost, LightGBM, CatBoost, Gradient Boosting, Random Forest, Stacking Regressor**

**Deployment: Solara, Hugging Face Spaces, Docker**


---


## Key Takeaways

✅ **End-to-end ML project**, covering everything from **scraping to deployment.**      
✅ Solves a real-world problem: Salary prediction for job seekers.                      
✅ Showcases multiple ML techniques: Feature engineering, model stacking, and deployment.   
✅ Successfully deployed model, making it accessible to users.  
✅ Provides practical insights into salary trends for Data Science roles in Inida.


---

## 💬 Let's Connect!    

📧 **Email**: mahammadshama77@gmail.com        
🔗 **LinkedIn**: [Profile](https://www.linkedin.com/in/mahammad-shama-5b50632b7)    


---

⭐ If you found this project useful, don’t forget to star this repository!


---



