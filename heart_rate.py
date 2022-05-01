"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

#Get age
answer = input('Please enter your age: ')

#Convert input to integer
age = int(answer)

#Calculate ideal heart rate
heart_rate = 220 - age
slowest = heart_rate * 0.65
fastest = heart_rate * 0.85

#print message
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.')