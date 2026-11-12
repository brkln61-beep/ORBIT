from config import APP_NAME, DEBUG, VERSION


def main():
    print(f"Запуск приложения: {APP_NAME}")
    print(f"Версия: {VERSION}")
    print(f"Режим отладки: {DEBUG}")


if __name__ == "__main__":
    main()