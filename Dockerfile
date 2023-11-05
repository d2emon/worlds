FROM cdrx/pyinstaller-linux:python3

COPY * /src/

RUN ["/entrypoint.sh", "pyinstaller --onefile hello.py"]
