from django.contrib.auth.models import User
import json
from django.http import JsonResponse
import concurrent.futures as thread_request
from django.shortcuts import render
from .models import UserProfile, UsuarioAcademic
import requests as fetch
from django.core.exceptions import MultipleObjectsReturned

def home(request):
    alumnoAcademic = buscar_alumno(request)
    
    return render(request, 'dist/index.html', {"json_alumno": alumnoAcademic})


def buscar_alumno(request):
    if request.user.is_authenticated:
        usr = User.objects.get(id=request.user.id)
        if UserProfile.objects.filter(user=usr).exists():
            perfil, created = UserProfile.objects.get_or_create(user=usr)

            if perfil.curp == "EXTRANJERO" or perfil.curp == "":
                alumnoAcademic = UsuarioAcademic.objects.filter(correo_electronico=usr.email)
            else:
                alumnoAcademic = UsuarioAcademic.objects.filter(curp=perfil.curp)

            return alumnoAcademic
    else:
        return None


def getAcademicStudents(route):
    authorization = "Basic TXpRMmZERmlaVFZtWkRneUxXWmlOemd0TkRNek9DMDRaamMyTFRGak1XVTFOamhtTm1ZM09YeEJiSFZ0Ym05eklGQnNZV2tnUWs4PTo4NTBGRDJEOTBBQzY0QzM0OEQwNjZEOEE2NTIyQzY1Nw=="
    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/json'
        }
    response = fetch.get(route, headers=headers)
    return response.json()

def updateAcademicStudents(page):
    route = f"https://apis.academic.lat/v3/schoolControl/students?onlyCurrentStudents=false&pageNumber={page}&rowsPerPage=200"
    respuesta = getAcademicStudents(route)

    for alumno in respuesta["informacion"]:
        try:
            _, created = UsuarioAcademic.objects.update_or_create(
                id_alumno = alumno["id"],
                curp = alumno["curp"],
                nombre = alumno["nombre"],
                apellido_paterno = alumno["apellido_paterno"],
                apellido_materno = alumno["apellido_materno"],
                correo_electronico = alumno["informacion_contacto"]["correo_electronico"],
                matricula = alumno["matricula"],
                fecha_ingreso = alumno["fecha_ingreso"],
                oferta_educativa = alumno["inscripcion_administrativa"]["oferta_educativa"]["nombre"],
                periodo = alumno["inscripcion_administrativa"]["periodo"]["nombre"],
                fecha_inicio_periodo = alumno["inscripcion_administrativa"]["periodo"]["fecha_inicio"],
                fecha_fin_periodo = alumno["inscripcion_administrativa"]["periodo"]["fecha_fin"],
                estatus = alumno["inscripcion_administrativa"]["estatus"]["nombre"]
                )
        except MultipleObjectsReturned:
            usuario = UsuarioAcademic.objects.filter(id_alumno=alumno["id"]).first()
            if usuario:
                usuario.curp = alumno["curp"]
                usuario.nombre = alumno["nombre"]
                usuario.apellido_paterno = alumno["apellido_paterno"]
                usuario.apellido_materno = alumno["apellido_materno"]
                usuario.correo_electronico = alumno["informacion_contacto"]["correo_electronico"]
                usuario.matricula = alumno["matricula"]
                usuario.fecha_ingreso = alumno["fecha_ingreso"]
                usuario.oferta_educativa = alumno["inscripcion_administrativa"]["oferta_educativa"]["nombre"]
                usuario.periodo = alumno["inscripcion_administrativa"]["periodo"]["nombre"]
                usuario.fecha_inicio_periodo = alumno["inscripcion_administrativa"]["periodo"]["fecha_inicio"]
                usuario.fecha_fin_periodo = alumno["inscripcion_administrativa"]["periodo"]["fecha_fin"]
                usuario.estatus = alumno["inscripcion_administrativa"]["estatus"]["nombre"]
                usuario.save()
            else:
                usuario = UsuarioAcademic.objects.create(
                    id_alumno=alumno["id"],
                    curp=alumno["curp"],
                    nombre=alumno["nombre"],
                    apellido_paterno=alumno["apellido_paterno"],
                    apellido_materno=alumno["apellido_materno"],
                    correo_electronico=alumno["informacion_contacto"]["correo_electronico"],
                    matricula=alumno["matricula"],
                    fecha_ingreso=alumno["fecha_ingreso"],
                    oferta_educativa=alumno["inscripcion_administrativa"]["oferta_educativa"]["nombre"],
                    periodo=alumno["inscripcion_administrativa"]["periodo"]["nombre"],
                    fecha_inicio_periodo=alumno["inscripcion_administrativa"]["periodo"]["fecha_inicio"],
                    fecha_fin_periodo=alumno["inscripcion_administrativa"]["periodo"]["fecha_fin"],
                    estatus=alumno["inscripcion_administrativa"]["estatus"]["nombre"]
                )
    return route

def thread_processing_students(request):
    initial_route = "https://apis.academic.lat/v3/schoolControl/students?onlyCurrentStudents=false&pageNumber=1&rowsPerPage=200"
    temporal_route = initial_route
    respuesta_inicial = getAcademicStudents(temporal_route)
    total_paginas = respuesta_inicial["meta"]["paginacion"]["total_paginas"]
    
    with thread_request.ThreadPoolExecutor() as executor:
        print("Actualizando usuarios de academic students")
        futures = [executor.submit(updateAcademicStudents, page) for page in range(1, total_paginas + 1)]

        for future in thread_request.as_completed(futures):
            result = future.result()
            print(result)

    return JsonResponse({
        'respuesta': 'usuarios actualizados'
    })
