from flask import Blueprint, request
from applications.public.http_tool import check_login_encrypt, not_check_login
from applications.units import tools
from applications.public.api import ApiResult
from applications.configs import errorCode

ota1411_update_view = Blueprint('1411ota_version',
                                __name__,
                                url_prefix='/cloud-ota')
log = tools.getLogger("1411ota_version")


@ota1411_update_view.route('/pltcheck', methods=["GET"])
# @not_check_login
def cloud_ota_1411():
    sn = request.args.get('sn', type=str)
    platform = request.args.get('platform', type=str)
    version = request.args.get('version', type=str)

    result = ApiResult.get_inst()
    api_data = {}
    api_data["md5"] = '11844a676d48b35f1645c4f52147665b'
    api_data['name'] = 'B-MD2FP1411V1.20-240415-re298.bin'
    api_data['platform'] = platform
    api_data['version'] = version
    api_data['sn'] = sn

    api_data['path'] = "http://www.prismxr.net:8010/static/bin/B-MD2FP1411V1.20-240415-re298.bin"

    # api_data[
    # 'tws_url'] = "http://49.234.155.206:5100/static/password/bin/EPH-YM-TLSR9516A-P1201-A-ADK-V0-230731-V110.bin"
    api_data['textNotes'] = "Firmware released V1.20"
    api_data['desc']=[
        "Fixed one display issue within APP"
    ]
    return result.success(data=api_data)
