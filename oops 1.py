class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_time(self, other_time):
        total_seconds = (self.hours + other_time.hours) * 3600 + \
                        (self.minutes + other_time.minutes) * 60 + \
                        self.seconds + other_time.seconds

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return Time(hours, minutes, seconds)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Input times
time1 = Time(3, 45, 30)
time2 = Time(1, 30, 15)

# Add the two times
result_time = time1.add_time(time2)

# Display the result
