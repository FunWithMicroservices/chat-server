from rest_framework.generics import CreateAPIView, RetrieveAPIView


class SlackAPI(CreateAPIView, RetrieveAPIView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


slack_api = SlackAPI.as_view()
