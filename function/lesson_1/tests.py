from handler import send_email

# Тесты для функции create_and_send_message

def test_normal_mode():
    """Тест для режима 'normal'."""
    recipient = "test@example.com"
    template = "Здравствуйте, {name}! Спасибо за регистрацию."
    mode = "normal"
    result = send_email(recipient, template, mode=mode)
    expected = {
        "status": "success",
        "message": "Сообщение отправлено.",
        "recipient": "test@example.com",
        "message": "Здравствуйте, test! Спасибо за регистрацию."
    }
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_preview_mode():
    """Тест для режима 'preview'."""
    recipient = "user@domain.com"
    template = "Добрый день, {name}! Ваш заказ готов."
    mode = "preview"
    result = send_email(recipient, template, mode=mode)
    expected = {
        "status": "preview",
        "message": "Сообщение готово к отправке.",
        "recipient": "user@domain.com",
        "message": "Добрый день, user! Ваш заказ готов."
    }
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_debug_mode():
    """Тест для режима 'debug'."""
    recipient = "admin@company.com"
    template = "Привет, {name}! Проверьте систему."
    mode = "debug"
    result = send_email(recipient, template, mode=mode)
    expected = {
        "status": "debug",
        "message": "Отладочная информация.",
        "recipient": "admin@company.com",
        "message": "Привет, admin! Проверьте систему."
    }
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

def test_invalid_mode():
    """Тест для некорректного режима."""
    recipient = "test@example.com"
    template = "Здравствуйте, {name}! Спасибо за регистрацию."
    mode = "invalid_mode"
    message = send_email(recipient, template, mode=mode)
    assert message == f"Неизвестный режим: {mode}. Используйте 'normal', 'preview', 'debug'."


def test_invalid_email():
    """Тест для некорректного email."""
    recipient = "invalid_email"
    template = "Здравствуйте, {name}! Спасибо за регистрацию."
    message = send_email(recipient, template)
    assert message == "Некорректный адрес получателя. Укажите валидный email."


def test_invalid_template():
    """Тест для некорректного шаблона."""
    recipient = "test@example.com"
    template = "Здравствуйте! Спасибо за регистрацию."
    message = send_email(recipient, template)
    assert message == "Некорректный шаблон сообщения. Убедитесь, что он содержит {name} для подстановки.", f"Ожидалось исключение TemplateError, получено: {e}"


if __name__ == "__main__":
    test_normal_mode()
    test_preview_mode()
    test_debug_mode()
    test_invalid_mode()
    test_invalid_email()
    test_invalid_template()
