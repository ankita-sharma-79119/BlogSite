import datetime

class Blog_Entry:
    def __init__(self,
                 title,
                 content, 
                 article_date, 
                 formatted_article_date) -> None:
        self.__title = title
        self.__content = content
        self.__article_date = article_date
        self.__formatted_article_date = formatted_article_date

    def get_title(self) -> str:
        return self.__title
    def get_content(self) -> str:
        return self.__content
    def get_publishdate(self) -> datetime:
        return self.__article_date
    def get_formatted_publishdate(self) -> datetime:
        return self.__formatted_article_date
    
    def db_insert_entry(self) -> dict:
        return {
            "title" : self.__title,
            "content" : self.__content,
            "publish_date" : self.__article_date,
            "formatted_article_date" : self.__formatted_article_date 
        }
    
    @staticmethod
    def db_map_entry(entry_json):
        return Blog_Entry(
            entry_json.get("title"),
            entry_json.get("content"),
            entry_json.get("publish_date"),
            entry_json.get("formatted_article_date")
        )

    def __str__(self) -> str:
        return self.__content +" "+self.__article_date
    
