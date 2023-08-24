- 👋 Hi, Project Version { Python: 3.11.4, Selenium : 4.11.2, pyinstaller: 5.13.0} 
- ✍ 파이썬으로 응용프로그램을 만들어서 프로그램 실행 시 자동으로 출석체크, 체크인 하는 프로그램 코드 입니다.
  아이디, 비밀번호, 홈페이지 URL은 conf.ini 파일에 작성 후 아래의 코드로 exe파일 혹은 dir 구조로 빌드하시면 됩니다.
<br/>
<br/>
- OneFile로 배포 시 conf.ini을 같은 경로에 만들어주세요.

<h3> selenium & pyinstaller 설치 </h3>
<pre>
  pip install selenium pyinstaller 
</pre>
<br/>
<h3>OneFile</h3>
<pre>
pyinstaller --clean -w -F --icon=icon.ico --add-data="./conf.ini;." --hidden-import configparser AutoCheck.py
</pre>

<h3>Or</h3>

<h3>Folder </h3>
<pre>
pyinstaller --clean -w --icon=icon.ico --add-data="./conf.ini;." --hidden-import configparser AutoCheck.py
</pre>
