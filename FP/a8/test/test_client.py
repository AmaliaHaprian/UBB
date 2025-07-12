from unittest import TestCase

from src.domain.client import Client


class TestClient(TestCase):
    def test_client(self):
        client=Client(100, "John Smith")
        self.assertEqual(client.client_id, 100)
        self.assertEqual(client.name, "John Smith")

        self.assertIsInstance(client, Client)

        client.name="Daniel Smith"
        self.assertEqual(client.name, "Daniel Smith")

        self.assertEqual(client.__str__(), "Client with id=100  is Daniel Smith")
        self.assertEqual(client.__repr__(), str(client))