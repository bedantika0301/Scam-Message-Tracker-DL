Scam Message Tracker

Project Overview :
The Scam Message Tracker is a Python-based project that helps users identify whether a message is safe or a potential scam. It is designed to promote digital awareness and online safety by detecting suspicious messages such as fake lottery wins, phishing links, or OTP frauds.
________________________________________

Features :
•	Detects Scam vs Safe messages 
•	Uses Machine Learning (Naive Bayes) 
•	Checks for risky keywords (OTP, win, free, etc.) 
•	Displays scam probability (%) 
•	Stores message history 
•	Provides a summary report 
________________________________________

How It Works ? 
1.	The system is trained on a dataset of scam and safe messages. 
2.	User enters a message. 
3.	The program: 
o	Cleans the text (removes punctuation, lowercase) 
o	Converts text into numerical form 
o	Predicts using a trained ML model 
o	Checks for suspicious keywords 
4.	Displays: 
o	Result (Scam/Safe) 
o	Probability score 
o	Risky keywords (if any) 
________________________________________

Technologies Used :
•	Python 
•	Scikit-learn 
•	CountVectorizer 
•	Multinomial Naive Bayes 
________________________________________

How to Run ?
1. Install dependencies
pip install scikit-learn
2. Run the program
python scam_tracker.py
________________________________________

Example Output :
Enter message: Win a free iPhone now!

Result:  SCAM DETECTED  
Scam Probability: 92.5 %  
Risky Keywords: win, free  
________________________________________

Future Improvements :
•	Add GUI (Tkinter) 
•	Build a web app (Flask) 
•	Increase dataset for better accuracy 
•	Add real-time SMS/email integration 
________________________________________

 Applications :
•	SMS filtering 
•	Email spam detection 
•	Social media safety 
•	Educational awareness tools 
________________________________________

Conclusion :
This project demonstrates how machine learning and simple rules can be combined to detect scam messages and improve digital safety. It is a practical example of applying technology to solve real-world problems.
________________________________________

Author :
Bedantika Banerjee
25BCE10597

