# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re


def pre_process(content):
    content = ''.join(content.splitlines())
    content = re.sub(pattern="\"", repl="\"\"", string=content)

    if ',' in content:
        content = '"' + content + '"'
    return content


# useful for handling different item types with a single interface
class YTBSpiderPipeline(object):
    f = open('res.csv', 'w+', encoding='utf-8')

    def open_spider(self, spider):
        self.f = open('res.csv', 'w+', encoding='utf-8')
        self.f.write('title,')
        self.f.write('video_id,')
        self.f.write('duration,')
        self.f.write('release_time,')
        self.f.write('view_count,')
        self.f.write('likes,')
        self.f.write('keywords,')
        self.f.write('description\n')

        self.f.flush()

    def process_item(self, item, spider):

        self.f.write(pre_process(str(item['title']))+",")
        self.f.write(str(item['video_id'])+",")
        self.f.write(str(item['duration'])+",")
        self.f.write(str(item['release_time'])+",")
        self.f.write(str(item['view_count'])+",")
        self.f.write(str(item['like_count'])+",")
        #if len(item['keywords']) > 0:
        #    self.f.write('"')
        #    for kw in item['keywords'][:-1]:
        #        self.f.write(pre_process(str(kw))+',')
        #    self.f.write(pre_process(str(item['keywords'][-1])))
        #    self.f.write('"')
        #self.f.write(',')
        if len(item['description']) > 0:
            self.f.write(pre_process(item['description']))
        else:
            self.f.write("\"\"")

        self.f.write('\n')

        self.f.flush()
        print('writing content: ')
        print(item['title'])
        print('\n')
        return item

        # 结束存放数据，在项目最后一步执行
        def close_spider(self, spider):
            # close_spider()函数只在所有数据抓取完毕后执行一次，
            self.f.close()
            print('执行了close_spider方法,项目已经关闭')
