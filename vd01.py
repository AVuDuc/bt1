import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Vũ Đức Anh !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
