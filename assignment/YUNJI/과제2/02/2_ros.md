# ROS2 Humble 설치 및 `ros2 run` 실습

---

##  1. 로봇 운영체제의 개념

일반적인 운영체제는 CPU, 메모리, 저장장치, 네트워크 및 주변 장치를 관리하고 응용 프로그램이 실행될 수 있는 환경을 제공한다. 로봇도 센서, 카메라, 모터, 제어기와 같은 여러 장치를 함께 사용하므로 장치 관리와 프로그램 간 통신을 지원하는 소프트웨어 환경이 필요하다.

ROS는 이름에 운영체제라는 표현이 들어가지만 Ubuntu나 Windows처럼 하드웨어를 직접 관리하는 운영체제 커널은 아니다. Ubuntu와 같은 운영체제 위에서 실행되며 로봇 프로그램 개발에 필요한 통신, 장치 연동, 실행 관리, 시각화, 디버깅 기능을 제공하는 소프트웨어 프레임워크이자 미들웨어에 가깝다.

ROS2는 다음과 같은 기능을 제공한다.

- 센서와 모터 드라이버 재사용
- 프로그램 간 Topic, Service, Action 통신
- 로봇 기능의 모듈화
- 분산 시스템 구성
- 데이터 기록과 재생
- RViz 등의 시각화 도구
- 실행 중인 노드와 통신 상태 확인

---

## 2. 운영체제를 사용하는 로봇과 사용하지 않는 로봇의 차이

여기서 운영체제를 사용하지 않는 로봇은 일반적인 Linux나 Windows를 사용하지 않고, 마이크로컨트롤러에서 펌웨어를 직접 실행하는 형태를 의미한다.

| 구분 | 운영체제를 활용하는 로봇 | 일반 운영체제를 사용하지 않는 로봇 |
|---|---|---|
| 실행 환경 | Ubuntu, Linux, RTOS 등 | 마이크로컨트롤러에서 펌웨어 직접 실행 |
| 프로그램 구성 | 기능을 여러 프로세스나 노드로 분리 가능 | 하나의 프로그램에 기능이 통합되는 경우가 많음 |
| 장치 관리 | 운영체제의 드라이버와 자원 관리 기능 활용 | 프로그램에서 하드웨어를 직접 제어 |
| 통신 | 프로세스 및 네트워크 통신 구성이 쉬움 | 통신 규칙을 직접 구현해야 함 |
| 개발 편의성 | 라이브러리, 디버깅, 시각화 도구 사용 가능 | 구조는 단순하지만 개발 도구가 제한적일 수 있음 |
| 자원 사용량 | 비교적 많은 CPU, 메모리, 저장공간 필요 | 적은 자원으로 동작 가능 |
| 적합한 예 | 자율주행 로봇, 서비스 로봇, 다중 센서 로봇 | 라인트레이서, 단순 반복 제어 장치 |

복잡한 로봇은 영상 처리, 지도 작성, 경로 계획, 센서 처리, 모터 제어 등을 동시에 수행해야 하므로 운영체제와 ROS2를 활용하는 것이 유리하다. 반대로 단순한 센서 입력과 모터 제어만 필요한 장치는 마이크로컨트롤러 프로그램만으로 구현하는 편이 효율적일 수 있다.

---

## 3. 실습 환경

```text
운영체제: Ubuntu 22.04.x LTS (Jammy Jellyfish)
셸: Bash
ROS2 배포판: Humble Hawksbill
```

현재 Ubuntu 버전은 다음 명령어로 확인한다.

```bash
lsb_release -a
```

또는 다음 명령어를 사용할 수 있다.

```bash
cat /etc/os-release
```

출력에 다음 내용이 포함되어 있어야 한다.

```text
VERSION_ID="22.04"
VERSION_CODENAME=jammy
```

ROS2 Humble의 Ubuntu용 deb 패키지는 Ubuntu 22.04 Jammy 환경을 대상으로 한다.

---

## 4. ROS2 Humble 설치

### 4.1UTF-8 로케일 확인

```bash
locale
```

출력에 UTF-8이 없다면 다음 명령어를 실행한다.

```bash
sudo apt update
sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
locale
```

### 4.2 Universe 저장소 활성화

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

### 4.3 ROS2 APT 저장소 등록

```bash
sudo apt update
sudo apt install curl -y
```

ROS2 APT 저장소 설정 패키지의 최신 버전을 확인한다.

```bash
export ROS_APT_SOURCE_VERSION=$(curl -s \
https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest \
| grep -F "tag_name" | awk -F'"' '{print $4}')
```

값을 확인한다.

```bash
echo $ROS_APT_SOURCE_VERSION
```

패키지를 내려받고 설치한다.

```bash
curl -L -o /tmp/ros2-apt-source.deb \
"https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"

sudo dpkg -i /tmp/ros2-apt-source.deb
```

### 4.4 시스템 업데이트와 ROS2 설치

```bash
sudo apt update
sudo apt upgrade
sudo apt install ros-humble-desktop
sudo apt install ros-dev-tools
```

`ros-humble-desktop`에는 ROS2 기본 도구, RViz, 데모와 튜토리얼이 포함되어 있어 이번 실습에 적합하다.

---

## 5. ROS2 환경 설정

ROS2를 설치한 뒤 각 터미널에서 다음 명령어를 실행해야 한다.

```bash
source /opt/ros/humble/setup.bash
```

`source` 명령은 ROS2 실행 파일과 패키지 경로를 현재 Bash 환경에 등록한다.

환경 설정 결과를 확인한다.

```bash
echo $ROS_DISTRO
```

정상적으로 설정되면 다음과 같이 출력된다.

```text
humble
```

ROS2 명령어도 확인한다.

```bash
ros2 --help
```

새 터미널마다 자동으로 환경 설정을 적용하려면 다음 명령어를 한 번만 실행한다.

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

추가 여부는 다음과 같이 확인한다.

```bash
tail -n 5 ~/.bashrc
```

---

## 6. `ros2 run` 명령어

`ros2 run`은 특정 패키지가 제공하는 실행 프로그램을 실행하는 명령어이다.

```bash
ros2 run <패키지 이름> <실행 프로그램 이름>
```

예시는 다음과 같다.

```bash
ros2 run demo_nodes_cpp talker
```

도움말은 다음 명령어로 확인한다.

```bash
ros2 run --help
```

`demo_nodes_cpp` 패키지에서 실행할 수 있는 프로그램은 다음과 같이 확인한다.

```bash
ros2 pkg executables demo_nodes_cpp
```

목록에서 다음 항목을 찾을 수 있다.

```text
demo_nodes_cpp talker
demo_nodes_cpp listener
```

ROS 전용 인자는 `--ros-args` 뒤에 작성할 수 있다.

```bash
ros2 run demo_nodes_cpp talker --ros-args -r __node:=my_talker
```

---

## 7. Talker와 Listener의 통신 구조

Talker와 Listener는 Topic 통신을 확인하기 위한 기본 데모이다.

- Talker: `/chatter` Topic에 문자열을 발행하는 Publisher
- Listener: `/chatter` Topic을 구독하는 Subscriber

```text
/talker 노드
    │
    │ std_msgs/msg/String 메시지 발행
    ▼
/chatter Topic
    │
    │ 메시지 구독
    ▼
/listener 노드
```

---

## 8. Talker와 Listener 실행

### 8.1 첫 번째 터미널: Talker

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```

정상 실행 시 다음과 비슷한 내용이 반복 출력된다.

```text
[INFO] [시간] [talker]: Publishing: 'Hello World: 1'
[INFO] [시간] [talker]: Publishing: 'Hello World: 2'
```

### 8.2 두 번째 터미널: Listener

Talker를 종료하지 않은 상태에서 두 번째 터미널을 연다.

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp listener
```

정상 통신 시 다음과 비슷한 내용이 반복 출력된다.

```text
[INFO] [시간] [listener]: I heard: [Hello World: 1]
[INFO] [시간] [listener]: I heard: [Hello World: 2]
```

Talker의 메시지 번호와 Listener가 수신한 메시지 번호가 계속 증가하면 두 노드가 동시에 실행되고 있는 것이다.

프로그램은 각 터미널에서 `Ctrl + C`로 종료한다.

