import requests

class NotionAPI():
    NOTION_POST_HEADERS = {
        "Authorization": "Bearer {notion_api_key}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    NOTION_GET_ALL_PAGES_DATABASE_URL = "https://api.notion.com/v1/databases/{database_id}/query"
    NOTION_GET_PAGE_CONTENT_URL = "https://api.notion.com/v1/blocks/{page_id}/children"

    def __init__(self, notion_api_key: str):
        self._notion_api_key = notion_api_key
        self.NOTION_POST_HEADERS["Authorization"] = self.NOTION_POST_HEADERS["Authorization"].format(notion_api_key=self._notion_api_key)
    
    def get_all_pages_database(self, database_id: str):
        get_all_pages_database_url = self.NOTION_GET_ALL_PAGES_DATABASE_URL.format(database_id=database_id)
        all_pages = []
        payload = {
        }

        while True:
            response = requests.post(get_all_pages_database_url, headers=self.NOTION_POST_HEADERS, json=payload)
            data = response.json()
            all_pages.extend(data["results"])
        
            # Check if there's more data
            if not data.get("has_more"):
                break

            # Use start_cursor for pagination
            payload["start_cursor"] = data["next_cursor"]

        return all_pages
    
    def get_page_content(self, page_id: str):
        response = requests.get(self.NOTION_GET_PAGE_CONTENT_URL.format(page_id=page_id), headers=self.NOTION_POST_HEADERS)
        data = response.json()

        if "results" in data:
            return data["results"]
        return None

