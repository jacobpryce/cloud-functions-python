from PyInstaller.utils.hooks import copy_metadata

datas = copy_metadata('google-cloud-vision')
datas += copy_metadata('google-cloud-core')
