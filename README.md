# 🇸🇪 Project : Nordic Shield - AML Risk Detection Engine

## 🎯 Objective
This project demonstrates a data-driven approach to Anti-Money Laundering (AML) within the Swedish financial landscape. The focus is on detecting **"Smurfing" (Structuring)**—a method where illicit funds are broken into smaller amounts (just under the 10,000 SEK reporting threshold) to avoid regulatory triggers.

## 🛠️ Skills Demonstrated
* **Regulatory Knowledge:** Understanding of Swedish Financial Supervisory Authority (Finansinspektionen) monitoring requirements.
* **Data Engineering:** Synthetic generation of GDPR-compliant PII (Personally Identifiable Information) using Python.
* **Advanced Analytics:** Pattern recognition using `Pandas` for behavioral transaction monitoring.

## 📊 Business Logic
The engine identifies high-risk actors by flagging users who:
1.  Execute more than 3 transactions within a 24-hour window.
2.  Maintain transaction values between **9,000 SEK and 9,999 SEK**.

## 🚀 Impact for the Organization
* **Reduced False Negatives:** Traditional static limits often miss high-frequency, low-value patterns.
* **Compliance Ready:** Built with data privacy in mind, allowing for logic testing without exposing real customer PII.

---
*Developed by a Data Professional with experience in Amazon Fraud Prevention.*
