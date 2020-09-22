class Config:
    def __init__(self, env):

        self.base_url = {
            'dev': "https://myDEV-env.com",
            'qa': "https://myQA-env.com"
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 9090
        }[env]
