import os

import pytest

import manager
import storage


TEST_FILE = "test_passwords.json"
storage.FILE_PATH = TEST_FILE

@pytest.fixture(autouse=True)
def setup_and_teardown():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_master_password():
    assert manager.check_master("password") == True
    assert manager.check_master("rosaria") == False

def test_add_and_get_entry():
    manager.add_entry("gmail.com","rosaria22","ciao22")
    entry = manager.get_entry("gmail.com")
    assert entry["username"] == "rosaria22"
    assert entry["password"] == "ciao22"

def test_update_entry():
    manager.add_entry("site.com", "olduser", "oldpass")
    updated = manager.update_entry("site.com", username="newuser", password="newpass")
    assert updated == True
    entry = manager.get_entry("site.com")
    assert entry["username"] == "newuser"
    assert entry["password"] == "newpass"

    # Aggiornamento parziale
    manager.update_entry("site.com", password="onlypass")
    entry = manager.get_entry("site.com")
    assert entry["username"] == "newuser"
    assert entry["password"] == "onlypass"


def test_delete_entry():
    manager.add_entry("delete.com", "user", "pass")
    deleted = manager.delete_entry("delete.com")
    assert deleted == True
    assert manager.get_entry("delete.com") is None

def test_list_sites():
    manager.add_entry("site.com", "olduser", "oldpass")
    manager.add_entry("facebook.com", "newuser", "newpass")
    manager.add_entry("google.com", "olduser", "oldpass")
    sites = manager.list_sites()
    assert "site.com" in sites
    assert "facebook.com" in sites
    assert "google.com" in sites
    assert len(sites) == 3