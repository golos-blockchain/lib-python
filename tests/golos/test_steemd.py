import unittest

from golos.steemd import Steemd


class SteemdTestCase(unittest.TestCase):
    def setUp(self):
        self.nodes = ['wss://golosd.steepshot.org']
        self.steemd = Steemd(nodes=self.nodes)
        self.trx = {
            "ref_block_num": 45193,
            "ref_block_prefix": 3694823045,
            "expiration": "2017-10-20T08:11:47",
            "operations": [
                [
                    "custom_json",
                    {
                        "required_auths": [],
                        "required_posting_auths": ["joseph.kalu"],
                        "id": "follow",
                        "json": "[\"follow\", {\"follower\": \"joseph.kalu\", \"following\": \"steepshot\", \"what\": [\"blog\"]}]"
                    }
                ]
            ],
            "extensions": [

            ],
            "signatures": [
                "1f610ca0afcfa7de5074ebcf9c46e7377836ed780f6181faf67151c7e92778ba29430b73be2cc0ad2dffdd2a6a503ea52ada13d7571bf8c0bf79fcd29830284c65"
            ]
        }

    def get_discusison_by(self, sort):
        limit = 5
        posts = self.steemd.get_posts(limit=limit, sort=sort)

        self.assertEqual(len(posts), limit)

        posts_next = self.steemd.get_posts(limit=limit, sort=sort, start=posts[-1].identifier)

        self.assertEqual(len(posts_next), limit)
        self.assertEqual(posts[-1].identifier, posts_next[0].identifier)

    def test_stream_comments(self):
        comments = self.steemd.stream_comments(start_block=15311400, end_block=15311463)
        self.assertGreaterEqual(len(list(comments)), 1)

    def test_get_blocks(self):
        block_nums = [15311400, 15311439, 15311463]
        blocks = self.steemd.get_blocks(block_nums)

        for i, block in enumerate(blocks):
            self.assertEqual(block['block_num'], block_nums[i])

    def test_get_trending_tags(self):
        after_tag = ''
        limit = 10
        tags = self.steemd.get_trending_tags(after_tag, limit)

        self.assertEqual(len(tags), limit)

        tags_next = self.steemd.get_trending_tags(tags[-1]['name'], limit)
        self.assertEqual(len(tags_next), limit)
        self.assertEqual(tags[-1]['name'], tags_next[0]['name'])

    def test_get_tags_used_by_author(self):
        tags = self.steemd.get_tags_used_by_author('istfak')
        self.assertGreaterEqual(len(tags), 1)

    def test_get_discussions_by_trending(self):
        self.get_discusison_by('trending')

    def test_get_discussions_by_created(self):
        self.get_discusison_by('created')

    def test_get_discussions_by_active(self):
        self.get_discusison_by('active')

    def test_get_discussions_by_payout(self):
        self.get_discusison_by('payout')

    def test_get_discussions_by_hot(self):
        self.get_discusison_by('hot')

    def test_get_block_header(self):
        block_header = self.steemd.get_block_header(15311463)
        self.assertIsNotNone(block_header)

    def test_get_block(self):
        block = self.steemd.get_block(15311463)
        self.assertIsNotNone(block)

    def test_get_ops_in_block(self):
        ops = self.steemd.get_ops_in_block(15311463, False)
        self.assertEqual(len(ops), 7)

    def test_get_config(self):
        cfg = self.steemd.get_config()
        self.assertIsNotNone(cfg)

    def test_get_dynamic_global_properties(self):
        props = self.steemd.get_dynamic_global_properties()
        self.assertIsNotNone(props)
        self.assertTrue('last_irreversible_block_num' in props)
        self.assertTrue('head_block_number' in props)

    def test_get_chain_properties(self):
        props = self.steemd.get_chain_properties()
        self.assertIsNotNone(props)

    def test_get_feed_history(self):
        history = self.steemd.get_feed_history()
        self.assertIsNotNone(history)

    def test_get_current_median_history_price(self):
        history = self.steemd.get_current_median_history_price()
        self.assertIsNotNone(history)

    def test_get_witness_schedule(self):
        schedule = self.steemd.get_witness_schedule()
        self.assertIsNotNone(schedule)

    def test_get_hardfork_version(self):
        version = self.steemd.get_hardfork_version()
        self.assertRegex(version, r'\d+\.\d+\.\d+')

    def test_get_next_scheduled_hardfork(self):
        version = self.steemd.get_next_scheduled_hardfork()
        self.assertRegex(version['hf_version'], r'\d+\.\d+\.\d+')

    def test_get_accounts(self):
        accounts = self.steemd.get_accounts(['steepshot'])
        self.assertEqual(len(accounts), 1)

    def test_lookup_account_names(self):
        accounts = self.steemd.lookup_account_names(['steepshot'])
        self.assertEqual(len(accounts), 1)

    def test_lookup_accounts(self):
        limit = 10
        accounts = self.steemd.lookup_accounts('steepshot', limit)
        self.assertEqual(len(accounts), limit)

    def test_get_account_count(self):
        self.assertIsNotNone(self.steemd.get_account_count())

    def test_get_account_history(self):
        limit = 10
        history = self.steemd.get_account_history('steepshot', 1000, limit)
        self.assertEqual(len(history), limit + 1)

    def test_get_order_book(self):
        limit = 10
        res = self.steemd.get_order_book(limit)
        self.assertEqual(len(res['asks']), limit)
        self.assertEqual(len(res['bids']), limit)

    def test_get_transaction_hex(self):
        hex_trx = self.steemd.get_transaction_hex(self.trx)
        self.assertIsNotNone(hex_trx)

    def test_get_transaction(self):
        trx_id = '5461e87076e385e6f0da6b09a886022bb4538bc0'
        trx = self.steemd.get_transaction(trx_id)
        self.assertIsNotNone(trx)

    def test_get_potential_signatures(self):
        signature = self.steemd.get_potential_signatures(self.trx)
        self.assertIsNotNone(signature)

    def test_verify_authority(self):
        authority = self.steemd.verify_authority(self.trx)
        self.assertTrue(authority)

    def test_get_active_votes(self):
        votes = self.steemd.get_active_votes('optimist', 'spasibo-golos')
        self.assertGreater(len(votes), 0)

    def test_get_account_votes(self):
        votes = self.steemd.get_account_votes('optimist')
        self.assertGreater(len(votes), 0)

    def test_get_content(self):
        content = self.steemd.get_content('optimist', 'spasibo-golos')
        self.assertEqual(content['author'], 'optimist')

    def test_get_content_replies(self):
        replies = self.steemd.get_content_replies('optimist', 'spasibo-golos')
        self.assertGreater(len(replies), 0)

    def test_get_all_content_replies(self):
        # replies = self.steemd.get_all_content_replies('optimist', 'spasibo-golos')
        replies = self.steemd.get_all_content_replies('joseph.kalu', 'test-2018-03-22-08-26-15')
        self.assertGreater(len(replies), 0)

    def test_get_trending_categories(self):
        limit = 10
        replies = self.steemd.get_trending_categories('', limit)
        self.assertEqual(len(replies), limit)

    def test_get_languages(self):
        languages = self.steemd.get_languages()
        self.assertGreater(len(languages), 0)

    def test_get_replies_by_last_update(self):
        limit = 10
        replies = self.steemd.get_replies_by_last_update('steepshot', '', limit)
        self.assertEqual(len(replies), limit)

    def test_get_witnesses(self):
        witnesses = self.steemd.get_witnesses([1672])
        self.assertEqual(witnesses[0]['owner'], 'steepshot')

    def test_get_witness_by_account(self):
        witness = self.steemd.get_witness_by_account('steepshot')
        self.assertEqual(witness['owner'], 'steepshot')

    def test_get_witnesses_by_vote(self):
        limit = 10
        witnesses = self.steemd.get_witnesses_by_vote('', limit)
        self.assertEqual(len(witnesses), limit)

    def test_lookup_witness_accounts(self):
        limit = 10
        witnesses = self.steemd.get_witnesses_by_vote('', limit)
        self.assertEqual(len(witnesses), limit)

    def test_get_witness_count(self):
        witnesses = self.steemd.get_witness_count()
        self.assertGreater(witnesses, 0)

    def test_get_active_witnesses(self):
        witnesses = self.steemd.get_active_witnesses()
        self.assertGreater(len(witnesses), 0)

    def test_get_followers(self):
        limit = 10
        followers = self.steemd.get_followers('joseph.kalu', '', 'blog', limit)
        self.assertEqual(len(followers), limit)

    def test_get_following(self):
        limit = 10
        following = self.steemd.get_following('joseph.kalu', '', 'blog', limit)
        self.assertEqual(len(following), limit)

    def test_get_follow_count(self):
        follow = self.steemd.get_follow_count('joseph.kalu')
        self.assertGreater(follow['follower_count'], 0)

    def test_get_account_reputations(self):
        limit = 10
        accounts = self.steemd.get_account_reputations('steepshot', limit)
        self.assertEqual(len(accounts), limit)

    def test_get_reblogged_by(self):
        reblogged_by = self.steemd.get_reblogged_by(
            'vp-liganovi4kov',
            'novaya-rubrika-obratnaya-svyaz-otvety-komandy-golos-io-na-voprosy-novichkov'
        )
        self.assertGreater(len(reblogged_by), 0)

    def test_get_ticker(self):
        ticker = self.steemd.get_ticker()
        self.assertIsNotNone(ticker)

    def test_get_volume(self):
        volume = self.steemd.get_volume()
        self.assertIsNotNone(volume)

