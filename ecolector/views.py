from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import json

def index(request):
    # Data for each ecolector user
    map_data = json.dumps([[19.32,-99.17],[19.34,-99.18],[19.33,-99.19]])
    routes_data = [["2018-09-29 05:57", 100398, "Angelopólis Sur", 999.50, 10],["2018-09-28 03:17", 100397, "Valle del Sol", 1909.10, 21], ["2018-09-26 07:59", 100395, "Angelopólis Sur", 750.50, 15]]
    context = {
        "total_kg": 25.6,
        "total_bags": 10,
        "total_routes": 100,
        "total_earning": "1,565.58",
        "actual_route": map_data,
        "routes_data": routes_data,
        "tasks": [],
        "messages": []
    }
    return render(request, 'ecolector/index.html', context)

def show_saldo(request):
    resume_data = [
        ["23/06/2019","Pago de ruta Puebla","P",52.5,52.5],
        ["20/06/2019","Retiro de saldo","R",52,0],
        ["18/06/2019","Pago de ruta Azteca","P",25.5, 52],
        ["12/06/2019","Pago de ruta Angelópolis","P",36.5,36.5]
    ]
    total_earning = 125.52
    context = {
        "resume_data": resume_data,
        "total_earning": total_earning
    }
    return render(request, 'ecolector/saldo.html', context)

def show_rutas(request):
    routes_data = [["2018-09-29 05:57", 100398, "Angelopólis Sur", 999.50, 10],["2018-09-28 03:17", 100397, "Valle del Sol", 1909.10, 21], ["2018-09-26 07:59", 100395, "Angelopólis Sur", 750.50, 15]]
    actual_route = True
    context = {
        "routes_data": routes_data,
        "actual_route": actual_route
    }
    return render(request, 'ecolector/ruta.html', context)