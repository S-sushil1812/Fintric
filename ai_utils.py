"""
AI utilities module for AI Finance Tracker.

Handles integration with Google Gemini AI for transaction categorization
and financial chatbot functionality.
"""

from typing import Optional
import google.generativeai as genai
from db import SessionLocal, Transaction
from config import GOOGLE_API_KEY, GEMINI_MODEL, CHATBOT_NAME, CHATBOT_SYSTEM_PROMPT, DEFAULT_TRANSACTION_LIMIT

# Configure Google Gemini API
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)


def categorize_transaction(description: str, amount: float) -> Optional[str]:
    """
    Suggest a category for a transaction using Google Gemini AI.
    
    Args:
        description: The transaction description or purchase details.
        amount: The transaction amount.
    
    Returns:
        A category string, or None if API is not configured or an error occurs.
    """
    if not GOOGLE_API_KEY:
        return None
    
    prompt = f"Suggest a short category for this transaction: '{description}' (Amount: {amount})."
    
    try:
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return None


def query_transactions_for_chat(user_id: int, limit: int = DEFAULT_TRANSACTION_LIMIT) -> list:
    """
    Fetch recent transactions for use as context in chatbot interactions.
    
    Args:
        user_id: The ID of the user whose transactions to fetch.
        limit: Maximum number of transactions to retrieve (default: 40).
    
    Returns:
        List of Transaction objects, ordered by date (most recent first).
    """
    db = SessionLocal()
    try:
        return db.query(Transaction).filter(
            Transaction.user_id == user_id
        ).order_by(
            Transaction.date.desc()
        ).limit(limit).all()
    finally:
        db.close()


def chat_with_data(user_id: int, user_message: str) -> str:
    """
    Handle chatbot functionality using transaction data as context.
    
    Args:
        user_id: The ID of the user chatting.
        user_message: The user's query or message.
    
    Returns:
        The AI's response, or an error message if something goes wrong.
    """
    if not GOOGLE_API_KEY:
        return "Google API key not configured. Please set the GOOGLE_API_KEY environment variable."
    
    # Fetch recent transactions to use as context
    transactions = query_transactions_for_chat(user_id)
    context = "\n".join([
        f"{t.date.isoformat()} | {t.description} | {t.amount} | {t.category or 'Uncategorized'}"
        for t in transactions
    ])
    
    # Construct the full prompt with system prompt, context, and user message
    full_prompt = f"{CHATBOT_SYSTEM_PROMPT}\n\nRecent transactions:\n{context}\n\nUser question: {user_message}"

    try:
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred with the AI model: {e}"
