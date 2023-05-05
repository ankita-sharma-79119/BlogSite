import datetime

class Blog_Entry:
    def __init__(self,
                 title,
                 author,
                 published_date,
                 formatted_date,
                 image,
                 image_alt,
                 content) -> None:
        self.__title = title
        self.__author = author
        self.__published_date = published_date
        self.__formatted_date = formatted_date
        self.__image = image
        self.__image_alt = image_alt
        self.__content = content
        

    def get_title(self) -> str:
        return self.__title
    def get_author(self) -> str:
        return self.__author
    def get_publisheddate(self) -> str:
        return self.__published_date
    def get_formatteddate(self) -> str:
        return self.__formatted_date
    def get_image(self) -> str:
        return self.__image
    def get_image_alt(self) -> str:
        return self.__image_alt
    def get_content(self) -> str:
        return self.__content
    
    def db_insert_entry(self) -> dict:
        return {
            "title" : self.__title,
            "author" : self.__author,
            "published_date" : self.__published_date,
            "content" : self.__content,
            "image_link" : self.__image,
            "image_alt" : self.__image_alt
        }
    
    @staticmethod
    def db_map_entry(entry_json):
        pub_date = datetime.datetime.strptime(entry_json.get("published_date"), "%Y-%m-%d").date()
        formatted_date = pub_date.strftime("%b %d")

        return Blog_Entry(
            entry_json.get("title"),
            entry_json.get("author"),
            entry_json.get("published_date"),
            formatted_date,
            entry_json.get("image_link"),
            entry_json.get("image_alt"),
            entry_json.get("content")
        )

    def __str__(self) -> str:
        return self.__title +" "+self.__author
    
