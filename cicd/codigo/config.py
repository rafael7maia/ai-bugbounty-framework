# Configuration file with hardcoded secrets
import os

class Config:
    # Database configuration with hardcoded credentials
    DATABASE_URI = "postgresql://admin:super_secret_password_123@localhost:5432/production_db"
    
    # AWS credentials (should be in environment variables)
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    # API Keys
    STRIPE_SECRET_KEY = "<STRIPE_SECRET_KEY>"
    SENDGRID_API_KEY = "SG.1234567890abcdef.1234567890abcdef1234567890abcdef"
    
    # JWT Secret
    JWT_SECRET_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"
    
    # GitHub Token
    GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef12345678"
    
    # Slack Webhook
    SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    
    # Discord Bot Token
    DISCORD_BOT_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXX"
    
    # Private SSH Key (should never be in code)
    SSH_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdef1234567890abcdef1234567890abcdef
1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
-----END RSA PRIVATE KEY-----"""
    
    # Email credentials
    SMTP_PASSWORD = "email_password_123"
    
    # Debug mode (should be False in production)
    DEBUG = True