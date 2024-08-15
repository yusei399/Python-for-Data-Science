from datetime import date
import time

today = date.today()
current_time = time.time()
day_s = today.strftime("%B %d, %Y")
day_1 = today.strftime("%b %d, %Y")
ft_string = []
ft_string.append("Seconds since {}: {:.2e} in scientific notation".format(day_s, current_time))
for i in ft_string:
	print(i)
print(day_1)