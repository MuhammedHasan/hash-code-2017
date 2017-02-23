from cache_server import CacheServer
from video import Video
from endpoint import Endpoint


def line_to_int_list(f):
    return list(map(int, f.readline().strip().split()))


def read_data(filename):
    with open('../inputs/%s.in' % filename) as f:
        fl = line_to_int_list(f)
        num_endpoint = fl[1]
        num_request = fl[2]
        num_cache = fl[3]
        cache_size = fl[4]

        cache_servers = [CacheServer(i, cache_size) for i in range(num_cache)]

        vidoe_sizes = line_to_int_list(f)
        vidoes = [Video(i, s) for i, s in enumerate(vidoe_sizes)]

        end_points = list()
        for i in range(num_endpoint):
            l = line_to_int_list(f)
            endpoint = Endpoint(i)
            for j in range(l[1]):
                ll = line_to_int_list(f)
                cache_serv = cache_servers[ll[0]]
                endpoint.latency.append((ll[1], cache_serv))
            end_points.append(endpoint)

        for i in range(num_request):
            lr = line_to_int_list(f)
            vi = vidoes[lr[0]]
            end_points[lr[1]].requests.append((lr[2], vi))

        return (cache_servers, vidoes, end_points)
