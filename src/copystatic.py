import os,shutil

def remove_dir(path):
    #to_delete_file= os.listdir(path="/home/ben/workspace/site__generator_boot_dev/public")
    #print(to_delete_file)
    try:
        shutil.rmtree(path)
    except:
        FileNotFoundError("Folder does not exist")
    os.mkdir(path)
def copy_dir(src,dest):

    os.makedirs(dest, exist_ok=True)

    for item in os.listdir(src):
         src_path= os.path.join(src, item)
         dest_path= os.path.join(dest, item)
         if os.path.isfile(src_path):
                  print(f"Copying file: {src_path} -> {dest_path}")
                  shutil.copy2(src_path, dest_path)
         elif os.path.isdir(src_path):
             print(f"making dir: {dest}/{item}")
             print(f"Creating directory: {dest_path}")
             copy_dir(src_path, dest_path)
                        
