import os 
from datetime import datetime,timedelta

def main():
    string=input("Enter file directories path: ")
    directories = [string]
    # directories = [r"C:\Users\hp\Downloads\ilovepdf_pages-to-jpg"]
    days=int(input("Enter days: "))
    stale_files = scan_directories(directories, days)
    if len(stale_files)==0:
        print("NO stale files found")
        return
    else:
        report = generate_report(stale_files)
        print_report(report)

def get_file_info(filepath):
    file_detail=os.stat(filepath)

    return {
        "path":filepath,
        "name":os.path.basename(filepath),
        "size":file_detail.st_size,
        "type":os.path.splitext(filepath)[1],
        "last_modified":datetime.fromtimestamp(file_detail.st_mtime)
    }

def is_stale(file_time, days):
    cutoff = datetime.now() - timedelta(days=days)
    if file_time < cutoff:
        return True
    else:
        return False

def scan_directories(directories, days):
    stale_files=[]
    for directory in directories:
        for root,dirs,files in os.walk(directory):
            for file in files:
                filepath=os.path.join(root,file)
                try:
                    info=get_file_info(filepath)
                    if is_stale(info["last_modified"], days):
                        stale_files.append(info)
                except Exception as e:
                    print(f"Error in {filepath}: {e}")
    return stale_files

def generate_report(stale_files):
    total_files = len(stale_files)
    total_size = sum(file["size"] for file in stale_files)

    return {
        "files": stale_files,
        "total_files": total_files,
        "total_size": total_size
    }

def print_report(report):
    for file in report["files"]:
        print(
            f"{file['name']} | "
            f"{file['type']} | "
            f"{file['size']} bytes | "
            f"{file['last_modified']}"
        )

    print("\nSummary:")
    print("Total stale files:", report["total_files"])
    print("Total stale files size :", report["total_size"], "bytes")


if __name__ == "__main__":
    main()