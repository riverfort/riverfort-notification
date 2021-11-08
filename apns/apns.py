import asyncio
from uuid import uuid4
from aioapns import APNs, NotificationRequest, PushType

apns = APNs(
    key="apns/auth_key/AuthKey_58M45W44RZ.p8",
    key_id="58M45W44RZ",
    team_id="A8X2W38P62",
    topic="com.RiverFort",  # Bundle ID
    use_sandbox=False,
)


def payload(companyNews):
    payload = {
        "aps": {
            "alert": {
                "title": "New Announcement",
                "subtitle": "{} ({})".format(
                    companyNews.company_name, companyNews.company_symbol
                ),
                "body": "{}".format(companyNews.headline),
            },
            "sound": "default",
        },
        "link": "{}".format(companyNews.link),
    }
    return payload


async def run(device_token, company_news):
    apns_key_client = apns
    request = NotificationRequest(
        device_token=device_token,
        message=payload(company_news),
    )
    await apns_key_client.send_notification(request)
