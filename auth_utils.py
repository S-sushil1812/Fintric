"""
Authentication utilities module for AI Finance Tracker.

Handles user authentication including password hashing/verification,
user registration, and Google OAuth integration.
"""

from typing import Optional
from passlib.context import CryptContext
from db import SessionLocal, User
from sqlalchemy.exc import IntegrityError
from urllib.parse import urlencode
import requests
import streamlit as st
from config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REDIRECT_URI, GOOGLE_OAUTH_SCOPES

# Password hashing context using bcrypt
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    Args:
        password: The plain-text password to hash.
    
    Returns:
        The bcrypt hashed password.
    """
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    """
    Verify a plain-text password against a bcrypt hash.
    
    Args:
        plain: The plain-text password to verify.
        hashed: The bcrypt hashed password to compare against.
    
    Returns:
        True if passwords match, False otherwise.
    """
    return pwd_context.verify(plain, hashed)


def register_user(username: str, password: str) -> Optional[User]:
    """
    Register a new user in the database.
    
    Args:
        username: The desired username (must be unique).
        password: The user's password (will be hashed before storage).
    
    Returns:
        The created User object, or None if username already exists.
    """
    db = SessionLocal()
    try:
        user = User(username=username, password_hash=get_password_hash(password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        # Username already exists
        db.rollback()
        return None
    finally:
        db.close()


def authenticate_user(username: str, password: str) -> Optional[User]:
    """
    Authenticate a user by username and password.
    
    Args:
        username: The user's username.
        password: The user's password (will be verified against the hash).
    
    Returns:
        The User object if authentication succeeds, None otherwise.
    """
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if user and verify_password(password, user.password_hash):
            return user
        return None
    finally:
        db.close()


def google_oauth_url() -> Optional[str]:
    """
    Generate the OAuth consent screen URL for Google authentication.
    
    Returns:
        The Google OAuth URL, or None if required credentials are not configured.
    """
    if not all([GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REDIRECT_URI]):
        return None
    
    params = {
        'client_id': GOOGLE_CLIENT_ID,
        'redirect_uri': GOOGLE_REDIRECT_URI,
        'scope': GOOGLE_OAUTH_SCOPES,
        'response_type': 'code',
        'access_type': 'offline',
        'prompt': 'consent'
    }
    return f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"


def google_exchange_code_for_token(code: str) -> Optional[dict]:
    """
    Exchange an authorization code for an access token.
    
    Args:
        code: The authorization code from the OAuth consent screen.
    
    Returns:
        The token data dict containing 'access_token', or None on failure.
    """
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': GOOGLE_REDIRECT_URI
    }
    response = requests.post(token_url, data=data)
    return response.json() if response.status_code == 200 else None


def google_get_user_info(access_token: str) -> Optional[dict]:
    """
    Fetch user information from Google using an access token.
    
    Args:
        access_token: The OAuth access token from Google.
    
    Returns:
        User information dict containing email and name, or None on failure.
    """
    userinfo_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(userinfo_url, headers=headers)
    return response.json() if response.status_code == 200 else None


def handle_google_signin() -> None:
    """
    Handle the Google Sign-In OAuth flow.
    
    Processes the authorization code from Google's OAuth callback,
    exchanges it for an access token, retrieves user information,
    and sets the Streamlit session state for logged-in users.
    
    Expected flow:
        1. User clicks "Continue with Google"
        2. Redirected to Google's consent screen
        3. Google redirects back with 'code' in query params
        4. This function exchanges code for token, gets user info
        5. Sets session state and re-runs the app
    """
    if 'code' in st.query_params:
        code = st.query_params['code']
        token_data = google_exchange_code_for_token(code)
        
        if token_data and 'access_token' in token_data:
            user_info = google_get_user_info(token_data['access_token'])
            if user_info and 'email' in user_info:
                email = user_info['email']
                # Use email as a unique ID for Google users
                st.session_state['logged_in'] = True
                st.session_state['user'] = {
                    'id': email,
                    'username': user_info.get('name', email),
                    'email': email,
                    'provider': 'google'
                }
                st.success(f'Welcome back, {user_info.get("name", email)}!')
                # Clear query params to prevent re-processing on page refresh
                st.query_params.clear()
                st.rerun()
            else:
                st.error('Could not retrieve user information from Google.')
        else:
            st.error('Failed to authenticate with Google.')
        
        st.query_params.clear()
