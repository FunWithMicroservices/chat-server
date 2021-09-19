# API & Websocket Documentation


<a name="toc_web_api"></a>

## ToC HTTP API
- [Create Thread](#create_thread)
- [Retrieve Thread](#retrieve_thread)
- [Post Message](#post_message)


<a name="toc_websockets"></a>

## ToC Websockets
- [Chat Websockets](#chat_websocket)


<a name="create_thread"></a>

### Create Thread
This Endpoint will create a thread on post request.

**Request Information**
| Type | URL                 |
| ---- | ------------------- |
| POST | /chat/thread/       |

**Header**
| Type         | Property name    |
| ------------ | ---------------- |
| Content-Type | application/json |

**JSON Body**
| Property Name | type | required | Description |
| ------------- | ---- | -------- | ----------- |
| user          | JSON | YES      | unstructured information given as JSON |

**Error Responses**
| Code | Message                                |
| ---- | -------------------------------------- |
| 400  | "This field may not be blank."         |

**Success Response**
| Property Name | type | Description |
| ------------- | ---- | ----------- |
| id            | uuid | unique thread identifier (uuid1)        |
| user          | JSON | previous sent user information          |
| timestamp     | str  | Timestamp in Format YYYY-mm-ddTMM:HH:SS |
| messages      | list | Empty list                              |


<a name="retrieve_thread"></a>

### Retrieve Thread
This endpoint will retrieve the full communication for a given thread.

**Request Information**
| Type | URL                     |
| ---- | ----------------------- |
| GET  | /chat/thread/:threadId/ |

**Header**
| Type         | Property name    |
| ------------ | ---------------- |
| Content-Type | application/json |

**Error Responses**
| Code | Message   |
| ---- | --------- |
| 404  | Not Found |

**Success Response**
| Property Name | type | Description |
| ------------- | ---- | ----------- |
| id            | uuid | unique thread identifier (uuid1)        |
| user          | JSON | previous sent user information          |
| timestamp     | str  | Timestamp in Format YYYY-mm-dd MM:HH:SS |
| messages      | list[messages] | List of `messages` which where already sent within that thread |

| _Message_     |      |             |
| ------------- | ---- | ----------- |
| Property Name | type | Description |
| ------------- | ---- | ----------- |
| id            | uuid | unique thread identifier (uuid1)         |
| user          | JSON | Information about author of that message |
| timestamp     | str  | Timestamp in Format YYYY-mm-dd MM:HH:SS  |
| body          | str  | Body of that message                     |
| send_by_user  | bool | If true: this message is sent by user, else via slack |


<a name="post_message"></a>

### Post Message
Its an endpoint for sending messages to a thread via post request.

**Request Information**
| Type | URL                 |
| ---- | ------------------- |
| POST | /chat/message/      |

**Header**
| Type         | Property name    |
| ------------ | ---------------- |
| Content-Type | application/json |

**JSON Body**
| Property Name | type | required | Description |
| ------------- | ---- | -------- | ----------- |
| user          | JSON | YES      | unstructured information given as JSON |
| thread        | uuid | YES      | id for thread where this message should belong to |
| body          | str  | YES      | Body of message which should be sent |
| send_by_user  | bool | NO       | If true: this message is sent by user, else via slack. __Default__: false |

**Error Responses**
| Code | Message                                |
| ---- | -------------------------------------- |
| 400  | "This field may not be blank."         |

**Success Response**
| Property Name | type | Description |
| ------------- | ---- | ----------- |
| id            | uuid | unique thread identifier (uuid1)         |
| user          | JSON | Information about author of that message |
| timestamp     | str  | Timestamp in Format YYYY-mm-dd MM:HH:SS  |
| body          | str  | Body of that message                     |
| send_by_user  | bool | If true: this message is sent by user, else via slack |
| thread        | uuid | Reference to thread where message should be sent to |


<a name="chat_websocket"></a>

### Chat Websocket
It's about Websocket Connection for chat

**Request Information**
| Type | URL                 |
| ---- | ------------------- |
| POST | ws/chat/:threadId   |

**Important:** you do not need to use the `api/` prefix anymore
Route should be like `ws://localhost:8000/ws/chat/:threadId/`

**On Message**
You are receiving Thread Messages on this event.

| Property Name | type | Description |
| ------------- | ---- | ----------- |
| id            | uuid | unique thread identifier (uuid1)         |
| user          | JSON | Information about author of that message |
| timestamp     | str  | Timestamp in Format YYYY-mm-dd MM:HH:SS  |
| body          | str  | Body of that message                     |
| send_by_user  | bool | If true: this message is sent by user, else via slack |
| thread        | uuid | Reference to thread where message should be sent to |
