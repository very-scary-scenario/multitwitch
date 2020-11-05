from multitwitch.lib.session import web, ajax
from pyramid.response import FileResponse
from pyramid.httpexceptions import HTTPFound

class WebView:
    @web(template="web/home.tmpl")
    def home(request):
        if request.path != '/':
            raise HTTPFound(request.route_path('root', streams=[]))

        streams = ['veryscaryscenario', 'adzpearson']
        return {'project' : 'Very Scary Scenario does some streams',
                'streams' : streams,
                'unique_streams' : streams,
                'nstreams' : len(streams)}

    @staticmethod
    def favicon(request):
        return FileResponse("multitwitch/static/favicon.ico", content_type="image/x-icon")
