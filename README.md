# Bubble-Store

## 1. Background and Overview  
SIn today’s highly competitive retail environment, small businesses face significant challenges in managing resources, forecasting demand, and retaining customers. The goal of this project is to demonstrate how machine learning (ML) can be leveraged to improve decision-making and business efficiency.

- Forecast sales and optimize inventory.  
- Improve customer satisfaction through personalized recommendations.  
- Enable better decision-making for managers, employees, and customers.  

This project focuses on a **simulated beverage store** and demonstrates how advanced ML techniques can be embedded into a user-friendly application with a graphical interface for real-world business use.  

---

## 2. Data Structure Overview  
The project uses a **simulated retail dataset** reflecting real-world café operations (2022–2024).  

Key entities include:  
- **Orders**: `OrderMasters`, `OrderDetails` (transactions, products, reviews).  
- **Products**: product details, categories, prices, availability.  
- **Ingredients & Recipes**: breakdown of product composition.  
- **Customers & Employees**: profiles, accounts, and activity logs.  

📊 Dataset size: ~300,000 rows of transactions  
🔧 Tools used: **Python, Pandas, NumPy, Mockaroo, Generatedata**  

---

## 3. Executive Summary – Overview of Findings  
From analyzing the data and applying ML models, several important findings emerged:  

- **Sales Seasonality**: Coffee consistently outperformed other beverages, with noticeable spikes during **holiday periods (New Year, July events)**.  
- **Customer Behavior**:  
  - Loyal customers gave consistently high ratings (avg. >4.5 stars).  
  - Occasional buyers were more critical, highlighting areas for service improvement.  
- **Employee Workload**: Only **8 employees handled the majority of orders**, while others were underutilized.  
- **Sales Trends**: Total sales grew steadily over time, with fluctuations driven by promotions and seasonal effects.  
- **Model Performance**:  
  - **SARIMA** was the best-performing forecasting model (capturing seasonal demand patterns).  
  - **SVD (collaborative filtering)** outperformed KNN for recommender systems due to better accuracy and efficiency.  
- **Operational Risk**: Without accurate forecasting, the store risks costly **overstocking** or **stockouts**, directly affecting profitability and customer trust.  

---

## 4. Insights Deep Dive  
Some deeper observations from the analysis:  
- **Product Insights**: Frappuccino and Latte followed coffee in popularity, while certain seasonal drinks saw short-lived surges.  
- **Holiday Impact**: December promotions nearly doubled average sales compared to regular months.  
- **Customer Segmentation**: High-frequency customers drove a disproportionate share of revenue.  
- **Employee Productivity Gaps**: Staff efficiency varied widely, suggesting mismatched allocation of shifts.  
- **Ratings Analysis**: Negative reviews correlated with **longer order wait times** and **stockouts**.  

---

## 5. Recommendations  
Based on these findings, the following actions are recommended:  

1. **Inventory & Supply Chain**  
   - Use SARIMA forecasts to maintain stock for peak-demand products (especially coffee during holidays).  
   - Reduce slow-moving items to free resources.  

2. **Customer Retention**  
   - Introduce loyalty rewards for repeat customers.  
   - Personalize marketing using the recommender system to upsell complementary drinks.  

3. **Employee Management**  
   - Rebalance workloads by adjusting schedules based on peak sales forecasts.  
   - Provide targeted training for underperforming employees.  

4. **Marketing Strategy**  
   - Launch promotions ahead of seasonal peaks to maximize revenue.  
   - Leverage customer ratings to identify and improve weak areas in service.  

---

## 6. Machine Learning Approach & Solution  
The solution integrates multiple ML models into a single application:  

- **Sales Forecasting**  
  - Models tested: ARIMA, SARIMA, Exponential Smoothing, Random Forest, XGBoost.  
  - **SARIMA selected** for deployment due to lowest error rates and strong seasonality handling.  

- **Recommender Systems**  
  - **Content-Based Filtering**: Suggests products based on attributes (TF-IDF & cosine similarity).  
  - **Collaborative Filtering (SVD)**: Learns from past customer-product interactions.  
  - **Hybrid Model**: Combines both for improved accuracy and cold-start problem reduction.  

- **Evaluation Metrics**  
  - Forecasting: RMSE, MAE, MAPE.  
  - Recommendation: RMSE, MAE across cross-validation folds.  

- **Application Deployment**  
  - **GUI built with PyQt6 & Qt Designer**.  
  - Role-based access:  
    - **Customer**: profile, order, history, recommendations.  
    - **Employee**: manage orders, customers, and products.  
    - **Manager**: visualize data, train models, forecast sales.  

---

✨ This project demonstrates how **small businesses can harness machine learning** for smarter operations, higher customer satisfaction, and long-term competitiveness.  
