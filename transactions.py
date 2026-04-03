"""
Transaction management module for AI Finance Tracker.

Handles CRUD operations on transactions including creation, editing, deletion,
filtering, and importing from CSV files.
"""

from typing import List, Optional
from datetime import datetime
import pandas as pd
from db import SessionLocal, Transaction
from sqlalchemy import or_
from config import DESCRIPTION_COLUMN_ALIASES, DATE_COLUMN_ALIASES, DEBIT_CREDIT_COLUMNS


def add_transaction(user_id: int, date, description: str, amount: float,
                   category: Optional[str] = None, notes: Optional[str] = None) -> Transaction:
    """
    Add a new transaction to the database.
    
    Args:
        user_id: ID of the transaction owner.
        date: Transaction date (string in ISO format or date object).
        description: Transaction description/merchant name.
        amount: Transaction amount (positive for income, negative for expense).
        category: Optional transaction category.
        notes: Optional additional notes about the transaction.
    
    Returns:
        The created Transaction object.
    """
    db = SessionLocal()
    try:
        if isinstance(date, str):
            date = datetime.fromisoformat(date).date()
        transaction = Transaction(
            user_id=user_id,
            date=date,
            description=description,
            amount=amount,
            category=category,
            notes=notes
        )
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction
    finally:
        db.close()


def edit_transaction(tx_id: int, **fields) -> Optional[Transaction]:
    """
    Edit an existing transaction in the database.
    
    Args:
        tx_id: The ID of the transaction to edit.
        **fields: Keyword arguments of fields to update (e.g., amount=100, category='Food').
                 Date strings are automatically converted to date objects.
    
    Returns:
        The updated Transaction object, or None if transaction not found.
    """
    db = SessionLocal()
    try:
        transaction = db.query(Transaction).get(tx_id)
        if not transaction:
            return None
        for key, value in fields.items():
            if key == 'date' and isinstance(value, str):
                value = datetime.fromisoformat(value).date()
            setattr(transaction, key, value)
        db.commit()
        db.refresh(transaction)
        return transaction
    finally:
        db.close()


def delete_transaction(tx_id: int) -> bool:
    """
    Delete a transaction from the database by its ID.
    
    Args:
        tx_id: The ID of the transaction to delete.
    
    Returns:
        True if deletion succeeded, False if transaction not found.
    """
    db = SessionLocal()
    try:
        transaction = db.query(Transaction).get(tx_id)
        if not transaction:
            return False
        db.delete(transaction)
        db.commit()
        return True
    finally:
        db.close()


def list_transactions(user_id: int, start_date=None, end_date=None,
                     category: Optional[str] = None, search: Optional[str] = None) -> List[Transaction]:
    """
    List transactions for a user with optional filters.
    
    Args:
        user_id: ID of the user whose transactions to retrieve.
        start_date: Filter transactions on or after this date (optional).
        end_date: Filter transactions on or before this date (optional).
        category: Filter by specific category (optional).
        search: Search in description and notes fields (optional, case-insensitive).
    
    Returns:
        List of matching Transaction objects, ordered by date (most recent first).
    """
    db = SessionLocal()
    try:
        query = db.query(Transaction).filter(Transaction.user_id == user_id)
        
        if start_date:
            query = query.filter(Transaction.date >= start_date)
        if end_date:
            query = query.filter(Transaction.date <= end_date)
        if category:
            query = query.filter(Transaction.category == category)
        if search:
            search_pattern = f"%{search}%"
            query = query.filter(or_(
                Transaction.description.ilike(search_pattern),
                Transaction.notes.ilike(search_pattern)
            ))
        
        return query.order_by(Transaction.date.desc()).all()
    finally:
        db.close()


def import_transactions_from_csv(user_id: int, csv_file) -> List[Transaction]:
    """
    Import transactions from a CSV file into the database.
    
    Automatically detects and standardizes various column name formats for:
    - Description: 'description', 'desc', 'details', 'narration', 'memo', 'payee'
    - Amount: 'amount' or calculated from 'debit'/'credit' columns
    - Date: 'date', 'transaction_date', 'posted', 'posted_date', 'value_date'
    
    Args:
        user_id: ID of the user importing transactions.
        csv_file: File-like object or path to the CSV file.
    
    Returns:
        List of successfully created Transaction objects.
        Returns empty list if no valid date column found or errors occur.
    """
    df = pd.read_csv(csv_file)
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Standardize description column
    if 'description' not in df.columns:
        for alt_name in DESCRIPTION_COLUMN_ALIASES:
            if alt_name in df.columns:
                df['description'] = df[alt_name]
                break

    # Standardize amount column from debit/credit if 'amount' not present
    if 'amount' not in df.columns and any(col in df.columns for col in DEBIT_CREDIT_COLUMNS):
        debit = pd.to_numeric(df.get('debit', 0), errors='coerce').fillna(0)
        credit = pd.to_numeric(df.get('credit', 0), errors='coerce').fillna(0)
        df['amount'] = credit - debit

    # Standardize date column
    date_column = next(
        (col for col in DATE_COLUMN_ALIASES if col in df.columns),
        None
    )
    if date_column:
        df['date_parsed'] = pd.to_datetime(df[date_column], errors='coerce').dt.date
    else:
        # No date column found
        return []

    created = []
    for _, row in df.iterrows():
        description = str(row.get('description', '')).strip()
        date_value = row.get('date_parsed')
        amount_value = pd.to_numeric(row.get('amount'), errors='coerce')

        # Only create transactions with valid data
        if pd.notna(date_value) and description and pd.notna(amount_value):
            category = row.get('category')
            notes = row.get('notes')
            transaction = add_transaction(
                user_id,
                date_value,
                description,
                float(amount_value),
                category,
                notes
            )
            created.append(transaction)
            
    return created
