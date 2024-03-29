import requests
from rich import console
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

console = console.Console()
APP_ID = '<APP-ID>'
SCOPES = ['Calendars.ReadWrite']

# Step 1. Generate Access Token
access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

# Step 2.1 Create an event
def construct_event_detail(event_name, **event_details):
    request_body = {
        'subject': event_name
    }
    for key, val in event_details.items():
        request_body[key] = val
    return request_body

response1_create = requests.post(
    GRAPH_API_ENDPOINT + f'/me/events',
    headers=headers,
    json=construct_event_detail('Movie Night')
)
console.print(response1_create.json())

# delete an event
# event_id1 = response1_create.json()['id']
# resposne1_delete = requests.delete(
#     GRAPH_API_ENDPOINT + f'/me/events/{event_id1}',
#     headers=headers
# )
# print(resposne1_delete.status_code)

# Step 2.2 Example (Detailed)
event_name = 'Work Holiday'
body = {
    # html or text
    'contentType': 'html',
    'content': '<b>2 weeks vacation</b>'
}
start = {
    'dateTime': '2022-04-25T08:00:00',
    'timeZone': 'America/Los_Angeles'
}
end = {
    'dateTime': '2022-05-02T17:00:00',
    'timeZone': 'America/Los_Angeles'
}
location = {
    'displayName': 'Tokyo, Japan'
}
attendees = [
    {
        'emailAddress': {
            'address': 'kevinkirui1340@gmail.com'
        },
         'type': 'required' # or optional
    }
]

response2_create = requests.post(
    GRAPH_API_ENDPOINT + f'/me/events',
    headers=headers,
    json=construct_event_detail(
            event_name,
            body=body,
            location=location,
            start=start,
            end=end,
            attendees=attendees,
        )
)
console.print(response2_create.json())


event_id2 = response2_create.json()['id']
resposne2_delete = requests.post(
    GRAPH_API_ENDPOINT + f'/me/events/{event_id2}/cancel',
    headers=headers
)
print(resposne2_delete.status_code)
print(resposne2_delete.reason)
