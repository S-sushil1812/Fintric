# AI Finance Tracker (Fintric)

A modern premium fintech dashboard built with Streamlit that uses AI to help you track, analyze, import, and interact with your financial data. Manage accounts, upload CSV bank statements, view analytics, and ask finance questions to your own AI assistant. Accounts and transactions remain local in SQLite for privacy and fast prototyping.

## ✨ Features

### Core Functionality
- **User Authentication**: Register/login with username & password or Google. Accounts are stored locally.
- **Profile Management**: View account info, reveal email/full name, and delete account (all user data removed).
- **Transaction Management**:
  - Add credit/debit transactions with description, category, notes
  - Delete individual or all transactions in-app
  - Import bank statements from CSV (custom and bank formats supported)
  - Export transactions to CSV
- **Analytics Dashboard**: Visualize gains, losses, category spend, and income with premium Nivo charts.
- **Financial Calculators**: A suite of interactive calculators for financial planning:
    - EMI Calculator (Equated Monthly Installment)
    - SIP Calculator (Systematic Investment Plan)
    - Compound Interest Calculator
    - Fixed Deposit (FD) Calculator
    - Recurring Deposit (RD) Calculator
- **AI Chatbot**: Ask smart questions about your finances using Google Gemini (optional, requires your API key)
- **FAQ Section**: 8 comprehensive FAQs covering all app features

### 🎨 Premium UI Design
- **Dark Fintech Theme**: Professional dark mode (#0B0F19) with cyan/indigo accents (#00D1FF, #6366F1)
- **Glowing Dividers**: Clean gradient dividers between sections with glow effects
- **Premium Display**: Gradient text, glassmorphic cards, shadow effects
- **Responsive Sliders**: Clean, minimal slider design with smooth interactions
- **Empty Box Removal**: Global CSS prevents any empty containers from rendering
- **Modern Typography**: Carefully crafted fonts, spacing, and visual hierarchy

## Getting Started

### 1. Requirements
- **Python 3.9+** (tested with Python 3.12, 3.13)
- **pip** (Python package manager)
- **Git** (optional, for version control)

### 2. Installation

#### Step 1: Navigate to project directory
```bash
cd "d:\PYTHON\PROJECTS\CLG PROJECT\FINTRIC_1"
```

#### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

**If pip install fails**, try:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit streamlit-elements pandas sqlalchemy plotly python-dotenv google-generativeai
```

#### Step 3: Optional - Setup environment variables
Create a `.env` file in the project root:
```env
# Google OAuth (optional)
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
GOOGLE_REDIRECT_URI=http://localhost:8501

# AI Chatbot (optional)
GOOGLE_API_KEY=your_api_key_here
```

### 3. Running the App

#### Method 1: Direct (Recommended)
```bash
cd "d:\PYTHON\PROJECTS\CLG PROJECT\FINTRIC_1"
python -m streamlit run app.py
```

#### Method 2: Using streamlit command
```bash
streamlit run app.py
```

#### Method 3: Using py launcher
```bash
py -m streamlit run app.py
```

### 4. Access the App
After running, you'll see:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8503
  Network URL: http://192.168.1.105:8503
```

Open one of these URLs in your browser.

### 5. First Time Setup
1. **Register** a new account with username and password
2. **Add transactions** manually or import from CSV
3. **View analytics** on the dashboard
4. **Use calculators** for financial planning
5. **Chat with AI** (if API key configured)

## 📋 Pages

### Dashboard
- Financial summary cards (Income, Expenses, Savings Rate)
- Monthly expense breakdown (Nivo Pie Chart)
- Monthly trend analysis
- Quick start guide

### Transactions
- Add new transactions with category, date, amount
- View all transactions in a table with filters
- Search by description or notes
- Filter by type (Credit/Debit) and category
- Category analysis with income/expense breakdown
- Monthly trend visualization
- Export transactions to CSV

### Financial Calculators
- **EMI Calculator**: Calculate monthly loan payments
- **SIP Calculator**: Project investment growth
- **Compound Interest**: Calculate interest on investments
- **FD Calculator**: Fixed deposit maturity amounts
- **RD Calculator**: Recurring deposit returns
- Each includes visual breakdown charts

### Import CSV
- Upload bank statements in CSV format
- Preview data before importing
- Edit data in table format
- View totals and trends
- Import to database

### AI Chatbot
- Ask questions about your finances
- Integrated with Google Gemini API
- Contextual responses based on your data

### Account
- View profile information
- Manage email & full name visibility
- Delete account (irreversible)

## 📁 File Structure
```
FINTRIC_1/
├── app.py              # Main Streamlit app entry point
├── ui.py               # All UI components and pages
├── db.py               # Database models and CRUD operations
├── transactions.py     # Transaction handling utilities
├── auth_utils.py       # Authentication (login, register, OAuth)
├── ai_utils.py         # AI chatbot interface
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .env               # Environment variables (create if needed)
```

## 🎯 Financial Calculators Details

Each calculator provides:
- **Interactive inputs** with sliders for easy adjustment
- **Real-time calculations** as you adjust values
- **Visual breakdown** with pie charts showing principal vs interest/returns
- **Multiple options** (e.g., compounding frequency for Compound Interest)

### Calculator Features
- Clean, minimal slider design
- Responsive layout with side-by-side input/results
- Premium gradient styling
- Instant visual feedback

## 🔒 Security & Privacy

- **Local storage only** - All data stays on your machine (SQLite database)
- **Secure authentication** - Passwords hashed with bcrypt
- **No cloud sync** - Except optional AI chatbot API
- **Account deletion** - Removes all data permanently and irreversibly

## 🐛 Known Limitations / Notes

- **Local SQLite DB** — No cloud backup; consider regular backups of `finance.db`
- **Account deletion is irreversible** — All transactions deleted immediately
- **Optional features require API keys**:
  - Google Sign-in: Need OAuth credentials
  - AI Chatbot: Need Google Gemini API key
- **Deprecation warnings**: App uses `google.generativeai` (consider upgrading to `google.genai` in future)

## 🚀 Future Enhancements

- Cloud database sync
- Budget goals and alerts
- Recurring transaction templates
- Multi-currency support
- Bill reminders
- Investment portfolio tracking
- Export reports (PDF)

## 📧 Support

For issues or questions:
1. Check the FAQ section in the app
2. Review error messages in the terminal
3. Verify all dependencies are installed
4. Ensure Python 3.9+ is being used

## 📄 License
MIT License
