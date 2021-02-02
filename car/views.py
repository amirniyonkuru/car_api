from django.shortcuts import render, redirect
import requests, json
from .models import Car
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from rest_framework import serializers


@api_view(["GET", "POST"])
def cars(request):
    if request.method == "GET":
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        carmake = request.data.get("carmake")
        carmodel = request.data.get("carmodel")

        serializer = CarSerializer(data=request.data)

        # The NHTSA Product Information Catalog Vehicle Listing Api

        external_url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{carmake}?format=json"

        # headers = {"Content-Type": "application/json"}
        res = requests.get(external_url).json()

        # get the array of car (make and model) fields only from the api request
        result = res["Results"]
        context = {"result": result}

        obj = list(
            filter(
                lambda item: item["Make_Name"] == carmake.upper()
                and item["Model_Name"] == carmodel.capitalize(),
                result,
            )
        )

        # check if the car exists and loop through all possible models of a given make
        if obj:
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)
        else:
            raise serializers.ValidationError(
                "Sorry but there is no such car in the API dataset!"
            )


@api_view(["GET", "POST"])
def car(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == "POST":
        serializer = CarSerializer(instance=car, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

    elif request.method == "GET":
        serializer = CarSerializer(car)

        return Response(serializer.data)


@api_view()
def rating(request):
    car = Car.objects.all().order_by("-id")
    serializer = CarSerializer(car, many=True)

    return Response(serializer.data)


# i was testing the templates ////

# def api_search(request):
#     if request.method == "GET":
#         make = request.GET.get("make")
#         model = request.GET.get("model")

#         # The NHTSA Product Information Catalog Vehicle Listing Api

#         external_url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"

#         res = requests.get(external_url).json()

#         # get the array of car (make and model) fields only from the api request
#         result = res["Results"]
#         context = {"result": result}

#         obj = list(
#             filter(
#                 lambda item: item["Make_Name"] == make.upper()
#                 and item["Model_Name"] == model.capitalize(),
#                 result,
#             )
#         )

#         # check if the car exists and loop through all possible models of a given make
#         if obj:
#             for obj in obj:
#                 carmodel = obj["Model_Name"]
#                 carmake = obj["Make_Name"]
#                 car = Car.objects.create(carmake=carmake, carmodel=carmodel)
#         else:
#             messages.error(request, "Sorry, but there is no such car !")

#     return render(request, "car/index.html", context)
