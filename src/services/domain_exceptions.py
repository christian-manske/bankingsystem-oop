"""
Custom exceptions for the banking system domain
"""

class BankingException(Exception):
    """Base exception for the banking operations."""
    pass

class InsufficientFundsException(BankingException):
    """Raised when account has insufficient funds for opeation."""
    pass

class InvalidAmountException(BankingException):
    """Raised when transaction amount is invalid."""
    pass

class AccountNotFoundException(BankingException):
    """Raised when account is not found."""
    pass

class DuplicateAccountException(BankingException):
    """Raised when trying to create account with existing number."""
    pass