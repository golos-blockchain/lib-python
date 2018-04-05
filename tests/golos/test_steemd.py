import unittest

from golos.steemd import Steemd


class SteemdTestCase(unittest.TestCase):
    def setUp(self):
        self.nodes = ['wss://golosd.steepshot.org']
        self.steemd = Steemd(nodes=self.nodes)

    def test_get_posts(self):
        limit = 10
        sort = 'hot'
        posts = self.steemd.get_posts(limit=limit, sort=sort)

        self.assertEqual(len(posts), limit)

        posts_next = self.steemd.get_posts(limit=limit, sort=sort, start=posts[-1].identifier)

        self.assertEqual(len(posts_next), limit)
        self.assertEqual(posts[-1].identifier, posts_next[0].identifier)

    def test_stream_comments(self):
        comments = self.steemd.stream_comments(start_block=15311400, end_block=15311463)
        self.assertGreaterEqual(len(list(comments)), 0)

    def test_get_block(self):
        blocks = self.steemd.get_blocks()
