import datetime

class Blog_Entry:
    def __init__(self,
                 title,
                 content, 
                 article_date, 
                 formatted_article_date,
                 createdAt) -> None:
        self.__title = title
        self.__content = content
        self.__article_date = article_date
        self.__formatted_article_date = formatted_article_date
        self.__createdAt = createdAt

    def get_title(self) -> str:
        return self.__title
    def get_content(self) -> str:
        return self.__content
    def get_publishdate(self) -> str:
        return self.__article_date
    def get_formatted_publishdate(self) -> str:
        return self.__formatted_article_date
    def get_createdAt(self) -> datetime:
        return self.__createdAt
    
    def db_insert_entry(self) -> dict:
        return {
            "title" : self.__title,
            "content" : self.__content,
            "publish_date" : self.__article_date,
            "formatted_article_date" : self.__formatted_article_date,
            "createdAt" : self.__createdAt
        }
    
    @staticmethod
    def db_map_entry(entry_json):
        return Blog_Entry(
            entry_json.get("title"),
            entry_json.get("content"),
            entry_json.get("publish_date"),
            entry_json.get("formatted_article_date"),
            entry_json.get("createdAt")
        )

    def __str__(self) -> str:
        return self.__content +" "+self.__article_date
    
