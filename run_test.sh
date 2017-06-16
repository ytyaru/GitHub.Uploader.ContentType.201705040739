#PYTHONPATH=./:./contenttype:./contenttype/tree:$PYTHONPATH
#PYTHONPATH=/tmp/GitHub.Uploader.ContentType.201705040739/contenttype:/tmp/GitHub.Uploader.ContentType.201705040739/contenttype/tree:$PYTHONPATH
python3 -m unittest TestResponse_TDD.py
python3 -m unittest TestResponse_BlackBox.py
python3 -m unittest TestPaginator.py
