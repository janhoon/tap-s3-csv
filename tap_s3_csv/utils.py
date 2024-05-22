import gzip


def read_gzip_s3(body):
    """
    Read a gzip file from S3
    :param body: file body
    :return: generator containing the lines of the file
    """
    return gzip.open(body, mode="rb")
