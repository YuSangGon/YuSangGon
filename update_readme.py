import feedparser

sanggon_blog_rss_url = "https://codingralro.tistory.com/rss"
rss_feed = feedparser.parse(sanggon_blog_rss_url)

latest_blog_post_list = ""

MAX_POST_NUM = 5

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"<a href='{feed['link']}'>{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}</a><br>\n"
    
markdown_text = """
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=d9ead3&height=300&section=header&text=YuSangGon's%20Profile&desc=Hopefully%20Desire%20Back-End%20Developer&fontSize=40&descSize=15&fontAlignY=40" />
<br>
<h3> 💻 I’m currently learning ... </h3> 
<p> Framework : <img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-sqare&logo=spring&logoColor=white"></p>
<p> ORM : <img src="https://img.shields.io/badge/Spring_Data_Jpa-6DB33F?style=flat-sqare&logo=spring&logoColor=white"></p>
<p> Security : <img src="https://img.shields.io/badge/Spring_Security-6DB33F?style=flat-sqare&logo=Spring-Security&logoColor=white"></p>
<p> Language : <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-sqare&logo=openjdk&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-sqare&logo=JavaScript&logoColor=white"> <img src="https://img.shields.io/badge/jQuery-0769AD?style=flat-sqare&logo=jquery&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-sqare&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-sqare&logo=html5&logoColor=white"></p>
<p> Database : <img src="https://img.shields.io/badge/MySQL-005C84?style=flat-sqare&logo=mysql&logoColor=white"></p>
<p> VCS : <img src="https://img.shields.io/badge/GIT-E44C30?style=flat-sqare&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/GitHub-100000?style=flat-sqare&logo=github&logoColor=white"></p>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YuSangGon&theme=blue-gree">
<br>
<h3> 📝 Projects I've done ... </h3>
<a href="https://github.com/YuSangGon/portfolio">Show YuSangGon's portfolio</a>
<br>
<h3> 📓 My Blog </h3>
<a href="https://codingralro.tistory.com">코딩하는 랄로</a>
<br>
<h4>⭐ Latest Blog Post ⭐</h4>
"""

end_text = """
<br>
<h3> 📫 How to contact me ... </h3>
<p>📧 : yusang5159@gmail.com</p>
<p>📱 : +82) 010-5159-9859</p>
</div>
"""

readme_text = f"{markdown_text}{latest_blog_post_list}{end_text}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
