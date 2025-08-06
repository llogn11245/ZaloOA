from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import FORM_URL
from services.template_service import (
    get_welcome_template_message,
    get_customercare_template_message, 
    get_reminder_template_message
)

# Temporary in-memory database - replace with real DB later
user_states = {}

def is_first_time_user(user_id):
    """Check if user is completely new (never seen before)"""
    return user_id not in user_states

def mark_user_as_seen(user_id):
    """Mark user as seen for the first time"""
    user_states[user_id] = {
        "first_seen": True, 
        "message_count": 1,  # First message
        "form_completed": False
    }

def increment_message_count(user_id):
    """Increment user message count"""
    if user_id in user_states:
        user_states[user_id]["message_count"] += 1

def mark_form_completed(user_id):
    """Mark that user completed the form"""
    if user_id in user_states:
        user_states[user_id]["form_completed"] = True

def get_user_message_count(user_id):
    """Get how many messages user has sent"""
    return user_states.get(user_id, {}).get("message_count", 0)

def has_completed_form(user_id):
    """Check if user completed the form"""
    return user_states.get(user_id, {}).get("form_completed", False)

def get_user_stage(user_id):
    """
    Determine what stage user is in:
    - 'first_time': Never seen before -> template_welcome_1
    - 'second_interaction': Has 1 interaction -> template_customercare_2  
    - 'follow_up': Has 2+ interactions, not completed -> template_customercare_3
    - 'completed': Has completed form -> thank you message
    """
    if is_first_time_user(user_id):
        return 'first_time'
    
    if has_completed_form(user_id):
        return 'completed'
        
    message_count = get_user_message_count(user_id)
    if message_count == 1:
        return 'second_interaction'
    else:
        return 'follow_up'

def get_welcome_message(user_name="Bạn"):
    """Get welcome message using template"""
    return get_welcome_template_message(user_name)

def get_form_message(user_name="Bạn"):
    """Get customer care form message using template"""
    return get_customercare_template_message(user_name, FORM_URL)

def get_after_interaction_message(user_name="Bạn"):
    """Get reminder message after user interaction using template"""
    return get_reminder_template_message(user_name, FORM_URL)
