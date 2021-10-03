import asyncio
from uuid import uuid4
from aioapns import APNs, NotificationRequest, PushType

apns = APNs(
    key="auth_key/AuthKey_58M45W44RZ.p8",
    key_id="58M45W44RZ",
    team_id="A8X2W38P62",
    topic="com.RiverFort",  # Bundle ID
    use_sandbox=True,
)


def payload(company_symbol, title, link):
    payload = {
        "aps": {
            "alert": {
                "title": "{}: New Announcement".format(company_symbol),
                "body": "{}".format(title),
            },
            "sound": "default",
            "badge": "1",
        }
    }
    return payload


async def run(device_token, company_symbol, title, link):
    apns_key_client = apns
    request = NotificationRequest(
        device_token=device_token,
        message=payload(company_symbol, title, link),
    )
    await apns_key_client.send_notification(request)
