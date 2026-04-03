"""
Configuration module for AI Finance Tracker.

This module centralizes all application constants, environment variables,
and configuration settings for easier maintenance and security.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================
BASE_DIR = Path(__file__).parent.absolute()
DB_PATH = BASE_DIR / 'data.db'
DB_URL = f'sqlite:///{DB_PATH}'
DB_CONNECT_ARGS = {'check_same_thread': False}

# ============================================================================
# GOOGLE GEMINI AI CONFIGURATION
# ============================================================================
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GEMINI_MODEL = 'models/gemini-1.5-flash-latest'

# ============================================================================
# GOOGLE OAUTH CONFIGURATION
# ============================================================================
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI', 'http://localhost:8501')
GOOGLE_OAUTH_SCOPES = 'openid email profile'

# ============================================================================
# APPLICATION CONFIGURATION
# ============================================================================
APP_TITLE = 'AI Finance Tracker'
APP_LAYOUT = 'wide'
DEFAULT_TRANSACTION_LIMIT = 40

# ============================================================================
# UI CONFIGURATION
# ============================================================================
# Color Palette
COLOR_PRIMARY_BG = '#0B0F19'
COLOR_SECONDARY_BG = '#111827'
COLOR_TERTIARY_BG = '#1F2937'
COLOR_ACCENT_PRIMARY = '#00D1FF'
COLOR_ACCENT_SECONDARY = '#6366F1'
COLOR_SUCCESS = '#22C55E'
COLOR_DANGER = '#EF4444'
COLOR_TEXT_PRIMARY = '#E5E7EB'
COLOR_TEXT_SECONDARY = '#9CA3AF'
COLOR_TEXT_MUTED = '#6B7280'
COLOR_BORDER = '#374151'

# ============================================================================
# TRANSACTION CSV IMPORT CONFIGURATION
# ============================================================================
DESCRIPTION_COLUMN_ALIASES = ['desc', 'details', 'narration', 'memo', 'payee']
DATE_COLUMN_ALIASES = ['date', 'transaction_date', 'posted', 'posted_date', 'value_date']
DEBIT_CREDIT_COLUMNS = ['debit', 'credit']

# ============================================================================
# AI CHATBOT CONFIGURATION
# ============================================================================
CHATBOT_NAME = 'Fintric'
CHATBOT_SYSTEM_PROMPT = (
    f"You are {CHATBOT_NAME}, a helpful assistant for personal finance. "
    "Use the provided transactions to answer the user's questions accurately."
)
