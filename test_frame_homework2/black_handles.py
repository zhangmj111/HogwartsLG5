import yaml
from appium.webdriver.common.mobileby import MobileBy


def black_handles(fun):
    def run(*args, **kwargs):
        with open ("../black_list.yaml", "r", encoding="utf-8") as f:
            blacklists = yaml.safe_load(f)
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in blacklists:
                eles = args[0].driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run
