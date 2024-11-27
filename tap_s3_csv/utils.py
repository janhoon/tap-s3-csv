import gzip
import zipfile
import io

def read_gzip_s3(body):
    """
    Read a gzip file from S3
    :param body: file body
    :return: generator containing the lines of the file
    """
    return gzip.open(body, mode="rb")

def read_zip_s3(body):
    """
    Read a zip file from S3
    :param body: file body
    :return: file-like object in binary mode
    """
    
    # Create a BytesIO object from the S3 body
    zip_data = io.BytesIO(body.read())
    
    # Keep references to prevent garbage collection
    zip_ref = zipfile.ZipFile(zip_data)
    first_file = zip_ref.namelist()[0]

    # Return the raw bytes without text decoding
    return zip_ref.open(first_file)
