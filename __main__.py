import os
import csv
from scrapy import cmdline
from word_counter import count
import stylecloud

os.chdir(os.path.dirname(os.path.abspath(__file__)))
total_comment_aoi = os.path.exists(os.path.abspath(".\\comments\\total_comments.csv"))

if not total_comment_aoi:
    cmdline.execute('scrapy crawl ytb -o ytb.csv'.split())
else:
    comments = []
    file = os.path.abspath(".\\comments\\total_comments.csv")
    with open(file, 'r', encoding="utf-8") as f:
        raw_comments = csv.reader(f)
        for row in raw_comments:
            comments.append(row[3])
    f.close()
    words = count(comments)

    outfile = os.path.abspath(".\\words_count.csv")
    with open(outfile, 'w+', encoding="utf-8") as out:
        for key in list(words.keys()):
            out.write(str(key)+','+str(words[key])+'\n')
            out.flush()
    out.close()

    stylecloud.gen_stylecloud(
        file_path=outfile,
        output_name="wordcloud.png",
        icon_name="fas fasbiking",
        size=2160
    )

