# ZaloOA Integration Guide

## Core Components

### 1. BotService (src/services/bot_service.py)
- Contains all business logic
- Platform independent
- Input: `UserAction` objects
- Output: `BotResponse` objects

### 2. ZaloAdapter (src/adapters/zalo_adapter.py)
**TODO: Implement these methods:**

#### convert_to_user_action(zalo_data)
Convert ZaloOA webhook data to UserAction format

#### send_response(response, zalo_context)  
Send BotResponse using ZaloOA API

#### convert_keyboard(telegram_keyboard)
Convert keyboard format to ZaloOA quick replies

### 3. Integration Steps
1. Implement ZaloAdapter methods
2. Create ZaloOA webhook handler
3. Use BotService for business logic
4. Test with ZaloOA sandbox

### 4. Example Usage
```python
# In your ZaloOA webhook handler
zalo_adapter = ZaloAdapter()
bot_service = BotService()

user_action = zalo_adapter.convert_to_user_action(webhook_data)
response = bot_service.handle_text_message(user_action)
await zalo_adapter.send_response(response, zalo_context)
```