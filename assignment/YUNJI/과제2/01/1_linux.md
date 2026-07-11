# Ubuntu Linux 기본 사용법 및 파이썬 프로그램 실행 실습

## 1. 학습 목적

ROS2는 명령어 실행, 워크스페이스 관리, 패키지 설치, 환경 설정 등의 작업을 터미널에서 자주 수행한다. 따라서 ROS2를 학습하기 전에 우분투 리눅스의 기본적인 터미널 사용법과 파일 시스템, 권한, 패키지 관리 방법을 이해할 필요가 있다.

본 문서에서는 리눅스의 기본 사용법을 정리하고, Chrome과 Visual Studio Code를 설치한 뒤 파이썬 프로그램을 작성하여 실행하는 과정을 다룬다.

---

## 2. 셸 환경과 터미널 실행

### 2.1 셸의 개념

셸(Shell)은 사용자가 입력한 명령어를 해석하여 운영체제에 전달하는 프로그램이다. 우분투에서는 일반적으로 Bash 셸이 사용된다.

현재 사용 중인 셸은 다음 명령어로 확인할 수 있다.

```bash
echo $SHELL
```

출력 예시는 다음과 같다.

```text
/bin/bash
```

### 2.2 터미널 실행 방법

우분투 데스크톱 환경에서는 다음 방법으로 터미널을 실행할 수 있다.

- 단축키 `Ctrl + Alt + T` 사용
- 애플리케이션 목록에서 `Terminal` 검색
- 파일 탐색기의 특정 디렉토리에서 마우스 오른쪽 버튼을 눌러 터미널 열기

터미널이 실행되면 일반적으로 다음과 같은 프롬프트가 표시된다.

```text
사용자명@컴퓨터명:현재경로$
```

`$`는 일반 사용자로 실행 중임을 의미하고, `#`는 슈퍼유저(root) 셸임을 나타내는 경우가 많다.

---

## 3. 파일과 디렉토리 관리 명령어

리눅스에서는 파일과 디렉토리를 경로를 기준으로 관리한다.

| 명령어 | 기능 | 사용 예시 |
|---|---|---|
| `pwd` | 현재 디렉토리의 절대 경로 확인 | `pwd` |
| `ls` | 디렉토리 내용 확인 | `ls -al` |
| `cd` | 디렉토리 이동 | `cd ~/study` |
| `mkdir` | 디렉토리 생성 | `mkdir -p ~/study/linux` |
| `touch` | 빈 파일 생성 또는 수정 시간 갱신 | `touch test.txt` |
| `cp` | 파일 또는 디렉토리 복사 | `cp file.txt backup.txt` |
| `mv` | 파일 이동 또는 이름 변경 | `mv old.txt new.txt` |
| `rm` | 파일 삭제 | `rm test.txt` |
| `rm -r` | 디렉토리와 내부 항목 삭제 | `rm -r test_dir` |
| `find` | 조건에 맞는 파일 검색 | `find ~/study -name "*.py"` |

### 3.1 절대 경로와 상대 경로

- 절대 경로: 루트 디렉토리 `/`부터 시작하는 전체 경로  
  예: `/home/user/study/linux`
- 상대 경로: 현재 디렉토리를 기준으로 나타낸 경로  
  예: `./1_hello.py`
- `.`: 현재 디렉토리
- `..`: 상위 디렉토리
- `~`: 현재 사용자의 홈 디렉토리

### 3.2 실습 디렉토리 생성

```bash
mkdir -p ~/study/linux
cd ~/study/linux
pwd
```

`-p` 옵션을 사용하면 상위 디렉토리가 없는 경우 함께 생성하며, 이미 디렉토리가 존재해도 오류가 발생하지 않는다.

---

## 4. 파일 내용 확인 및 편집

### 4.1 파일 내용 확인 명령어

| 명령어 | 기능 |
|---|---|
| `cat 파일명` | 파일 전체 내용을 출력 |
| `less 파일명` | 긴 파일을 페이지 단위로 확인 |
| `head 파일명` | 파일 앞부분을 확인 |
| `tail 파일명` | 파일 뒷부분을 확인 |
| `tail -f 파일명` | 파일에 추가되는 내용을 실시간으로 확인 |

사용 예시는 다음과 같다.

```bash
cat /test/hello_linux.txt
head -n 5 example.txt
tail -n 5 example.txt
```

### 4.2 파일 편집 방법

터미널 기반 편집기로는 `nano`, `vim` 등이 있으며, 그래픽 환경에서는 Visual Studio Code를 사용할 수 있다.

```bash
nano test.txt
vim test.txt
code test.txt
```

초보자는 `nano` 또는 Visual Studio Code를 사용하면 비교적 쉽게 파일을 편집할 수 있다.

---

## 5. 파일 권한의 개념과 변경 방법

### 5.1 권한의 종류

리눅스 파일 권한은 다음 세 사용자 범주에 각각 적용된다.

- `u`(user): 파일 소유자
- `g`(group): 파일 소유 그룹
- `o`(others): 그 외 사용자

각 범주에는 다음 권한을 부여할 수 있다.

- `r`(read): 읽기 권한
- `w`(write): 쓰기 권한
- `x`(execute): 실행 권한

파일 권한은 다음 명령어로 확인한다.

```bash
ls -l
```

출력 예시는 다음과 같다.

```text
-rwxr-xr-- 1 user user 500 Jul 11 10:00 1_hello.py
```

첫 글자는 파일 종류를 나타내며, 이후 문자는 소유자·그룹·기타 사용자의 권한을 순서대로 나타낸다.

### 5.2 chmod 명령어

소유자에게 실행 권한을 추가하는 명령어는 다음과 같다.

```bash
chmod u+x 1_hello.py
```

숫자 방식도 사용할 수 있다.

```bash
chmod 755 1_hello.py
```

숫자 권한은 다음 값을 더하여 계산한다.

- 읽기 `r` = 4
- 쓰기 `w` = 2
- 실행 `x` = 1

따라서 `755`는 소유자에게 `rwx`, 그룹과 기타 사용자에게 `r-x` 권한을 부여한다.

권한을 지나치게 넓게 설정하는 `chmod 777`은 보안상 문제가 될 수 있으므로 필요한 범위에서만 권한을 부여해야 한다.

### 5.3 소유자 변경

파일이나 디렉토리의 소유자는 `chown`으로 변경할 수 있다.

```bash
sudo chown 사용자명:그룹명 대상경로
```

현재 로그인 사용자를 소유자로 지정할 때는 다음과 같이 작성할 수 있다.

```bash
sudo chown "$USER":"$USER" /test
```

---

## 6. 실행 파일, 셸 스크립트와 source 명령어

### 6.1 실행 파일

실행 파일은 운영체제가 직접 실행할 수 있는 파일이다. 셸 스크립트나 파이썬 파일을 직접 실행하려면 다음 조건이 필요하다.

1. 파일에 실행 권한이 있어야 한다.
2. 첫 줄에 어떤 인터프리터로 실행할지 나타내는 shebang이 있어야 한다.

파이썬 파일의 shebang 예시는 다음과 같다.

```python
#!/usr/bin/env python3
```

실행 권한을 부여한 뒤 다음과 같이 실행할 수 있다.

```bash
chmod u+x 1_hello.py
./1_hello.py
```

실행 권한 없이 인터프리터를 직접 지정하는 방법도 있다.

```bash
python3 1_hello.py
```

### 6.2 셸 스크립트

셸 스크립트는 여러 셸 명령어를 하나의 파일에 작성하여 순서대로 실행하는 파일이다.

```bash
#!/bin/bash

echo "Hello Shell"
pwd
```

파일 이름을 `example.sh`로 저장한 경우 다음과 같이 실행한다.

```bash
chmod u+x example.sh
./example.sh
```

### 6.3 source 명령어

일반적인 `./script.sh` 실행은 새로운 하위 셸에서 스크립트를 실행한다. 반면 `source`는 현재 셸에서 스크립트를 실행하므로 환경 변수나 셸 설정 변경 사항이 현재 터미널에 적용된다.

```bash
source script.sh
```

`.` 명령어도 같은 기능을 수행한다.

```bash
. script.sh
```

ROS2에서는 설치된 환경을 현재 터미널에 적용하기 위해 다음과 같이 사용한다.

```bash
source /opt/ros/humble/setup.bash
```

워크스페이스를 빌드한 후에는 다음과 같이 해당 워크스페이스 환경을 적용할 수 있다.

```bash
source ~/ros2_ws/install/setup.bash
```

새 터미널을 열 때마다 자동으로 적용하려면 `~/.bashrc`에 source 명령을 추가할 수 있다.

---

## 7. 사용자 권한, 슈퍼유저와 sudo

### 7.1 일반 사용자와 슈퍼유저

- 일반 사용자: 자신의 홈 디렉토리와 허용된 파일을 중심으로 작업한다.
- 슈퍼유저(root): 시스템 전체 파일과 설정에 접근할 수 있는 최고 권한 사용자이다.

현재 사용자 이름은 다음 명령어로 확인한다.

```bash
whoami
```

사용자 ID와 그룹 정보는 다음 명령어로 확인한다.

```bash
id
```

### 7.2 sudo 명령어

`sudo`는 허가된 일반 사용자가 특정 명령을 관리자 권한으로 실행할 때 사용한다.

```bash
sudo apt update
sudo mkdir /test
```

`sudo` 사용 시 현재 사용자의 비밀번호를 요구할 수 있다. 입력 중에는 화면에 문자나 별표가 표시되지 않지만 실제로는 입력되고 있다.

관리자 권한은 시스템 파일을 변경할 수 있으므로, 필요한 명령에만 제한적으로 사용해야 한다. 특히 출처를 확인하지 않은 명령을 `sudo`로 실행해서는 안 된다.

---

## 8. 우분투 패키지 관리와 apt 명령어

우분투는 APT(Advanced Package Tool)를 사용하여 패키지를 설치, 갱신, 삭제한다.

### 8.1 주요 apt 명령어

| 명령어 | 기능 |
|---|---|
| `sudo apt update` | 저장소의 최신 패키지 목록 갱신 |
| `sudo apt upgrade` | 설치된 패키지 업그레이드 |
| `sudo apt install 패키지명` | 패키지 설치 |
| `sudo apt remove 패키지명` | 패키지 삭제 |
| `sudo apt purge 패키지명` | 패키지와 설정 파일 삭제 |
| `apt search 검색어` | 패키지 검색 |
| `apt show 패키지명` | 패키지 정보 확인 |
| `sudo apt autoremove` | 더 이상 필요하지 않은 의존성 삭제 |

일반적인 시스템 갱신 순서는 다음과 같다.

```bash
sudo apt update
sudo apt upgrade
```

로컬에 내려받은 `.deb` 파일은 다음 형식으로 설치할 수 있다.

```bash
sudo apt install ./파일명.deb
```

`./`를 붙여 현재 디렉토리의 파일임을 명확하게 지정한다.

---

## 9. 홈 디렉토리의 개념

홈 디렉토리는 각 사용자의 개인 파일과 설정을 저장하는 기본 디렉토리이다.

일반 사용자의 홈 디렉토리는 보통 다음 형식이다.

```text
/home/사용자명
```

`~`는 현재 사용자의 홈 디렉토리를 의미한다.

```bash
cd ~
echo $HOME
```

홈 디렉토리에는 문서, 다운로드 파일, 프로젝트와 사용자 설정 파일이 저장된다. 이름이 `.`으로 시작하는 파일은 숨김 파일이며 다음 명령어로 확인할 수 있다.

```bash
ls -al ~
```

대표적인 사용자 설정 파일에는 `~/.bashrc`가 있다.

---

## 10. Chrome 웹 브라우저 설치

Google Chrome은 우분투용 64비트 `.deb` 패키지를 내려받아 설치할 수 있다.

### 10.1 설치 파일 내려받기

1. 우분투에 기본 설치된 Firefox를 실행한다.
2. Google Chrome 공식 다운로드 페이지로 이동한다.
3. `64 bit .deb (For Debian/Ubuntu)` 항목을 선택한다.
4. 설치 파일을 `다운로드(Downloads)` 디렉토리에 저장한다.

### 10.2 터미널에서 설치

```bash
cd ~/Downloads
sudo apt install ./google-chrome-stable_current_amd64.deb
```

설치 후 다음 명령어로 실행할 수 있다.

```bash
google-chrome
```

설치 여부는 다음과 같이 확인한다.

```bash
google-chrome --version
```

파일 이름이 다르게 저장된 경우 `ls` 명령어로 실제 파일 이름을 확인한 뒤 해당 이름을 사용한다.

---

## 11. Visual Studio Code 설치

Visual Studio Code 공식 사이트에서 Debian/Ubuntu용 `.deb` 패키지를 내려받는다.

### 11.1 설치 파일 내려받기

1. VS Code 공식 다운로드 페이지를 연다.
2. Linux용 `.deb` 패키지를 선택한다.
3. 파일을 `~/Downloads` 디렉토리에 저장한다.

### 11.2 터미널에서 설치

```bash
cd ~/Downloads
sudo apt install ./code_*.deb
```

설치 후 다음 명령어로 실행한다.

```bash
code
```

버전은 다음과 같이 확인한다.

```bash
code --version
```

VS Code의 `.deb` 패키지를 설치하면 업데이트에 사용할 Microsoft APT 저장소와 서명 키를 추가할지 묻는 화면이 나타날 수 있다.

---

## 12. 파이썬 프로그램 작성

### 12.1 Python 설치 확인

```bash
python3 --version
```

Python이 설치되어 있지 않은 경우 다음 명령어로 설치한다.

```bash
sudo apt update
sudo apt install python3
```

### 12.2 작업 디렉토리 생성

```bash
mkdir -p ~/study/linux
cd ~/study/linux
```

### 12.3 VS Code로 디렉토리 열기

```bash
code ~/study/linux
```

VS Code에서 `1_hello.py` 파일을 생성하고 다음 내용을 작성한다.

```python
#!/usr/bin/env python3
"""Create /test/hello_linux.txt containing 'Hello Linux'."""

from pathlib import Path
import sys


TARGET_DIR = Path("/test")
TARGET_FILE = TARGET_DIR / "hello_linux.txt"
MESSAGE = "Hello Linux\n"


def main() -> int:
    """Create the target directory and text file."""
    try:
        TARGET_DIR.mkdir(parents=True, exist_ok=True)
        TARGET_FILE.write_text(MESSAGE, encoding="utf-8")
    except PermissionError:
        print(
            "권한이 부족합니다. 문서의 권한 설정 방법을 수행한 후 다시 실행하세요.",
            file=sys.stderr,
        )
        return 1
    except OSError as error:
        print(f"파일 생성 중 오류가 발생했습니다: {error}", file=sys.stderr)
        return 1

    print(f"파일 생성 완료: {TARGET_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

이 프로그램은 다음 순서로 동작한다.

1. `/test` 디렉토리가 없으면 생성한다.
2. `/test/hello_linux.txt` 파일을 UTF-8 형식으로 생성한다.
3. 파일에 `Hello Linux` 문자열을 저장한다.
4. 정상 처리 여부를 터미널에 출력한다.
5. 권한 또는 운영체제 관련 오류가 발생하면 원인을 출력하고 비정상 종료 코드를 반환한다.

---

## 13. 프로그램 실행과 권한 문제 해결

### 13.1 권한 문제가 발생하는 이유

`/test`는 사용자의 홈 디렉토리가 아니라 루트 디렉토리 `/` 바로 아래에 위치한다. 일반 사용자는 기본적으로 루트 디렉토리 아래에 새 디렉토리를 생성하거나 파일을 작성할 권한이 없다.

따라서 일반 사용자로 바로 실행하면 다음과 같은 권한 오류가 발생할 수 있다.

```text
Permission denied
```

### 13.2 권장 방법: 디렉토리만 관리자 권한으로 준비

관리자 권한은 `/test` 디렉토리를 준비하는 단계에서만 사용하고, 파이썬 프로그램은 일반 사용자 권한으로 실행한다.

```bash
sudo mkdir -p /test
sudo chown "$USER":"$USER" /test
```

설정 결과를 확인한다.

```bash
ls -ld /test
```

현재 사용자가 소유자로 표시되면 파이썬 프로그램을 예외 없이 실행할 수 있다.

### 13.3 실행 권한 부여 및 실행

```bash
cd ~/study/linux
chmod u+x 1_hello.py
./1_hello.py
```

정상 실행 시 다음과 같은 결과가 출력된다.

```text
파일 생성 완료: /test/hello_linux.txt
```

인터프리터를 직접 지정하여 실행할 수도 있다.

```bash
python3 1_hello.py
```

### 13.4 대체 방법

디렉토리 소유권을 변경하지 않고 프로그램 전체를 관리자 권한으로 실행할 수도 있다.

```bash
sudo python3 1_hello.py
```

다만 일반적으로는 프로그램 전체를 관리자 권한으로 실행하기보다, 필요한 디렉토리만 적절한 권한으로 준비하는 방법이 권장된다.

---

## 14. 프로그램 실행 결과 확인

### 14.1 파일 존재 여부 확인

```bash
ls -l /test
```

또는 다음과 같이 파일의 상세 정보를 직접 확인한다.

```bash
ls -l /test/hello_linux.txt
```

### 14.2 파일 내용 확인

```bash
cat /test/hello_linux.txt
```

정상 결과는 다음과 같다.

```text
Hello Linux
```

### 14.3 파일 형식 확인

```bash
file /test/hello_linux.txt
```

### 14.4 종료 상태 확인

프로그램 실행 직후 다음 명령어를 입력한다.

```bash
echo $?
```

정상적으로 실행된 경우 다음과 같이 `0`이 출력된다.

```text
0
```

리눅스에서는 일반적으로 종료 코드 `0`을 성공, `0` 이외의 값을 오류로 해석한다.

---

## 15. 제출용 디렉토리 구성

프로젝트 루트에서 다음 명령어를 실행한다.

```bash
mkdir -p 2/1
```

작성한 파일을 지정된 위치로 복사한다.

```bash
cp ~/study/linux/1_hello.py 2/1/
cp 1_linux.md 2/1/
```

최종 디렉토리 구조는 다음과 같다.

```text
프로젝트루트/
└── 2/
    └── 1/
        ├── 1_linux.md
        └── 1_hello.py
```

파일이 정상적으로 배치되었는지 확인한다.

```bash
find 2/1 -maxdepth 1 -type f -print
```

Git 저장소에 게시하는 경우 다음과 같이 추가하고 커밋할 수 있다.

```bash
git add 2/1/1_linux.md 2/1/1_hello.py
git commit -m "Add Linux basic study and Python practice"
git push
```

