import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Vu Duc Anh !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
