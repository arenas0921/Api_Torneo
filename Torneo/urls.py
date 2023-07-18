from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('api/torneo', TorneoViewSet, 'torneo')
router.register('api/fecha', FechaViewSet, 'fecha')
router.register('api/partido', PartidoViewSet, 'partido')
router.register('api/equipo', EquipoViewSet, 'equipo')
router.register('api/partido_equipo', Partido_EquipoViewSet, 'partido_equipo')
router.register('api/jugador', JugadorViewSet, 'jugador')
router.register('api/tecnico', TecnicoViewSet, 'tecnico')


urlpatterns = router.urls

