class CustomerModel:
    def __init__(self):
        self.cus_id = None
        self.cus_name = None
        self.cus_pass = None
        self.cus_url = None
        self.cus_avatar_url = None
        self.cus_style = None

        self.cus_background_url = ''
        self.cus_legal = 1

    def set(self, cus_id, cus_name, cus_pass, cus_url, cus_avatar_url, cus_style):
        self.cus_id = cus_id
        self.cus_name = cus_name
        self.cus_pass = cus_pass
        self.cus_url = cus_url
        self.cus_avatar_url = cus_avatar_url
        self.cus_style = cus_style

        self.cus_background_url = ''
        self.cus_legal = 1
