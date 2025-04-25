# 🔐 Password Generator & Breach Checker

This project is a web application that allows users to generate strong, random passwords and check if they’ve been exposed in known data breaches using the Have I Been Pwned API.

🌐 **Live Site:** [https://password-checker-v5cv.onrender.com](https://password-checker-v5cv.onrender.com)

📝 **Made for the BUCC (Brac University Computer Club) Interview – Spring 2025**  
🚫 **Rejected by BUCC.**

<div align="center" style="display: flex; justify-content: center; gap: 40px;">
  <div style="text-align: center;">
    <img src="https://drive.google.com/uc?export=view&id=1SYBuCr0QieA8bpMKBDI03FaXKULZ1YwR" alt="Thumbnail" width="250" height="250"/>
    <p><b>Thumbnail</b></p>
  </div>
  <div style="text-align: center;">
    <img src="https://drive.google.com/uc?export=view&id=1J6hHAkfsnQ0kVkgBO-nRBtMwmndlwgYF" alt="Website Screenshot" width="666"/>
    <p><b>Website Preview</b></p>
  </div>
</div>




## 🛠️ Tools & Technologies

- **Python**
- **Flask**
- **HTML/CSS**
- **JavaScript**
- **Have I Been Pwned API**
- **Render (for deployment)**

## 🚀 How to Build & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/password-checker.git
   cd password-checker
   ```


2. **Create a virtual environment & activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your secret key:
     ```
     SECRET_KEY=your-secret-key
     ```

5. **Run the application**
   ```bash
   flask run
   ```

6. **Visit in browser**
   ```
   http://localhost:5000
   ```

## 💡 Key Features

- Generates strong passwords with customizable length
- Checks if the password has appeared in any data breaches
- Password strength meter
- Copy to clipboard with a single click
- Clean UI with live preview and feedback

## ⚠️ Challenges

- Integrating the breach check securely and efficiently
- Deploying Flask on a free hosting platform like Render
- Getting Open Graph metadata (like preview image) to update properly across platforms


