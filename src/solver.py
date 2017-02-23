from services import *


class Solver:

    def __init__(self, filename):
        self.caches = dict()
        self.filename = filename
        (self.cache_servers, self.vidoes, self.end_points) = \
            read_data(filename)

    def store_video(self, cache_id, video_id):
        if cache_id not in self.caches:
            self.caches[cache_id] = set()
        self.caches[cache_id].add(video_id)

    def solve(self):
        req_end = [[end, req_vi[0], req_vi[1]]
                   for end in self.end_points for req_vi in end.requests]

        video_hist = dict()

        for (end_point, req, video) in req_end:
            video_hist.setdefault(video, 0)
            video_hist[video] += req

        for i in range(len(req_end)):
            req_end[i][1] = video_hist[req_end[i][2]]

        for (end_point, req, video) in sorted(req_end, key=lambda x: 25 * x[2].size - x[1]):
            if end_point.has_video_in_cache(video):
                continue
            for la, cac in sorted(end_point.latency, key=lambda x: x[0]):
                if cac.is_there_place_for(video):
                    cac.store(video)
                    self.store_video(cac.id, video.id)
                    break

    def parse(self):
        with open('../outputs/%s.txt' % self.filename, 'w') as f:
            f.write('%d\n' % len(self.caches))
            for k, v in self.caches.items():
                f.write(str(k))
                for j in v:
                    f.write(' %d' % j)
                f.write('\n')
