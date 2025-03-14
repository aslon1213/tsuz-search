import unittest
from unittest.mock import patch, MagicMock
from tsuz_search import Client, ElasticSearch, SearchParams


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {"data": []}

    @patch("tsuz_search.client.requests.get")
    def test_get_by_mxik_code(self, mock_get):
        # Setup
        mock_get.return_value = self.mock_response
        self.mock_response.json.return_value = {
            "success": True,
            "code": 200,
            "reason": "OK",
            "data": {
                "id": "test_id",
                "mxikCode": "10406001002000000",
                "groupNameUz": "Test Group",
                "groupNameRu": "Test Group Ru",
                "classNameUz": "Test Class",
                "classNameRu": "Test Class Ru",
                "positionNameUz": "Test Position",
                "positionNameRu": "Test Position Ru",
                "subPositionNameUz": "Test SubPosition",
                "subPositionNameRu": "Test SubPosition Ru",
                "isActive": "1",
                "createdAt": "2023-01-01",
                "updatedAt": "2023-01-02",
                "status": 1,
                "packageNames": [],
            },
        }

        # Execute
        result = self.client.get_by_mxik_code("10406001002000000")

        # Assert
        mock_get.assert_called_once_with(
            "https://tasnif.soliq.uz/api/cls-api/integration-mxik/get/history/10406001002000000",
        )
        self.assertTrue(result.success)
        self.assertEqual(result.code, 200)
        self.assertEqual(result.data.mxikCode, "10406001002000000")

    @patch("tsuz_search.client.requests.get")
    def test_search(self, mock_get):
        # Setup
        mock_get.return_value = self.mock_response
        search_params = ElasticSearch(search="test_search")

        # Execute
        result = self.client.search(search_params)

        # Assert
        mock_get.assert_called_once_with(
            "https://tasnif.soliq.uz/api/cls-api/elasticsearch/search",
            params=search_params.model_dump(),
        )
        self.assertEqual(result.data, [])

    @patch("tsuz_search.client.requests.get")
    def test_search_by_params(self, mock_get):
        # Setup
        mock_get.return_value = self.mock_response
        search_params = SearchParams(params={"key": "value"})

        # Execute
        result = self.client.search_by_params(search_params)

        # Assert
        expected_params = {"key": "value", "size": 20, "page": 0, "lang": "uz"}
        mock_get.assert_called_once_with(
            "https://tasnif.soliq.uz/api/cls-api/mxik/search/by-params",
            params=expected_params,
        )
        self.assertEqual(result.data, [])

    @patch("tsuz_search.client.requests.get")
    def test_search_dv_cert(self, mock_get):
        # Setup
        mock_get.return_value = self.mock_response
        search_params = SearchParams(params={"cert_number": "12345"})

        # Execute
        result = self.client.search_dv_cert(search_params)

        # Assert
        mock_get.assert_called_once_with(
            "https://tasnif.soliq.uz/api/cls-api/mxik/search/dv-cert-number",
            params=search_params.model_dump(),
        )
        self.assertEqual(result.data, [])

    def test_custom_base_url(self):
        # Setup
        custom_client = Client(base_url="https://custom-url.com/api")

        # Assert
        self.assertEqual(custom_client.base_url, "https://custom-url.com/api")


if __name__ == "__main__":
    unittest.main()
