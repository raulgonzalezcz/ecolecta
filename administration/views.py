from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import json

def index(request):
    # Data for each ecolector user
    places_data_d = [[1515,"México","Puebla","Angelópolis", "Angelópolis Sur","Carlos A.","carlos@gmail.com","Fachada de color azul con lozetas de barro","2 veces por semana"],[1150,"México","Puebla","Valle del Sol", "Sección Sur","Juan B.","juan@gmail.com","Fachada de color rojo sin lozetas","1 vez por semana"],[917,"México","Puebla","Centro", "Sección Norte","Rodrigo C.","rodri@gmail.com","Fachada de color verde","5 veces por semana"]]
    places_data_r = [[1515,"México","Puebla","Centro", "Sección Sur","Carlos M.","carlosm@gmail.com","Fachada de color verde con lozetas de barro","4 veces por semana"]]
    routes_data = [["2018-09-29 05:57", 100398, "Angelopólis Sur", 999.50, 10],["2018-09-28 03:17", 100397, "Valle del Sol", 1909.10, 21], ["2018-09-26 07:59", 100395, "Angelopólis Sur", 750.50, 15]]
    context = {
        "total_kg": 25.6,
        "total_bags": 10,
        "total_routes": 100,
        "total_earning": 1565.58,
        "places_data_d": places_data_d,
        "places_data_r": places_data_r,
        "routes_data": routes_data,
        "tasks": [],
        "messages": []
    }
    return render(request, 'administration/index-admin.html', context)

def show_lugar_domestico(request):
    countries = ["México"]
    zones = ["Puebla","Oaxaca","CDMX"]
    fracs = ["Angelópolis","Valle del Sol","Centro","Villa Frontera","CU"]
    subfracs = ["Sección sur","Sección norte","Sección II"]
    
    #Sort data
    countries.sort()
    zones.sort()
    fracs.sort()
    subfracs.sort()

    data_select = [countries,zones,fracs,subfracs]

    places_data_d = [[1515,"México","Puebla","Angelópolis", "Angelópolis Sur","Carlos A.","carlos@gmail.com","Fachada de color azul con lozetas de barro","2 veces por semana"],[1150,"México","Puebla","Valle del Sol", "Sección Sur","Juan B.","juan@gmail.com","Fachada de color rojo sin lozetas","1 vez por semana"],[917,"México","Puebla","Centro", "Sección Norte","Rodrigo C.","rodri@gmail.com","Fachada de color verde","5 veces por semana"]]
    places_data_r = [[1515,"México","Puebla","Centro", "Sección Sur","Carlos M.","carlosm@gmail.com","Fachada de color verde con lozetas de barro","4 veces por semana"]]
    context = {
        "places_data_d": places_data_d,
        "places_data_r": places_data_r,
        "data_select": data_select
    }
    return render(request, 'administration/lugar_domestico.html', context)

def show_lugar_comercio(request):
    countries = ["México"]
    zones = ["Puebla","Oaxaca","CDMX"]
    fracs = ["Angelópolis","Valle del Sol","Centro","Villa Frontera","CU"]
    subfracs = ["Sección sur","Sección norte","Sección II"]
    
    #Sort data
    countries.sort()
    zones.sort()
    fracs.sort()
    subfracs.sort()

    data_select = [countries,zones,fracs,subfracs]

    places_data_d = [[1515,"México","Puebla","Angelópolis", "Angelópolis Sur","Carlos A.","carlos@gmail.com","Fachada de color azul con lozetas de barro","2 veces por semana"],[1150,"México","Puebla","Valle del Sol", "Sección Sur","Juan B.","juan@gmail.com","Fachada de color rojo sin lozetas","1 vez por semana"],[917,"México","Puebla","Centro", "Sección Norte","Rodrigo C.","rodri@gmail.com","Fachada de color verde","5 veces por semana"]]
    places_data_r = [[1515,"México","Puebla","Centro", "Sección Sur","Carlos M.","carlosm@gmail.com","Fachada de color verde con lozetas de barro","4 veces por semana"]]
    context = {
        "places_data_d": places_data_d,
        "places_data_r": places_data_r,
        "data_select": data_select
    }
    return render(request, 'administration/lugar_comercio.html', context)

def show_catalogo(request):
    countries = ["México"]
    zones = ["Puebla","Oaxaca","CDMX"]
    fracs = ["Angelópolis","Valle del Sol","Centro","Villa Frontera","CU"]
    subfracs = ["Sección sur","Sección norte","Sección II"]
    
    #Sort data
    countries.sort()
    zones.sort()
    fracs.sort()
    subfracs.sort()

    data_select = [countries,zones,fracs,subfracs]

    places_data_d = [[1515,"México","Puebla","Angelópolis", "Angelópolis Sur","Carlos A.","carlos@gmail.com","Fachada de color azul con lozetas de barro","2 veces por semana"],[1150,"México","Puebla","Valle del Sol", "Sección Sur","Juan B.","juan@gmail.com","Fachada de color rojo sin lozetas","1 vez por semana"],[917,"México","Puebla","Centro", "Sección Norte","Rodrigo C.","rodri@gmail.com","Fachada de color verde","5 veces por semana"]]
    places_data_r = [[1515,"México","Puebla","Centro", "Sección Sur","Carlos M.","carlosm@gmail.com","Fachada de color verde con lozetas de barro","4 veces por semana"]]
    context = {
        "places_data_d": places_data_d,
        "places_data_r": places_data_r,
        "data_select": data_select
    }
    return render(request, 'administration/catalogo.html', context)

def show_ruta(request):
    countries = ["México"]
    zones = ["Puebla","Oaxaca","CDMX"]
    fracs = ["Angelópolis","Valle del Sol","Centro","Villa Frontera","CU"]
    subfracs = ["Sección sur","Sección norte","Sección II"]
    
    #Sort data
    countries.sort()
    zones.sort()
    fracs.sort()
    subfracs.sort()

    data_select = [countries,zones,fracs,subfracs]

    current_routes = {
        "Angelopolis Sur": ["casa1","casa2","casa3"],
        "Valle del Sol": ["edi1","edi2","edi3"],
        "Centro": ["apar1","apar2"]
    }
    available_routes = ["dis1","dis2"]
    routes_data = [[100398, "Mexico", "Puebla", "Angelópolis", "Angelopólis Sur", 999.50, 10, 5, 9],[100398, "Mexico", "Puebla", "Valle del Sol", "Zona Norte", 99.50, 11, 6, 10], [100398, "Mexico", "Puebla", "Centro", "Sur", 75.10, 10, 5, 9]]
    context = {
        "available_routes": available_routes,
        "current_routes": current_routes,
        "routes_data": routes_data,
        "data_select": data_select
    }
    return render(request, 'administration/rutas.html', context)

def show_tesoreria(request):
    current_transfers = [
        ["19/08/19","Juan Pérez","JuanPerez.pdf","JuanPerez.xml","600.50"],
        ["19/08/19","Jorge Medrano","JorgeMedrano.pdf","JorgeMedrano.xml","100.50"],
        ["18/08/19","Arturo Ortiz","ArtutoOrtiz.pdf","ArturoOrtiz.xml","90"],
        ["15/08/19","Arturo Loya","ArturoLoya.pdf","ArturoLoya.xml","500.75"],
        ["15/08/19","Pablo Pérez","PabloPerez.pdf","PabloPerez.xml","1,800.50"]
    ]
    context = {
        "current_transfers": current_transfers
    }
    return render(request, 'administration/tesoreria.html', context)
