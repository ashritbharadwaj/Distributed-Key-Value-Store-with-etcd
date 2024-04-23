

import unittest
import etcd3

from etcd import *

class TestEtcdClient(unittest.TestCase):
    def setUp(self):
        self.etcd_client = etcd3.client(host='localhost',port=1111)

    def test_get_all(self):
        insert_etcd_key_value(self.etcd_client,'key1', 'value1')
        insert_etcd_key_value(self.etcd_client,'key2', 'value2')
        result = get_all_etcd_keys(self.etcd_client)
        self.assertEqual(result, ['key1', 'key2'])

    def test_get_one(self):
        result = get_etcd_key_value(self.etcd_client,'key1')
        self.assertEqual(result, 'value1')

    def test_get_none(self):
        result = get_etcd_key_value(self.etcd_client,'nonexistent_key')
        self.assertIsNone(result)

    def test_put_one(self):
        result = insert_etcd_key_value(self.etcd_client,'key', 'value')
        self.assertTrue(result)

    def test_delete_one(self):
        insert_etcd_key_value(self.etcd_client,'key', 'value')
        result = delete_etcd_key(self.etcd_client,'key')
        self.assertTrue(result)

    def test_delete_none(self):
        result = delete_etcd_key(self.etcd_client,'nonexistent_key')
        self.assertFalse(result)

    def test_get_after_delete(self):
        insert_etcd_key_value(self.etcd_client,'key', 'value')
        delete_etcd_key(self.etcd_client,'key')
        result = get_etcd_key_value(self.etcd_client,'key')
        self.assertIsNone(result)

    def test_insert_none(self):
        result = insert_etcd_key_value(self.etcd_client,'key', None)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

