#!/usr/bin/env python3
"""
A module for filtering logs.
"""
import logging
import os
import mysql.connector
import re
import bcrypt

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        formats a LogRecord.
        """
        def filter_datum(match):
            return self.REDACTION

        record.msg = re.sub(
            rf'({"|".join(self.fields)})=([^{self.SEPARATOR}]*)',
            filter_datum,
            record.msg
        )
        return super().format(record)


def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    """
    Filters a log line.
    """
    return re.sub(rf'({"|".join(fields)})=([^{separator}]*{separator})', f'{redaction}{separator}', message)


def get_logger() -> logging.Logger:
    """
    Creates a new logger for user data
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Creates a connector to a database.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    dbname = os.getenv("PERSONAL_DATA_DB_NAME")

    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=dbname
    )
    return connection


def main() -> None:
    """
    Logs the information about user records in a table.
    """
    logger = get_logger()
    db = get_db()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")

    logger.info("Filtered data:")
    for row in cursor.fetchall():
        logger.info("; ".join(f"{field}={value}" for field, value in zip(cursor.column_names, row)))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
