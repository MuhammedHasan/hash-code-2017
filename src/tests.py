import unittest

from video import Video
from endpoint import Endpoint
from cache_server import CacheServer
from services import *


class TestVideoCacher(unittest.TestCase):

    def setUp(self):
        self.videos = [Video(0, 50), Video(1, 30)]
        self.cache_servers = [
            CacheServer(0, 40)
        ]
        self.endpoints = [
            Endpoint(0, {0: 100, 1: 200}, [(10, self.cache_servers[0])]),
            Endpoint(0, {0: 100, 1: 50})
        ]

    def test_store(self):
        self.cache_servers[0].store(self.videos[1])

    def test_is_there_place_for(self):
        is_place = self.cache_servers[0].is_there_place_for(self.videos[0])
        self.assertTrue(not is_place)

    def test_total_size_of_videos(self):
        tsize = self.cache_servers[0].total_size_of_videos()
        self.assertEqual(tsize, 30)

    def test_read_data(self):
        (cache_servers, vidoes, end_points) = read_data('me_at_the_zoo')
        self.assertEqual(len(cache_servers), 10)
        self.assertEqual(len(vidoes), 100)
        self.assertEqual(len(end_points), 10)


if __name__ == "__main__":
    unittest.main()
