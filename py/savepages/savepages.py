from pywebcopy import save_webpage

url = 'https://en.wikipedia.org/wiki/NBA_Jam_(1993_video_game)'
download_folder = 'D://testep/'

kwargs = {'bypass_robots': True, 'project_name': 'save_pages'}

#config.setup_config(url, download_folder, project_name, **kwargs)

save_webpage(url, download_folder, **kwargs)


