import shutil, sys, os, re

# export the html documentation in this directory and call this script

def get_all_files():
    expr = re.compile(r'"elementHeader2">([a-zA-z0-9/_]+)</.*?<img src="([a-zA-Z0-9_\./]+)"', flags=re.DOTALL)
    return expr.findall(htmlFile)

def copy_file(target_path, element_name, image_file):
    target_name = os.path.join(target_path, element_name.replace('/','_')+'_Schema.png')
    shutil.copy2(image_file, target_name)

def copy_all_files(target_path):
    all_files = get_all_files()
    for element_name, image_file in all_files:
        copy_file(target_path, element_name, image_file)

def getFilename(name):
    what = '"elementHeader2">' + name + '<'
    start = htmlFile.find(what)
    if start < 0:
        raise RuntimeError("key not found!")
    start2 = htmlFile.find('<img src="', start + 1)
    start3 = htmlFile.find('"', start2 + 11)
    print(htmlFile[start2+10:start3] + ' -> ' + what[17:-1].replace('/','_')+'_Schema.png')
    return (htmlFile[start2+10:start3], os.path.join(targetPath, what[17:-1].replace('/','_')+'_Schema.png'))



if __name__ == "__main__":
    htmlFile = open('fmi3ModelDescription.html').read()
    if len(sys.argv) > 1:
        targetPath = sys.argv[1] + '\\'
    else:
        raise RuntimeError("Please provide a target path as argument")
    copy_all_files(targetPath)