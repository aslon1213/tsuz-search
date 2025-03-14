import unittest
from tsuz_search import (
    PackageName,
    MxikData,
    MxikResponse,
    SearchResponse,
    SearchParams,
    ElasticSearch,
    MxikSearchItem,
)


class TestModels(unittest.TestCase):
    def test_package_name_model(self):
        # Test creating a PackageName instance
        package = PackageName(
            code=123,
            mxikCode="12345",
            nameUz="Test Name Uz",
            packageType="Test Type",
            nameRu="Test Name Ru",
            nameLat="Test Name Lat",
        )

        self.assertEqual(package.code, 123)
        self.assertEqual(package.mxikCode, "12345")
        self.assertEqual(package.nameUz, "Test Name Uz")
        self.assertEqual(package.packageType, "Test Type")
        self.assertEqual(package.nameRu, "Test Name Ru")
        self.assertEqual(package.nameLat, "Test Name Lat")

    def test_mxik_data_model(self):
        # Test creating a MxikData instance
        package = PackageName(
            code=123,
            mxikCode="12345",
            nameUz="Test Name Uz",
            packageType="Test Type",
            nameRu="Test Name Ru",
            nameLat="Test Name Lat",
        )

        mxik_data = MxikData(
            id="test_id",
            mxikCode="12345",
            groupNameUz="Test Group Uz",
            groupNameRu="Test Group Ru",
            classNameUz="Test Class Uz",
            classNameRu="Test Class Ru",
            positionNameUz="Test Position Uz",
            positionNameRu="Test Position Ru",
            subPositionNameUz="Test SubPosition Uz",
            subPositionNameRu="Test SubPosition Ru",
            isActive="1",
            createdAt="2023-01-01",
            updatedAt="2023-01-02",
            status=1,
            packageNames=[package],
        )

        self.assertEqual(mxik_data.id, "test_id")
        self.assertEqual(mxik_data.mxikCode, "12345")
        self.assertEqual(len(mxik_data.packageNames), 1)
        self.assertEqual(mxik_data.packageNames[0].code, 123)

    def test_mxik_response_model(self):
        # Test creating a MxikResponse instance
        package = PackageName(
            code=123,
            mxikCode="12345",
            nameUz="Test Name Uz",
            packageType="Test Type",
            nameRu="Test Name Ru",
            nameLat="Test Name Lat",
        )

        mxik_data = MxikData(
            id="test_id",
            mxikCode="12345",
            groupNameUz="Test Group Uz",
            groupNameRu="Test Group Ru",
            classNameUz="Test Class Uz",
            classNameRu="Test Class Ru",
            positionNameUz="Test Position Uz",
            positionNameRu="Test Position Ru",
            subPositionNameUz="Test SubPosition Uz",
            subPositionNameRu="Test SubPosition Ru",
            isActive="1",
            createdAt="2023-01-01",
            updatedAt="2023-01-02",
            status=1,
            packageNames=[package],
        )

        response = MxikResponse(success=True, code=200, reason="OK", data=mxik_data)

        self.assertTrue(response.success)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.reason, "OK")
        self.assertEqual(response.data.id, "test_id")

    def test_mxik_search_response_model(self):
        # Test creating a MXIKSearchResponse instance
        package = PackageName(
            code=123,
            mxikCode="12345",
            nameUz="Test Name Uz",
            packageType="Test Type",
            nameRu="Test Name Ru",
            nameLat="Test Name Lat",
        )

        mxik_data = MxikSearchItem(
            mxikCode="12345",
            name="Test Name",
            description="Test Description",
            internationalCode="12345",
            label="Test Label",
            fullName="Test Full Name",
            groupCode="12345",
            groupName="Test Group Name",
            className="Test Class Name",
            positionCode="12345",
            positionName="Test Position Name",
            positionNameUz="Test Position Uz",
            positionNameRu="Test Position Ru",
            subPositionNameUz="Test SubPosition Uz",
            subPositionNameRu="Test SubPosition Ru",
            isActive="1",
            createdAt="2023-01-01",
            updatedAt="2023-01-02",
            status=1,
            packageNames=[package],
        )

        search_response = SearchResponse(
            code=200, success=True, reason="OK", data=[mxik_data]
        )

        self.assertEqual(len(search_response.data), 1)
        self.assertEqual(search_response.data[0].mxikCode, "12345")

    def test_search_params_model(self):
        # Test creating a SearchParams instance
        params = SearchParams(params={"key": "value"}, size=30, page=2, lang="ru")

        self.assertEqual(params.params, {"key": "value"})
        self.assertEqual(params.size, 30)
        self.assertEqual(params.page, 2)
        self.assertEqual(params.lang, "ru")

    def test_elastic_search_model(self):
        # Test creating an ElasticSearch instance
        search = ElasticSearch(search="test query", size=50, page=3, lang="en")

        self.assertEqual(search.search, "test query")
        self.assertEqual(search.size, 50)
        self.assertEqual(search.page, 3)
        self.assertEqual(search.lang, "en")


if __name__ == "__main__":
    unittest.main()
