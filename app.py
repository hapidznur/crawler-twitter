import streaming

class Crawler:

    def get_timeline(self, user):     
        return streaming.user_timeline(user)

crawler = Crawler()
print(crawler.get_timeline('elfarqy'))