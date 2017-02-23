class CacheServer:

    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.videos = list()

    def store(self, video):
        if self.is_there_place_for(video):
            self.videos.append(video)
        else:
            raise ValueError('there is no place for you')

    def is_there_place_for(self, video):
        return self.size >= self.total_size_of_videos() + video.size

    def total_size_of_videos(self):
        return sum(i.size for i in self.videos)
