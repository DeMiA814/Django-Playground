class Router(object):
    def db_for_read(self, model, **hints):
        #ここでランダムに選択すると、dbの負荷分散っぽいことが出来る
        #例：return random.choice['default','users']
        if model._meta.app_label == "akademia_sns":
            return "another"
        return "default"
    def db_for_write(self, model, **hints):
        if model._meta.app_label == "akademia_sns":
            return "another"
        return "default"
    def allow_relation(self, obj1, obj2, **hints):
        #Trueはリレーションを認める、Falseは認めない、Noneはこのコードでは関知しないという意味
        return None
    def allow_migrate(self, db, model):
        #userアプリの場合はusers設定のデータベースへmigrate。
        #他のアプリはusers以外のデータベースへmigrateする設定
        if model._meta.app_label == "akademia_sns"
            return db == "another":
        else:
            return True
        return False
