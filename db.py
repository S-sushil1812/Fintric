"""
Database module for AI Finance Tracker.

This module manages database connections, schemas, and ORM models
using SQLAlchemy for SQLite persistence.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config import DB_URL, DB_CONNECT_ARGS

# Create the database engine
ENGINE = create_engine(DB_URL, connect_args=DB_CONNECT_ARGS)

# Create a sessionmaker to manage database sessions
SessionLocal = sessionmaker(bind=ENGINE, autoflush=False, autocommit=False)

# Create a base class for declarative models
Base = declarative_base()

# Define the User model
class User(Base):
    """
    User account model.
    
    Attributes:
        id: Unique user identifier (primary key).
        username: Unique username for login.
        password_hash: Bcrypt hashed password for security.
        transactions: Relationship to associated Transaction records.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    # Relationship with transactions - cascade delete orphans
    transactions = relationship('Transaction', back_populates='user', cascade='all, delete-orphan')


class Transaction(Base):
    """
    Financial transaction model.
    
    Attributes:
        id: Unique transaction identifier (primary key).
        user_id: Foreign key referencing the owning User.
        date: Transaction date (indexed for range queries).
        description: Merchant/payee name or transaction description.
        amount: Transaction amount (positive for income, negative for expense).
        category: Optional transaction category (e.g., 'Groceries', 'Gas').
        notes: Optional additional notes or memo.
        user: Relationship back to the owning User.
    """
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    date = Column(Date, index=True, nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
    # Relationship back to user
    user = relationship('User', back_populates='transactions')


def init_db() -> None:
    """Initialize the database by creating all tables if they don't exist."""
    Base.metadata.create_all(ENGINE)


def delete_user(user_id: int) -> bool:
    """
    Delete a user and all their associated transactions.
    
    This cascading delete ensures referential integrity and removes all
    transaction records owned by the user.
    
    Args:
        user_id: The ID of the user to delete.
    
    Returns:
        True if deletion succeeded, False if user not found or error occurred.
    """
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
    except Exception:
        db.rollback()
        return False
    finally:
        db.close()


if __name__ == '__main__':
    # Allow running this script directly to initialize the database
    init_db()
