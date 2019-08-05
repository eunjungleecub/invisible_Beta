from django.urls import path, include

from . import views

urlpatterns = [
    path('about/', views.about, name="about"), #about(소개) 페이지
    path('search/', views.search, name="search"), #검색 페이지
    path('signup/', views.signup, name="signup"), #회원가입 페이지
    path('login/', views.login, name="login"), #로그인 페이지
    path('findpw/', views.findpw, name="findpw"), #비밀번호찾기 페이지
    path('changepw/', views.changepw, name="changepw"), #비밀번호 재설정 페이지
    path('auth_number/', views.auth_number, name="auth_number"), #인증번호 입력 페이지
    path('logout/', views.logout, name='logout'),
    path('likedlecture/',views.likedlecture, name='likedlecture'), #좋아요한 강의 페이지
    path('selectkeyword/',views.selectkeyword, name='selectkeyword'), #선호하는 키워드 페이지
    path('mytype/',views.mytype, name='mytype'), #나의 강의타입 페이지
    path('accounts/', include('allauth.urls')), #소셜로그인
]


    
    
   