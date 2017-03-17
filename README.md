# History-of-HearthStone
하스스톤은 Blizzard의 월드 오브 워크래프트 세계관을 기반으로 만들어진 TCG 게임입니다.

이 문서는 하스스톤의 패치 역사와 담겨있는 스토리를 다룹니다.

# Crawler
크롤러는 [하스스톤 소식](http://kr.battle.net/hearthstone/ko/blog)을 모두 크롤링 해 옵니다.

### requirements
- json
- os.listdir
- urllib.request.urlopen
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)

### execute
```
$ python crawler.py
```

# parser
파서는 [크롤러](#crawler)가 크롤링한 데이터를 통해 이벤트를 파싱합니다.

### requirements
- json
- re
- os.path.isfile
- os. remove, listdir

### execute
```
$ python parser.py
```

## news

## expansion
