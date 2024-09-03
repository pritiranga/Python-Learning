# Script to take backup
import shutil
import datetime
import os

def backup_files(source, destination):
    today=datetime.date.today()
    backup_file_name= os.path.join(destination, f"backup_{today}")  # if need any variable in string then use f"_"
    shutil.make_archive(backup_file_name,'gztar', source)  # make_archive used to compress file

source="C:\\Users\\Priti Ranga\\Documents\\Python Workshop\\take_its_backup"
destination=r"C:\\Users\\Priti Ranga\\Documents\\Python Workshop\\backups"
backup_files(source, destination)