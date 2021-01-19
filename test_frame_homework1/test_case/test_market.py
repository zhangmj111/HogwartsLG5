from test_frame_homework1.app import App


class TestMarket:
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        self.app.stop()

    def test_market(self):
        result = self.app.goto_main().goto_market().goto_event().get_event_title()
        assert "自选大事" == result
