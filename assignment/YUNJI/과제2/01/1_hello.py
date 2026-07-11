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
