from django.db import models
from django.db.models import Model

class Employee(Model):

    class Marital(models.IntegerChoices):
        SINGLE = 0
        MARRIED = 1

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    passport = models.CharField(max_length=30)
    marital_status = models.IntegerField(choices=Marital.choices)
    education = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    e_mail = models.EmailField()
    rank = models.CharField(max_length=25)
    employ_date = models.DateField()
    work_experience = models.IntegerField()

class Crew(Model):
    name = models.CharField(max_length=25)
    employee = models.ManyToManyField(Employee, through="CrewComposition")

class CrewComposition(Model):
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Region(Model):
    coordinates = models.CharField(max_length=20)
    landscape = models.CharField(max_length=100)
    peculiarity = models.CharField(max_length=100)

class WheatherData(Model):
    temperature = models.IntegerField()
    precipitation = models.IntegerField()
    wind_speed = models.IntegerField()
    wind_direction = models.CharField(max_length=100)
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    date = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Airfield(Model):
    name = models.CharField(max_length=100)
    runway_class = models.CharField(max_length=2)
    class_by_take_off_weight = models.IntegerField()


class Route(Model):
    name = models.CharField(max_length=100)
    take_off_airfield = models.ForeignKey(Airfield, on_delete=models.CASCADE, related_name="take_off_airfield")
    landing_airfield = models.ForeignKey(Airfield, on_delete=models.CASCADE, related_name="landing_airfield")
    region = models.ManyToManyField(Region, through="RouteComposition")

class RouteComposition(Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    flight_profile = models.CharField(max_length=100)

class Aircraft(Model):
    registration_number = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    year_of_release = models.DateField()
    payload = models.IntegerField()
    appointment = models.CharField(max_length=100)
    fixed_crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    home_airfield = models.ForeignKey(Airfield, on_delete=models.CASCADE)

class FlightAssignment(Model):
    purpose = models.CharField(max_length=100)
    date_flight = models.DateField()
    registration_number_aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)

class FuelAndLubricants(Model):
    name_CLM = models.CharField(max_length=25)
    class_CLM = models.IntegerField()
    type_CLM = models.CharField(max_length=25)

class FuelCapacity(Model):
    name_CLM = models.ForeignKey(FuelAndLubricants, on_delete=models.CASCADE)
    amount_of_CLM = models.IntegerField()

class ExpenditureCLM(Model):
    airfield = models.ForeignKey(Airfield, on_delete=models.CASCADE)
    name_CLM = models.ForeignKey(FuelAndLubricants, on_delete=models.CASCADE)
    expenditure_CLM =  models.IntegerField()
