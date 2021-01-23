from test_frame_homework2.basepage import BasePage


class SearchPage(BasePage):
    def search(self):
        self.run_steps('../page/search_page.yaml', 'search')
        return True
