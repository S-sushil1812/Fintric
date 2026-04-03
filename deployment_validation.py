#!/usr/bin/env python3
"""
Deployment Validation Script for FINTRIC

This script validates that all deployment requirements are met before pushing to production.
Run with: python deployment_validation.py
"""

import os
import sys
import subprocess
from pathlib import Path

class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_status(status, message):
    """Print a status message with color"""
    colors = {
        'pass': Colors.GREEN + '✅' + Colors.END,
        'fail': Colors.RED + '❌' + Colors.END,
        'warn': Colors.YELLOW + '⚠️' + Colors.END,
        'info': Colors.BLUE + 'ℹ️' + Colors.END,
    }
    print(f"{colors.get(status, status)} {message}")

def check_python_version():
    """Verify Python 3.9+ is being used"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 9:
        print_status('pass', f"Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print_status('fail', f"Python 3.9+ required, but {version.major}.{version.minor} found")
        return False

def check_dependencies():
    """Verify all dependencies are installed"""
    required_packages = [
        'streamlit',
        'pandas',
        'sqlalchemy',
        'passlib',
        'bcrypt',
        'requests',
        'google.generativeai',
        'plotly',
        'dotenv',
    ]
    
    all_installed = True
    for package in required_packages:
        try:
            __import__(package if package != 'dotenv' else 'dotenv')
            print_status('pass', f"Package '{package}' installed")
        except ImportError:
            print_status('fail', f"Package '{package}' NOT installed")
            all_installed = False
    
    return all_installed

def check_project_structure():
    """Verify required project files exist"""
    required_files = [
        'app.py',
        'config.py',
        'db.py',
        'auth_utils.py',
        'transactions.py',
        'ai_utils.py',
        'styles.py',
        'requirements.txt',
        'README.md',
        '.env.example',
        '.gitignore',
        'Dockerfile',
        'Procfile',
        'runtime.txt',
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print_status('pass', f"File exists: {file}")
        else:
            print_status('fail', f"Missing file: {file}")
            all_exist = False
    
    return all_exist

def check_imports():
    """Verify all Python imports work correctly"""
    modules = [
        'app',
        'config',
        'db',
        'auth_utils',
        'transactions',
        'ai_utils',
        'styles',
    ]
    
    all_valid = True
    for module in modules:
        try:
            __import__(module)
            print_status('pass', f"Module '{module}' imports successfully")
        except Exception as e:
            print_status('fail', f"Module '{module}' import failed: {str(e)}")
            all_valid = False
    
    return all_valid

def check_database():
    """Verify database initialization works"""
    try:
        from db import init_db
        init_db()
        print_status('pass', "Database initialized successfully")
        return True
    except Exception as e:
        print_status('fail', f"Database initialization failed: {str(e)}")
        return False

def check_env_variables():
    """Verify environment variables can be loaded"""
    from dotenv import load_dotenv
    load_dotenv()
    
    required_vars = []  # None are truly required (graceful fallbacks)
    recommended_vars = ['GOOGLE_API_KEY']
    
    optional_vars = [
        'GOOGLE_CLIENT_ID',
        'GOOGLE_CLIENT_SECRET',
        'GOOGLE_REDIRECT_URI',
    ]
    
    # Check recommended
    for var in recommended_vars:
        if os.getenv(var):
            print_status('pass', f"Recommended variable '{var}' is set")
        else:
            print_status('warn', f"Recommended variable '{var}' is NOT set (features limited)")
    
    # Check optional
    oauth_vars = [v for v in optional_vars if os.getenv(v)]
    if len(oauth_vars) == 3:
        print_status('pass', "OAuth variables are fully configured")
        return True
    elif len(oauth_vars) == 0:
        print_status('info', "OAuth variables not configured (basic auth still works)")
        return True
    else:
        print_status('warn', f"OAuth variables partially configured ({len(oauth_vars)}/3)")
        return True

def check_gitignore():
    """Verify .gitignore includes sensitive files"""
    gitignore_path = Path('.gitignore')
    if not gitignore_path.exists():
        print_status('fail', ".gitignore file missing")
        return False
    
    content = gitignore_path.read_text()
    required_patterns = ['.env', '__pycache__', '*.db', '.streamlit']
    
    all_present = True
    for pattern in required_patterns:
        if pattern in content:
            print_status('pass', f".gitignore includes '{pattern}'")
        else:
            print_status('fail', f".gitignore missing '{pattern}'")
            all_present = False
    
    return all_present

def run_validation():
    """Run all validation checks"""
    print(f"{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BLUE}FINTRIC Deployment Validation{Colors.END}")
    print(f"{Colors.BLUE}{'='*70}{Colors.END}\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Project Structure", check_project_structure),
        ("Imports", check_imports),
        ("Database", check_database),
        ("Environment Variables", check_env_variables),
        ("Git Ignore Configuration", check_gitignore),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{Colors.BLUE}Checking: {name}{Colors.END}")
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print_status('fail', f"Check failed with error: {str(e)}")
            results.append((name, False))
    
    # Summary
    print(f"\n{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BLUE}Validation Summary{Colors.END}")
    print(f"{Colors.BLUE}{'='*70}{Colors.END}\n")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = 'pass' if result else 'fail'
        print_status(status, f"{name}: {'PASSED' if result else 'FAILED'}")
    
    print(f"\nTotal: {passed}/{total} checks passed\n")
    
    if passed == total:
        print_status('pass', "✨ Application is READY for deployment! ✨")
        return 0
    else:
        print_status('fail', f"⚠️ {total - passed} checks failed. Please fix before deploying.")
        return 1

if __name__ == '__main__':
    sys.exit(run_validation())
