import logging
from enum import Enum

from .exception import TemplateError, EmailAddressError, ModeError


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def create_and_send_message(recipient, template, mode="normal"):
    """
    Создает и имитирует отправку сообщения на почту по указанному шаблону.

    :param recipient: str, адрес получателя (обязательный параметр).
    :param template: str, шаблон сообщения с подстановкой {name} для имени получателя.
    :param mode: str, режим работы функции (необязательный параметр, по умолчанию "normal").
                 Возможные значения: "normal", "preview", "debug", "silent".
    :return: dict, результат выполнения функции.
    """
    if not isinstance(recipient, str) or "@" not in recipient:
        raise EmailAddressError("Некорректный адрес получателя. Укажите валидный email.")

    if not isinstance(template, str) or "{name}" not in template:
        raise TemplateError("Некорректный шаблон сообщения. Убедитесь, что он содержит {name} для подстановки.")

    name = recipient.split("@")[0]
    message = template.format(name=name)

    if mode == "normal":
        logger.info(f"Отправка сообщения на адрес {recipient}:\n{message}\n")
        return {"status": "success", "message": "Сообщение отправлено.", "recipient": recipient, "message": message}

    elif mode == "preview":
        logger.info(f"Предварительный просмотр сообщения для {recipient}:\n{message}\n")
        return {"status": "preview", "message": "Сообщение готово к отправке.", "recipient": recipient,
                "message": message}

    elif mode == "debug":
        logger.info(f"[DEBUG] Данные для отправки:\nПолучатель: {recipient}\nСообщение: {message}\n")
        return {"status": "debug", "message": "Отладочная информация.", "recipient": recipient, "message": message}

    else:
        raise ModeError(f"Неизвестный режим: {mode}. Используйте 'normal', 'preview', 'debug'.")
