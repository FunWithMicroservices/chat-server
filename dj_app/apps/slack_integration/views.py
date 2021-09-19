from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class SlackAPI(CreateAPIView):
    def post(self, request, *args, **kwargs):
        challenge = request.data["challenge"]
        return Response({"challenge": challenge})


slack_api = SlackAPI.as_view()
