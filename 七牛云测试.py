from qiniu import Auth, put_file, etag

auth = Auth("", "")

auth.upload_token()