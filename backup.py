import os
import datetime
import subprocess
import oci

# Load config from default location (~/.oci/config)
config = oci.config.from_file()

# Oracle Object Storage client
object_storage = oci.object_storage.ObjectStorageClient(config)
namespace = object_storage.get_namespace().data
bucket_name = "pos-backup"   # make sure you create this bucket in Oracle Cloud Console

# Step 1: Run pg_dump to export DB
backup_name = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
backup_file = os.path.join(os.getcwd(), backup_name)

cmd = f'pg_dump -U postgres -d week8db > "{backup_file}"'
os.system(cmd)

# Step 2: Upload to Oracle Object Storage
with open(backup_file, "rb") as f:
    object_storage.put_object(namespace, bucket_name, backup_name, f)

print(f"✅ Backup {backup_name} uploaded successfully to Oracle Object Storage bucket {bucket_name}")
