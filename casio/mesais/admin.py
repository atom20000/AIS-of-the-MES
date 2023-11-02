from django.contrib import admin

from .models import *

@admin.register(
    Employee,
    Crew,
    CrewComposition,
    Region,
    WheatherData,
    Airfield,
    Route,
    RouteComposition,
    Aircraft,
    FlightAssignment,
    FuelAndLubricants,
    FuelCapacity,
    ExpenditureCLM
)
class MesaisAdmin(admin.ModelAdmin):
    pass