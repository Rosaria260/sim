import storage


def check_master(password):
    data = storage.load_data()
    if data["master_password"] is None:
        data["master_password"] = password
        storage.save_data(data)
        return True
    return data["master_password"] == password

def add_entry(site,username,password):
    data = storage.load_data()
    data["entries"][site] = {"username":username,"password":password}
    storage.save_data(data)

def get_entry(site):
    data = storage.load_data()
    return data["entries"].get(site)

def update_entry(site,username=None,password=None):
    data = storage.load_data()
    if site in data["entries"]:
        if username:
            data["entries"][site]["username"] = username
        if password:
            data["entries"][site]["password"] = password
        storage.save_data(data)
        return True
    return False


def delete_entry(site):
    data = storage.load_data()
    if site in data["entries"]:
        del data["entries"][site]
        storage.save_data(data)
        return True
    return False

def list_sites():
    data = storage.load_data()
    return list(data["entries"].keys())