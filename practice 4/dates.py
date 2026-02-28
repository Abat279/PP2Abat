from datetime import datetime, timedelta

# 1. Current date and time
now = datetime.now()
print(now)

# 2. Format date
print(now.strftime("%Y-%m-%d"))

# 3. Tomorrow
tomorrow = now + timedelta(days=1)
print(tomorrow)

# 4. Yesterday
yesterday = now - timedelta(days=1)
print(yesterday)

# 5. Difference between two dates
d1 = datetime(2026, 1, 1)
d2 = datetime(2026, 1, 10)
print((d2 - d1).days)