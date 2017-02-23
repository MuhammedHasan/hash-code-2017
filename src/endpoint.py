class Endpoint:

    def __init__(self, id):
        self.id = id
        self.requests = list()  # list of tuple (r,vi)
        self.latency = list()  # list of tuple (l,c)

    def max_video(self):
        return min(self.requests, key=lambda x: x[1].size)[1]

    def sort_latency(self):
        pass

    def has_video_in_cache(self, video):
        for l, c in self.latency:
            if video in c.videos:
                return True
