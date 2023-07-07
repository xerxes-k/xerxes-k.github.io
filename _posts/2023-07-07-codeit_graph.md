---
layout: single
title:  "graph "
---

**Table of contents**<a id='toc0_'></a>    
- [graph](#toc1_)    
  - [그래프 특징](#toc1_1_)    
    - [인접 행렬](#toc1_1_1_)    
    - [인접 리스트](#toc1_1_2_)    
  - [그래프 탐색 = 순회](#toc1_2_)    
    - [대표적인 두 알고리즘](#toc1_2_1_)    
      - [BFS 너비 우선 탐색](#toc1_2_1_1_)    
      - [DFS](#toc1_2_1_2_)    
      - [bfs backtracking](#toc1_2_1_3_)    
      - [dijkstra 알고리즘의 세 요소](#toc1_2_1_4_)    
  - [수료증](#toc1_3_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[graph](#toc0_)
---

![](https://bakey-api.codeit.kr/files/2455/HUdiCM?name=1.png)

## <a id='toc1_1_'></a>[그래프 특징](#toc0_)
---
그래프는 연결 관계를 표현하기 위해 사용한다  
마치 지하철 노선도처럼

그래프는 노드를 이용해 관계에 대한 reference를 저장할 수 있다  
그 reference를 edge라고 부르고 a, b 노드 간의 edge를 (a,b)라고 부른다  
서로 에지가 있는 노드는 "서로 인접해 있다"고 표현한다  
서로 인접하지 않은 노드가 매개를 통해 연결되면 이어지는 방법을 경로라고 부른다  
경로로 이어질 때까지 소요되는 에지의 개수를 거리라고 부른다

특정 노드에서 다시 자기 자신으로 돌아오는 경로를 사이클이라 부른다  
경로 중 최단 거리를 최단 경로라 부른다

한 노드가 갖고 있는 에지의 개수를 차수라고 부른다

친구 관계처럼 에지가 쌍방향이면 무방향 undirected graph라 부른다  
인스타 팔로우 처럼 에지가 일방향이면 directed graph라 부른다

방향이 있는 그래프에서는 차수를 출력 차수, 입력 차수로 구분한다

가중치 그래프는 에지에 값이 부여된 그래프다  
가중치 그래프의 거리는 에지들의 가중치 합이다


```python
class StationNode:
    """metro station"""
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits
```

모든 노드를 배열, 리스트에 저장하면 인덱스(고유값)으로 불러올 수 있다  
해시 테이블로 저장하면 키key를 통해 가져올 수 있다


```python
class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name
        


def create_station_nodes(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file, 'r', encoding='utf-8') as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 여기에 코드를 작성하세요
                stations[station_name] = StationNode(station_name)

    return stations



stations = create_station_nodes("./stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다

# 테스트 코드
# stations에 저장한 역들 이름 출력 (채점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
    print(stations[station].station_name)
```

    가능
    가락시장
    가산디지털단지
    가양
    가좌
    가평
    간석
    간석오거리
    갈매
    갈산
    강남
    강남구청
    강동
    강동구청
    강변
    강촌
    개롱
    개봉
    개포동
    개화
    개화산
    거여
    건대입구
    검암
    경마공원
    경복궁
    경원대
    경인교대입구
    경찰병원
    계산
    계양
    고덕
    고려대
    고속터미널
    고잔
    곡산
    공단
    공덕
    공릉
    공항시장
    공항화물청사
    과천
    관악
    광나루
    광명
    광명사거리
    광화문
    광흥창
    교대
    구로
    구로디지털단지
    구룡
    구리
    구반포
    구산
    구성
    구의
    구일
    구파발
    국수
    국제업무지구
    국회의사당
    군자
    군포
    굴봉산
    굴포천
    굽은다리
    귤현
    금곡
    금릉
    금정
    금천구청
    금촌
    금호
    기흥
    길동
    길음
    김유정
    김포공항
    까치산
    까치울
    낙성대
    남구로
    남동인더스파크
    남부터미널
    남성
    남영
    남춘천
    남태령
    남한산성입구
    내방
    노들
    노량진
    노원
    녹번
    녹사평
    녹양
    녹천
    논현
    능곡
    단대오거리
    답십리
    당고개
    당산
    당정
    대곡
    대공원
    대림
    대모산입구
    대방
    대성리
    대야미
    대청
    대치
    대화
    대흥
    덕계
    덕소
    덕정
    도곡
    도농
    도림천
    도봉
    도봉산
    도심
    도원
    도화
    독립문
    독바위
    독산
    돌곶이
    동대문
    동대문역사문화공원
    동대입구
    동두천
    동두천중앙
    동막
    동묘앞
    동수
    동암
    동인천
    동작
    동춘
    두정
    둔촌동
    등촌
    디지털미디어시티
    뚝섬
    뚝섬유원지
    마곡
    마두
    마들
    마석
    마장
    마천
    마포
    마포구청
    망우
    망원
    망월사
    망포
    매봉
    먹골
    면목
    명동
    명일
    명학
    모란
    목동
    몽촌토성
    무악재
    문래
    문산
    문정
    문학경기장
    미금
    미아
    미아삼거리
    박촌
    반월
    반포
    발산
    방배
    방이
    방학
    방화
    배방
    백마
    백석
    백양리
    백운
    버티고개
    범계
    별내역
    병점
    보라매
    보문
    보산
    보정
    복정
    봉명
    봉은사
    봉천
    봉화산
    부개
    부천
    부천시청
    부천종합운동장
    부평
    부평구청
    부평삼거리
    부평시장
    불광
    사가정
    사당
    사릉
    사평
    산본
    산성
    삼각지
    삼산체육관
    삼성
    삼성중앙
    삼송
    상갈
    상계
    상도
    상동
    상록수
    상봉
    상수
    상왕십리
    상월곡
    상일동
    상천
    새절
    샛강
    서강
    서대문
    서동탄
    서빙고
    서울대입구
    서울숲
    서울역
    서정리
    서초
    서현
    석계
    석수
    석촌
    선릉
    선바위
    선유도
    선정릉
    선학
    성균관대
    성북
    성수
    성신여대입구
    성환
    세류
    세마
    센트럴파크
    소래포구
    소사
    송내
    송도
    송정
    송탄
    송파
    수내
    수락산
    수리산
    수색
    수서
    수원
    수유
    수진
    숙대입구
    숭실대입구
    시청
    신갈
    신금호
    신길
    신길온천
    신논현
    신답
    신당
    신대방
    신대방삼거리
    신도림
    신림
    신목동
    신반포
    신방화
    신사
    신설동
    신연수
    신용산
    신원
    신이문
    신정
    신정네거리
    신중동
    신창
    신천
    신촌
    신촌 (경의중앙선)
    신풍
    신흥
    쌍문
    쌍용
    아산
    아신
    아차산
    아현
    안국
    안산
    안암
    안양
    암사
    압구정
    압구정로데오
    애오개
    야탑
    약수
    양수
    양원
    양재
    양재시민의숲
    양정
    양주
    양천구청
    양천향교
    양평
    어린이대공원
    언주
    여의나루
    여의도
    역곡
    역삼
    역촌
    연수
    연신내
    염창
    영등포
    영등포구청
    영등포시장
    영통
    예술회관
    오금
    오류동
    오리
    오목교
    오빈
    오산
    오산대
    오이도
    옥수
    온수
    온양온천
    올림픽공원
    왕십리
    외대앞
    용답
    용두
    용마산
    용문
    용산
    우장산
    운길산
    운서
    운정
    원당
    원덕
    원인재
    월계
    월곡
    월곶
    월드컵경기장
    월롱
    을지로3가
    을지로4가
    을지로입구
    응봉
    응암
    의왕
    의정부
    이대
    이매
    이수
    이촌
    이태원
    인덕원
    인천
    인천국제공항
    인천논현
    인천대입구
    인천시청
    인천터미널
    일산
    일원
    임학
    작전
    잠실
    잠실나루
    잠원
    장승배기
    장암
    장지
    장한평
    정발산
    정부과천청사
    정왕
    정자
    제기동
    제물포
    종각
    종로3가
    종로5가
    종합운동장
    주안
    주엽
    죽전
    중계
    중곡
    중동
    중랑
    중앙
    중화
    증미
    증산
    지식정보단지
    지제
    지축
    지행
    직산
    진위
    창동
    창신
    천안
    천왕
    천호
    철산
    청계산입구
    청구
    청담
    청량리
    청명
    청평
    춘의
    춘천
    충무로
    충정로
    캠퍼스타운
    탄현
    태릉입구
    태평
    테크노파크
    퇴계원
    파주
    판교
    팔당
    평내호평
    평촌
    평택
    풍산
    하계
    학동
    학여울
    한강진
    한남
    한대앞
    한성대입구
    한양대
    한티
    합정
    행당
    행신
    혜화
    호구포
    홍대입구
    홍제
    화곡
    화랑대
    화서
    화전
    화정
    회기
    회룡
    회현
    효창공원앞
    흑석
    ﻿소요산
    

### <a id='toc1_1_1_'></a>[인접 행렬](#toc0_)
---
- 각 노드를 리스트에 저장해 고유 정수 인덱스를 준다
- 노드 수 x 노드 수 크기의 행렬을 만든다
- 노드들 엣지 유무 및 가중치에 따라 행렬 요소를 채운다
- 방향성이 없으면 대칭으로 표현된다
- 가중치는 행렬 상에 표시한다
- 가운데는 자기 자신과의 관계이므로 빈다

![](https://bakey-api.codeit.kr/files/2414/kDvdKN?name=2.png)


```python
# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

# 여기에 코드를 작성하세요

adjacency_matrix[0][1] = 1
adjacency_matrix[0][2] = 1

adjacency_matrix[1][0] = 1
adjacency_matrix[1][3] = 1
adjacency_matrix[1][5] = 1

adjacency_matrix[2][0] = 1
adjacency_matrix[2][5] = 1

adjacency_matrix[3][1] = 1
adjacency_matrix[3][4] = 1
adjacency_matrix[3][5] = 1

adjacency_matrix[4][3] = 1
adjacency_matrix[4][5] = 1

adjacency_matrix[5][1] = 1
adjacency_matrix[5][2] = 1
adjacency_matrix[5][3] = 1
adjacency_matrix[5][4] = 1

print(adjacency_matrix)
```

    [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0]]
    

### <a id='toc1_1_2_'></a>[인접 리스트](#toc0_)
---
- 노드 별로 인접 노드의 리스트를 속성으로 갖는다
  - 방향 그래프는 출력 노드에만 등록한다
  - 가중치는 튜플을 이용해 노드명과 같이 저장한다

![](https://bakey-api.codeit.kr/files/2414/FOYmEY?name=3.png)


```python
class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []  # 인접 리스트


    def add_connection(self, other_station):
        """지하철 역 노드 사이 엣지 저장하기"""
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)


    def __str__(self):
        """지하철 노드 문자열 메소드. 지하철 역 이름과 연결된 역들을 모두 출력해준다"""
        res_str = f"{self.station_name}: "  # 리턴할 문자열

        # 리턴할 문자열에 인접한 역 이름들 저장
        for station in self.adjacent_stations:
            res_str += f"{station.station_name} "

        return res_str
```


```python
# 코드를 추가하세요
def create_subway_graph(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프를 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file, 'r', encoding='utf-8') as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            prev = None
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in stations:
                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                    stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 노드 인스턴스를 value로 저장한다
                    
                    # 해당 역에 전, 다음 역을 넣거나
                    # 해당 역 전 역에 해당 역을 넣거나 >>> 해설도 이걸로 가는 듯 근데 힌트를 보고 있는데 이걸 쓰는 방법을 안 알려준다
                else:
                    current_station = stations[station_name]
                if prev is not None:
                    current_station.add_connection(prev)  # 현재 역과 전 역의 엣지를 연결한다
                prev = current_station
                
                    

    return stations


stations = create_subway_graph("./stations.txt")  # stations.txt 파일로 그래프를 만든다

# stations에 저장한 역 인접 역들 출력 (채점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
        print(stations[station])
```

    가능: 녹양 의정부 
    가락시장: 수서 경찰병원 송파 문정 
    가산디지털단지: 광명 독산 남구로 철산 
    가양: 양천향교 증미 
    가좌: 홍대입구 디지털미디어시티 
    가평: 상천 굴봉산 
    간석: 동암 주안 
    간석오거리: 부평삼거리 인천시청 
    갈매: 망우 별내역 
    갈산: 작전 부평구청 
    강남: 역삼 교대 양재 
    강남구청: 청담 학동 압구정로데오 선정릉 
    강동: 천호 길동 
    강동구청: 천호 몽촌토성 
    강변: 구의 잠실나루 
    강촌: 백양리 김유정 
    개롱: 오금 거여 
    개봉: 구일 오류동 
    개포동: 구룡 대모산입구 
    개화: 김포공항 
    개화산: 방화 김포공항 
    거여: 개롱 마천 
    건대입구: 성수 구의 어린이대공원 뚝섬유원지 
    검암: 계양 운서 
    경마공원: 선바위 대공원 
    경복궁: 독립문 안국 
    경원대: 복정 태평 
    경인교대입구: 계산 작전 
    경찰병원: 가락시장 오금 
    계산: 임학 경인교대입구 
    계양: 김포공항 검암 귤현 
    고덕: 명일 상일동 
    고려대: 안암 월곡 
    고속터미널: 잠원 교대 반포 내방 신반포 사평 
    고잔: 중앙 공단 
    곡산: 대곡 백마 
    공단: 고잔 안산 
    공덕: 마포 애오개 대흥 효창공원앞 신촌 (경의중앙선) 서강 서울역 홍대입구 
    공릉: 하계 태릉입구 
    공항시장: 김포공항 신방화 
    공항화물청사: 운서 인천국제공항 
    과천: 대공원 정부과천청사 
    관악: 석수 안양 
    광나루: 아차산 천호 
    광명: 인천 가산디지털단지 
    광명사거리: 철산 천왕 
    광화문: 서대문 종로3가 
    광흥창: 상수 대흥 
    교대: 강남 서초 고속터미널 남부터미널 
    구로: 신도림 구일 
    구로디지털단지: 신대방 대림 
    구룡: 도곡 개포동 
    구리: 도농 양원 
    구반포: 동작 신반포 
    구산: 연신내 응암 
    구성: 보정 신갈 
    구의: 건대입구 강변 
    구일: 구로 개봉 
    구파발: 지축 연신내 
    국수: 아신 신원 
    국제업무지구: 센트럴파크 
    국회의사당: 당산 여의도 
    군자: 장한평 아차산 중곡 어린이대공원 
    군포: 금정 당정 
    굴봉산: 가평 백양리 
    굴포천: 삼산체육관 부평구청 
    굽은다리: 길동 명일 
    귤현: 계양 박촌 
    금곡: 사릉 평내호평 
    금릉: 운정 금촌 
    금정: 명학 군포 범계 산본 
    금천구청: 독산 석수 
    금촌: 금릉 월롱 
    금호: 약수 옥수 
    기흥: 신갈 상갈 
    길동: 강동 굽은다리 
    길음: 미아삼거리 성신여대입구 
    김유정: 강촌 남춘천 
    김포공항: 개화산 송정 개화 공항시장 디지털미디어시티 계양 
    까치산: 신정네거리 화곡 신정 
    까치울: 온수 부천종합운동장 
    낙성대: 사당 서울대입구 
    남구로: 대림 가산디지털단지 
    남동인더스파크: 호구포 원인재 
    남부터미널: 교대 양재 
    남성: 이수 숭실대입구 
    남영: 서울역 용산 
    남춘천: 김유정 춘천 
    남태령: 사당 선바위 
    남한산성입구: 산성 단대오거리 
    내방: 고속터미널 이수 
    노들: 노량진 흑석 
    노량진: 용산 대방 샛강 노들 
    노원: 상계 창동 마들 중계 
    녹번: 불광 홍제 
    녹사평: 삼각지 이태원 
    녹양: 양주 가능 
    녹천: 창동 월계 
    논현: 학동 반포 
    능곡: 행신 대곡 
    단대오거리: 남한산성입구 신흥 
    답십리: 마장 장한평 
    당고개: 상계 
    당산: 영등포구청 합정 선유도 국회의사당 
    당정: 군포 의왕 
    대곡: 백석 화정 능곡 곡산 
    대공원: 경마공원 과천 
    대림: 구로디지털단지 신도림 신풍 남구로 
    대모산입구: 개포동 수서 
    대방: 노량진 신길 
    대성리: 마석 청평 
    대야미: 수리산 반월 
    대청: 학여울 일원 
    대치: 도곡 학여울 
    대화: 주엽 
    대흥: 광흥창 공덕 
    덕계: 덕정 양주 
    덕소: 도심 양정 
    덕정: 지행 덕계 
    도곡: 매봉 대치 한티 구룡 
    도농: 양정 구리 
    도림천: 신도림 양천구청 
    도봉: 도봉산 방학 
    도봉산: 망월사 도봉 장암 수락산 
    도심: 팔당 덕소 
    도원: 제물포 동인천 
    도화: 주안 제물포 
    독립문: 무악재 경복궁 
    독바위: 불광 연신내 
    독산: 가산디지털단지 금천구청 
    돌곶이: 상월곡 석계 
    동대문: 동묘앞 종로5가 혜화 동대문역사문화공원 
    동대문역사문화공원: 을지로4가 신당 동대문 충무로 을지로4가 청구 
    동대입구: 충무로 약수 
    동두천: ﻿소요산 보산 
    동두천중앙: 보산 지행 
    동막: 동춘 캠퍼스타운 
    동묘앞: 신설동 동대문 신당 창신 
    동수: 부평 부평삼거리 
    동암: 백운 간석 
    동인천: 도원 인천 
    동작: 이촌 이수 흑석 구반포 
    동춘: 원인재 동막 
    두정: 직산 천안 
    둔촌동: 상일동 올림픽공원 
    등촌: 증미 염창 
    디지털미디어시티: 증산 월드컵경기장 가좌 수색 홍대입구 김포공항 
    뚝섬: 한양대 성수 
    뚝섬유원지: 건대입구 청담 
    마곡: 송정 발산 
    마두: 정발산 백석 
    마들: 수락산 노원 
    마석: 평내호평 대성리 
    마장: 왕십리 답십리 
    마천: 거여 
    마포: 여의나루 공덕 
    마포구청: 월드컵경기장 망원 
    망우: 양원 상봉 상봉 갈매 
    망원: 마포구청 합정 
    망월사: 회룡 도봉산 
    망포: 영통 
    매봉: 양재 도곡 
    먹골: 태릉입구 중화 
    면목: 상봉 사가정 
    명동: 충무로 회현 
    명일: 굽은다리 고덕 
    명학: 안양 금정 
    모란: 수진 태평 야탑 
    목동: 신정 오목교 
    몽촌토성: 강동구청 잠실 
    무악재: 홍제 독립문 
    문래: 신도림 영등포구청 
    문산: 파주 
    문정: 가락시장 장지 
    문학경기장: 인천터미널 선학 
    미금: 정자 오리 
    미아: 수유 미아삼거리 
    미아삼거리: 미아 길음 
    박촌: 귤현 임학 
    반월: 대야미 상록수 
    반포: 논현 고속터미널 
    발산: 마곡 우장산 
    방배: 서초 사당 
    방이: 올림픽공원 오금 
    방학: 도봉 창동 
    방화: 개화산 
    배방: 아산 온양온천 
    백마: 곡산 풍산 
    백석: 마두 대곡 
    백양리: 굴봉산 강촌 
    백운: 부평 동암 
    버티고개: 한강진 약수 
    범계: 평촌 금정 
    별내역: 갈매 퇴계원 
    병점: 세류 세마 
    보라매: 신대방삼거리 신풍 
    보문: 창신 안암 
    보산: 동두천 동두천중앙 
    보정: 죽전 구성 
    복정: 장지 산성 수서 경원대 
    봉명: 천안 쌍용 
    봉은사: 삼성중앙 종합운동장 
    봉천: 서울대입구 신림 
    봉화산: 화랑대 
    부개: 송내 부평 
    부천: 소사 중동 
    부천시청: 신중동 상동 
    부천종합운동장: 까치울 춘의 
    부평: 부개 백운 부평시장 동수 
    부평구청: 굴포천 갈산 부평시장 
    부평삼거리: 동수 간석오거리 
    부평시장: 부평구청 부평 
    불광: 연신내 녹번 역촌 독바위 
    사가정: 면목 용마산 
    사당: 방배 낙성대 이수 남태령 
    사릉: 퇴계원 금곡 
    사평: 고속터미널 신논현 
    산본: 금정 수리산 
    산성: 복정 남한산성입구 
    삼각지: 숙대입구 신용산 효창공원앞 녹사평 
    삼산체육관: 상동 굴포천 
    삼성: 종합운동장 선릉 
    삼성중앙: 선정릉 봉은사 
    삼송: 원당 지축 
    상갈: 기흥 청명 
    상계: 당고개 노원 
    상도: 숭실대입구 장승배기 
    상동: 부천시청 삼산체육관 
    상록수: 반월 한대앞 
    상봉: 중화 면목 망우 중랑 망우 
    상수: 합정 광흥창 
    상왕십리: 신당 왕십리 
    상월곡: 월곡 돌곶이 
    상일동: 고덕 둔촌동 
    상천: 청평 가평 
    새절: 응암 증산 
    샛강: 여의도 노량진 
    서강: 공덕 홍대입구 
    서대문: 충정로 광화문 
    서동탄: 신창 
    서빙고: 한남 이촌 
    서울대입구: 낙성대 봉천 
    서울숲: 왕십리 압구정로데오 
    서울역: 시청 남영 회현 숙대입구 용산 신촌 (경의중앙선) 공덕 
    서정리: 송탄 지제 
    서초: 교대 방배 
    서현: 이매 수내 
    석계: 성북 신이문 돌곶이 태릉입구 
    석수: 금천구청 관악 
    석촌: 잠실 송파 
    선릉: 삼성 역삼 선정릉 한티 
    선바위: 남태령 경마공원 
    선유도: 신목동 당산 
    선정릉: 언주 삼성중앙 강남구청 선릉 
    선학: 문학경기장 신연수 
    성균관대: 의왕 화서 
    성북: 월계 석계 
    성수: 뚝섬 건대입구 용답 
    성신여대입구: 길음 한성대입구 
    성환: 평택 직산 
    세류: 수원 병점 
    세마: 병점 오산대 
    센트럴파크: 인천대입구 국제업무지구 
    소래포구: 월곶 인천논현 
    소사: 역곡 부천 
    송내: 중동 부개 
    송도: 연수 
    송정: 김포공항 마곡 
    송탄: 진위 서정리 
    송파: 석촌 가락시장 
    수내: 서현 정자 
    수락산: 도봉산 마들 
    수리산: 산본 대야미 
    수색: 디지털미디어시티 화전 
    수서: 일원 가락시장 대모산입구 복정 
    수원: 화서 세류 
    수유: 쌍문 미아 
    수진: 신흥 모란 
    숙대입구: 서울역 삼각지 
    숭실대입구: 남성 상도 
    시청: 종각 서울역 을지로입구 충정로 
    신갈: 구성 기흥 
    신금호: 청구 행당 
    신길: 대방 영등포 영등포시장 여의도 
    신길온천: 안산 정왕 
    신논현: 사평 언주 
    신답: 용두 용답 
    신당: 동대문역사문화공원 상왕십리 청구 동묘앞 
    신대방: 신림 구로디지털단지 
    신대방삼거리: 장승배기 보라매 
    신도림: 영등포 구로 대림 문래 도림천 
    신림: 봉천 신대방 
    신목동: 염창 선유도 
    신반포: 구반포 고속터미널 
    신방화: 공항시장 양천향교 
    신사: 압구정 잠원 
    신설동: 제기동 동묘앞 용두 
    신연수: 선학 원인재 
    신용산: 삼각지 이촌 
    신원: 국수 양수 
    신이문: 석계 외대앞 
    신정: 까치산 목동 
    신정네거리: 양천구청 까치산 
    신중동: 춘의 부천시청 
    신창: 온양온천 서동탄 
    신천: 잠실 종합운동장 
    신촌: 홍대입구 이대 
    신촌 (경의중앙선): 서울역 공덕 
    신풍: 보라매 대림 
    신흥: 단대오거리 수진 
    쌍문: 창동 수유 
    쌍용: 봉명 아산 
    아산: 쌍용 배방 
    아신: 오빈 국수 
    아차산: 군자 광나루 
    아현: 이대 충정로 
    안국: 경복궁 종로3가 
    안산: 공단 신길온천 
    안암: 보문 고려대 
    안양: 관악 명학 
    암사: 천호 
    압구정: 옥수 신사 
    압구정로데오: 서울숲 강남구청 
    애오개: 공덕 충정로 
    야탑: 모란 이매 
    약수: 동대입구 금호 버티고개 청구 
    양수: 신원 운길산 
    양원: 구리 망우 
    양재: 남부터미널 매봉 강남 양재시민의숲 
    양재시민의숲: 양재 청계산입구 
    양정: 덕소 도농 
    양주: 덕계 녹양 
    양천구청: 도림천 신정네거리 
    양천향교: 신방화 가양 
    양평: 오목교 영등포구청 원덕 오빈 
    어린이대공원: 군자 건대입구 
    언주: 신논현 선정릉 
    여의나루: 여의도 마포 
    여의도: 신길 여의나루 국회의사당 샛강 
    역곡: 온수 소사 
    역삼: 선릉 강남 
    역촌: 응암 불광 
    연수: 원인재 송도 
    연신내: 구파발 불광 독바위 구산 
    염창: 등촌 신목동 
    영등포: 신길 신도림 
    영등포구청: 문래 당산 양평 영등포시장 
    영등포시장: 영등포구청 신길 
    영통: 청명 망포 
    예술회관: 인천시청 인천터미널 
    오금: 경찰병원 방이 개롱 
    오류동: 개봉 온수 
    오리: 미금 죽전 
    오목교: 목동 양평 
    오빈: 양평 아신 
    오산: 오산대 진위 
    오산대: 세마 오산 
    오이도: 정왕 월곶 
    옥수: 금호 압구정 응봉 한남 
    온수: 오류동 역곡 천왕 까치울 
    온양온천: 배방 신창 
    올림픽공원: 둔촌동 방이 
    왕십리: 상왕십리 한양대 행당 마장 서울숲 청량리 응봉 
    외대앞: 신이문 회기 
    용답: 신답 성수 
    용두: 신설동 신답 
    용마산: 사가정 중곡 
    용문: 원덕 
    용산: 남영 노량진 이촌 서울역 
    우장산: 발산 화곡 
    운길산: 양수 팔당 
    운서: 검암 공항화물청사 
    운정: 탄현 금릉 
    원당: 화정 삼송 
    원덕: 용문 양평 
    원인재: 신연수 동춘 남동인더스파크 연수 
    월계: 녹천 성북 
    월곡: 고려대 상월곡 
    월곶: 오이도 소래포구 
    월드컵경기장: 디지털미디어시티 마포구청 
    월롱: 금촌 파주 
    을지로3가: 을지로입구 을지로4가 종로3가 충무로 
    을지로4가: 을지로3가 동대문역사문화공원 종로3가 동대문역사문화공원 
    을지로입구: 시청 을지로3가 
    응봉: 왕십리 옥수 
    응암: 역촌 구산 새절 
    의왕: 당정 성균관대 
    의정부: 가능 회룡 
    이대: 신촌 아현 
    이매: 야탑 서현 
    이수: 동작 사당 내방 남성 
    이촌: 신용산 동작 서빙고 용산 
    이태원: 녹사평 한강진 
    인덕원: 정부과천청사 평촌 
    인천: 동인천 광명 
    인천국제공항: 공항화물청사 
    인천논현: 소래포구 호구포 
    인천대입구: 지식정보단지 센트럴파크 
    인천시청: 간석오거리 예술회관 
    인천터미널: 예술회관 문학경기장 
    일산: 풍산 탄현 
    일원: 대청 수서 
    임학: 박촌 계산 
    작전: 경인교대입구 갈산 
    잠실: 잠실나루 신천 몽촌토성 석촌 
    잠실나루: 강변 잠실 
    잠원: 신사 고속터미널 
    장승배기: 상도 신대방삼거리 
    장암: 도봉산 
    장지: 문정 복정 
    장한평: 답십리 군자 
    정발산: 주엽 마두 
    정부과천청사: 과천 인덕원 
    정왕: 신길온천 오이도 
    정자: 수내 미금 판교 
    제기동: 청량리 신설동 
    제물포: 도화 도원 
    종각: 종로3가 시청 
    종로3가: 종로5가 종각 안국 을지로3가 광화문 을지로4가 
    종로5가: 동대문 종로3가 
    종합운동장: 신천 삼성 봉은사 
    주안: 간석 도화 
    주엽: 대화 정발산 
    죽전: 오리 보정 
    중계: 노원 하계 
    중곡: 용마산 군자 
    중동: 부천 송내 
    중랑: 상봉 회기 
    중앙: 한대앞 고잔 
    중화: 먹골 상봉 
    증미: 가양 등촌 
    증산: 새절 디지털미디어시티 
    지식정보단지: 테크노파크 인천대입구 
    지제: 서정리 평택 
    지축: 삼송 구파발 
    지행: 동두천중앙 덕정 
    직산: 성환 두정 
    진위: 오산 송탄 
    창동: 방학 녹천 노원 쌍문 
    창신: 동묘앞 보문 
    천안: 두정 봉명 
    천왕: 광명사거리 온수 
    천호: 광나루 강동 암사 강동구청 
    철산: 가산디지털단지 광명사거리 
    청계산입구: 양재시민의숲 판교 
    청구: 동대문역사문화공원 신금호 약수 신당 
    청담: 뚝섬유원지 강남구청 
    청량리: 회기 제기동 회기 왕십리 
    청명: 상갈 영통 
    청평: 대성리 상천 
    춘의: 부천종합운동장 신중동 
    춘천: 남춘천 
    충무로: 을지로3가 동대입구 동대문역사문화공원 명동 
    충정로: 아현 시청 애오개 서대문 
    캠퍼스타운: 동막 테크노파크 
    탄현: 일산 운정 
    태릉입구: 석계 화랑대 공릉 먹골 
    태평: 경원대 모란 
    테크노파크: 캠퍼스타운 지식정보단지 
    퇴계원: 별내역 사릉 
    파주: 월롱 문산 
    판교: 청계산입구 정자 
    팔당: 운길산 도심 
    평내호평: 금곡 마석 
    평촌: 인덕원 범계 
    평택: 지제 성환 
    풍산: 백마 일산 
    하계: 중계 공릉 
    학동: 강남구청 논현 
    학여울: 대치 대청 
    한강진: 이태원 버티고개 
    한남: 옥수 서빙고 
    한대앞: 상록수 중앙 
    한성대입구: 성신여대입구 혜화 
    한양대: 왕십리 뚝섬 
    한티: 선릉 도곡 
    합정: 당산 홍대입구 망원 상수 
    행당: 신금호 왕십리 
    행신: 화전 능곡 
    혜화: 한성대입구 동대문 
    호구포: 인천논현 남동인더스파크 
    홍대입구: 합정 신촌 서강 가좌 공덕 디지털미디어시티 
    홍제: 녹번 무악재 
    화곡: 우장산 까치산 
    화랑대: 태릉입구 봉화산 
    화서: 성균관대 수원 
    화전: 수색 행신 
    화정: 대곡 원당 
    회기: 외대앞 청량리 중랑 청량리 
    회룡: 의정부 망월사 
    회현: 명동 서울역 
    효창공원앞: 공덕 삼각지 
    흑석: 노들 동작 
    ﻿소요산: 동두천 
    

graph에서는 점근 표기법 asymptotic notation에서 사용하는 알파벳이 다르다  
그 이유는 각 노드를 부르는 명칭이 n이 아니라 vertex의 V이기 때문이다  
사실 행렬에서 vertex는 벡터를 표시하지만 점근 표기법에서는 노드의 개수를 뜻하는 걸로 사용한다  
그 외에 edge의 개수를 E로 표시한다

||행렬|리스트|
|:-:|:-:|:-:|
|노드 공간|O(V)|O(V)|
|행렬 공간|O(V**2)|O(E)|
|연결 노드 찾는 시간|O(V)|O(1)|
- 확인 필요

## <a id='toc1_2_'></a>[그래프 탐색 = 순회](#toc0_)
---

하나의 시작점에서 모든 연결된 노드를 찾는 것  
자료구조에 포함된 모든 자료를 보는 걸 순회라 부르기 때문에 순회라고도 부른다

### <a id='toc1_2_1_'></a>[대표적인 두 알고리즘](#toc0_)
---
1. breadth first search
2. depth first search

![bfsdfs](https://www.freelancinggig.com/blog/wp-content/uploads/2019/02/BFS-and-DFS-Algorithms.png)

#### <a id='toc1_2_1_1_'></a>[BFS 너비 우선 탐색](#toc0_)
---
시작점에서 가까운 노드들을 탐색

이 때 큐를 먼저 알아야 한다  
queue는 맨 뒤 데이터 삽입 맨 앞 데이터 접근, 삭제하는 FIFO 추상 자료형이다

- 시작 노드를 방문 표시 후 큐에 넣는다
- 큐에 아무 노드가 없을 때까지
  - 큐 가장 앞 노드를 꺼낸다
  - 꺼낸 노드에 인접한 노드를 돌면서
    - 방문한 노드는 표시한다
    - 큐에 넣는다  
- 방문한 노드는 다시 큐에 넣지 않는다


```python
class StationNode:
    """지하철 역을 나타내는 역"""
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = False

    def add_connection(self, station):
        """파라미터로 받은 역과 엣지를 만들어주는 메소드"""
        self.adjacent_stations.append(station)
        station.adjacent_stations.append(self)


def create_station_graph(input_file):
    stations = {}

    # 일반 텍스트 파일을 여는 코드
    with open(input_file, 'r', encoding='utf-8') as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            previous_station = None  # 엣지를 저장하기 위한 변수
            raw_data = line.strip().split("-")

            for name in raw_data:
                station_name = name.strip()

                if station_name not in stations:
                    current_station = StationNode(station_name)
                    stations[station_name] = current_station

                else:
                    current_station = stations[station_name]

                if previous_station is not None:
                    current_station.add_connection(previous_station)

                previous_station = current_station

    return stations
```


```python
from collections import deque

def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque()  # 빈 큐 생성

    # 일단 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False
    
    start_node.visited = True
    queue.append(start_node)
    
    while queue:
        out = queue.popleft()
        for x in out.adjacent_stations:
            if x.visited is False:
                x.visited = True
                #x.prev = out
                queue.append(x)
            
    
    


stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)
```

    True
    True
    True
    True
    False
    False
    False
    False
    

#### <a id='toc1_2_1_2_'></a>[DFS](#toc0_)
---

깊이를 먼저 간 후, 길이 있는 위의 노드로 올라간 후 옆으로 이동

BFS를 queue로 하듯 DFS는 stack으로 한다

스택: 맨 뒤 데이터 추가, 맨 뒤 데이터 접근, 삭제 LIFO

- 스택에 아무 노드도 없을 때까지:

  - 스택에서 가장 위 노드를 꺼낸다
  - 짙은 회색(방문 처리) 표시한다
  - 이 노드에 인접해 있는 노드들을 돌면서:
    - 노란색 노드면:
    - 옅은 회색으로 표시한다
    - 스택에 넣는다


```python
class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name
        self.visited = 0  # 한 번도 본적 없을 때: 0, 스택에 있을 때: 1, 발견된 상태: 2
        self.adjacent_stations = []


    def add_connection(self, other_station):
        """지하철 역 노드 사이 엣지 저장하기"""
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)


def create_station_graph(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file, 'r', encoding='utf-8') as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            previous_station = None  # 엣지를 저장하기 위한 도우미 변수. 현재 보고 있는 역 전 역을 저장한다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in stations:
                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                    stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 인스턴스를 value로 저장한다

                else:
                    current_station = stations[station_name]  # 이미 저장한 역이면 stations에서 역 인스턴스를 갖고 온다

                if previous_station is not None:
                    current_station.add_connection(previous_station)  # 현재 역과 전 역의 엣지를 연결한다

                previous_station = current_station  # 현재 역을 전 역으로 저장

    return stations


```


```python
from collections import deque

def dfs(graph, start_node):
    """dfs 함수"""
    stack = deque()  # 빈 스택 생성

    # 모든 노드를 처음 보는 노드로 초기화
    for station_node in graph.values():
        station_node.visited = 0

    # 테스트 코드
    stack.append(start_node)
    start_node.visited = 2
    
    while stack:
        out = stack.pop()
        out.visited = 2
        for x in out.adjacent_stations:
            if x.visited is 0:
                x.visited = 1
                stack.append(x)



stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)


```

    2
    2
    2
    2
    0
    0
    0
    0
    

    <>:19: SyntaxWarning: "is" with a literal. Did you mean "=="?
    <>:19: SyntaxWarning: "is" with a literal. Did you mean "=="?
    C:\Users\path1\AppData\Local\Temp\ipykernel_12452\4247855436.py:19: SyntaxWarning: "is" with a literal. Did you mean "=="?
      if x.visited is 0:
    

다양한 최단 경로 알고리즘 중
1. BFS (비가중치의 경우에만) >>> backtracking
2. Dikstra (가중치의 경우)

#### <a id='toc1_2_1_3_'></a>[bfs backtracking](#toc0_)
---
- 시작 노드를 방문 표시 후 큐에 넣는다
- 큐에 아무 노드가 없을 때까지
  - 큐 가장 앞 노드를 꺼낸다
  - "꺼낸 노드"에 인접한 노드를 돌면서
    - 처음 방문한 노드면:
      - 방문 표시한다
      - prev 변수에 "꺼낸 노드"를 넣는다
      - 큐에 넣는다  
- 방문한 노드는 다시 큐에 넣지 않는다

backtracking:  
- 현재 노드를 경로에 추가
- 현재 노드의 prev로 간다
- prev가 없을 때까지 반복

bfs 최단경로 검증  



```python
class StationNode:
    """지하철 역을 나타내는 역"""
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = False
        self.predecessor = None

    def add_connection(self, station):
        """파라미터로 받은 역과 엣지를 만들어주는 메소드"""
        self.adjacent_stations.append(station)
        station.adjacent_stations.append(self)


def create_station_graph(input_file):
    stations = {}

    # 일반 텍스트 파일을 여는 코드
    with open(input_file, 'r', encoding='utf-8') as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            previous_station = None  # 엣지를 저장하기 위한 변수
            raw_data = line.strip().split("-")

            for name in raw_data:
                station_name = name.strip()

                if station_name not in stations:
                    current_station = StationNode(station_name)
                    stations[station_name] = current_station

                else:
                    current_station = stations[station_name]

                if previous_station is not None:
                    current_station.add_connection(previous_station)

                previous_station = current_station

    return stations
```


```python
from collections import deque

# 코드를 추가하세요
def bfs(graph, start_node):
    """최단 경로용 bfs 함수"""
    queue = deque()  # 빈 큐 생성

    # 모든 노드를 방문하지 않은 노드로 표시, 모든 predecessor는 None으로 초기화
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None

    # 시작점 노드를 방문 표시한 후 큐에 넣어준다
    start_node.visited = True
    queue.append(start_node)
    
    while queue:  # 큐에 노드가 있을 때까지
        current_station = queue.popleft()  # 큐의 가장 앞 데이터를 갖고 온다
        for neighbor in current_station.adjacent_stations:  # 인접한 노드를 돌면서
            if not neighbor.visited:  # 방문하지 않은 노드면
                neighbor.visited = True  # 방문 표시를 하고
                neighbor.predecessor = current_station ## 직전 경로를 넣고
                queue.append(neighbor)  # 큐에 넣는다


def back_track(destination_node):
    """최단 경로를 찾기 위한 back tracking 함수"""
    res_str = ""  # 리턴할 결과 문자열
    # 테스트 코드    
    q = deque()
    prev = destination_node.predecessor ## 도착지의 직전 경로를 설정
    q.append(str(destination_node.station_name))
    while prev: ## 직전 경로가 있으면
        q.append(prev.station_name)
        prev = prev.predecessor
    
    while q:
        out = q.pop()
        res_str += str(out) + " "
    
    return res_str


stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

bfs(stations, stations["을지로3가"])  # 지하철 그래프에서 을지로3가역을 시작 노드로 bfs 실행
print(back_track(stations["강동구청"]))  # 을지로3가에서 강동구청역까지 최단 경로 출력

```

    을지로3가 을지로4가 동대문역사문화공원 신당 상왕십리 왕십리 마장 답십리 장한평 군자 아차산 광나루 천호 강동구청 
    


```python
for station in sorted(stations.keys()):
        print(stations[station].predecessor)
```

    None
    None
    None
    None
    None
    <__main__.StationNode object at 0x0000021AAD0CFEB0>
    <__main__.StationNode object at 0x0000021AAD0551B0>
    <__main__.StationNode object at 0x0000021AAD0558A0>
    <__main__.StationNode object at 0x0000021AAD054C40>
    <__main__.StationNode object at 0x0000021AAD0B9C00>
    <__main__.StationNode object at 0x0000021AAD046800>
    <__main__.StationNode object at 0x0000021AACFF04C0>
    <__main__.StationNode object at 0x0000021AAD047220>
    None
    <__main__.StationNode object at 0x0000021AAD0452A0>
    <__main__.StationNode object at 0x0000021AAD0473A0>
    None
    <__main__.StationNode object at 0x0000021AAD0B9660>
    <__main__.StationNode object at 0x0000021AAD054490>
    <__main__.StationNode object at 0x0000021AAD0575B0>
    <__main__.StationNode object at 0x0000021AAD0575B0>
    <__main__.StationNode object at 0x0000021AAD0B92A0>
    <__main__.StationNode object at 0x0000021AAD046710>
    <__main__.StationNode object at 0x0000021AAD0BAF20>
    <__main__.StationNode object at 0x0000021AAD05F610>
    <__main__.StationNode object at 0x0000021AAD054430>
    <__main__.StationNode object at 0x0000021AAD0BBFA0>
    <__main__.StationNode object at 0x0000021AAD0BBFA0>
    <__main__.StationNode object at 0x0000021AAD057130>
    <__main__.StationNode object at 0x0000021AAD0B91E0>
    <__main__.StationNode object at 0x0000021AAD047760>
    <__main__.StationNode object at 0x0000021AAD0BB700>
    <__main__.StationNode object at 0x0000021AAD0BA740>
    <__main__.StationNode object at 0x0000021AAD055090>
    <__main__.StationNode object at 0x0000021AAD047460>
    <__main__.StationNode object at 0x0000021AAD0BAE60>
    <__main__.StationNode object at 0x0000021AAD0474C0>
    <__main__.StationNode object at 0x0000021AAD0BBFA0>
    <__main__.StationNode object at 0x0000021AAD057340>
    <__main__.StationNode object at 0x0000021AAD056800>
    <__main__.StationNode object at 0x0000021AAD055C00>
    <__main__.StationNode object at 0x0000021AAD0BBC40>
    <__main__.StationNode object at 0x0000021AAD0BA260>
    <__main__.StationNode object at 0x0000021AAD0BBCA0>
    <__main__.StationNode object at 0x0000021AAD05F700>
    <__main__.StationNode object at 0x0000021AAD0565C0>
    <__main__.StationNode object at 0x0000021AAD0BBFA0>
    <__main__.StationNode object at 0x0000021AAD047700>
    <__main__.StationNode object at 0x0000021AAD0BB7C0>
    <__main__.StationNode object at 0x0000021AAD0B8280>
    <__main__.StationNode object at 0x0000021AAD057520>
    <__main__.StationNode object at 0x0000021AAD0B8160>
    <__main__.StationNode object at 0x0000021AAD055840>
    <__main__.StationNode object at 0x0000021AAD05EE60>
    <__main__.StationNode object at 0x0000021AAD056B60>
    <__main__.StationNode object at 0x0000021AAD0BAAA0>
    <__main__.StationNode object at 0x0000021AAD05E950>
    <__main__.StationNode object at 0x0000021AAD0B9A20>
    <__main__.StationNode object at 0x0000021AAD0BAC20>
    <__main__.StationNode object at 0x0000021AAD047B80>
    <__main__.StationNode object at 0x0000021AAD0BB5E0>
    <__main__.StationNode object at 0x0000021AAD057010>
    <__main__.StationNode object at 0x0000021AAD057DC0>
    None
    <__main__.StationNode object at 0x0000021AAD0B9240>
    <__main__.StationNode object at 0x0000021AAD05E5C0>
    <__main__.StationNode object at 0x0000021AAD0BA4A0>
    <__main__.StationNode object at 0x0000021AAD047640>
    <__main__.StationNode object at 0x0000021AAD046CB0>
    <__main__.StationNode object at 0x0000021AAD057AC0>
    <__main__.StationNode object at 0x0000021AAD0575E0>
    <__main__.StationNode object at 0x0000021AAD0B8400>
    <__main__.StationNode object at 0x0000021AAD0467A0>
    <__main__.StationNode object at 0x0000021AAD055390>
    <__main__.StationNode object at 0x0000021AAD057400>
    <__main__.StationNode object at 0x0000021AAD047760>
    <__main__.StationNode object at 0x0000021AAD046AA0>
    <__main__.StationNode object at 0x0000021AAD047A90>
    <__main__.StationNode object at 0x0000021AAD0BB9A0>
    <__main__.StationNode object at 0x0000021AAD0B81C0>
    <__main__.StationNode object at 0x0000021AAD045180>
    <__main__.StationNode object at 0x0000021AAD0BA860>
    <__main__.StationNode object at 0x0000021AAD056860>
    <__main__.StationNode object at 0x0000021AAD057460>
    <__main__.StationNode object at 0x0000021AAD0BB280>
    <__main__.StationNode object at 0x0000021AAD0466B0>
    <__main__.StationNode object at 0x0000021AAD056E30>
    <__main__.StationNode object at 0x0000021AAD0B9EA0>
    <__main__.StationNode object at 0x0000021AAD05F7C0>
    <__main__.StationNode object at 0x0000021AAD0B9780>
    <__main__.StationNode object at 0x0000021AAD0B9A20>
    <__main__.StationNode object at 0x0000021AAD046F20>
    <__main__.StationNode object at 0x0000021AAD0B9660>
    <__main__.StationNode object at 0x0000021AAD0BB640>
    <__main__.StationNode object at 0x0000021AAD05F700>
    <__main__.StationNode object at 0x0000021AAD046650>
    <__main__.StationNode object at 0x0000021AAD0B9780>
    <__main__.StationNode object at 0x0000021AAD0550F0>
    <__main__.StationNode object at 0x0000021AAD0BB640>
    <__main__.StationNode object at 0x0000021AAD05F940>
    <__main__.StationNode object at 0x0000021AAD05F2B0>
    <__main__.StationNode object at 0x0000021AAD05F8E0>
    None
    <__main__.StationNode object at 0x0000021AAD0BA5C0>
    <__main__.StationNode object at 0x0000021AAD0BB4C0>
    <__main__.StationNode object at 0x0000021AAD0CFD60>
    <__main__.StationNode object at 0x0000021AAD05F880>
    <__main__.StationNode object at 0x0000021AAD055D20>
    <__main__.StationNode object at 0x0000021AAD0449A0>
    <__main__.StationNode object at 0x0000021AAD054F70>
    <__main__.StationNode object at 0x0000021AAD057700>
    <__main__.StationNode object at 0x0000021AAD0BAFE0>
    <__main__.StationNode object at 0x0000021AAD0B9BA0>
    <__main__.StationNode object at 0x0000021AAD0B8460>
    <__main__.StationNode object at 0x0000021AAD047C70>
    <__main__.StationNode object at 0x0000021AAD0BB760>
    None
    <__main__.StationNode object at 0x0000021AAD05E950>
    <__main__.StationNode object at 0x0000021AAD054370>
    <__main__.StationNode object at 0x0000021AAD05F940>
    <__main__.StationNode object at 0x0000021AAD046920>
    <__main__.StationNode object at 0x0000021AAD0BBA60>
    None
    <__main__.StationNode object at 0x0000021AAD0BACE0>
    <__main__.StationNode object at 0x0000021AAD0BAC20>
    <__main__.StationNode object at 0x0000021AAD0BA0E0>
    <__main__.StationNode object at 0x0000021AAD0579A0>
    <__main__.StationNode object at 0x0000021AAD0CFFD0>
    <__main__.StationNode object at 0x0000021AAD046CE0>
    <__main__.StationNode object at 0x0000021AACCAD060>
    <__main__.StationNode object at 0x0000021AAD0543D0>
    <__main__.StationNode object at 0x0000021AAD045F00>
    <__main__.StationNode object at 0x0000021AAD05E950>
    <__main__.StationNode object at 0x0000021AAD05F3D0>
    <__main__.StationNode object at 0x0000021AAD0CFFA0>
    <__main__.StationNode object at 0x0000021AAD0440A0>
    <__main__.StationNode object at 0x0000021AAD0B8040>
    <__main__.StationNode object at 0x0000021AACFF0520>
    <__main__.StationNode object at 0x0000021AAD0BA6E0>
    <__main__.StationNode object at 0x0000021AAD0BA500>
    <__main__.StationNode object at 0x0000021AAD0B8160>
    <__main__.StationNode object at 0x0000021AAD05F730>
    <__main__.StationNode object at 0x0000021AAD0B8FA0>
    <__main__.StationNode object at 0x0000021AAD0B8F40>
    <__main__.StationNode object at 0x0000021AAD0BA7A0>
    <__main__.StationNode object at 0x0000021AACCACEB0>
    <__main__.StationNode object at 0x0000021AACCACF70>
    <__main__.StationNode object at 0x0000021AAD046EC0>
    <__main__.StationNode object at 0x0000021AAD0B9000>
    <__main__.StationNode object at 0x0000021AACFF1E70>
    <__main__.StationNode object at 0x0000021AACFF02B0>
    <__main__.StationNode object at 0x0000021AAD0B80A0>
    <__main__.StationNode object at 0x0000021AAD0BB580>
    <__main__.StationNode object at 0x0000021AAD046F20>
    <__main__.StationNode object at 0x0000021AAD0B8AC0>
    <__main__.StationNode object at 0x0000021AAD057280>
    <__main__.StationNode object at 0x0000021AAD054AC0>
    <__main__.StationNode object at 0x0000021AAD0B9C00>
    <__main__.StationNode object at 0x0000021AAD0B9120>
    <__main__.StationNode object at 0x0000021AAD0B9240>
    <__main__.StationNode object at 0x0000021AAD057160>
    <__main__.StationNode object at 0x0000021AAD0BA200>
    <__main__.StationNode object at 0x0000021AAD0BB040>
    <__main__.StationNode object at 0x0000021AAD0469E0>
    <__main__.StationNode object at 0x0000021AAD0B90C0>
    <__main__.StationNode object at 0x0000021AAD0570D0>
    <__main__.StationNode object at 0x0000021AAD0579A0>
    <__main__.StationNode object at 0x0000021AAD056C20>
    <__main__.StationNode object at 0x0000021AAD056080>
    <__main__.StationNode object at 0x0000021AAD0B9BA0>
    <__main__.StationNode object at 0x0000021AAD0CFC40>
    <__main__.StationNode object at 0x0000021AAD057C40>
    <__main__.StationNode object at 0x0000021AAD0BAB60>
    <__main__.StationNode object at 0x0000021AAD056140>
    <__main__.StationNode object at 0x0000021AAD056080>
    <__main__.StationNode object at 0x0000021AAD0BA7A0>
    <__main__.StationNode object at 0x0000021AAD0573A0>
    <__main__.StationNode object at 0x0000021AAD0B8340>
    <__main__.StationNode object at 0x0000021AAD054250>
    <__main__.StationNode object at 0x0000021AAD057D00>
    <__main__.StationNode object at 0x0000021AAD0B93C0>
    <__main__.StationNode object at 0x0000021AAD0BA680>
    <__main__.StationNode object at 0x0000021AAD0B9AE0>
    <__main__.StationNode object at 0x0000021AAD0478B0>
    <__main__.StationNode object at 0x0000021AAD0BAE60>
    <__main__.StationNode object at 0x0000021AAD0470A0>
    <__main__.StationNode object at 0x0000021AAD055F90>
    <__main__.StationNode object at 0x0000021AAD0BB1C0>
    <__main__.StationNode object at 0x0000021AAD0BB220>
    <__main__.StationNode object at 0x0000021AAD047610>
    None
    <__main__.StationNode object at 0x0000021AAD0BBAC0>
    <__main__.StationNode object at 0x0000021AAD0BAAA0>
    <__main__.StationNode object at 0x0000021AAD055F00>
    <__main__.StationNode object at 0x0000021AAD0B9780>
    <__main__.StationNode object at 0x0000021AAD0BAF20>
    <__main__.StationNode object at 0x0000021AAD05F8E0>
    <__main__.StationNode object at 0x0000021AAD0BBF40>
    <__main__.StationNode object at 0x0000021AAD0B8CA0>
    <__main__.StationNode object at 0x0000021AAD047CD0>
    <__main__.StationNode object at 0x0000021AAD0BA260>
    <__main__.StationNode object at 0x0000021AAD046740>
    <__main__.StationNode object at 0x0000021AACFF1E70>
    <__main__.StationNode object at 0x0000021AAD0BA860>
    <__main__.StationNode object at 0x0000021AAD0BB940>
    <__main__.StationNode object at 0x0000021AAD046B90>
    <__main__.StationNode object at 0x0000021AAD0B86A0>
    <__main__.StationNode object at 0x0000021AAD055900>
    <__main__.StationNode object at 0x0000021AAD056980>
    <__main__.StationNode object at 0x0000021AACCACF10>
    <__main__.StationNode object at 0x0000021AAD057D60>
    <__main__.StationNode object at 0x0000021AAD0BAE00>
    <__main__.StationNode object at 0x0000021AAD0B8B80>
    <__main__.StationNode object at 0x0000021AAD0546D0>
    <__main__.StationNode object at 0x0000021AAD0B9840>
    <__main__.StationNode object at 0x0000021AAD056560>
    <__main__.StationNode object at 0x0000021AACFF1E70>
    <__main__.StationNode object at 0x0000021AACFF0310>
    <__main__.StationNode object at 0x0000021AAD0555D0>
    <__main__.StationNode object at 0x0000021AAD055660>
    <__main__.StationNode object at 0x0000021AAD0472E0>
    <__main__.StationNode object at 0x0000021AAD047340>
    <__main__.StationNode object at 0x0000021AAD047280>
    <__main__.StationNode object at 0x0000021AAD055390>
    <__main__.StationNode object at 0x0000021AAD0BA560>
    <__main__.StationNode object at 0x0000021AAD0560E0>
    <__main__.StationNode object at 0x0000021AAD0BB640>
    <__main__.StationNode object at 0x0000021AAD046A70>
    <__main__.StationNode object at 0x0000021AAD0BAAA0>
    <__main__.StationNode object at 0x0000021AAD0B8400>
    <__main__.StationNode object at 0x0000021AAD055090>
    <__main__.StationNode object at 0x0000021AAD0BB460>
    <__main__.StationNode object at 0x0000021AAD0553F0>
    <__main__.StationNode object at 0x0000021AAD0B9540>
    <__main__.StationNode object at 0x0000021AAD054610>
    <__main__.StationNode object at 0x0000021AAD0BA3E0>
    <__main__.StationNode object at 0x0000021AAD0564A0>
    <__main__.StationNode object at 0x0000021AAD0BB040>
    <__main__.StationNode object at 0x0000021AAD055AE0>
    <__main__.StationNode object at 0x0000021AAD0554B0>
    <__main__.StationNode object at 0x0000021AAD0BBB20>
    <__main__.StationNode object at 0x0000021AAD045B40>
    <__main__.StationNode object at 0x0000021AAD056CB0>
    <__main__.StationNode object at 0x0000021AAD0B9000>
    <__main__.StationNode object at 0x0000021AAD0566E0>
    <__main__.StationNode object at 0x0000021AAD0572E0>
    <__main__.StationNode object at 0x0000021AAD046860>
    <__main__.StationNode object at 0x0000021AAD056EC0>
    <__main__.StationNode object at 0x0000021AAD05F940>
    <__main__.StationNode object at 0x0000021AAD0579A0>
    <__main__.StationNode object at 0x0000021AAD057880>
    None
    <__main__.StationNode object at 0x0000021AAD0B8DC0>
    <__main__.StationNode object at 0x0000021AAD0BB580>
    <__main__.StationNode object at 0x0000021AAD0B97E0>
    <__main__.StationNode object at 0x0000021AAD0B90C0>
    <__main__.StationNode object at 0x0000021AAD05E980>
    <__main__.StationNode object at 0x0000021AAD0B88E0>
    <__main__.StationNode object at 0x0000021AAD0B9720>
    <__main__.StationNode object at 0x0000021AAD054040>
    <__main__.StationNode object at 0x0000021AAD05FC40>
    <__main__.StationNode object at 0x0000021AAD0B8220>
    <__main__.StationNode object at 0x0000021AAD0B93C0>
    <__main__.StationNode object at 0x0000021AAD054610>
    <__main__.StationNode object at 0x0000021AAD0BB6A0>
    <__main__.StationNode object at 0x0000021AAD0B9B40>
    <__main__.StationNode object at 0x0000021AAD055D80>
    <__main__.StationNode object at 0x0000021AAD046FE0>
    <__main__.StationNode object at 0x0000021AAD0B8520>
    <__main__.StationNode object at 0x0000021AAD05F730>
    <__main__.StationNode object at 0x0000021AAD0B9180>
    <__main__.StationNode object at 0x0000021AAD0BB2E0>
    <__main__.StationNode object at 0x0000021AAD0B8A00>
    <__main__.StationNode object at 0x0000021AAD0B8640>
    <__main__.StationNode object at 0x0000021AAD0B8700>
    <__main__.StationNode object at 0x0000021AAD044E20>
    <__main__.StationNode object at 0x0000021AAD046380>
    <__main__.StationNode object at 0x0000021AAD05ED10>
    <__main__.StationNode object at 0x0000021AACFF04F0>
    <__main__.StationNode object at 0x0000021AAD046290>
    <__main__.StationNode object at 0x0000021AAD0BBFA0>
    <__main__.StationNode object at 0x0000021AAD0B8880>
    <__main__.StationNode object at 0x0000021AAD054EE0>
    <__main__.StationNode object at 0x0000021AAD055F90>
    <__main__.StationNode object at 0x0000021AAD0563B0>
    <__main__.StationNode object at 0x0000021AAD0BBA00>
    <__main__.StationNode object at 0x0000021AAD056E30>
    <__main__.StationNode object at 0x0000021AAD054310>
    <__main__.StationNode object at 0x0000021AAD0B85E0>
    <__main__.StationNode object at 0x0000021AAD0BB160>
    <__main__.StationNode object at 0x0000021AAD054EB0>
    <__main__.StationNode object at 0x0000021AAD05F700>
    <__main__.StationNode object at 0x0000021AAD055B40>
    <__main__.StationNode object at 0x0000021AAD0B8E80>
    <__main__.StationNode object at 0x0000021AAD0568C0>
    <__main__.StationNode object at 0x0000021AAD057820>
    <__main__.StationNode object at 0x0000021AAD05ECE0>
    <__main__.StationNode object at 0x0000021AAD0BBD60>
    <__main__.StationNode object at 0x0000021AAD054790>
    <__main__.StationNode object at 0x0000021AAD0B9F60>
    <__main__.StationNode object at 0x0000021AAD0B8FA0>
    <__main__.StationNode object at 0x0000021AAD0B99C0>
    <__main__.StationNode object at 0x0000021AAD0559C0>
    <__main__.StationNode object at 0x0000021AAD05FFA0>
    <__main__.StationNode object at 0x0000021AAD0B98A0>
    <__main__.StationNode object at 0x0000021AAD054A00>
    <__main__.StationNode object at 0x0000021AAD0547F0>
    <__main__.StationNode object at 0x0000021AAD054D00>
    <__main__.StationNode object at 0x0000021AAD0BA980>
    <__main__.StationNode object at 0x0000021AAD05E830>
    <__main__.StationNode object at 0x0000021AAD046F80>
    <__main__.StationNode object at 0x0000021AAD0BB4C0>
    <__main__.StationNode object at 0x0000021AAD045FC0>
    <__main__.StationNode object at 0x0000021AAD05E9B0>
    <__main__.StationNode object at 0x0000021AAD057CA0>
    <__main__.StationNode object at 0x0000021AAD0B9E40>
    <__main__.StationNode object at 0x0000021AAD055630>
    <__main__.StationNode object at 0x0000021AAD0B8D60>
    <__main__.StationNode object at 0x0000021AAD0B9480>
    <__main__.StationNode object at 0x0000021AAD0B9C00>
    <__main__.StationNode object at 0x0000021AAD05F700>
    <__main__.StationNode object at 0x0000021AAD0B9A20>
    <__main__.StationNode object at 0x0000021AAD054FD0>
    <__main__.StationNode object at 0x0000021AAD0BB100>
    <__main__.StationNode object at 0x0000021AAD0B8BE0>
    <__main__.StationNode object at 0x0000021AAD0B8C40>
    <__main__.StationNode object at 0x0000021AAD046200>
    <__main__.StationNode object at 0x0000021AAD057640>
    <__main__.StationNode object at 0x0000021AAD0B9D80>
    <__main__.StationNode object at 0x0000021AAD05EE60>
    <__main__.StationNode object at 0x0000021AAD0BBD00>
    <__main__.StationNode object at 0x0000021AAD0567A0>
    <__main__.StationNode object at 0x0000021AAD0B82E0>
    <__main__.StationNode object at 0x0000021AAD0575B0>
    <__main__.StationNode object at 0x0000021AAD0BA920>
    <__main__.StationNode object at 0x0000021AAD054520>
    <__main__.StationNode object at 0x0000021AAD0B9D80>
    <__main__.StationNode object at 0x0000021AAD054190>
    <__main__.StationNode object at 0x0000021AAD0BA800>
    <__main__.StationNode object at 0x0000021AAD0479A0>
    <__main__.StationNode object at 0x0000021AAD0452A0>
    <__main__.StationNode object at 0x0000021AAD0B9600>
    <__main__.StationNode object at 0x0000021AAD0BAB60>
    <__main__.StationNode object at 0x0000021AAD047F40>
    <__main__.StationNode object at 0x0000021AAD0CFE20>
    <__main__.StationNode object at 0x0000021AAD0B9DE0>
    <__main__.StationNode object at 0x0000021AAD054CA0>
    <__main__.StationNode object at 0x0000021AAD0B9AE0>
    <__main__.StationNode object at 0x0000021AAD0B9240>
    <__main__.StationNode object at 0x0000021AAD054610>
    <__main__.StationNode object at 0x0000021AAD057A00>
    <__main__.StationNode object at 0x0000021AAD054880>
    <__main__.StationNode object at 0x0000021AAD05F7C0>
    <__main__.StationNode object at 0x0000021AAD0B9540>
    <__main__.StationNode object at 0x0000021AAD0BA500>
    <__main__.StationNode object at 0x0000021AAD046F20>
    <__main__.StationNode object at 0x0000021AAD0BA500>
    <__main__.StationNode object at 0x0000021AAD0549A0>
    <__main__.StationNode object at 0x0000021AAD05E710>
    <__main__.StationNode object at 0x0000021AAD0B9B40>
    <__main__.StationNode object at 0x0000021AAD05E710>
    <__main__.StationNode object at 0x0000021AAD056DA0>
    <__main__.StationNode object at 0x0000021AAD047160>
    <__main__.StationNode object at 0x0000021AAD0BAEC0>
    None
    <__main__.StationNode object at 0x0000021AAD05FF40>
    <__main__.StationNode object at 0x0000021AAD0554E0>
    <__main__.StationNode object at 0x0000021AAD057BB0>
    <__main__.StationNode object at 0x0000021AAD057BB0>
    <__main__.StationNode object at 0x0000021AAD0B87C0>
    <__main__.StationNode object at 0x0000021AAD0B8760>
    <__main__.StationNode object at 0x0000021AAD0BBE20>
    <__main__.StationNode object at 0x0000021AAD0BA8C0>
    <__main__.StationNode object at 0x0000021AAD05EEC0>
    <__main__.StationNode object at 0x0000021AAD0B8D00>
    <__main__.StationNode object at 0x0000021AAD057190>
    <__main__.StationNode object at 0x0000021AAD0B9060>
    <__main__.StationNode object at 0x0000021AAD05FB20>
    <__main__.StationNode object at 0x0000021AAD0B9FC0>
    <__main__.StationNode object at 0x0000021AAD05EE30>
    <__main__.StationNode object at 0x0000021AAD056050>
    <__main__.StationNode object at 0x0000021AAD055000>
    <__main__.StationNode object at 0x0000021AAD05F700>
    <__main__.StationNode object at 0x0000021AAD057F70>
    <__main__.StationNode object at 0x0000021AAD0462C0>
    <__main__.StationNode object at 0x0000021AAD047850>
    <__main__.StationNode object at 0x0000021AAD047AF0>
    <__main__.StationNode object at 0x0000021AAD0BA2C0>
    <__main__.StationNode object at 0x0000021AAD057BB0>
    <__main__.StationNode object at 0x0000021AAD047070>
    <__main__.StationNode object at 0x0000021AAD05FE50>
    <__main__.StationNode object at 0x0000021AAD056740>
    <__main__.StationNode object at 0x0000021AAD0BBE80>
    <__main__.StationNode object at 0x0000021AAD056E30>
    <__main__.StationNode object at 0x0000021AAD047970>
    None
    None
    None
    <__main__.StationNode object at 0x0000021AAD0B8EE0>
    <__main__.StationNode object at 0x0000021AAD0B8EE0>
    <__main__.StationNode object at 0x0000021AAD0B90C0>
    <__main__.StationNode object at 0x0000021AAD056E90>
    <__main__.StationNode object at 0x0000021AAD0B84C0>
    <__main__.StationNode object at 0x0000021AAD0CF9A0>
    <__main__.StationNode object at 0x0000021AAD0B9D20>
    <__main__.StationNode object at 0x0000021AAD054130>
    <__main__.StationNode object at 0x0000021AAD0BB5E0>
    <__main__.StationNode object at 0x0000021AAD05F2B0>
    <__main__.StationNode object at 0x0000021AAD056A40>
    <__main__.StationNode object at 0x0000021AAD0BB880>
    <__main__.StationNode object at 0x0000021AAD0B8100>
    <__main__.StationNode object at 0x0000021AAD0476A0>
    <__main__.StationNode object at 0x0000021AAD046320>
    <__main__.StationNode object at 0x0000021AAD046D40>
    <__main__.StationNode object at 0x0000021AAD0471C0>
    <__main__.StationNode object at 0x0000021AAD047100>
    <__main__.StationNode object at 0x0000021AAD047BE0>
    <__main__.StationNode object at 0x0000021AAD0BAD40>
    <__main__.StationNode object at 0x0000021AAD0475B0>
    <__main__.StationNode object at 0x0000021AAD047400>
    <__main__.StationNode object at 0x0000021AAD0B9360>
    <__main__.StationNode object at 0x0000021AAD0B9300>
    <__main__.StationNode object at 0x0000021AAD0BA9E0>
    <__main__.StationNode object at 0x0000021AAD055BD0>
    <__main__.StationNode object at 0x0000021AAD0CFC40>
    <__main__.StationNode object at 0x0000021AAD055210>
    <__main__.StationNode object at 0x0000021AAD0576A0>
    <__main__.StationNode object at 0x0000021AAD0BA1A0>
    <__main__.StationNode object at 0x0000021AAD0BB820>
    None
    <__main__.StationNode object at 0x0000021AAD0BBDC0>
    <__main__.StationNode object at 0x0000021AAD046110>
    <__main__.StationNode object at 0x0000021AAD05EE30>
    <__main__.StationNode object at 0x0000021AACFF0400>
    <__main__.StationNode object at 0x0000021AAD05EE60>
    <__main__.StationNode object at 0x0000021AAD0B8EE0>
    <__main__.StationNode object at 0x0000021AAD05EE60>
    <__main__.StationNode object at 0x0000021AAD0544F0>
    <__main__.StationNode object at 0x0000021AACFF1DE0>
    <__main__.StationNode object at 0x0000021AAD0BA140>
    <__main__.StationNode object at 0x0000021AAD054A60>
    <__main__.StationNode object at 0x0000021AAD0562F0>
    <__main__.StationNode object at 0x0000021AAD057640>
    None
    <__main__.StationNode object at 0x0000021AACFF06D0>
    <__main__.StationNode object at 0x0000021AAD05FB20>
    <__main__.StationNode object at 0x0000021AAD0BBBE0>
    None
    <__main__.StationNode object at 0x0000021AAD056080>
    <__main__.StationNode object at 0x0000021AAD054B20>
    <__main__.StationNode object at 0x0000021AAD056E30>
    <__main__.StationNode object at 0x0000021AAD046DA0>
    <__main__.StationNode object at 0x0000021AAD0B8940>
    None
    <__main__.StationNode object at 0x0000021AAD0BA440>
    <__main__.StationNode object at 0x0000021AACCACFD0>
    <__main__.StationNode object at 0x0000021AAD0B8A60>
    <__main__.StationNode object at 0x0000021AAD0B8820>
    <__main__.StationNode object at 0x0000021AAD0BB0A0>
    <__main__.StationNode object at 0x0000021AAD05E830>
    <__main__.StationNode object at 0x0000021AAD0B8B20>
    <__main__.StationNode object at 0x0000021AAD05F7C0>
    <__main__.StationNode object at 0x0000021AAD0574C0>
    <__main__.StationNode object at 0x0000021AAD0B8160>
    <__main__.StationNode object at 0x0000021AAD0461D0>
    <__main__.StationNode object at 0x0000021AAD0B8FA0>
    <__main__.StationNode object at 0x0000021AAD055D80>
    <__main__.StationNode object at 0x0000021AAD0B90C0>
    <__main__.StationNode object at 0x0000021AAD055780>
    <__main__.StationNode object at 0x0000021AAD0468C0>
    <__main__.StationNode object at 0x0000021AAD055750>
    <__main__.StationNode object at 0x0000021AAD046560>
    <__main__.StationNode object at 0x0000021AAD0B8EE0>
    <__main__.StationNode object at 0x0000021AAD05E980>
    <__main__.StationNode object at 0x0000021AAD046E60>
    None
    <__main__.StationNode object at 0x0000021AAD047B50>
    <__main__.StationNode object at 0x0000021AAD05F730>
    <__main__.StationNode object at 0x0000021AAD0542B0>
    <__main__.StationNode object at 0x0000021AAD046E00>
    <__main__.StationNode object at 0x0000021AAD046B30>
    <__main__.StationNode object at 0x0000021AAD047910>
    <__main__.StationNode object at 0x0000021AAD046170>
    None
    <__main__.StationNode object at 0x0000021AAD044B20>
    <__main__.StationNode object at 0x0000021AAD046980>
    <__main__.StationNode object at 0x0000021AAD0BB8E0>
    <__main__.StationNode object at 0x0000021AAD0B89A0>
    <__main__.StationNode object at 0x0000021AAD047BB0>
    <__main__.StationNode object at 0x0000021AAD056290>
    <__main__.StationNode object at 0x0000021AAD055D80>
    <__main__.StationNode object at 0x0000021AAD0BAC80>
    <__main__.StationNode object at 0x0000021AAD056920>
    <__main__.StationNode object at 0x0000021AAD0BA920>
    <__main__.StationNode object at 0x0000021AAD0BBB80>
    <__main__.StationNode object at 0x0000021AAD0BB340>
    <__main__.StationNode object at 0x0000021AAD0B90C0>
    <__main__.StationNode object at 0x0000021AAD0B9540>
    <__main__.StationNode object at 0x0000021AAD0B9C00>
    <__main__.StationNode object at 0x0000021AAD0577C0>
    <__main__.StationNode object at 0x0000021AAD047D30>
    <__main__.StationNode object at 0x0000021AAD05F2E0>
    <__main__.StationNode object at 0x0000021AAD0462F0>
    <__main__.StationNode object at 0x0000021AAD0579A0>
    <__main__.StationNode object at 0x0000021AAD0BA620>
    <__main__.StationNode object at 0x0000021AAD057FA0>
    <__main__.StationNode object at 0x0000021AAD0565C0>
    <__main__.StationNode object at 0x0000021AAD0B8580>
    <__main__.StationNode object at 0x0000021AAD047DC0>
    <__main__.StationNode object at 0x0000021AAD0BA260>
    <__main__.StationNode object at 0x0000021AAD05E6E0>
    <__main__.StationNode object at 0x0000021AAD0CFB20>
    <__main__.StationNode object at 0x0000021AAD0BB3A0>
    <__main__.StationNode object at 0x0000021AAD0579A0>
    <__main__.StationNode object at 0x0000021AAD0548E0>
    <__main__.StationNode object at 0x0000021AACCACE50>
    


```python
def back_track(destination_node):
    """최단 경로를 찾기 위한 back tracking 함수"""
    res_str = ""  # 리턴할 결과 문자열
    temp = destination_node  #  도착 노드에서 시작 노드까지 찾아가는 데 사용할 변수

    # 시작 노드까지 갈 때까지
    while temp is not None:
        res_str = f"{temp.station_name} {res_str}"  # 결과 문자열에 역 이름을 더하고
        temp = temp.predecessor  # temp를 다음 노드로 바꿔준다
        
    ##################### f string 안에 자기 자신을 문자열로 또 넣을 수가 있구나 멋지다!
    # 이렇게 하면 계속 직전 문자열 앞에 새로운 문자열을 넣을 수가 있네

    return res_str

stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

bfs(stations, stations["을지로3가"])  # 지하철 그래프에서 을지로3가역을 시작 노드로 bfs 실행
print(back_track(stations["강동구청"]))  # 을지로3가에서 강동구청역까지 최단 경로 출력

```

    을지로3가 을지로4가 동대문역사문화공원 신당 상왕십리 왕십리 마장 답십리 장한평 군자 아차산 광나루 천호 강동구청 
    

#### <a id='toc1_2_1_4_'></a>[dijkstra 알고리즘의 세 요소](#toc0_)
---
1. distance: 특정 노드까지의 최단 거리 예상치 (현재까지 계산된 값 중 최소값)
2. predecessor: 특정 노드까지 최단 거리 경로의 직전 노드
3. complete: 최단 경로를 찾았는지 여부

relax edge(a, b) : b를 방문할 때 b의 변수 distance, predecessor를 바꿔준다

dijkstra  
- 시작점 distance = 0, predecessor = None
- 모든 node가 complete일 때까지:
  - choose minimum distance node
  - choose its incomplete node
    - relax each edge
  - complete the node

tbd Dijkstra example

다익스트라를 보다보니 optimal substructure 랑 greedy property(현재 최적의 선택이 최선의 선택)가 있어보여서 검색해보니 다익스트라도 greedy algorithm에 속하는 게 맞았다 천재

## <a id='toc1_3_'></a>[수료증](https://www.codeit.kr/certificates/InUrg-E72Q6-Gmuwl-CmMWs) [&#8593;](#toc0_)
