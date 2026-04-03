"""
Main application entry point for AI Finance Tracker.

Streamlit-based web application for personal finance tracking with AI-powered insights.
Handles page routing, initialization, and session management.
"""

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from db import init_db
from config import APP_TITLE, APP_LAYOUT
from styles import MAIN_APP_STYLE
from ui import (
    show_login_page, show_dashboard, show_transaction_page, 
    show_chatbot_page, show_import_csv_page, show_account_page, show_calculator_page
)

# Initialize database
init_db()

# Configure Streamlit page
st.set_page_config(page_title=APP_TITLE, layout=APP_LAYOUT)

# Apply global styling
st.markdown(MAIN_APP_STYLE, unsafe_allow_html=True)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['user'] = None


def logout() -> None:
    """Log out the user and reset session state."""
    st.session_state['logged_in'] = False
    st.session_state['user'] = None
    st.rerun()


def show_sidebar() -> None:
    """Display the sidebar with user info and navigation."""
    st.sidebar.write(f"Welcome: {st.session_state['user']['username']}")
    if st.sidebar.button('Logout'):
        logout()

    # Initialize page navigation
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Dashboard'

    st.sidebar.subheader('Pages:')
    pages = [
        ('Dashboard', 'Dashboard'),
        ('Transaction', 'Transaction'),
        ('Chatbot', 'Chatbot'),
        ('Import CSV', 'Import CSV'),
        ('Calculator', 'Calculator'),
        ('Account', 'Account'),
    ]
    
    for page_name, page_key in pages:
        if st.sidebar.button(page_name, key=f'nav_{page_key.lower().replace(" ", "_")}'):
            st.session_state['page'] = page_name
            st.rerun()


def show_page_content(page: str, user_id: int) -> None:
    """
    Display the content for the selected page.
    
    Args:
        page: The name of the page to display.
        user_id: The ID of the current user.
    """
    page_router = {
        'Dashboard': lambda: show_dashboard(user_id),
        'Transaction': lambda: show_transaction_page(user_id),
        'Chatbot': lambda: show_chatbot_page(user_id),
        'Import CSV': lambda: show_import_csv_page(user_id),
        'Calculator': lambda: show_calculator_page(user_id),
        'Account': lambda: show_account_page(st.session_state['user']),
    }
    
    if page in page_router:
        page_router[page]()


def main() -> None:
    """
    Main application entry point.
    
    Handles page routing based on user authentication status
    and manages navigation between different pages.
    """
    if not st.session_state.get('logged_in'):
        show_login_page()
    else:
        show_sidebar()
        
        page = st.session_state.get('page', 'Dashboard')
        user_id = st.session_state['user']['id']
        
        show_page_content(page, user_id)


if __name__ == '__main__':
    main()

