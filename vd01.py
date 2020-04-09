import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Ngô Thị Mai Trâm 2172107 !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
