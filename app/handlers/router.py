@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    print("🔥 CALLBACK:", call.data)

    try:
        # ❗ ВСЕГДА ОТВЕЧАЕМ СРАЗУ
        bot.answer_callback_query(call.id)

        if not is_allowed(call.from_user.id):
            bot.answer_callback_query(
                call.id,
                "⛔ Нет доступа",
                show_alert=True
            )
            return

        data = call.data

        if data == "menu_server":
            render_server(bot, call)

        elif data == "menu_gym":
            render_gym(bot, call)

        elif data == "back_main":
            bot.edit_message_text(
                "🚀 ПАНЕЛЬ УПРАВЛЕНИЯ",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=main_menu()
            )

        elif data in ["srv_status", "srv_disk", "srv_uptime", "srv_vpn"]:
            action_server(bot, call, data)

        elif data == "gym_progress":
            bot.send_message(
                call.message.chat.id,
                get_last_workouts(call.from_user.id)
            )

    except Exception as e:
        print("🔥 CALLBACK ERROR:", e)