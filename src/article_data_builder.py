import pandas as pd
import shutil
from pathlib import Path
import errno
import os


class BioStudies_builder():

    def __init__(
            self,
            raw_images_folder: str = '',
            bacmman_folder: str = '',
            target_path: str = '',
            dry_run: bool = False):

        self.raw_images_folder = Path(raw_images_folder)
        self.bacmman_folder = Path(bacmman_folder)
        self.target_path = Path(target_path)
        self.dry_run = dry_run

        
    def build(self):
        df_list = pd.read_csv('../Dataset_list.csv')

        i=0
        for name in df_list.Name:
            i += 1
            print(f'Processing dataset {i}/{len(df_list.Name)}')
            
            ds, exp = name.split('_')

            self.copy_bacmman_dataset(name)
            self.copy_raw_images(ds, exp)

        if self.dry_run:
            print('Dry run completed - no files copied')
            print('All folders were successfully found')
        else:
            print(f'Copying to {self.target_path} finished')

            
    def copy_bacmman_dataset(self, name: str) -> None:
        src = self.bacmman_folder / 'Timelapse' / name
        dst = self.target_path / 'Bacmman' / name

        if self.dry_run:
            if not src.exists():
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), src)
        else:
            shutil.copytree(src, dst)
                

    def copy_raw_images(self, ds:str , exp: str) -> None:
        src = self.raw_images_folder / ds / exp
        dst = self.target_path / 'raw_images' / ds / exp

        if self.dry_run:
            if not src.exists():
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), src)
        else:
            shutil.copytree(src, dst)


if __name__ == '__main__':

    builder = BioStudies_builder(
        raw_images_folder='/media/elkaroui/Daniel Thédié/Omero_backup_2026-03-31/dthedie',
        bacmman_folder='../../daniels-bacmman-folder',
        target_path='',
        dry_run=True
    )
    
    builder.build()
