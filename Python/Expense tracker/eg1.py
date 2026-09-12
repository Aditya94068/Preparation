from datetime import datetime
date = "01-02-2026"
ans = datetime.strptime(date,"%d-%m-%Y")
print(ans)

print(ans.date())
print(ans.day)
print(ans.month)
print(ans.year)

print(ans.strftime("%B %Y"))