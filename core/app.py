class OrbitApp:
    def __init__(self):
        self.is_running = False
        self.start_count = 0

    def start(self):
        if self.is_running:
            print("ORBIT уже запущен")
            return


        self.is_running = True
        self.start_count += 1
        print(f"Количество запусков: {self.start_count}")
        print("ORBIT запущен!")

    def stop(self):
        if not self.is_running:
            print("ORBIT уже остановлен!")
            return

        self.is_running = False
        print("ORBIT остановлен!")

    def status(self):
        return self.is_running
        
    def get_start_count(self):
        return self.start_count