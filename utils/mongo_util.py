from model.blog_entry import Blog_Entry

def update_article_list_filtered(app, start_date, end_date):
    filtered_entries = []
    for en in app.db.entries.find({ 'published_date': 
                                        {'$gte': start_date, 
                                         '$lte': end_date}
                                    }):
        filtered_entries.append(Blog_Entry.db_map_entry(en))
    return filtered_entries