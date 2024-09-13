11.김향은
gimhyangeun_50679
오프라인 표시

11. 김혜지 — 어제 오전 10:08
/cart/
cart/
11.신덕근 — 어제 오전 10:13
reviews/views.py 파일에서
상단에 import 추가
from django.core.files.base import ContentFile

edit_review(request, review_id)부분 전체 내용 변경
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                image_content = ContentFile(image_file.read())
                review.image.save(image_file.name, image_content, save=False)
            elif form.cleaned_data['image'] is False:
                review.image = None
            review.save()
            messages.success(request, '리뷰가 성공적으로 수정되었습니다.')
            return redirect('profile_display')
        else:
            messages.error(request, '폼 유효성 검사 실패')
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'reviews/edit_review.html', context)


reviews/forms.py 파일
이미지 필드 내용 추가
rating = forms.ChoiceField{
    ~~~
} 밑 부분에

image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))



myweb/settings.py 파일
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')로 내용 변경
11. 김혜지 — 어제 오전 10:19
코드 작성하면서 어려웠던 기능 -> 어떻게 해결했는지
기능 구현 하려고 했는데 못한 기능 -> 왜 못했는지
3차때는 어떤 기능을 하고 싶은지
11. 김혜지 — 어제 오전 10:36
이미지
이미지
이미지
11.김향은 — 어제 오전 10:49
이미지
[강사] 양석환 — 어제 오전 11:01
안녕하세요. 오늘이 사실상 프로젝트 마지막 날입니다. 진행/발표준비는 잘 되고 계신가요?
11. 김혜지 — 어제 오전 11:03
네 저희 발표 준비 중입니다!
[강사] 양석환 — 어제 오전 11:04
통합된 시스템은 잘 작동하고 있나요?
11. 김혜지 — 어제 오전 11:05
넵 기본적인 기능은 잘 작동합니다
[강사] 양석환 — 어제 오전 11:05
예. 알겠습니다. 그럼 오늘도 마지막까지 화이팅 합시다.
11.신덕근 — 어제 오전 11:59
리뷰 작성 한 파일 메일로 세분께 다 보내드렸습니다.
기존에 있던 아이디는 다 삭제했고, 
superuser아이디는
아이디:root123
비밀번호:root123

개인 아이디
아이디:각자 이름(한글)
비밀번호:root1234

로 생성해 리뷰 개인당 2품목씩 리뷰 작성했습니다.
사진이 제대로 나오는지 한번 확인 부탁드립니다.
혹시 제품 사진 나오지 않는다면 이 사진 파일로 수정 부탁드립니다.
첨부 파일 형식: archive
제품 사진.zip
116.49 KB
11. 김지웅 — 어제 오후 12:54
제품사진이랑 리뷰 잘보입니다!
11.신덕근 — 어제 오후 1:00
별도로 사진 파일 추가 안하셔도 잘보이시나요?
11. 김지웅 — 어제 오후 1:00
네네
11.신덕근 — 어제 오후 1:00
네 다행이네요!
11.김향은 — 어제 오후 1:38
코드 작성하면서 어려웠던 기능
-Category 기능 구현이 어려웠음
-처음에는 프로젝트 초기 단계에서 빠르게 개발을 진행하고 데이터베이스 구조를 단순화 시키기 위해 CharField 또는 ChoiceField를 사용하려 했음
-그러나 프로젝트가 커지면서 확장성과 데이터 관리의 어려움이 예상되어 독립된 Category 모델을 사용하는 게 더 적합하다고 결론 내림
-하지만, 카테고리 필드를 Product모델에 추가하면서 기존에 등록된 Product 데이터와의 호환성 문제를 겪음
-Product 모델에 새로운 Category 필드를 추가했지만, 기존에 저장된 제품 데이터에는 이 필드와 연결된 Category 객체가 없었기 때문에,
외래 키 제약 조건을 위반하는 오류가 발생함
-이 문제를 해결하기 위해 우선 기존 제품 데이터에 대해 기본 카테고리를 설정해주고, 새롭게 정의된 Category 객체와 기존 데이터를 연결하는 마이그레이션 작업을 수행함
-마이그레이션 과정에서 기존 데이터의 무결성을 유지하면서 새로운 필드를 적용하는 것이 어려웠지만 여러 시도 끝에 다행히 잘 구현됨

구현하지 못한 기능
-구매 이력 조회 기능을 구현하지 못했음
-기본적인 데이터 모델과 프로젝트 연결은 완료했으나 데이터를 적절히 불러오는 로직과 템플릿에서 해당 데이터를 표시하는 방식에 여러 이슈가 발생했음
-또한, 각 구매자의 주문 내역을 효율적으로 필터링하는 부분에 문제가 있었는데, 이 부분은 3차 프로젝트에서 보완할 계획임

3차때는 어떤 기능을 구현할 것인지
-우선 구매 이력 조회 기능을 완료할 계획임, 날짜별로 주문 내역을 필터링 하거나 주문 상태(배송중, 배송완료 등)에 따라 정렬하는 기능을 추가할 예정
-또한 상품의 상세 페이지에서 좋아요 기능을 통해 사용자 참여를 높이는 기능을 구현하고자 함

이번 프로젝트를 하면서 느낀점)
깃허브 연동이 잘 안 되어서 아쉬웠음. 
3차때는 꼭 깃을 활용하여 팀 프로젝트 진행에 도움이 되었음 좋겠음! 
11. 김지웅 — 어제 오후 1:47
1) 코드 작성하면서 어려웠던 기능
CSS 디자인 조정의 어려움
문제점: 새로운 기능을 추가할 때마다 CSS 디자인이 미세하게 맞지 않아 어려움을 겪었고, 주로 margin과 padding을 통해 조정하였지만 정확한 조정이 어려웠음.
해결 방법: 여러 번의 시도 끝에 디자인을 시각적으로 적절하게 맞출 수 있었고, 특히 메인 홈페이지의 배너 슬라이드 기능에서 스크립트를 사용해 3초마다 배너가 넘어가도록 구현함. 하지만, 페이지 크기를 조절할 때 배너 크기가 적절히 조정되지 않는 문제가 여전히 남아있음.

비밀번호 재확인 폼의 입력란 잠금 기능
문제점: 사용자 프로필에 들어가기 전에 비밀번호를 재확인하는 폼에서, 아이디 입력란을 잠그고 싶었음.
해결 방법: readonly 속성을 사용하여 입력 필드를 수정할 수 없게 만들었음. readonly 속성은 HTML의 <input> 요소에서 사용자가 값을 수정하지 못하도록 설정하는 속성으로, 보안과 사용자 편의성을 동시에 달성할 수 있었음.
<input type="text" name="id" value="{{ user.username }}" readonly class="readonly-input">

2) 구현하려 했으나 해결하지 못한 기능
선물특가 타이머 기능
타이머 기능을 구현할 때, 새로고침을 해도 타이머가 흐른 시간을 유지하도록 하려고 했으나, 시간이 한번 설정되면 수정이 불가능한 문제가 발생했음. 새로고침 후에도 타이머가 초기화되지 않고 흐른 시간이 유지되도록 하는 것이 어려웠음.
현재 상태: 결국 타이머는 새로고침 시마다 시간이 초기화되는 방식으로 설정되었으며, 해당 문제는 3차 프로젝트에서 해결할 계획임.

3) 3차 프로젝트에서 구현하고 싶은 기능
개인 페이지에서 회원 정보 및 비밀번호 수정 기능
사용자들이 자신의 회원 정보를 수정할 수 있는 기능을 추가하고 비밀번호를 변경할 수 있는 기능을 함께 구현하여 사용자 경험을 개선하고, 보안을 강화할 예정.

추천인 코드 및 마일리지 기능
추천인 코드를 통해 새로운 회원 가입 시 추천한 사용자에게 마일리지를 적립해주는 기능을 구현할 예정임. 이 기능을 통해 사용자들의 참여를 독려하고, 마일리지를 활용해 다양한 혜택을 제공할 수 있도록 할 계획임.

홈페이지 검색어 입력 기능 연동
사용자가 검색어를 입력하면 해당 검색어에 맞는 상품이나 정보를 연동하여 제공하는 검색 기능을 추가할 예정임. 
11.신덕근 — 어제 오후 1:58
이번에 기능들을 정리하며 놓친 부분을 발견해서 수정했습니다.
리뷰 표시할때 제품 상세 페이지에 별점 평균 표시 기능과 적립금 계산 용도로 작성했던 커스텀 템플릿 태그 부분이 현재 아무 기능도 하고 있지 않기 때문에 그냥 놔두셔도 별 문제는 없지만 삭제하는 편이 더 깔끔할것 같습니다.

reviews/templates/reviews/review_mypage.html 파일
제일 상단에 위치한 밑에 내용 부분 삭제
{% load review_extras %}

reviews/apps.py 파일
밑에 내용 부분 삭제
 def ready(self):# 커스텀 템플릿 태그 모듈을 임포트하여 등록
      import reviews.templatetags.review_extras

reviews/templatetags 디렉토리 삭제
11. 김혜지 — 어제 오후 2:00
넵! 그리고 1~2줄 분량으로 이번 팀플하면서 느꼈던 점, 3차때는 어떻게 하면 좋겠다 등을 작성해서 보내주세요
짧게 작성해주시면 돼요
11. 김지웅 — 어제 오후 2:02
이번 팀 프로젝트를 진행하면서, 협업의 중요성과 각자의 역할 분담이 프로젝트의 성공에 큰 영향을 미친다는 것을 느꼈습니다. 3차 때는 각자 맡은 역할을 더욱 명확하게 분담하고, 코드 리뷰와 소통을 자주 하여 더 효율적인 개발 과정을 만들면 좋겠습니다.
11.김향은 — 어제 오후 2:03
저는 위에 올려둔 글에 수정해서 추가했습니다!!
11. 김지웅 — 어제 오후 2:40
저희 홈페이지 전체 캡처 사진입니다
이미지
11. 김혜지 — 어제 오후 2:57
혹시 여기서 추가하거나 삭제할 부분 있나요?
이미지
11.신덕근 — 어제 오후 2:59
제 쪽은 괜찮은거 같습니다.
11. 김지웅 — 어제 오후 3:00
저도 괜찮습니다!
11.김향은 — 어제 오후 3:00
저도 괜찮습니다!
11. 김혜지 — 어제 오후 3:12
향은님! 혹시 시연 영상 찍어주실 수 있으신가요? 오늘 중으로 ppt랑 대본 만들다보면 시간이 조금 빠듯할 것 같아 여쭤봅니다
11.김향은 — 어제 오후 3:13
넵 한번 해볼게요!
11. 김혜지 — 어제 오후 3:14
네!! 혹시 잘 안되면 말씀해주세요 감사합니다😀
11.김향은 — 어제 오후 3:48
영상에 최대한 깔끔하게 동선 짜고싶어서 생각보다 좀 걸리네요ㅜㅜ 5시 내로 찍어서 보내드릴게요!
11.신덕근 — 어제 오후 4:27
생각보다 많이 늦어졌네요 죄송합니다.
## 구매 확인된 상품에 대해서만 리뷰 작성 가능하게 하기

### 실제 구현된 코드:
@login_required
def review_entry_form(request, product_id):
    product = get_object_or_404(Product, id=product_id)
확장
프로젝트.txt
11KB
11.김향은 — 어제 오후 4:29
혜지님 메일로 영상 보냈는데 보시고 혹시 제가 놓친 기능이나 보완해야 할 부분 있으면 말씀해주세요!
그리고 카테고리 부분 두 가지밖에 없어서 좀 더 추가해서 찍어봤어요
11. 김혜지 — 어제 오후 4:30
넵! 감사합니다
11. 김혜지 — 어제 오후 4:41
회원가입 할 때 이미지도 추가해서 마이페이지에서 이미지가 보일 수 있게 해주세요
리뷰 삭제 전에 수정 되는 장면 추가하고 삭제 보여주시면 될 것 같아요

진짜 너무 너무 감사합니다ㅠㅠ 동선도 너무 깔끔하고 시간도 너무 좋아요 2가지만 수정해서 보내주시면 그걸로 제출하겠습니다!  😀
11.김향은 — 어제 오후 4:43
네넵!
11.신덕근 — 어제 오후 4:44
각자 프로필 만들때 사용한 사진 있는데 필요하시면 사용하셔도 되요 올려놓겠습니다.
이미지
이미지
이미지
이미지
11.김향은 — 어제 오후 4:44
오 넵 감사합니다
11.김향은 — 어제 오후 5:06
혜지님 메일 보냈습니다!
11. 김혜지 — 어제 오후 5:15
확인했습니다 정말 고생 많으셨어요 감사합니다:)
11.김향은 — 어제 오후 5:16
넵! 또 도움 필요하시면 말씀해주세요!
11. 김혜지 — 어제 오후 10:33
https://www.canva.com/design/DAGQgtRPG5Y/6GwHUEgTg_uPNs9YSGAMiQ/edit?utm_content=DAGQgtRPG5Y&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
늦은 시간에 죄송합니다 ppt완성본 보냅니다! 내일 오전 9시 30분까지 확인 후에 수정사항 있으면 피드백 부탁드립니다 내일 뵙겠습니다:)
11. 김혜지 — 오늘 오전 8:59
11시까지 자료 제출해야되는게 많아서 제출 전에 이야기 해보려고 합니다! 9시 30분에 음성 채팅으로 만날게요
11.신덕근 — 오늘 오전 9:00
네 알겠습니다!
11. 김혜지 — 오늘 오전 9:32
첨부 파일 형식: spreadsheet
[BES11] 3팀 버그박멸단 기획안 및 일일보고서.xlsx
50.41 KB
11. 김지웅 — 오늘 오전 9:33
###  🚀Clean_Curly 프로젝트 1st 🚀
- 마켓컬리 백엔드 클론코딩 프로젝트.
- 이커머스 사이트의 필수 기능을 구현
- 1차 프로젝트 결과임으로 아직 완벽하게 완성된 버전은 아님


### 🚴개발 인원 및 기간
- [팀프로젝트 기간] 2024-09.02(월) ~ 2024-09.13(금)
- [개발인원] : 백엔드 4명

### 🛠️기술스택
- Language : `python3`
- Framework : `Django`

### 💡ERD(1st)
![image](https://github.com/user-attachments/assets/2bcc12f3-f569-4b35-812c-f2b53c66e4c5)


### 🤗 팀 멤버
- [신덕근](https://github.com/shindeokgeun)
- [김향은](https://github.com/myangeun)
- [김혜지](https://github.com/hjkim977)
- [김지웅](https://github.com/kgw08003)

### 홈페이지 데모
![클린컬리](https://github.com/user-attachments/assets/bd02c593-fa10-48bb-979d-a24f744183ea)


### 📃 구현 기능📃 

#### 김혜지
- [`ERD` 내 `ORDERS` `CARTS` 기능 담당]
- 장바구니 기능 (추가, 수정, 삭제)
- 물건구매
- ![image](https://github.com/user-attachments/assets/ed41cf67-889d-4b0b-b627-c8200ace2cbb)
- ![image](https://github.com/user-attachments/assets/195cc85e-a542-455c-b352-1e509268a252)
- ![image](https://github.com/user-attachments/assets/56935614-85f0-406c-926a-65464457e190)

#### 신덕근
- [`ERD` 내 `REVIEWS` 기능 담당]
- 상품 리뷰 작성, 수정, 삭제
- ![image](https://github.com/user-attachments/assets/90e46f61-5d60-4405-9fe5-f480564151e0)
- ![image](https://github.com/user-attachments/assets/f50d81d4-2887-4e5a-99f7-c34af2871507)


#### 김지웅
- [`ERD` 내 `USER` 기능 담당]
- 회원가입 및 유저 관련 내용 로그인 페이지
- 로그인, 회원가입
![image](https://github.com/user-attachments/assets/0e599038-ebb7-4f53-a9cf-77babee87063)
![image](https://github.com/user-attachments/assets/5c82ea31-0d02-46f7-ac5b-cee173fb1056)

- 비밀번호 재확인 페이지, 개인정보 페이지(`users` 내 비밀번호 재확인 페이지, 개인정보 페이지(유저정보 관련 내용)
![image](https://github.com/user-attachments/assets/f87e64ca-d6d7-4f37-a2b6-4a0e363e3de8)
![image](https://github.com/user-attachments/assets/3216e47e-51e1-437a-9877-36062881d80e)


#### 김향은
- [`ERD` 내 `PRODUCTS` 기능 담당]
- 판매할 물건 등록, 삭제, 수정
- ![image](https://github.com/user-attachments/assets/118953dc-762e-4785-ad8e-a1030b02dd01)




### 🔐 코드 작성하면서 어려웠던 기능🔐
### [김혜지]
###### 장바구니에 있는 상품을 주문으로 생성
- 문제점: 리뷰 기능과 합해지면서 오류가 발생: 리뷰에서는 로그인이 된 사용자, 물건을 구매한 사용자만이 리뷰를 작성할 수 있도록 구현하였으나 이점을 고려하지 않고 orders 기능을 구현하여 오류가 발생
- 해결 방법: 현재 요청을 보낸 사용자가 로그인이 된 상태인지 확인하기 위해 `order_create` 함수에 사용자 정보를 설정하는 `order.user = request.user` 코드를 추가

###  📝구현하려 했으나 해결하지 못한 기능📝
###### <담기> 버튼 기능
- 자바스크립트를 이용하면 쉽게 구현 가능한 기능
- 현재 상황:<담기> 버튼을 누르면 상품 상세페이지로 이동

### 🔥2차 프로젝트에서 구현하고 싶은 기능🔥
- 구매 이력 조회
- 메인 페이지에서 <담기> 버튼을 누르면 장바구니에 해당 상품이 담기게 하기
- <주문요청하기> 버튼을 누르면 배송상태가 `delivered`로 변경
- 찜하기 기능 추가

---------
### 🔐 코드 작성하면서 어려웠던 기능🔐
### [신덕근]
###### 리뷰 작성 가능한 상품 필터링
- 문제점: 주문, 상품, 다른 종류의 여러 데이터들을 한꺼번에 연결, 사용자가 주문한 상품, 배송상태, 리뷰 상태를 동시에 연결, 이미 리뷰를 작성한 상품은 제외하는 로직을 구현
- 해결 방법: Django orm 의 쿼리 사용 : 지정된 필드의 값만 가져오는 values_list 와 제외 기능인 exclude를 활용하여 데이터를 추출

###  📝구현하려 했으나 해결하지 못한 기능📝
###### 주문 시스템과의 미연동
- 현재 주문 시스템과의 자동 연동 기능이 구현되지 않아 admin에서 직접 주문상태를 delivered 로 설정해야 리뷰 작성 가능
###### 마이 페이지 -> 구매평
- 마이페이지 구매평 부분에 html, css문제로 클릭을 해야만 구매평(리뷰 관련 내용)이 표시됨

### 🔥2차 프로젝트에서 구현하고 싶은 기능🔥
- 주문 시스템과의 연동
- 리뷰 정렬 방식 개선(좋아요 기능 추가)
- 평균 별점 표시
- 마이페이지에서 리뷰 내용이 바로 보이도록 html과 css파일 재정리
... (54줄 남음)
접기
message.txt
8KB
11. 김혜지 — 오늘 오전 9:34
https://github.com/hjkim977/Team-Project/tree/main
GitHub
GitHub - hjkim977/Team-Project
Contribute to hjkim977/Team-Project development by creating an account on GitHub.
11. 김혜지 — 오늘 오전 9:51
첨부 파일 형식: acrobat
3팀 중간발표.pdf
394.61 KB
첨부 파일 형식: acrobat
3팀 최종발표.pdf
6.18 MB
첨부 파일 형식: spreadsheet
[BES11] 3팀 버그박멸단 기획안 및 일일보고서.xlsx
51.01 KB
11. 김지웅 — 오늘 오전 10:02
https://www.youtube.com/watch?v=lelVripbt2M&t=750s
YouTube
코딩알려주는누나
깃, 깃허브 한번에 이해시켜드리고 포트폴리오 올리는 법까지 알려드림.  15분안에 당신은 Github 전문가가 됩니다
이미지
﻿
###  🚀Clean_Curly 프로젝트 1st 🚀
- 마켓컬리 백엔드 클론코딩 프로젝트.
- 이커머스 사이트의 필수 기능을 구현
- 1차 프로젝트 결과임으로 아직 완벽하게 완성된 버전은 아님


### 🚴개발 인원 및 기간
- [팀프로젝트 기간] 2024-09.02(월) ~ 2024-09.13(금)
- [개발인원] : 백엔드 4명

### 🛠️기술스택
- Language : `python3`
- Framework : `Django`

### 💡ERD(1st)
![image](https://github.com/user-attachments/assets/2bcc12f3-f569-4b35-812c-f2b53c66e4c5)


### 🤗 팀 멤버
- [신덕근](https://github.com/shindeokgeun)
- [김향은](https://github.com/myangeun)
- [김혜지](https://github.com/hjkim977)
- [김지웅](https://github.com/kgw08003)

### 홈페이지 데모
![클린컬리](https://github.com/user-attachments/assets/bd02c593-fa10-48bb-979d-a24f744183ea)


### 📃 구현 기능📃 

#### 김혜지
- [`ERD` 내 `ORDERS` `CARTS` 기능 담당]
- 장바구니 기능 (추가, 수정, 삭제)
- 물건구매
- ![image](https://github.com/user-attachments/assets/ed41cf67-889d-4b0b-b627-c8200ace2cbb)
- ![image](https://github.com/user-attachments/assets/195cc85e-a542-455c-b352-1e509268a252)
- ![image](https://github.com/user-attachments/assets/56935614-85f0-406c-926a-65464457e190)

#### 신덕근
- [`ERD` 내 `REVIEWS` 기능 담당]
- 상품 리뷰 작성, 수정, 삭제
- ![image](https://github.com/user-attachments/assets/90e46f61-5d60-4405-9fe5-f480564151e0)
- ![image](https://github.com/user-attachments/assets/f50d81d4-2887-4e5a-99f7-c34af2871507)


#### 김지웅
- [`ERD` 내 `USER` 기능 담당]
- 회원가입 및 유저 관련 내용 로그인 페이지
- 로그인, 회원가입
![image](https://github.com/user-attachments/assets/0e599038-ebb7-4f53-a9cf-77babee87063)
![image](https://github.com/user-attachments/assets/5c82ea31-0d02-46f7-ac5b-cee173fb1056)

- 비밀번호 재확인 페이지, 개인정보 페이지(`users` 내 비밀번호 재확인 페이지, 개인정보 페이지(유저정보 관련 내용)
![image](https://github.com/user-attachments/assets/f87e64ca-d6d7-4f37-a2b6-4a0e363e3de8)
![image](https://github.com/user-attachments/assets/3216e47e-51e1-437a-9877-36062881d80e)


#### 김향은
- [`ERD` 내 `PRODUCTS` 기능 담당]
- 판매할 물건 등록, 삭제, 수정
- ![image](https://github.com/user-attachments/assets/118953dc-762e-4785-ad8e-a1030b02dd01)




### 🔐 코드 작성하면서 어려웠던 기능🔐
### [김혜지]
###### 장바구니에 있는 상품을 주문으로 생성
- 문제점: 리뷰 기능과 합해지면서 오류가 발생: 리뷰에서는 로그인이 된 사용자, 물건을 구매한 사용자만이 리뷰를 작성할 수 있도록 구현하였으나 이점을 고려하지 않고 orders 기능을 구현하여 오류가 발생
- 해결 방법: 현재 요청을 보낸 사용자가 로그인이 된 상태인지 확인하기 위해 `order_create` 함수에 사용자 정보를 설정하는 `order.user = request.user` 코드를 추가

###  📝구현하려 했으나 해결하지 못한 기능📝
###### <담기> 버튼 기능
- 자바스크립트를 이용하면 쉽게 구현 가능한 기능
- 현재 상황:<담기> 버튼을 누르면 상품 상세페이지로 이동

### 🔥2차 프로젝트에서 구현하고 싶은 기능🔥
- 구매 이력 조회
- 메인 페이지에서 <담기> 버튼을 누르면 장바구니에 해당 상품이 담기게 하기
- <주문요청하기> 버튼을 누르면 배송상태가 `delivered`로 변경
- 찜하기 기능 추가

---------
### 🔐 코드 작성하면서 어려웠던 기능🔐
### [신덕근]
###### 리뷰 작성 가능한 상품 필터링
- 문제점: 주문, 상품, 다른 종류의 여러 데이터들을 한꺼번에 연결, 사용자가 주문한 상품, 배송상태, 리뷰 상태를 동시에 연결, 이미 리뷰를 작성한 상품은 제외하는 로직을 구현
- 해결 방법: Django orm 의 쿼리 사용 : 지정된 필드의 값만 가져오는 values_list 와 제외 기능인 exclude를 활용하여 데이터를 추출

###  📝구현하려 했으나 해결하지 못한 기능📝
###### 주문 시스템과의 미연동
- 현재 주문 시스템과의 자동 연동 기능이 구현되지 않아 admin에서 직접 주문상태를 delivered 로 설정해야 리뷰 작성 가능
###### 마이 페이지 -> 구매평
- 마이페이지 구매평 부분에 html, css문제로 클릭을 해야만 구매평(리뷰 관련 내용)이 표시됨

### 🔥2차 프로젝트에서 구현하고 싶은 기능🔥
- 주문 시스템과의 연동
- 리뷰 정렬 방식 개선(좋아요 기능 추가)
- 평균 별점 표시
- 마이페이지에서 리뷰 내용이 바로 보이도록 html과 css파일 재정리
- 신고기능
- 리뷰의 통계를 세분화하여 시각화(리뷰 작성률, 구매자 정보 통계 등을 이용)

--------
### 🔐 코드 작성하면서 어려웠던 기능🔐
### [김지웅]
###### 리뷰 작성 가능한 상품 필터링
- 문제점: 마이페이지를 들어가기 전, 비밀번호를 재확인하는 폼에서 아이디 입력란을 잠그고 싶었으나 에러가 발생
- 해결 방법:`readonly` 속성을 사용하여 입력 필드를 수정할 수 없게 만들었음. `readonly` 속성은 HTML의 `<input>` 요소에서 사용자가 값을 수정하지 못하도록 설정하는 속성으로, 보안과 사용자 편의성을 동시에 달성할 수 있었음.

###  📝구현하려 했으나 해결하지 못한 기능📝
###### 선물특가 타이머 기능
- 타이머 기능을 구현할 때, 한 번 설정한 시간은 수정이 불가능하여 새로 고침을 하면 타이머가 초기화됨.
- 현재 상황 : 새로고침 할 때마다 시간이 초기화되는 방식으로 설정됨


### 🔥2차 프로젝트에서 구현하고 싶은 기능🔥
- 개인 페이지에서 회원 정보 및 비밀번호 수정
- 추천인 코드 및 마일리지 기능
- 홈페이지 검색어 입력 기능 연동
- 선물특가 타이머 기능

----------
### 🔐 코드 작성하면서 어려웠던 기능🔐
### [김향은]
###### 리뷰 작성 가능한 상품 필터링
- 문제점: Category필드를 Product 모델에 추가하면서 기존에 등록된 Product 데이터와의 호환성 문제를 겪음, Produce 모델에 새로운 Catefory필드를 추가했지만, 기존에 저장된 제품 데이터에는 연결된 Category 객체가 없어 외래키 제약 조건을 위반하는 문제 발생
- 해결 방법: 기존 제품 데이터에 대해 기본 Category를 설정하고 새로운 Category 객체와 기존 데이터를 연결하는 마이그레이션 작업 수행

###  📝구현하려 했으나 해결하지 못한 기능📝
###### 구매 이력 조회 기능
- 기본적인 데이터 모델과 프로젝트 연결은 완료했으나 해당 데이터를 표시하는 방식에 여러 이슈가 발생
- 각 구매자의 주문 내역을 효율적으로 필터링하는 부분에서 문제 발생

### 🔥2차 프로젝트에서 구현하고 싶은 기능🔥
- 구매 이력 조회
- 날짜별 주문 내역 필터링
- 주문상태(배송중, 배송완료 등)에 따라 정렬
- 상품의 상세 페이지에서 좋아요 기능

------------

### 실행 방법 ⚙️
##### 패키지 설치
```  images파일 추가
python -m venv myweb
만들어진 폴더에 zip 파일내용 붙여넣기
cd myweb
./Scripts/activate
pip install django djangorestframework
pip install django_extensions pillow
또는 pip install -r requirements.txt 이용
python manage.py runserver
```
message.txt
8KB
