async def handle_yes(query):
    await query.edit_message_text("Bạn chọn tạo tài khoản BCP rồi \ncảm ơn bạn")

async def handle_no(query):
    await query.edit_message_text("Bạn chọn chưa tạo tài khoản BCP \nmình mong bạn sẽ tạo tài khoản, BCP rất tuyệt")