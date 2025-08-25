from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
date_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(date_sao_paulo)
