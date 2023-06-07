from django.contrib.auth.models import User
import json
import concurrent.futures as thread_request
from django.shortcuts import render
from .models import UserProfile
import requests as fetch

def home(request):
    authorization = "Basic TXpRMmZERmlaVFZtWkRneUxXWmlOemd0TkRNek9DMDRaamMyTFRGak1XVTFOamhtTm1ZM09YeEJiSFZ0Ym05eklGQnNZV2tnUWs4PTo4NTBGRDJEOTBBQzY0QzM0OEQwNjZEOEE2NTIyQzY1Nw=="
    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/json'
    }

    response = fetch.get('https://apis.academic.lat/v3/schoolControl/students?onlyCurrentStudents=false&pageNumber=2&rowsPerPage=200', headers=headers)
    response_json = response.json()
    total_paginas = response_json["meta"]["paginacion"]["total_paginas"]
    alumnoAcademic = []

    with thread_request.ThreadPoolExecutor() as executor:
        futures = [executor.submit(buscar_alumno, request, page) for page in range(1, total_paginas + 1)]

        for future in thread_request.as_completed(futures):
            result = future.result()

            if result:
                alumnoAcademic.append(result)
                print(alumnoAcademic)
                if len(alumnoAcademic) == 5:
                    break

    return render(request, 'dist/index.html', {"json_alumno": alumnoAcademic})


def buscar_alumno(request, page):
    if request.user.is_authenticated:
        usr = User.objects.get(id=request.user.id)
        if UserProfile.objects.filter(user=usr).exists():
            perfil, created = UserProfile.objects.get_or_create(user=usr)
            authorization = "Basic TXpRMmZERmlaVFZtWkRneUxXWmlOemd0TkRNek9DMDRaamMyTFRGak1XVTFOamhtTm1ZM09YeEJiSFZ0Ym05eklGQnNZV2tnUWs4PTo4NTBGRDJEOTBBQzY0QzM0OEQwNjZEOEE2NTIyQzY1Nw=="
            headers = {
                'Authorization': authorization,
                'Content-Type': 'application/json'
            }

            response = fetch.get(f"https://apis.academic.lat/v3/schoolControl/students?onlyCurrentStudents=false&pageNumber={page}&rowsPerPage=200", headers=headers)
            response_json = response.json()

            if perfil.curp == "EXTRANJERO":
                alumnoAcademic = next((alumno for alumno in response_json["informacion"] if alumno["correo"] == usr.email), {})
            else:
                alumnoAcademic = next((alumno for alumno in response_json["informacion"] if alumno["curp"] == perfil.curp), {})

            alumnoAcademic =  alumnoAcademic if alumnoAcademic else {}

            return alumnoAcademic
    else:
        return {}

