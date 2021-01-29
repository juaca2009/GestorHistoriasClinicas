from services.adminP_servicie import adminP_servicie
from services.ciudad_service import ciudad_service
from services.tipoDocumento_service import tipoDocumento_servicie
from services.login_service import login_servicie
from services.solicitudes_service import solicitudes_service
from services.adminC_service import adminC_service

service_adminP = adminP_servicie()
service_ciudad = ciudad_service()
service_tdocumento = tipoDocumento_servicie()
services_login = login_servicie()
services_solicitudes = solicitudes_service()
services_adminC = adminC_service()
