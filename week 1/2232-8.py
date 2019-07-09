X = int(input())
H = int(input())
M = int(input())
start_night = H * 60 + M
longless = start_night + X
wake_time_hour = longless // 60
wake_time_minutes = longless % 60
print(wake_time_hour)
print(wake_time_minutes)