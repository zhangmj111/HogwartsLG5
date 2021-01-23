from test_frame_homework2.app import App


class TestMarket:
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        self.app.stop()

    def test_market(self):
        result = self.app.goto_main().goto_market().goto_search().search()
        print(result)
        assert True == result
