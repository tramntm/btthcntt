import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Ngo Thi Mai Tram 2172107 !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
