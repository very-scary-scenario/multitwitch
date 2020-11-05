from multitwitch.lib.session import web, ajax
from pyramid.response import FileResponse

class WebView:
    @web(template="web/home.tmpl")
    def home(request):
        streams = ['veryscaryscenario', 'adzpearson']
        return {'project' : 'Very Scary Scenario does some streams',
                'streams' : streams,
                'unique_streams' : streams,
                'nstreams' : len(streams)}

    @staticmethod
    def favicon(request):
        return FileResponse("multitwitch/static/favicon.ico", content_type="image/x-icon")
