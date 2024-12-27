def formatTime(sec):
    # Исходное число секунд
    total_seconds = sec

    # Вычисление дней, часов, минут и секунд
    days = total_seconds // 86400  # 86400 секунд в одном дне
    hours = (total_seconds % 86400) // 3600  # 3600 секунд в одном часе
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Формирование строки в формате DD:HH:MM:SS, если есть дни
    if days > 0:
        time_str = f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"
    elif hours > 0:
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        time_str = f"{minutes:02}:{seconds:02}"

    return time_str
