import phonenumbers 
from phonenumbers import timezone,geocoder,carrier
number=input("Enter a phone including your country code. -> ")
phone = phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en") #"en" represents english
reg=geocoder.description_for_number(phone,"en")
print(phone)
print("Time Zone of the number is",time)
print("Carrier is",car)
print("Registered area is",reg)