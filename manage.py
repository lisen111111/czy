#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj2.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# 读者： http://localhost:8080/zxjyts/front/index.html
# 管理员： http://127.0.0.1:8080/admin

# 若是mysql8需要将CURRENT_TIMESTAMP设置为OFF，mysql5不需要操作。
# SHOW GLOBAL VARIABLES LIKE "explicit_defaults_for_timestamp";
# SET persist explicit_defaults_for_timestamp=OFF;

