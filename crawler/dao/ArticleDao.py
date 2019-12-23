import util.MySql as MySql
import model.ArticleModel as ArtMod


class ArticleDao:

    def __init__(self, base: MySql.MySql):
        self.__base = base

    def count_article_by_url(self, url):
        search_sql = "select count(*) from Articles where art_url = '%s'" % url
        self.__base.execute_sql(search_sql)
        result = self.__base.get_result_one()
        return result[0]

    def search_article_id_by_url(self, url):
        search_sql = "select art_id from Articles where art_url = '%s'" % url
        self.__base.execute_sql(search_sql)
        result = self.__base.get_result_one()
        if result is None:
            return None
        else:
            return result[0]

    def insert_article(self, art_mod: ArtMod.ArticleModel):
        insert_sql = "insert into Articles(art_title, art_url, art_class, art_image_url, " \
                     "art_content, art_tags, " \
                     "art_customer_id, art_time, art_comment_num, art_legal)" \
                     " values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d)" \
                     % (art_mod.art_title, art_mod.art_url, art_mod.art_class, art_mod.art_image_url,
                        art_mod.art_content, art_mod.art_tags,
                        art_mod.art_customer_id, art_mod.art_time, art_mod.art_comment_num, art_mod.art_legal)
        self.__base.execute_sql(insert_sql)
        self.__base.commit_transactions()

    def update_article_comment_num(self, art_id):
        update_sql = "update Articles set art_comment_num = art_comment_num + 1 where art_id = %d" % art_id
        self.__base.execute_sql(update_sql)
        self.__base.commit_transactions()