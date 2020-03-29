# anorak_webpage

## local server에서 django project run 하기 (bash 기준)
git clone 후 anorak_webpage 폴더로 이동  
$ cd anorak_webpage

가상환경 활성화  
$ pipenv shell

Pillow 설치 (데이터베이스 이용 시 필요)  
$ pip install Pillow

Django local server 실행  
$ python manage.py runserver
