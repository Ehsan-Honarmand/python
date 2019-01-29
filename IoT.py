# internet object thing ---> IoT

class Devise:
    count = 0
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac_address = mac
        self.name = name
        Devise.count += 1
        # result = ping Devise
        if result:
            self.status = 'active'
        else:
            self.status = 'unknown'
        def get_status(self):
            # return result based on ping result for self.ip

class TV(Devise):
    def turn_on(self):
        # connect to self.ip and Turn on
        pass
    def turn_off(self):
        # connect to self.ip and Turn off
        pass

class Thermo(Devise):
    def get_degree(self):
        # connect to self.ip and read degree and return result
        return result

class SmartTv(TV):
    def turn_on(self):
        # turn on smart TV from self.ip 