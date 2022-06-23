import os
from pyodm import Node
import time
from datetime import datetime
import subprocess

ODM_HOST = '127.1'
ODM_PORT = 3000

PHOTOS_DIR = '/home/...'
RESULT_DIR = '/home/...'


def run_odm(photos_dir, result_dir):
    print('started')
    node = Node(ODM_HOST, ODM_PORT)
    photos = [os.path.join(photos_dir, x) for x in os.listdir(photos_dir)]

    params = {"dsm": True,
              "force-gps": True,
              "gps-accuracy": 0.5,
              "orthophoto-resolution": 4,
              #'dem-gapfill-steps': 3,
              #'mesh-size': 800000,
              #'mesh-octree-depth': 12,
              "feature-quality": 'high',
              #'pc-quality': 'high',
              "min-num-features": 80000,
              "skip-report": False,
              "skip-3dmodel": False,
              #'ignore-gsd': False,
              #'use-3dmesh': False,
              'pc-csv': True,
              #'pc-rectify': True,
              #'pc-geometric': False,  # ! try to enable
              'verbose': True,
              'time': True}

    odm_task = node.create_task(photos, params)
    task_info = odm_task.info()
    
    print('task_info = ', task_info)
    odm_task.wait_for_completion()
    
    print(odm_task.output())
    odm_task.download_assets(result_dir)

    print(odm_task.output())


run_odm(PHOTOS_DIR, RESULT_DIR)

subprocess.run(['ffplay', '/home/anon/notification.mp3'])
