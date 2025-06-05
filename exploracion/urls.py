from django.urls import path
from . import views

urlpatterns = [
    path('misiones/', views.MisionList.as_view(), name='mision_list'),
    path('misiones/crear/', views.MisionCreate.as_view(), name='mision_create'),
    path('misiones/editar/<int:pk>/', views.MisionUpdate.as_view(), name='mision_update'),
    path('misiones/eliminar/<int:pk>/', views.MisionDelete.as_view(), name='mision_delete'),

    path('astronautas/', views.AstronautaList.as_view(), name='astronauta_list'),
    path('astronautas/crear/', views.AstronautaCreate.as_view(), name='astronauta_create'),
    path('astronautas/editar/<int:pk>/', views.AstronautaUpdate.as_view(), name='astronauta_update'),
    path('astronautas/eliminar/<int:pk>/', views.AstronautaDelete.as_view(), name='astronauta_delete'),

    path('experimentos/', views.ExperimentoList.as_view(), name='experimento_list'),
    path('experimentos/crear/', views.ExperimentoCreate.as_view(), name='experimento_create'),
    path('experimentos/editar/<int:pk>/', views.ExperimentoUpdate.as_view(), name='experimento_update'),
    path('experimentos/eliminar/<int:pk>/', views.ExperimentoDelete.as_view(), name='experimento_delete'),
]
