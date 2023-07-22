import os
import sys

print(sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

__all__ = ["test_message_defs", "test_plugin_manager", "test_logger.py"]