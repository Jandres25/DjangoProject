from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import requests

def obtener_datos():
    url = "https://www.freetogame.com/api/games"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener los datos. Código de estado {response.status_code}")
        return None

def mostrar_api(request):
    # Llamamos a la función para obtener los datos de la API
    datos = obtener_datos()

    # Verificar si obtuvimos los datos
    if datos is not None:
        # Implementar la paginación
        items_per_page = 10  # Número de elementos por página
        paginator = Paginator(datos, items_per_page)

        # Obtener el número de página desde la solicitud GET. Si no está disponible, establecer la página 1 como predeterminada.
        page_number = request.GET.get('page', 1)
    
        try:
            # Obtener la página solicitada
            page = paginator.page(page_number)
        except EmptyPage:
            # Si el número de página está fuera de rango (por ejemplo, página 99999), mostrar la última página.
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            # Si el número de página no es un número entero, mostrar la primera página.
            page = paginator.page(1)

        return render(request, 'api.html', {'page': page})  # Contexto que se pasa al template

    return render(request, 'api.html', {'page': None})  # Si no se obtuvieron datos, pasar el objeto 'page' como None al contexto

